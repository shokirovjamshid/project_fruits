from csv import reader
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f = open(data, mode='r+')
    data_reader = list(reader(f))
    price = 0
    for i in data_reader[1:]:
        price+=float(i[1])
    return price

    