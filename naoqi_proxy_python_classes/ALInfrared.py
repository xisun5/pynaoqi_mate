#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/softbank/naoqi-sdk-2.5.5.5-linux64/include/alproxies/alinfraredproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALInfrared(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALInfrared")

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALInfrared")
        return self.proxy.ping()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALInfrared")
        return self.proxy.version()
