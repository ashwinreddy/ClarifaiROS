#!/usr/bin/env python
import rospy
from classifier import Classifier
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from omega.msg import TagList
from geometry_msgs.msg import Twist
from sound_play.libsoundplay import SoundClient
class Main():
	def __init__(self, target):
		self.classifier = Classifier(app_id='', app_secret='')
		rospy.init_node('main', anonymous=False)
		self.target = target
		rospy.on_shutdown(self.shutdown)
		self.sound = SoundClient()
		rospy.Subscriber("/camera/rgb/image_rect_color", Image, self.kinectInput)
		self.publisher = rospy.Publisher('results', TagList, queue_size=10)

	def kinectInput(self, img):
		cv2.imwrite('lki.jpg', CvBridge().imgmsg_to_cv2(img, 'bgr8'))
		self.results = self.classifier.tag(open('lki.jpg'))
		resultMsg = TagList()
		resultMsg.tags  = self.results
		self.publisher.publish(resultMsg)
		if self.target in self.results:
			rospy.sleep(1)
			r = rospy.Rate(10)
			self.sound.say('I found the {0}'.format(self.target))
			
	def shutdown(self):
		rospy.loginfo("stopping")

if __name__ == "__main__":
	while not rospy.is_shutdown():
		Main('door')
		rospy.spin()
