

#p and q were large 512 bit prime numbers found online
p = 6997040548236306032270028142697844577679802860009390483825615834396766817911865846408328563633463004219619254639348141491179371158391819359706834377936017

q = 8593701979078313474945043728666349994614714557320430419781846880808258697302068260916571720507008823663836468130075453764283766701743551377885890781118909

#plaintextMessage was given during part 3 of the passoff
plaintextMessage = 212788291171290661843158364587637197333531097895143818988755059744299426205080018037256906030614828346200464605058471107535343001238694433356829682872

#encryptedMessage was given during part 4 of the passoff
encryptedMessage = 38836004958973333808444474744049950597152340928568277009922464771958929445481001650323472151575854567252425265205811145901606099326089029141609035935574695159638546746822086067633268843681771212436983924976927634925742602911873891599802616821582340073810951502143926279012766864221984005313249745229167595735

#e was defined in part 1 of the passoff
e = 65537

def createSecretKey(p, q, e):
	N = p * q
	phiN = (p-1)*(q-1)
	gcd, xPrime, d = euclidianGCD(phiN, e)
	if gcd == 1:
		print "phi-N and e are relatively prime. Operation Successful"
		return d
	else:
		print "phi-N and e are NOT relatively prime. Operation Aborted"
		return None

 
def encrypt(plaintextMessage, e, publicKey):
	return modexp(plaintextMessage, e, publicKey)


def decrypt(encryptedMessage, secretKey, publicKey):
	return modexp(encryptedMessage, secretKey, publicKey)

#Returns GCD, X', Y'
def euclidianGCD(a,b):
	prevx, x=1, 0
	prevy, y=0, 1
	while b:
		q = a/b
		x, prevx = prevx - q*x, x #Finding X' 
		y, prevy = prevy - q*y, y #Finding Y'
		a, b = b, a%b #Determining the GCD
	return a, prevx, prevy

def modexp(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
	