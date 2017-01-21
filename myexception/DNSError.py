#!/usr/bin/env python


class DNSNameError(Exception):
    def __init__(self, argum):
        self.__dname = argum

    def __str__(self):
        print(self.__dname)
