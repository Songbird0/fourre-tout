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
        assert btB == 10.0, "btB is equal to %s.".format(btB)
        btkb = bitsToKb(1000)
        assert btkb == 1.0, "btkb is equal to %s.".format(btkb)
        btkB = bitsToKB(10000 * 8)
        assert btkB == 10.0, "btkB is equal to %s.".format(btkB)
        btmb = bitsToMb(1000000)
        assert btmb == 1.0, "btmb is equal to %s.".format(btmb)
        btmB = bitsToMB(1000000 * 8)
        assert btmB == 1.0, "btmB is equal to %s." % btmB
        btgb = bitsToGb(1000000000)
        assert btgb == 1.0, "btgb is equal to %s." % btgb
        btgB = bitsToGB(1000000000 * 8)
        assert btgB == 1.0, "btgB is equal to %s." % btgB
        gbtmB = gbToMB(1)
        assert gbtmB == 125.0, "gbtmB is equal to %s." % gbtmB
        
