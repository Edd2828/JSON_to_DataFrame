def add_zeros_to_pagination(file_name, list_count):

    # Create our list to iterate through
    items = []
    for i in range(1,list_count):
        items.append(i)

    # Finding out the largest number of characters 
    items_in_list = str(len(items))
    char_with_max_count = len(items_in_list)

    # Create list of strings to hold our text for file naming
    file_name_suffix = []

    # Iterating each item to add suffix all with same number of characters
    for i in items:
    
        # Need item in items as string
        i_as_str = str(i)

        # Need length of characters in the item
        length_of_i = len(i_as_str)

        # Creating the new item name with same number of characters in each and all items as well as page number for ordering
        new_suffixed_item = f"{file_name}{str('0'*int(char_with_max_count - length_of_i))}{i_as_str}.file"

        # Appending created item to new list
        file_name_suffix.append(new_suffixed_item)

    print(file_name_suffix)

# Example: 1000 pagination pages in an API GET
add_zeros_to_pagination("PagingationPage_", 1000)