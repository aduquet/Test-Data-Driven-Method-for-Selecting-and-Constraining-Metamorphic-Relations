'''
/**
 * Returns the covariance of two data sequences, which is 
 * <tt>cov(x,y) = (1/(size()-1)) * Sum((x[i]-mean(x)) * (y[i]-mean(y)))</tt>.
 * See the <A HREF="http://www.cquest.utoronto.ca/geog/ggr270y/notes/not05efg.html"> math definition</A>.
 */
public static double covariance(DoubleArrayList data1, DoubleArrayList data2) {
	int size = data1.size();
	if (size != data2.size() || size == 0) throw new IllegalArgumentException();
	double[] elements1 = data1.elements();
	double[] elements2 = data2.elements();
	
	double sumx=elements1[0], sumy=elements2[0], Sxy=0;
	for (int i=1; i<size; ++i) {
		double x = elements1[i];
		double y = elements2[i];
		sumx += x;
		Sxy += (x - sumx/(i+1))*(y - sumy/i);
		sumy += y;
		// Exercise for the reader: Why does this give us the right answer?
	}
	return Sxy/(size-1);
}
'''

def covariance(data1, data2):
    size = len(data1)

    if(size != len(data2) or size == 0):
        raise NameError('IligalArgumentException')

    elements1 = data1.copy()
    elements2 = data2.copy()

    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(1, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)

