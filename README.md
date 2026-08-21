# SMCUT: Split-Merge Clustering Algorithm

[![Thesis](https://img.shields.io/badge/Type-Diploma_Thesis-blue.svg)]()
[![Institution](https://img.shields.io/badge/Institution-University_of_Ioannina-red.svg)]()
[![Language](https://img.shields.io/badge/Language-Python-FFD43B?logo=python&logoColor=blue)]()
[![Environment](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?logo=jupyter&logoColor=white)]()

This repository presents the research and methodology developed in the diploma thesis titled "A Split-Merge Clustering Algorithm based on Unimodality Testing". The project introduces SMCUT, a novel clustering algorithm that significantly enhances the baseline UniForCE framework. By integrating the multivariate mud-pod statistical test directly after the initial overclustering phase, this algorithm mathematically guarantees the homogeneity of foundational subclusters.

## Author

**Giannis Fillis**  
Diploma Thesis, June 2026 
Department of Computer Science & Engineering, University of Ioannina

**Supervisor:** Professor Aristidis Likas

## Core Contributions

* **Statistical Validation:** Integrates the mud-pod test immediately after the global k-means++ partitioning phase to rigorously verify the internal unimodality of each initial subcluster.
* **Dynamic Refinement:** Utilizes Mahalanobis distances and linear random projections to actively detect and further partition multimodal subclusters, preventing structural flaws from propagating.
* **Hyperparameter Robustness:** Relaxes the strict dependency on the initial overclustering parameter K, dynamically correcting suboptimal user-defined settings during execution.

## Experimental Results

Extensive benchmarking against both synthetic and complex real-world datasets demonstrates the structural superiority of the SMCUT algorithm:
* The algorithm consistently achieves higher or comparable Adjusted Mutual Information (AMI) scores compared to the baseline.
* By dynamically reconstructing the feature space into truly unimodal blocks, it provides a highly accurate estimation of the final cluster count, k.
* SMCUT achieves its optimal clustering performance at a lower initial resolution of K=40, whereas the standard UniForCE framework requires a resolution of K=50.

## Reproducing the Experiments

The repository includes a Jupyter Notebook designed to easily recreate the experimental evaluations. 

1. **Data Preparation:** Ensure all required datasets are placed in the appropriate data directory as structured in the repository.
2. **Execution:** Navigate to the notebook directory and launch the environment by running:
   ```bash
   cd code/notebook
   jupyter notebook Diploma.ipynb
   ```

## Acknowledgements

This project builds upon the foundational work and open-source contributions of the following repositories:

* **UniForCE:** The baseline bottom-up clustering framework utilized and expanded upon in this thesis. Repository: [gvardakas/UniForCE](https://github.com/gvardakas/UniForCE)
* **mudpod:** The implementation of the multivariate unimodality test that was integrated into our methodology for subcluster validation. Repository: [prokolyvakis/mudpod](https://github.com/prokolyvakis/mudpod)
* **Clustering Benchmark:** The source of the synthetic 2D and 3D datasets (such as Banana, Complex9, and Chainlink) used to evaluate the algorithm's topological capabilities. Repository: [deric/clustering-benchmark](https://github.com/deric/clustering-benchmark)

## Repository Documents

* **diploma_thesis.pdf**: The comprehensive diploma thesis document detailing the theoretical background, mathematical proofs, architectural pipeline, and full experimental evaluations.
