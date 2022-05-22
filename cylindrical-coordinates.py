#
#
#
#
#	Useful functions in Cylindrical Coordinates
#
#
#

def magnitude(r,phi,z):
	#  Return the distance from the Origin to point P
	#  This is the same as the magnitude of the vector P
	#  Interestingly, magnitude is a function of r and z only

	distance = sqrt( r**2 + z**2 )
	return distance



def distance_between_points(r1,phi1,z1, r2,phi2,z2):
	#  Return the distance between points P and Q
	#  Use the Law of Cosines to find the distance between
	#  the projection of the two points on the r phi plane, then do the
	#  Pythagorean Theorem with that and their z difference.
	#  Law of Cosines:
	#  c^2 = a^2 + b^2 - 2ab cos( gamma )

	c_squared = r1**2 + r2**2 - 2*r1*r2*cos(phi1-phi2)
	d = sqrt( c_squared + ((z1-z2)**2)  )
	return d
