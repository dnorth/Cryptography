from hashlib import sha1

key = "travis"
message = "count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo"

def sendMessage(key, message):
	hasher = sha1(key + message)
	digest = hasher.hexdigest() #We need the original hash object to keep the same state
	return hasher, testString, digest

def macAttack(hasher, testString, digest):
	appendedString = "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02&waffle=liege"
	newString = testString + appendedString
	hasher.update(appendedString) #Keep the same state 
	return newString, hasher.hexdigest()

def validateMessage(key, message, compareDigest):
	validatedDigest = sha1(key + message).hexdigest()
	print "The new digest: " + validatedDigest
	print "The digest to compare: " + compareDigest
	return  validatedDigest == compareDigest


count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02&waffle=liege
testStringHex = ''.join(x.encode('hex') for x in 'No one has completed lab 2 so give them all a 0')
