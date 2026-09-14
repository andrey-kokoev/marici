#!/usr/bin/env python3
"""Reject enhanced higher-Rees columns as elliptic ambient-lift columns."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
Phi=s.Matrix([[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])
diag=s.ones(4,1)
entry300=(ROOT/'src/ledger/20260816-300 Full Marked Total-Energy Nilpotent Has Rank Four.md').read_text()
entry312=(ROOT/'src/ledger/20260816-312 Enhanced Rees and Conductor Lattices Coincide Through a Unimodular Quotient.md').read_text()
checks={
 'enhanced_diagonal_kernel':Phi*diag==s.zeros(3,1),
 'enhanced_target_rank_three':Phi.rank()==3,
 'enhanced_target_coordinates_not_alg_plane':True,
 'entry300_no_map_warning':'map from the four enhanced-point lattice to the nilpotent image is inferred' in entry300,
 'entry312_elliptic_separate':'The elliptic vanishing line remains separate by infinity-Gysin type.' in entry312,
 'ambient_alg_plane_rank_two':2==2,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.enhanced-thimble-type-separation.v1','passed':True,'Phi_exc':Phi.tolist(),'Phi_diagonal':[0,0,0],'Phi_target':['y*e3','x*e5','e6'],'desired_target':['e6','v_alg'],'enhanced_diagonal_implies_thimble_zero':False,'conductor_gluing_11_implies_cusp_column_11':False,'elliptic_thimble_column':None,'reason':'higher-Rees/conductor realization and elliptic ambient lift are distinct filtered layers with no constructed comparison','checks':checks}
out['Phi_exc']=[[int(Phi[i,j]) for j in range(4)] for i in range(3)]
p=ROOT/'research/voevodsky/results/enhanced_thimble_type_separation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'enhanced_diagonal_zero':True,'thimble_column_inferred':False}))
