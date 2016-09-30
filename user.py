name = raw_input("Enter your name: ")
if name != "":
	while True:
		msg = raw_input("Message : ")
		if msg == "<<<":
			newmsg = name + " : MultiLine Message \n========================================================================\n"
			temp = raw_input("")
			while temp != ">>>":
				newmsg = newmsg + temp + "\n"
				temp = raw_input("")
			fd = open("msg","a")
			fd.write(newmsg+"========================================================================\n")
			fd.close()
		if msg != "" and msg!="<<<":
			fd = open("msg","a")
			fd.write(name+" : "+msg+"\n")
			fd.close()