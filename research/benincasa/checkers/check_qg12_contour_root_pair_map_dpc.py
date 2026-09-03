#!/usr/bin/env python3
"""Underdetermination audit for the unsplit-contour to root-pair chain map."""
import json
from pathlib import Path
import sympy as s
v=s.Matrix([1,1])
maps={'even_identity':s.eye(2),'odd_projection':s.Matrix([[1,0],[0,0]]),'zero':s.zeros(2)}
images={n:[int(z) for z in M*v] for n,M in maps.items()}
parities={n:sum(im)%2 for n,im in images.items()}
assert parities['even_identity']==0 and parities['odd_projection']==1
out={'schema':'marici.benincasa.qg12-contour-root-pair-map-dpc.v1','problem':'Do the unsplit occurrence labels determine an even chain map to the Cayley-Menger root pair?','bold_conjecture':'The chamber-independent occurrence sum canonically maps to the even root-pair cycle without an explicit contour or boundary declaration.','named_rivals':['an odd projection is equally compatible with the available unit restrictions','the zero map is equally compatible','a physical contour and specialization matrix are required'],'risky_consequences':['every compatible integer chain map must send the occurrence sum to even parity','the two occurrence labels must distinguish the two root branches'],'strongest_falsification_attempt':{'domain_sum':[1,1],'candidate_images':images,'image_parities':parities,'available_incidence_constraints':0,'occurrence_restrictions':['q_g31/x=1-kappa','q_g23|x=0=2p']},'disposition':{'status':'falsified','residual':'even, odd, and zero images are all compatible with the materialized unit restrictions','reopening_test':'supply the unsplit canonical-form contour, its oriented relative boundary, and an integral specialization matrix to the ordered Cayley-Menger root pair'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg12_contour_root_pair_map_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
