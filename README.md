# JSON_to_DataFrame

## Challenge
JSON is a common format for sending and requesting data through a REST API and it can offen have multiple dimensions. 
JSON can get very complex and difficult to analyst with common tools that prefer 2 dimension tables like Excel, Power BI, Tableau etc.

## Solutions
This repository attempts to provide multiple methods to extract JSON Data and convert this data to a DataFrame (two dimensional table with columns and rows).

Various types of JSON files examples will be provided with different structures for holding data (for example, dictionarys, lists, lists within list etc.)
Each JSON file will have functions that will extract the data into a Pandas DataFrame table. A unique id column will be given to each row within the DataFrame.

### Repository Folders:

- 01SingleLayer: JSON List with Dictionaries
- 02NestedList: JSON List with Dictionaries with Nested Lists

### 00UsefulFunctions:

- Pagination_In_Filename:
    Saving multiple paginated JSON files with page number included in the name with a fixed number of characters for ordering and later extraction ( must know
    number of pages in API call beforehand or count them to get total number of pages )
