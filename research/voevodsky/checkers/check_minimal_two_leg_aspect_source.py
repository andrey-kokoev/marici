#!/usr/bin/env python3
"""Exact integral audit of the minimal coupled two-leg source complex."""
from functools import reduce
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/minimal_two_leg_source_complex_for_aspect_target.md';RESULT=ROOT/'research/voevodsky/results/minimal_two_leg_aspect_source.json';CONTRACT=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
c=json.loads(CONTRACT.read_text(encoding='utf-8'));D=s.Matrix(c['residue_map']);dA=s.Matrix([[1,-1]]);F1=s.eye(2);F0=s.Matrix([1,-1,1]);cycle=s.Matrix([1,1]);checks={}
checks['chain_square']=D*F1==F0*dA
checks['source_cycle']=dA*cycle==s.zeros(1,1)
checks['cycle_image_target']=F1*cycle==s.Matrix(c['target_relative_cocycle'])
source_betti={'1':2-dA.rank(),'0':1-dA.rank()};checks['source_homology']=source_betti=={'1':1,'0':0}
d2=F1.col_join(-dA);d1=D.row_join(F0);checks['cone_square']=d1*d2==s.zeros(3,2);cone_betti={'2':2-d2.rank(),'1':3-d1.rank()-d2.rank(),'0':3-d1.rank()};checks['cone_homology']=cone_betti=={'2':0,'1':0,'0':2}
def determinantal_gcd(M,r):
 vals=[]
 for rs in combinations(range(M.rows),r):
  for cs in combinations(range(M.cols),r):vals.append(abs(int(M.extract(rs,cs).det())))
 return reduce(gcd,vals,0)
checks['integral_primitivity']=determinantal_gcd(d2,2)==1 and determinantal_gcd(d1,1)==1 and gcd(*map(abs,list(dA)))==1
checks['individual_legs_noncycles']=dA*s.Matrix([1,0])!=s.zeros(1,1) and dA*s.Matrix([0,1])!=s.zeros(1,1)
text=PACKET.read_text(encoding='utf-8');checks['formal_gate_retained']='generators remain formal' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.minimal-two-leg-aspect-source.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'aspect_contract_sha256':sha256(CONTRACT.read_bytes()).hexdigest(),'source_differential':[[1,-1]],'map_degree_1':[[1,0],[0,1]],'map_degree_0':[[1],[-1],[1]],'source_betti':source_betti,'cone_differentials':{'d2':[list(map(int,d2.row(i))) for i in range(d2.rows)],'d1':[list(map(int,d1.row(i))) for i in range(d1.rows)]},'cone_betti':cone_betti,'checks':checks,'passed':all(checks.values()),'disposition':{'minimal_free_shape':'Z^2 --(1,-1)--> Z','geometric_status':'unrealized','next_object':'relative pair with two labelled chains and one shared oriented boundary class'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'source_betti':source_betti,'cone_betti':cone_betti,'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
