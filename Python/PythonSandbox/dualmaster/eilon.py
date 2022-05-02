import time

str="""
       eeeeeeeeeeee     llllll    iiiiii                     o o o o o         nnnnnnnnnnnnnnnnnnnnnn
       eeeeeeeeeeee     llllll    iiiiii                  o             o      nnnnnnnnnnnnnnnnnnnnnn
       eee              llllll    iiiiii                 o               o     nnnnn            nnnnn
       eee              llllll    iiiiii                o                 o    nnnnn            nnnnn
       eeeeeeeeeeee     llllll    iiiiii                o                  o   nnnnn            nnnnn
       eeeeeeeeeeee     llllll    iiiiii                o                  o   nnnnn            nnnnn
       eeeeeeeeeeee     llllll    iiiiii                o                  o   nnnnn            nnnnn
       eee              llllll    iiiiii                o                  o   nnnnn            nnnnn
       eee              llllll    iiiiii                o                 o    nnnnn            nnnnn
       eeeeeeeeeeee     llllll    iiiiiiiiiiiiiiiiii     o               o     nnnnn            nnnnn
       eeeeeeeeeeee     llllll    iiiiiiiiiiiiiiiiii       o  o o o o o        nnnnn            nnnnn
"""

for i in str:
  print(i, end="")
  time.sleep(0.0003)
