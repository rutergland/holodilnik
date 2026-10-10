import datetime
from decimal import Decimal

goods = {}
DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    if title not in items.keys():
        items[title] = []
    items[title].append({'amount': amount, 'expiration_date': expiration_date})

def add_by_note(items, note):
    i = note.split()
    expiration_date = None
    if i[-1].count('-') == 2:
        expiration_date = i.pop()
    amount = Decimal(i.pop())
    title = ''.join(i)
    add(items, title, amount, expiration_date)

def amount(items, needle):
    res = Decimal('0')
    for title in find(items, needle):
        for i in items[title]:
            res += i['amount']
    return res

def find(items, needle):
    res = []
    for i in items.keys():
        if needle.lower() in i.lower():
            res.append(i)
    return res

add(goods, 'Вода', Decimal('2.5'), '2023-08-01')
add(goods, 'Вода', Decimal('2.5'), '2023-08-02')
add_by_note(goods,'Нига 1')

print(goods)
print(amount(goods, 'Вода'))
print(find(goods, 'да'))