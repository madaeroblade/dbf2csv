def header(db, output):
    if(not db.isOpen() or output.closed):
        pass
        # TODO: Exception
    
    header = ""
    for field_name in db.fieldNames():
        header += field_name + ","
    
    output.write(header[:-1] + "\n")
    

def records(db, output, offset, records):
    if(not db.isOpen() or output.closed):
        pass
        # TODO: Exception
    
    for i in range(offset, offset + records):
        rec = db[i]
        
        rec_str = ""
        for fldName in db.fieldNames():
            rec_str += str(rec[fldName]) + ','
            
        output.write(rec_str[:-1] + "\n")