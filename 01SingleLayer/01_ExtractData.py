#required to convert sample json string into <class 'dict'>
import json
#required to convert constructed <class 'list'> into a pandas DataFrame
import pandas as pd

#Sample JSON string
sample = """{
"contents": [
    {
		"Colour": "red",
		"Order": 1
	},
	{
		"Colour": "green",
		"Order": 2
	},
	{
		"Colour": "blue",
		"Order": 3
	},
	{
		"Colour": "cyan",
		"Order": 4
	},
	{
		"Colour": "magenta",
		"Order": 5
	},
	{
		"Colour": "yellow",
		"Order": 6
	}
 ]
 }"""

#Converting sample to <class 'dict'> ( confirm with 'print(type(js))' )
js = json.loads(sample)

#Empty List to add dictionaries (this will be a single row for our table) to
dictionary_list = []

#Looping through each dictionary in the JSON sample to extract required data
for i in js['contents']:
  
  #Extracting data as variables
  colour = i.get("Colour").capitalize()
  order = i.get("Order")
  
  #Constructing our row
  row = {
    "Colour": colour,
    "Order": order
	}
    
  #Adding our row
  dictionary_list.append(row)

#Converting our List of Dictionaries to a pandas DataFrame
pandas_df = pd.DataFrame(dictionary_list).set_index("Order")

print(pandas_df)
