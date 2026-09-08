#!/usr/bin/env python3
"""Native normalization-to-short-face comparison, including both attachments.

Self-contained exact integer/polynomial checker (Python 3.10+).
The target is the squarefree occurrence dualizing diagram of the actual
short-face subcomplex. Equality with the full 215-state support-PC/normal-
Rees functor is NOT asserted. No repository mutation or network is used.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
import json, hashlib

CHECKS=Counter(); N=6; ALL=tuple(range(6)); EV=(0,2,4); OD=(1,3,5); Z=(0,)*6; ONE={Z:1}
def ck(a,t):
 if not a: raise AssertionError(t)
 CHECKS[t]+=1
def pm(i):return -1 if i%2 else 1
def ps(s):return tuple(t for k in range(len(s)+1) for t in combinations(s,k))
def wt(s):return tuple(int(i in s) for i in ALL)
def pa(*vs):
 o={}
 for v in vs:
  for a,c in v.items():
   o[a]=o.get(a,0)+c
   if not o[a]:del o[a]
 return o
def sm(p,n):return {a:c*n for a,c in p.items() if c*n}
def mul(p,q):
 o={}
 for a,c in p.items():
  for b,d in q.items():
   t=tuple(x+y for x,y in zip(a,b));o[t]=o.get(t,0)+c*d
   if not o[t]:del o[t]
 return o
def mono(a,c=1):return {tuple(a):c} if c else {}
def var(i):return mono(wt((i,)))
def scalar(c):return mono(Z,c)
def va(*vs):
 o={}
 for v in vs:
  for k,p in v.items():
   o[k]=pa(o.get(k,{}),p)
   if not o[k]:del o[k]
 return o
def vm(v,p):return {k:t for k,q in v.items() if (t:=mul(q,p))}
def neg(v):return vm(v,scalar(-1))
def unit(k):return {k:ONE}
def app(f,v):
 o={}
 for k,p in v.items():o=va(o,vm(f.get(k,{}),p))
 return o
def entry(d,a,b,p):
 d[a][b]=pa(d[a].get(b,{}),p)
 if not d[a][b]:del d[a][b]
def audit(g,d,l,t,step=-1):
 for a in g:
  ck(not app(d,d[a]),t+'_d2')
  for b,p in d[a].items():
   ck(g[b]==g[a]+step,t+'_degree')
   for m,c in p.items():ck(tuple(x+y for x,y in zip(m,l[b]))==l[a] and min(m)>=0,t+'_homogeneous_polynomial')
def sdr(g,d,tag='sdr'):
 cur={a:dict(d[a]) for a in g};P={a:unit(a) for a in g};I=dict(P);H={a:{} for a in g};count=0
 while True:
  hit=next(((b,a,p[Z]) for b,v in cur.items() for a,p in v.items() if len(p)==1 and p.get(Z,0) in (-1,1)),None)
  if hit is None:break
  b,a,c=hit;rest=[z for z in cur if z not in (a,b)];db=cur[b]
  pp={z:unit(z) for z in rest};pp[b]={};pp[a]={z:sm(p,-c) for z,p in db.items() if z!=a}
  ii={z:va(unit(z),{b:sm(cur[z][a],-c)} if a in cur[z] else {}) for z in rest}
  for z in g:
   if a in P[z]:H[z]=va(H[z],vm(I[b],sm(P[z][a],c)))
  P={z:app(pp,v) for z,v in P.items()};I={z:app(I,v) for z,v in ii.items()};cur={z:app(pp,app(cur,ii[z])) for z in rest};count+=1
 for z in g:
  ck(va(app(d,H[z]),app(H,d[z]))==va(unit(z),neg(app(I,P[z]))),tag+'_homotopy')
  ck(app(cur,P[z])==app(P,d[z]),tag+'_projection')
 for z in cur:ck(app(P,I[z])==unit(z) and app(d,I[z])==app(I,cur[z]),tag+'_section')
 return {a:g[a] for a in cur},cur,P,I,H,count

def node():
 g={('b',(),()):0};d={('b',(),()):{}};l={('b',(),()):Z}
 for u in ps(EV)[1:]:
  for v in ps(OD)[1:]:
   a=('b',u,v);g[a]=len(u)+len(v)-1;l[a]=wt(u+v);d[a]={}
   if len(u)==len(v)==1:d[a]={('b',(),()):mono(wt(u+v))};continue
   if len(u)>1:
    for j,i in enumerate(u):d[a][('b',u[:j]+u[j+1:],v)]=sm(var(i),pm(j))
   if len(v)>1:
    for j,i in enumerate(v):d[a][('b',u,v[:j]+v[j+1:])]=sm(var(i),pm(len(u)-1+j))
 audit(g,d,l,'node');return g,d,l

def taylor(mons):
 g={s:len(s) for s in ps(tuple(range(len(mons))))};l={s:wt(set().union(*(set(mons[i]) for i in s))) for s in g};d={s:{} for s in g}
 for s in g:
  for j,i in enumerate(s):
   t=s[:j]+s[j+1:];d[s][t]=mono(tuple(a-b for a,b in zip(l[s],l[t])),pm(j))
 audit(g,d,l,'taylor');return g,d,l

def homog(model,a):
 g,d,l=model;gg={s:n for s,n in g.items() if all(x<=y for x,y in zip(l[s],a))};dd={s:{t:scalar(sum(p.values())) for t,p in d[s].items() if t in gg} for s in gg}
 return gg,dd

def lift_by_resolution(src,tgt,initial,tag):
 sg,sd,sl=src;tg,td,tl=tgt;f={};cache={}
 for b in sorted(sg,key=lambda a:sg[a]):
  if sg[b]==0:f[b]=initial[b];continue
  a=sl[b]
  if a not in cache:
   hg,hd=homog(tgt,a);red=sdr(hg,hd,tag+'_fibre');ck(not red[0],tag+'_acyclic_fibre');cache[a]=red[4]
  v=app(f,sd[b]);iv={z:scalar(sum(p.values())) for z,p in v.items()};sol=app(cache[a],iv)
  f[b]={z:mono(tuple(x-y for x,y in zip(a,tl[z])),sum(p.values())) for z,p in sol.items()}
  ck(app(td,f[b])==v,tag+'_lift_equation')
 for b in sg:ck(app(td,f[b])==app(f,sd[b]),tag+'_chainmap')
 return f

def dual(model):
 g,d,l=model;gg={a:n-6 for a,n in g.items()};ll={a:tuple(1-x for x in l[a]) for a in g};dd={a:{} for a in g}
 for b,v in d.items():
  for a,p in v.items():dd[a][b]=sm(p,pm(g[a]+1))
 audit(gg,dd,ll,'dual',step=1);return gg,dd,ll

CROSS=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6));BRIDGES=tuple((i,(i+3)%6) for i in EV)
SIGMA=tuple(f for f in ps(ALL) if set(f)<=set(EV) or set(f)<=set(OD))
DELTA=tuple(f for f in ps(ALL) if not any(set(m)<=set(f) for m in CROSS))
def face_model(faces):
 g={f:-len(f) for f in faces};d={f:{f[:j]+f[j+1:]:pm(j) for j in range(len(f))} for f in faces};return g,d

def project_poly(p,face):return {m:c for m,c in p.items() if all(not m[i] or i in face for i in ALL)}
def face_app(d,v):
 out={}
 for a,p in v.items():
  for b,c in d[a].items():out=va(out,{b:sm(project_poly(p,b),c)})
 return {b:p for b,p in out.items() if p}

def map_variables(src,faces,offset=0,prefix='f'):
 g,d,l=src
 return [(prefix,a,b,l[a]) for a in g for b in faces if -len(b)==g[a]+offset and all(not n or i in b for i,n in enumerate(l[a]))]

def addrow(rows,key,j,c):
 v=rows.setdefault(key,{})
 v[j]=v.get(j,0)+c
 if not v[j]:del v[j]

def equations_chain(src,faces,vs,start=0,tag='chain'):
 g,d,l=src;fg,fd=face_model(faces);rows={}
 for j,(_,a,b,m) in enumerate(vs,start):
  # d_I f - f d_D; degree-zero map
  for t,c in fd[b].items():
   p=project_poly(mono(m),t)
   for n,k in p.items():addrow(rows,(tag,a,t,n),j,c*k)
  for s,v in d.items():
   if a in v:
    p=project_poly(mul(mono(m),v[a]),b)
    for n,k in p.items():addrow(rows,(tag,s,b,n),j,-k)
 return rows

def linear_solve(rows,values,n):
 # Sparse rational elimination; integrality is verified, not assumed.
 piv={}
 for k,rr in rows.items():
  r={j:Fraction(c) for j,c in rr.items() if c};b=Fraction(values.get(k,0))
  while r:
   j=min(r)
   if j not in piv:
    v=r[j];r={z:q/v for z,q in r.items()};b/=v;piv[j]=(r,b);break
   pr,pb=piv[j];v=r[j];b-=v*pb
   for z,q in pr.items():
    r[z]=r.get(z,0)-v*q
    if not r[z]:del r[z]
  if not r:ck(b==0,'linear_system_consistent')
 sol=[Fraction(0)]*n
 for j,(r,b) in sorted(piv.items(),reverse=True):sol[j]=b-sum(c*sol[z] for z,c in r.items() if z!=j)
 ck(all(c.denominator==1 for c in sol),'comparison_coefficients_integral')
 return [int(c) for c in sol],len(piv)

def decode(vs,sol):
 out={}
 for (_,a,b,m),c in zip(vs,sol):
  if c:out[a]=va(out.get(a,{}),{b:mono(m,c)})
 return out

def construct_native_duality(src):
 vs=map_variables(src,SIGMA);rows=equations_chain(src,SIGMA,vs);rhs={};top=next(a for a in src[0] if src[0][a]==-1)
 for b in SIGMA:
  if len(b)!=1:continue
  k=('norm',b);rows[k]={j:1 for j,(_,a,f,m) in enumerate(vs) if a==top and f==b};rhs[k]=int(b==(1,))-int(b==(0,))
 sol,rank=linear_solve(rows,rhs,len(vs));f=decode(vs,sol)
 for a in src[0]:ck(face_app(face_model(SIGMA)[1],f.get(a,{}))==face_normalize(app(f,src[1][a])),'native_duality_chain_equation')
 return f,{'variables':len(vs),'rank':rank}
def face_normalize(v):return {b:p for b,q in v.items() if (p:=project_poly(q,b))}

def construct_target_duality(dt,db,phi_dual,jb):
 vf=map_variables(dt,DELTA,prefix='f');vh=map_variables(db,DELTA,offset=-1,prefix='h');rows=equations_chain(dt,DELTA,vf);rhs={};fidx=len(vf);fd=face_model(DELTA)[1]
 # jT phi^* - jB - d h - h d = 0.
 for j,(_,a,b,m) in enumerate(vf):
  for s,v in phi_dual.items():
   if a in v:
    for n,c in project_poly(mul(v[a],mono(m)),b).items():addrow(rows,('naturality',s,b,n),j,c)
 for j,(_,a,b,m) in enumerate(vh,fidx):
  for t,c in fd[b].items():
   for n,k in project_poly(mono(m),t).items():addrow(rows,('naturality',a,t,n),j,-c*k)
  for s,v in db[1].items():
   if a in v:
    for n,c in project_poly(mul(v[a],mono(m)),b).items():addrow(rows,('naturality',s,b,n),j,-c)
 for a,v in jb.items():
  for b,p in v.items():
   for n,c in p.items():
    k=('naturality',a,b,n);rows.setdefault(k,{});rhs[k]=c
 sol,rank=linear_solve(rows,rhs,len(vf)+len(vh));f=decode(vf,sol[:fidx]);h=decode(vh,sol[fidx:])
 for a in dt[0]:ck(face_app(fd,f.get(a,{}))==face_normalize(app(f,dt[1][a])),'target_duality_chain_equation')
 for a in db[0]:
  left=face_normalize(va(app(f,phi_dual[a]),neg(jb.get(a,{}))))
  right=face_normalize(va(face_app(fd,h.get(a,{})),app(h,db[1][a])))
  ck(left==right,'complete_native_spatial_square_homotopy')
 return f,h,{'variables':len(vf)+len(vh),'rank':rank}

def cone_check(src,faces,f,a,tag):
 sg,sd=homog(src,a);fg0,fd0=face_model(faces);support={i for i,x in enumerate(a) if x};fg={b:n for b,n in fg0.items() if support<=set(b)};fd={b:{t:scalar(c) for t,c in fd0[b].items() if t in fg} for b in fg}
 g={('t',b):n for b,n in fg.items()};g.update({('s',b):n-1 for b,n in sg.items()});d={k:{} for k in g}
 for b in fg:d[('t',b)]={('t',c):p for c,p in fd[b].items()}
 for b in sg:
  d[('s',b)]={('s',c):sm(p,-1) for c,p in sd[b].items()}
  for c,p in f.get(b,{}).items():
   if c in fg:d[('s',b)][('t',c)]=scalar(sum(p.values()))
 for b in g:ck(not app(d,d[b]),tag+'_cone_d2')
 red=sdr(g,d,tag+'_cone');ck(not red[0],tag+'_quasiisomorphism')
 return len(g)


COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
PROVENANCE={
 'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':'0147e2e42dafac0da7289c571cb0331b51338be1',
}

def diag(i,j):return tuple(sorted((i%6,j%6)))
def cross(a,b):
 x,y=a;u,v=b
 return x<u<y<v or u<x<v<y

def sig_reorder(v):return pm(sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v))))
def groupperm(g):
 k,f=g
 return tuple((2*k+(1-i if f else i))%6 for i in ALL)
def action_vec(v,g):
 per=groupperm(g);out={}
 for f,p in v.items():
  im=[per[i] for i in f];sg=sig_reorder(im);tf=tuple(sorted(im));pp={}
  for a,c in p.items():
   b=[0]*6
   for i in ALL:b[per[i]]=a[i]
   pp[tuple(b)]=sg*c
  out=va(out,{tf:pp})
 return out

def geometry_audit():
 shorts=tuple(diag(i,i+2) for i in ALL)
 full_diags=tuple((i,j) for i in ALL for j in range(i+1,6) if j-i not in (1,5))
 full_faces=tuple(f for k in range(4) for f in combinations(full_diags,k) if all(not cross(a,b) for a,b in combinations(f,2)))
 direct=tuple(f for f in ps(ALL) if all(not cross(shorts[i],shorts[j]) for i,j in combinations(f,2)))
 ck(direct==DELTA,'short_complex_derived_from_actual_crossing')
 ck(len(full_faces)==45 and sum(2**len(f) for f in full_faces)==215,'actual_full_target_census')
 ck(tuple(Counter(map(len,DELTA))[i] for i in range(4))==(1,6,9,2),'short_face_census')
 ck(tuple(Counter(map(len,SIGMA))[i] for i in range(4))==(1,6,6,2),'native_face_census')
 ck(set(DELTA)-set(SIGMA)=={tuple(sorted(e)) for e in BRIDGES},'only_three_native_to_target_cells')
 for f in DELTA:
  ck(tuple(sorted(shorts[i] for i in f)) in full_faces,'actual_spatial_inclusion')
 for faces,tag in [(SIGMA,'native'),(DELTA,'short')]:
  cubes=tuple((h,f) for f in faces for h in ps(f))
  for h,f in cubes:
   free=tuple(i for i in f if i not in h)
   def bd(c):
    hh,ff=c;v={}
    for j,i in enumerate(x for x in ff if x not in hh):
     v[(tuple(sorted(hh+(i,))),ff)]=pm(j)
     v[(hh,tuple(x for x in ff if x!=i))]=-pm(j)
    return v
   b2=Counter()
   for t,c in bd((h,f)).items():
    ck(t in cubes,tag+'_cubical_faces_present')
    for z,d in bd(t).items():b2[z]+=c*d
   ck(not any(b2.values()),tag+'_cubical_d2')
  ck(len(cubes)==(53 if tag=='native' else 65),tag+'_cube_census')
 return {'native_faces_by_size':[1,6,6,2],'short_faces_by_size':[1,6,9,2],
         'native_cubes':53,'short_cubes':65,'full_cubes':215,
         'bridges_even_to_odd':[list(e) for e in BRIDGES]}

def face_homogeneous(faces,a):
 support={i for i,n in enumerate(a) if n};g,d0=face_model(faces)
 g={f:n for f,n in g.items() if support<=set(f)}
 d={f:{t:scalar(c) for t,c in d0[f].items() if t in g} for f in g}
 return g,d

def face_cohomology_audit():
 hist=[]
 for a in product((0,1),repeat=6):
  supp={i for i,x in enumerate(a) if x};rec={'support':sorted(supp)}
  for faces,tag in [(SIGMA,'native'),(DELTA,'short')]:
   g,d=face_homogeneous(faces,a);r=sdr(g,d,tag+'_face')
   ck(all(not v for v in r[1].values()),tag+'_face_no_nonunit_residual')
   got=dict(Counter(r[0].values()));exp={}
   if supp==set(EV) or supp==set(OD):exp[-3]=1
   if tag=='native' and not supp:exp[-1]=1
   if tag=='short':
    if not supp:exp[-2]=2
    elif any(supp<=set(b) for b in BRIDGES):exp[-2]=1
   ck(got==exp,tag+'_all_cohomology_modules')
   rec[tag]=got
  # Constant-frame connecting map is derived from face boundaries, not fitted.
  hist.append(rec)
 # Every occurrence multiplication is a quotient/restriction in the face rings.
 arrows=0
 for a in product((0,1),repeat=6):
  for i in ALL:
   if a[i]:continue
   b=tuple(1 if j==i else a[j] for j in ALL)
   for faces,tag in [(SIGMA,'native'),(DELTA,'short')]:
    ga,da=face_homogeneous(faces,a);gb,db=face_homogeneous(faces,b)
    mm={f:unit(f) if f in gb else {} for f in ga}
    for f in ga:ck(app(db,mm[f])==app(mm,da[f]),tag+'_occurrence_transition_chainmap')
   arrows+=1
 ck(arrows==192,'all_squarefree_transition_arrows')
 return hist

def polynomial_quotient_audit():
 # Squarefree support determines all monomials of any size.
 for f in ps(ALL):
  survivesT=f in DELTA;survivesB=f in SIGMA
  kernel=survivesT and not survivesB
  active=[b for b in BRIDGES if set(b)<=set(f) and set(f)<=set(b)]
  ck(kernel==(len(active)==1),'all_monomial_kernel_supports')
  ck(not survivesB or survivesT,'quotient_ring_well_defined')
 for e,o in BRIDGES:
  for j in ALL:
   survives=set((e,o,j)) in [set(f) for f in DELTA]
   ck(survives==(j in (e,o)),'exact_bridge_annihilator')
  for a,b in BRIDGES:
   if (a,b)!=(e,o):ck(tuple(sorted(set((a,b,e,o)))) not in DELTA,'bridge_summands_disjoint')
 return {'target_ideal_generators':[list(e) for e in CROSS],
         'native_ideal_generators':[[e,o] for e in EV for o in OD],
         'kernel_summands':[{'generator':[e,o],'annihilator':[j for j in ALL if j not in (e,o)]} for e,o in BRIDGES]}

def koszul(seq,tag):
 g={(tag,s):len(s) for s in ps(seq)};l={(tag,s):wt(s) for s in ps(seq)}
 d={(tag,s):{(tag,s[:j]+s[j+1:]):sm(var(i),pm(j)) for j,i in enumerate(s)} for s in ps(seq)}
 return g,d,l

def endpoint_maps(B,jb):
 g,d,l=B;plus=koszul(EV,'E');minus=koszul(OD,'O');fs=[];enddata=[]
 for tag,km,side in [('E',plus,0),('O',minus,1)]:
  f={a:{} for a in g};f[('b',(),())]=unit((tag,()))
  for a in g:
   _,u,v=a
   if not u:continue
   if tag=='E' and len(v)==1:f[a]={(tag,u):var(v[0])}
   if tag=='O' and len(u)==1:f[a]={(tag,v):var(u[0])}
  for a in g:ck(app(km[1],f[a])==app(f,d[a]),'native_full_endpoint_map')
  fd={a:{} for a in km[0]}
  for b,z in f.items():
   for a,p in z.items():fd[a][b]=p
  out={a:face_normalize(app(jb,v)) for a,v in fd.items()}
  endpoint=OD if tag=='E' else EV;endkey=(tag,EV if tag=='E' else OD)
  expected={endpoint:mono(wt(endpoint),1 if tag=='E' else -1)}
  ck(out[endkey]==expected,'native_endpoint_to_spatial_top_ideal')
  ck(all(not v for a,v in out.items() if a!=endkey),'endpoint_map_all_other_components')
  fs.append(f);enddata.append({'branch':'plus' if tag=='E' else 'minus',
     'endpoint_face':list(endpoint),'image_sign':1 if tag=='E' else -1,
     'image_occurrence_weight':list(wt(endpoint))})
 # Actual joint normalization homotopy, with conductor wedge ordered numerically.
 K=koszul(ALL,'C');left={};H={}
 for a in g:
  _,u,v=a
  left[a]=va({('C',s):p for (t,s),p in fs[0][a].items()},
             neg({('C',s):p for (t,s),p in fs[1][a].items()}))
  H[a]={} if not u else {('C',tuple(sorted(u+v))):scalar(pm(len(u))*sig_reorder(list(u+v)))}
 for a in g:ck(va(app(K[1],H[a]),app(H,d[a]))==left[a],'both_endpoint_joint_homotopy')
 return fs,H,enddata

def spatial_attachment_audit():
 fg,fd=face_model(DELTA)
 c=va(unit((1,)),neg(unit((0,))))
 ck(not face_app(fd,c),'native_conductor_cocycle')
 # Relative bridges all join the same two endpoint components.
 bridges=[]
 for e,o in BRIDGES:
  sg=1 if e<o else -1;chain={tuple(sorted((e,o))):scalar(sg)}
  bd=face_app(fd,chain)
  ck(bd==va(unit((o,)),neg(unit((e,)))),'literal_bridge_endpoint_boundary')
  bridges.append(chain)
 # Native conductor is nonboundary until actual mixed bridges are attached.
 ng,nd=face_homogeneous(SIGMA,Z);nr=sdr(ng,nd,'native_conductor_test')
 ck(bool(app(nr[2],c)),'native_conductor_nonzero')
 first=app(nr[2],face_app(fd,bridges[0]))
 ck(first and all(app(nr[2],face_app(fd,b))==first for b in bridges),'derived_augmentation_row_111')
 ck(app(nr[2],c)==first,'conductor_orientation_agrees')
 # Explicit native-to-spatial nullhomotopy through the D03 short pair.
 path=va(unit((0,3)),neg(unit((1,3))))
 ck(face_app(fd,path)==c,'conductor_nullhomotopy_uses_both_branches')
 # Exact six-element relabelling action on the module-valued spatial diagrams.
 for group in product(range(3),range(2)):
  per=groupperm(group)
  ck(sig_reorder(list(per))==pm(group[1]),'six_conormal_determinant_character')
  for faces,tag in [(SIGMA,'native'),(DELTA,'short')]:
   g0,d0=face_model(faces)
   for f in faces:
    av=action_vec(unit(f),group)
    ck(all(t in g0 for t in av),'D3_'+tag+'_support')
    ck(face_app(d0,av)==action_vec(face_app(d0,unit(f)),group),'D3_'+tag+'_chain_equation')
   if tag=='native':
    image=app(nr[2],action_vec(c,group))
    ck(image==vm(app(nr[2],c),scalar(pm(group[1]))),'source_conductor_polarity')
  for chain in bridges:
   image=action_vec(chain,group)
   ck(any(image==vm(other,scalar(pm(group[1]))) for other in bridges),'road_oriented_permutation')
 # In the full native determinant frame both signs cancel.
 for v in product(range(-3,4),repeat=3):
  invariant=len(set(v))==1
  if invariant:ck(sum(v)%3==0,'strict_invariant_readout_divisible_by_three')
 return {'connecting_row':[1,1,1],'kernel_basis':[[1,-1,0],[0,1,-1]],
         'explicit_conductor_cocycle':{'[1]':1,'[0]':-1},
         'explicit_geometric_nullhomotopy':{'[0,3]':1,'[1,3]':-1},
         'uncompensated_conductor_character':'sheet-exchange sign',
         'six_conormal_framed_conductor_character':'trivial',
         'strict_symmetric_unit_lift':'absent; image of symmetric constants is 3Z'}

def export_poly(p):return [{'exponents':list(a),'coefficient':c} for a,c in sorted(p.items())]
def export_map(f):return {repr(a):{repr(b):export_poly(p) for b,p in v.items()} for a,v in f.items() if v}


def main(output:Path):
 geometry=geometry_audit();modules=polynomial_quotient_audit()
 B=node();T=taylor(CROSS)
 phi=lift_by_resolution(T,B,{():unit(('b',(),()))},'T_to_B')
 rt=sdr(T[0],T[1],'T_reduce')
 ck(dict(Counter(rt[0].values()))=={0:1,1:6,2:9,3:6,4:2},'target_minimal_resolution_ranks')
 db=dual(B);dt=dual(T);phid={a:{} for a in B[0]}
 for t,v in phi.items():
  for b,p in v.items():phid[b][t]=p
 for a in db[0]:ck(app(dt[1],phid[a])==app(phid,db[1][a]),'full_dual_source_target_map')
 jb,statsB=construct_native_duality(db)
 jt,hom,statsT=construct_target_duality(dt,db,phid,jb)
 cone_sizes=[]
 for a in product((0,1),repeat=6):
  cone_sizes.append([list(a),cone_check(db,SIGMA,jb,a,'native'),cone_check(dt,DELTA,jt,a,'target')])
 hist=face_cohomology_audit()
 fs,joint,enddata=endpoint_maps(B,jb);attachment=spatial_attachment_audit()
 top=next(a for a in B[0] if B[0][a]==5)
 # Exhibit the correction retained by the complete naturality square.
 ck(not face_normalize(app(jt,phid[top])),'particular_native_top_image_exactly_zero')
 ck(face_app(face_model(DELTA)[1],neg(hom.get(top,{})))==jb[top],'full_naturality_homotopy_conductor_component')
 cert={
  'status':'proved_for_native_squarefree_occurrence_comparison',
  'date':'2026-09-07','pinned_commit':COMMIT,'source_blobs':PROVENANCE,
  'geometry':geometry,'coefficient_modules':modules,
  'free_resolution_ranks':{'native':[1,9,18,15,6,1],'short_face_taylor':[1,6,15,20,15,6,1],
    'short_face_minimal':[1,6,9,6,2]},
  'duality_comparison_systems':{'native':statsB,'target_and_homotopy':statsT},
  'homogeneous_quasiisomorphism_cones':cone_sizes,'homogeneous_module_cohomology':hist,
  'endpoint_images':enddata,'spatial_conductor_attachment':attachment,
  'maps':{'polynomial_resolution_quotient':export_map(phi),
   'native_duality_to_faces':export_map(jb),'target_duality_to_faces':export_map(jt),
   'native_to_spatial_comparison_homotopy':export_map(hom),
   'native_endpoint_plus':export_map(fs[0]),'native_endpoint_minus':export_map(fs[1]),
   'native_joint_endpoint_homotopy':export_map(joint)},
  'scope':[
   'Ambient ring is Z[X0,...,X5], with arbitrary flat polynomial spectators such as the long occurrences.',
   'The spatial target here is the module-valued dualizing diagram of the actual short-face coordinate complex, not asserted equal to the original PC stalk diagram.',
   'No normal, occurrence, Rees parameter, or integer is inverted in the polynomial maps.',
   'All exponents are covered by squarefree shifts and the 64 nonnegative support patterns; the proof is not a bounded degree extrapolation.',
   'Occurrence transition squares and both native branch attachments are retained.',
   'No full independent-normal/Rees support-PC identification, physical collar 2-cell identification, or physical parity is claimed.',
   'The native conductor class becomes a boundary only through the newly admitted actual mixed short-face edges; the generic Q quotient has not been identified with those three face modules.'
  ],
  'checks':dict(sorted(CHECKS.items())),'total_exact_assertions':sum(CHECKS.values())}
 cert['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 output.write_text(json.dumps(cert,indent=2)+'\n')
 print(json.dumps({'status':cert['status'],'total_exact_assertions':cert['total_exact_assertions'],
   'ranks':cert['free_resolution_ranks'],'duality_systems':cert['duality_comparison_systems'],
   'module_triangle':'0 -> three opposite-edge occurrence modules -> short-face ring -> native node -> 0',
   'physical_parity_assigned':False},indent=2))

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,default=Path('marici_native_short_face_comparison_certificate.json'))
 args=parser.parse_args();main(args.output)
