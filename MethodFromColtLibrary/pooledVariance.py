'''
/**
 * Returns the pooled variance of two data sequences.
 * That is <tt>(size1 * variance1 + size2 * variance2) / (size1 + size2)</tt>;
 *
 * @param size1 the number of elements in data sequence 1.
 * @param variance1 the variance of data sequence 1.
 * @param size2 the number of elements in data sequence 2.
 * @param variance2 the variance of data sequence 2.
 */
public static double pooledVariance(int size1, double variance1, int size2, double variance2) {
	return (size1 * variance1 + size2 * variance2) / (size1 + size2);
}
'''
def pooledVariance(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
