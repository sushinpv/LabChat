no=0;
while True:
	fd = open("msg","r")
	currentno = 0
	for i in fd:
		currentno = currentno + 1
	if no != currentno:
		temp = 0
		fd1 = open("msg","r")
		for i in fd1:
			temp = temp + 1
			if no<temp:
				print i.rstrip()
		no = temp