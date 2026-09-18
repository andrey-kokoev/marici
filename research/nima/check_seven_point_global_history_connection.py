#!/usr/bin/env python3
"""Global flat history-frame connection plus local boundary defects on n=7 cells."""
import cmath,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
inc=json.loads((ROOT/'research/nima/results/seven-point-cellulation-incidence.json').read_text())
def add(A,B):return tuple(a+b for a,b in zip(A,B))
def sub(A,B):return tuple(a-b for a,b in zip(A,B))
def mm(A,B):return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
def det(A):return A[0]*A[3]-A[1]*A[2]
def adj(A):return (A[3],-A[1],-A[2],A[0])
def inv(A):return tuple(v/det(A) for v in adj(A))
def outer(a,b):return (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
def norm(A):
 r=cmath.sqrt(det(A));return tuple(v/r for v in A)
def errI(A):return max(abs(A[i]-(1 if i in (0,3) else 0)) for i in range(4))
def z(v):return {'real':v.real,'imag':v.imag}
n=7;lam={i:(1+0j,cmath.exp(2j*cmath.pi*i/n)) for i in range(1,n+1)};til={i:(complex(.4+.09*i,.13*i),complex(.2*i-.3,.17-.05*i)) for i in range(1,n-1)};M=(0j,0j,0j,0j)
for i in range(1,n-1):M=add(M,outer(lam[i],til[i]))
L=(lam[n-1][0],lam[n][0],lam[n-1][1],lam[n][1]);Y=mm(inv(L),tuple(-v for v in M));til[n-1]=(Y[0],Y[1]);til[n]=(Y[2],Y[3]);x={1:(0j,0j,0j,0j)}
for i in range(1,n+1):x[i+1]=sub(x[i],outer(lam[i],til[i]))
def X(a,b):return sub(x[a],x[b])
def path(vertices):
 A=(1+0j,0j,0j,1+0j)
 for k,(a,b) in enumerate(zip(vertices,vertices[1:])):A=mm(A,X(a,b) if k%2==0 else adj(X(a,b)))
 return A
hs=compile_nnmhv_histories(n);I=(1+0j,0j,0j,1+0j);frames=[]
for h in hs:frames.append(norm(path((n,)+h.inner_prefix)) if h.inner_prefix else I)
def edge(a,b):return norm(mm(frames[b],inv(frames[a])))
cycles=((0,1,2,4),(0,4,5),(2,3,4));cycle_data=[]
for cyc in cycles:
 H=I
 for a,b in zip(cyc,cyc[1:]+cyc[:1]):H=mm(edge(a,b),H)
 cycle_data.append({'cells':list(cyc),'flatness_error':errI(H),'holonomy':[z(v) for v in H]})
defects=[]
for k,h in enumerate(hs):
 for u in h.boundary_updates:
  transported=path((n,)+u.replacement_path);reference=frames[k] if u.side=='upper' else I;D=norm(mm(reference,inv(transported)));tr=D[0]+D[3];disc=cmath.sqrt(tr*tr-4);rap=cmath.log((tr+disc)/2);defects.append({'cell':k,'side':u.side,'rapidity':z(rap),'nontriviality':errI(D)})
checks={'momentum_closure':max(abs(v) for v in x[n+1])<1e-8,'three_adjacency_cycles':len(cycle_data)==3,'intercell_connection_flat':all(c['flatness_error']<1e-8 for c in cycle_data),'boundary_defects_present':len(defects)==5 and all(d['nontriviality']>1e-6 for d in defects),'boundary_defects_have_phase':any(abs(d['rapidity']['imag'])>1e-6 for d in defects)}
out={'schema':'marici.nima.seven-point-global-history-connection.v1','cell_frames':[[z(v) for v in F] for F in frames],'cycle_holonomies':cycle_data,'boundary_update_defects':defects,'checks':checks,'passed':all(checks.values()),'meaning':'History-prefix frames define a flat pure-gauge connection on the cell adjacency graph; source boundary updates are localized affine defects carrying boost and phase.'};p=ROOT/'research/nima/results/seven-point-global-history-connection.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
