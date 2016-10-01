import sys
import os
import time
from ctypes import windll, create_string_buffer;
import struct;


"""
 _____    ____   _____    ____    _    _ 
|___  |  |  __| |  _  |  / __ \  | \  / |
   /  /  | |__  | |_| | | |  | |  \ \/ / 
  /  /   |  __| |    /  | |  | |   >  <  
 /  /__  | |__  | |\ \  | |__| |  / /\ \ 
|_____|  |____| |_| \_\  \____/  |_/  \_|
"""
"""
*
* animate.py
* Version - 1.0
* Licensed under the MIT license - http://opensource.org/licenses/MIT
*
* Copyright (c) 2016 Nguyen Viet Hung
*
"""

DURATION       = 1; #The default time for animation duration is 1 sec
CONSOLE_HEIGHT = 0;
CONSOLE_WIDTH  = 0;

h = windll.kernel32.GetStdHandle(-12);
csbi = create_string_buffer(22);
res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi);
if res:
    (bufx, bufy, curx, cury, wattr,left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    CONSOLE_WIDTH  = right - left + 1;
    CONSOLE_HEIGHT = bottom - top + 1;
else:
    CONSOLE_WIDTH  = 80;
    CONSOLE_HEIGHT = 25;

##################################################

"""
Special effect =))
"""

#[1]: Typing text
def Typing(text,**kwargs):
	d = 0;
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	else:
		d = DURATION;
	#calculate the duration
	t = (float)(d) / len(text);
	for i in range(len(text)):
		sys.stdout.write(text[i]);
		time.sleep(t);

Typing("abv",duration=5)
#[2]: Bounce text (optional power)
def Bounce(text,**kwargs):
	power = 5; #default bounce power is 5
	if "power" in kwargs:
		power = kwargs.get("power",None);
	t = 0.05;
	x = 0;
	while x < power:
		sys.stdout.write("\n"*x+text);
		x = x + 1;
		time.sleep(t);
		os.system('cls' if os.name == 'nt' else 'clear');
	while power > 0:
		sys.stdout.write("\n"*power+text);
		power = power - 1;
		time.sleep(t);
		if power > 0:
			os.system('cls' if os.name == 'nt' else 'clear');

#[3]: Get text info frame
def Frame(text):
	text = text.replace("\t","");
	line = []; #Store list of line length in string 
	lines = text.splitlines()
	#handle all lines
	for s in lines:
		line.append(len(s));
	width = max(line);
	res = ["+" + "-" * width + "+"]
	for s in lines:
		res.append("|" + (s + " " * width)[:width] + "|");
	res.append("+" + "-" * width + "+")
	sys.stdout.write("\n".join(res))

#[4]: Run character from right
def CharRun(text,**kwargs):
	distance = len(text); #defaut distance is text length (distance must > text length)
	if "d" in kwargs:
		distance = kwargs.get("d",None);
	y = " " * distance + "   ".join(text);
	z = 0;
	while y:
	    w = y[0] == text[z];
	    y = y[1+w:];
	    z += w;
	    os.system('cls' if os.name == 'nt' else 'clear');
	    print((text[:z]+y)[:distance]);
	    time.sleep(0.1);
"""
Slide in effect
There is 4 slide in effect : right, left, bottom, top
"""

#[1]: slideInRight
def slideInRight(text,*args,**kwargs):
	x = 0; #number of space
	i = 0; #counter
	distance = 0; #distance here !importance (default it's 0)
	d = DURATION; #duration
	if "distance" in kwargs:
		distance = kwargs.get("distance",None);
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	rmain = 0;
	x = CONSOLE_WIDTH - len(text);
	#Check if the distance is greater than 1
	if distance < 1:
		#calculate the duration
		t = (float)(d) / x;
		rmain = x;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*rmain + text);
			time.sleep(t);
			rmain = rmain - 1; 
	else:
		#calculate the duration
		t = (float)(d) / distance;
		rmain = x;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*rmain + text);
			time.sleep(t);
			rmain = rmain - 1; 
			i = i + 1;
			if i > distance:
				break;

#[2]: slideInLeft
def slideInLeft(text,*args,**kwargs):
	"""
	Remember if you use the slideInLeft effect 
	your text will be align right unless you set the distance > 1
	This is the slideInRight effect but reversed =))
	"""
	x = 0; #number of space
	i = 0; #counter
	l = 0;
	d = DURATION;
	distance = 0; #distance here !importance (default it's 0)
	if "distance" in kwargs:
		distance = kwargs.get("distance",None);
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	rmain = CONSOLE_WIDTH - len(text);
	#calculate the duration
	if distance < 1:
		t = (float)(d) / rmain;
		while l <= rmain:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*l + text);
			time.sleep(t);
			l = l + 1;
	else:
		t = (float)(d) / distance;
		while l <= rmain:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*l + text);
			time.sleep(t);
			l = l + 1;
			i = i + 1;
			if i > distance:
				break;

#[3]: slideInBottom (optional distance)
def slideInBottom(text,*args,**kwargs):
	"""
	Now It's quite like the slideInLeft and slideInRight, 
	you just need to rotate your computer screen =))
	"""
	x = 0; #number of space
	i = 0; #counter
	d = 0;
	d = DURATION;
	distance = 0; #distance here !importance (default it's 0)
	if "distance" in kwargs:
		distance = kwargs.get("distance",None);
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	rmain = CONSOLE_HEIGHT - 1;
	#calculate the duration
	if distance < 1:
		t = (float)(DURATION) / rmain;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write("\n"*rmain + text);
			time.sleep(t);
			rmain = rmain - 1;
	else:
		t = (float)(DURATION) / distance;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write("\n"*rmain + text);
			time.sleep(t);
			rmain = rmain - 1;
			i = i + 1;
			if i > distance:
				break;

#[4]: slideInTop (optional distance)
def slideInTop(text,*args,**kwargs):
	"""
	Remeber if you set the distance < 1 
	the text will run down and it won't stop
	untill the text touch the bottom of the console 
	"""
	x = 0; #number of space
	i = 0; #counter
	d = DURATION;
	distance = 0; #distance here !importance (default it's 0)
	if "distance" in kwargs:
		distance = kwargs.get("distance",None);
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	rmain = 0;
	#Check if the distance is greater than 1
	if distance < 1:
		x = CONSOLE_HEIGHT - 1;
		#calculate the duration
		t = (float)(DURATION) / x;
		rmain = x;
	else:
		#calculate the duration
		t = (float)(DURATION) / distance;
		rmain = distance;
	while i <= rmain:
		os.system('cls' if os.name == 'nt' else 'clear');
		sys.stdout.write("\n"*i + text);
		time.sleep(t);
		i = i + 1;

