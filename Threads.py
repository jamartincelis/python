"""import threading
class MiThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	
	def run(self):
		print "Soy el hilo", self.num

print "Soy el hilo principal"
for i in range(0, 10):
	t = MiThread(i)
	t.start()
	t.join()
"""

import threading
def imprime(num):
	print "Soy el hilo", num

print "Soy el hilo principal "
for i in range(0, 10):
	t = threading.Thread(target=imprime, args=(i, ))
	t.start()	