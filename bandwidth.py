#!/usr/bin/python

# -*- coding: utf-8 -*-

import argparse

def bitsToB(bits):
	return bits / 8
def bitsToKb(bits):
	return bits / 1000
def bitsToKB(bits):
	return bitsToKb(bits) / 8
def bitsToMb(bits):
	return bitsToKb(bits) / 1000
def bitsToMB(bits):
	return bitsToMb(bits) / 8
def bitsToGb(bits):
        return bitsToMb(bits) / 1000
def bitsToGB(bits):
        return bitsToGb(bits) / 8

# ---

def bytesToBits(bytesAmount):
        return bytesAmount * 8
def kbToBits(kbAmount):
        return kbAmount * 1000
def mbToBits(mbAmount):
        return kbToBits(mbAmount * 1000)
def gbToBits(gbAmount):
        return mbToBits(gbAmount * 1000)

# ---

def mbToKB(mb):
        return bitsToKB(mbToBits(mb))
def mbToMB(mb):
        return mb / 8
def gbToMB(gb):
        return bitsToMB(gbToBits(gb))

if __name__ == '__main__':
        btB = bitsToB(80)
        assert btB == 10.0, "btB is equal to {0}.".format(btB)
        btkb = bitsToKb(1000)
        assert btkb == 1.0, "btkb is equal to {0}.".format(btkb)
        btkB = bitsToKB(10000 * 8)
        assert btkB == 10.0, "btkB is equal to {0}.".format(btkB)
        btmb = bitsToMb(1000000)
        assert btmb == 1.0, "btmb is equal to {0}.".format(btmb)
        btmB = bitsToMB(1000000 * 8)
        assert btmB == 1.0, "btmB is equal to {0}.".format(btmB)
        btgb = bitsToGb(1000000000)
        assert btgb == 1.0, "btgb is equal to {0}.".format(btgb)
        btgB = bitsToGB(1000000000 * 8)
        assert btgB == 1.0, "btgB is equal to {0}.".format(btgB)
        gbtmB = gbToMB(1)
        assert gbtmB == 125.0, "gbtmB is equal to {0}.".format(gbtmB)
        parser = argparse.ArgumentParser(prog='BytesConverter', description= """
Convertisseur d'unité de mesure de bande passante.
La bande passante (réseau) est très souvent exprimée en Mbit/s ou Mbitps ou encore
Gbit/s.
Cet utilitaire a pour but de convertir ces données en unités plus intelligibles,
comme le Mo, le Ko ou le Go.
""")
        parser.add_argument('-mbmo', type=float, nargs=1, metavar='<N Mbits>', help='''
Convertit N Mbits en Mo. La valeur en Mbits doit forcément être flottante. Si,
de base, elle ne l'est pas, ajoutez une virgule. Exemple:
10Mbits => écrivez 10.0
''')
        args = parser.parse_args()
        submittedValue = args.mbmo[0]
        convertedValue = mbToMB(submittedValue)
        print("""
{0}Mbits(mega bits) vaut {1}Mo(mega octects).
""".format(submittedValue, convertedValue))
