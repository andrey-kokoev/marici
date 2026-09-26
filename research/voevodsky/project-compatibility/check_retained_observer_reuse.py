"""Reuse an existing contraction theorem on two independently sourced packets."""
from pathlib import Path
import hashlib,json,runpy
import sympy as s
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
prior=ROOT/'research/voevodsky/consistency-complexes-retract-to-corrected-observers-while-discrepancies-kill-synchronized-classes.md'
paths=[Path(__file__),HERE/'retained-observer-construction-reuse.md',prior,HERE/'check_spectral_observer_completion.py',HERE/'check_readout_realized_pullback.py']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes()
a=runpy.run_path(str(paths[3]));b=runpy.run_path(str(paths[4]))
def check(i,r,d,h):
 n=i.cols;m=i.rows;k=d.rows
 assert r*i==s.eye(n)
 assert d*i==s.zeros(k,n)
 assert d*h==s.eye(k)
 assert r*h==s.zeros(n,k)
 assert s.simplify(i*r+h*d-s.eye(m))==s.zeros(m)
 assert (i*r)**2==i*r
 return {'source_rank':n,'packet_rank':m,'discrepancy_rank':k,'split_identities':True}
# The spectral source already supplies F,H,L; discrepancies occupy its first port.
spectral=check(a['F'],a['L'],a['H'],s.eye(3).col_join(s.zeros(3)))
# Actual sourced primitive and detector rows, not an independently fitted diagonal.
i=s.Matrix(b['detectors'])*s.Matrix(b['z'])
r=s.Matrix([[1,0,0]])
d=s.Matrix([[1,-1,0],[0,1,-1]])
h=s.Matrix([[0,0],[-1,0],[-1,-1]])
integral=check(i,r,d,h)
assert all(x.q==1 for M in (i,r,d,h) for x in M)
assert r*i==s.ones(1) and (-s.ones(1,3)*i)[0]%3==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'spectral':spectral,'integral':integral,'integral_denominators_inverted':False,'discrepancy_kills_source_in_both':True,'integral_trace_mod3_kills_source':True,'new_general_theorem':False,'physical_cross_sector_map_certified':False,'completion_certified':False,'scope':'Exact reuse of prior split contraction identities on existing finite source packets. Ambient discrepancy splitting is algebraic, not a sourced physical constructor.'}
(HERE/'retained-observer-construction-reuse.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
