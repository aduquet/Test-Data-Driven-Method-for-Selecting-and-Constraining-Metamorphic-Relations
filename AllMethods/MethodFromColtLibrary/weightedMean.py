'''
/**
 * Returns the weighted mean of a data sequence.
 * That is <tt> Sum (data[i] * weights[i]) / Sum ( weights[i] )</tt>.
 */
public static double weightedMean(DoubleArrayList data, DoubleArrayList weights) {
	int size = data.size();
	if (size != weights.size() || size == 0) throw new IllegalArgumentException();
	
	double[] elements = data.elements();
	double[] theWeights = weights.elements();
	double sum = 0.0;
	double weightsSum = 0.0;
	for (int i=size; --i >= 0; ) {
		double w = theWeights[i];
		sum += elements[i] * w;
		weightsSum += w;
	}

	return sum/weightsSum;
}
'''
def weightedMean(data, weights):

    size = len(data)
    
    if(size != len(weights) or size == 0):
        raise NameError('IligalArgumentException')
    
    elements = data.copy()
    theWeights = weights.copy()
    suma = 0
    weightSum = 0
    
    for i in range(size, -1, -1):
        w = theWeights[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
