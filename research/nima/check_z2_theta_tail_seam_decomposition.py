#!/usr/bin/env python3
"""Finite toy of wall identity plus retained theta-tail/seam history."""
import itertools,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];G=list(itertools.product((0,1),repeat=2))
def add(x,y):return (x[0]^y[0],x[1]^y[1])
def conv(f,v):return {x:sum(f[add(x,y)]*v[y] for y in G) for x in G}
def aug(v):return sum(v.values())
def sub(a,b):return {x:a[x]-b[x] for x in G}
def plus(a,b):return {x:a[x]+b[x] for x in G}
def show(v):return {str(x):str(v[x]) for x in G}
e={x:Fraction(x==(0,0)) for x in G};f=dict(zip(G,map(Fraction,(2,1,3,-2))));g=dict(zip(G,map(Fraction,(1,2,-1,3))))
resolved=conv(f,e);mass=aug(resolved);wall={x:mass/Fraction(4) for x in G};tail=sub(resolved,wall);full_next=conv(g,resolved);wall_next=conv(g,wall);tail_next=conv(g,tail);reconstructed=plus(wall_next,tail_next)
out={'schema':'marici.nima.z2-theta-tail-seam-decomposition.v1','resolved':show(resolved),'wall_identity_channel':show(wall),'theta_tail_seam_channel':show(tail),'wall_mass':str(mass),'tail_augmentation':str(aug(tail)),'next_full_state':show(full_next),'next_wall_only_state':show(wall_next),'next_transported_tail':show(tail_next),'next_reconstructed_state':show(reconstructed),'checks':{'exact_wall_plus_tail_split':resolved==plus(wall,tail),'tail_is_in_augmentation_kernel':aug(tail)==0,'tail_survives_resolved_transport':any(v!=0 for v in tail_next.values()),'wall_only_loses_information':wall_next!=full_next,'tail_restores_full_history':reconstructed==full_next,'scalar_augmentation_cannot_detect_tail':aug(wall_next)==aug(full_next)}}
out['passed']=all(out['checks'].values());out['interpretation']='The wall is the trivial character projection; the zero-augmentation complement is transported tail/seam memory required for exact multiphase reconstruction.'
p=ROOT/'research/nima/results/z2-theta-tail-seam-decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
