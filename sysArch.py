# Check architecture
# @author: João Vitor Mussel Canato

import sys

def sysArch():
    return ("32", "64")[sys.maxsize > 2**32]

def is32():
    return not sys.maxsize > 2**32

def is64():
    return sys.maxsize > 2**32
