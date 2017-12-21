import os
import time

os.system('iptables -A INPUT')
os.system('iptables -Z')
fout = open('net_data.txt', 'w')
init_time = time.time()

os.system('iptables -vxn -L | awk \'{print $7}\' >> throughput.txt')
f = open('throughput.txt', 'r')
old1 = int(f.readline())

ff = open('throughput.txt', 'w')
time.sleep(1)

for i in range(200):
	curr_time = time.time()
	os.system('iptables -vxn -L | awk \'{print $7}\' >> throughput.txt')
	f = open('throughput.txt', 'r')
	input1 = int(f.readline())
	print(input1)

	delta1 = float(input1 - old1)
	old1 = input1

	fout.write(str(round(curr_time - init_time, 3)) + '\t' + str(round(delta1 / 1024 ** 2, 3)) + '\n')

	ff = open('throughput.txt', 'w')
	
	time.sleep(1)
