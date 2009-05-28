#!/usr/bin/env python2.5

import urllib

def fetchpage(url):
	"""Returns whether an url is valid.
	"""

	page = urllib.urlopen(url)
	first = page.readline()

	return first != '\n'

def main():
	badurl = "http://googleio.appspot.com/a/839625"
        goodurl = "http://googleio.appspot.com/a/83962566"

	print "bad = %s" % fetchpage(badurl)
        print "good = %s" % fetchpage(goodurl)

if __name__ == '__main__':
	main()

