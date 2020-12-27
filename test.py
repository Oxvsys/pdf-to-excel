import easyocr

reader = easyocr.Reader(['mr', 'en'])

result = reader.readtext('output/5/0_0.png')

for each_item in result:
    print(each_item)
