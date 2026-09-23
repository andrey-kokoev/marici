"""Normalize exact rational strings for mathematical packet hashes; reject floats."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json,re
pattern=re.compile(r'-?[0-9]+(?:/[0-9]+)?\Z')
def canonical(value):
 if not isinstance(value,str) or not pattern.fullmatch(value):raise ValueError('NONCANONICAL_OR_INEXACT_RATIONAL')
 try:q=Q(value)
 except ZeroDivisionError:raise ValueError('ZERO_DENOMINATOR') from None
 return str(q)
def H(packet):return sha256(json.dumps([canonical(x) for x in packet],separators=(',',':')).encode()).hexdigest()
a=['0','1','0','0','1'];b=['00','1/1','-0','0/1','2/2']
assert H(a)==H(b) and H(a)!=sha256(json.dumps(b).encode()).hexdigest()
assert canonical('-2/4')=='-1/2' and canonical('3/6')=='1/2'
for value in (1.0,'1.0','1e0',' 1','+1','NaN'):
 try:canonical(value)
 except ValueError as err:assert str(err)=='NONCANONICAL_OR_INEXACT_RATIONAL'
 else:raise AssertionError('inexact encoding accepted')
try:canonical('1/0')
except ValueError as err:assert str(err)=='ZERO_DENOMINATOR'
else:raise AssertionError('division zero accepted')
report={'passed':True,'equivalent_integer_fraction_lexemes':'same normalized packet digest','negative_half':'-2/4 -> -1/2','float_decimal_exponent_and_whitespace':'refused','zero_denominator':'refused','scope':'Local exact arithmetic normalization only, no publisher signature, event identity or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/canonical-rational-packet.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
