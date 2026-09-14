#!/usr/bin/env python3
"""Native algebraic variance mate; framed D35 adapter status stays explicit.

Standard library only.  The source is the native normalized endpoint bar
cochain complex, not ambient RHom.  A diagonal Koszul projection and the
relative-module factorization define a map to the native conductor-resolution
Hom with E_beta,k coefficients.  The antipode converts right to left action.

This script does not contain the unmounted physical endpoint/adaptor files.
It verifies the normalized coefficient mate, not a support/line identification
with the eight physical frames.  --output writes deterministic JSON.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json

LABELS=('13','15','35','02','04','24')
SIDES=(tuple(range(3)),tuple(range(3,6)))
ZERO=(0,)*6
COUNTS=Counter()

def ck(ok,name,detail=None):
    if not ok: raise AssertionError((name,detail))
    COUNTS[name]+=1

def pm(n): return -1 if n%2 else 1

def add_to(d,k,v):
    if v:
        d[k]=d.get(k,0)+v
        if not d[k]: del d[k]

def add(a,b,scale=1):
    out=dict(a)
    for k,v in b.items(): add_to(out,k,scale*v)
    return out

def scaled(a,c): return {k:c*v for k,v in a.items() if c*v}

def subsets(xs):
    return tuple(t for n in range(len(xs)+1) for t in combinations(xs,n))

def parity(xs):
    return pm(sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs))))

def flat(w): return tuple(x for b in w for x in b)

def degree(w): return sum(map(len,w))

def normalize(xs):
    out=[];sgn=1;i=0
    while i<len(xs):
        j=i+1
        while j<len(xs) and xs[j]//3==xs[i]//3: j+=1
        b=xs[i:j]
        if len(set(b))!=len(b): return {}
        sgn*=parity(b);out.append(tuple(sorted(b)));i=j
    return {tuple(out):sgn}

def multiply(a,b):
    out={}
    for wa,ca in a.items():
        for wb,cb in b.items():
            for w,c in normalize(flat(wa)+flat(wb)).items(): add_to(out,w,ca*cb*c)
    return out

def bracket(a,b):
    if not a or not b:return {}
    da=degree(next(iter(a)));db=degree(next(iter(b)))
    return add(multiply(a,b),multiply(b,a),-pm(da*db))

@lru_cache(None)
def all_words(n,first=-1):
    if n==0:return ((),)
    out=[]
    for s in (0,1):
        if first>=0 and s!=first:continue
        for b in subsets(SIDES[s]):
            if b and len(b)<=n:
                out.extend((b,)+rest for rest in all_words(n-len(b),1-s))
    return tuple(out)

MIXED=tuple(J for J in subsets(tuple(range(6))) if any(i<3 for i in J) and any(i>=3 for i in J))

@lru_cache(None)
def rel_generator(J):
    root=min(i for i in J if i<3)
    out=normalize((root,))
    for i in reversed(tuple(i for i in J if i!=root)):
        out=bracket(normalize((i,)),out)
    return out

@lru_cache(None)
def rel_words(n):
    if n==0:return ((),)
    return tuple((J,)+rest for J in MIXED if len(J)<=n for rest in rel_words(n-len(J)))

@lru_cache(None)
def rel_image(w):
    if not w:return {():1}
    return multiply(rel_generator(w[0]),rel_image(w[1:]))

def antipode(a):
    out={}
    for w,c in a.items():
        f=flat(w);n=len(f)
        for v,sg in normalize(tuple(reversed(f))).items():
            add_to(out,v,c*pm(n*(n+1)//2)*sg)
    return out

def quotient(a,own):
    return {w:c for w,c in a.items() if not w or w[-1][0]//3!=own}

# E/E E_own^+ = R tensor exterior(opposite). All operations below use actual
# word columns and their integer inverse, rather than assigned rank values.
@lru_cache(None)
def factorization(n,own):
    other=SIDES[1-own]
    labels=[];cols=[]
    for O in subsets(other):
        if len(O)>n:continue
        for rw in rel_words(n-len(O)):
            labels.append((rw,O))
            cols.append(quotient(multiply(rel_image(rw),normalize(O)),own))
    piv={}
    for j,c in enumerate(cols):
        v=dict(c);coeff={j:1}
        while v:
            row=min(v);a=v[row]
            if row in piv:
                pv,pc=piv[row]
                v=add(v,pv,-a);coeff=add(coeff,pc,-a)
            else:
                ck(abs(a)==1,'factorization_unit_pivot',(n,own,j,row,a))
                piv[row]=(scaled(v,a),scaled(coeff,a));break
        ck(bool(v),'factorization_independent_column',(n,own,j))
    basis=[w for w in all_words(n) if not w or w[-1][0]//3!=own]
    ck(len(basis)==len(labels)==len(piv),'factorization_complete_basis',(n,own))
    return tuple(labels),piv

def project_relative(a,own):
    if not a:return {}
    out={}
    bydeg={}
    for w,c in quotient(a,own).items():add_to(bydeg.setdefault(degree(w),{}),w,c)
    for n,v0 in bydeg.items():
        labels,piv=factorization(n,own)
        v=dict(v0);coeff={}
        while v:
            row=min(v);a0=v[row]
            if row not in piv:raise AssertionError(('not_spanned',own,n,row))
            pv,pc=piv[row];v=add(v,pv,-a0);coeff=add(coeff,pc,a0)
        for j,c in coeff.items():
            rw,O=labels[j]
            if not O:out=add(out,rel_image(rw),c)
    return out

def mate_minimal(a,own):
    # Output is the v component of RHom_B(P_C,E_beta,k).
    return antipode(project_relative(a,own))

@lru_cache(None)
def monomials(n,side=-1):
    if n==0:return (ZERO,)
    out=[]
    for s in (0,1):
        if side>=0 and side!=s:continue
        for es in product(range(n+1),repeat=3):
            if sum(es)==n:
                z=[0]*6
                for j,e in zip(SIDES[s],es):z[j]=e
                out.append(tuple(z))
    return tuple(out)

def monodeg(m):return sum(m)

def monovalue(i):return tuple(int(i==j) for j in range(6))

def single_letter(m):
    return m.index(1) if sum(m)==1 else None

@lru_cache(None)
def split_monomial(m,allow_empty_second=False):
    out=[]
    for a in product(*(range(x+1) for x in m)):
        if sum(a)==0:continue
        b=tuple(x-y for x,y in zip(m,a))
        if sum(b) or allow_empty_second:out.append((a,b))
    return tuple(out)

# A bar cochain basis is (tuple of positive monomials, final branch monomial).
# Its internal occurrence weight is minus the sum of those exponent vectors.
@lru_cache(None)
def bar_basis(n,total,own):
    out=[]
    if n==0:return tuple(((),m) for m in monomials(total,own))
    for k in range(1,total+1):
        for head in monomials(k):
            for bars,m in bar_basis(n-1,total-k,own):out.append(((head,)+bars,m))
    return tuple(out)

def bar_delta(v):
    out={}
    for (bars,m),c in v.items():
        n=len(bars)
        for i,b in enumerate(bars):
            for l,r in split_monomial(b):
                add_to(out,(bars[:i]+(l,r)+bars[i+1:],m),c*pm(i+1))
        for l,r in split_monomial(m,True):
            add_to(out,(bars+(l,),r),c*pm(n+1))
    return out

def bar_koszul_projection(v,own):
    out={}
    for (bars,m),c in v.items():
        if m!=ZERO or any(monodeg(b)!=1 for b in bars):continue
        out=add(out,normalize(tuple(single_letter(b) for b in bars)),c)
    return quotient(out,own)

def bar_mate(v,own):return mate_minimal(bar_koszul_projection(v,own),own)

def cup_words(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():add_to(out,x+y,c*d)
    return out

def cup_bracket(a,b):
    if not a or not b:return {}
    return add(cup_words(a,b),cup_words(b,a),-pm(len(next(iter(a)))*len(next(iter(b)))))

@lru_cache(None)
def bar_rel_generator(J):
    root=min(i for i in J if i<3);a={(root,):1}
    for i in reversed(tuple(i for i in J if i!=root)):
        a=cup_bracket({(i,):1},a)
    return a

def bar_cup(a,v):
    out={}
    for word,c in a.items():
        prefix=tuple(monovalue(i) for i in word)
        for (bars,m),d in v.items():add_to(out,(prefix+bars,m),c*d)
    return out

def permutations():
    ds=tuple(tuple(int(x) for x in a) for a in LABELS)
    result=[]
    for rot,ref in product(range(3),(False,True)):
        perm=[]
        for a,b in ds:
            new=tuple(sorted((((1-a if ref else a)+2*rot)%6,((1-b if ref else b)+2*rot)%6)))
            perm.append(ds.index(new))
        result.append(tuple(perm))
    return tuple(result)

def transport(a,p):
    out={}
    for w,c in a.items():out=add(out,normalize(tuple(p[i] for i in flat(w))),c)
    return out

def record(a):
    return [{'word':[[LABELS[i] for i in b] for b in w],'coefficient':c} for w,c in sorted(a.items())]

def run(outpath):
    maxn=4
    gens=[J for J in MIXED if len(J)<=4]
    quad=[J for J in gens if len(J)==2]
    ck(Counter(map(len,MIXED))=={2:9,3:18,4:15,5:6,6:1},'generator_degree_counts')
    for own in (0,1):
        for n in range(maxn+1):factorization(n,own)

    # All native endpoint-bar cochain basis vectors of total occurrence degree
    # <=4, not just already closed operation representatives.
    for own in (0,1):
        for total in range(maxn+1):
            for n in range(total+1):
                for b in bar_basis(n,total,own):
                    v={b:1};dv=bar_delta(v)
                    ck(not bar_delta(dv),'bar_d_squared',(own,n,total,b))
                    ck(not bar_koszul_projection(dv,own),'bar_projection_chain_equation',(own,n,total,b))
                    ck(not bar_mate(dv,own),'mate_chain_equation',(own,n,total,b))
                    for J in gens:
                        if total+len(J)>maxn:continue
                        lhs=bar_mate(bar_cup(bar_rel_generator(J),v),own)
                        rhs=scaled(multiply(bar_mate(v,own),antipode(rel_generator(J))),pm(len(J)*n))
                        ck(lhs==rhs,'native_bar_relative_intertwining',(own,J,n,total,b))

    eps={((),ZERO):1};images=[]
    for own in (0,1):
        ck(bar_mate(eps,own)=={():1},'primitive_to_v_coefficient_one',own)
        for J in gens:
            actual=bar_mate(bar_cup(bar_rel_generator(J),eps),own)
            wanted=antipode(rel_generator(J))
            ck(actual==wanted,'primitive_generator_mate',(own,J))
            images.append({'own_sheet':own,'generator':[LABELS[i] for i in J],
                           'operation_degree':len(J),'target_v_cochain':record(actual)})
        for J in quad:
            for K in quad:
                cochain=bar_cup(bar_rel_generator(J),bar_cup(bar_rel_generator(K),eps))
                actual=bar_mate(cochain,own)
                expected=multiply(antipode(rel_generator(K)),antipode(rel_generator(J)))
                ck(actual==expected,'all_81_quadratic_products',(own,J,K))

    quadratic_detectors=[]
    eta35=normalize((2,))
    for J in quad:
        pos=next(i for i in J if i<3);neg=next(i for i in J if i>=3)
        row=((neg,),(pos,))
        image=antipode(rel_generator(J))
        ck(image.get(row)==-1,'quadratic_target_unit_detector',J)
        for w in all_words(1):
            ck(multiply(eta35,{w:1}).get(row,0)==0,'quadratic_detector_kills_all_boundaries',(J,w))
        for own in (0,1):
            seq=(pos,neg) if own==0 else (neg,pos)
            # Cross-sheet adjacent product and the final action vanish.
            ck(seq[0]//3!=seq[1]//3 and seq[-1]//3!=own,'quadratic_source_bar_cycle',(own,J))
            ck(bar_rel_generator(J).get(seq)==1,'quadratic_source_unit_evaluation',(own,J))
        quadratic_detectors.append({'generator':[LABELS[i] for i in J],
              'target_row':[[LABELS[neg]],[LABELS[pos]]],'value':-1,
              'target_boundary_test':'zero on every beta*eta35*E^1 boundary'})

    # The normalized conductor Hom has differential d(alpha*u)=beta*eta_k*alpha*v.
    # Converting right action via S includes the degree of the module element.
    for own in (0,1):
        for J in gens:
            for m in range(maxn-len(J)+1):
                for w in all_words(m):
                    if w and w[-1][0]//3==own:continue
                    a={w:1};g=rel_generator(J)
                    lhs=mate_minimal(quotient(multiply(g,a),own),own)
                    rhs=scaled(multiply(mate_minimal(a,own),antipode(g)),pm(len(J)*m))
                    ck(lhs==rhs,'relative_module_intertwining',(own,J,w))
                    # Source ordering is (bar cochain) tensor (endpoint line).
                    # Swapping that line to the left contributes (-1)^(m*ell).
                    for ell in (0,1):
                        framed_lhs=scaled(lhs,pm((len(J)+m)*ell))
                        framed_value=scaled(mate_minimal(a,own),pm(m*ell))
                        framed_rhs=scaled(multiply(framed_value,antipode(g)),pm(len(J)*(m+ell)))
                        ck(framed_lhs==framed_rhs,'endpoint_line_Koszul_interchange',(own,J,w,ell))
    for k in range(6):
        eta=normalize((k,))
        for m in range(3):
            for w in all_words(m):
                ck(not multiply(eta,multiply(eta,{w:1})),'conormal_Hom_d_squared',(k,w))
                for J in gens:
                    if m+len(J)>maxn:continue
                    Sg=antipode(rel_generator(J))
                    lhs=scaled(multiply(eta,multiply({w:1},Sg)),pm(len(J)*m))
                    rhs=scaled(multiply(multiply(eta,{w:1}),Sg),pm(len(J))*pm(len(J)*(m+1)))
                    ck(lhs==rhs,'converted_action_dg_sign',(k,w,J))

    for J in MIXED:
        a=rel_generator(J)
        ck(antipode(a)==scaled(a,-1),'primitive_antipode_sign',J)
        ck(antipode(antipode(a))==a,'antipode_involution',J)
        for p in permutations():
            ck(antipode(transport(a,p))==transport(antipode(a),p),'antipode_labelled_covariance',(J,p))
    for J in gens:
        for K in gens:
            if len(J)+len(K)>6:continue
            a=rel_generator(J);b=rel_generator(K)
            ck(antipode(multiply(a,b))==scaled(multiply(antipode(b),antipode(a)),pm(len(J)*len(K))),
               'graded_antimultiplicativity',(J,K))

    # Complete module transport; normalization into relative words is not
    # replaced by an action on indecomposable generator ranks.
    for own in (0,1):
        for n in range(maxn+1):
            for w in all_words(n):
                if w and w[-1][0]//3==own:continue
                for p in permutations():
                    new_own=p[SIDES[own][0]]//3
                    ck(mate_minimal(transport({w:1},p),new_own)==transport(mate_minimal({w:1},own),p),
                       'full_labelled_module_transport',(own,w,p))

    # Known degree-four reflection, checked as a whole polynomial, not ranks.
    atom=lambda i:normalize((i,))
    g=bracket(atom(1),bracket(atom(3),bracket(atom(4),atom(0))))
    r21=bracket(atom(1),atom(3));r12=bracket(atom(0),atom(4))
    correction=bracket(r21,r12)
    reflections=[p for p in permutations() if p[0]//3==1]
    reflected=[p for p in reflections if transport(g,p)==add(scaled(g,-1),correction)]
    ck(len(reflected)==1,'specified_reflection_found')
    ck(bool(correction),'reflection_product_correction_nonzero')
    for own in (0,1):
        p=reflected[0]
        new_own=p[SIDES[own][0]]//3
        ck(mate_minimal(transport(quotient(g,own),p),new_own)==transport(mate_minimal(quotient(g,own),own),p),
           'decomposable_reflection_mate',own)

    # Negative control only: unconverted right action reverses the ordered pair.
    A=bracket(atom(0),atom(3));B=bracket(atom(1),atom(4))
    defect=add(multiply(A,B),multiply(B,A),-1)
    detector=((0,),(3,),(1,),(4,))
    ck(defect.get(detector)==1,'unconverted_order_defect_unit_detector')
    ck(all(not(w and w[0][0]//3==0 and 2 in w[0]) for w in [detector]),
       'detector_outside_eta35_boundary_rows')

    cert={
      'decision':3,
      'status':'normalized_native_algebraic_mate_checked_physical_line_support_adapter_unavailable',
      'physical_framed_mate_certified':False,
      'source':'normalized native bar cochains RHom_B(B_sigma,C), without replacing final branch by its ideal',
      'target':'native minimal conductor-resolution Hom(P_C,E_beta,k), v component',
      'primitive':'branch augmentation -> v with coefficient 1',
      'construction':'Phi = v * antipode * relative_seed_zero_projection * bar_diagonal_Koszul_projection',
      'variance':'right action becomes left action r.star.n=(-1)^(|r||n|) n.S(r)',
      'scope_of_external_line':'same symbolic line; the required native-to-conormal line/support morphism chi_sigma is an unset input',
      'line_interchange_sign':'Phi(f tensor ell)=(-1)^(degree(f)*degree(ell))*chi_sigma(ell)*S(P_sigma Q_sigma(f))',
      'scope_of_support':'same retained coefficient ring C; no support functor on the physical normal packet chosen',
      'tested_generators_per_endpoint':{'quadratic':9,'cubic':18,'quartic':15},
      'tested_ordered_quadratic_products_per_endpoint':81,
      'bar_basis_max_total_occurrence_degree':maxn,
      'factorization_seeds_per_endpoint':8,
      'product_order_control':{'word':[LABELS[i] for b in detector for i in b],
                               'value':1,'defect':record(defect),
                               'not_a_first_quadratic_obstruction':True},
      'primitive_images':images,
      'quadratic_integral_detectors':quadratic_detectors,
      'reflection':{'permutation':[LABELS[i] for i in reflected[0]],'correction':record(correction)},
      'proof_boundary':[
        'Finite checks do not substitute for the all-degree bar projection and Hopf-module factorization proof.',
        'No supplied first-jet or native-operation adapter was executed; those files were not mounted.',
        'The algebraic mate is not a covariant repair of ambient RHom_A.',
        'No physical H_sigma,r is set to zero from equality on cohomology.',
        'Physical shifts and determinant/support maps require the actual adapter interfaces.'
      ],
      'checks':dict(sorted(COUNTS.items())),
      'assertions':sum(COUNTS.values()),
    }
    Path(outpath).write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':cert['status'],'checks':cert['checks'],'assertions':cert['assertions']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('native_variance_mate_certificate.json'))
    args=p.parse_args();run(args.output)
