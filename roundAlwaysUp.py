def roundAlwaysUp( toRound, end = 10 ):
	""" 
	This snippet will round-up any given integer or float, to at least 10 or to the highest multiple of 10.
	You can pass an unsigned/positive integer as the "end" argument if you want the number to be rounded to at least a multiple of "end".
	Returned value will always be an integer.
	"""
	end = abs( int(end) )

	if end == 0:
		end = 10
	times = toRound/end

	if times >= 0:
		times = times + 1
	else:
		times = times - 1
	return ( int( times ) )*end;


