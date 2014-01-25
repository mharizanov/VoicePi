#!/usr/bin/env python

from optparse import OptionParser
import sys
import os

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option('-f', '--from',
            action='store', dest='sender',
            default=None, help='specify sender')
    parser.add_option('-s', '--subject',
            action='store', dest='subject',
            default=None, help='specify subject')
    parser.add_option('-m', '--message',
            action='store', dest='message',
            default=None, help='specify message')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    (options, args) = parser.parse_args()

    # rest of program...
    if options.sender is None or options.subject is None or options.message is None:
	sys.exit("Not all parameters are passed")
    if options.sender=='******----*******@gmail.com' and options.subject=='Note to self':

	if options.message =='TV off':
		if os.path.isfile('/home/pi/lg.py'): # that' my TV command script
			cmd = '/home/pi/lg.py 1'
			os.system(cmd)
			print 'Switched TV off'

	if options.message.startswith('Log '): # Catch 'log' commands, these are expected to be in the format: 'Log Martin weight 12.3' i.e. 'Log Dim1 Dim2 value'
		if os.path.isfile('/home/pi/gdoc.py'):
			cmd = '/home/pi/gdoc.py '+ options.message[4:] # pass on the parameters from 'Log ' onwards
			os.system(cmd)
			print 'Logged to Google Document'

	if options.message.startswith('Internet '):
		if os.path.isfile('/home/pi/dani.sh'):
			cmd = '/home/pi/dani.sh ' +options.message[4:]
			os.system(cmd)
			print 'Internet access for teenager son is now ' +options.message[4:] +'ed'


if __name__ == '__main__':
    main()
