import re

with open("preproinsulin-seq.txt", 'r') as source: 
    seq = source.read()
    
print(seq)

semistripped = seq[(seq.find('GIN') +3) : seq.find('//')]
numstripped = semistripped.replace(' ', '').replace('\n', '')
stripped = re.sub(r'\d', '', numstripped)
print(stripped)

print('Preproinsulin character count : ', len(stripped))

with open('preproinsulin-seq-clean.txt', 'w') as output: 
    output.write(stripped)
    

filename = 'Isinsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(stripped[:24])
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), ' characters')
    

filename = 'binsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(stripped[24:54])
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), ' characters')


filename = 'cinsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(stripped[54:89])
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), ' characters')


filename = 'ainsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(stripped[89:])
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), ' characters')
    

