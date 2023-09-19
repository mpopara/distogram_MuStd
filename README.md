# distogram_MuStd
Python script to compute and visualize residue pairwise mean distance and standard deviation of a distogram

## General description

Since distograms are multidimensional arrays, we can only visualize them in some kind of condensed form- for instance, by extracting the features/moments of distrograms.
Already within the repository [_distogram_](https://github.com/mpopara/distogram) this issue was tackled by computing the mean, standard deviation and skewness of distogram, which are after normalization stacked into a R,G,B array (0-1 float), 
in order to create a RGB image. However, such representation is difficult to interpret, because all three features of inter-residue distance distribution are combined into one color code.
Furthermore, we might be more interested to be able to separately inspect moments of distribution.
Script [_moments_of_distogram.py_](https://github.com/mpopara/distogram_MuStd/blob/main/moments_of_distogram.py) calculates mean distance and standard deviation of all pairwise inter-residue distance
distributions, and plots them separately on upper and lower triangle of the residue pairwise matrix. 
Such reduced representation of a distogram is particularly convenient for the comparison of two distograms.

![mean_std_300dpi](https://github.com/mpopara/distogram_MuStd/assets/40856779/eea73859-5be1-42df-898d-be31ade10f4d)

Illustration is adapted from the article by Dittrich _et al_, 2023.<sup>1</sup>


## Input file requirements
As input files are required:

* Counts (i.e. distance bin occupancies) and distance bins as two numpy objects with extension .npy. For details on how distogram is computed, reader is referred
to repository [_distogram_](https://github.com/mpopara/distogram). 
Exemplary input files are provided in the [_example_data_](https://github.com/mpopara/distogram_MuStd/tree/main/example_data) directory of this repository.

## Dependencies
[_moments_of_distogram.py_](https://github.com/mpopara/distogram_MuStd/blob/main/moments_of_distogram.py) is a python script built on Python 3.8.8. Script was tested with provided exemplary data under the following configuration:

* Windows 10
* Python 3.8.8
* numpy 1.23.0
* matplotlib 3.7.1

## References

1. Dittrich, J.; Popara, M.; Kubiak, J.; Dimura, M.; Schepers, B.; Verma, N.; Schmitz, B.; Dollinger, . P.; Kovacic, F.; Jaeger, K. E.;
Seidel, C. A. M.; Peulen, T. O.; Gohlke, H., Resolution of Maximum Entropy Method-Derived Posterior Conformational Ensembles of a Flexible System Probed by FRET and Molecular Dynamics Simulations.
J Chem Theory Comput 2023, 19 (8), 2389-2409.

## Authors

* Milana Popara
* Thomas-Otavio Peulen
