from socket import gethostname
import os,platform, psutil,sys,time  
from psutil._common import bytes2human

maxCPU=10
maxCapacity=50
def clear():
	os.system("cls")

def stats(): 
	#sys.stdout=ready	
	#ready.close()
	systime=time.strftime("%d %b %Y %H:%M:%S")
	usr=os.getlogin()
	pcname=gethostname()
	totCPU=psutil.cpu_percent()
	syspart = psutil.disk_usage("C:\\")
	syspart = bytes2human(syspart.used)
	OSname=platform.uname().system+" "+platform.uname().version
	
	return (systime,
			usr,
			pcname,
			totCPU,
			syspart,
			OSname)
	
	"""	<--	Check each CPU core load by percentage
		for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
			sys.stdout.write(f"\rCore {i+1}: {perc}% ") 
	"""
	"""	<-- 
	
					if totCPU>=maxCPU or float(syspart.strip("G"))>=maxCapacity:
					print(float(syspart.strip("G")))
					with open ("Отчет.txt","a") as fin:
						fin.write("CPU usage level: "+str(totCPU)+"\n")
	"""
def log(systime,usr,pcname,totCPU,syspart,OSname):
	print("-"*20,
			f"\nCurrent time:\t{systime}\nCurrent user:\t{usr} \nName of machine:{pcname}  \nRunning on:\t{OSname} \nPartition used:\t{syspart} \nTotal CPU Usage:{totCPU}%\n")
	if totCPU>=maxCPU: 
		with open ("D:\HW x Telegram\HW info\Отчет.txt","a") as fin:
			fin.write(systime+" ")
			fin.write("CPU usage level: "+str(totCPU)+"\n")
if __name__=="__main__":
		try:
			while True:
				systime,usr,pcname,totCPU,syspart,OSname=stats()		
				log(systime,usr,pcname,totCPU,syspart,OSname)
				time.sleep(2)
				sys.stdout.flush()
				clear()
		except KeyboardInterrupt:
			print("Abort by KB")
'''--?
	What else need to be captured & logged?
	Do we need a login session for personal recommendations? 
'''