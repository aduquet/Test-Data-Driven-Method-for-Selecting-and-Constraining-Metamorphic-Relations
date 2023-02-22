import math
'''
/**
 * Returns the sample skew of a data sequence.
 *
 * Ref: R.R. Sokal, F.J. Rohlf, Biometry: the principles and practice of statistics
 * in biological research (W.H. Freeman and Company, New York, 1998, 3rd edition)
 * p. 114-115.
 *
 * @param size the number of elements of the data sequence.
 * @param moment3 the third central moment, which is <tt>moment(data,3,mean)</tt>.
 * @param sampleVariance the <b>sample variance</b>.
 */
public static double sampleSkew(int size, double moment3, double sampleVariance) {
	 int    n=size;
	 double s=Math.sqrt(sampleVariance); // sqrt( (y-ymean)^2/(n-1) )
	 double m3 = moment3*n;    // (y-ymean)^3
	 return n*m3 / ((n-1)*(n-2)*s*s*s);
}
'''

def sampleSkew(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)
