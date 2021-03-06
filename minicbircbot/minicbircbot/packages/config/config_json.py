# -*- coding: utf-8 -*-
import os
import sys
import json
import copy, base64
from base64 import b64encode, b64decode
from copy import copy
from  io import StringIO
import logging
import zlib

logger = logging.getLogger(__name__)



#yes overhead everywere but i dont care. it just load  small pieces of code
#nothing important  impact is almost zero. uncompressing a zip has  more overhead than this code
#kthx bye


class ConfigJson(object):
	""" Class to read and parse json config """
	DEFAULT_OPTS = {

					'address' : 'irc.falai.org',
					'port' : 6667,
					'chans': '#python',
					'nickname' : 'mrTest',
					'identd' : 'HUE',
					'console' : False,
					'modules' : []
					

					}


	def __init__(self,cfg, use_base64 = True):
		self.cfg_path = cfg
		self.opts = {}
		self.usebase64  = use_base64



	def setDefaultOpts(self, key, value):
		if not key or not value:
			return False

		# to do not overwriting existent  config  she should not allow  insertion if already exists
		if not key  in self.opts:
			self.opts[key] = value
			logger.info("Key {0}:{1} added".format(key, value))

		else:
			logger.info("Key {0} already exists".format(key))

	
	def encode(self,str):
		return b64encode(str)

	def decode(self, str):
		return b64decode(str)

	def load(self):
		
		try:
			logging.info("Tried to load CFG")
			with open(self.cfg_path, mode="r", encoding="utf-8") as f:
				


				cfg = json.load(f)

	
				self.opts = copy(cfg)
				#logger.warning("READING:  {0}".format(self.opts) )

		except Exception as ex:
				
				
				with open(self.cfg_path, mode="w", encoding="utf-8") as f:
						
						default_opts = copy(self.DEFAULT_OPTS)

						#sorting keys will mess your config if you  wrote in manully 
						#its better off
						
						json.dump(default_opts, f, indent=4, sort_keys=False)
						#self.opts.clear()
						self.opts = copy(default_opts)
						#logger.warning("WRITING:  {0}".format(data) )
					
						

	def save(self):

		with open(self.cfg_path, mode="w", encoding="utf-8") as f:



			json.dump(self.opts, f, indent=4, sort_keys=True)
			logging.info("CFG Saved")
			


	
	def edit(self, key, value):



		if not key and not value:
			return False

		old_key = key
		old_value = value

		if  not key in self.opts:
			logger.warning("Config Key:{0} doesnt exists".format(key))
			return False
		else:
			self.opts[key] = value
			logging.info("Key {0}:{1} was modified to {2}:{3}".format(old_key,old_value, key, value))
			return True

		return False






	def get(self, key):

		if not key:
			return None
		
		if  not key in self.opts:
			logger.warning("Config Key: {0} doesnt exists. if required. please add them manully".format(key))
			return None

		else:
			return self.opts[key]

		return None