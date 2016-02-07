# OmegaBot
This is a project that I've been working on but it is also an open source package for others to view, build, and use.

##Usage/Purpose
The purpose of this package is to help create smarter robots that can understand their surroundings. For this, I used the Clarifai API and I created a basic wrapper in ROS to do this.

The package reads images from the kinect stream and then sends it to clarifai for processing. The results are published and can be used for anything after that. By default, the script uses the built-in ROS sound library to announce that it has found the target object (which is set to door).
You will need to put an App Id and Secret from Clarifai into the program to work.
