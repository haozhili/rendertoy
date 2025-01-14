#!coding=utf-8
import base
import camera.cameraobj as cameraobj
from .defines import *

class CMgr(object):
	__metaclass__ = base.Singleton

	m_dType2Camera = {
		TYPE_NORMAL: cameraobj.CUVNCamera()
	}

	def GetCamera(self, iType):
		return self.m_dType2Camera.get(iType)