#!/usr/bin/env python3

import random
data = ""
with open("/path/to/output.txt", "w") as game:
        for _ in range(10000):
            """
            If you wanna mix things up a bit

            rand = random.randint(0,1)
            if (rand < .33):
                data += "2\n0\n1\n1\n0\n1\n"
            elif (rand < .67):
                data += "1\n0\n0\n2\n2\n1\n"
            else:
                data += "0\n2\n0\n0\n1\n2\n"
            """
            data += "2\n0\n1\n1\n0\n1\n"
        game.write(data)
        game.write("5\nNo\n")

#piping format is: python /path/to/bot.py < /path/to/output.txt
