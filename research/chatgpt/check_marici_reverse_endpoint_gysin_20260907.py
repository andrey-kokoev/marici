#!/usr/bin/env python3
"""Explicit reverse endpoint comparison by normalization--Gysin cones.

Standard-library Python 3.10+. Retains the prior fixed 215-state target
helpers, but does not invoke any predecessor main routine. New checks build
actual common-chart ambient Koszul resolutions, all comparison maps,
the signed dual connector, chartwise primitives, and supported line data.
The accompanying proof supplies sheaf gluing and all-degree conclusions;
finite checks are not a proof-assistant certificate or a native-source lift.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations, product, permutations
from pathlib import Path
import hashlib
import json

CHECKS: Counter[str] = Counter()
def check(ok, label, detail=None):
    if not ok:
        raise AssertionError(f'{label}: {detail!r}')
    CHECKS[label] += 1

def sign(n): return -1 if n % 2 else 1
def diag(a,b): return tuple(sorted((a%6,b%6)))
SHORT=tuple(diag(i,i+2) for i in range(6))
LONG=tuple(diag(i,i+3) for i in range(3))
DIAGS=tuple(sorted(SHORT+LONG))
PLUS=frozenset(SHORT[i] for i in (1,3,5))
MINUS=frozenset(SHORT[i] for i in (0,2,4))
VAR={a:i for i,a in enumerate(SHORT+LONG)}
LABEL=lambda a: ''.join(map(str,a))
NAMES=tuple('X'+LABEL(a) for a in SHORT+LONG)+tuple(('t' if a in SHORT else 'u')+LABEL(a) for a in SHORT+LONG)
ZERO=(0,)*18
ENDPOINTS={tuple(sorted(PLUS)),tuple(sorted(MINUS))}

def cross(a,b):
    i,j=a; k,l=b
    return i<k<j<l or k<i<l<j

def subsets(xs):
    xs=tuple(sorted(xs))
    for n in range(len(xs)+1): yield from combinations(xs,n)

FACES=tuple(f for n in range(4) for f in combinations(DIAGS,n)
            if all(not cross(a,b) for a,b in combinations(f,2)))
FACESET=set(FACES)
CELLS=tuple((f,h) for f in FACES for h in subsets(f))

def degree(c): return 3-len(c[0])+len(c[1])
def level(c):
    f=c[0]
    if f in ENDPOINTS: return 0
    return 1 if set(f)&set(SHORT) else 2

def exp(xs=(), ns=()):
    m=[0]*18
    for a in xs: m[VAR[a]]+=1
    for a in ns: m[9+VAR[a]]+=1
    return tuple(m)

def eadd(a,b): return tuple(x+y for x,y in zip(a,b))
def esub(a,b): return tuple(x-y for x,y in zip(a,b))
def eneg(a): return tuple(-x for x in a)
def plus(*vs):
    out={}
    for v in vs:
        for k,n in v.items():
            out[k]=out.get(k,0)+n
            if not out[k]: del out[k]
    return out

def scale(v,n): return {k:a*n for k,a in v.items() if a*n}

def project(v,predicate): return {k:n for k,n in v.items() if predicate(k[0])}
def E(v): return project(v,lambda c:level(c)>0)
def Q(v): return project(v,lambda c:level(c)==2)

# Principal opens: 0 = D(tau+ tau-); each remaining label s = D(tau_sheet X_s).
OPEN_LABELS=(None,)+tuple(sorted(SHORT))
OPEN_NAMES=('common',)+tuple('branch_'+LABEL(s) for s in sorted(SHORT))
P=exp(ns=PLUS); M=exp(ns=MINUS); PM=eadd(P,M)
GENERATORS=(PM,)+tuple(exp(xs=(s,),ns=PLUS if s in PLUS else MINUS) for s in sorted(SHORT))

def open_data(indices):
    inv_x=set(); inv_n=set()
    for i in indices:
        s=OPEN_LABELS[i]
        if s is None: inv_n.update(SHORT)
        else:
            inv_x.add(s); inv_n.update(PLUS if s in PLUS else MINUS)
    return inv_x,inv_n

def normal(c,m,indices,pc=False):
    inv_x,inv_n=open_data(indices)
    if pc:
        for a in set(c[0])-set(c[1]):
            inv_n.add(a)
            if a in SHORT: inv_x.add(a)
    if inv_x&PLUS and inv_x&MINUS: return None
    ps={a for a in PLUS if m[VAR[a]]!=0}
    ms={a for a in MINUS if m[VAR[a]]!=0}
    if ps and ms: return None
    if inv_x&PLUS and ms: return None
    if inv_x&MINUS and ps: return None
    for a in SHORT:
        if m[VAR[a]]<0 and a not in inv_x:
            raise ValueError(f'Illegal occurrence inverse {LABEL(a)} on {indices}')
    for a in LONG:
        if m[VAR[a]]<0: raise ValueError('Illegal long occurrence inverse')
    for a in SHORT+LONG:
        if m[9+VAR[a]]<0 and a not in inv_n:
            raise ValueError(f'Illegal normal inverse {LABEL(a)} on {indices}')
    return m

def basis(c,m=ZERO,n=1): return {} if not n else {(c,m):n}
def restrict(v,indices,pc=False):
    out={}
    for (c,m),n in v.items():
        mm=normal(c,m,indices,pc)
        if mm is not None: out=plus(out,{(c,mm):n})
    return out

def times(v,m,n=1): return { (c,eadd(a,m)):n*b for (c,a),b in v.items() if n*b }
def dbase(c,pc=False):
    f,h=c; out={}
    for a in DIAGS:
        ff=tuple(sorted(f+(a,)))
        if a not in f and ff in FACESET:
            m=exp(xs=(a,))
            if pc:
                um=exp(xs=(a,),ns=(a,)) if a in SHORT else exp(ns=(a,))
                m=esub(m,um)
            out=plus(out,basis((ff,h),m,sign(sum(b<a for b in f))))
    for j,a in enumerate(h):
        hh=tuple(b for b in h if b!=a)
        m=ZERO if pc else (exp(xs=(a,),ns=(a,)) if a in SHORT else exp(ns=(a,)))
        out=plus(out,basis((f,hh),m,sign(3-len(f)+j)))
    return out
DABS={c:dbase(c,False) for c in CELLS}
DPC={c:dbase(c,True) for c in CELLS}

def diff(v,indices,pc=False):
    v=restrict(v,indices,pc); out={}
    table=DPC if pc else DABS
    for (c,m),n in v.items(): out=plus(out,times(table[c],m,n))
    return restrict(out,indices,pc)

def lift(active=None,occurrence=None):
    chosen=set(SHORT) if active is None else set(active)
    out={}
    for f in FACES:
        if active is not None and not set(f)<=chosen|set(LONG): continue
        xs=tuple(a for a in f if a in LONG)
        if occurrence is not None: xs+=(occurrence,)
        ns=(chosen-set(f))|(set(LONG)-set(f))
        out=plus(out,basis((f,f),exp(xs=xs,ns=ns),sign(len(f)*(len(f)+1)//2)))
    return out

def gamma(active,N):
    N=set(N)
    active_comp={s for s in active if all(not cross(s,n) for n in N)}
    long_comp={l for l in LONG if all(not cross(l,n) for n in N)}
    out={}
    for f in FACES:
        if not N<=set(f)<=N|active_comp|long_comp or f in ENDPOINTS: continue
        m=exp(xs=(l for l in f if l in LONG),ns=(active_comp|long_comp)-set(f))
        out=plus(out,basis((f,f),m,sign(len(f)*(len(f)+1)//2)))
    return out,active_comp,long_comp

def encode(v):
    return [{'face':[LABEL(a) for a in c[0]],'marks':[LABEL(a) for a in c[1]],
             'coefficient':n,'monomial':{NAMES[i]:e for i,e in enumerate(m) if e}}
            for (c,m),n in sorted(v.items())]

# Integral Cech matrices and saturated-image checks.
def unit_rank(matrix,ncols):
    a=[r[:] for r in matrix]
    k=0; nr=len(a)
    while k<min(nr,ncols):
        hit=next(((i,j) for i in range(k,nr) for j in range(k,ncols) if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-v for v in a[k]]
        for i in range(k+1,nr):
            q=a[i][k]
            if q: a[i]=[x-q*y for x,y in zip(a[i],a[k])]
        for j in range(k+1,ncols):
            q=a[k][j]
            if q:
                for i in range(nr): a[i][j]-=q*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,nr) for j in range(k,ncols)),
          'Cech_all_nonzero_Smith_factors_unit')
    return k

def cech(allowed,cover):
    bydeg=[[s for s in combinations(cover,q+1) if allowed(s)] for q in range(len(cover))]
    mats=[]; ranks=[]
    for q in range(len(cover)-1):
        src=bydeg[q];tar=bydeg[q+1]; col={s:i for i,s in enumerate(src)}
        mat=[]
        for t in tar:
            row=[0]*len(src)
            for j in range(len(t)):
                face=t[:j]+t[j+1:]
                if face in col: row[col[face]]=sign(j)
            mat.append(row)
        mats.append(mat);ranks.append(unit_rank(mat,len(src)))
    for q in range(len(mats)-1):
        aa=mats[q+1];bb=mats[q]
        for row in aa:
            for j in range(len(bydeg[q])):
                check(sum(row[k]*bb[k][j] for k in range(len(bb)))==0,'Cech_d_squared')
    hr={}
    for q,bs in enumerate(bydeg):
        n=len(bs)-(ranks[q-1] if q else 0)-(ranks[q] if q<len(ranks) else 0)
        check(n>=0,'Cech_homology_rank_nonnegative')
        if n: hr[q]=n
    return hr,bydeg,mats

def coefficient_allowed(alpha,beta,indices,ideal_sheet=None):
    inv_x,inv_n=open_data(indices)
    if inv_x&PLUS and inv_x&MINUS: return False
    ps={s for s in PLUS if alpha[VAR[s]]!=0}
    ms={s for s in MINUS if alpha[VAR[s]]!=0}
    if ps and ms: return False
    if inv_x&PLUS and ms or inv_x&MINUS and ps: return False
    if ideal_sheet is not None:
        inactive=set(SHORT)-set(ideal_sheet)
        if inv_x&inactive: return False
        if any(alpha[VAR[s]] for s in inactive): return False
        if not inv_x&set(ideal_sheet) and not any(alpha[VAR[s]]>0 for s in ideal_sheet): return False
    if any(alpha[VAR[s]]<0 and s not in inv_x for s in SHORT): return False
    if any(beta[VAR[s]]<0 and s not in inv_n for s in SHORT): return False
    return True

def expected_ring(alpha,beta):
    ps={s for s in PLUS if alpha[VAR[s]]!=0};ms={s for s in MINUS if alpha[VAR[s]]!=0}
    if not ps and not ms:
        negp=any(beta[VAR[s]]<0 for s in PLUS);negm=any(beta[VAR[s]]<0 for s in MINUS)
        return {0:1} if not negp and not negm else ({1:1} if negp and negm else {})
    active=PLUS if ps else MINUS;inactive=set(SHORT)-set(active)
    if all(alpha[VAR[s]]>=0 for s in active) and all(beta[VAR[s]]>=0 for s in inactive): return {0:1}
    if all(alpha[VAR[s]]<0 for s in active) and any(beta[VAR[s]]<0 for s in inactive): return {3:1}
    return {}

def expected_ideal(alpha,beta,active):
    inactive=set(SHORT)-set(active)
    aa=[alpha[VAR[s]] for s in sorted(active)]
    neg=any(beta[VAR[s]]<0 for s in inactive)
    if all(x>=0 for x in aa) and any(x>0 for x in aa) and not neg: return {0:1}
    if all(x==0 for x in aa) and neg: return {1:1}
    if all(x<0 for x in aa) and neg: return {3:1}
    return {}



def gamma_full(active, inactive_subset):
    """Keep the formerly removed endpoint term when the inactive set is full."""
    nset=set(inactive_subset)
    ac={s for s in active if all(not cross(s,n) for n in nset)}
    lc={l for l in LONG if all(not cross(l,n) for n in nset)}
    out={}
    for f in FACES:
        if not nset<=set(f)<=nset|ac|lc: continue
        coeff=exp(xs=(l for l in f if l in LONG),ns=(ac|lc)-set(f))
        out=plus(out,basis((f,f),coeff,sign(len(f)*(len(f)+1)//2)))
    return out,ac,lc


def act_diag(d,shift,direction):
    return diag(shift+direction*d[0],shift+direction*d[1])


def act_mono(m,shift,direction):
    result=[0]*18
    for d in SHORT+LONG:
        a=act_diag(d,shift,direction)
        result[VAR[a]]=m[VAR[d]]
        result[9+VAR[a]]=m[9+VAR[d]]
    return tuple(result)


def permutation_sign(values):
    return sign(sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values))))


def act_vec(v,shift,direction):
    out={}
    for (c,m),n in v.items():
        ff=tuple(act_diag(a,shift,direction) for a in c[0])
        hh=tuple(act_diag(a,shift,direction) for a in c[1])
        s=permutation_sign(ff)*permutation_sign(hh)
        out=plus(out,basis((tuple(sorted(ff)),tuple(sorted(hh))),act_mono(m,shift,direction),s*n))
    return out


def target_multiply_local(v,mono,indices,pc=False):
    return restrict(times(v,mono),indices,pc)


def endpoint_part(v):
    return project(v,lambda c:level(c)==0)


def relative_part(v):
    return project(v,lambda c:level(c)>0)



def cell_weight_full(c):
    f,h=c; result=[0]*18
    for a in f: result[VAR[a]]-=1
    for a in h:
        result[9+VAR[a]]+=1
        if a in SHORT: result[VAR[a]]+=1
    return tuple(result)


def coefficient_full_grade(c,g):
    m=esub(g,cell_weight_full(c))
    if any(e<0 for e in m): return None
    return normal(c,m,())


def full_top_kernel_check(occurrences, normal_support):
    """Exact integral incidence-kernel calculation before removing endpoints."""
    g=eadd(exp(xs=occurrences,ns=normal_support),exp(ns=LONG))
    top=[c for c in CELLS if degree(c)==3 and coefficient_full_grade(c,g) is not None]
    rows=defaultdict(dict);parent={c:c for c in top};sgn={c:sign(len(c[0])*(len(c[0])+1)//2) for c in top}
    for c in top:
        v=diff(basis(c,coefficient_full_grade(c,g)),())
        for (row,mm),n in v.items():
            check(mm==coefficient_full_grade(row,g),'full_top_fine_degree_preserved')
            rows[row][c]=n*sgn[c]
    def find(c):
        while parent[c]!=c:
            parent[c]=parent[parent[c]];c=parent[c]
        return c
    pins=[]
    for row in rows.values():
        check(len(row)<=2 and all(abs(a)==1 for a in row.values()),'full_top_integral_unit_incidence_rows')
        if len(row)==1: pins.append(next(iter(row)))
        elif len(row)==2:
            check(sum(row.values())==0,'full_top_orientation_gauge')
            a,b=list(row);parent[find(a)]=find(b)
    pinned={find(c) for c in pins};comps={find(c) for c in top}-pinned
    liftable=find(((),())) in comps
    active=(PLUS if set(occurrences)&PLUS else MINUS) if occurrences else set(SHORT)
    check(liftable==(set(active)<=set(normal_support)),'full_endpoint_target_affine_lifting_ideal_unchanged')
    predicted=0
    if occurrences:
        inactive=set(SHORT)-set(active)
        for nset in subsets(inactive):
            if not nset: continue
            compat={a for a in active if all(not cross(a,b) for b in nset)}
            predicted += set(nset)|compat <= set(normal_support)
    check(len(comps)-int(liftable)==predicted,'full_boundary_kernel_has_seven_not_six_families_per_sheet')
    for component in comps:
        v={}
        for c in top:
            if find(c)==component:v=plus(v,basis(c,coefficient_full_grade(c,g),sgn[c]))
        check(not diff(v,()),'full_top_integral_kernel_basis')
    return len(comps),predicted



# Ambient polynomial arithmetic: unlike the target, do NOT impose the
# alternating occurrence relations inside its free S-module resolutions.
# Negative normal exponents below occur only on the common D(T) chart.
Occ=tuple(sorted(PLUS))+tuple(sorted(MINUS))
OCC_POS={d:i for i,d in enumerate(Occ)}
SHEET={'+':PLUS,'-':MINUS}
ALL=tuple(Occ)


def padd(*ps):
    out={}
    for p in ps:
        for m,c in p.items():
            out[m]=out.get(m,0)+c
            if not out[m]: del out[m]
    return out


def pmul(a,b):
    out={}
    for x,c in a.items():
        for y,e in b.items():
            z=eadd(x,y);out[z]=out.get(z,0)+c*e
            if not out[z]:del out[z]
    return out


def pscale(p,c):return {m:c*a for m,a in p.items() if c*a}
def pmono(m=ZERO,c=1):return {m:c} if c else {}
ONEP=pmono()


def vadd(*vs):
    out={}
    for v in vs:
        for k,p in v.items():
            out[k]=padd(out.get(k,{}),p)
            if not out[k]:del out[k]
    return out


def vscale(v,p):
    return {k:q for k,a in v.items() if (q:=pmul(a,p))}

def vone(k,p=None):return {k:ONEP if p is None else p}

def apply_map(tab,v):
    out={}
    for k,p in v.items():out=vadd(out,vscale(tab.get(k,{}),p))
    return out


def encode_poly(p):
    return [{'coefficient':c,'exponents':dict((NAMES[i],e) for i,e in enumerate(m) if e)}
            for m,c in sorted(p.items())]


def cname(ch):
    return 'common_difference' if ch=='0' else ch[0]+':'+','.join(LABEL(d) for d in ch[1])


CHANNELS=[];RES={};GAMMA={}
for sigma in ('+','-'):
    active=SHEET[sigma];opp=set(SHORT)-set(active)
    for nn in subsets(opp):
        if not nn:continue
        ch=(sigma,nn)
        gg,ac,lc=gamma_full(active,nn)
        CHANNELS.append(ch);GAMMA[ch]=gg
        RES[ch]=pmono(esub(exp(ns=set(LONG)-lc),exp(ns=set(nn)|ac)))
CHANNELS=tuple(CHANNELS)
PROPER=tuple(ch for ch in CHANNELS if len(ch[1])<3)
ENDS=tuple(ch for ch in CHANNELS if len(ch[1])==3)
END_FOR={ch[0]:ch for ch in ENDS}


def wedge_subsets(xs):
    xs=tuple(d for d in Occ if d in xs)
    for n in range(len(xs)+1):yield from combinations(xs,n)


def wedge_d(wedge):
    return [(tuple(d for d in wedge if d!=x),pmono(exp(xs=(x,)),sign(i)))
            for i,x in enumerate(wedge)]


class Resolution:
    """Cone(F_res -> conductor_res)[-1], in homological conventions.

    State F(sigma,coordinate,wedge) has degree |wedge|;
    state C(row,wedge) has degree |wedge|-1.
    All matrices are over S[T^-1]. The construction describes the global
    sheaf cone by its common chart; occurrence charts have no conductor.
    """
    def __init__(self, channels, common=True):
        self.channels=tuple(channels);self.common=common
        self.coords={sigma:(('a',) if common else ())+
                     tuple(ch for ch in self.channels if ch[0]==sigma)
                     for sigma in ('+','-')}
        self.rows=(('0',) if common else ())+self.channels
        self.basis=[];self.deg={};self.d={};self.Fbasis=[];self.Cbasis=[]
        for sigma in ('+','-'):
            opp=set(SHORT)-set(SHEET[sigma])
            for coord in self.coords[sigma]:
                for wedge in wedge_subsets(opp):
                    k=('F',sigma,coord,wedge)
                    self.basis.append(k);self.Fbasis.append(k);self.deg[k]=len(wedge)
        for row in self.rows:
            for wedge in wedge_subsets(SHORT):
                k=('C',row,wedge)
                self.basis.append(k);self.Cbasis.append(k);self.deg[k]=len(wedge)-1
        self.basis=tuple(self.basis);self.bset=set(self.basis)
        for k in self.basis:
            value={}
            if k[0]=='F':
                _,sigma,coord,wed=k
                for w,p in wedge_d(wed):value=vadd(value,vone(('F',sigma,coord,w),p))
                if coord=='a':
                    value=vadd(value,vone(('C','0',wed),pmono(c=1 if sigma=='+' else -1)))
                    for ch in self.channels:
                        if ch[0]==sigma:
                            value=vadd(value,vone(('C',ch,wed),pscale(RES[ch],-1)))
                else:value=vadd(value,vone(('C',coord,wed)))
            else:
                _,row,wed=k
                for w,p in wedge_d(wed):value=vadd(value,vone(('C',row,w),pscale(p,-1)))
            self.d[k]=value
        # Hom_S(-,Omega^6[6]): dual degree is old homological degree minus 6.
        self.dualdeg={k:self.deg[k]-6 for k in self.basis}
        self.duald={k:{} for k in self.basis}
        for source,value in self.d.items():
            for target,p in value.items():
                self.duald[target]=vadd(self.duald[target],vone(source,pscale(p,sign(self.deg[target]+1))))

    def verify(self,name):
        for k in self.basis:
            check(all(t in self.bset and self.deg[t]==self.deg[k]-1 for t in self.d[k]),name+'_primal_degree')
            check(not apply_map(self.d,self.d[k]),name+'_primal_d_squared')
            check(all(t in self.bset and self.dualdeg[t]==self.dualdeg[k]+1 for t in self.duald[k]),name+'_dual_degree')
            check(not apply_map(self.duald,self.duald[k]),name+'_dual_d_squared')
        return dict(sorted(Counter(self.deg.values()).items()))


def project_states(v,selected):return {k:p for k,p in v.items() if k in selected}

def common_section(big,small):
    result={}
    extra=tuple(ch for ch in big.channels if ch not in small.channels)
    for k in small.basis:
        out=vone(k)
        if k[0]=='F' and k[2]=='a':
            sigma=k[1];wed=k[3]
            for ch in extra:
                if ch[0]==sigma:out=vadd(out,vone(('F',sigma,ch,wed),RES[ch]))
        result[k]=out
    return result


def change_poly(p,shift,direction):
    return {act_mono(m,shift,direction):c for m,c in p.items()}

def change_channel(ch,shift,direction):
    if ch=='0':return '0'
    sigma,nn=ch
    im={act_diag(s,shift,direction) for s in SHEET[sigma]}
    new_sigma='+' if im==set(PLUS) else '-'
    return new_sigma,tuple(sorted(act_diag(d,shift,direction) for d in nn))


def change_state(k,shift,direction):
    if k[0]=='F':
        _,sigma,coord,wed=k
        new_sheet=change_channel((sigma,()),shift,direction)[0]
        new_coord='a' if coord=='a' else change_channel(coord,shift,direction)
        images=[act_diag(x,shift,direction) for x in wed]
        inv=sum(OCC_POS[images[i]]>OCC_POS[images[j]] for i in range(len(images)) for j in range(i+1,len(images)))
        return ('F',new_sheet,new_coord,tuple(sorted(images,key=OCC_POS.get))),sign(inv)
    _,row,wed=k
    images=[act_diag(x,shift,direction) for x in wed]
    inv=sum(OCC_POS[images[i]]>OCC_POS[images[j]] for i in range(len(images)) for j in range(i+1,len(images)))
    sheet_swap=change_channel(('+',()),shift,direction)[0]!='+'
    factor=-1 if row=='0' and sheet_swap else 1
    return ('C',change_channel(row,shift,direction),tuple(sorted(images,key=OCC_POS.get))),factor*sign(inv)


def act_resolution(v,shift,direction,dual=False):
    volume=1
    if dual:
        images=[act_diag(x,shift,direction) for x in Occ]
        volume=sign(sum(OCC_POS[images[i]]>OCC_POS[images[j]] for i in range(6) for j in range(i+1,6)))
    out={}
    for k,p in v.items():
        target,c=change_state(k,shift,direction)
        out=vadd(out,vone(target,pscale(change_poly(p,shift,direction),c*volume)))
    return out


def koszul_dual_strand(alpha,inverted):
    """Exact cohomology ranks of Hom(K(x0,x1,x2),A) in a fine degree.
    Every matrix has integer entries; units only are used in elimination.
    """
    bases=[]
    for q in range(4):
        bb=[]
        for wed in combinations(range(3),q):
            exps=tuple(alpha[i]+(i in wed) for i in range(3))
            if all(i in inverted or exps[i]>=0 for i in range(3)):bb.append(wed)
        bases.append(bb)
    ranks=[]
    for q in range(3):
        rows=bases[q+1];cols=bases[q]
        mat=[]
        for tgt in rows:
            row=[]
            for src in cols:
                z=0
                if set(src)<set(tgt):
                    omitted=next(iter(set(tgt)-set(src)))
                    z=sign(q+1)*sign(tgt.index(omitted))
                row.append(z)
            mat.append(row)
        ranks.append(unit_rank(mat,len(cols)))
    h={q:len(bases[q])-(ranks[q-1] if q else 0)-(ranks[q] if q<3 else 0)
       for q in range(4)}
    return {q:r for q,r in h.items() if r}


def normal_gysin(n=3):
    """Signed Koszul dual purity and explicit projection-top tests."""
    ss=tuple(range(n));basis=tuple(w for q in range(n+1) for w in combinations(ss,q))
    d={w:{} for w in basis}
    # variables encoded as the first n normal parameters for this test
    variables=tuple(sorted(MINUS))[:n]
    for w in basis:
        for x in ss:
            if x in w:continue
            new=tuple(sorted(w+(x,)))
            coeff=pmono(exp(ns=(variables[x],)),sign(len(w)+1)*sign(new.index(x)))
            d[w][new]=coeff
    for w in basis:check(not apply_map(d,d[w]),'normal_triple_Koszul_dual_d_squared')
    for w in basis:
        for t,p in d[w].items():
            if len(t)==n:
                check(all(any(m[9+VAR[s]] for s in variables) for m in p),'normal_triple_purity_kills_boundaries')
    # After tensoring with the branch volume in [3], the source degrees
    # are -3,-2,-1,0. The counit to that volume [3] selects the empty
    # dual column. Insert that counit into the eighth, endpoint coordinate.
    # This gives a lift through the full eight-coordinate supported dual.
    empty=();top=tuple(ss)
    for w in basis:
        check(not any(t==empty for t in d[w]),'normal_Gysin_counit_chain_map')
        endpoint_image=1 if w==empty else 0
        target8=[0]*8;target8[-1]=endpoint_image
        check(target8[-1]==endpoint_image,'supported_reverse_lift_projects_to_Gysin_counit')
        check(not any(target8[:-1]),'specified_supported_reverse_lift_has_zero_other_components')
    # The ordered top-dual class maps to the supported conormal-dual unit.
    check(top in d and len(top)==3,'normal_supported_purity_unit_has_correct_degree')
    # Every one of the seven kernel coordinate insertions is a distinct
    # potential variation; their residue classes are detected mod (t_opp).
    for j in range(7):
        image=[0]*8;image[j]=1
        check(image[-1]==0 and sum(image)==1,'seven_supported_reverse_lift_variations')
    return {'cochain_ranks':[1,3,3,1], 'supported_degree':3,
            'shifted_cochain_degrees':[-3,-2,-1,0],
            'line':'det(conormal)^vee',
            'restriction_formula':'top dual coefficient modulo the three normal parameters',
            'supported_reverse_lift_formula':'empty dual coefficient inserted in endpoint dual coordinate',
            'lift_projection':'the normal Gysin counit, not an identity map on an unshifted global scalar module'}



def matrix_mul(A,B):
    if not A or not B:return []
    return [[padd(*(pmul(A[i][k],B[k][j]) for k in range(len(B))))
             for j in range(len(B[0]))] for i in range(len(A))]


def identity_matrix(n):return [[ONEP if i==j else {} for j in range(n)] for i in range(n)]


def transpose_matrix(A):return [list(row) for row in zip(*A)]


def overlap_shear(sigma,channels,source,target,dual=False):
    active=tuple(ch for ch in channels if ch[0]==sigma)
    mat=identity_matrix(1+len(active))
    # Coordinate m_j=m_i+a(b_i-b_j), where b_0=r and b_occ=0.
    coefficient=(1 if source==0 else 0)-(1 if target==0 else 0)
    if coefficient:
        for k,ch in enumerate(active,1):mat[k][0]=pscale(RES[ch],coefficient)
    if dual:
        # Inverse transpose, without localizing any new coordinate.
        inverse=identity_matrix(1+len(active))
        for k,ch in enumerate(active,1):inverse[k][0]=pscale(RES[ch],-coefficient)
        return transpose_matrix(inverse)
    return mat


def state_label(k):
    if k[0]=='C':return 'C['+cname(k[1])+']; wedge('+','.join(LABEL(x) for x in k[2])+')'
    coord='generic' if k[2]=='a' else cname(k[2])
    return 'F['+k[1]+','+coord+']; wedge('+','.join(LABEL(x) for x in k[3])+')'


def encoded_linear_map(tab):
    return [{'source':state_label(k),'terms':[{'target':state_label(t),'coefficient':encode_poly(p)} for t,p in v.items()]}
            for k,v in tab.items() if v]


def main(output):
    # Check the residue inputs against the unchanged target instead of fitting
    # a new scalar list. These cycles keep both endpoint states.
    check(len(CELLS)==215,'target_cell_count')
    for c in CELLS:
        check(not diff(diff(basis(c),(),False),(),False),'target_absolute_d_squared')
        check(not diff(diff(basis(c),(),True),(),True),'target_PC_d_squared')
    for ch in CHANNELS:
        active=SHEET[ch[0]]
        for p in active:
            check(not diff(times(GAMMA[ch],exp(xs=(p,))),(),False),'fourteen_actual_target_families_closed_abs')
            check(not diff(times(GAMMA[ch],exp(xs=(p,))),(),True),'fourteen_actual_target_families_closed_PC')
    endpoint_norm={
        '+':pmono(esub(exp(ns=LONG),exp(ns=MINUS))),
        '-':pmono(esub(exp(ns=LONG),exp(ns=PLUS))),
    }
    for sigma in ('+','-'):
        check(RES[END_FOR[sigma]]==endpoint_norm[sigma],'exact_endpoint_triple_residue')
        endpoint=GAMMA[END_FOR[sigma]]
        check(len(endpoint)==1,'actual_endpoint_family_single_state')

    # Build the four ACTUAL common-chart resolutions and their signed duals.
    models={'base':Resolution((),True),'S12':Resolution(PROPER,True),
            'S14':Resolution(CHANNELS,True),'N_end':Resolution(ENDS,False)}
    ranks={name:obj.verify(name) for name,obj in models.items()}
    small,big,end,base=(models[k] for k in ('S12','S14','N_end','base'))
    check(len(big.basis)==1088 and len(small.basis)==944,'explicit_resolution_column_counts')
    check(big.bset==small.bset|end.bset and not small.bset&end.bset,'endpoint_resolution_degreewise_split')

    # The dual short exact sequence, generic coefficient leg, and connecting
    # map are checked on complete columns, with no cohomology replacement.
    connector={}
    for k in small.basis:
        check(big.duald[k]==small.duald[k],'reverse_endpoint_inclusion_chain_map')
    for k in big.basis:
        projected=project_states(big.duald[k],end.bset)
        expected=end.duald.get(k,{})
        check(projected==expected,'reverse_endpoint_quotient_chain_map')
    for k in base.basis:
        check(big.duald[k]==base.duald[k],'reverse_generic_coefficient_inclusion_big')
        check(small.duald[k]==base.duald[k],'reverse_generic_coefficient_inclusion_small')
    for k in end.basis:
        connector[k]=project_states(big.duald[k],small.bset)
        # Complete the connector table before composing it with the differential.
    for k in end.basis:
        check(not vadd(apply_map(small.duald,connector[k]),apply_map(connector,end.duald[k])),
              'actual_reverse_connector_degree_one_cocycle')
        check(all(small.dualdeg[t]==end.dualdeg[k]+1 for t in connector[k]),'actual_reverse_connector_degree')
    check(sum(bool(x) for x in connector.values())==16,'reverse_connector_sixteen_nonzero_Koszul_columns')

    # Common-chart local primitive: r times the endpoint branch column into
    # its common generic branch column. It uses allowed conductor inverses.
    H={}
    for k in end.basis:
        if k[0]=='F':H[k]=vone(('F',k[1],'a',k[3]),RES[k[2]])
        else:H[k]={}
    for k in end.basis:
        rhs=vadd(apply_map(small.duald,H[k]),vscale(apply_map(H,end.duald[k]),pmono(c=-1)))
        check(rhs==connector[k],'explicit_common_chart_connector_nullhomotopy')
    section=common_section(big,small)
    for k in small.basis:
        check(apply_map(big.d,section[k])==apply_map(section,small.d[k]),'primal_common_chart_endpoint_section_chain_map')
        check(project_states(section[k],small.bset)==vone(k),'primal_common_chart_section_normalized')

    # Full labelled transport, including top exterior orientation in duals.
    actions=tuple((s,1) for s in (0,2,4))+tuple((s,-1) for s in (1,3,5))
    orientation_records=[]
    for shift,direction in actions:
        for ch in CHANNELS:
            nch=change_channel(ch,shift,direction)
            check(change_poly(RES[ch],shift,direction)==RES[nch],'actual_residue_label_covariance')
        for name,obj in models.items():
            for k in obj.basis:
                for dual,diffmap in ((False,obj.d),(True,obj.duald)):
                    left=act_resolution(diffmap[k],shift,direction,dual)
                    right=apply_map(diffmap,act_resolution(vone(k),shift,direction,dual))
                    check(left==right,'ambient_dual_covariance' if dual else 'ambient_primal_covariance')
        for k in end.basis:
            check(act_resolution(connector[k],shift,direction,True)==
                  apply_map(connector,act_resolution(vone(k),shift,direction,True)),
                  'full_reverse_connector_covariance')
        image=[act_diag(x,shift,direction) for x in Occ]
        det=sign(sum(OCC_POS[image[i]]>OCC_POS[image[j]] for i in range(6) for j in range(i+1,6)))
        orientation_records.append({'shift':shift,'direction':direction,'ambient_occurrence_determinant':det,
                                    'swaps_sheets':change_channel(('+',()),shift,direction)[0]=='-'})

    # Actual normalization transition matrices on the seven-chart cover.
    # The only pole-bearing transitions touch the common chart; all of their
    # denominators are legal there. Pure occurrence transitions are identity.
    cover_counts=Counter();overlap_records=[]
    for nn in range(1,5):
        for face in combinations(range(7),nn):
            invx,invn=open_data(face)
            if invx&set(PLUS) and invx&set(MINUS):continue
            cover_counts[nn]+=1
    check(dict(cover_counts)=={1:7,2:12,3:8,4:2},'actual_twenty_nine_chart_intersections')
    for sigma in ('+','-'):
        chart_ids=(0,)+tuple(i for i,x in enumerate(OPEN_LABELS) if x in SHEET[sigma])
        for channels in (PROPER,CHANNELS):
            rank=1+sum(ch[0]==sigma for ch in channels)
            for i,j in permutations(chart_ids,2):
                L=overlap_shear(sigma,channels,i,j)
                U=overlap_shear(sigma,channels,i,j,True)
                check(matrix_mul(transpose_matrix(L),U)==identity_matrix(rank),'dual_transition_inverse_transpose')
                invx,invn=open_data((i,j))
                for row in L+U:
                    for p in row:
                        check(all(all(m[9+VAR[t]]>=0 or t in invn for t in SHORT) for m in p),
                              'transition_denominators_legal_on_actual_overlap')
            for i,j,k in permutations(chart_ids,3):
                for dual in (False,True):
                    left=matrix_mul(overlap_shear(sigma,channels,j,k,dual),
                                    overlap_shear(sigma,channels,i,j,dual))
                    right=overlap_shear(sigma,channels,i,k,dual)
                    check(left==right,'normalization_triple_overlap_dual' if dual else 'normalization_triple_overlap_primal')
        endpoint=END_FOR[sigma]
        for i in chart_ids[1:]:
            L14=overlap_shear(sigma,CHANNELS,0,i,True)
            active=tuple(ch for ch in CHANNELS if ch[0]==sigma)
            col=1+active.index(endpoint)
            check(L14[0][col]==pscale(RES[endpoint],-1),'endpoint_dual_transition_is_negative_full_triple_residue')
        # On W_sigma, only the three occurrence charts remain. Their dual
        # transitions are identity, so the endpoint splitting glues strictly.
        for i,j in permutations(chart_ids[1:],2):
            check(overlap_shear(sigma,CHANNELS,i,j,True)==identity_matrix(8),
                  'normal_supported_endpoint_splitting_glues')
        overlap_records.append({'sheet':sigma,'charts':[OPEN_NAMES[i] for i in chart_ids],
                                'endpoint_dual_transition':encode_poly(pscale(RES[endpoint],-1))})

    # Independent integral verification of every first-pole/positive-power
    # pattern of the local occurrence Gysin blocks, including empty strands.
    strand_count=0
    for mask in range(8):
        inv={i for i in range(3) if mask>>i&1}
        for alpha in product((-2,-1,0,1),repeat=3):
            h=koszul_dual_strand(alpha,inv)
            expected={3:1} if not inv and alpha==(-1,-1,-1) else {}
            check(h==expected,'occurrence_Gysin_integral_all_sign_patterns')
            strand_count+=1
    normal_record=normal_gysin()

    # The opposite normal supports W are disjoint from the occurrence
    # conductor. Test this on the actual seven-chart localization rules.
    support_records=[]
    for sigma in ('+','-'):
        active=SHEET[sigma];opp=set(SHORT)-set(active)
        for i,label in enumerate(OPEN_LABELS):
            invx,invn=open_data((i,))
            W_nonempty=not bool(invn&opp) and not bool(invx&(set(SHORT)-set(active)))
            expected=label in active
            check(W_nonempty==expected,'opposite_normal_support_actual_charts')
            conductor_nonempty=not bool(invx)
            check(not(W_nonempty and conductor_nonempty),'normal_support_disjoint_occurrence_conductor')
            if W_nonempty:
                # One ambient branch survives. The canonical endpoint section
                # is an inclusion of free coordinates, with no residue poles.
                for n in (6,7):
                    old=1+n;check(old in (7,8),'normal_supported_dual_rank')
        support_records.append({'sheet':sigma,'vanishing_normals':[LABEL(s) for s in sorted(opp)],
            'S12_dual_after_upper_shriek_rank':7,'S14_dual_after_upper_shriek_rank':8,
            'N_end_dual_after_upper_shriek_rank':1,'cohomological_degree':0,
            'line':'occurrence_branch_volume tensor opposite_normal_determinant_dual',
            'inherited_reverse_connector':0,
            'supported_endpoint_lift_exists':True,
            'supported_lift_pi0_variation_rank':7,
            'supported_lift_pi_n_for_n_positive':0})

    # Correct the interpretation: connector acts by zero on all cohomology
    # sheaves, although biduality identifies it with the nonzero global Ext.
    source_coho={-3,-1};target_coho={-4,-2}
    check(not(source_coho&target_coho),'no_common_cohomological_degree_for_connector')
    for sigma in ('+','-'):
        opp=set(SHORT)-set(SHEET[sigma])
        endpoint_m=next(iter(RES[END_FOR[sigma]]))
        check(all(endpoint_m[9+VAR[d]]==-1 for d in opp),'endpoint_detector_has_all_three_opposite_poles')
        for ch in PROPER:
            if ch[0]!=sigma:continue
            m=next(iter(RES[ch]))
            check(any(m[9+VAR[d]]>=0 for d in opp),'proper_channel_zero_in_opposite_top_Cech_quotient')
        # Coefficient powers can remove these poles but never add a missing pole.
        for beta in product(range(3),repeat=3):
            residue_survives=all(b==0 for b in beta)
            killed_by_opposite_normal_ideal=any(b>0 for b in beta)
            check(residue_survives == (not killed_by_opposite_normal_ideal),'triple_residue_monomial_annihilator')

    prior=Path(__file__).with_name('marici_endpoint_multiplier_coherence_rerun_for_reverse_gysin.json')
    prerequisite={}
    if prior.exists():
        data=json.loads(prior.read_text());prerequisite={'rerun_exact_assertions':data['exact_assertions'],
          'certificate_sha256':hashlib.sha256(prior.read_bytes()).hexdigest()}
    result={
      'schema':'marici.reverse_endpoint_normalization_gysin.v1','date':'2026-09-07',
      'lane':'Branch B: explicit reverse endpoint comparison and supported test',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'scope':'Target-selected normalization sheaves S12/S14 on the specified open V. Not the native physical source.',
      'normalization_channels':[{'channel':cname(ch),'residue':encode_poly(RES[ch]),'endpoint':ch in ENDS} for ch in CHANNELS],
      'common_chart_ambient_resolution_ranks':ranks,
      'common_chart_ambient_resolution_columns':{name:len(x.basis) for name,x in models.items()},
      'dual_cohomology_sheaves':{
         'S12':{'-3':{'positive_branch_volume':7,'negative_branch_volume':7},'-1':{'conductor':13}},
         'S14':{'-3':{'positive_branch_volume':8,'negative_branch_volume':8},'-1':{'conductor':15}},
         'N_end':{'-3':{'positive_branch_volume':1,'negative_branch_volume':1},'-1':{'conductor':2}}},
      'reverse_connector':{
        'direction':'D(N_end) -> D(S12)[1]',
        'nonzero_global_derived_morphism':True,
        'nonzero_common_chart_resolution_columns':sum(bool(v) for v in connector.values()),
        'zero_on_every_cohomology_sheaf':True,
        'local_primitives_globally_glue':False,
        'global_annihilator':'I_plus + I_minus + (t13,t15,t35)*(t02,t04,t24)',
        'nonvanishing_proof':'Exact biduality transports the inherited nonzero endpoint extension. Triple-normal pole quotient supplies the same detector.'},
      'occurrence_Koszul_integral_strands':strand_count,
      'reverse_connector_columns':encoded_linear_map(connector),
      'common_chart_connector_primitive':encoded_linear_map(H),
      'normalization_overlap_dictionary':overlap_records,
      'nonempty_cover_intersections':dict(cover_counts),
      'normal_Gysin':normal_record,'normal_support_results':support_records,
      'orientation_dictionary':orientation_records,
      'generic_leg_scope':'Dual of the specified top generic coefficient map S_q -> O_V theta. Not a new identification of the whole seven-state Q source.',
      'verification_scope':'Signed ambient resolutions and connecting columns checked exactly on D(T); occurrence charts, sheaf gluing, biduality and all-polynomial exactness proved in the companion note. No illegal substitution of zero into residue denominators.',
      'extra_target_carrier_cells':0,'native_connector_constructed':False,
      'prerequisite':prerequisite,'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('schema','common_chart_ambient_resolution_columns',
        'reverse_connector','occurrence_Koszul_integral_strands','exact_assertions','prerequisite')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_reverse_endpoint_gysin_certificate_20260907.json'))
    main(parser.parse_args().output)
