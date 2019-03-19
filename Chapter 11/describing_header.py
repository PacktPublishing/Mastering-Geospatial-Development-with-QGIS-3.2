header = myVector.fields() 
print("How many columns?", header.count()) 
print("does the column 4 exist?", header.exists(4)) 
print("does the column named 'value' exist?", header.indexFromName('value')) 
print("Column 0 has name", header[0].name()) 
for column in header: 
    print("name", column.name()) 
    print("type", column.typeName()) 
    print("precision", column.precision()) 
