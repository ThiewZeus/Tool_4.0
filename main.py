# main.py
import marshal

with open("Tool", "rb") as f:
    code = marshal.loads(f.read())

exec(code)
#print(code)
