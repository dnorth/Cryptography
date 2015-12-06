import subprocess

def writeToFile(string):
	f = open('fortunes.txt', 'a')
	f.write(string)

def main():
	fortunes = []
	while True:
		process = subprocess.Popen(['./fortune_static', '-a'], stdout=subprocess.PIPE)
		out, err = process.communicate()
		split1 = out.split("Your fortune:\n\n")[1]
		fortune = split1.split("\n\n")[0]
		if fortune not in fortunes:
			fortunes.append(fortune)
			writeToFile(fortune + "\n\n")
			print fortune
			print "\n\n Fortunes: " + str(len(fortunes))
	

if __name__== '__main__':
	main()
