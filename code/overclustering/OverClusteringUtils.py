from numpy import ndarray
import numpy as np
from sklearn.cluster import KMeans

from data.enums.Algorithm_Over_Clustering import Algorithm_Over_Clustering
from data.results.OverClusteringResult import OverClusteringResult
from overclustering.GlobalKMeansPp import GlobalKmeansPp
from overclustering.common import get_view, get_monte_carlo_test
from data.options.UniforceOptions import MudpodOptions

def over_clustering(
        data: ndarray,
        algorithm: Algorithm_Over_Clustering,
        number_of_clusters: int
) -> OverClusteringResult:
    match algorithm:
        case Algorithm_Over_Clustering.GlobalKMeansPp:
            return _execute_global_kmeans_pp(data, number_of_clusters)
        case Algorithm_Over_Clustering.GlobalKMeansPpParallel:
            return _execute_global_kmeans_pp_parallel(data, number_of_clusters)
        case Algorithm_Over_Clustering.KmeansPp:
            return _execute_sklearn_kmeans(data, number_of_clusters)

def check_clusters_with_mudpod(
    data: ndarray,
    initial_result : OverClusteringResult,
    mudpod_options: MudpodOptions,
    min_size: int =25
) -> OverClusteringResult:

    mudpod_settings = {
       '<pj>': mudpod_options.pj,
        '--obs': mudpod_options.obs,
        '--dist': mudpod_options.dist,
        '<pv>': mudpod_options.pv,
        '<sims>': mudpod_options.sims
    }
    
    mct = get_monte_carlo_test(mudpod_settings, workers_num=1)
    
    labels = np.copy(initial_result.labels)
    unique_labels = list(np.unique(labels))
    next_new_label = max(unique_labels) + 1
    
    clusters_to_check = unique_labels.copy()
    while clusters_to_check:
    
        cluster_id = clusters_to_check.pop(0)
        cluster_indices = np.where(labels == cluster_id)[0]
        cluster_data = data[cluster_indices]
        
        # if size of cluster less than min_size, move to the next cluster
        if len(cluster_data) < min_size:
            continue
    
        
        if not mct.test(cluster_data):
            # break into 2 subclusters
            kmeans2 = KMeans(n_clusters = 2).fit(cluster_data)
            sub_labels = kmeans2.labels_
            
            index_0 = cluster_indices[sub_labels == 0]
            index_1 = cluster_indices[sub_labels == 1]
            
            # update labels
            labels[index_0] = cluster_id # one keeps the previous id
            labels[index_1] = next_new_label 
            
            # add the new ones to check them again
            clusters_to_check.append(cluster_id)
            clusters_to_check.append(next_new_label)
            
            next_new_label += 1
            
        
    final_unique_labels = np.unique(labels)
    remapped_labels = np.zeros_like(labels)
    final_centers = []
        
    for new_id, old_id in enumerate(final_unique_labels):
        remapped_labels[labels == old_id] = new_id
        final_centers.append(data[labels == old_id].mean(axis=0))
            
    
    return OverClusteringResult(labels = remapped_labels,
            cluster_centers = np.array(final_centers)
        )
    
def _execute_global_kmeans_pp(data: ndarray, number_of_clusters: int) -> OverClusteringResult:
    return GlobalKmeansPp(number_of_clusters=number_of_clusters, n_init=10).fit(data)


def _execute_global_kmeans_pp_parallel(data: ndarray, number_of_clusters: int) -> OverClusteringResult:
    return GlobalKmeansPp(number_of_clusters=number_of_clusters, n_init=10).fit_parallel(data)


def _execute_sklearn_kmeans(data: ndarray, number_of_clusters: int) -> OverClusteringResult:
    selected_model = KMeans(n_clusters=number_of_clusters, n_init=10).fit(data)
    return OverClusteringResult(labels=selected_model.labels_, cluster_centers=selected_model.cluster_centers_)
