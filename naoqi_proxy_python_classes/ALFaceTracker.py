#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/softbank/naoqi-sdk-2.5.5.5-linux64/include/alproxies/alfacetrackerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALFaceTracker(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALFaceTracker")

    def getPosition(self):
        """Return the [x, y, z] position of the face in FRAME_TORSO. This is done assuming an average face size, so it might not be very accurate.  This invalidates the isNewData field of the tracker. See isNewData()) for more details.

        :returns std::vector<float>: An Array containing the face position [x, y, z].
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.getPosition()

    def isActive(self):
        """Return true if the face Tracker is running.

        :returns bool: true if the face Tracker is running.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.isActive()

    def isNewData(self):
        """Return true if a new face was detected since the last getPosition().

        :returns bool: true if a new face was detected since the last getPosition().
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.isNewData()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.ping()

    def setWholeBodyOn(self, pWholeBodyOn):
        """if true, the tracking will be through a Whole Body Process.

        :param bool pWholeBodyOn: The whole Body state
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.setWholeBodyOn(pWholeBodyOn)

    def startTracker(self):
        """Start the tracker by Subscribing to Event FaceDetected from ALFaceDetection module. Then Wait Event FaceDetected from ALFaceDetection module. And finally send information to motion for head tracking. NOTE: Stiffness of Head must be set to 1.0 to move!
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.startTracker()

    def stopTracker(self):
        """Stop the tracker by Unsubscribing to Event FaceDetected from ALFaceDetection module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.stopTracker()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker")
        return self.proxy.version()
