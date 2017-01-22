#!/usr/bin/env python

import sys
import DNS
from myexception import IPError, DNSError
from checkers import common


def __str__():
    print '''
    Checker DNS availability for Keepalived MISC_CHECK
    return 0 if DNS available and 1 if not
    '''


def main(dns_ip, name, *args):
    try:
        ip = common.checkIp(dns_ip)
    except IPError.IPValidError:
        print >> sys.stderr, IPError.IPValidError("invalid ip")
        sys.exit(1)

    try:
        dname = common.checkName(name)
    except DNSError.DNSNameError:
        print >> sys.stderr, DNSError.DNSNameError("Name not valid < 1 byte")
        sys.exit(1)

    # request=DNS.Base.DnsRequest()


if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: {0} ip name".format(sys.argv[0])
else:
    main(sys.argv[1], sys.argv[2])
