def hello_name(name):
  return "Hello "+name+"!"
  
def make_abba(a, b):
  return a+b*2+a

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"
  
def make_out_word(out, word):
  return out[0:len(out)/2]+word+out[len(out)/2:len(out)]
  
def extra_end(str):
  return str[-2:]*3
  
def first_two(str):
  if len(str)>2:
    return str[0:2]
  return str

def first_half(str):
  return str[0:len(str)/2]
  
def without_end(str):
  return str[1:len(str)-1]
  
def combo_string(a, b):
  if len(a)>len(b):
    return b+a+b
  return a+b+a
  
def non_start(a, b):
  s=""
  if len(a)>1:s=s+a[1:]
  if len(b)>1:s=s+b[1:]
  return s
  
def left2(str):
  s=str[2:]
  s=s+str[0:2]
  return s
  
