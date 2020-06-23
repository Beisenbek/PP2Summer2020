import re

f = open("data.txt", "r")
text = f.read() 

binResult = re.search(r"БИН(?P<BIN>.*)", text)  
znmResult = re.search(r"ЗНМ:(?P<ZNM>.*)", text)  
kassaResult = re.search(r"Касса(?P<Kassa>.*)", text)  
receiptResult = re.search(r"Чек(?P<Receipt>.*)", text)  
dateAdressResults = re.search(r"Время:(?P<Date>.*)\n(?P<Adress>.*)", text)  

binText = binResult.group("BIN").strip() 
znmText = znmResult.group("ZNM").strip()
kassaText = kassaResult.group("Kassa").strip() 
receiptText = receiptResult.group("Receipt").strip() 
dateText = dateAdressResults.group("Date").strip()
adressText = dateAdressResults.group("Adress").strip()

item_pattern_text = r"(?P<item_title>.*)\n{1}(?P<item_count>.*)x(?P<item_price>.*)\n{1}(?P<total>.*)\n{1}(?P<caption>Стоимость)\n{1}(?P<total2>.*)\n{1}"
item_pattern = re.compile(item_pattern_text)

data = [["БИН","ЗНМ","Касса","Чек","Наименование товара","Цена за единиц","Кол-во","Сумма","Дата и Время","Адрес"]]

for m in re.finditer(item_pattern, text):
    data.append([
        binText,
        znmText,
        kassaText,
        receiptText,
        m.group("item_title"),
        m.group("item_price"),
        m.group("item_count"),
        m.group("total"),
        dateText,
        adressText
    ])

import csv

with open("result.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)