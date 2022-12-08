import random

sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
xbos = [5, 14, 15, 8, 12, 1, 2, 13, 11, 4, 6, 3, 0, 7, 9, 10]

def round (k, m):
	return sbox[m ^ k]

def enc (k, m):
	t = round(m, k[0])
	c = round(t, k[1])
	return c

def back_round(k, c):
	return xbos[c] ^ k

def dec(k, c):
	t = back_round(k[1], c)
	m = back_round(k[0], t)
	return m





#exercice 2

def enc_byte(octet,cle):
	f=ord(octet)
	l,k=f>>4,f&0x0F
	s=enc(l,cle)
	m=enc(k,cle)
	r=((s<<4)+m)
	return r
	


def dec_byte(octet,cle):
	   l,k= octet>>4,octet&0x0F
	   s = dec(l,cle)
	   m = dec(k,cle)
	   r= ((s<<4)+m)
	   return chr(r)

def enc_file(filename,cle):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".enc","w") as file_enc:
			for i in txt:
				i_enc = enc_byte(i,cle)
				file_enc.write(chr(i_enc))
# enc_file("atester.txt", (11,3))

def dec_file(filename,cle):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".dec","w") as file_dec:
			for i in txt:
				i_dec = dec_byte(ord(i), cle)
				file_dec.write(i_dec)
#dec_file("atester.txt.enc", (11,3))

# exercice 3:

def enc_file_cbc(filename,cle,vec):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".enc","w") as file_enc:
			for i in txt:
				xor =ord(i) ^ vec
				xor_enc =enc_byte(chr(xor),cle)
				vec = xor_enc
				file_enc.write(chr(xor_enc))
#enc_file_cbc("coucou.txt", (9,0), 5)

def dec_file_cbc(filename,cle,vec):
    with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".dec","w") as file_dec:
			for i in txt:
			    i_dec = dec_byte(ord(i),cle)
			    xor = ord(i_dec)  ^ v
			    vec = ord(i)
			    file_dec.write(chr(xor))	

#dec_file_cbc("coucou.txt.enc", (9,0), 5)


def enc_file_cfb(filename,cle,vec):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".enc","w") as file_enc:
			for i in txt:
				vec_enc = enc_byte(chr(vec) , cle)
				xor = ord(i) ^ vec_enc
				vec = xor
				file_enc.write(chr(xor))

#enc_file_cfb("coucou.txt", (9,0), 5)

def dec_file_cfb(filename,cle,vec):
    with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".dec","w") as file_dec:
			for i in txt:
				vec_enc = enc_byte(chr(vec) ,cle)
				xor = ord(i)  ^ vec_enc
				vec = ord(i)
				file_dec.write(chr(xor))	

#dec_file_cfb("coucou.txt.enc", (9,0), 5)


def enc_file_ofb(filename,cle,vec):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".enc","w") as file_enc:
			for i in txt:
				vec_enc = enc_byte(chr(vec), cle)
				xor =ord(i) ^ vec_enc
				vec = vec_enc
				file_enc.write(chr(xor))


def dec_file_ofb(filename,cle,vec):
	with open(filename,"r") as file:
		txt=file.read()
		with open(filename +".dec","w") as file_dec:
			for i in txt:
				vec_enc = enc_byte(chr(vec), cle)
				xor = ord(i) ^ vec_enc
				vec = vec_enc
				file_dec.write(chr(xor))





