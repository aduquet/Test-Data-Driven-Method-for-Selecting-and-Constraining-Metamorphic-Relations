'''
/**
 * Returns the mean deviation of a dataset.
 * That is <tt>Sum (Math.abs(data[i]-mean)) / data.size())</tt>.
 */
public static double meanDeviation(DoubleArrayList data, double mean) {
	double[] elements = data.elements();
	int size = data.size();
	double sum=0;
	for (int i=size; --i >= 0;) sum += Math.abs(elements[i]-mean);
	return sum/size;
}
'''
def meanDeviation(data, mean):

    elements = data.copy()
    size = len(elements)

    sum = 0

    for i in range(size-1 , -1, -1):
        sum += abs(elements[i] - mean)
        
    return sum / size

