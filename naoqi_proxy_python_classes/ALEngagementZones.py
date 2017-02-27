#!/usr/bin/env python
# Class autogenerated from ./alengagementzonesproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALEngagementZones(object):
    def __init__(self):
        self.proxy = ALProxy("ALEngagementZones")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def computeEngagementZone(self, x, y, z):
        """Computes the engagement zone in which an object is from its position in FRAME_ROBOT

        :param float x: X coordinate of the object in FRAME_ROBOT
        :param float y: Y coordinate of the object in FRAME_ROBOT
        :param float z: Z coordinate of the object in FRAME_ROBOT
        :returns int: Engagement zone of the object
        """
        return self.proxy.computeEngagementZone(x, y, z)

    def computeEngagementZone(self, xAngle, yAngle, distance, cameraPositionRobot):
        """Computes the engagement zone in which an object is from its anglular position in the camera image, its distance from the robot, and the position of the camera in FRAME_ROBOT

        :param float xAngle: X angular coordinate of the object in the image
        :param float yAngle: Y angular coordinate of the object in the image
        :param float distance: distance of the object from the robot
        :param AL::ALValue cameraPositionRobot: camera position in FRAME_ROBOT
        :returns int: Engagement zone of the object
        """
        return self.proxy.computeEngagementZone(xAngle, yAngle, distance, cameraPositionRobot)

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getCurrentPeriod()

    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        return self.proxy.getCurrentPrecision()

    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getEventList()

    def getFirstLimitDistance(self):
        """Get the first distance used for the delimitation of the engagement zones (nearest limit)

        :returns float: Current first distance (in meters) used for delimitation (nearest limit)
        """
        return self.proxy.getFirstLimitDistance()

    def getLimitAngle(self):
        """Get the angle used for the delimitation of the engagement zones

        :returns float: Current angle used for delimitation
        """
        return self.proxy.getLimitAngle()

    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getMemoryKeyList()

    def getMethodHelp(self, methodName):
        """Retrieves a method's description.

        :param str methodName: The name of the method.
        :returns AL::ALValue: A structure containing the method's description.
        """
        return self.proxy.getMethodHelp(methodName)

    def getMethodList(self):
        """Retrieves the module's method list.

        :returns std::vector<std::string>: An array of method names.
        """
        return self.proxy.getMethodList()

    def getModuleHelp(self):
        """Retrieves the module's description.

        :returns AL::ALValue: A structure describing the module.
        """
        return self.proxy.getModuleHelp()

    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getMyPeriod(name)

    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        return self.proxy.getMyPrecision(name)

    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        return self.proxy.getOutputNames()

    def getSecondLimitDistance(self):
        """Get the second distance used for the delimitation of the engagement zones (furthest limit)

        :returns float: Current second distance (in meters) used for delimitation (furthest limit)
        """
        return self.proxy.getSecondLimitDistance()

    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        return self.proxy.getSubscribersInfo()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def isPaused(self):
        """Gets extractor pause status

        :returns bool: True if the extractor is paused, False if not
        """
        return self.proxy.isPaused()

    def isProcessing(self):
        """Gets extractor running status

        :returns bool: True if the extractor is currently processing images, False if not
        """
        return self.proxy.isProcessing()

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def pause(self, status):
        """Changes the pause status of the extractor

        :param bool status: New pause satus
        """
        return self.proxy.pause(status)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def setFirstLimitDistance(self, distance):
        """Set the first distance used for the delimitation of the engagement zones (nearest limit)

        :param float distance: New first distance (in meters) for delimitation (nearest limit), it should be positive and smaller than the second distance
        """
        return self.proxy.setFirstLimitDistance(distance)

    def setLimitAngle(self, angle):
        """Set the angle used for the delimitation of the engagement zones

        :param float angle: New angle (in degrees) for delimitation, it should be below 180
        """
        return self.proxy.setLimitAngle(angle)

    def setSecondLimitDistance(self, distance):
        """Set the second distance used for the delimitation of the engagement zones (furthest limit)

        :param float distance: New second distance (in meters) for delimitation (furthest limit), it should be positive and bigger than the first distance
        """
        return self.proxy.setSecondLimitDistance(distance)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        return self.proxy.subscribe(name, period, precision)

    def subscribe(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        return self.proxy.subscribe(name)

    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        return self.proxy.unsubscribe(name)

    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        return self.proxy.updatePeriod(name, period)

    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        return self.proxy.updatePrecision(name, precision)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()

    def wait(self, id, timeoutPeriod):
        """Wait for the end of a long running method that was called using 'post'

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :param int timeoutPeriod: The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
        :returns bool: True if the timeout period terminated. False if the method returned.
        """
        return self.proxy.wait(id, timeoutPeriod)