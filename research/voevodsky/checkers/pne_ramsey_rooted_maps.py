"""Fix both roots, and A,B. Count actual intertwiners, not abstract presentations. Use stored native eight-chart table indexed by (t,i,j) for C=stay-then-cross. The alternative cross-then-stay is C conjugated by stay since stay is involutive on chart readings. Test every named wiring as reference."""
from pathlib import Path
import json,itertools
D=Path(__file__).resolve().parents[1];raw=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());W=raw['wirings'];S=raw['address_masks'];E=list(map(tuple,raw['edge_order']))
def move(p):
 m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];e=[E.index(tuple(sorted((m[i],m[j])))) for i,j in E];return {w:sum((w>>i&1)<<j for i,j in enumerate(e)) for w in W}
A,B,C=[move(p) for p in ([1,0,3,2,4,5,6],[1,0,2,3,5,4,6],[0,1,4,5,2,3,6])];charts=json.loads((D/'results/pne_eight_chart_action.json').read_text());rows=[]
# Index 4*t+2*i+j. At t=1 the action of A and B on the address axes is exchanged.
a=lambda z:z^(2 if z<4 else 1);b=lambda z:z^(1 if z<4 else 2);c=lambda z:z^4;alt=lambda z:a(c(a(z)))
flag_audit=[];substeps=[];red_test=[];joint_test=[];red={q['wiring']:q['matches_P_step'] for q in json.loads((D/'results/ramsey_red_p_face_pair.json').read_text())}
def swap(i,j):
 p=list(range(7));p[i],p[j]=p[j],p[i];return move(p)
first_swaps={'01':swap(0,1),'45':swap(4,5)}
# Enumerate all source-label permutations. Reject maps that leave the fixed address or slot set, then compare exact actions on all eight wirings.
label_actions={}
for p in itertools.permutations(range(7)):
 try: action=move(p)
 except ValueError: continue
 if set(action.values())==set(W):label_actions.setdefault(tuple(action[w] for w in W),[]).append(p)
# Independent of chart matching: find square roots of the named transposition (01) acting on wirings, restricted only by the stored Ramsey chart. Count the ordered two-letter words in the registered A/B/C frame generators producing these actions.
ramsey_roots=[]
for img,reps in label_actions.items():
 t=dict(zip(W,img));
 if all(t[t[w]]==first_swaps['01'][w] for w in W):
  letters=dict(A=A,B=B,C=C);words=[i+j for i,I in letters.items() for j,J in letters.items() if all(J[I[w]]==t[w] for w in W)];ramsey_roots.append(dict(images=img,representatives=reps,words=words))
print('Ramsey only:',len(label_actions),'actions;',[(len(z['representatives']),z['words']) for z in ramsey_roots]);(D/'results/ramsey_chart_square_roots.json').write_text(json.dumps(ramsey_roots,indent=2)+'\n');cross_lifts={}
for w0 in W:
 # The image of w0 is 0; the image of C(w0) determines the rest by A,B.
 fits=[]
 for z1 in range(4,8):
  f={}
  for w,z in [(w0,0),(C[w0],z1)]:
   for i,j in itertools.product(range(2),repeat=2):
    u,v=w,z
    if i:u,v=A[u],a(v)
    if j:u,v=B[u],b(v)
    f[u]=v
  assert len(f)==len(set(f.values()))==8 and all(f[A[w]]==a(f[w]) and f[B[w]]==b(f[w]) for w in W)
  for name,g in [('RX',c),('XR',alt)]:
   if all(f[C[w]]==g(f[w]) for w in W):fits.append((name,f))
 assert len(fits)==2;(_,u),(_,v)=fits;agreement=[w for w in W if u[w]==v[w]];assert set(agreement)=={w0,A[w0],B[w0],A[B[w0]]}
 for name,f in fits:
  g=c if name=='RX' else alt
  for chart in charts:
   geom=list(map(json.loads,chart['example']));rootC,rootCell=geom[0];opposite=geom[b(0)][1] # B=RXX takes the opposite cell
   same_site=sum(red[w]==(geom[f[w]][0]==rootC) for w in W);same_pair=sum(red[w]==(geom[f[w]][1] in (rootCell,opposite)) for w in W);red_test.append(dict(root=w0,exchange=name,perm=chart['perm'],site_agreements=same_site,pair_agreements=same_pair))
   bins={}
   for w in W:
    cs,cell=geom[f[w]];bits=(cs==rootC,cell in (rootCell,opposite));bins.setdefault(bits,[]).append(dict(w=w,cell=cell,red=red[w]))
   assert len(bins)==4 and all(len(pair)==2 for pair in bins.values());joint_test.append(dict(root=w0,exchange=name,perm=chart['perm'],bins=[dict(bits=k,members=v) for k,v in bins.items()],mixed=sum(len({m['red'] for m in pair})==2 for pair in bins.values())))
  inv={v:k for k,v in f.items()};x=lambda z:c(a(z));action=tuple(inv[x(f[w])] for w in W);reps=label_actions[action];assert all(x(x(f[w]))==f[first_swaps['01'][w]] and x(f[w])!=f[w] for w in W);assert all(action[i]==(C[A[w]] if name=='RX' else A[C[w]]) for i,w in enumerate(W));assert cross_lifts.setdefault(name,reps)==reps
  # B=RXX; its two strict intermediate readings are R and RX, irrespective of the image selected for the Ramsey C. Here c is always physical RX.
  for w in W:
   z=f[w];assert f[B[w]]==b(z); mids=[a(z),c(z)];assert len({z,*mids,b(z)})==4
   substeps.append(dict(root=w0,exchange=name,w=w,matches={k:(1+mids.index(f[t[w]]) if f[t[w]] in mids else None) for k,t in first_swaps.items()}))
  edges={(w,T[w]) for T in (A,B) for w in W};lift=lambda u,v:(f[u],f[v]);observed=set();fixed_reverse=0
  for T,U,t in [(A,B,a),(B,A,b)]:
   for w in W:
    u=T[w];x,y=lift(w,u);assert y==t(x);observed.add((x,y));assert lift(u,w)==(t(x),t(y))==(y,x);assert U[C[w]]==C[u] and lift(C[w],C[u])==(g(x),g(y));fixed_reverse+=int((C[u],C[w])==(C[w],C[u]))
  assert len(edges)==len(observed)==16
  flag_audit.append(dict(root=w0,exchange=name,flags=len(observed),reversed_pairs=len(observed)//2))
 rows.append(dict(root=w0,agreed=len(agreement),Croot_images={name:f[C[w0]] for name,f in fits},example_geometry={name:charts[0]['example'][f[C[w0]]] for name,f in fits}))
(D/'results/pne_ramsey_single_cross.json').write_text(json.dumps(cross_lifts,indent=2)+'\n');print(cross_lifts);(D/'results/ramsey_red_step_joint_test.json').write_text(json.dumps(joint_test,indent=2)+'\n');(D/'results/ramsey_red_step_geometric_test.json').write_text(json.dumps(red_test,indent=2)+'\n');(D/'results/pne_ramsey_B_substep_matches.json').write_text(json.dumps(substeps,indent=2)+'\n');(D/'results/pne_ramsey_transition_lift.json').write_text(json.dumps(flag_audit,indent=2)+'\n');print(len(flag_audit),'rooted lifts of 16 flags');print(rows[0]);(D/'results/pne_ramsey_rooted_maps.json').write_text(json.dumps(rows,indent=2)+'\n')
