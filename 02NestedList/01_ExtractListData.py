#required to convert sample json string into <class 'dict'>
import json
#required to convert constructed <class 'list'> into a pandas DataFrame
import pandas as pd

#Sample JSON string
sample = """{
"contents": [
    {
		"PhoneBrandId": "001",
		"PhoneBrand": "iPhone14",
		"ColoursAvailable": [
			{
			"Colour": "black"
			},
			{
			"Colour": "white"
			},
			{
			"Colour": "red"
			},
			{
			"Colour": "grey"
			},
			{
			"Colour": "pink"
			},
			{
			"Colour": "yellow"
			}
			
		]
	},
	{
		"PhoneBrandId": "002",
		"PhoneBrand": "SamsungGalaxyS23",
		"ColoursAvailable": [
			{
			"Colour": "green"
			},
			{
			"Colour": "black"
			},
			{
			"Colour": "white"
			},
			{
			"Colour": "pink"
			},
			{
			"Colour": "yellow"
			}
			
		]
	},
	{
		"PhoneBrandId": "003",
		"PhoneBrand": "Google Pixel 7",
		"ColoursAvailable": [
			{
			"Colour": "green"
			},
			{
			"Colour": "black"
			},
			{
			"Colour": "white"
			}			
		]
	}

 ]
}"""

#Converting sample to <class 'dict'> ( confirm with 'print(type(js))' )
js = json.loads(sample)

#Empty List to add dictionaries with their nested lists (this will be a single row for our table)
nested_dictionary_list = []

#Looping through each dictionary in the JSON sample to extract required data
for i in js['contents']:
  
  #Extracting data as variables
  PhoneBrandId = i.get("PhoneBrandId")
  PhoneBrand = i.get("PhoneBrand")
  ColoursAvailable = i.get("ColoursAvailable")
  
  #Constructing our row
  row = {
    "PhoneBrandId": PhoneBrandId,
    "PhoneBrand": PhoneBrand,
    "ColoursAvailable": ColoursAvailable
	}
    
  #Adding our row
  nested_dictionary_list.append(row)

#New Empty list for final flattened table
final_constructed_list = []

#Unpacking nested list
for n in nested_dictionary_list:
    #Taking values to be duplicated on each row for each list iteration
    PhoneBrandId = n.get("PhoneBrandId")
    PhoneBrand = n.get("PhoneBrand")

    #tracking each iteration
    i = 0
    #Extracting colour data from list
    for c in n.get("ColoursAvailable"):
        Colour = c.get("Colour")

        #Unique Id can be constructed using PhoneBrandId and Iteration Track
        row = {
            "Id": int(str(PhoneBrandId) + str(i)),
            "PhoneBrandId": PhoneBrandId,
            "PhoneBrand": PhoneBrand,
            "Colour": Colour,
            "ColourOrder": i        
        }
        final_constructed_list.append(row)
        i += 1


#Converting our List of Dictionaries to a pandas DataFrame
pandas_df = pd.DataFrame(final_constructed_list)

print(pandas_df)