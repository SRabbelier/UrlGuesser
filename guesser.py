#!/usr/bin/env python2.5

import urllib
import sys

NOTFOUND_TITLE = '<title>404 Not Found</title>'
CLAIMABLE_TITLE = '    <title>Google I/O - Claim your OpenSocial profile page</title>\n'
CLAIMED_TITLE = '    <title>Google I/O - Friend Connect Scavenger Hunt</title>\n'

INVALID = "invalid"
CLAIMABLE = "claimable"
CLAIMED = "claimed"
UNKNOWN = "unknown"


DIGITS='0123456789ABCDEF'

def generate_permutations(prefix):
	if len(prefix) == 8:
		return [prefix]

	permutations = []

	for i in DIGITS:
		permutations.extend(generate_permutations(prefix +i))

	return permutations

def generate(start):
	i = start
	maxValue = int('0xFFFFFFFF', 16)
	while i <= maxValue:
		hexString = "%.8X" % i
		hexString = hexString.upper()
		i += 1
		yield hexString


def fetchpage(url):
	"""Returns whether an url is valid.
	"""

	page = urllib.urlopen(url)
	content = page.readlines()

	if NOTFOUND_TITLE in content:
		return INVALID

	if CLAIMABLE_TITLE in content:
		return CLAIMABLE
	
	if CLAIMED_TITLE in content:
		return CLAIMED

	return UNKNOWN

def main():
	invalidurl = "http://googleio.appspot.com/a/839625"
        claimedurl = "http://googleio.appspot.com/a/83962566"
	unclaimedurl = "http://googleio.appspot.com/a/FACF4339"
	unknownurl = "http://googleio.appspot.com/"

	print "invalid = %s" % fetchpage(invalidurl)
        print "claimed = %s" % fetchpage(claimedurl)
	print "claimeble = %s" % fetchpage(unclaimedurl)
	print "unknownurl = %s" % fetchpage(unknownurl)

	start = ""

	if len(sys.argv) > 1:
		start = int(sys.argv[1])

	generate_permutations(start)

if __name__ == '__main__':
	main()

