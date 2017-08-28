import webbrowser as br

def allIndex(mlist, query): #finds the indexes of all instances of query in mlist (list or string)
    indexes = []
    count = 0
    if len(query) == 1:
        for i in mlist:
            if i == query:
                indexes.append(count)
            count += 1
    else:
        for i in mlist:
            if i == query[0]:
                charlist = ''
                for x in range(len(query)):
                    charlist = charlist + mlist[count + x]
                if charlist == query:
                    indexes.append(count)
            count += 1
    if len(indexes) == 0:
        indexes = None
    return indexes

def gsearch(query, Open): #Searches the string query on google, opens a browser window if Open is true
    pquery = query.split(' ')
    gquery = ''
    for i in pquery:
        gquery = gquery + i + '+'

    url = 'https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjrw4Tuw4TVAhXDaT4KHZEiCBoQPQgD#hl=en&q=' + gquery
    if Open:
        br.open_new(url)
    return url




