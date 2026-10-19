"""Exact reference-space symplectic connector and three distinct penalty laws.
Standard-library rational arithmetic only. No physical-time interpretation.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
OUT=BASE/'results/symplectic-neutral-connector'

def ident(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def zero(n,m=None):return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in zip(*b)] for row in a]
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(s,a):return [[s*x for x in row] for row in a]
def block(a,b,c,d):return [ar+br for ar,br in zip(a,b)]+[cr+dr for cr,dr in zip(c,d)]
def rank(a):
 a=[row[:] for row in a];k=0
 for j in range(len(a[0])):
  p=next((i for i in range(k,len(a)) if a[i][j]),None)
  if p is None:continue
  a[k],a[p]=a[p],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
  for i in range(k+1,len(a)):
   if a[i][j]:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k

def pmatrix(p):return [[Q(j==p[i]) for j in range(len(p))] for i in range(len(p))]
def realify(a):return block(a,zero(len(a)),zero(len(a)),a)
def energy(k,z):return mul(transpose(z),mul(k,z))[0][0]/2
def norm2(z):return sum(x[0]**2 for x in z)
def nonzero(a):return sum(bool(x) for row in a for x in row)

hashes={}
def load(path):
 b=(ROOT/path).read_bytes();hashes[path]=hashlib.sha256(b).hexdigest();return json.loads(b)
def fresh(d):
 for path,digest in d.get('sourceHashes',{}).items():
  assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,('stale input',path)

def main():
 protocol=load('research/strominger/inputs/symplectic-neutral-connector-protocol-v1.json')
 receipt=load('research/strominger/results/cavity-reference-closure/verification.json');assert receipt['status']=='pass';fresh(receipt)
 maps={}
 for case in receipt['results']:
  for op in case['nativeFactors']:maps.setdefault(tuple(op['permutation']),[]).append({'case':case['label'],'kind':op['kind'],'native':True})
  if case['conditionalClosure']:
   op=case['conditionalClosure']['comparison'];maps.setdefault(tuple(op['permutation']),[]).append({'case':case['label'],'kind':'conditional-comparison','native':False})
 path='research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'
 b=(ROOT/path).read_bytes();hashes[path]=hashlib.sha256(b).hexdigest()
 match=re.search(r'neutron:Object\.freeze\(\[([0-4,]+)\]\)',b.decode());assert match
 advance=tuple(map(int,match.group(1).split(',')));maps.setdefault(advance,[]).append({'kind':'source-neutron-advance','native':True})
 n=10;I=ident(n);Z=zero(n);J=block(zero(5),ident(5),scale(-1,ident(5)),zero(5))
 boundary=block(J,Z,Z,scale(-1,J));dynamic=block(J,Z,Z,J);II=ident(2*n)
 swap=block(Z,I,I,Z);assert mul(transpose(swap),mul(boundary,swap))==scale(-1,boundary)
 records=[]
 for p,provenance in maps.items():
  assert sorted(p)==list(range(5))
  S=realify(pmatrix(p));inverse=transpose(S)
  assert mul(transpose(S),mul(J,S))==J
  symplectic_adjoint=mul(scale(-1,J),mul(transpose(S),J));assert symplectic_adjoint==inverse
  assert mul(inverse,S)==I and mul(S,inverse)==I
  graph=I+S # vertical stack, dimension20 by10
  graph_inverse=I+inverse
  assert rank(graph)==n and mul(transpose(graph),mul(boundary,graph))==zero(n)
  assert mul(swap,graph)==mul(graph_inverse,S)
  B=[[-x for x in sr]+ir for sr,ir in zip(S,I)]
  K=mul(transpose(B),B)
  assert rank(K)==n and mul(K,graph)==zero(2*n,n)
  assert mul(B,transpose(B))==scale(2,I) and mul(K,K)==scale(2,K)
  # Opposite-sign boundary form: a Hamiltonian penalty produces a shear.
  A_boundary=mul(scale(-1,boundary),K)
  assert add(mul(transpose(A_boundary),boundary),mul(boundary,A_boundary))==zero(2*n)
  assert rank(A_boundary)==n and mul(A_boundary,A_boundary)==zero(2*n)
  assert mul(B,A_boundary)==zero(n,2*n)
  z=[[Q(0)] for _ in range(2*n)];z[n][0]=1
  velocity=mul(A_boundary,z);assert nonzero(velocity)>0
  drift=[]
  for s in (1,2,4):
   flow=add(II,scale(s,A_boundary));zs=mul(flow,z)
   assert mul(transpose(flow),mul(boundary,flow))==boundary
   assert mul(B,zs)==mul(B,z) and energy(K,zs)==energy(K,z)
   drift.append({'auxiliaryParameter':s,'squaredNorm':str(norm2(zs)),'penalty':str(energy(K,zs))})
  assert drift[-1]['squaredNorm']!=drift[0]['squaredNorm']
  # Same-sign dynamical form: relative modes oscillate, they do not relax.
  A_dynamic=mul(scale(-1,dynamic),K)
  assert add(mul(transpose(A_dynamic),dynamic),mul(dynamic,A_dynamic))==zero(2*n)
  assert mul(B,A_dynamic)==scale(-2,mul(J,B))
  assert mul(A_dynamic,mul(A_dynamic,A_dynamic))==scale(-4,A_dynamic)
  common=add(II,scale(Q(-1,2),K))
  quarter=add(common,scale(Q(1,2),A_dynamic))
  quarter_inverse=add(common,scale(Q(-1,2),A_dynamic))
  assert mul(quarter_inverse,quarter)==II
  assert mul(quarter,mul(quarter,mul(quarter,quarter)))==II
  assert mul(transpose(quarter),mul(dynamic,quarter))==dynamic
  assert mul(transpose(quarter),mul(K,quarter))==K
  assert norm2(mul(B,mul(quarter,z)))==norm2(mul(B,z))
  # Auxiliary gradient step: mismatch contracts but phase-space volume does too.
  gradient=add(II,scale(Q(-1,4),K))
  assert mul(B,gradient)==scale(Q(1,2),B)
  assert energy(K,mul(gradient,z))==energy(K,z)/4
  assert mul(transpose(gradient),mul(dynamic,gradient))!=dynamic
  assert mul(transpose(gradient),mul(boundary,gradient))!=boundary
  records.append({'permutation':list(p),'provenance':provenance,
   'realDimension':n,'symplectic':True,'symplecticAdjointEqualsInverse':True,
   'graphLagrangianDimension':rank(graph),'endpointSwapIsAntisymplectic':True,
   'penaltyRank':rank(K),'zeroModes':n,'nonzeroHessianEigenvalue':2,
   'oppositeSignHamiltonian':{'generatorRank':rank(A_boundary),'nilpotencyOrder':2,'mismatchConstant':True,'samples':drift},
   'sameSignHamiltonian':{'relativeGenerator':'-2J','oscillationNotAttraction':True,'exactQuarterMapOrder':4,'zeroCommonModes':n},
   'auxiliaryGradient':{'step':'1/4','mismatchMultiplier':'1/2','penaltyMultiplier':'1/4','determinant':str(Q(1,2)**n),'symplectic':False},
   'admissionUnchanged':True})
 # Correct reversal must reverse composition order, not just invert factors.
 T=tuple(receipt['results'][1]['conditionalClosure']['comparison']['permutation'])
 A=realify(pmatrix(advance));C=realify(pmatrix(T));forward=mul(A,C)
 backward=mul(transpose(C),transpose(A));wrong_order=mul(transpose(A),transpose(C))
 assert mul(backward,forward)==I and wrong_order!=backward
 # All saved complete PE factor products are checked as symplectic maps too.
 product_checks=0
 for case in receipt['results']:
  ops={op['id']:op for op in case['nativeFactors']}
  for shortcut in case['activeReferenceShortcuts']:
   pn,ne=(ops[i] for i in shortcut['factors'])
   product=mul(realify(pmatrix(ne['permutation'])),realify(pmatrix(pn['permutation'])))
   assert product==realify(pmatrix(shortcut['permutation']))
   assert mul(transpose(product),mul(J,product))==J;product_checks+=1
 # Positive symplectic balance alone cannot guarantee stable repeated transfer.
 squeeze=block(scale(2,ident(5)),zero(5),zero(5),scale(Q(1,2),ident(5)))
 assert mul(transpose(squeeze),mul(J,squeeze))==J and transpose(squeeze)!=mul(scale(-1,J),mul(transpose(squeeze),J))
 v=[[Q(int(i==0))] for i in range(n)];assert norm2(mul(squeeze,v))==4*norm2(v)
 broken=ident(n);broken[0][0]=2
 assert mul(transpose(broken),mul(J,broken))!=J
 bad_graph=I+broken;assert nonzero(mul(transpose(bad_graph),mul(boundary,bad_graph)))>0
 OUT.mkdir(parents=True,exist_ok=True)
 for path in (Path(__file__),BASE/'checkers/check_cavity_reference_closure.mjs'):
  hashes[str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
 result={'schema':'marici.symplectic-neutral-connector.v1','status':'pass','protocol':protocol,'sourceHashes':hashes,
  'maps':records,'PEProductsChecked':product_checks,'reverseOrderControlRejected':True,
  'nonSymplecticCoordinateCorruptionRejected':True,
  'symplecticSqueeze':{'preservesJ':True,'oneTransferSquaredNormMultiplier':4,'repeatedTransferMultiplier':'4^k; k is a composition count, not physical time'},
  'disposition':'Saved permutations supply neutral canonical relations under the declared reference form. Stabilization is not selected: opposite-sign boundary Hamiltonian shears, same-sign product Hamiltonian oscillates, and auxiliary gradient damping is nonsymplectic. No neutron-specific energy, physical time, charge or occupancy law is derived.'}
 (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':'pass','distinctSourceMaps':len(records),'PEProductsChecked':product_checks,
                   'classification':'neutral-reference-relation-with-dynamical-form-and-restoring-law-residuals'}))

if __name__=='__main__':main()
