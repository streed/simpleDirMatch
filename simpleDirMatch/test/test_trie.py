from nose.tools import assert_equals
from simpleDirMatch.trie import Trie

def test_Trie_word():
	t = Trie( [ "people", "are", "awesome" ] )
	
	assert_equals( False, t.find( "fake" ) )
	assert_equals( "people", t.find( "people" ) )

def test_performance():
	a = [ str( i ) for i in xrange( 10000, 50000 ) ]
	t = Trie( a )

	import time
	start = time.time()
	for i in xrange( 10000, 50000 ):
		t.find( str( i ) )
	end = time.time()

	print "Trie (All are in set): %d runs in %.4f seconds ( %.2f per/sec )" % ( 
			( 50000 - 10000 ), 
			end - start, 
			( 50000 - 10000 ) / ( end - start ) )
	
	start = time.time()
	for i in xrange( 10000, 50000 ):
		_ = str( i ) in a
	end = time.time()

	print "List (All are in set ): %d runs in %.4f seconds ( %.2f per/sec )" % ( 
			( 50000 - 10000 ), 
			end - start, 
			( 50000 - 10000 ) / ( end - start ) )


	start = time.time()
	for i in xrange( 1000000, 1050000 ):
		t.find( str( i ) )
	end = time.time()

	print "Trie (All are not in set): %d runs in %.4f seconds ( %.2f per/sec )" % ( 
			( 1050000 - 1000000 ), 
			end - start, 
			( 1050000 - 1000000 ) / ( end - start ) )

	start = time.time()
	for i in xrange( 1000000, 1050000 ):
		_ = str( i ) in a
	end = time.time()

	print "List (All are not in set): %d runs in %.4f seconds ( %.2f per/sec )" % ( 
			( 1050000 - 1000000 ), 
			end - start, 
			( 1050000 - 1000000 ) / ( end - start ) )
