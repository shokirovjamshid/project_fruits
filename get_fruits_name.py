from csv import reader
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f = open(data, mode='r+')
    data_reader = list(reader(f))
    name = []
    for i in data_reader[1:]:
        name.append(i[0])
    return name