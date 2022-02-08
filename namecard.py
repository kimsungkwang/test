from dataclasses import dataclass
from database import con

@dataclass
class NameCard:
    name:str
    email:str
    phone:str
    address:str
    def insert(self):
        cursor=con.cursor()
        sql=f'insert into NameCard values("{self.name}","{self.email}","{self.phone}","{self.address}")'
        cursor.execute(sql)
        con.commit()
        cursor.close()

    @classmethod
    def all(cls):
        cursor=con.cursor()
        sql='select * from NameCard'
        cursor.execute(sql)
        records=cursor.fetchall()
        records=list(map(lambda r:cls(*r),records))

        cursor.close()
        return records

def main():
    
    book=[]
    with open('addressbook.txt',encoding='utf-8') as file:
        namecard=file.readlines()

    for n in namecard:
        print(n. split(','))
        a=n. split(',')
        A=NameCard(a[0],a[1],a[2],a[3])
        book.append(A)
        B=NameCard(a[0],a[1],a[2],a[3])
        B.insert()
    print(book)
    

main()

