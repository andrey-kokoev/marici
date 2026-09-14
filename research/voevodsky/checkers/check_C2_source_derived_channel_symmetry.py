#!/usr/bin/env python3
"""Derive channel parity, reversal, and the averaged metric from C2 data."""
import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(A):return tuple(zip(*A))
def add(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def ident():return ((1,0),(0,1))
def key(A):return tuple(x for r in A for x in r)
def group_generated(gens):
 seen={key(ident()):ident()};front=[ident()]
 while front:
  a=front.pop()
  for g in gens:
   b=mm(a,g)
   if key(b) not in seen:seen[key(b)]=b;front.append(b)
 return list(seen.values())
def avg_metric(group,G):
 out=((Fraction(0),Fraction(0)),(Fraction(0),Fraction(0)))
 for g in group:out=add(out,mm(mm(tr(g),G),g))
 q=Fraction(1,len(group));return tuple(tuple(q*x for x in r) for r in out)
def main():
 # Unique nontrivial character of C2: chi(g)=(-1)^g.
 character={0:1,1:-1};assert character[0]==1 and all(character[a^b]==character[a]*character[b] for a in (0,1) for b in (0,1))
 S=((1,0),(0,-1));J=((0,-1),(-1,0));Gamma=group_generated([S,J]);assert len(Gamma)==8
 seeds=[((2,1),(1,3)),((5,-2),(-2,4)),((1,0),(0,1))]
 averages=[]
 for G in seeds:
  A=avg_metric(Gamma,G);assert A[0][1]==A[1][0]==0 and A[0][0]==A[1][1]
  assert all(mm(mm(tr(g),A),g)==A for g in Gamma);averages.append([[str(x) for x in r] for r in A])
 result={'schema':'marici.voevodsky.C2-source-derived-channel-symmetry.v1','source_group':'C2','nontrivial_character':character,'parity_action':[list(r) for r in S],'reversal_action':[list(r) for r in J],'generated_symmetry_group_order':len(Gamma),'generated_group':'D4 matrix representation','seed_metrics_checked':len(seeds),'averaged_metrics':averages,'averaging_always_scalar_on_checked_symbolic_basis':True,'conclusion':'C2 character supplies parity; simplicial order reversal plus channel exchange supplies J; averaging over their D4 action supplies the right-angle metric up to scale.','claim_boundary':'Internal construction for the chosen C2 model; not a derivation that every coherence pyramid must carry C2 channel data.'}
 out=Path(__file__).parents[1]/'results'/'C2_source_derived_channel_symmetry.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
