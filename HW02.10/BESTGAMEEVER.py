import time
print("Select your level:",end="")
level = int(input())
easterneggs = 0
if level>10:
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
#FIRST BATTLE
print("Have a good journey!")
time.sleep(3)
print("Oh no! There is the goul on your way!")
time.sleep(2)
print("He tries to kill you! Run away or get him down?", end="")
if input() == "Yeah, that stupid goul can't stop me!":
    print("Show him Kuskinu mat'! Good luck!")
else:
    print("Your bravery is less than zero! OK, but he's faster! You can't choose!")
