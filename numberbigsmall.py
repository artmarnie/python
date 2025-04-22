largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
        break
    try: 
        numero = int(num)
    except:
        print "Invalid input"
        continue

    if largest is None:
        largest = numero
    elif largest < numero:
        largest = numero

    if smallest is None: 
        smallest = numero
    elif smallest > numero:
        smallest = numero
    
print "Maximum is", largest

print "Minimum is", smallest
