import numpy as np
from numpy import interp
from neuron import neuron
import random
from recep_field import rf
import imageio
import math

def encode_deterministic(pot):
	#defining time frame of 1s with steps of 5ms
	T = 200;
	#initializing spike train
	train = []

	for l in range(16):
		for m in range(16):
			temp = np.zeros([(T+1),])
			#calculating firing rate proportional to the membrane potential
			freq = interp(pot[l][m], [-2,5], [1,20])
			# print freq
			if freq>0:
				freq1 = math.ceil(T/freq)
				#generating spikes according to the firing rate
				k = freq1
				while k<(T+1):
					temp[int(k)] = 1
					k = k + freq1
			train.append(temp)
			# print sum(temp)
	return train

if __name__  == '__main__':
	m = []
	n = []
	img = imageio.imread("../images/100.png")
	pot = rf(img)
	train = encode_deterministic(pot)
	# print train
