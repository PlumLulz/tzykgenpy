# Turkey Zyxel
# Zyxel VMG3312-B10B and VGM3313-B10A
import hashlib
import argparse

def turkey_zyxelgen(serial):

	junk = 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
	'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
	'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
	'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
	'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
	'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
	'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
	'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
	'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
	'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
	'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
	'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
	'veivelvevvidvikvisvriyreyte'

	md5 = hashlib.md5()
	md5.update(serial.encode())

	p = ""
	summ = 0

	for i in range(16):
		byte = md5.digest()[i]
		c1 = hex(byte >> 4)[2:].upper()
		c2 = hex(byte % 16)[2:]
		if c1 == "0":
			c1 = c2
		p += c1
		p += c2
		summ = summ + ord(c1) + ord(c2)
	i = summ % 265
	if summ & 1:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:]
	else:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:].upper()

	s2 = "%s%s%s%s%s%s%s" % (p[0], s1[0:2], p[1:3], s1[2:4], p[3:6], s1[4:6], p[6:])
	
	md52 = hashlib.md5()
	md52.update(s2.encode())
	# Manually convert each byte and check for leading 0. 
	hex_digest = ""
	for i in range(16):
		hbyte = "{:02X}".format(md52.digest()[i])
		if hbyte[0] == "0":
			hbyte = hbyte[1] + hbyte[1]
		hex_digest += hbyte
	alter = [dig.upper() if not i % 2 else dig.lower() for i, dig in enumerate(hex_digest)]
	alter = "".join(alter)
	key = alter[13:26]
	print(key)


parser = argparse.ArgumentParser(description='Turkey Zyxel Keygen. (Zyxel VMG3312-B10B and VGM3313-B10A)')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

turkey_zyxelgen(args.serial)
