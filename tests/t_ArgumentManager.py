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

from sources.ArgumentManager import ArgumentManager


def test_normal_case():

    argMan = ArgumentManager()

    argv = ['./308reedpipes', '1.5', '2', '2', '2', '5', '11']

    assert argMan.checkArgs(argv) != 84


def test_wrong_number_args(capsys):

    argMan = ArgumentManager()

    argv = ['./308reedpipes', '2', '2', '2', '5', '11']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == 'ERROR: wrong number of arguments.\n'


def test_not_a_digit(capsys):

    argMan = ArgumentManager()

    argv = ['./308reedpipes', 'a', '2', '2', '2', '5', '11']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == 'ERROR: a not a digit.\n'


def test_last_float(capsys):

    argMan = ArgumentManager()

    argv = ['./308reedpipes', '1.0', '2', '2', '2', '5', '2.3']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == 'ERROR: 2.3 not an integer.\n'


def test_negative_arg(capsys):

    argMan = ArgumentManager()

    argv = ['./308reedpipes', '-3.0', '2', '2', '2', '5', '11']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == 'ERROR: -3.0 is negative.\n'


def test_needHelp_h():

    argMan = ArgumentManager()

    argv = ['./303make', '-h']

    assert argMan.needHelp(argv) is True


def test_needHelp_help():

    argMan = ArgumentManager()

    argv = ['./303make', '--help']

    assert argMan.needHelp(argv) is True


def test_needHelp_wrong_case():

    argMan = ArgumentManager()

    argv = ['./303make', 'no']

    assert argMan.needHelp(argv) is False
