# clicktime-google-directions

Your challenge is to write an application that will answer the following question: how can you get from your current location to the ClickTime office, if you have to stop off somewhere to get coffee and donuts for the dev team? Your application should always start at the user's current location, which could be anywhere in the United States (don't worry about overseas).

Try to stay away from hard-coding locations or names of places into your application, if possible (besides the address of ClickTime, of course). Also, you don't need to render the route on an actual map, just provide step by step instructions that someone could follow in order to get to ClickTime. Please only use the walking, biking, and public transportation options, because some of us don't have cars. Have fun!
fczcz
Address of ClickTime office: 282 2nd Street 4th floor, San Francisco, CA 94105

Please install these following files in the console before running the file:#
pip install googlemaps
pip install python-google-places

To run the file:

python clicktime.py "driving | bicycling | walking | transit" "distance | prominence"
