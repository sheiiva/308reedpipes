#!/usr/bin/env python3
############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 308reedpipes         #
#                                          #
############################################


from sys import argv

from sources.Usage import Usage
from sources.ArgumentManager import ArgumentManager
from sources.ReedPipes import ReedPipes


def main():

    argsManager = ArgumentManager()

    if argsManager.needHelp(argv):
        Usage()
    elif argsManager.checkArgs(argv) == 84:
        exit(84)
    else:
        ReedPipes().run(argv)


if __name__ == "__main__":
    main()
