import re

def extract_counties(file):
    ret_list = []
    header = []
    '''
    Add your code here to parse the file.
    You will need to determine which lines contain data, header
    values or junk.
    Also remove 'met county' where necessary from the names to make them look
    tidier.
    '''
    return header,ret_list


def main(mortality_files):
    for file in mortality_files:
        (header,data)=extract_counties(file)
        print(header)
        '''
        for additional marks can you sort the rows based on a column?
        '''
        for row in data:
            print(row)

main(['counties-m-birth.csv','counties-f-birth.csv'])


