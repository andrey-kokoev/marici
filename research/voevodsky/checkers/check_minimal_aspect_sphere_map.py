#!/usr/bin/env python3
"""Check the minimal formal sphere map and its integral mapping cone."""
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/minimal_sphere_map_into_aspect_residue_complex.md';RESULT=ROOT/'research/voevodsky/results/minimal_aspect_sphere_map.json';CONTRACT=ROOT/'research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json'
c=json.loads(CONTRACT.read_text(encoding='utf-8'));D=s.Matrix(c['residue_map']);v=s.Matrix(c['target_relative_cocycle']);d2=v;d1=D
checks={}
checks['contract_vectors_exact']=D==s.Matrix([[1,-1],[-1,1],[1,-1]]) and v==s.Matrix([1,1])
checks['chain_square_zero']=d1*d2==s.zeros(3,1)
checks['target_kernel_rank_one']=2-D.rank()==1
checks['source_hits_full_kernel']=s.Matrix.hstack(v).columnspace()==D.nullspace()
# Integral primitivity: v and the generator of im(D) each have coordinate gcd one.
image_generator=D.col(0)
checks['kernel_generator_primitive']=gcd(*[abs(int(x)) for x in v])==1
checks['image_generator_primitive']=gcd(*[abs(int(x)) for x in image_generator])==1
cone_betti={'2':1-d2.rank(),'1':2-d1.rank()-d2.rank(),'0':3-d1.rank()}
checks['cone_betti_2_1_0']=cone_betti=={'2':0,'1':0,'0':2}
checks['formal_source_gate_retained']='formal and has no resolved/Rees or Cayley--Menger provenance' in PACKET.read_text(encoding='utf-8')
checks['aspect_authority_still_false']=c['source_authority_gate']['currently_constructed'] is False;checks={k:bool(vv) for k,vv in checks.items()}
result={'schema':'marici.voevodsky.minimal-aspect-sphere-map.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'aspect_contract_sha256':sha256(CONTRACT.read_bytes()).hexdigest(),'source_complex':{'degree_1_basis':['formal_e'],'differential':[[0]]},'target_differential':c['residue_map'],'map_degree_1':c['target_relative_cocycle'],'cone_betti':cone_betti,'integral_homology':{'H2':'0','H1':'0','H0':'Z^2'},'checks':checks,'passed':all(checks.values()),'disposition':{'algebraic_map':'complete minimal chain map','source_status':'formal_source_only','physical_status':'not verified','missing':'source-derived exceptional-generator identification and contour/readout authority'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'cone_betti':cone_betti,'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
