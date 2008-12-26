#!/usr/bin/env python2.5

from __future__ import with_statement
import os
import random


word_path = os.path.expanduser ("~/.mydict")
repeat = 5 
sa = 30 #star amount

word_list = []
with open (word_path) as f:
    for line in f:
        if len ( line.split (' ') ) == 2:
            word_list.append ( [ line.split (' ')[0].strip(' \n'),
                                 int ( line.split (' ')[1].strip(' \n') ) ] )
        else:
            word_list.append ( [ line.strip(' \n'), 0 ] )

random.seed ()

while True:
    if len (word_list) == 0:
        print 'List is empty'
        break
    r = random.randrange (0, len (word_list), 1)
#     print '~' * sa
    print word_list [r][0]
#     print '~' * sa
#     print "Y/N/D/E?"
    choice = raw_input()
    if choice == 'y':
        word_list [r][1] += 1
        if word_list [r][1] == repeat:
            del word_list [r]
    if choice == 'n':
        os.system ( "sdcvformat.sh " + word_list [r][0] + " | pager" )
    if choice == 'd':
        del word_list [r]
    if choice == 'q':
        break
    
with open (word_path, 'w') as f:
    for word in word_list:
        f.write ( word[0] +' '+ str (word[1]) + '\n' )
