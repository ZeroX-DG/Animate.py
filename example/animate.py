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
 /  /_   | |__  | |\ \  | |__| |  / /\ \ 
|_____|  |____| |_| \_\  \____/  |_/  \_|
"""
"""
*
* animate.py
* Version - 2.0
* Licensed under the MIT license - http://opensource.org/licenses/MIT
*
* Copyright (c) 2016 Nguyen Viet Hung
*
"""

DURATION       = 1; #The default time for animation duration is 1 sec
CONSOLE_HEIGHT = 0;
CONSOLE_WIDTH  = 0;
VERSION        = 2; #version of animate.py

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
		power -= 1;
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
	if "distance" in kwargs:
		distance = kwargs.get("distance",None);
	y = " " * distance + "   ".join(text);
	z = 0;
	while y:
	    w = y[0] == text[z];
	    y = y[1+w:];
	    z += w;
	    os.system('cls' if os.name == 'nt' else 'clear');
	    print((text[:z]+y)[:distance]);
	    time.sleep(0.1);

#[5]: Blinking typing text
def BlinkTyping(text,**kwargs):
	#calculate the duration
	d = 0;
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	else:
		d = DURATION;
	t = (float)(d) / len(text);
	ptext = "";
	for i in range(len(text)):
		os.system('cls' if os.name == 'nt' else 'clear');
		ptext += text[i];
		if i % 2 == 0:
			sys.stdout.write(ptext+"|");
			time.sleep(0.5);
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(ptext+"|");
		else:
			sys.stdout.write(ptext);
		time.sleep(t);

#[6]: FadeOut text
def FadeOut(text):
	t = 0.08;
	for i in range(len(text)+1):
		os.system('cls' if os.name == 'nt' else 'clear');
		sys.stdout.write(text[:len(text)-i]);
		time.sleep(t);

#[7]: Diamond text
def Diamond(text):
	#A vaild text is a text whose length is divisible by 4 and greater than 0
	if len(text) % 4 == 0 and len(text) > 0:
		lrow = len(text) / 4 + 1;
		arr = [];
		c = 0;
		i = 1;
		a = 0;
		arr.append(text[0]);
		#get pair of character in to a array element
		while c < len(text[1:][::-1][1:][::-1]):
			p = text[1:][::-1][1:][::-1][c] + text[1:][::-1][1:][::-1][c + 1];
			arr.append(p);
			c += 2;
		arr.append(text[::-1][0]);
		def getSpace(n):
			#get the space for each row :3
			c = 1;
			if n == 1:
				return 0;
			elif n == 2:
				return 1;
			else:
				for i in range(n-2):
					c += 2;
				return c;
		width = getSpace(lrow) + 2;
		spacef = (width - 1) / 2;
		#Begin to print
		print " " * spacef + arr[0] + " " * spacef;
		for s in range(1,lrow-1):
			print " " * (spacef - i) + (" " * getSpace(s+1)).join(arr[s]);
			i = i + 1;
		print (" "*getSpace(lrow)).join(arr[lrow-1]);
		for s in range(1,lrow-1):
			print " " * (1 + spacef - i) + (" " * getSpace(i)).join(arr[lrow-1:][s]);
			i = i - 1;
		print " " * spacef + arr[len(arr)-1] + " " * spacef;
	else:
		print "[!]:Please check your string length if it's greater than 0 and divisible by 4";

#[8]: Old printer effect (optional duration)
def OldPrinter(text,**kwargs):
	#calculate the duration
	d = 0;
	if "duration" in kwargs:
		d = kwargs.get("duration",None);
	else:
		d = DURATION;
	t = (float)(d) / len(text.splitlines());
	lines = text.splitlines();
	for s in lines:
		print s;
		time.sleep(t);

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
			rmain -= 1; 
	else:
		#calculate the duration
		t = (float)(d) / distance;
		rmain = x;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*rmain + text);
			time.sleep(t);
			rmain -= 1; 
			i += 1;
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
			l += 1;
	else:
		t = (float)(d) / distance;
		while l <= rmain:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write(" "*l + text);
			time.sleep(t);
			l += 1;
			i += 1;
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
			rmain -= 1;
	else:
		t = (float)(DURATION) / distance;
		while rmain >= 0:
			os.system('cls' if os.name == 'nt' else 'clear');
			sys.stdout.write("\n"*rmain + text);
			time.sleep(t);
			rmain -= 1;
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
		i += 1;

"""
Some other effect
"""
#[1]: Print text from top to bottom right (optional postion)
def TopToBottomRight(text,**kwargs):
	t = 0.05;
	d = CONSOLE_HEIGHT;
	p = 0;
	if "position" in kwargs:
		p = kwargs.get("position",None);
	for i in range(1,d):
		print(" "*p + " "*i + text);
		time.sleep(t);

#[2]: Print text from top to bottom left (optional postion)
def TopToBottomLeft(text,**kwargs):
	t = 0.05;
	d = CONSOLE_HEIGHT;
	p = 0;
	if "position" in kwargs:
		p = kwargs.get("position",None);
		p = CONSOLE_WIDTH - (p + len(text));
	i = CONSOLE_WIDTH-len(text)-1-p;
	while d > 0:
		print(" "*i + text);
		time.sleep(t);
		d -= 1;
		i -= 1;

"""
Combine effects 
These effects was created using the basic effect in this module
"""

#[1]: Horizontal bounce (optional time)
def HBounce(text,**kwargs):
	if "time" in kwargs:
		time = kwargs.get("time",None);
	else:
		time = 1; #defautl time is 1
	while time > 0:
		slideInLeft(text);
		slideInRight(text);
		time -= 1;

#[2]: Vertical bounce (optional time)
def VBounce(text,**kwargs):
	if "time" in kwargs:
		time = kwargs.get("time",None);
	else:
		time = 1; #defautl time is 1
	while time > 0:
		slideInTop(text);
		slideInBottom(text);
		time -= 1;


