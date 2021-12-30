import time

str="""
      o o o o o             FFFFFFFFFFFFFF       ____        RRRRR
   o             o          FFFFFFFFFFFFFF     /     \       RRRRR
  o               o         FFFF              |       |      RRRRRRRRRRRRRRRRR
 o                 o            FFFF               \_____/       RRRRRRRRRRRRRRRRR
 o                  o       FFFF                IIIII        RRRRR          RRR
 o                  o   FFFFFFFFFFFFFF          IIIII        RRRRR           RRR
 o                  o   FFFFFFFFFFFFFF          IIIII        RRRRR
 o                  o       FFFF                IIIII        RRRRR
 o                 o        FFFF                IIIII        RRRRR
  o               o         FFFF                IIIII        RRRRR
    o  o o o o o            FFFF                IIIII        RRRRR
                            FFFF                IIIII        RRRRR
"""

for i in str:
    print(i, end="")
    time.sleep(0.003)