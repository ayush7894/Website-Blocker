# Website-Blocker
I have created a  Python application that runs in the background and blocks a list of websites during any hours according to  user. We will do this with Python’s built-in libraries, so no need to install external packages.  So how do you block a website? Every operating system has a hosts file. This hosts file is used to map hostnames (or domains) to IP addresses. This host file is used to restrict access to unwanted websites and domains. Most of the website blockers and parental control apps use this host file for this purpose. 

What these lines of code will do is when someone requests access to www.facebook.com or www.twitter.com from a web browser on this PC, they will be redirected back to the local IP address of this PC which is 127.0.0.1. Our application will use file manipulation methods of Python to open this file and put these lines of code in this file.

Once our program is running, it will always run in the background and automatically enter these lines of code when the clock ticks the start time entered by user. Then it will check the clock every 2 minutes and remove these lines of code from the host file when the time reaches the end time submitted by user. We will use the Python’s built-in libraries date and datetime for this program. This is a very handy solution because you don’t want to log into all computers in your office and do this manually twice every day

Go through the code once,the comments out there will definitely help you in understanding each line of code.
