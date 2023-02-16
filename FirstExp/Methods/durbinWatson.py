'''
/**
 * Durbin-Watson computation.
 */
public static double durbinWatson(DoubleArrayList data) {
	int size = data.size();
	if (size < 2) throw new IllegalArgumentException("data sequence must contain at least two values.");

	double[] elements = data.elements();
	double run = 0;
	double run_sq = 0;
	run_sq = elements[0] * elements[0];
	for(int i=1; i<size; ++i) {
		double x = elements[i] - elements[i-1];
		run += x*x;
		run_sq += elements[i] * elements[i];
	}

	return run / run_sq;
}
'''

def durbinWatson(data):
    size = len(data)
    if(size < 2):
        raise NameError('data sequence must contain at least two values.')

    elements = data.copy()
    run = 0
    run_sq = 0

    run_sq = elements[0] * elements [0]

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]
        run += x * x
        run_sq += elements[i] * elements [i]

    return run/run_sq
