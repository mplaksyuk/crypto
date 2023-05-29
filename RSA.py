import random
import math

# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()

public_key = None
private_key = None
n = None

def fill_primes():
	# Method used to fill the primes set is Sieve of
	# Eratosthenes (a method to collect prime numbers)
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Filling the prime numbers
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Picking a random prime number and erasing that prime
# number from list because p!=q
def pick_random_prime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime)
	for _ in range(k):
		next(it)

	ret = next(it)
	prime.remove(ret)
	return ret


def set_keys():
    def find_public_key(): #e
        global public_key
        public_key = 2 
        while True:
            if math.gcd(public_key, fi) == 1:
                break
            public_key += 1
	    
    def find_private_key(): #d
        global public_key, private_key
        private_key = 2
        while True:
            if (private_key * public_key) % fi == 1:
                break
            private_key += 1
	    
    global n
    p = pick_random_prime() # First prime number
    q = pick_random_prime() # Second prime number

    n = p * q
    fi = (p - 1) * (q - 1) #Euler's totient function

    find_public_key()
    find_private_key()

def crypt_handler(text, key):
    global n
    crypted_text = 1
    while key > 0:
        crypted_text *= text
        crypted_text %= n
        key -= 1
    return crypted_text

# To encrypt the given number
def encrypt(message):
	global public_key
	return crypt_handler(message, public_key)
	
# To decrypt the given number
def decrypt(encrypted_text):
	global private_key
	return crypt_handler(encrypted_text, private_key)


# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
	encoded = list(map(lambda letter: encrypt(ord(letter)), message))
	return encoded


def decoder(encoded):
	decoded = ''.join(map(lambda num: chr(decrypt(num)), encoded))
	return decoded


if __name__ == '__main__':
	fill_primes()
	set_keys()
	message = "Test Message"

	coded = encoder(message)

	print("\nInitial message: \033[92m" + message + '\033[0m')
	print("\nThe encoded message(encrypted by public key): \033[91m" + ''.join(str(p) for p in coded) + '\033[0m')
	print("\nThe decoded message(decrypted by private key): \033[92m" + decoder(coded) + '\033[0m')