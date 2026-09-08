#!/usr/bin/env python3
"""Endpoint multiplier syzygies and the unchanged endpoint extension class.

Helper model retained from the preceding exact target-side descent checker.

Standard-library Python 3.10+. No external services or repository writes.
Rebuilds all 215 target cells, the seven unit lifts on actual principal opens,
their overlap cocycle, twelve residue coordinates, and integral fine-graded
Cech cohomology. See the companion proof for the all-polynomial conclusions.
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



# ---------------------------------------------------------------------------
# New calculation. The target routines above are copied from the checked
# predecessor to make this file self-contained; its main() is not included.
# ---------------------------------------------------------------------------
A_LABELS=tuple(sorted(PLUS))
B_LABELS=tuple(sorted(MINUS))
NORMAL_ORDER=A_LABELS+B_LABELS
NVAR={s:i for i,s in enumerate(NORMAL_ORDER)}
N0=(0,)*6
GENERIC=('generic',())

def nmono(labels):
    return tuple(sum(s==t for s in labels) for t in NORMAL_ORDER)

def nadd(a,b): return tuple(x+y for x,y in zip(a,b))

def nsparse_add(*terms):
    out={}
    for v in terms:
        for k,n in v.items():
            out[k]=out.get(k,0)+n
            if out[k]==0: del out[k]
    return out

# A sparse polynomial vector is keyed by (basis object, exponent).
def pscale(v,e=N0,c=1):
    return {(b,nadd(m,e)):n*c for (b,m),n in v.items() if n*c}

def papply(table,v):
    ans={}
    for (b,m),n in v.items(): ans=nsparse_add(ans,pscale(table[b],m,n))
    return ans


def ideal_resolution():
    """Tensor the truncated, augmented Koszul resolutions of the two ideals.

    Homological degree of (A,B) is |A|+|B|-2. Both subsets are nonempty.
    Every coefficient is one labelled normal variable with its Koszul sign.
    """
    bases=[[] for _ in range(5)]
    differential={}
    for aa in subsets(A_LABELS):
        if not aa: continue
        for bb in subsets(B_LABELS):
            if not bb: continue
            g=(aa,bb); bases[len(aa)+len(bb)-2].append(g)
            out={}
            if len(aa)>1:
                for k,a in enumerate(aa):
                    dest=(aa[:k]+aa[k+1:],bb)
                    out[(dest,nmono((a,)))]=sign(k)
            if len(bb)>1:
                for k,b in enumerate(bb):
                    dest=(aa,bb[:k]+bb[k+1:])
                    out[(dest,nmono((b,)))]=sign(len(aa)-1+k)
            differential[g]=out
    augmentation={g:{(('scalar',),nmono(g[0]+g[1])):1} for g in bases[0]}
    return bases,differential,augmentation


def shift_basis(g): return nmono(g[0]+g[1])


def int_rank(matrix,ncols):
    """Exact integer unit-pivot reduction, certifying saturated image."""
    a=[r[:] for r in matrix]; k=0; rows=len(a)
    while k<min(rows,ncols):
        pivot=next(((i,j) for i in range(k,rows) for j in range(k,ncols)
                    if abs(a[i][j])==1),None)
        if pivot is None: break
        i,j=pivot; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-v for v in a[k]]
        for i in range(k+1,rows):
            x=a[i][k]
            if x: a[i]=[v-x*w for v,w in zip(a[i],a[k])]
        for j in range(k+1,ncols):
            x=a[k][j]
            if x:
                for i in range(rows): a[i][j]-=x*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,rows) for j in range(k,ncols)),
          'new_all_nonzero_integer_Smith_factors_are_one')
    return k


def dual_strand(bases,dd,alpha,inverted):
    active=[]
    for bb in bases:
        active.append([g for g in bb if all(i in inverted or alpha[i]+shift_basis(g)[i]>=0
                                          for i in range(6))])
    ranks=[]
    for q in range(4):
        columns={g:j for j,g in enumerate(active[q])}
        mat=[]
        for target in active[q+1]:
            row=[0]*len(columns)
            for (source,mon),c in dd[target].items():
                if source in columns: row[columns[source]]+=sign(q+1)*c
            mat.append(row)
        ranks.append(int_rank(mat,len(columns)))
    h={}
    for q,bb in enumerate(active):
        n=len(bb)-(ranks[q-1] if q else 0)-(ranks[q] if q<4 else 0)
        check(n>=0,'dual_strand_nonnegative_cohomology')
        if n:h[q]=n
    return h


def expected_dual(alpha,inverted):
    out={}
    if all(i in inverted or alpha[i]>=0 for i in range(6)):out[0]=1
    for block in (set(range(3)),set(range(3,6))):
        if not(block&inverted) and all(alpha[i]==-1 for i in block) and all(
                i in inverted or alpha[i]>=0 for i in set(range(6))-block):
            out[2]=out.get(2,0)+1
    if not inverted and alpha==(-1,)*6:out[4]=1
    return out


def ideal_strand(bases,dd,alpha):
    active=[[g for g in bb if all(x>=s for x,s in zip(alpha,shift_basis(g)))]
            for bb in bases]
    ranks=[]
    for q in range(1,5):
        ri={g:i for i,g in enumerate(active[q-1])}
        mat=[[0]*len(active[q]) for _ in ri]
        for j,g in enumerate(active[q]):
            for (target,mon),n in dd[g].items():
                check(target in ri,'ideal_strand_differential_stays_in_strand')
                mat[ri[target]][j]+=n
        ranks.append(int_rank(mat,len(active[q])))
    h={}
    for q,bb in enumerate(active):
        val=len(bb)-(ranks[q-1] if q else 0)-(ranks[q] if q<4 else 0)
        check(val>=0,'ideal_strand_nonnegative_homology')
        if val:h[q]=val
    pred={0:1} if any(alpha[:3]) and any(alpha[3:]) else {}
    check(h==pred,'all_ideal_resolution_strands_exact_above_zero',(alpha,h))
    return h


def mapadd(*vs): return plus(*vs)

def mapscale(v,m=ZERO,c=1):
    return {(out,inp,eadd(e,m)):n*c for (out,inp,e),n in v.items() if n*c}

def evalmap(v,inp,coefficient=ZERO):
    out={}
    for (a,b,e),n in v.items():
        if b==inp:out=plus(out,{(a,eadd(e,coefficient)):n})
    return out


def encode_map(v):
    def channel(k):
        return k[0]+(':'+','.join(LABEL(s) for s in k[1]) if k[1] else '')
    return [{'output':channel(out),'input':channel(inp),'coefficient':n,
             'monomial':{NAMES[i]:e for i,e in enumerate(mon) if e}}
            for (out,inp,mon),n in sorted(v.items())]


def main(output):
    bases,dd,aug=ideal_resolution()
    check([len(b) for b in bases]==[9,18,15,6,1],'normal_product_ideal_Betti_numbers')
    for q in range(1,5):
        for g in bases[q]:
            if q==1:val=papply(aug,dd[g])
            else:val=papply(dd,dd[g])
            check(not val,'full_polynomial_resolution_d_squared',g)
    # Complete possible monomial incidence patterns, plus repetitions as a
    # check that coefficients are not reduced modulo powers.
    ideal_cases=0
    for alpha in product((0,1,2),repeat=6):
        ideal_strand(bases,dd,alpha);ideal_cases+=1
    dual_cases=0
    dual_examples=[]
    for inv_tuple in subsets(range(6)):
        inverted=set(inv_tuple)
        for alpha in product((-1,0),repeat=6):
            h=dual_strand(bases,dd,alpha,inverted)
            check(h==expected_dual(alpha,inverted),'complete_dual_localization_sign_patterns',(alpha,inv_tuple,h))
            dual_cases+=1
            if not inverted and alpha in ((-1,)*3+(0,)*3,(0,)*3+(-1,)*3,(-1,)*6,(0,)*6):
                dual_examples.append({'normal_degree':alpha,'cohomology':h})
    # A coordinate with exponent below -1 gives no basis unless it was
    # explicitly inverted. This verifies the extra possible inequality case.
    for i in range(6):
        alpha=[0]*6;alpha[i]=-2
        for inv in (set(),{i},set(range(6))):
            h=dual_strand(bases,dd,tuple(alpha),inv)
            check(h==expected_dual(tuple(alpha),inv),'dual_exponents_below_first_pole')

    # Rebuild all fourteen actual coefficient chains and residue values.
    channels=[];proper=[];end=[]; G={}; residue={};active_of={}
    for active,polarity in ((PLUS,'+'),(MINUS,'-')):
        for nn in subsets(set(SHORT)-set(active)):
            if not nn:continue
            key=(polarity,nn);v,ac,lc=gamma_full(active,nn)
            channels.append(key);G[key]=v;active_of[key]=active
            residue[key]=esub(exp(ns=set(LONG)-lc),exp(ns=set(nn)|ac))
            (end if len(nn)==3 else proper).append(key)
    endpoint={k[0]:k for k in end}
    inputs=[GENERIC]+proper
    check((len(proper),len(end),len(CELLS))==(12,2,215),'original_target_and_source_coordinate_counts')
    for pc in (False,True):
        for c in CELLS:
            check(not diff(diff(basis(c),(0,),pc),(0,),pc),'retained_target_d_squared')
    for key in channels:
        check(not Q(G[key]),'residue_families_have_zero_generic_projection')
        for s in active_of[key]:
            chart=OPEN_LABELS.index(s)
            for pc in (False,True):
                check(not diff(G[key],(chart,),pc),'actual_full_boundary_families_closed')

    F={}
    for p in A_LABELS:
        for m in B_LABELS:
            g=((p,),(m,)); coeff=exp(ns=(p,m))
            value={(k,k,coeff):1 for k in inputs}
            kp=('+',tuple(s for s in B_LABELS if s!=m))
            km=('-',tuple(s for s in A_LABELS if s!=p))
            cp=esub(eadd(coeff,residue[endpoint['+']]),residue[kp])
            cm=esub(eadd(coeff,residue[endpoint['-']]),residue[km])
            check(all(e>=0 for e in cp+cm),'nine_lifts_use_polynomial_coefficients')
            value[(endpoint['+'],kp,cp)]=1
            value[(endpoint['-'],km,cm)]=1
            F[g]=value
            check(eadd(cp,residue[kp])==eadd(coeff,residue[endpoint['+']]),'nine_lifts_positive_conductor_identity')
            check(eadd(cm,residue[km])==eadd(coeff,residue[endpoint['-']]),'nine_lifts_negative_conductor_identity')

    def normal18(mon):
        result=[0]*18
        for s,n in zip(NORMAL_ORDER,mon):result[9+VAR[s]]=n
        return tuple(result)

    defects={};records=[]
    for g in bases[1]:
        value={}
        for (target,mon),n in dd[g].items():
            value=mapadd(value,mapscale(F[target],normal18(mon),n))
        defects[g]=value
        check(bool(value),'each_of_eighteen_relation_defects_is_nonzero',g)
        check(len(value)==2,'each_relation_defect_has_two_endpoint_terms',g)
        check(all(out in end for out,inp,e in value),'relation_defect_lies_entirely_at_actual_endpoints',g)
        outputs={out for out,inp,e in value}
        check(len(outputs)==1,'each_relation_defect_has_one_polarity')
        check(all(inp in proper for out,inp,e in value),'relation_defects_depend_on_retained_boundary_coordinates')
        # All conductor values cancel, hence these are genuine ideal-valued
        # endpoint maps on the normalization-pullback source.
        conductor={}
        for (out,inp,mon),n in value.items():
            conductor=plus(conductor,{(out,eadd(mon,residue[inp])):n})
        check(not conductor,'all_relation_defects_vanish_on_the_conductor')
        for (out,inp,mon),n in value.items():
            active=active_of[out]
            check(active==active_of[inp],'no_cross_polarity_ideal_map_used')
            chart=OPEN_LABELS.index(sorted(active)[0])
            for pc in (False,True):
                chain=restrict(times(G[out],mon,n),(chart,),pc)
                check(bool(chain),'explicit_nonzero_relation_defect_witness')
                check(not diff(chain,(chart,),pc),'defect_witness_is_actual_target_cycle')
                check(not Q(chain),'defect_witness_does_not_change_Q')
                check(chain==endpoint_part(chain),'defect_witness_keeps_endpoint_cube')
            # On the common chart a positive occurrence gives a valid
            # normalization-kernel input instead of the unit used off conductor.
            for s in active:
                chain=restrict(times(G[out],eadd(mon,exp(xs=(s,))),n),(0,))
                check(bool(chain) and not diff(chain,(0,)),'common_chart_ideal_valued_defect_witness')
        records.append({'plus_subset':[LABEL(s) for s in g[0]],
                        'minus_subset':[LABEL(s) for s in g[1]],
                        'endpoint_map':encode_map(value)})
    for g in bases[2]:
        value={}
        for (target,mon),n in dd[g].items():
            value=mapadd(value,mapscale(defects[target],normal18(mon),n))
        check(not value,'all_fifteen_second_syzygies_of_endpoint_defects',g)

    # All labelled D3 transports act on both the source channels and endpoints.
    def channel_action(k,shift,direction):
        if k==GENERIC:return GENERIC
        active=frozenset(act_diag(s,shift,direction) for s in active_of[k])
        return ('+' if active==PLUS else '-',tuple(sorted(act_diag(s,shift,direction) for s in k[1])))
    def action_map(v,shift,direction):
        return {(channel_action(a,shift,direction),channel_action(b,shift,direction),
                 act_mono(mon,shift,direction)):n for (a,b,mon),n in v.items()}
    def action_generator(g,shift,direction):
        aa=tuple(act_diag(s,shift,direction) for s in g[0]);bb=tuple(act_diag(s,shift,direction) for s in g[1])
        sn=permutation_sign(aa)*permutation_sign(bb)
        aa=tuple(sorted(aa));bb=tuple(sorted(bb))
        if set(aa)<=set(B_LABELS):
            sn*=sign((len(aa)-1)*(len(bb)-1));aa,bb=bb,aa
        return (aa,bb),sn
    for shift,direction in [(a,1) for a in (0,2,4)]+[(a,-1) for a in (1,3,5)]:
        for g in bases[0]:
            gg,sn=action_generator(g,shift,direction)
            check(sn==1,'degree_zero_normal_product_transport_no_unprescribed_sign')
            check(action_map(F[g],shift,direction)==F[gg],'all_nine_lifts_D3_covariance')
        for g in bases[1]:
            gg,sn=action_generator(g,shift,direction)
            check(action_map(defects[g],shift,direction)==mapscale(defects[gg],ZERO,sn),
                  'eighteen_defects_D3_covariance_with_Koszul_orientation')
        for q in range(1,5):
            for g in bases[q]:
                gg,sn=action_generator(g,shift,direction)
                lhs={}
                for (source,mon),n in dd[g].items():
                    source_g,s=action_generator(source,shift,direction)
                    mon_g=[0]*6
                    for d,e in zip(NORMAL_ORDER,mon):mon_g[NVAR[act_diag(d,shift,direction)]]=e
                    lhs=nsparse_add(lhs,{(source_g,tuple(mon_g)):n*s})
                rhs=pscale(dd[gg],N0,sn)
                check(lhs==rhs,'whole_resolution_D3_chain_covariance')

    # Geometry of the ORIGINAL seven-chart open. K=(a)(b) is the unit ideal
    # on the common chart; on a positive occurrence chart K=(b), and vice versa.
    # These are exact monomial-ideal reductions, not set-theoretic substitutions.
    chart_types=[]
    for i,s in enumerate(OPEN_LABELS):
        invx,invn=open_data((i,))
        surviving=[tuple(t for t in (p,m) if t not in invn) for p in A_LABELS for m in B_LABELS]
        minimal={tuple(sorted(ss)) for ss in surviving}
        minimal={ss for ss in minimal if not any(set(tt)<set(ss) for tt in minimal)}
        predicted={()} if i==0 else {(t,) for t in (B_LABELS if s in PLUS else A_LABELS)}
        check(minimal==predicted,'annihilator_product_ideal_on_actual_source_chart')
        # Full global annihilator I+ + I- + K is unit on every chart of V.
        full_ann_has_unit=(() in minimal) or bool(invx)
        check(full_ann_has_unit,'cyclic_Ext_module_support_does_not_meet_V')
        chart_types.append({'chart':OPEN_NAMES[i],
                            'normal_product_ideal_generators':[[LABEL(t) for t in ss] for ss in sorted(minimal)],
                            'codimension':0 if i==0 else 3})

    # Explicit regular-sequence dual calculation on each occurrence chart:
    # it is the truncated three-variable Koszul dual, H0=O and H2=O/(b).
    # All choices of remaining inverted normals are covered by the complete
    # localization strand checks above. The full six-normal intersection is
    # absent from V; its affine H4 class dies on each actual chart.
    for chart in chart_types:
        i=OPEN_NAMES.index(chart['chart']); invn=open_data((i,))[1]
        inv={NVAR[t] for t in invn}
        h=dual_strand(bases,dd,(-1,)*6,inv)
        check(4 not in h,'affine_degree_four_conductor_class_absent_on_every_V_chart')
        for alpha in product((-1,0),repeat=6):
            h=dual_strand(bases,dd,alpha,inv)
            check(set(h)<={0,2},'actual_chart_Hom_of_ideal_has_only_degrees_zero_and_two')
            check(1 not in h,'actual_chart_Ext1_of_ideal_is_zero')

    pred=Path(__file__).with_name('check_marici_normalization_endpoint_extension_20260907.py')
    rerun=Path(__file__).with_name('endpoint_input_rerun_certificate.json')
    prior_info={}
    if pred.exists():prior_info['checker_sha256']=hashlib.sha256(pred.read_bytes()).hexdigest()
    if rerun.exists():
        rr=json.loads(rerun.read_text());prior_info['independently_rerun_assertions']=rr['exact_assertions']
        prior_info['rerun_certificate_sha256']=hashlib.sha256(rerun.read_bytes()).hexdigest()
    result={
      'schema':'marici.endpoint_multiplier_coherence.v1',
      'date':'2026-09-07','lane':'Branch B: coefficient descent and endpoint relations',
      'source_scope':'The explicit target-selected S12 and S14 normalization sheaves on V; not a native physical source identification.',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'normal_order':[LABEL(s) for s in NORMAL_ORDER],
      'ideal':'K=(t13,t15,t35)*(t02,t04,t24)',
      'ideal_resolution_ranks':[len(b) for b in bases],
      'quotient_resolution_ranks':[1]+[len(b) for b in bases],
      'ideal_integral_strands_checked':ideal_cases,
      'dual_integral_strands_checked':dual_cases,
      'affine_dual_homology_examples':dual_examples,
      'nine_endpoint_lift_maps':[{'p':LABEL(g[0][0]),'m':LABEL(g[1][0]),'map':encode_map(F[g])} for g in bases[0]],
      'eighteen_relation_defects':records,
      'source_chart_ideal_types':chart_types,
      'proved_low_degree_adjoint_result':{
        'Hom':'Hom(K tensor S12,S14) = Hom(S12,S14), naturally by multiplication',
        'Ext1':'Ext1(S12,N_end) -> Ext1(K derived_tensor S12,N_end) is an isomorphism',
        'endpoint_class':'the pulled-back class is the original nonzero endpoint class under this isomorphism',
        'collective_lift_exists':False,
        'all_positive_ideal_powers':'same Hom and Ext1 conclusion, by the regular-sequence grade proof',
        'remaining_derived_dual':'H0=N_end, H2=two opposite triple-normal supported lines with determinant duals; no other sheaf cohomology on V',
      },
      'annihilator':'I_plus + I_minus + K',
      'new_independent_Ext_class_claimed':False,
      'native_source_or_spatial_endpoint_connectors_constructed':False,
      'extra_target_cells_added':False,
      'proof_scope':'Unit-pivot computations test all finite incidence patterns. Arbitrary exponents, global Ext injectivity/isomorphism, and all ideal powers are proved in the companion note rather than inferred from test counts.',
      'prerequisite':prior_info,
      'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('schema','ideal_resolution_ranks','ideal_integral_strands_checked',
          'dual_integral_strands_checked','exact_assertions','prerequisite')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_endpoint_multiplier_coherence_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
