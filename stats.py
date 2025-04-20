import sys

filePath = sys.argv[1]

def book(file):
    with open(file) as f:
        content = f.read()
        return content

def words(file):
    count = 0
    with open(file) as f:
        contents_file = f.read().split()
    for i in contents_file:
        count += 1
    return count
    
def count_Characters(file):
    sorted_list = []
    dica = {}
    with open(file) as f:
        contents_file = f.read().lower().split()
        for i in contents_file:
            for cha in i:
                if cha not in dica:
                    dica[cha] = 1
                else:
                    dica[cha] += 1
        sorted_list.append(dica)
        

    return dica

def lis(dic):
    sepList = []
    for k,v in dic.items():
            new = {'cha':k,'count':v}
            sepList.append(new)

    return sepList

def get_count(d):
    return d['count']
    

charec = lis(count_Characters(filePath))
charec.sort(key=get_count,reverse=True)


def recipt():
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filePath}...')
    print('----------- Word Count ----------')
    print(f'Found {words(filePath)} total words')
    print('--------- Character Count -------')
    for i in charec:
        print(f'{i['cha']}: {i['count']}')
    print('============= END ===============')

#print(words(filePath))
#print(count_Characters(filePath))
#print(book(filePath))
#print(recipt())