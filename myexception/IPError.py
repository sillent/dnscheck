#!/usr/bin/env python


class IPValidError(Exception):
    def __init__(self, argum):
        self.__value = argum

    def __str__(self):
        print(self.__value)
