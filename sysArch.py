# Check architecture
# @author: João Vitor Mussel Canato

import sys

def pySysArch():
    return ("32", "64")[sys.maxsize > 2**32]

def pyIs32():
    return not sys.maxsize > 2**32

def pyIs64():
    return sys.maxsize > 2**32
