from csv import reader
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    f = open(data, mode='r+')
    data_reader = list(reader(f))
    price = []
    name = []
    for i in data_reader[1:]:
        price.append(float(i[1]))
        name.append(i[0])
    price_max = max(price)
    index_max = price.index(price_max)
    name_max = name[index_max]
    return name_max


