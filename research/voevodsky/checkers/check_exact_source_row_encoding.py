"""Canonical source row digests require exact rational values and ordered rows."""
from hashlib import sha256
from fractions import Fraction
from pathlib import Path
import json,re
rx=re.compile(r'-?[0-9]+(?:/[0-9]+)?\Z')
def rational(x):
 if type(x) is int:return str(x)
 if type(x) is not str or not rx.fullmatch(x):raise ValueError('INEXACT_ROW_BOUND')
 try:return str(Fraction(x))
 except ZeroDivisionError:raise ValueError('ZERO_DENOMINATOR') from None
def manifest(rows):
 normalized=[]
 for row in rows:
  if set(row)!={'normal','bound'} or len(row['normal'])!=2:raise ValueError('INVALID_ROW_SHAPE')
  normalized.append({'normal':[rational(v) for v in row['normal']],'bound':rational(row['bound'])})
 return sha256(json.dumps({'schema':'ordered-rational-rows@1','rows':normalized},sort_keys=True,separators=(',',':')).encode()).hexdigest()
a=[{'normal':[1,0],'bound':1},{'normal':[0,1],'bound':'2/2'}]
b=[{'normal':['1/1','0/1'],'bound':'01/1'},{'normal':[0,1],'bound':1}]
assert manifest(a)==manifest(b) and manifest(a)!=manifest(list(reversed(a)))
for bad in (1.0,True,'1.0','1e0'):
 try:manifest([{'normal':[1,0],'bound':bad}])
 except ValueError as err:assert str(err)=='INEXACT_ROW_BOUND'
 else:raise AssertionError('loose row bound accepted')
report={'passed':True,'exact_equivalent_rationals':'same manifest digest','row_reordering':'different digest','float_boolean_decimal_exponent':'rejected','scope':'Local ordered row encoding only, not owner-issued source or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/exact-source-row-encoding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
