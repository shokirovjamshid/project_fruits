from csv import reader
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    f = open(data, mode='r+')
    data_reader = list(reader(f))
    price = []
    for i in data_reader[1:]:
        price.append(float(i[1]))
    price_min = min(price)
    index_min = price.index(price_min)+1
    return index_min
print(get_cheapest_fruit_id('fruits.csv'))
    
        
        
            