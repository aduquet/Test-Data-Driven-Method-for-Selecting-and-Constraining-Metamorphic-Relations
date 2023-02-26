#!/bin/sh

python3 'executerFiles/executer_add_values.py' -i 'MR_InputTransformations/TestData_MRT.json' -o add_values
# python3 'executerFiles/executer_array_copy.py' -i 'MR_InputTransformations/TestData_MRT.json' -o array_copy
python3 'executerFiles/executer_average.py' -i 'MR_InputTransformations/TestData_MRT.json' -o average
# python3 'executerFiles/executer_bubble.py' -i 'MR_InputTransformations/TestData_MRT.json' -o bubble
python3 'executerFiles/executer_checkNonNegative.py' -i 'MR_InputTransformations/TestData_MRT.json' -o	checkNonNegative
python3 'executerFiles/executer_checkPositive.py' -i 'MR_InputTransformations/TestData_MRT.json' -o checkPositive
python3 'executerFiles/executer_cnt_zeros.py' -i 'MR_InputTransformations/TestData_MRT.json' -o cnt_zeros
python3 'executerFiles/executer_count_non_zeros.py' -i 'MR_InputTransformations/TestData_MRT.json' -o count_non_zeros
python3 'executerFiles/executer_durbinWatson.py' -i 'MR_InputTransformations/TestData_MRT.json' -o durbinWatson
python3 'executerFiles/executer_entropy.py' -i 'MR_InputTransformations/TestData_MRT.json' -o entropy
python3 'executerFiles/executer_find_magnitude.py' -i 'MR_InputTransformations/TestData_MRT.json' -o find_magnitude
python3 'executerFiles/executer_find_max.py' -i 'MR_InputTransformations/TestData_MRT.json' -o find_max
python3 'executerFiles/executer_find_max2.py' -i 'MR_InputTransformations/TestData_MRT.json' -o find_max2
python3 'executerFiles/executer_find_median.py' -i 'MR_InputTransformations/TestData_MRT.json' -o find_median
python3 'executerFiles/executer_find_min.py' -i 'MR_InputTransformations/TestData_MRT.json' -o find_min
python3 'executerFiles/executer_geometric_mean.py' -i 'MR_InputTransformations/TestData_MRT.json' -o geometric_mean
python3 'executerFiles/executer_harmonicMean.py' -i 'MR_InputTransformations/TestData_MRT.json' -o harmonicMean
# python3 'executerFiles/executer_insertion_sort.py' -i 'MR_InputTransformations/TestData_MRT.json' -o insertion_sort
python3 'executerFiles/executer_kurtosis.py' -i 'MR_InputTransformations/TestData_MRT.json' -o kurtosis
python3 'executerFiles/executer_max.py' -i 'MR_InputTransformations/TestData_MRT.json' -o max
python3 'executerFiles/executer_min.py' -i 'MR_InputTransformations/TestData_MRT.json' -o min
python3 'executerFiles/executer_product.py' -i 'MR_InputTransformations/TestData_MRT.json' -o product
# python3 'executerFiles/executer_reverse.py' -i 'MR_InputTransformations/TestData_MRT.json' -o reverse
python3 'executerFiles/executer_safeNorm.py' -i 'MR_InputTransformations/TestData_MRT.json' -o safeNorm
python3 'executerFiles/executer_sampleVariance.py' -i 'MR_InputTransformations/TestData_MRT.json' -o sampleVariance
python3 'executerFiles/executer_skew.py' -i 'MR_InputTransformations/TestData_MRT.json' -o skew
# python3 'executerFiles/executer_square.py' -i 'MR_InputTransformations/TestData_MRT.json' -o square
# python3 'executerFiles/executer_standardize.py' -i 'MR_InputTransformations/TestData_MRT.json' -o standardize
python3 'executerFiles/executer_sum.py' -i 'MR_InputTransformations/TestData_MRT.json' -o sum
python3 'executerFiles/executer_sumOfLogarithms.py' -i 'MR_InputTransformations/TestData_MRT.json' -o sumOfLogarithms
python3 'executerFiles/executer_variance.py' -i 'MR_InputTransformations/TestData_MRT.json' -o variance