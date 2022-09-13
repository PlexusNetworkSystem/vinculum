import ast

def kontrol(dosya):
    try:
        ast.parse(dosya)
        return True
    except SyntaxError:
        return False
#Created by https://github.com/datheia
