"""Certified vertex lifts define a non-affine continuous common section."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
R=[Q(1,128**j) for j in range(4)];C=[Q(50),Q(51),Q(52),Q(53)];delta=Q(1,128**4)
def source(p,q,h,k):
 U=sum(C)+delta*p;V=sum(a*b for a,b in zip(C,R))+delta*q
 t0=C[0]+delta*h;t1=C[1]+delta*k
 u=U-t0-t1;v=V-t0-R[1]*t1;t2=(v-R[3]*u)/(R[2]-R[3])
 return (t0,t1,t2,u-t2)
def rows():
 # a dot (p,q,h,k)<=b; common fiber is max(p,q)<=h<=min(1,p+q), 0<=k<=1.
 return [((-1,0,0,0),0),((1,0,0,0),1),((0,-1,0,0),0),((0,1,0,0),1),
 ((0,0,-1,0),0),((0,0,1,0),1),((0,0,0,-1),0),((0,0,0,1),1),
 ((1,0,-1,0),0),((0,1,-1,0),0),((-1,-1,1,0),0)]
def main():
 corners=[]
 for z in product((Q(0),Q(1)),repeat=4):
  x=source(*z);assert all(0<v<100+2*j for j,v in enumerate(x))
  corners.append({'local':list(map(str,z)),'source':list(map(str,x))})
 vertices=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
 lifts=[source(p,q,max(p,q),Q(0)) for p,q in vertices]
 for (p,q),x in zip(vertices,lifts):
  z=(p,q,max(p,q),Q(0));assert all(sum(Q(a)*v for a,v in zip(n,z))<=b for n,b in rows())
 # Diagonal triangulation; forced vertex heights rule out global affinity.
 h=[max(p,q) for p,q in vertices];assert h[0]+h[2]!=h[1]+h[3]
 report={'public_vertices':[list(map(str,v)) for v in vertices], 'triangles':[[0,1,2],[0,2,3]],
 'vertex_source_lifts':[list(map(str,x)) for x in lifts],
 'fine_rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows()],
 'admitted_local_cube':corners,'section':'h=max(p,q), k=0, followed by affine source inverse',
 'scope':'Common section for joint affine source/evidence on a square; full domain certified by simplex vertices and matching faces.'}
 (OUT/'polyhedral-common-section.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'triangles':2,'source_vertices':4,'cube_corners':16,'global_affine_section_impossible':True}))
if __name__=='__main__':main()
