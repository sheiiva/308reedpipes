############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 308reedpipes         #
#                                          #
############################################


def isFloat(var) -> bool:
    try:
        float(var)
    except ValueError:
        return False
    else:
        return True


def isInt(var) -> bool:
    try:
        int(var)
    except ValueError:
        return False
    else:
        return True
