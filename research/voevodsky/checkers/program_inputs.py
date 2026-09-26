"""Public constructor domain; explicit exceptions survive Python -O."""
def word(value):
 result=tuple(value)
 if any(type(x) is not int or x not in (0,1) for x in result):
  raise ValueError('word must contain exact integer bits 0 or 1')
 return result

def natural(value):
 if type(value) is not int or value<0:raise ValueError('index/fuel must be a nonnegative exact integer')
 return value

def program(value,allowed):
 result=[]
 for instruction in value:
  pair=tuple(instruction)
  if len(pair)!=2:raise ValueError('instruction must have exactly two fields')
  op,arg=pair
  if not isinstance(op,str) or op not in allowed:raise ValueError('unsupported instruction')
  if op=='union':arg=word(arg)
  elif op in ('ifadd','scan'):
   arg=tuple(arg)
   if len(arg)!=(3 if op=='ifadd' else 2):raise ValueError('wrong operand arity')
   arg=tuple(natural(x) for x in arg)
  else:arg=natural(arg)
  result.append((op,arg))
 return result
