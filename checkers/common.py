#!/usr/bin/env python

import re
from myexception import DNSError, IPError


def checkIp(ip):
    if len(ip) < 7:  # len 7 == 1.1.1.1
        raise IPError.IPValidError("invalid IP address")

    regexp = re.search('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip)
    if regexp is not None:
        return regexp.group(0)
    else:
        raise IPError("invalid IP address")


def checkName(name):
    if len(name) <= 1:
        raise DNSError.DNSNameError("invalid DNS name")
