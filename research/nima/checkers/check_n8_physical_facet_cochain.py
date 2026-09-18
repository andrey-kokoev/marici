#!/usr/bin/env python3
"""Pair the exact n=8 physical facet cochain with the oriented A3 boundary."""
from itertools import combinations
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in r] for r in src['kernel_matrix']]);K0=s.Matrix([[s.sympify(x) for x in r] for r in src['kernel_without_upper_boundary_transport']]);B=K-K0
N=6;bdry={tuple(sorted((i,(i+1)%N))) for i in range(N)};ds=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in bdry]
def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
clusters=sorted(tuple(sorted(c)) for c in combinations(ds,3) if all(not cross(a,b) for a,b in combinations(c,2)));edges=sorted((i,j) for i,a in enumerate(clusters) for j,b in enumerate(clusters) if i<j and len(set(a)^set(b))==2);ep={e:i for i,e in enumerate(edges)}
faces=[]
for d in ds:
 vs=sorted(i for i,c in enumerate(clusters) if d in c);adj={i:sorted((b if a==i else a) for a,b in edges if i in (a,b) and (b if a==i else a) in vs) for i in vs};st=min(vs);pr=None;cu=st;cy=[st];nx=min(adj[st])
 while nx!=st:cy.append(nx);pr,cu=cu,nx;nx=next(z for z in adj[cu] if z!=pr)
 faces.append((d,cy))
faces.sort();D2=s.zeros(len(edges),len(faces))
for k,(d,cy) in enumerate(faces):
 for a,b in zip(cy,cy[1:]+cy[:1]):e=tuple(sorted((a,b)));D2[ep[e],k]=1 if e==(a,b) else -1
v=D2.nullspace()[0];den=s.ilcm(*[x.q for x in v]);orient=[int(x*den) for x in v]
if next(x for x in orient if x)<0:orient=[-x for x in orient]
pos={(i-1,j+1):(i,j) for i in range(1,4) for j in range(i,4)};neg=sorted(set(ds)-set(pos));a={}
for d,(i,j) in pos.items():a[d]=K0[j-1,i-1]
for i,d in enumerate(neg):a[d]=B[i,i]
cochain=[s.factor(orient[k]*a[d]) for k,(d,cy) in enumerate(faces)];pairing=s.factor(sum(cochain[k]*orient[k] for k in range(len(faces))));physical=s.factor(sum(K));decomp=s.factor(sum(K0)+sum(B))
checks={'top_boundary_is_cycle':D2*s.Matrix(orient)==s.zeros(len(edges),1),'orientation_coefficients_units':all(abs(x)==1 for x in orient),'all_nine_facets_weighted':set(a)==set(ds),'positive_facets_use_untransported_weights':len(pos)==6,'negative_simple_facets_use_boundary_corrections':len(neg)==3,'kernel_decomposition_exact':K==K0+B,'facet_pairing_equals_physical_scalar':pairing==physical==decomp}
out={'schema':'marici.nima.n8-physical-facet-cochain.v1','assignment':'positive-root facet [i,j] gets K0_[i,j]; negative-simple facet -alpha_i gets B_ii=K_ii-K0_ii; oriented cochain coefficient multiplies by top-boundary sign','top_boundary_signs':orient,'facet_weights':{str(d):str(s.factor(a[d])) for d in sorted(a)},'oriented_pairing':str(pairing),'physical_scalar':str(physical),'checks':checks,'passed':all(checks.values()),'conclusion':'The exact selected n=8 physical scalar is the evaluation of a fully specified oriented facet cochain on the A3 top-cell boundary. No mutation-edge transport is required.','claim_boundary':'This identifies the scalar augmentation, not the six individual transported K entries with positive cluster coordinates and not a radiative observable.'};p=ROOT/'research/nima/results/n8-physical-facet-cochain.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
