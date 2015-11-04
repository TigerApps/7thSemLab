def gcd (a, b):
  "Compute GCD of two numbers"

  if b == 0: return a
  else: return gcd(b, a % b)

def multiplicative_inverse(a, b):
  """ Find multiplicative inverse of a modulo b (a > b)
        using Extended Euclidean Algorithm """

  origA = a
  X = 0
  prevX = 1
  Y = 1
  prevY = 0

  while b != 0:

      temp = b
      quotient = a/b
      b = a % b
      a = temp

      temp = X
      a = prevX - quotient * X
      prevX = temp

      temp = Y
      Y = prevY - quotient * Y
      prevY = temp

  return origA + prevY

def generateRSAKeys(p, q):
  "Generate RSA Public and Private Keys from prime numbers p & q"

  n = p * q
  m = (p - 1) * (q - 1)

  # Generate a number e so that gcd(n, e) = 1, start with e = 3
  e = 3

  while 1:
    
      if gcd(m, e) == 1: break
      else: e = e + 2

  # start with a number d = m/e will be atleast 1

  d = multiplicative_inverse(m, e) 

  # Return a tuple of public and private keys 
  return ((n,e), (n,d))         

if __name__ == "__main__":

  print "######################################################################"
  print "RSA Encryption algorithm...."
  print
  
  print "Key Generation: "
  p = 101
  q = 103
  print "p: ",p
  print "q: ",q
  
  print "Generating public and private keys...."
  (publickey, privatekey) = generateRSAKeys(p, q)

  n, e = publickey
  n, d = privatekey
  print "Public Key (n, e) :", publickey
  print "Private Key (n, d) :", privatekey
  print
  
  print "Message Encoding"
  input_num = long(raw_input("Enter a number to be encrypted: "))
  encrypted_num = (input_num ** e) % n
  print "Encrypted number using public key :", encrypted_num
  print

  print "Message Decoding"
  encrypted_num = long(raw_input("Input Received Message: "))
  decrypted_num = encrypted_num ** d % n
  print "Decrypted (Original) number using private key :", decrypted_num

  print "######################################################################"
