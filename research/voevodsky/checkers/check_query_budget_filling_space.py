"""The unbounded-query obstruction as conditional fibers of one source space.

H binary zero-frame memberships give 2^H admitted refinements. A partial
query boundary fixes selected memberships; its filling fiber is a Boolean
subcube. Test every partial boundary on the owning ten-coordinate family.
"""
from pathlib import Path
from itertools import product
import subprocess
import sys
import json
import hashlib
ROOT=Path(__file__).resolve().parents[3]
N=ROOT/'research/nima';OUT=ROOT/'research/voevodsky/results'
p=N/'results/certified-forgetting-storage-obstruction-packet.json'
cpath=N/'results/certified-forgetting-storage-obstruction-contract.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
owner=json.loads(cpath.read_text());coords=owner['finite_test']['probe_coordinates'];H=len(coords);full=(1<<H)-1
cp=OUT/'query-budget-filling-space-contract.json'
save(cp,{'packet_sha256':sha(p),'owning_contract_sha256':sha(cpath),
 'filling_space':'Admitted zero-frame refinement sets J on the owning H query coordinates; each has the owning feasible infinite-tail witness.',
 'boundary':'Partial assignment of query answers; fixed origin, source path, optimum and current certificate.',
 'fiber':'All J whose source-certified answers match that partial assignment.',
 'prediction':'Every consistent partial boundary has exactly 2^(H-k) fillings, and compatible boundaries glue by intersection. Full query contexts still distinguish all 2^H fillings.',
 'scope':'Evidence-carrier fillings, not unique microscopic tail realizations. Budget counts bits, not number of formal geometric coordinates.'})
subprocess.run([sys.executable,str(N/'checkers/verify_certified_forgetting_storage_obstruction.py')],check=True,capture_output=True,text=True)
d=json.loads(p.read_text());histories=d['histories']
assert len(histories)==1<<H
masks={h['mask'] for h in histories};assert masks==set(range(1<<H))
# Bit n=1 means zero frame present, hence feasibility probe answer false.
for h in histories:
 assert h['future_feasibility']==[not bool(h['mask']&(1<<i)) for i in range(H)]

def fiber(z,o):
 assert not z&o
 return frozenset(m for m in masks if m&z==0 and m&o==o)

def boundary_id(z,o):return z,o
fibers={};size_counts={};total_incidences=0
for pattern in product((-1,0,1),repeat=H):
 z=sum(1<<i for i,b in enumerate(pattern) if b==0)
 o=sum(1<<i for i,b in enumerate(pattern) if b==1)
 K=fiber(z,o);k=(z|o).bit_count()
 assert len(K)==1<<(H-k)
 fibers[z,o]=K;size_counts[len(K)]=size_counts.get(len(K),0)+1
 total_incidences+=len(K)
assert len(fibers)==3**H and total_incidences==4**H
# Every one-coordinate boundary extension, including disagreement. Generator
# intersection identities imply arbitrary finite gluing and regrouping.
glue_checks=conflicts=0
for (z,o),K in fibers.items():
 for i in range(H):
  for value in (0,1):
   bit=1<<i
   atomic=fibers[(bit,0) if value==0 else (0,bit)]
   nz,no=(z|bit,o) if value==0 else (z,o|bit)
   common=K&atomic
   if nz&no:
    assert not common;conflicts+=1
   else:
    assert common==fibers[nz,no]
   glue_checks+=1
# General information lower bound: all complete assignments are singleton
# fillings; a differing bit is an independently justified separating query.
separators=0
for difference in range(1,1<<H):
 i=(difference&-difference).bit_length()-1
 assert (0&(1<<i)) != (difference&(1<<i))
 separators+=1
assert len(fibers[0,0])==1024
assert sha(p)==json.loads(cp.read_text())['packet_sha256']
report={'passed':True,'contract_sha256':sha(cp),'source_refinement_fillings':1<<H,
 'partial_boundaries':len(fibers),'filling_incidences':total_incidences,
 'fiber_size_histogram':{str(k):v for k,v in sorted(size_counts.items())},
 'single_query_gluing_checks':glue_checks,'contradictory_extensions_rejected':conflicts,
 'separating_difference_checks':separators,
 'unconditioned_current_certificate_fiber':1<<H,
 'obstruction_type':'Representation cardinality, not source gluing: every consistent query boundary has admitted fillings and exact intersection gluing.',
 'general_result':'For H independent admitted probes, complete boundaries distinguish 2^H fillings. Exact query-complete presentation needs at least H bits. With unbounded H no uniform finite bit bound exists.',
 'interpretation':'A compact formula can describe the whole filling family, while naming or answering for an arbitrary member requires increasing information. Changing orientation of the membership relation does not alter that separating family.',
 'scope':'Restricted owning zero-frame/query family; no general undecidability or physical-source reconstruction claim.'}
save(OUT/'query-budget-filling-space.json',report)
print(json.dumps(report,indent=2))
