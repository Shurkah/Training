f = [32, 32, 32, 32, 47, 41, 47, 41, 10]
r = [32, 32, 32, 40, 32, 46, 46, 92]
i = [32, 32, 32, 32]
e = [111, 95, 95, 95, 111, 10, 32, 32, 32]
n = [47, 39, 45, 46, 95, 41, 32, 32, 32]
d = [40, 94, 46, 94, 41, 10, 32, 32, 47, 35, 47,]
s = [32, 32, 32, 32, 32, 32, 111, 47, 40]
h = [32, 41, 92, 111, 10, 32, 47, 35, 47, 32]
p = [32, 32, 79, 95, 46, 94, 46, 95, 79, 10]

inp = f+r+i+e+n+d+s+h+i+p

def ascii_to_symbols(*ascii_lists):
    result = []
    for ascii_list in ascii_lists:
        symbols = [chr(code) for code in ascii_list]
        result.append(''.join(symbols))
    return result

output_symbols = ascii_to_symbols(inp)

for i, output in enumerate(output_symbols):
    print(output)