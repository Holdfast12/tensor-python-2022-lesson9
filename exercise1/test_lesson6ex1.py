#!/usr/bin/python3
import lesson6ex1


def test_strinbyte_1234567890():
    assert lesson6ex1.strinbyte(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']) == [b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'0']