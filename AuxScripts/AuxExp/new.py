from operator import methodcaller
import count_non_zeros

foo_ = methodcaller("count_non_zeros", a=[2,3,0,0])
print(foo_(count_non_zeros))