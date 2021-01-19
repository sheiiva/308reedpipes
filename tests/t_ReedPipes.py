############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 308reedpipes         #
#                                          #
############################################

import pytest

from sources.ReedPipes import ReedPipes
from tests.deps.expected import NORMAL_CASE_1, NORMAL_CASE_2

def test_normal_case_1(capsys):

    argv = ['./308reedpipes', '1.5', '2', '2', '2', '5', '11']

    r = ReedPipes().run(argv)
    redir = capsys.readouterr()

    assert redir.out == NORMAL_CASE_1


def test_normal_case_2(capsys):

    argv = ['./308reedpipes', '2', '3', '2', '4', '5', '13']

    r = ReedPipes().run(argv)
    redir = capsys.readouterr()

    assert redir.out == NORMAL_CASE_2
