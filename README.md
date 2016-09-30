#LabChat App<br/>
This is simple program which makes your college labs as a chat room<br/>
![ScreenShort](https://github.com/sushinpv/LabChat/blob/master/Screenshot%20from%202016-09-30%2007-15-24.png?raw=true)

#HOW TO USE<br/>
<br/>
##STEP 1 : Initialize
Connect many computer's using LAN or Wifi and copy all three files (msg, read.py and user.py) any one of the PC(master) and to any folder. Check the IP address of the PC (172.22.14.4)
<br/>Example : copy all files into Documents/LabChat/
##STEP 2: Make connection
Open terminal on other computers (slaves) and remote login to the PC which you copied the file<br/>
`ssh username@ip_address`<br/>
`ssh user@172.22.14.4`
<br/>it will ask for the password: Type the password of the master computer, username is master pc username
##STEP 3: Run the files
Change your folder to the folder in which you copied the file.Type the following codes<br/>
`cd path_to_the_files`<br>
`cd ~/Documents/LabChat/`<br/>
`python user.py`<br/>
**Open One more terminal and repeat the step 2 then run the following cmd** <br/>
`cd ~/Documents/LabChat/` <br/>
`python read.py`

##TO send Multi line message
in message type <<< then followed by the message then >>><br/>
`message : <<<`<br/>
`This`<br/>
`is`<br/>
`a`<br/>
`simple`<br/>
`message`<br/>
`>>>`
