from dataclasses import dataclass

from .SpanningTreeOptions import SpanningTreeOptions
from ..enums.Algorithm_Over_Clustering import Algorithm_Over_Clustering
from ..enums.Algorithm_Spanning_Tree import Algorithm_Spanning_Tree

@dataclass
class MudpodOptions:
    pj: str = 'jl'
    obs: str = 'percentile'
    dist: str = 'mahalanobis'
    pv: float = 0.05
    sims: int = 20

@dataclass
class UniforceOptions:
    algorithm_over_clustering: Algorithm_Over_Clustering = Algorithm_Over_Clustering.GlobalKMeansPp
    algorithm_spanning_tree: Algorithm_Spanning_Tree = Algorithm_Spanning_Tree.Kruskal
    number_of_clusters: int = 50
    spanning_tree_options: SpanningTreeOptions = SpanningTreeOptions
    mudpod_options: MudpodOptions = MudpodOptions
