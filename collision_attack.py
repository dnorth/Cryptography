from hashlib import sha1
import time

test = "travis"

def collision(inputString, hash_size):
	startTime = time.time()
	currentHashes = []
	coll = False
	testString = inputString
	while not coll:
		testString = str(int(testString) + 1) 
		testHash = sha1(testString).hexdigest()[:hash_size]
		if testString == inputString:
			pass
		if testHash in currentHashes:
			coll = True
		else:
			currentHashes.append(testHash)
	endTime = time.time()
	timeDifference = endTime - startTime
	return timeDifference, inputString, testString, len(currentHashes), testHash

def myPreImage(inputString, hash_size):
	startTime = time.time()
	sha = sha1(inputString)
	realHash = sha.hexdigest()[:hash_size]
	coll = False
	testString = "00000"
	testHash = "00000"
	while not coll:
		if testHash == realHash:
			coll=True
		else:
			testString = str(int(testString) + 1) 
			testHash = sha1(testString).hexdigest()[:hash_size]
	endTime = time.time()
	timeDifference = endTime - startTime
	return timeDifference, inputString, testString, realHash, testHash