
#
from cis2010utils4 import StartHere, EndHere, strhash
import pandas as pd
#####################################################################################
# Start Workshop
#
# Task 2 
StartHere( "Arlette Ruiz", "S11", "Fall 2024")

#Task 3 setup variables
x3 = 0
dd = ', doo-doo'
fish = ['minnow', 'bass', 'tuna', 'shark']
fm = ['baby', 'mommy', 'daddy', 'grandma', 'grandpa']
fm_c = len(fm)
sk = ' '
sk += fish[3]
x3 += 1

#
#Task 4 If statement
who = fm[0]
earworm = who + sk
x4 = 0             
if (x4 < 3) :
    x4 += 1
    earworm += dd
if (x4 < 3) :
    x4 += 1
    earworm += dd
if (x4 < 3) :
    x4 += 1
    earworm += dd
if (x4 < 3) :
    x4 += 1
    earworm += dd
if (x4 < 3) :
    x4 += 1
    earworm += dd
    
print(earworm)
#
#Task 5 FOR Loop
msg5 = 'I will not facebook in class'
for item in range(5) :
    print( msg5 )
print('. . . until tomorrow')
v5 = item
#
# BING Copilot  https://bing.com/copilot
# enter this prompt to Copilot
#  Build a python loop to print the message “I will not facebook in class” nine times using the loop variable i6. In the post-loop afterparty print the message “…until tomorrow”, then also print the loop variable.
#
#Task 6
# Loop to print the message 5 times
for i6 in range(5):
    print("I will not facebook in class")

# Post-loop afterparty
print("...until tomorrow")
print("Loop variable after the loop:", i6)

#
#Task 7
#setup variables
doodoos = 3
who = fm[0]
who2 = who + sk
ew1= ""
ew1 += who2
print('earworm 1')
#loop
for a in range(doodoos) :
    ew1 += dd
ew1 += '\n'
print(ew1)
ew1_h = strhash(ew1)
#endstate variables
a7= a
r7 = range(doodoos)
#
#Task 8
verse = 3
ew2 = ''
print('earworm 2')
# nested loop
for b in range(verse) :
    ew2 += who2
    for a in range(doodoos) :
        ew2 += dd
    ew2 += '\n'
ew2 += (who2 + '\n')
print(ew2)
#endstate
ew2_h = strhash(ew2)
a8 = 8
b8 = b
r8 = range(verse)
#
#Task 9
GAc = pd.read_csv('GAcodes.csv')
hx = strhash(str(GAc))
# Workshop END
#
###########################################################
# Collaboration Challenge
#
# S11ccq Q7
ce = ['hello', 'WORLD']
ce_h = strhash(str(ce))
#
# S11ccq Q8
grades = [92, 74, 84, 89, 95]
grades.append(79)
cnt = len(grades)
total = 0
for item in range(cnt) :
    score = grades[item]
    total = total + score
total = (total / cnt)
print('final grade is', total)
#
# S11ccq Q11
jz = 0
cz = 0
for jz in range(10) :
    cz += 1
print('jz:', jz)
print('cz:', cz)
#
# S11ccq Q12
verse = 3
ew3 = ''
print('earworm 2')
# nested loop
for b in range(verse) :
    ew3 += who2
    for a in range(doodoos) :
        ew3 += dd
    ew3 += '\n'
ew3 += (who2 + '\n')
print(ew3)
#endstate
ew3_h = strhash(ew3)
a8 = 8
b8 = b
r8 = range(verse)
for c in fm :
    who2 = c + sk
    for b in range(verse) :
        ew3 += who2
        for a in range(doodoos) :
            ew3 += dd
        ew3 += '\n'
    ew3 += (who2 + '\n')
c9 = c
ew3_h = hash(ew3)


#
print(strhash(str(grades)))
# S11icq Q3
a1 = ""              #this is an empty string, nothing between the quotes
m1 = "hello"     #no leading or trailing spaces
a1 = m1 + m1
pyQ3 = strhash(a1)
#
# S11icq Q4
a2 = "Hello"
m2 = "World"
a2 = a2 + m2 + '!'
pyQ4 = strhash(a2)
#
# S11icq Q5
se = fm[2]
sf = fish [2]
sg = se + sf
#
# S11icq Q6
for sm in range(2) :
    sg += dd
    print(sg)
sg_h = strhash(sg)
sg_c = len(sg)
    
#
# S11icq Q9
for item in range(5) :
    print ('this works')
    break
#
# S11icq Q10
ans9 = ""
for _ in range(74):
    ans9 += "hello "
ans9 += "world"
print(ans9)
ans9_h = strhash(str(ans9))
#
# Individual Challenge  END
EndHere( globals())
#exit()
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>#UFWQJYYJ%WZN_%4ZXJWX4FWQJYYJWZN_lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
