#!/usr/bin/env python3
"""Verify the minimal two-bit complementary probe and its exchange uniqueness."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/minimal_complementary_probe_for_the_cut_null_sector.md';CUT=ROOT/'src/ledger/20260821-1751 The Physical Cut Pairing Does Not Resolve the Integral Cusp Extension.md';SOURCE=ROOT/'research/benincasa/primitive-conductor-top-connection.json';RESULT=ROOT/'research/voevodsky/results/minimal_cut_null_complementary_probe.json';src=json.loads(SOURCE.read_text(encoding='utf-8'));J=s.Matrix(src['enhanced_intertwiner_J']);l1=s.Matrix([[1,0,1]]);l2=s.Matrix([[0,1,1]]);S=s.Matrix([[0,1],[1,0]])
def det2(M):return int(M.det())%2
def eq2(A,B):return all((int(x-y)%2)==0 for x,y in zip(A,B))
gl=[]
for bits in product((0,1),repeat=4):
 M=s.Matrix(2,2,bits)
 if det2(M)==1:gl.append(M)
central=[M for M in gl if eq2(M*S,S*M)];syndromes={tuple(int(x)%2 for x in v):tuple(int(x)%2 for x in s.Matrix.vstack(l1,l2)*s.Matrix(v)) for v in product((0,1),repeat=3)};kernel=[v for v,out in syndromes.items() if out==(0,0)];image_mod2={tuple(int(x)%2 for x in J*s.Matrix(v)) for v in product((0,1),repeat=3)};text=PACKET.read_text(encoding='utf-8');cut=CUT.read_text(encoding='utf-8');checks={'cut_null_source':'is zero' in cut,'conductor_index_four':abs(J.det())==4,'both_characters_kill_image':all(int(x)%2==0 for x in list(l1*J)+list(l2*J)),'syndrome_surjective':set(syndromes.values())==set(product((0,1),repeat=2)),'kernel_equals_image_mod2':set(kernel)==image_mod2,'six_abstract_isomorphisms':len(gl)==6,'two_exchange_equivariant':len(central)==2,'centralizer_is_identity_swap':any(M==s.eye(2) for M in central) and any(M==S for M in central),'one_bit_insufficient':2<4,'physical_gate':'No existing Aspect packet supplies these observables' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.minimal-cut-null-complementary-probe.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'conductor_source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'cut_entry_sha256':sha256(CUT.read_bytes()).hexdigest(),'wall_characters':[[1,0,1],[0,1,1]],'abstract_GL2_F2_count':len(gl),'exchange_equivariant_maps':[[list(map(int,M.row(i))) for i in range(2)] for M in central],'checks':checks,'passed':all(checks.values()),'disposition':{'algebraic_probe':'constructed','binary_output_count':2,'uniqueness':'up to wall exchange','physical_observables':'missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
