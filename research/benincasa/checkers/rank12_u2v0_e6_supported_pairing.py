"""Supported pairing of the first-Rees e6 residue with the physical node boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-u2v0-e6-supported-pairing.json'

omega=[Fraction(-1,8),Fraction(1,8)]      # (e_plus^*,e_minus^*)
gamma=[-1,1]                              # e_minus-e_plus
pair=sum(x*y for x,y in zip(omega,gamma))
assert pair==Fraction(1,4)

# Face order (p,s,l), l=B-1.  The same universal Tate class is reached from
# each face, so its edge differences vanish.
face=[Fraction(-1,8)]*3
edge=[face[1]-face[0],face[2]-face[1],face[0]-face[2]]
assert edge==[0,0,0]

packet={
 'schema':'marici.benincasa.rank12_u2v0_e6_supported_pairing.v1',
 'sheet_order':['e_plus','e_minus'],
 'first_rees_covector':['-1/8','1/8'],
 'physical_boundary_vector':[-1,1],
 'pairing':'1/4',
 'support_face_order':['p','s','B-1'],
 'face_coefficients':['-1/8','-1/8','-1/8'],
 'edge_differences':['0','0','0'],
 'overlap_coherent':True,
 'physical_slice':{'s':1,'condition':'B-1 != 0','selected_face':'p'},
 'classification':'nonzero source-normalized rational supported pairing at first Rees order; integral target normalization remains separate'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))
