'''
/**
 * Returns the auto-correlation of a data sequence.
 */
public static double autoCorrelation(DoubleArrayList data, int lag, double mean, double variance) {
	int N = data.size();
	if (lag >= N) throw new IllegalArgumentException("Lag is too large");

	double[] elements = data.elements();
	double run = 0;
	for( int i=lag; i<N; ++i)
		run += (elements[i]-mean)*(elements[i-lag]-mean);
  
	return (run/(N-lag)) / variance;
}
'''

def autoCorrelation(data, lag, mean, variance):

    N = len(data)
    if(lag >= N):
        raise NameError('Lag is too large')

    elements = data.copy()

    run = 0
    for i in range(lag, N):
        run += (elements[i] - mean) * (data[i - lag] - mean)
    return ((run / (N-lag)) /variance)

