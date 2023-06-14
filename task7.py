a2 = 180
a3 = 37
a4 = 25
a5 = 0
a6 = 1
ba2 = bin(a2)[2:]
ba3 = bin(a3)[2:]
ba4 = bin(a4)[2:]
ba5 = bin(a5)[2:]
ba6 = bin(a6)[2:]
if len(ba2) < 10:
    ba2 = '0' * (10 - len(ba2)) + ba2
if len(ba3) < 6:
    ba3 = '0' * (6 - len(ba3)) + ba3
if len(ba4) < 5:
    ba4 = '0' * (5 - len(ba4)) + ba4
if len(ba5) < 2:
    ba5 = '0' * (2 - len(ba5)) + ba5
# print(ba6, ba5, ba4, ba3, ba2)
print(hex(int(ba6, 2)), hex(int(ba5, 2)), hex(int(ba4, 2)), hex(int(ba3, 2)), hex(int(ba2, 2)))
res = ba6 + ba5 + ba4 + ba3 + ba2 + "00000000"
print(res, len(res))
print(hex(int(res, 2)))

#x = {'A2': '470', 'A3': '16', 'A4': '1', 'A5': '2', 'A6': '1'}
def main(x):
    a2 = int(x['A2'])
    a3 = int(x['A3'])
    a4 = int(x['A4'])
    a5 = int(x['A5'])
    a6 = int(x['A6'])
    ba2 = bin(a2)[2:]
    ba3 = bin(a3)[2:]
    ba4 = bin(a4)[2:]
    ba5 = bin(a5)[2:]
    ba6 = bin(a6)[2:]
    if len(ba2) < 10:
        ba2 = '0' * (10 - len(ba2)) + ba2
    if len(ba3) < 6:
        ba3 = '0' * (6 - len(ba3)) + ba3
    if len(ba4) < 5:
        ba4 = '0' * (5 - len(ba4)) + ba4
    if len(ba5) < 2:
        ba5 = '0' * (2 - len(ba5)) + ba5
    res = ba6 + ba5 + ba4 + ba3 + ba2 + "00000000"
    return(hex(int(res, 2)))

print(main({'A2': '470', 'A3': '16', 'A4': '1', 'A5': '2', 'A6': '1'}))
print(main({'A2': '991', 'A3': '24', 'A4': '16', 'A5': '0', 'A6': '1'}))
print(main({'A2': '776', 'A3': '10', 'A4': '15', 'A5': '2', 'A6': '1'}))
print(main({'A2': '180', 'A3': '37', 'A4': '25', 'A5': '0', 'A6': '1'}))

'''
main({'A2': '470', 'A3': '16', 'A4': '1', 'A5': '2', 'A6': '1'})
'0xc141d600'

main({'A2': '991', 'A3': '24', 'A4': '16', 'A5': '0', 'A6': '1'})
'0x9063df00'

main({'A2': '776', 'A3': '10', 'A4': '15', 'A5': '2', 'A6': '1'})
'0xcf2b0800'

main({'A2': '180', 'A3': '37', 'A4': '25', 'A5': '0', 'A6': '1'})
'0x9994b400'
'''
