import os

import pytest

from src.decorators import log


def test_log_file():
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_console(capsys):
    @log(filename="")
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_file_raise():
    @log(filename="mylog.txt")
    def example_function(x, y):
        raise TypeError("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(5, 100)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function TypeError: Что-то пошло не так. Inputs: (5, 100), {}\n"


def test_log_console_raise(capsys):
    @log(filename="")
    def example_function(x, y):
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError, match="Что-то пошло не так"):
        example_function(5, 100)

    captured = capsys.readouterr()

    assert captured.out == "example_function ValueError: Что-то пошло не так. Inputs: (5, 100), {}\n"
