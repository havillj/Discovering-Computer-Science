"""
Exercise 12.1.12

Discovering Computer Science, Second Edition
Jessen Havill
"""

class Senator:
    # your class goes here
    
def getSenators():
    senatorFile = open('senators.txt', 'r', encoding = 'utf-8')
    senators = []
    line = senatorFile.readline()
    while line != '':
        line = line.strip()
        name = line[:-7]
        party = line[-5]
        state = line[-3:-1]
        senator = Senator(name, party, state)
        line = senatorFile.readline()
        while line != '\n' and line != '':
            committee = line.strip()
            senator.addCommittee(committee)
            line = senatorFile.readline()
        senators.append(senator)
        line = senatorFile.readline()
    return senators

    
def main():
    pass
        
main()
