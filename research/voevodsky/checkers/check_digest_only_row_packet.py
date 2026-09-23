"""Digest binds disclosed rows but cannot substitute for undisclosed coefficients."""
from hashlib import sha256
from pathlib import Path
import json
names=('x-low','x-high','y-low','y-high')
a=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
altered=(((-2,0),0),)+a[1:]
m=(0,1,0,1);target=((1,1),2)
def digest(rows):return sha256(repr(('ordered-rows-v1',names,rows)).encode()).hexdigest()
commitment=digest(a)
def verify(rows,claimed):
 if rows is None:raise ValueError('ROW_MATRIX_UNDISCLOSED')
 if digest(rows)!=claimed:raise ValueError('MANIFEST_OPENING_MISMATCH')
 got=(tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4)))
 if got!=target:raise ValueError('FARKAS_EQUATION_MISMATCH')
 return 'LOCAL_MATH_VERIFIED'
try:verify(None,commitment)
except ValueError as err:assert str(err)=='ROW_MATRIX_UNDISCLOSED'
else:raise AssertionError('hash treated as rows')
assert verify(a,commitment)=='LOCAL_MATH_VERIFIED'
assert digest(altered)!=commitment and (tuple(sum(altered[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(altered[i][1]*m[i] for i in range(4)))==target
try:verify(altered,commitment)
except ValueError as err:assert str(err)=='MANIFEST_OPENING_MISMATCH'
else:raise AssertionError('different manifest with same target accepted')
report={'passed':True,'digest_only':'ROW_MATRIX_UNDISCLOSED','correct_opening':'LOCAL_MATH_VERIFIED','unused_row_change_same_packet_target':'MANIFEST_OPENING_MISMATCH','issuer_status':'UNAUTHENTICATED; mathematical opening is not row publisher grant','scope':'Fixed local encoding, digest integrity conditional on disclosed rows; not a zero-knowledge proof or cryptographic issuer attestation.'}
out=Path(__file__).resolve().parents[1]/'results/digest-only-row-packet.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
