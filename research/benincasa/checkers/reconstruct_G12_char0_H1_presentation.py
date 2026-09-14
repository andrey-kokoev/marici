#!/usr/bin/env python3
"""VC2b0: materialize the exact characteristic-zero stage-1 cokernel presentation."""
import gzip,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());mod=json.loads((ROOT/'research/benincasa/results/G12_four_component_Hermite_image.json').read_text())
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};K=s.sympify(data['K0'],locals=L);VK=s.diff(K,a)-s.diff(K,b)
qs=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];vq=[-1,1,-1,1];P=s.expand(s.prod(qs));cof=[s.expand(s.prod(qs[j] for j in range(4) if j!=i)) for i in range(4)]
def V(f):return s.diff(f,a)-s.diff(f,b)
other=[s.expand(sum(vq[j]*cof[j] for j in range(4) if j!=i)) for i in range(4)]
A=s.expand(K*P);C=[s.expand(K*qs[i]*V(cof[i])-s.Rational(3,2)*cof[i]*VK*qs[i]-2*cof[i]*K*vq[i]-3*K*qs[i]*other[i]) for i in range(4)]
cols=[(comp,(i,j,d-i-j)) for comp in range(4) for d in range(11) for i in range(d+1) for j in range(d-i+1)];rows=[(i,j,d-i-j) for d in range(19) for i in range(d+1) for j in range(d-i+1)];ridx={e:i for i,e in enumerate(rows)}
def terms(poly):return s.Poly(poly,a,b,c,domain=s.QQ).terms()
At=terms(A);Ct=[terms(x) for x in C];entries=[]
for col,(comp,e) in enumerate(cols):
 acc={};i,j,k=e
 for base,x in Ct[comp]:
  z=tuple(base[t]+e[t] for t in range(3));acc[z]=acc.get(z,0)+x
 for de,fac in (((i-1,j,k),i),((i,j-1,k),-j)):
  if fac:
   for base,x in At:
    z=tuple(base[t]+de[t] for t in range(3));acc[z]=acc.get(z,0)+fac*x
 for z,x in acc.items():
  if x:entries.append((ridx[z],col,int(x.p),int(x.q)))
lines=['%%MatrixMarket matrix coordinate rational general',f'{len(rows)} {len(cols)} {len(entries)}']+[f'{r+1} {c0+1} {p}/{q}' for r,c0,p,q in entries]
blob=('\n'.join(lines)+'\n').encode();dest=ROOT/'research/benincasa/results/G12_stage1_char0_matrix.mtx.gz'
with dest.open('wb') as raw:
 with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as z:z.write(blob)
checks={'matrix_shape_1330_1144':(len(rows),len(cols))==(1330,1144),'nonempty_exact_entries':len(entries)>0,'all_denominators_one_or_two':{q for _,_,_,q in entries}<={1,2},'modular_rank_stable_761':all(x['rank']==761 for x in mod['modular_tests']),'target_survives_modularly':all(not x['target_in_image'] for x in mod['modular_tests']),'gzip_roundtrip':gzip.decompress(dest.read_bytes())==blob}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-char0-H1-presentation.v1','prospective_action':'VC2b0_reconstruct_char0_H1','base_field':'Q','presentation':'H1_Q = coker(d0: Q^1144 -> Q^1330)','matrix_artifact':str(dest.relative_to(ROOT)).replace('\\','/'),'matrix_market_uncompressed_sha256':hashlib.sha256(blob).hexdigest(),'compressed_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'shape':[len(rows),len(cols)],'nonzero_entries':len(entries),'coefficient_denominators':sorted({q for _,_,_,q in entries}),'rank_evidence':mod['modular_tests'],'VC2b0_resolution':'++','interface_added':'char0_H1_presentation','qualification':'The exact Q-linear presentation is reconstructed. Rank 761 is certified in the tested modular fibers; an exact characteristic-zero Smith/rank decomposition is not claimed or required to type the cokernel.','next':'VC2b2_compare_overlap_to_H1','checks':checks,'passed':True};(ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','shape':out['shape'],'nnz':len(entries),'artifact':out['matrix_artifact'],'next':out['next']}))
