import pigpio
import time

class hcsr:

	def __init__(self, pi, trig, echo):
		self.pi = pi
		self.trig = trig
		self.echo = echo
		self._cb = None
		self._tick = 0
		self._micros = 0

		# setup
		pi.set_mode(self.trig, pigpio.OUTPUT)
		pi.set_mode(self.echo, pigpio.INPUT)
		# actions
		pi.write(self.trig, 0)

		self._cb = pi.callback(self.echo, pigpio.EITHER_EDGE, self._cbf)
		#pi.gpio_trigger(self.trig, 10, 1)

	def _cbf(self, gpio, level, tick):
		if level == 1:
			self._tick = tick
			#print("level == 1")
			#print(tick)

		elif level == 0:
			diff = pigpio.tickDiff(self._tick, tick)
			self._micros = diff
			#print("level == 2")
			#print(diff)

	def get_distance(self, pi):
		pi = pigpio.pi()
		pi.gpio_trigger(self.trig, 10, 1)
		pi.stop()

		time_elapsed = self._micros
		distance = (time_elapsed*0.034300)/2

		#print distance
		return distance
