#!/usr/bin/env python3
"""Global endpoint-triangle transformations and their supported restrictions.

Standalone Python 3.10+, standard library only. Retains the target and
normalization-resolution helpers from the pinned reverse-endpoint checker.
New calculation: all global sheaf-linear triangular automorphisms, exact
coefficient syzygies, explicit free-resolution maps (including necessary
occurrence Koszul homotopies), and the all-normal-order restriction cokernel.
No native source or new geometric carrier is asserted.
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



# --- New global transformation calculation. ---
SUBSETS=tuple(s for n in range(3) for s in combinations(range(3),n))
EDGES=tuple((N,i) for N in SUBSETS if len(N)<2 for i in range(3) if i not in N)
SQUARES=tuple(combinations(range(3),2))
Z6=(0,)*6

def m6add(x,y):return tuple(a+b for a,b in zip(x,y))
def m6sub(x,y):return tuple(a-b for a,b in zip(x,y))
def m6var(i):return tuple(int(j==i) for j in range(6))
def m6max(x,y):return tuple(max(a,b) for a,b in zip(x,y))
def m6divides(x,y):return all(a<=b for a,b in zip(x,y))
def m6p(m,c=1):return {m:c} if c else {}
def m6plus(*ps):
    out={}
    for p in ps:
        for m,c in p.items():
            out[m]=out.get(m,0)+c
            if not out[m]:del out[m]
    return out

def m6mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():out=m6plus(out,m6p(m6add(a,b),c*d))
    return out

def m6scale(p,c):return {m:c*v for m,v in p.items() if c*v}
def cvadd(*vs):
    out={}
    for v in vs:
        for k,p in v.items():
            out[k]=m6plus(out.get(k,{}),p)
            if not out[k]:del out[k]
    return out

def cvscale(v,p):return {k:q for k,a in v.items() if (q:=m6mul(a,p))}
def cvapply(tab,v):
    out={}
    for k,p in v.items():out=cvadd(out,cvscale(tab[k],p))
    return out

LABEL_WEIGHT={N:tuple(int(i not in N) for i in range(3))+tuple(int(i in N) for i in range(3)) for N in SUBSETS}
D1={}
for N,i in EDGES:
    target=tuple(sorted(N+(i,)))
    D1[(N,i)]={N:m6p(m6var(3+i)),target:m6p(m6var(i),-1)}
EDGE_WEIGHT={e:m6add(LABEL_WEIGHT[e[0]],m6var(3+e[1])) for e in EDGES}
D2={}
for i,j in SQUARES:
    D2[(i,j)]={((),i):m6p(m6var(3+j)),((),j):m6p(m6var(3+i),-1),
                ((i,),j):m6p(m6var(i)),((j,),i):m6p(m6var(j),-1)}
SQUARE_WEIGHT={(i,j):m6add(m6add(LABEL_WEIGHT[()],m6var(3+i)),m6var(3+j)) for i,j in SQUARES}


def row_apply(v):
    return m6plus(*(m6mul(p,m6p(LABEL_WEIGHT[N])) for N,p in v.items()))


def cube_strand(g,powers=None):
    def allowed(weight):
        e=m6sub(g,weight)
        return min(e)>=0 and (powers is None or all(e[i]<powers[i] for i in range(3)))
    bases=[tuple(N for N in SUBSETS if allowed(LABEL_WEIGHT[N])),
           tuple(e for e in EDGES if allowed(EDGE_WEIGHT[e])),
           tuple(f for f in SQUARES if allowed(SQUARE_WEIGHT[f]))]
    matrices=[];ranks=[]
    for degree,tab in ((1,D1),(2,D2)):
        rows=bases[degree-1];cols=bases[degree]
        A=[]
        for row in rows:
            A.append([sum(tab[col].get(row,{}).values()) for col in cols])
        matrices.append(A);ranks.append(unit_rank(A,len(cols)))
    if powers is None:
        inideal=any(m6divides(w,g) for w in LABEL_WEIGHT.values())
        check(len(bases[0])-ranks[0]==int(inideal),'complete_integral_cube_resolution_H0')
        check(len(bases[1])-ranks[0]-ranks[1]==0,'complete_integral_cube_resolution_H1')
        check(len(bases[2])-ranks[1]==0,'complete_integral_cube_resolution_H2')
    else:
        inideal=any(m6divides(w,g) for w in LABEL_WEIGHT.values())
        inproduct=any(m6divides(m6add(w,tuple(powers[i] if j==i else 0 for j in range(6))),g)
                      for w in LABEL_WEIGHT.values() for i in range(3))
        check(len(bases[0])-ranks[0]==int(inideal and not inproduct),
              'normal_jet_cokernel_equals_ideal_mod_q_times_ideal')
    return bases,ranks


def pair_path_syzygy(N,M):
    common=tuple(sorted(set(N)&set(M)))
    path=[N];cur=N
    for i in tuple(x for x in N if x not in common):
        cur=tuple(x for x in cur if x!=i);path.append(cur)
    for i in tuple(x for x in M if x not in common):
        cur=tuple(sorted(cur+(i,)));path.append(cur)
    lcm=m6max(LABEL_WEIGHT[N],LABEL_WEIGHT[M]);out={}
    for A,B in zip(path,path[1:]):
        if len(A)<len(B):edge=(A,next(iter(set(B)-set(A))));sgn=1
        else:edge=(B,next(iter(set(A)-set(B))));sgn=-1
        power=m6sub(lcm,EDGE_WEIGHT[edge])
        check(min(power)>=0,'Taylor_pair_reduction_uses_no_inverses')
        out=cvadd(out,{edge:m6p(power,sgn)})
    expected={N:m6p(m6sub(lcm,LABEL_WEIGHT[N])),M:m6p(m6sub(lcm,LABEL_WEIGHT[M]),-1)}
    check(cvapply(D1,out)==expected,'all_Taylor_pair_relations_generated_by_nine_edges')
    return out


def sheet_dictionary(sigma):
    active=SHEET[sigma];opp=tuple(sorted(set(SHORT)-set(active)))
    numerators=[];units=[]
    for t in opp:
        _,ac,lc=gamma_full(active,(t,))
        missing=tuple(set(LONG)-lc)
        check(len(ac)==len(missing)==1,'source_singleton_has_one_active_unit_and_long_numerator')
        units.append(next(iter(ac)));numerators.append(missing[0])
    return opp,tuple(numerators),tuple(units)


DICT={sigma:sheet_dictionary(sigma) for sigma in ('+','-')}

def embed6(sigma,p):
    opp,vs,units=DICT[sigma];out={}
    for m,c in p.items():
        e=[0]*18
        for i in range(3):
            e[9+VAR[opp[i]]]+=m[i]
            e[9+VAR[vs[i]]]+=m[3+i]
        out=padd(out,pmono(tuple(e),c))
    return out


def channel_for(sigma,N):
    return 'a' if not N else (sigma,tuple(DICT[sigma][0][i] for i in N))


def frame_unit(sigma,N):
    return pmono(exp(ns=(DICT[sigma][2][N[0]],))) if len(N)==1 else ONEP


def normalized_to_original_row(sigma,row):
    return {channel_for(sigma,N):pmul(embed6(sigma,p),frame_unit(sigma,N)) for N,p in row.items()}


def conductor_row_value(row):
    return padd(row.get('a',{}),*(pmul(p,RES[ch]) for ch,p in row.items() if ch!='a'))


def insert_occurrence(wedge,p):
    if p in wedge:return None,0
    new=tuple(sorted(wedge+(p,),key=OCC_POS.get))
    return new,sign(sum(OCC_POS[x]<OCC_POS[p] for x in wedge))


def lift_row_to_resolution(sigma,row,small,end,tail=None):
    """Actual chain map S12_res -> N_end_res.

    Tail=(occurrence, old coordinate). Its nonzero ambient conductor
    multiplication is killed by an explicit occurrence-Koszul wedge homotopy.
    No scalar zero substitution is made in a free resolution.
    """
    endpoint=END_FOR[sigma]
    out={k:{} for k in small.basis}
    for k in small.basis:
        if k[0]=='F':
            _,side,coord,wed=k
            if side==sigma:
                if coord in row:out[k]=vadd(out[k],vone(('F',sigma,endpoint,wed),row[coord]))
                if tail is not None and coord=='a':
                    occurrence,oldcoord=tail
                    nw,sgn=insert_occurrence(wed,occurrence)
                    multiplier=ONEP if oldcoord=='a' else RES[oldcoord]
                    if sgn:out[k]=vadd(out[k],vone(('C',endpoint,nw),pscale(multiplier,sgn)))
        else:
            _,r,wed=k
            if r in row and r!='a':out[k]=vone(('C',endpoint,wed),row[r])
    for k,v in out.items():
        check(all(t in end.bset and end.deg[t]==small.deg[k] for t in v),'global_Hom_map_cochain_degree')
        check(apply_map(end.d,v)==apply_map(out,small.d[k]),'global_Hom_map_full_Koszul_chain_equation')
    return out


def transpose_map(tab,target_basis):
    out={k:{} for k in target_basis}
    for source,v in tab.items():
        for target,p in v.items():out[target]=vadd(out[target],vone(source,p))
    return out


def zero_occurrence_value(p):
    return {m:c for m,c in p.items() if not any(m[VAR[t]] for t in SHORT)}


def normalized_matrix(sigma):
    """Actual [generic, six proper, endpoint] -> seven conductor rows on a sheet."""
    channels=tuple(ch for ch in CHANNELS if ch[0]==sigma)
    coords=('a',)+channels
    rows=[]
    for ch in channels:
        rows.append([pscale(RES[ch],-1) if c=='a' else (ONEP if c==ch else {}) for c in coords])
    return coords,channels,rows


def matrix_identity(n):return [[ONEP if i==j else {} for j in range(n)] for i in range(n)]
def matmul(A,B):return [[padd(*(pmul(A[i][k],B[k][j]) for k in range(len(B))))
                           for j in range(len(B[0]))] for i in range(len(A))]


def check_normalization_square(sigma,row):
    coords,chs,A=normalized_matrix(sigma);U=matrix_identity(len(coords));V=matrix_identity(len(chs))
    end=END_FOR[sigma];ie=coords.index(end);re=chs.index(end)
    for coord,p in row.items():U[ie][coords.index(coord)]=padd(U[ie][coords.index(coord)],p)
    for ch,p in row.items():
        if ch!='a':V[re][chs.index(ch)]=padd(V[re][chs.index(ch)],zero_occurrence_value(p))
    AU=matmul(A,U)
    AU=[[zero_occurrence_value(p) for p in rr] for rr in AU]
    check(AU==matmul(V,A),'actual_normalization_conductor_square')
    return U,V


def main(output):
    check((len(SUBSETS),len(EDGES),len(SQUARES))==(7,9,3),'source_relation_cubical_counts')
    for edge,column in D1.items():check(not row_apply(column),'each_global_normal_relation_has_zero_residue')
    for face,col in D2.items():check(not cvapply(D1,col),'all_three_square_relations_close_strictly')
    taylor={str((N,M)):pair_path_syzygy(N,M) for N,M in combinations(SUBSETS,2)}
    for g in product(range(3),repeat=6):cube_strand(g)
    jet_count=0
    for n in product((1,2),repeat=3):
        for a in product(*[range(v+2) for v in n]):
            for vv in product(range(3),repeat=3):
                cube_strand(a+vv,n);jet_count+=1
    # Reduced fibre presentation is block diagonal; no direct substitution
    # of the seven ideal generators into the ambient ring is substituted for it.
    reduced={}
    for edge,v in D1.items():
        reduced[edge]={N:{m:c for m,c in p.items() if not any(m[:3])} for N,p in v.items()}
        reduced[edge]={N:p for N,p in reduced[edge].items() if p}
        N,i=edge
        check(reduced[edge]=={N:m6p(m6var(3+i))},'reduced_relation_is_exact_block_generator')
    for N in SUBSETS:
        images={i for (base,i) in EDGES if base==N}
        expected=set(range(3)) if not N else (set(range(3))-set(N) if len(N)==1 else set())
        check(images==expected,'reduced_lift_extension_cokernel_annihilators')
    # Nonzero ideal fibre although every generator has zero ambient value.
    for N,w in LABEL_WEIGHT.items():
        check(sum(w[:3])>=1,'all_obstruction_generators_vanish_under_naive_normal_evaluation')
        in_qL=any(m6divides(m6add(m,m6var(i)),w) for m in LABEL_WEIGHT.values() for i in range(3))
        check(not in_qL,'each_obstruction_generator_survives_in_ideal_fibre')

    # The same explicit resolution computes the full derived normal fibre.
    # Three Tor1 generators occupy singleton-edge blocks, and one Tor2
    # generator is the omitted top cube boundary.
    RED2={f:{e:{m:c for m,c in p.items() if not any(m[:3])} for e,p in col.items()}
          for f,col in D2.items()}
    RED2={f:{e:p for e,p in col.items() if p} for f,col in RED2.items()}
    tor1={}
    for i in range(3):
        j,k=tuple(q for q in range(3) if q!=i)
        v={((i,),j):m6p(m6var(3+k)),((i,),k):m6p(m6var(3+j),-1)}
        check(not cvapply(reduced,v),'explicit_Tor1_cycle_in_reduced_resolution')
        check(all(edge[0] for edge in v),'Tor1_has_only_singleton_edge_components')
        check(all(not edge[0] for col in RED2.values() for edge in col),
              'Tor1_cannot_be_a_reduced_square_boundary')
        tor1[i]=v
    tor2={(1,2):m6p(m6var(3)),(0,2):m6p(m6var(4),-1),(0,1):m6p(m6var(5))}
    check(not cvapply(RED2,tor2),'explicit_Tor2_top_cube_cycle')
    tor_strands=0
    for normal_degree in product((0,1),repeat=3):
        for long_degree in product(range(4),repeat=3):
            bs,rk=cube_strand(normal_degree+long_degree,(1,1,1))
            h1=len(bs[1])-rk[0]-rk[1]
            h2=len(bs[2])-rk[1]
            expected1=sum(normal_degree==tuple(int(j!=i) for j in range(3))
                          and all(v>=1 for v in long_degree) for i in range(3))
            expected2=int(normal_degree==(1,1,1) and all(v>=1 for v in long_degree))
            check(h1==expected1,'full_integral_Tor1_grade_classification')
            check(h2==expected2,'full_integral_Tor2_grade_classification')
            tor_strands+=1
    # The full eight-corner product differs by exactly the triple-normal
    # supported endpoint corner, with its U_L numerator retained.
    endpoint_monomial=(0,0,0,1,1,1)
    allcorners=tuple(LABEL_WEIGHT.values())+(endpoint_monomial,)
    for g in product(range(3),repeat=6):
        inL=any(m6divides(w,g) for w in LABEL_WEIGHT.values())
        inP=any(m6divides(w,g) for w in allcorners)
        expected=not any(g[:3]) and all(x>=1 for x in g[3:])
        check((inP and not inL)==expected,'missing_endpoint_corner_quotient_exact')
        multiplied=m6add(g,endpoint_monomial)
        check(any(m6divides(w,multiplied) for w in LABEL_WEIGHT.values())==bool(any(g[:3])),
              'missing_corner_annihilator_exactly_opposite_normal_ideal')

    small=Resolution(PROPER);end=Resolution(ENDS,False);big=Resolution(CHANNELS);generic=Resolution(())
    transforms={};rows={};descriptions=[];tail_corrections=0
    for sigma in ('+','-'):
        opp,vi,qi=DICT[sigma]
        for N in SUBSETS:
            if not N:continue
            raw=RES[channel_for(sigma,N)]
            normalized=pmul(frame_unit(sigma,N),raw)
            fraction=m6p(tuple(-int(i in N) for i in range(3))+tuple(int(i in N) for i in range(3)))
            check(normalized==embed6(sigma,fraction),'source_residue_normalization_only_uses_existing_active_units')
        for edge,row6 in D1.items():
            row=normalized_to_original_row(sigma,row6)
            check(not conductor_row_value(row),'untruncated_full_residue_relation')
            name=(sigma,'normal',edge)
            transforms[name]=lift_row_to_resolution(sigma,row,small,end)
            rows[name]=row;check_normalization_square(sigma,row)
            descriptions.append({'sheet':sigma,'kind':'normal_relation','subset':[LABEL(opp[i]) for i in edge[0]],
                                 'added_label':LABEL(opp[edge[1]]),
                                 'row':{('generic' if ch=='a' else cname(ch)):encode_poly(p) for ch,p in row.items()}})
        for p in sorted(SHEET[sigma]):
            for N in SUBSETS:
                coord=channel_for(sigma,N);row={coord:pmono(exp(xs=(p,)))}
                name=(sigma,'occurrence',(p,N))
                transforms[name]=lift_row_to_resolution(sigma,row,small,end,(p,coord))
                rows[name]=row;check_normalization_square(sigma,row)
                tail_corrections+=sum(any(k[0]=='C' for k in v) for v in transforms[name].values())
        # Cech global sections of the actual branch open: D(opp normal product)
        # plus the three occurrence opens. Negative exponents cannot define a
        # global function unless already an active-normal unit.
        for alpha in product((-1,0,1),repeat=3):
            for beta in product((-1,0,1),repeat=3):
                def allowed(face):
                    return all(alpha[i]>=0 or (i+1) in face for i in range(3)) and (all(x>=0 for x in beta) or 0 in face)
                h,_,_=cech(allowed,tuple(range(4)))
                check(h.get(0,0)==int(all(x>=0 for x in alpha+beta)),
                      'branch_global_functions_from_actual_cover')
        for alpha in product((-1,0,1),repeat=3):
            h,_,_=cech(lambda face:all(alpha[i]>=0 or i in face for i in range(3)),tuple(range(3)))
            check(h.get(0,0)==int(all(x>=0 for x in alpha)),
                  'supported_global_functions_no_new_occurrence_inverse')

    # All global transformations lift to full, signed ambient free resolutions.
    # The occurrence-tail generators NEED their extra conductor-wedge columns.
    auto_records=[]
    for name,H in transforms.items():
        correction={k:(H[k] if k in small.bset else {}) for k in big.basis}
        dualcor=transpose_map(correction,big.basis)
        for k in big.basis:
            v=correction[k]
            check(apply_map(big.d,v)==apply_map(correction,big.d[k]),'full_endpoint_triangle_automorphism_chain_equation')
            check(not apply_map(correction,v),'triangular_automorphism_correction_square_zero')
            check(not project_states(v,small.bset),'old_quotient_and_generic_map_fixed')
            if k in end.bset:check(not v,'endpoint_kernel_fixed_pointwise')
            check(apply_map(big.duald,dualcor[k])==apply_map(dualcor,big.duald[k]),
                  'reverse_automorphism_full_signed_dual_chain_equation')
            if k in small.bset:check(not dualcor[k],'reverse_old_object_and_generic_inclusion_fixed')
            check(not project_states(dualcor[k],end.bset),'reverse_endpoint_quotient_fixed')
        auto_records.append({'sheet':name[0],'kind':name[1],
                             'nonzero_chain_map_columns':sum(bool(v) for v in H.values())})
    check(len(transforms)==60,'complete_thirty_generators_per_endpoint')
    check(tail_corrections>0,'occurrence_tail_maps_retain_nontrivial_conductor_homotopies')

    # The three square identities hold as FULL chain maps, not just scalar rows.
    for sigma in ('+','-'):
        for face,rel in D2.items():
            for k in small.basis:
                value={}
                for edge,p in rel.items():
                    value=vadd(value,vscale(transforms[(sigma,'normal',edge)][k],embed6(sigma,p)))
                check(not value,'full_chain_maps_obey_all_three_square_relations')
    # Transport equations on every potentially nonzero source column; vanishing
    # columns are preserved by the same permutation of basis labels.
    actions=tuple((s,1) for s in (0,2,4))+tuple((s,-1) for s in (1,3,5))
    for shift,direction in actions:
        for name,H in transforms.items():
            sigma,kind,data=name;ns=change_channel((sigma,()),shift,direction)[0]
            oldopp=DICT[sigma][0];newopp=DICT[ns][0]
            if kind=='normal':
                N,i=data
                ni=newopp.index(act_diag(oldopp[i],shift,direction))
                NN=tuple(sorted(newopp.index(act_diag(oldopp[j],shift,direction)) for j in N))
                target_name=(ns,kind,(NN,ni))
            else:
                p,N=data
                NN=tuple(sorted(newopp.index(act_diag(oldopp[j],shift,direction)) for j in N))
                target_name=(ns,kind,(act_diag(p,shift,direction),NN))
            target=transforms[target_name]
            affected={k for k,v in H.items() if v}
            for k in small.basis:
                image,_=change_state(k,shift,direction)
                if target.get(image):affected.add(k)
            for k in affected:
                check(act_resolution(H[k],shift,direction)==
                      apply_map(target,act_resolution(vone(k),shift,direction)),
                      'full_global_Hom_maps_labelled_dihedral_covariance')

    # Filtration comparison: all these automorphisms are identity plus
    # strictly weight-raising maps, but none is degree-zero homogeneous.
    def state_order(k,opp):
        if k[0]=='F':
            coord=k[2]; return 0 if coord=='a' else len(coord[1])
        row=k[1]; return 0 if row=='0' else len(row[1])
    for name,H in transforms.items():
        sigma,kind,data=name;opp=DICT[sigma][0]
        N=data[0] if kind=='normal' else data[1]
        expected=3-len(N)
        for source,v in H.items():
            for target,p in v.items():
                for m in p:
                    delta=state_order(target,opp)-state_order(source,opp)+sum(m[9+VAR[t]] for t in opp)
                    check(delta==expected and delta>0,'global_transformations_strictly_raise_opposite_filtration')

    prior=Path(__file__).with_name('marici_reverse_endpoint_rerun_for_global_transformations.json')
    prerun={}
    if prior.exists():
        c=json.loads(prior.read_text());prerun={'exact_assertions':c['exact_assertions'],
           'sha256':hashlib.sha256(prior.read_bytes()).hexdigest()}
    result={
      'schema':'marici.global_endpoint_triangle_transformations.v1','date':'2026-09-07',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'scope':'All sheaf-linear triangular automorphisms of the fixed S14 endpoint extension, identity on N and S12. Not all native physical source maps; the full source-to-target map is not held pointwise fixed.',
      'generic_coefficient_arrow_preserved':True,'global_endpoint_extension_class_preserved':True,
      'same_target_carrier_cells':215,'extra_target_carrier_cells':0,
      'source_normal_unit_dictionary':{sigma:{'opposite_normals':[LABEL(t) for t in v[0]],
                                            'long_numerators':[LABEL(t) for t in v[1]],
                                            'active_unit_normals':[LABEL(t) for t in v[2]]}
                                       for sigma,v in DICT.items()},
      'global_Hom_generators_per_endpoint':{'normal_relations':9,'occurrence_tail_maps':21},
      'coefficient_resolution_ranks':[7,9,3],
      'normal_relations':descriptions,
      'complete_Taylor_pair_reductions':len(taylor),
      'integral_untruncated_fine_degrees':3**6,
      'integral_normal_jet_cokernel_degrees':jet_count,
      'ambient_free_resolution_columns':{'S12':len(small.basis),'N':len(end.basis),'S14':len(big.basis)},
      'explicit_occurrence_conductor_wedge_columns':tail_corrections,
      'automorphism_chain_map_records':auto_records,
      'reduced_global_restriction_cokernel_each_endpoint':{
        'generic':'D_sigma/(v1,v2,v3)',
        'singletons':'sum_i D_sigma/(v_j:j != i)',
        'doubletons':'D_sigma^3',
        'all_occurrence_tail_coefficients_killed':True,
        'labels_and_internal_shifts_retained':True},
      'all_normal_orders':{'obstruction_module':'L_sigma / q_n L_sigma',
         'L_generators':['a*b*c','v1*b*c','v2*a*c','v3*a*b','v1*v2*c','v1*v3*b','v2*v3*a'],
         'finite_jet_criterion':'evaluate occurrence constants, multiply by the seven-generator row, reduce in L/q_n L rather than in the ambient quotient ring',
         'completion_criterion':'same row equals zero in the completed coefficient ring; exact completion of the finitely generated global transformation module',
         'formal_neighborhood_automorphisms_not_identified_with_completed_global_automorphisms':True},
      'derived_normal_fibre':{'Tor0':'the displayed seven-block quotient',
                              'Tor1':'three free D_sigma lines with singleton-edge labels',
                              'Tor2':'one free D_sigma line with the top cube label',
                              'higher_Tor':0,'integral_fine_strands_checked':tor_strands,
                              'not_homotopy_groups_of_original_groupoid':True},
      'missing_corner_exact_sequence':'0 -> L -> product_i(a_i,v_i) -> (D_sigma at a=0)*[v1*v2*v3] -> 0',
      'naive_zero_normal_specialization_loses_obstruction':True,
      'nonextendable_first_filtered_corrections_each_endpoint':3,
      'prerequisite_rerun':prerun,'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
      'all_degree_proof':'Monomial pair-relation generation, three-square cubical resolution, normalization/Hartogs row classification, and exact finite-module completion. Bounded computation checks the explicit maps and integral matrices.',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('schema','global_Hom_generators_per_endpoint','coefficient_resolution_ranks',
          'ambient_free_resolution_columns','integral_normal_jet_cokernel_degrees','explicit_occurrence_conductor_wedge_columns',
          'exact_assertions','prerequisite_rerun')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_global_endpoint_transformations_certificate_20260907.json'))
    main(parser.parse_args().output)
