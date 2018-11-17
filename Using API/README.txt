The purpose of this code is to get a list of cuisines for each of the restaurants given. 

I have used Zomato API's to get this work done.

The input format is a csv file of [restaurant name,restaurant id], and the output file of the format [input restaurant name,restaurant id, restuarant name returned by API(for double checking), list of cuisines]

The API calls have a limit if 1000 API calls per IP address and per API key.

So the input file is broken into 4 files, and then again merged to get the desired output. make_in.py and make_out.py are used for this purpose.


Zomato API's are inconsistent as they give 404 error for restaurants which are closed(temporarily or permamently). As I needed the cuisine information for some of the closed restaurants as well, this code did not fully solve my problem. I used requests library with beautifulSoupr late to get the required information

Sample input file : restaurants.csv
Sample output file: cuisines.csv

Closed.txt - stores a list of restaurants which are closed.

To run this code simply run the python code get_cuisines.py and specify the correct path of the input file
