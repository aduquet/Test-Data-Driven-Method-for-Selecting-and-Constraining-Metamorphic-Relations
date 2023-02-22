'''
/**
 * Returns the sample kurtosis (aka excess) of a data sequence.
 *
 * Ref: R.R. Sokal, F.J. Rohlf, Biometry: the principles and practice of statistics
 * in biological research (W.H. Freeman and Company, New York, 1998, 3rd edition)
 * p. 114-115.
 *
 * @param size the number of elements of the data sequence.
 * @param moment4 the fourth central moment, which is <tt>moment(data,4,mean)</tt>.
 * @param sampleVariance the <b>sample variance</b>.
 */
public static double sampleKurtosis(int size, double moment4, double sampleVariance) {
	 int    n=size;
	 double s2=sampleVariance; // (y-ymean)^2/(n-1)
	 double m4 = moment4*n;    // (y-ymean)^4
	 return m4*n*(n+1) / ((n-1)*(n-2)*(n-3)*s2*s2)
		  - 3.0*(n-1)*(n-1)/((n-2)*(n-3));
}
'''

def sampleKurtosis(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
