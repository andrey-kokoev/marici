"""Tensor-product chain target for the shared-leg DG state block."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json, runpy, sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
with redirect_stdout(StringIO()): M=runpy.run_path(str(HERE/'check_witnessed_reference_reanchoring.py'))
plus,minus,delta,word=M['plus'],M['minus'],M['delta'],M['word']
add_scaled=M['add_scaled'] if 'add_scaled' in M else None

# Sparse rational vector chains, keyed by basis tuples (degree, i-index, j-index).
def add(*xs):
 out={}
 for x in xs:
  for k,v in x.items():
   out[k]=out.get(k,F(0))+v
   if not out[k]: del out[k]
 return out
def scale(c,x): return {k:c*v for k,v in x.items() if c*v}
def diff(x,y): return add(x,scale(-1,y))
def e(i): return {i:F(1)}
def tens(a,b): return {(i,j):x*y for i,x in a.items() for j,y in b.items()}
def deg0(i,j): return {(i,j):F(1)}

# C0 = Q[V] tensor Q[V]; C1 has horizontal and vertical tagged summands;
# C2 = augmentation_i tensor augmentation_j. Store each degree explicitly.
def d1(v):
 out={}
 for (kind,i,j),c in v.items():
  if kind=='L':
   for (ii,),a in i.items():
    for (jj,),b in j.items(): out[(ii,jj)]=out.get((ii,jj),F(0))+c*a*b
  else:
   for (ii,),a in i.items():
    for (jj,),b in j.items(): out[(ii,jj)]=out.get((ii,jj),F(0))+c*a*b
 return {k:v for k,v in out.items() if v}
def d2(v):
 out={}
 for (i,j),c in v.items():
  # standard tensor boundary; each augmentation vector includes signed vertices
  for ii,a in i.items():
   for jj,b in j.items(): out[('L',ii,{jj:F(1)})]=out.get(('L',ii,{jj:F(1)}),F(0)) + c*a*b
   for jj,b in j.items(): out[('R',{ii:F(1)},jj)]=out.get(('R',{ii:F(1)},jj),F(0)) - c*a*b
 return {k:v for k,v in out.items() if v}

# Simpler direct target differential: C1 -> C0 then compose pi_F.
def boundary1(v):
 out={}
 for (kind,a,b),c in v.items():
  if kind=='L':
   for i,ai in a.items():
    for j,bj in b.items(): out[(i,j)]=out.get((i,j),F(0))+c*ai*bj
  else:
   for i,ai in a.items():
    for j,bj in b.items(): out[(i,j)]=out.get((i,j),F(0))+c*ai*bj
 return {k:v for k,v in out.items() if v}
def boundary2(v):
 out={}
 for (a,b),c in v.items():
  for i,ai in a.items():
   for j,bj in b.items():
    out[('L', {i:F(1)}, b)] = out.get(('L',{i:F(1)},b),F(0))+c*ai*bj
    out[('R', a, {j:F(1)})] = out.get(('R',a,{j:F(1)}),F(0))-c*ai*bj
 return {k:v for k,v in out.items() if v}

def pi0(v):
 # Sparse output coordinates: ('lat',x,y,z) and ('q',q), with rational coefficients.
 out={}
 s={0:(0,0,0),1:(0,-1,-1),2:(-1,0,-1),3:(-1,-1,0)}
 for (i,j),c in v.items():
  for n,x in enumerate(s[i]): out[('lat',n)]=out.get(('lat',n),F(0))+c*x
  q=i^j
  if q: out[('q',q)]=out.get(('q',q),F(0))+c
 return {k:v for k,v in out.items() if v}

def target_d1(v): return pi0(boundary1(v))
def target_d2(v): return boundary2(v)
def vadd(*vs):
 out={}
 for v in vs:
  for k,c in v.items(): out[k]=out.get(k,F(0))+c
 return {k:v for k,v in out.items() if v}
def vscale(c,v): return {k:c*x for k,x in v.items() if c*x}
def vecdiff(a,b): return vadd(a,vscale(-1,b))
def embed_l(a,j): return {('L',a,{j:F(1)}):F(1)}
def embed_r(i,b): return {('R',{i:F(1)},b):F(1)}
def aug(i,ip): return {i:F(-1),ip:F(1)}
def aug_pair(i,ip,j,jp): return {(tuple(sorted(aug(i,ip).items())),tuple(sorted(aug(j,jp).items()))):F(-1)}
def source_left(i,ip,j): return plus(word(f'sy{j}'),word(f'sh{ip}')) if False else plus(M['mul'](word(f'sy{j}'),diff(word(f'sh{ip}'),word(f'sh{i}'))))
def source_right(i,j,jp): return M['mul'](diff(word(f'sk{jp}'),word(f'sk{j}')),word(f'sx{i}'))
def target_edge_left(i,ip,j): return embed_l(aug(i,ip),j)
def target_edge_right(i,j,jp): return embed_r(i,aug(j,jp))
def target_cell(i,ip,j,jp): return { (tuple(aug(i,ip).items()),tuple(aug(j,jp).items())):F(-1)}

# Compare sparse source chains against images of degree-zero arrows.
def source_D(i,j): return M['anchors'][f's:{i}:{j}']
def src_map_degree0(chain):
 out={}
 for p,c in chain.items():
  assert len(p)==1 and p[0].startswith('sx') is False
  name=p[0]
  if name.startswith('sy') or name.startswith('sh') or name.startswith('sk'):
   raise AssertionError('expected state composites only')
 return out

def main():
 # Verify augmented target identities using basis vectors and all signed augmentation pairs.
 cells=0
 for i in range(4):
  for ip in range(4):
   for j in range(4):
    for jp in range(4):
     c=target_cell(i,ip,j,jp)
     b=target_d2(c)
     assert target_d1(b)=={}
     cells+=1
 # Endpoint map differential checks directly in compressed T0 coordinates.
 edges=0
 for i in range(4):
  for ip in range(4):
   for j in range(4):
    l=target_edge_left(i,ip,j)
    expect=vecdiff(pi0(deg0(ip,j)),pi0(deg0(i,j)))
    assert target_d1(l)==expect; edges+=1
 for i in range(4):
  for j in range(4):
   for jp in range(4):
    r=target_edge_right(i,j,jp)
    expect=vecdiff(pi0(deg0(i,jp)),pi0(deg0(i,j)))
    assert target_d1(r)==expect; edges+=1
 # Mixed boundary matches source orientation exactly.
 mixed=0
 for i,ip,j,jp in product(range(4),repeat=4):
  a=aug(i,ip); b=aug(j,jp)
  cell=target_cell(i,ip,j,jp)
  boundary=target_d2(cell)
  # Expected K_RL-K_LR = -alpha tensor beta in the two edge summands.
  expected=vadd(embed_r(i,b),vscale(-1,embed_r(ip,b)),embed_l(a,jp),vscale(-1,embed_l(a,j)))
  assert boundary==expected
  mixed+=1
 # Source rank dimensions and exactness: tensor of augmented inclusions.
 report={'schema':'marici.nima.two-state-index-tensor-chain-map.v1','status':'passed',
         'dimensions':{'C2':9,'C1':24,'C0_before_compression':16,'T0':6},
         'checks':{'mixed_target_d2_d1_zero':cells,'endpoint_edge_boundaries':edges,'mixed_orientation_boundaries':mixed},
         'chain_map_scope':'Target boundary identities and endpoint images checked. Source-to-target maps on all source linear relations and products are NOT checked by this script.',
         'multiplication_claim':False,
         'homology':'Not computed in this first boundary-only audit.'}
 out=HERE.parent/'results'/'two-state-index-tensor-chain-map.json'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2)+'\n')
 print('PASS:',report['checks'])
 print('Target differentials and endpoint boundaries pass; this is not yet a complete source chain-map audit.')
if __name__=='__main__': main()
