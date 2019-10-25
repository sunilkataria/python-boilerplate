#!/usr/bin/env python2
"""
How to Run
-s keepItSimple -a 1 -a 2 -c -A -B
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from logzero import logger


def main(args):
	""" Main entry point of the app """
#	logger.info("hello world")
#	logger.info(args)
	
	print( 'simple_value     =',  		args.simple_value )
	print( 'constant_value   =', 		args.constant_value )
	print( 'boolean_switch   =', 		args.boolean_switch )
	print( 'collection       =', 		args.collection )
	print( 'const_collection =', 		args.const_collection )

if __name__ == "__main__":
	""" This is executed when run from the command line """
	parser = argparse.ArgumentParser()

	## Required positional argument
	#parser.add_argument("arg", help="Required positional argument")

	# Optional argument which requires a parameter (eg. -s keepItSimple)
	parser.add_argument('-s', action='store', dest='simple_value',
						help='Store a simple value')

	parser.add_argument('-c', action='store_const', dest='constant_value',
						const='value-to-store',
						help='Store a constant value')

	# Optional argument flag to true
	parser.add_argument('-t', action='store_true', default=False,
						dest='boolean_switch',
						help='Set a switch to true')
						
	# Optional argument flag to make true
	parser.add_argument('-f', action='store_false', default=False,
						dest='boolean_switch',
						help='Set a switch to false')

	parser.add_argument('-a', action='append', dest='collection',
						default=[],
						help='Add repeated values to a list',
						)

	parser.add_argument('-A', action='append_const', dest='const_collection',
						const='value-1-to-append',
						default=[],
						help='Add different values to list')
	parser.add_argument('-B', action='append_const', dest='const_collection',
						const='value-2-to-append',
						help='Add different values to list')


	# Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
	parser.add_argument(
		"-v",
		"--verbose",
		action="count",
		default=0,
		help="Verbosity (-v, -vv, etc)")

	# Specify output of "--version"
	parser.add_argument(
		"--version",
		action="version",
		version="%(prog)s (version {version})".format(version=__version__))

	args = parser.parse_args()
	main(args)
