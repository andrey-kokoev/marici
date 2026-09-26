"""Exact row rational grammar collapses negative zero and rejects signed denominators."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,re
rx=re.compile(r'-?[0-9]+(?:/[0-9]+)?\Z')
def norm(x):
 if not isinstance(x,str) or not rx.fullmatch(x):raise ValueError('ROW_RATIONAL_GRAMMAR')
 try:return str(Fraction(x))
 except ZeroDivisionError:raise ValueError('ZERO_DENOMINATOR') from None
def H(x):return sha256(json.dumps({'schema':'row-rational@1','bound':norm(x)},sort_keys=True).encode()).hexdigest()
assert norm('-0')==norm('-0/2')==norm('00')=='0' and H('-0')==H('0/2')
assert norm('-2/4')=='-1/2'
for x in ('1/-2','-1/-2','+1/2','--1',' 0','0 ','1/0'):
 try:norm(x)
 except ValueError as err:assert str(err) in ('ROW_RATIONAL_GRAMMAR','ZERO_DENOMINATOR')
 else:raise AssertionError(f'bad grammar accepted: {x}')
report={'passed':True,'negative_zero':'-0, -0/2, 0/2 normalize to 0','negative_half':'-2/4 reduces to -1/2','signed_denominator_and_whitespace':'refused','zero_denominator':'refused','scope':'Local rational encoding, no authenticated source issuer or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/source-row-zero-grammar.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
