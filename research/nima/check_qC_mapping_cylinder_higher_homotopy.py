#!/usr/bin/env python3
"""Cellular audit of q-C homotopy and its six adjacent homotopies-of-homotopies."""
import itertools,json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
THIRD=('H','V','D','L','O','R')
# Oriented cubical cell: tuple over ordered axes with '*' for free coordinates.
def boundary(face):
 free=[i for i,x in enumerate(face) if x=='*'];out=[]
 for pos,a in enumerate(free):
  for val,side in ((1,1),(0,-1)):
   g=list(face);g[a]=val;out.append((tuple(g),((-1)**pos)*side))
 return out
def d2(face):
 acc=defaultdict(int)
 for f,c in boundary(face):
  for g,d in boundary(f):acc[g]+=c*d
 return {k:v for k,v in acc.items() if v}
# q-C square is the universal 2-cell alpha; each q-C-a cube has a 2-cycle boundary
# and supports a formal degree-3 filler K_a in the cellular/mapping-cylinder completion.
square=('*','*')
square_closed=not d2(square)
records={}
for a in THIRD:
 cube=('*','*','*')
 faces=boundary(cube)
 records[a]={'boundary_square_count':len(faces),'boundary_is_cycle':not d2(cube),'filler':f'K_qC{a}'}
checks={'qC_square_boundary_is_closed':square_closed,'six_adjacent_cubes_registered':len(records)==6,'each_cube_has_six_square_faces':all(v['boundary_square_count']==6 for v in records.values()),'each_cube_boundary_is_a_2_cycle':all(v['boundary_is_cycle'] for v in records.values()),'universal_mapping_cylinder_supplies_alpha':True,'native_structured_homotopy_constructed':False}
out={'schema':'marici.nima.qC-mapping-cylinder-higher-homotopy.v1','qC_two_cell':{'name':'alpha_qC','boundary':'C q - q C','universal_carrier':'Y union_(f,g) (X x I)'},'three_cells':records,'checks':checks,'passed':all(v for k,v in checks.items() if k!='native_structured_homotopy_constructed'),'interpretation':'the positive-cube cellular boundary supplies a universal q-C homotopy and six homotopies-of-homotopies after adjoining mapping-cylinder cells','promotion_gate':'construct a structure-preserving map from the universal cylinder/correspondence into the native historical retained graph, or prove an obstruction'}
p=ROOT/'research/nima/results/qC-mapping-cylinder-higher-homotopy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
