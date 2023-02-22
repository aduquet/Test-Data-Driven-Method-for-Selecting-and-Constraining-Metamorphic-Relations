'''
/**
 * Returns the pooled mean of two data sequences.
 * That is <tt>(size1 * mean1 + size2 * mean2) / (size1 + size2)</tt>.
 *
 * @param size1 the number of elements in data sequence 1.
 * @param mean1 the mean of data sequence 1.
 * @param size2 the number of elements in data sequence 2.
 * @param mean2 the mean of data sequence 2.
 */
public static double pooledMean(int size1, double mean1, int size2, double mean2) {
	return (size1 * mean1 + size2 * mean2) / (size1 + size2);
}

'''
def pooledMean(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
