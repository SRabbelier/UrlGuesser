#!/usr/bin/env python2.5

import urllib

NOTFOUND_TITLE = '<title>404 Not Found</title>'
CLAIMABLE_TITLE = '    <title>Google I/O - Claim your OpenSocial profile page</title>\n'
CLAIMED_TITLE = '    <title>Google I/O - Friend Connect Scavenger Hunt</title>\n'

INVALID = "invalid"
CLAIMABLE = "claimable"
CLAIMED = "claimed"
UNKNOWN = "unknown"


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


if __name__ == '__main__':
	main()

