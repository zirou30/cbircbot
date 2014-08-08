import sys, os
import json


class Config(object):
	
	DEFAULT_OPTS = {
				
				"server":"irc.lazy.org",
				"port":"6667",
				"nick":"joaoaranha",
				"modules": "*",
				"channels": "#python;#brasil",
				
				
				}
	
	
	def __init__(self, *args, **kwargs):
		self.option = {}
        
	def add(self, key, value):
		
		if key != '' and value != '':
			self.option[key] = value  
	
	def save(self):
		
		with open("config.cfg", "wb") as f:
			json.dump(self.option,f)
			
	def defaultKeys(self):
		
		self.option.clear()
		self.option = self.DEFAULT_OPTS
		
		self.save()
		self.open()
		
	
	def open(self):
		
		try:
			with open("config.cfg","rb") as fb:
				self.option.clear()
				self.option = json.load(fb)
				self.parse(self.option) 
		except:
			with open("config.cfg", "wb") as fb:
				self.defaultKeys()
		
	def parse(self, list): #for debug purposes cause  did methos is useless 
		for i in list.keys():
			if i  in self.DEFAULT_OPTS:
				pass
				#print "{0} is valid".format(i)
			else:
				pass
				#print "{0} invalid command ".format(i)
		
			
	def __str__(self):
		
		for c in  self.option.keys():
			print "{0}->{1}".format(c,self.option[c])
		
		
c = Config()
c.open()