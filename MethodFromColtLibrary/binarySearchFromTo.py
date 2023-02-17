'''
/**
 * Searches the receiver for the specified value using
 * the binary search algorithm.  The receiver must <strong>must</strong> be
 * sorted (as by the sort method) prior to making this call.  If
 * it is not sorted, the results are undefined: in particular, the call
 * may enter an infinite loop.  If the receiver contains multiple elements
 * equal to the specified object, there is no guarantee which instance
 * will be found.
 *
 * @param key the value to be searched for.
 * @param from the leftmost search position, inclusive.
 * @param to the rightmost search position, inclusive.
 * @return index of the search key, if it is contained in the receiver;
 *	       otherwise, <tt>(-(<i>insertion point</i>) - 1)</tt>.  The <i>insertion
 *	       point</i> is defined as the the point at which the value would
 * 	       be inserted into the receiver: the index of the first
 *	       element greater than the key, or <tt>receiver.size()</tt>, if all
 *	       elements in the receiver are less than the specified key.  Note
 *	       that this guarantees that the return value will be &gt;= 0 if
 *	       and only if the key is found.
 * @see java.util.Arrays
 */
public int binarySearchFromTo(double key, int from, int to) {
	int low=from;
	int high=to;
	while (low <= high) {
		int mid =(low + high)/2;
		double midVal = get(mid);

		if (midVal < key) low = mid + 1;
		else if (midVal > key) high = mid - 1;
		else return mid; // key found
	}
	return -(low + 1);  // key not found.
}
'''
def binarySearchFromTo(data, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)/2
        midVal = data[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)


