#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/softbank/naoqi-sdk-2.5.5.5-linux64/include/alproxies/alcolorblobdetectionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALColorBlobDetection(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALColorBlobDetection")

    def getActiveCamera(self):
        """Gets extractor active camera

        :returns int: Id of the current active camera of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getActiveCamera()

    def getAutoExposure(self):
        """Get the camera auto exposure mode

        :returns bool: A flag saying the exposure is auto or not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getAutoExposure()

    def getCircle(self):
        """Send back the x,y,radius of the circle if any

        :returns AL::ALValue: The circle as x,y,radius in image relative coordinates (x,radius divided by rows and y by cols)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getCircle()

    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getCurrentPeriod()

    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getCurrentPrecision()

    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getEventList()

    def getFrameRate(self):
        """Gets extractor framerate

        :returns int: Current value of the framerate of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getFrameRate()

    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getMemoryKeyList()

    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getMyPeriod(name)

    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getMyPrecision(name)

    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getOutputNames()

    def getResolution(self):
        """Gets extractor resolution

        :returns int: Current value of the resolution of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getResolution()

    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.getSubscribersInfo()

    def isPaused(self):
        """Gets extractor pause status

        :returns bool: True if the extractor is paused, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.isPaused()

    def isProcessing(self):
        """Gets extractor running status

        :returns bool: True if the extractor is currently processing images, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.isProcessing()

    def pause(self, paused):
        """Changes the pause status of the extractor

        :param bool paused: New pause satus
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.pause(paused)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.ping()

    def setActiveCamera(self, cameraId):
        """Sets extractor active camera

        :param int cameraId: Id of the camera that will become the active camera
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setActiveCamera(cameraId)

    def setAutoExposure(self, mode):
        """Set the camera auto exposure to on

        :param bool mode: Whether the exposure is auto or not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setAutoExposure(mode)

    def setColor(self, r, g, b, colorThres):
        """Color parameter setting

        :param int r: The R component in RGB of the color to find
        :param int g: The G component in RGB of the color to find
        :param int b: The B component in RGB of the color to find
        :param int colorThres: The color threshold
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setColor(r, g, b, colorThres)

    def setFrameRate(self, subscriberName, framerate):
        """Sets the extractor framerate for a chosen subscriber

        :param str subscriberName: Name of the subcriber
        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setFrameRate(subscriberName, framerate)

    def setFrameRate2(self, framerate):
        """Sets the extractor framerate for all the subscribers

        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setFrameRate(framerate)

    def setObjectProperties(self, minSize, span):
        """Object parameter setting

        :param int minSize: The minimum size of the cluster to find
        :param float span: The span of the object in meters
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setObjectProperties(minSize, span)

    def setObjectProperties2(self, minSize, span, shape):
        """Object parameter setting

        :param int minSize: The minimum size of the cluster to find
        :param float span: The span of the object in meters
        :param str shape: The shape of the object
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setObjectProperties(minSize, span, shape)

    def setParameter(self, paramName, value):
        """DEPRECATED: Sets pause and resolution

        :param str paramName: Name of the parameter to set
        :param AL::ALValue value: New value
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setParameter(paramName, value)

    def setResolution(self, resolution):
        """Sets extractor resolution

        :param int resolution: New resolution
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.setResolution(resolution)

    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.subscribe(name, period, precision)

    def subscribe2(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.subscribe(name)

    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.unsubscribe(name)

    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.updatePeriod(name, period)

    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.updatePrecision(name, precision)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALColorBlobDetection")
        return self.proxy.version()
