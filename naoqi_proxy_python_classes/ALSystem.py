#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/softbank/naoqi-sdk-2.5.5.5-linux64/include/alproxies/alsystemproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALSystem(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALSystem")

    def changePassword(self, old, new2):
        """Change the user password.

        :param str old: password The current password of the user.
        :param str new2: password The new user password.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.changePassword(old, new2)

    def diskFree(self, all):
        """Display free disk space

        :param bool all: Show all mount partions.
        :returns std::vector<AL::ALValue>: A vector with all partions' infos
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.diskFree(all)

    def freeMemory(self):
        """Amount of available memory in heap

        :returns int: amount of available memory in heap
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.freeMemory()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.ping()

    def previousSystemVersion(self):
        """Previous system version before software update (empty if this is not the 1st boot after a software update)

        :returns str: Previous system version before software update.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.previousSystemVersion()

    def reboot(self):
        """Reboot robot
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.reboot()

    def robotIcon(self):
        """Robot icon

        :returns AL::ALValue: icon of the robot
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.robotIcon()

    def robotName(self):
        """System hostname

        :returns str: name of the robot
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.robotName()

    def setRobotName(self, name):
        """Set system hostname

        :param str name: name to use
        :returns bool: whether the operation was successful
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.setRobotName(name)

    def setTimezone(self, timezone):
        """Set current timezone

        :param str timezone: timezone to use
        :returns bool: whether the operation was successful
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.setTimezone(timezone)

    def shutdown(self):
        """Shutdown robot
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.shutdown()

    def systemInfo(self):
        """Running system version

        :returns AL::ALValue: information about the system version
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.systemInfo()

    def systemVersion(self):
        """Running system version

        :returns str: running system version
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.systemVersion()

    def timezone(self):
        """Current timezone

        :returns str: current timezone
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.timezone()

    def totalMemory(self):
        """Amount of total memory in heap

        :returns int: amount of total memory in heap
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.totalMemory()

    def upgrade(self, image, checksum):
        """Change the user password.

        :param str image: Local path to a valid image.
        :param str checksum: Local path to a md5 checksum file, or empty string for no verification
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.upgrade(image, checksum)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSystem")
        return self.proxy.version()
