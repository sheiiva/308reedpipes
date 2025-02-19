############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 308reedpipes         #
#                                          #
############################################

from sources.utils import isFloat, isInt

class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        if len(argv) != 7:
            print('ERROR: wrong number of arguments.')
            return 84
        for arg in argv[1:]:
            if isFloat(arg) is False:
                print(f'ERROR: {arg} not a digit.')
                return 84
            elif float(arg) <= 0:
                print(f'ERROR: {float(arg)} is negative.')
                return 84
        if isInt(argv[-1]) is False or int(argv[-1]) <= 0:
            print(f'ERROR: {argv[-1]} not an integer.')
            return 84


    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
