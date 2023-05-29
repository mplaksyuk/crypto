# Diffie-Hellman Code

def is_prime(p):
	if p < 1:
		return False
	elif p > 1:
		if p == 2:
			return True
		for i in range(2, p):
			if p % i == 0:
				return False
			return True


def is_primitive(g, p, L):
	for i in range(1, p):
		L.append(pow(g, i) % p)
	for i in range(1, p):
		if L.count(i) > 1:
			L.clear()
			return False
		return True


if __name__ == '__main__':
    l = []
    while True:
        P = int(input("Enter P : "))
        if not is_prime(P):
            print("Number Is Not Prime, Please Enter Again!")
            continue
        break

    while True:
        G = int(input(f"Enter The Primitive Root Of {P} : "))
        if not is_primitive(G, P, l):
            print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
            continue
        break

    # Private Keys
    private_key1 = int(input("Enter The Private Key Of User 1 : "))
    private_key2 = int(input("Enter The Private Key Of User 2 : "))
    while private_key1 >= P or private_key2 >= P:
        print(f"Private Key Of Both The Users Should Be Less Than {P}!")

        private_key1 = int(input("Enter The Private Key Of User 1 : "))
        private_key2 = int(input("Enter The Private Key Of User 2 : "))

    # Calculate Public Keys
    public_key1 = pow(G, private_key1) % P 
    public_key2 = pow(G, private_key2) % P

    # Generate Secret Keys
    secret_key1 = pow(public_key2, private_key1) % P
    secret_key2 = pow(public_key1, private_key2) % P

    print(f"\nSecret Key For User 1 Is {secret_key1}\nSecret Key For User 2 Is {secret_key2}\n")

    if secret_key1 == secret_key2:
        print("Keys Have Been Exchanged Successfully")
    else:
        print("Keys Have Not Been Exchanged Successfully")
