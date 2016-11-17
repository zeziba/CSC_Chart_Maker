import pandas


with open("LOG0.CSV", "r") as old_file:
    with open("LOG0_new.CSV", "w+") as new_file:
        data = pandas.read_csv(old_file)
        print(list(data))
        data[list(data)[0]] = data[list(data)[0]].apply(lambda x: int(x) / 1000.0)
        data.to_csv(new_file)
