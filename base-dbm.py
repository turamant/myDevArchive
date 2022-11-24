import dbm

with dbm.open('base1.db', 'n') as db:
    db['key'] = 'value'
    db['today'] = 'Sunday'
    db['author'] = 'Doug'

print(dbm.whichdb('base1.db'))

with dbm.open('base1.db', 'r') as db:
    print('keys():', db.keys())
    for k in db.keys():
        print('iterating:', k, db[k])
    print('db["author"]=', db['author'])
