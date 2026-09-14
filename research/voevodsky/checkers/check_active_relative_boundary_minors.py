#!/usr/bin/env python3
"""Classify active-boundary minors of the source intersection matrix."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/active_relative_boundary_restriction_has_exactly_two_nondegenerate_parity_minors.md';RESULT=ROOT/'research/voevodsky/results/active_relative_boundary_minors.json';PAGE=ROOT/'references/extractions/pdf-search-all/cosmology-meets-cohomology-2308-03753/pdf-page-0021.txt'
C=s.Matrix([[0,-1,1,0],[1,0,0,0],[1,1,0,1],[-1,0,1,-1]]);rows=[0,2,3];minors=[]
for omit in range(4):
 cols=[j for j in range(4) if j!=omit];M=C.extract(rows,cols);chars=[]
 for bits in product((0,1),repeat=3):
  if any(bits) and all(int(v)%2==0 for v in s.Matrix([bits])*M):chars.append(list(bits))
 smith=[abs(int(smith_normal_form(M,domain=ZZ)[i,i])) for i in range(3)] if M.det()!=0 else None;minors.append({'omitted_column':omit+1,'matrix':[list(map(int,M.row(i))) for i in range(3)],'determinant':int(M.det()),'smith_invariants':smith,'nonzero_mod2_left_characters':chars})
checks={'determinant_census':[m['determinant'] for m in minors]==[2,0,0,2],'exactly_two_nondegenerate':sum(m['determinant']!=0 for m in minors)==2,'nondegenerate_columns':[m['omitted_column'] for m in minors if m['determinant']!=0]==[1,4],'nondegenerate_smith':all(m['smith_invariants']==[1,1,2] for m in minors if m['determinant']!=0),'active_character':all(m['nonzero_mod2_left_characters']==[[1,1,1]] for m in minors if m['determinant']!=0),'singular_middle_omissions':minors[1]['determinant']==0 and minors[2]['determinant']==0,'subquotient_gate_retained':'not yet admitted relative subquotients' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.active-relative-boundary-minors.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'source_page_sha256':sha256(PAGE.read_bytes()).hexdigest(),'active_rows':['S3','S23','S13'],'minors':minors,'checks':checks,'passed':all(checks.values()),'disposition':{'candidate_omissions':[1,4],'arithmetic_type':'Smith (1,1,2)','connection_stability':'untested','relative_subquotient':'unverified'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'determinants':[m['determinant'] for m in minors],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
