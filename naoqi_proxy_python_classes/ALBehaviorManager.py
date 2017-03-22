#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/softbank/naoqi-sdk-2.5.5.5-linux64/include/alproxies/albehaviormanagerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALBehaviorManager(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALBehaviorManager")

    def addDefaultBehavior(self, behavior):
        """Set the given behavior as default

        :param str behavior: Behavior name
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.addDefaultBehavior(behavior)

    def getBehaviorNames(self):
        """Get behaviors

        :returns std::vector<std::string>: Returns the list of behaviors prefixed by their type (User/ or System/). DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getBehaviorNames()

    def getBehaviorNature(self, behavior):
        """Get the nature of the given behavior.

        :param str behavior: The local path towards a behavior or a directory.
        :returns str: The nature of the behavior.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getBehaviorNature(behavior)

    def getBehaviorTags(self, behavior):
        """Get tags found on the given behavior.

        :param str behavior: The local path towards a behavior or a directory.
        :returns std::vector<std::string>: The list of tags found.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getBehaviorTags(behavior)

    def getBehaviorsByTag(self, tag):
        """Get installed behaviors directories names and filter it by tag.

        :param str tag: A tag to filter the list with.
        :returns std::vector<std::string>: Returns the behaviors list
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getBehaviorsByTag(tag)

    def getDefaultBehaviors(self):
        """Get default behaviors

        :returns std::vector<std::string>: Return default behaviors
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getDefaultBehaviors()

    def getInstalledBehaviors(self):
        """Get installed behaviors directories names

        :returns std::vector<std::string>: Returns the behaviors list
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getInstalledBehaviors()

    def getLoadedBehaviors(self):
        """Get loaded behaviors

        :returns std::vector<std::string>: Return loaded behaviors
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getLoadedBehaviors()

    def getRunningBehaviors(self):
        """Get running behaviors

        :returns std::vector<std::string>: Return running behaviors
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getRunningBehaviors()

    def getSystemBehaviorNames(self):
        """Get system behaviors

        :returns std::vector<std::string>: Returns the list of system behaviors prefixed by System/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getSystemBehaviorNames()

    def getTagList(self):
        """Get tags found on installed behaviors.

        :returns std::vector<std::string>: The list of tags found.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getTagList()

    def getUserBehaviorNames(self):
        """Get user's behaviors

        :returns std::vector<std::string>: Returns the list of user's behaviors prefixed by User/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.getUserBehaviorNames()

    def installBehavior(self, localPath):
        """Install a behavior. Check the given local path for a valid behavior or package. On success, behavior added or updated signal is emitted. DEPRECATED in favor of PackageManager.install.

        :param str localPath: the relative destination path.
        :returns bool: true on success, false on failure.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.installBehavior(localPath)

    def installBehavior2(self, absolutePath, localPath, overwrite):
        """Install a behavior. Check and take the behavior found at the given absolute path andimport it to the given local path, relative to behaviors path. On success, behavior added signal is emitted before returning.DEPRECATED in favor of PackageManager.install.

        :param str absolutePath: a behavior on the local file system to install.
        :param str localPath: the relative destination path.
        :param bool overwrite: whether to replace existing behavior if present.
        :returns bool: true on success, false on failure.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.installBehavior(absolutePath, localPath, overwrite)

    def isBehaviorInstalled(self, name):
        """Tell if supplied name corresponds to a behavior that has been installed

        :param str name: The behavior directory name
        :returns bool: Returns true if it is a valid behavior
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.isBehaviorInstalled(name)

    def isBehaviorLoaded(self, behavior):
        """Tell if supplied name corresponds to a loaded behavior

        :param str behavior: Behavior name
        :returns bool: Returns true if it is a loaded behavior
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.isBehaviorLoaded(behavior)

    def isBehaviorPresent(self, prefixedBehavior):
        """Tell if the supplied namecorresponds to an existing behavior.

        :param str prefixedBehavior: Prefixed behavior or just behavior's name (latter usage deprecated, in this case the behavior is searched for amongst user's behaviors, then in system behaviors) DEPRECATED in favor of ALBehaviorManager.isBehaviorInstalled.
        :returns bool: Returns true if it is an existing behavior
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.isBehaviorPresent(prefixedBehavior)

    def isBehaviorRunning(self, behavior):
        """Tell if supplied name corresponds to a running behavior

        :param str behavior: Behavior name
        :returns bool: Returns true if it is a running behavior
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.isBehaviorRunning(behavior)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.ping()

    def playDefaultProject(self):
        """Play default behaviors
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.playDefaultProject()

    def preloadBehavior(self, behavior):
        """Load a behavior

        :param str behavior: Behavior name
        :returns bool: Returns true if it was successfully loaded.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.preloadBehavior(behavior)

    def removeBehavior(self, behavior):
        """Remove a behavior from the filesystem. DEPRECATED in favor of PackageManager.remove.

        :param str behavior: Behavior name
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.removeBehavior(behavior)

    def removeDefaultBehavior(self, behavior):
        """Remove the given behavior from the default behaviors

        :param str behavior: Behavior name
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.removeDefaultBehavior(behavior)

    def resolveBehaviorName(self, name):
        """Find out the actual <package>/<behavior> path behind a behavior name.

        :param str name: name of a behavior
        :returns str: The actual <package>/<behavior> path if found, else an empty string. Throws an ALERROR if two behavior names conflicted.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.resolveBehaviorName(name)

    def runBehavior(self, behavior):
        """Runs a behavior, returns when finished

        :param str behavior: Behavior name
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.runBehavior(behavior)

    def startBehavior(self, behavior):
        """Starts a behavior, returns when started.

        :param str behavior: Behavior name
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.startBehavior(behavior)

    def stopAllBehaviors(self):
        """Stop all behaviors
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.stopAllBehaviors()

    def stopBehavior(self, behavior):
        """Stop a behavior

        :param str behavior: Behavior name
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.stopBehavior(behavior)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALBehaviorManager")
        return self.proxy.version()
