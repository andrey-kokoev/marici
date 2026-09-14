#!/usr/bin/env python3
"""Finite exhaustive audit of the cyclic C2 bar object and Möbius holonomy."""
import itertools,json
from pathlib import Path

def words(n):return list(itertools.product((0,1),repeat=n))
def face(x,i):
 n=len(x)
 if i==0:return x[1:]
 if i==n:return x[:-1]
 return x[:i-1]+(x[i-1]^x[i],)+x[i+1:]
def degen(x,i):return x[:i]+(0,)+x[i:]
def tau(x):
 if not x:return x
 return (sum(x)%2,)+x[:-1]
def power(f,x,k):
 for _ in range(k):x=f(x)
 return x
def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))
def main():
 checked=0
 for n in range(1,8):
  for x in words(n):
   assert power(tau,x,n+1)==x
   assert face(tau(x),0)==face(x,n)
   for i in range(1,n+1):assert face(tau(x),i)==tau(face(x,i-1))
   assert degen(tau(x),0)==power(tau,degen(x,n),2)
   for i in range(1,n+1):assert degen(tau(x),i)==tau(degen(x,i-1))
   checked+=1
 J=((0,-1),(-1,0));vp=(1,1);vm=(1,-1)
 assert mv(J,vp)==(-1,-1) and mv(J,vm)==vm
 assert mv(J,mv(J,vp))==vp
 det=J[0][0]*J[1][1]-J[0][1]*J[1][0];assert det==-1
 result={'schema':'marici.voevodsky.cyclic-C2-mobius-channel-bundle.v1','cyclic_simplices':'B_n(C2)=C2^n, identity-loop component of cyclic bar construction','degrees_checked':'1..7','simplices_checked':checked,'cyclic_order_law':True,'cyclic_face_laws':True,'cyclic_degeneracy_laws':True,'channel_holonomy':[list(r) for r in J],'holonomy_determinant':det,'fixed_eigenline':'span(nu_left-nu_right)','mobius_eigenline':'span(nu_left+nu_right)','normal_bundle_split':'trivial real line plus Mobius real line','globally_labelled_planes':False,'conclusion':'The cyclic realization supplies the arity circle; signed channel exchange supplies a nonorientable mapping-torus normal bundle.','claim_boundary':'The cyclic enhancement is extra structure relative to a bare simplicial 2-Segal object, although it is canonical for this C2 identity-loop bar model.'}
 out=Path(__file__).parents[1]/'results'/'cyclic_C2_mobius_channel_bundle.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
