import re

p = re.compile("ca.e")

m = p.match("case")

def print_match(m):
    if m:
        print("m.group():", m.group())
        print("m.string:", m.string)
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")
    
m = p.match("careless")
print_match(m)
    
m = p.search("good care")    

m = p.findall("careless")