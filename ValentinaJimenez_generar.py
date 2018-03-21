

import numpy as np

#funcion que retorna N numeros aleatorios siguiendo la distribucion discreta de probabilidad P

def sample_1(N):
	
	b=[-10,-5,3,9]

	aleatorios=np.random.choice(b,N,p=[0.1,0.4,0.2,0.3])


	return aleatorios



#funcion que retorna N numeros aleatorios siguiendo la distribucion discreta de probabilidad exponencial con beta igual a 0.5


def sample_2(N):

	bet=0.5

	a=(bet, N)


	return a


#funcion que retorna M promedios Sn dada una funcion ejemplo

def get_mean(sampling_fun, N, M):
	lista=[]

	#ciclo para recorrer el rango de M que imprima ese numero de promedios para una funcion de prueba
	for i in range (M):

		prom=np.mean(sampling_fun(N))
		lista.append(prom)

	return lista



funciones=[sample_1, sample_2]
nombre=['sample_1','sample_2']
ns= [10,100,1000]
M=10000

for i in range (len(funciones)):


	for j in range (len(ns)):

		promedio=get_mean(funciones[i],ns[j], M)

		nom= nombre[i] + '_' + str(ns[j]) + '.txt'
		np.savetxt(nom, promedio)




	














