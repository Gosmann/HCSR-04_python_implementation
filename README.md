# HCSR-04 python implementation

How to implement a program in python to use the (extremely popular) HCSR-04 ultrassonic sensor. 

The aim of this repository is implementing a python solution to use the HCSR sensor along with a raspberry pi in a dynamic and reliable way. The problem seen in most usual implementations are ineffective (due to pooling method) and not reliable (due to waiting while loops) codes. This way, I considered necessary implementing a solution that solved this problems. In order to do that, I used the (extremely awesome) pigpio library, whitch can be accessed trough this link: http://abyz.co.uk/rpi/pigpio/python.html

The solution consists in two codes, they are basically self-explanatory through the comments and consist on a class implementation (so as to guarantee it will be able to work in general applications) and the program that calls this class. Not much more to say, take a look at the code and feel free to fork!
