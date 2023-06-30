#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path

def rm(filename):
    os.remove(filename)

# Add Validation to rm
# The rm method defined earlier is quite oversimplified. We’d like to have it validate that a path exists and is a file before just blindly attempting to remove it. Let’s refactor rm to be a bit smarter:

def rm_smarter(filename):
    if os.path.isfile(filename):
        os.remove(filename)


# File-Removal as a Service with Python's Mock Patch

class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)


