#!/bin/sed -f

s:\\:\\textbackslash:g
s:[`&$%^#_{}]:\\&{}:g
s:\\textbackslash:\\textbackslash{}:g


