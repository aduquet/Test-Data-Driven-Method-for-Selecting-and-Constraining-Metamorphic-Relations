'''
/**
 * Returns the kurtosis (aka excess) of a data sequence.
 * @param moment4 the fourth central moment, which is <tt>moment(data,4,mean)</tt>.
 * @param standardDeviation the standardDeviation.
 */
public static double kurtosis(double moment4, double standardDeviation) {
	return -3 + moment4 / (standardDeviation * standardDeviation * standardDeviation * standardDeviation);
}
/**
 * Returns the kurtosis (aka excess) of a data sequence, which is <tt>-3 + moment(data,4,mean) / standardDeviation<sup>4</sup></tt>.
 */
public static double kurtosis(DoubleArrayList data, double mean, double standardDeviation) {
	return kurtosis(moment(data,4,mean), standardDeviation);
}
'''

import math

def kurtosis(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)
