import time
from random import*
#CREATE Console User Interface
print("Select your hardness level:",end="")
hlevel = int(input())
level = 3
easterneggs = 0
if hlevel>10:
    print("So you have chosen death")
    next = input()
    if next == "Saruman?":
        print("""/                   ....
                                .'' .'''
.                             .'   :
\\                          .:    :
 \\                        _:    :       ..----.._
  \\                    .:::.....:::.. .'         ''.
   \\                 .'  #-. .-######'     #        '.
    \\                 '.##'/ ' ################       :
     \\                  #####################         :
      \\               ..##.-.#### .''''###'.._        :
       \\             :--:########:            '.    .' :
        \\..__...--.. :--:#######.'   '.         '.     :
        :     :  : : '':'-:'':'::        .         '.  .'
        '---'''..: :    ':    '..'''.      '.        :'
           \\  :: : :     '      ''''''.     '.      .:
            \\ ::  : :     '            '.      '      :
             \\::   : :           ....' ..:       '     '.
              \\::  : :    .....####\\ .~~.:.             :
               \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\    .'  ########## \ \ _.' '. '-.       '''.
                :\\  :     ########   \ \      '.  '-.        :
               :  \\'    '   #### :    \ \      :.    '-.      :
              :  .'\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\  '  :      :     :\ \       :        '.   :
             ::   :  \\'  :.      :     : \ \      :          '. :
             ::. :    \\  : :      :    ;  \ \     :           '.:
              : ':    '\\ :  :     :     :  \:\     :        ..'
                 :    ' \\ :        :     ;  \|      :   .'''
                 '.   '  \\:                         :.''
                  .:..... \\:       :            ..''
                 '._____|'.\\......'''''''.:..'''
                            \\""")
        easterneggs+=1
        print(f"Eastern eggs: {easterneggs}/3")
print("Enter your name:", end = "")
name = input()
exp = 1900
health = 50*level-5*hlevel#TO UNIVERSE BALANCE
print("Have a good journey!")
#Battle with goul
print("Oh no! There is the goul on your way!")
time.sleep(2)
print("He tries to kill you! Run away or get him down?", end="")
if input() == "Yeah, that stupid goul can't stop me!":
    print("Show him Kuskinu mat'! Good luck!")
else:
    print("Your bravery is less than zero! OK, but he's faster! You can't choose!")
goul_health=randint(1, level+1*30//hlevel)#Conditions changed to Universe balance