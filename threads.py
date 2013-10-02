import thread, time

def ausgabe():
	global count
	t_id = thread.get_ident()
	for i in range(5):
		count =+1
		print("Thread {} Counter {} Iterator {}").format(t_id,count,i)
		time.sleep(2)
	return
	
#Main Programm
t_id = thread.get_ident()
count = 0
for i in range(5):
	print("Main thread: {} Counter: {} Iterator: {}").format(t_id,count,i)
	thread.start_new_thread(ausgabe,())
	count =+ 1
	time.sleep(1)
	
time.sleep(20)