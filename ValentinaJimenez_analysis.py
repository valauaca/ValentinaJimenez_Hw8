import numpy as np

#funcion que saca la distribucion normal, dados x, mean y sigma como parametros

def normal_dist(x,mean,sigma):

	s= np.random.normal(mean,sigma,x)

	return s

def get_fit(filename):
