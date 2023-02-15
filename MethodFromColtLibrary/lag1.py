'''
/**
 * Returns the lag-1 autocorrelation of a dataset; 
 * Note that this method has semantics different from <tt>autoCorrelation(..., 1)</tt>;
 */
public static double lag1(DoubleArrayList data, double mean) {
	int size = data.size();
	double[] elements = data.elements();
	double r1 ;
	double q = 0 ;
	double v = (elements[0] - mean) * (elements[0] - mean) ;

	for (int i = 1; i < size ; i++) {
		double delta0 = (elements[i-1] - mean);
		double delta1 = (elements[i] - mean);
		q += (delta0 * delta1 - q)/(i + 1);
		v += (delta1 * delta1 - v)/(i + 1);
	}

	r1 = q / v ;
	return r1;
}
'''
def lag1(data, mean):
    size = len(data)
    elements = data.copy()
    q = 0
    v = (elements[0] - mean) * (elements[0] - mean)

    for i in range(1, size):
        
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1

