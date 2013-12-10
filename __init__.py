#!/usr/bin/env python

def lib1(arg):
  return "Hello %s, I am lib1" % arg
  
if __name__ == '__main__':
  print lib1("World")
