#!/usr/bin/env python3
"""Exact path-space criterion audit for the C2 nerve."""
import itertools, json
from pathlib import Path

G=(0,1)
def X(n): return list(itertools.product(G, repeat=n))
def dx(x,i):
 n=len(x)
 if i==0:return x[1:]
 if i==n:return x[:-1]
 return x[:i-1]+(x[i-1]^x[i],)+x[i+1:]

def Y(n):return X(n+1)  # initial path space, omit d0
def Z(n):return X(n+1)  # final path space, omit last face
def dy(x,i):return dx(x,i+1)
def dz(x,i):return dx(x,i)

def restrict_edge(simplex, i, face):
 # Keep vertices i and i+1 of an n-simplex by deleting other vertices high-to-low.
 n=len(simplex)-1
 out=simplex
 for vertex in reversed([v for v in range(n+1) if v not in (i,i+1)]):out=face(out,vertex)
 return out

def segal_audit(space,face,max_n):
 rows=[]
 edges=space(1)
 for n in range(2,max_n+1):
  signatures={tuple(restrict_edge(x,i,face) for i in range(n)) for x in space(n)}
  compatible=[]
  for chain in itertools.product(edges,repeat=n):
   if all(face(chain[i],0)==face(chain[i+1],1) for i in range(n-1)):compatible.append(chain)
  assert signatures==set(compatible) and len(signatures)==len(space(n))
  rows.append({'dimension':n,'simplices':len(space(n)),'compatible_spines':len(compatible),'segal_map_bijective':True})
 return rows

def main():
 initial=segal_audit(Y,dy,6);final=segal_audit(Z,dz,6)
 periodic=[{'degree':n,'X_type':n%4,'initial_path_type':(n+1)%4,'final_path_type':(n+1)%4} for n in range(8)]
 result={'schema':'marici.voevodsky.two-directional-path-spaces.v1','simplicial_object':'nerve of one-object category C2','initial_path_space_1_segal':True,'final_path_space_1_segal':True,'two_segal_by_path_space_criterion':True,'initial_rows':initial,'final_rows':final,'periodic_type_shift':periodic,'opposite_orientation_established':False,'orthogonality_established':False,'claim_boundary':'Exact finite audit through degree six plus the general nerve-of-category theorem; does not derive 90-degree geometry or opposite signs.'}
 out=Path(__file__).parents[1]/'results'/'two_directional_path_spaces.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
