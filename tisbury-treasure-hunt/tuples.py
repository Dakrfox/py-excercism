"""Functions to help Azara and Rui locate pirate treasure."""
def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return tuple(azara_record[1]) in rui_record
    
def create_record(azara_record, rui_record):
    if(compare_records(azara_record, rui_record)):
        azara_record+=rui_record
        return azara_record
    return "not a match"
    
def clean_up(combined_record_group):
    aux = ""
    for items in combined_record_group:
        aux += f"{(items[0], items[2], items[3], items[4])}\n"
    return aux
