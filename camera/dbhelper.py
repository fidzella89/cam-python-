from sqlite3 import connect, Row


database:str = "studentinfo.db"

def getprocess(sql:str)->list:
    rows:list
    db=connect(database)
    cursor = db.cursor()
    db.row_factory = Row
    cursor.execute(sql)
    data:list = cursor.fetchall()
    [rows.append(dict(item)) for item in data]
    db.close()
    return rows

def postprocess(sql:str)->bool:
    db=connect(database)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    return True if cursor.rowcount>0 else False
    
def add_record(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    flds:Str = "','".join(keys)
    dta:str = "','".join(values)
    sql:str = f"INSERT INTO `{table}` (`{fld}`) VALUES(`{dta}`)"
    return postprocess(sql)

def getall_records(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    return getprocess(sql)
    
def getall_books()->list:
        sql:str = f"SELECT isbn,title,author,copyright,edition,price,qty,[price]*[qty] as total FROM `books`"
        return getprocess(sql)
        