############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 308reedpipes         #
#                                          #
############################################


class ReedPipes():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        # Resolved linear system’s vector result
        self._vector = [0.0, 0.0, 0.0, 0.0, 0.0]
        # Radius (in cm) of pipe at the [0, 5, 10, 15, 20]cm abscissa
        self._rs = []
        # Number of points needed to display the radius
        self._n = 0

    def parse(self, argv: list) -> None:

        self._rs = [float(arg) for arg in argv[1:6]]
        self._n = int(argv[-1])

    def compute(self) -> list:

        def mean(maxi: int, total: int, index: int) -> float:
            return maxi / total * index

        def spline(imean: int, rs: list, vector: list) -> float:

            ab = [x for x in range(0, 25, 5)]
            i = int(imean/len(ab)) + 1 if imean != 20 else 4

            return  - vector[i-1]/30 * (imean - ab[i])**3\
                    + vector[i]/30 * (imean - ab[i-1])**3\
                    - (rs[i-1]/5 - 5/6 * vector[i-1]) * (imean - ab[i])\
                    + (rs[i]/5 - 5/6 * vector[i]) * (imean - ab[i-1])

        data = []

        A = 6 * (self._rs[2] - 2 * self._rs[1] + self._rs[0]) / 50
        B = 6 * (self._rs[3] - 2 * self._rs[2] + self._rs[1]) / 50
        C = 6 * (self._rs[4] - 2 * self._rs[3] + self._rs[2]) / 50
        self._vector[2] = (B -(A + C) / 4) * 4 / 7
        self._vector[3] = C / 2 - 0.25 * self._vector[2] ## SIMPLIFY
        self._vector[1] = A / 2 - 0.25 * self._vector[2] ## SIMPLIFY

        for i in range(self._n):
            imean = mean(20, self._n-1, i) if i < self._n-1 else 20
            data.append({'abscissa': imean,
                        'radius': spline(imean, self._rs, self._vector)})

        return data

    def printResult(self, data: list) -> None:

        # Format in case of -0.0 to 0.0
        self._vector = [-x if -0.1<x<0 else x for x in self._vector]
        # Print resolved linear system’s vector result
        print("vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(
            self._vector[0], self._vector[1], self._vector[2], self._vector[3], self._vector[4]
        ))
        #
        for i in range(self._n):
            print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(
                data[i]['abscissa'], data[i]['radius']
            ))

    def run(self, argv: list) -> None:

        """
        Run computations and process output printing.
        """

        self.parse(argv)
        data = self.compute()
        self.printResult(data)