# ottocoffee
Automated Coffee maachine!

We created a website that can control a raspberry pi servo. 

The continued work on this project would be to build out the website add logic for setting alarms and create a more resiliant servo system for button presses. 

To deploy install from requirements.txt on a raspberry pi and run: 

	sudo python otto-control.py

Then on the same local network navigate to the ip address of your pi. 
If you hit: 

	127.your.ip.0.1/forward   	#The servo will rotate clockwise and 
	127.your.ip.0.1/backwards 	#The servo will rotate counterclockwise. 

[@timmyreilly](http://twitter.com/timmyreilly) if you have any questions!
