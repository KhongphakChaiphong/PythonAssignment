data='asjdfh:   0.8765'
txt1=data.find(':')
txt2=data[txt1+1:100].lstrip()
txt3=float(txt2)
print(txt3)