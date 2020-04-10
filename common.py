import csv

def tsv_to_dict(filename, key_col=0, val_col=1):
    
    the_dict = {}
    
    with open(filename, 'r') as fp:
        reader = csv.reader(fp, delimiter='\t')
    
        for row in reader:
            if len(row) > 1: 
                the_dict[row[key_col]] = row[val_col]
            
    return the_dict