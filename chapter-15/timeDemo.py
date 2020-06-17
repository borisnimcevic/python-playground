#! python3

import threading, time
print('Start of program.')

def takeNap():
	time.sleep(5)
	print('Wake up!')

threadObj = threading.Thread(target=takeNap)
threadObj.start()

print('End of the program')
