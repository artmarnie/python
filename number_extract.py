text = "X-DSPAM-Confidence:    0.8475";
n = 0
pos = None
while n < 10 :
    n_str = str(n)
    pos = text.find(n_str)
    if pos is not None :
        break
    n = n +1
    
if pos is None :
    print "No number in the string"
    quit()
    
    
r = text[pos:pos+99] 
try:
    r2 = float(r)
except:
    print "could not convert to float"

print r2
