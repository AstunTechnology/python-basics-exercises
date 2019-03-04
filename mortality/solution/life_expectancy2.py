import re

def extract_counties(file):
    ret_list = []
    header = []
    with open(file, 'r') as f:
        first = True;
        for line in f.readlines():
            cols=line.strip().split(',')
            if cols[4]:
                if first:
                    # make sure to take a copy of the list
                    header = cols[:]
                    first = False
                else:
                    name = cols[1]
                    #remove the '(Met County)' from the name
                    cols[1] = name.replace('(Met County)','')
                    ret_list.append(cols)
    return header,ret_list


def main(mortality_files, sort_col='Area Name'):
    data=[]
    for file in mortality_files:
        (header,d)=extract_counties(file)
        data.append(d)
    print(header)
    try:
        index = header.index(sort_col)
    except ValueError:
        index = 0
    desc = True
    if index < 2:
        desc = False

    for i in range(0,len(data)):
        data[i].sort(key=lambda x:x[index], reverse=desc)

    for row in range(0,len(data[0])):
        for i in range(0, len(data)):
            print(data[i][row])

main(['counties-m-birth.csv','counties-f-birth.csv'],'2012–2014')


