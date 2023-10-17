import re


# Python 3.7.16
# encoding utf-8


# Get the raw preproinsulin sequence

with open("preproinsulin-seq.txt", 'r') as source: 
    seq = source.read()
    
print(seq)


# Store the human preproinsulin sequence in a variable called preproinsulin:

semistripped = seq[(seq.find('GIN') +3) : seq.find('//')]
stripped = semistripped.replace(' ', '').replace('\n', '')
preproInsulin = re.sub(r'\d', '', stripped)
print(preproInsulin)

print('Preproinsulin character count : ', len(stripped))

with open('preproinsulin-seq-clean.txt', 'w') as output: 
    output.write(stripped)
    

IsInsulin = stripped[:24]
bInsulin = stripped[24:54]
cInsulin = stripped[54:89]
aInsulin = stripped[89:]

filename = 'Isinsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(IsInsulin)
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), 'IsInsulin characters')
    

filename = 'binsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(bInsulin)
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), 'bInsulin characters')


filename = 'cinsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(cInsulin)
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), 'cInsulin characters')


filename = 'ainsulin-seq-clean.txt'
with open(filename, 'w') as output: 
    output.write(aInsulin)
    
with open(filename, 'r') as source: 
    numtest = source.read()
    print(len(numtest), 'aInsulin characters')
    
    
insulin = bInsulin + aInsulin
    

# Printing insulin
print('The sequence of human preproinsulin: ')
print(preproInsulin)

# Printing with +
print('The sequence of human insulin, chain a: ' + aInsulin)



# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  

print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))


molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - //
    molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
