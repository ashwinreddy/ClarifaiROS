from clarifai.client import ClarifaiApi
import os
class Classifier():
	def __init__(self, **kargs):
		os.environ['CLARIFAI_APP_ID']=kargs['app_id']
		os.environ['CLARIFAI_APP_SECRET']=kargs['app_secret']
		self.cfa = ClarifaiApi()

	def tag(self, data):
		result 	= self.cfa.tag_images(data)['results'][0]['result']['tag']['classes']
		return result
