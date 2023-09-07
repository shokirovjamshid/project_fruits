from csv import reader
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    f = open(data, mode='r+')
    data_reader = list(reader(f))
    price = []
    name = []
    for i in data_reader[1:]:
        price.append(float(i[1]))
        name.append(i[0])
    price_min = min(price)
    index_min = price.index(price_min)
    name_min = name[index_min]
    return name_min