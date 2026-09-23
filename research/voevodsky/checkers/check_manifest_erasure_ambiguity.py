"""Ordered rows reconstruct local digest; labels alone cannot reconstruct rows."""
from hashlib import sha256
from pathlib import Path
import json
names=('x-low','x-high','y-low','y-high')
a=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
b=(((-1,0),0),((2,0),2),((0,-1),0),((0,1),1))
c=(((-2,0),0),((1,0),1),((0,-1),0),((0,1),1))
m=(0,1,0,1)
def digest(rows):return sha256(repr(('ordered-rows-v1',names,rows)).encode()).hexdigest()
def image(rows):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))
assert digest(a)!=digest(b)!=digest(c) and digest(a)!=digest(c)
assert image(a)==((1,1),2) and image(b)==((2,1),3)
assert image(c)==image(a) # unused row changes manifest but not this proof
assert names==names and m==m
assert digest(a)==digest(tuple(a))
report={'passed':True,'digest_reconstructible_from_complete_ordered_rows_under_fixed_encoding':True,'erased_rows_and_digest':'same names/multipliers compatible with distinct target and source manifest','unused_row_change':'same selected proof target but distinct source manifest','manifest_A_digest':digest(a),'manifest_B_digest':digest(b),'manifest_C_digest':digest(c),'scope':'Local canonical repr encoding v1, not interoperable serialization or issuer attestation. Row labels do not uniquely identify primitive coefficients.'}
out=Path(__file__).resolve().parents[1]/'results/manifest-erasure-ambiguity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
