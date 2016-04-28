#Author: Pawel Sikora
#Date  : 03.04.2016

# argv[1] - number of how many retries to do with measurements 

import pexpect
import sys

command = "python2.7 /usr/bin/grabserial -v -d \"/dev/ttyUSB0\" -b 115200 -w 8 -p N -s 1 -e 60 -t" 
two_time_brackets = "(\[([0-9]{0,2}\.[0-9]{0,8}) ([0-9]{0,2}\.[0-9]{0,8})\])" 


class Nowa:
	def expect_pattern(child, string):
		child.expect(string)
		return child 
	def match(self, child):
		self.var = child.match.group(2).decode("utf-8")
		return child	
	def safe_points_to_file(self, string):
		fo = open(string, "a")
		print("Saving following time points: \""+starting_kernel_time+" "+starting_linux_time+" "+starting_rfs_time+" "+starting_prompt_time+"\" do pliku: \'"+fo.name+"\'")
		fo.write(starting_kernel_time+" "+starting_linux_time+" "+starting_rfs_time+" "+starting_prompt_time+"\r\n")
		fo.close()
	def catch_line_with_string(self, string, child):
		child.expect(str(two_time_brackets) + " " + string)
		child = self.match(child)
		print ("Time up to " + string + " " +self.var)
		return child
	
	def measure(self):	
		retries = int(sys.argv[1])
		
		print ("Command used in pexpect.spawn: "+command)
		child = pexpect.spawn(str(command), timeout=240)
		
		while (retries > 0):	
			print("There is still "+str(retries)+" tries left...")
			print("Reset the target to start measurements...")
			child = self.catch_line_with_string("Starting kernel", child) 
			child = self.catch_line_with_string("Starting logging", child))
			child = self.catch_line_with_string("Welcome to", child))
			child = self.catch_line_with_string("buildroot login", child))
			safe_points_to_file(str("nowy_plik"))
			retries = retries - 1
	

main = Nowa()
main.measure()


