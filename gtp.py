#Author: Pawel Sikora
#Date  : 03.04.2016

# argv[1] - number of how many retries to do with measurements 

import pexpect
import sys

retries = int(sys.argv[1])
command = "python2.7 /usr/bin/grabserial -v -d \"/dev/ttyUSB0\" -b 115200 -w 8 -p N -s 1 -e 60 -t" 

print ("Command used in pexpect.spawn: "+command)

while (retries > 0):
	child = pexpect.spawn(str(command), timeout=240)
	
	print("There is still "+str(retries)+" tries left...")
	print("Reset the target to start measurements...")
	child.expect(r'(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\]) Starting kernel')
	starting_kernel_time = child.match.group(2).decode("utf-8")
	print ("Time up to \'Starting Kernel\': "+starting_kernel_time)
	#child.expect(r'(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\] \[( ){0,5}([0-9]{0,2}\.[0-9]{0,8})\]) Starting logging')
	child.expect(r'(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\]) Starting logging')
	starting_linux_time = child.match.group(2).decode("utf-8")
	print ("Time up to \'Starting logging\': "+starting_linux_time)
	child.expect(r'(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\]) Welcome to')
	starting_rfs_time = child.match.group(2).decode("utf-8")
	print ("Time up to \'mounted filesystem\': "+starting_rfs_time)
	child.expect(r'(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\]) buildroot login\:')
	starting_prompt_time = child.match.group(2).decode("utf-8")
	print ("Time up to \'buildroot login:\': "+starting_prompt_time)

	fo = open("step_times_kernel_modifications", "a")
	print("Saving following time points: \""+starting_kernel_time+" "+starting_linux_time+" "+starting_rfs_time+" "+starting_prompt_time+"\" do pliku: \'"+fo.name+"\'")
	fo.write(starting_kernel_time+" "+starting_linux_time+" "+starting_rfs_time+" "+starting_prompt_time+"\r\n")
	fo.close()
	
	retries = retries - 1
	
	

