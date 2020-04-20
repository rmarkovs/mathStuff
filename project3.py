import argparse
def main():
    stateFile = open("MathState.txt", "r")
    stateCode = stateFile.read()
    stateCode = stateCode.rstrip('\r\n').replace("\n", '')
    frequencies = {}
    i = 0
    while i<len(stateCode) -1:
        temp = ""
        temp = stateCode[i:i+2]
        if temp in frequencies:
            frequencies[temp] +=1
        else:
            frequencies[temp] = 1
        i = i +1
    count = 0
    for i in frequencies:
        temp = frequencies[i]
        count = count + temp
    for i in frequencies:
        tempVal = frequencies[i]
        frequencies[i] = tempVal/count
    print(frequencies)
main()
