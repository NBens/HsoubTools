# Oldest : 73985
# New Newest https://io.hsoub.com/go/75935

from bs4 import BeautifulSoup
import urllib.request
import time
from random import randint

unknown = b'\xd9\x85\xd8\xb3\xd8\xaa\xd8\xae\xd8\xaf\xd9\x85 \xd9\x85\xd8\xac\xd9\x87\xd9\x88\xd9\x84' # Chinese, Don't touch it plz
first = 73985 #Don't touch this, and don't put 1, we don't want to crash Hsoub servers
last = 75935  #Go to https://io.hsoub.com/new and get the latest topic (better do it in private browser mode)

totalComments = 0
unknownComments = 0

my_file = open("comments.txt", "w")


for i in range(first,last + 1):
	url = "https://io.hsoub.com/go/{}".format(i)
	try:
		req = urllib.request.Request(
			url, 
			data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			}
		)
		
		content = urllib.request.urlopen(url).read()

		soup = BeautifulSoup(content)

		spans = soup.find_all('span', {'class' : 'postUsername'})
		spans.pop(0)
		totalComments += len(spans)
		for span in spans:
		
			string = span.string.encode('utf-8')
			
			if (unknown in string):
				unknownComments += 1
	except urllib.error.HTTPError as e:
		print("Error in {} - Code: {}".format(i, e.code))
	except urllib.error.URLError as e:
		print("Error in {} - Code: {}".format(i, e.reason))
		
	print('No : {}'.format(i))
	
	time.sleep(3 + randint(0,3))

my_file.write("Total Comments: " + str(totalComments))	
my_file.write("\nUnknown Comments: " + str(unknownComments))
my_file.write("\nKnown Comments: " + str(totalComments - unknownComments))	
my_file.write("\nPercentage (Unknown / total): " + str((unknownComments / totalComments) * 100))

my_file.close()
	
