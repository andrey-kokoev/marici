"""Resolve-then-read is non-atomic; frozen bytes need digest and provenance."""
from hashlib import sha256
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
p=json.loads((root/'results/unsent-owner-handoff-payload.json').read_text())
item=p['local_evidence'][0];original=(root/item['path']).read_bytes();expected=item['sha256']
assert sha256(original).hexdigest()==expected
# Two-stage read model: first validate name/target; then adversary replaces bytes.
def read_after_validate(validated,read_bytes):
 if not validated:raise ValueError('PATH_NOT_VALIDATED')
 return read_bytes
replaced=read_after_validate(True,original+b'\n')
assert replaced!=original and sha256(replaced).hexdigest()!=expected
# A frozen byte snapshot avoids reading an altered path later; compare against
# payload commitment before attaching it, not merely when resolving the name.
attachment=bytes(original)
assert sha256(attachment).hexdigest()==expected
assert sha256(replaced).hexdigest()!=sha256(attachment).hexdigest()
# Identical bytes at a DIFFERENT physical source cannot be distinguished by a
# content digest: path/source provenance must be bound independently.
assert sha256(bytes(original)).hexdigest()==expected
report={'passed':True,'resolve_then_read':'race possible if bytes change between operations','changed_bytes_at_read':'EVIDENCE_DIGEST_DRIFT','immutable_verified_attachment':'matching frozen bytes under local model','same_bytes_different_origin':'digest insufficient to prove physical source or authority','physical_evidence_mutated':False,'authorization':'LOCAL_PREPARED_UNSENDABLE','scope':'Synthetic temporal model, not an OS-level race-free open/descriptor, authorized owner address or issuer attestation.'}
out=root/'results/evidence-file-swap-model.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
