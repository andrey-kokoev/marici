"""Two matching byte providers substitute for math, not event-bound authority."""
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
encode=lambda r:json.dumps(r,separators=(',',':')).encode()
digest=sha256(encode(rows)).hexdigest()
class Provider:
 def __init__(self,name,event,source):self.name=name;self.event=event;self.source=source;self.rows=rows;self.live=True
 def read(self,source,event=None):
  if not self.live or self.rows is None:raise PermissionError('PROVIDER_UNAVAILABLE')
  if self.source!=source:raise PermissionError('FOREIGN_SOURCE')
  if event is not None and self.event!=event:raise PermissionError('FOREIGN_EVENT')
  if sha256(encode(self.rows)).hexdigest()!=digest:raise ValueError('ROW_DIGEST_MISMATCH')
  return self.rows
A=Provider('archive-A','event-A','unit-square');B=Provider('archive-B','event-B','unit-square')
def mathematical_replay(r):
 p=(1,2,0,0);q=(0,1,1,1);k=tuple(q[i]-p[i] for i in range(4))
 image=lambda m:(tuple(sum(r[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(r[i][1]*m[i] for i in range(4)))
 return image(p)==image(q)==((1,0),2) and image(k)==((0,0),0)
assert mathematical_replay(A.read('unit-square','event-A'))
assert mathematical_replay(B.read('unit-square','event-B'))
A.live=False;A.rows=None
try:A.read('unit-square','event-A')
except PermissionError:pass
else:raise AssertionError('revoked archive read')
assert mathematical_replay(B.read('unit-square'))
try:B.read('unit-square','event-A')
except PermissionError as e:assert str(e)=='FOREIGN_EVENT'
else:raise AssertionError('B promoted to A provenance')
try:B.read('different-source')
except PermissionError as e:assert str(e)=='FOREIGN_SOURCE'
else:raise AssertionError('cross-source math silently promoted')
B.rows=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),1))
try:B.read('unit-square')
except ValueError:pass
else:raise AssertionError('changed bytes accepted')
B.rows=rows
size=len(encode(rows));assert size>0
report={'passed':True,'matching_provider_rows_digest':digest,'archive_A_revoked_and_removed':True,'archive_B_fresh_math_replay':True,'archive_B_cannot_answer_A_event':True,'foreign_source_and_mutated_rows_refused':True,'serialized_row_payload_bytes_each':size,'two_payload_receipt_fields_sum':2*size,'scope':'Hypothetical process-local provider labels and availability, not independently authenticated owners; byte receipts exclude shared code, provenance proof, heap and physical storage.'}
out=Path(__file__).resolve().parents[1]/'results/dual-archive-substitution.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
