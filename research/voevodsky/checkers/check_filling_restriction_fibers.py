"""Restriction fibers for actual local observers, with independent boundary factors.

W is the 70 admitted behavioral states. Boundaries u,v,x,w are exact pair
projections of four already existing observer coordinates. Factorizations are
fiber products of those projections, NOT defined from W to force equivalence.
Witness identity is discrete behavioral-state identity in this finite test.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import subprocess
import json
import sys
import hashlib
ROOT=Path(__file__).resolve().parents[3]
N=ROOT/'research/nima'; OUT=ROOT/'research/voevodsky/results'
p=N/'results/relational-live-witness-runtime.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
cp=OUT/'filling-restriction-fibers-contract.json'
save(cp,{'packet_sha256':sha(p),
 'filling_space':'70 source-admitted behavioral witness rows, with discrete identity.',
 'boundaries':{'a':'source-only local quotient value','b':'acquisition-only local quotient value','c':'recipient-only local quotient value','d':'faithfully retained origin bit'},
 'edge_types':'Exact admitted pair images u=(a,b),v=(b,c),x=(a,d),w=(d,c); each edge has unit membership witness.',
 'maps':'Restrict each filling to (a,b,c) or (a,d,c). For fixed (a,c), these land in the two independent edge fiber products.',
 'prediction':'Each restriction has singleton fibers over every locally compatible factorization.',
 'scope':'Tests set-level equivalence. Discrete singleton means contractible here; no nontrivial homotopy identification is introduced.'})
subprocess.run([sys.executable,str(N/'checkers/verify_relational_membership_live_witness.py')],check=True,capture_output=True,text=True)
rows=json.loads(p.read_text())['lifted_rows']
W=[(*r['views'],r['origin']) for r in rows]
assert len(set(W))==70
u={(a,b) for a,b,c,d in W};v={(b,c) for a,b,c,d in W}
x={(a,d) for a,b,c,d in W};w={(d,c) for a,b,c,d in W}
UV={(a,b,c) for a,b in u for bb,c in v if b==bb}
XW={(a,d,c) for a,d in x for dd,c in w if d==dd}
fuv={t:[] for t in UV};fxw={t:[] for t in XW}
for i,(a,b,c,d) in enumerate(W):
 fuv[a,b,c].append(i);fxw[a,d,c].append(i)
def audit(fibers):
 hist=defaultdict(int)
 for f in fibers.values():hist[len(f)]+=1
 return {'domain_factorizations':len(fibers),'fiber_size_histogram':dict(sorted(hist.items())),
         'empty_examples':[{'boundary':list(t),'fiber':f} for t,f in sorted(fibers.items()) if not f][:3],
         'multiple_examples':[{'boundary':list(t),'fiber':f} for t,f in sorted(fibers.items()) if len(f)>1][:3],
         'equivalence':all(len(f)==1 for f in fibers.values())}
uv,xw=audit(fuv),audit(fxw)
# Source-admitted triples as retained factors may repair existence but need
# not repair witness multiplicity. Verify both distinctions separately.
actual_uv={t for t,f in fuv.items() if f};actual_xw={t for t,f in fxw.items() if f}
quad={(a,b,c,d) for a,b,c in UV for aa,d,cc in XW if a==aa and c==cc}
qfib={q:[] for q in quad}
for i,t in enumerate(W):qfib[t].append(i)
# The full boundary tuple is injective because runtime keys contain views+bit.
assert all(len(f)<=1 for f in qfib.values())
assert sum(bool(f) for f in qfib.values())==70
# Verify paired restriction recovers every admitted filling, independent of
# whether all formally matched edge factorizations are realizable.
paired={((a,b,c),(a,d,c)):i for i,(a,b,c,d) in enumerate(W)}
assert len(paired)==70
assert sha(p)==json.loads(cp.read_text())['packet_sha256']
report={'passed':True,'contract_sha256':sha(cp),'filling_witnesses':70,
 'edge_counts':{'u':len(u),'v':len(v),'x':len(x),'w':len(w)},
 'uv_restriction':uv,'xw_restriction':xw,'four_edge_assembly':audit(qfib),
 'actual_uv_image':len(actual_uv),'actual_xw_image':len(actual_xw),
 'paired_restriction_injective':True,
 'interpretation':'Zero fibers obstruct existence; multiple discrete fibers obstruct uniqueness/equivalence. Both restrictions must be tested rather than inferred from a rotated picture.',
 'source_witness_rows':W,
 'scope':'Actual independently admitted behavioral carrier, but this four-boundary arrangement is newly declared for the test. Results concern these particular observer projections.'}
save(OUT/'filling-restriction-fibers.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='source_witness_rows'},indent=2))
