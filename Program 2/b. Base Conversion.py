# 2b) b2d and o2h
def bin2Dec(bin):
    dec = 0
    for i in range(len(bin)):
        dec+=(int(bin[i])) * ((2** (len(bin)-i-1)))
    return dec

def oct2Hex(oct):
    dec = 0
    for i in range(len(oct)):
        dec += int(oct[i]) * ((8**(len(oct)-i-1)))
    hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    octHex = ' '
    while dec > 0:
        rem = dec % 16
        octHex += hexa[rem]
        dec = dec // 16
        
    return octHex

bin=input("Enter the Binary Number:")
print("Binary to Decimal is ",bin2Dec(bin))
oct=input("Enter the octal Number:")
print("Octal to Decimal is ",oct2Hex(oct))