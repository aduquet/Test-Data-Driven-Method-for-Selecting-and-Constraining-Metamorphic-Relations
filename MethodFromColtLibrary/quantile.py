'''
/**
 * Returns the <tt>phi-</tt>quantile; that is, an element <tt>elem</tt> for which holds that <tt>phi</tt> percent of data elements are less than <tt>elem</tt>.
 * The quantile need not necessarily be contained in the data sequence, it can be a linear interpolation.
 * @param sortedData the data sequence; <b>must be sorted ascending</b>.
 * @param phi the percentage; must satisfy <tt>0 &lt;= phi &lt;= 1</tt>.
 */
public static double quantile(DoubleArrayList sortedData, double phi) {
	double[] sortedElements = sortedData.elements();
	int n = sortedData.size();
	
	double index = phi * (n - 1) ;
	int lhs = (int)index ;
	double delta = index - lhs ;
	double result;

	if (n == 0) return 0.0 ;

	if (lhs == n - 1) {
		result = sortedElements[lhs] ;
	}
	else {
		result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1] ;
	}

	return result ;
}
'''

def quantile(data, phi):

    sortedElements = data.copy()
    n = len(sortedElements)

    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
