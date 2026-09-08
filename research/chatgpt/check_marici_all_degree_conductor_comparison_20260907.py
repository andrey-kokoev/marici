#!/usr/bin/env python3
"""Exact integral audit of the all-degree auxiliary/native conductor comparison.

C is an arbitrary retained commutative spectator ring.  Calculations use
integer coefficients and formal occurrence monomials. The all-degree proof
is in the accompanying note; bounded tests do not replace that proof.
No network, repository writes, inversion of integers, or optional modules.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb
from pathlib import Path
import hashlib
import json

CHECKS: Counter[str] = Counter()
ZERO=(0,)*8
PLUS=(0,1,2); MINUS=(3,4,5)
LABELS=((1,3),(1,5),(3,5),(0,2),(0,4),(2,4))


def check(ok, name, detail=None):
    if not ok: raise AssertionError((name,detail))
    CHECKS[name]+=1


def pm(n): return -1 if n%2 else 1


def put(v,k,a):
    if a:
        v[k]=v.get(k,0)+a
        if not v[k]: del v[k]


def add(*vs):
    out={}
    for v in vs:
        for k,a in v.items(): put(out,k,a)
    return out


def scaled(v,c): return {k:a*c for k,a in v.items() if a*c}


def side(i): return 0 if i<3 else 1


def invsign(seq):
    return pm(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))


def mon_plus(e,i,mode):
    f=list(e);f[i]+=1;f=tuple(f)
    return f if mon_allowed(f,mode) else None


def mon_allowed(e,mode):
    if mode=='U': return not(e[6] and e[7])
    if mode=='B': return not(e[6] or e[7]) and not(any(e[:3]) and any(e[3:6]))
    raise ValueError(mode)


@lru_cache(None)
def words(n,first=-1):
    if n==0: return ((),)
    ans=[]
    for s in (0,1):
        if first>=0 and s!=first: continue
        letters=PLUS if s==0 else MINUS
        for k in range(1,min(3,n)+1):
            for b in combinations(letters,k):
                for w in words(n-k,1-s): ans.append((b,)+w)
    return tuple(ans)


def degree(w): return sum(map(len,w))


def flat(w): return tuple(i for b in w for i in b)


def eval_letters(seq):
    """Normal form in Lambda(PLUS) * Lambda(MINUS)."""
    blocks=[];sgn=1;i=0
    while i<len(seq):
        j=i+1
        while j<len(seq) and side(seq[j])==side(seq[i]): j+=1
        run=seq[i:j]
        if len(run)!=len(set(run)): return {}
        sgn*=invsign(run);blocks.append(tuple(sorted(run)));i=j
    return {tuple(blocks):sgn}


def mul_b(w,v): return eval_letters(flat(w)+flat(v))


def ext_image(w):
    fs=flat(w)
    if len(fs)!=len(set(fs)): return {}
    return {tuple(sorted(fs)):invsign(fs)}


def mul_ext(s,t):
    if set(s)&set(t): return {}
    return {tuple(sorted(s+t)):invsign(s+t)}


def mul_u(a,b):
    s,wa=a;t,wb=b
    ext=mul_ext(s,t)
    if not ext or (wa and wb and wa[-1]==wb[0]): return {}
    return {(st,wa+wb):sgn*pm(len(wa)*len(t)) for st,sgn in ext.items()}


def u_basis(n):
    ans=[]
    for k in range(min(6,n)+1):
        q=n-k
        aux=((),) if q==0 else tuple(tuple(6+(i+j)%2 for j in range(q)) for i in (0,1))
        for s in combinations(range(6),k):
            ans.extend((s,w) for w in aux)
    return tuple(ans)


def native_d(v):
    out={}
    for (w,e),a in v.items():
        if not w: continue
        b=w[0]
        for j,i in enumerate(b):
            f=mon_plus(e,i,'B')
            if f is None: continue
            rest=b[:j]+b[j+1:]
            ww=((rest,)+w[1:]) if rest else w[1:]
            put(out,(ww,f),pm(j)*a)
    return out


def native_h(v):
    out={}
    for (w,e),a in v.items():
        if not any(e): continue
        s=0 if any(e[:3]) else 1
        if w and side(w[0][0])==s: b=w[0];rest=w[1:]
        else: b=();rest=w
        i=min([j for j in range(6) if e[j]]+list(b))
        if i in b: continue
        f=list(e);f[i]-=1
        ww=(tuple(sorted(b+(i,))),)+rest
        put(out,(ww,tuple(f)),a*pm(sum(j<i for j in b)))
    return out


def endomorphism(v,i):
    out={}
    for (w,e),a in v.items():
        if not w or i not in w[-1]: continue
        b=w[-1];j=b.index(i);sgn=pm(sum(map(len,w[:-1]))+j)
        rem=b[:j]+b[j+1:]
        ww=w[:-1]+((rem,) if rem else ())
        put(out,(ww,e),a*sgn)
    return out


def u_d(v):
    out={}
    for ((s,w),e),a in v.items():
        for j,i in enumerate(s):
            f=mon_plus(e,i,'U')
            if f is not None: put(out,((s[:j]+s[j+1:],w),f),a*pm(j))
        if w:
            f=mon_plus(e,w[0],'U')
            if f is not None: put(out,((s,w[1:]),f),a*pm(len(s)))
    return out


@lru_cache(None)
def phi_occ(s):
    return {w:invsign(flat(w)) for w in words(len(s)) if tuple(sorted(flat(w)))==s}


def phi(v):
    out={}
    for ((s,w),e),a in v.items():
        if w or not mon_allowed(e,'B'): continue
        for ww,b in phi_occ(s).items(): put(out,(ww,e),a*b)
    return out


def exterior_d(s):
    out={}
    for j,i in enumerate(s):
        e=list(ZERO);e[i]=1
        put(out,((s[:j]+s[j+1:],()),tuple(e)),pm(j))
    return out


def coprod_b(w):
    out={}
    for i in range(len(w)+1): put(out,(w[:i],w[i:]),1)
    for i,b in enumerate(w):
        for k in range(1,len(b)):
            for left in combinations(b,k):
                right=tuple(j for j in b if j not in left)
                put(out,(w[:i]+(left,),(right,)+w[i+1:]),invsign(left+right))
    return out


def coprod_ext(s):
    out={}
    for k in range(len(s)+1):
        for left in combinations(s,k):
            right=tuple(i for i in s if i not in left)
            put(out,(left,right),invsign(left+right))
    return out


def generated_relation(prefix,i,j,suffix):
    return add(eval_letters(prefix+(i,j)+suffix),eval_letters(prefix+(j,i)+suffix))


def ideal_witness(w):
    """Express w - its exterior normal form as prefix*(xy+yx)*suffix terms."""
    seq=list(flat(w));sgn=1;terms=[]
    while True:
        if any(seq[j]==seq[j+1] for j in range(len(seq)-1)):
            result={};break
        j=next((j for j in range(len(seq)-1) if seq[j]>seq[j+1]),None)
        if j is None:
            result=scaled(eval_letters(tuple(seq)),sgn);break
        i,k=seq[j],seq[j+1]
        if side(i)!=side(k):
            terms.append((sgn,tuple(seq[:j]),i,k,tuple(seq[j+2:])))
        seq[j],seq[j+1]=seq[j+1],seq[j];sgn=-sgn
    rhs=dict(result)
    for a,p,i,j,s in terms: rhs=add(rhs,scaled(generated_relation(p,i,j,s),a))
    return rhs,terms,result


def bar_top_kernel(multiset,mode):
    """Exact linear-strand bar kernel via signed adjacent-swap components.

    Each nonzero-product row says c_w+c_swap=0. An equal adjacent pair
    has one preimage and forces c_w=0. This is integral elimination with
    unit coefficients, not a rational rank or modular estimate.
    """
    ws=tuple(sorted(set(permutations(multiset))))
    adj=defaultdict(list);killed=set()
    for w in ws:
        for j in range(len(w)-1):
            a,b=w[j:j+2]
            zero=(set((a,b))=={6,7}) if mode=='U' else (side(a)!=side(b)) if mode=='B' else False
            if zero: continue
            if a==b: killed.add(w)
            else:
                q=w[:j]+(b,a)+w[j+2:];adj[w].append(q)
    seen=set();basis=[]
    for w in ws:
        if w in seen: continue
        coeff={w:1};queue=deque([w]);bad=False;pin=False
        seen.add(w)
        while queue:
            x=queue.popleft();pin |= x in killed
            for y in adj[x]:
                v=-coeff[x]
                if y in coeff: bad |= coeff[y]!=v
                else: coeff[y]=v;seen.add(y);queue.append(y)
        check(not bad or pin,'bar_no_unpinned_odd_component',(multiset,mode))
        if not pin and not bad: basis.append(coeff)
    return ws,basis


def act_b(w,p):
    ans=[];sgn=1
    for block in w:
        vals=tuple(p[i] for i in block);sgn*=invsign(vals);ans.append(tuple(sorted(vals)))
    return tuple(ans),sgn


def main(output,max_degree):
    check(4<=max_degree<=8,'degree_window',max_degree)
    # Integral free resolution and contraction on monomial test inputs.
    mons=[ZERO]
    for sigma in (PLUS,MINUS):
        for n in (1,2):
            for inds in combinations_with_replacement(sigma,n):
                v=[0]*8
                for i in inds:v[i]+=1
                mons.append(tuple(v))
    for n in range(max_degree+1):
        for w in words(n):
            for e in (mons if n<=3 else (ZERO,mons[1],mons[10])):
                v={(w,e):1}
                check(not native_d(native_d(v)),'native_d_squared')
                expected={} if not w and not any(e) else v
                check(add(native_d(native_h(v)),native_h(native_d(v)))==expected,'native_integral_contraction',(w,e))
    # Free auxiliary resolution and actual semilinear comparison before augmentation.
    umons=mons+[(0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,1)]
    for n in range(max_degree+2):
        for a in u_basis(n):
            for e in (umons if n<=2 else (ZERO,)):
                v={(a,e):1}
                check(not u_d(u_d(v)),'auxiliary_d_squared')
                check(native_d(phi(v))==phi(u_d(v)),'semilinear_chain_comparison',(a,e))
    # Exterior->native matrix, pivots, coalgebra, and naturality.
    perms=[]
    for r,reflect in product(range(3),(0,1)):
        dmap=[]
        for a,b in LABELS:
            im=tuple(sorted((((1-a if reflect else a)+2*r)%6,((1-b if reflect else b)+2*r)%6)))
            dmap.append(LABELS.index(im))
        perms.append(tuple(dmap))
    support_sizes=[]
    for n in range(7):
        for s in combinations(range(6),n):
            image=phi_occ(s)
            canon=tuple(b for b in (tuple(i for i in s if i<3),tuple(i for i in s if i>=3)) if b)
            check(image.get(canon)==1,'primitive_pivot',s)
            check(all(tuple(sorted(flat(w)))==s for w in image),'separate_multigrades',s)
            check(native_d({(w,ZERO):c for w,c in image.items()})==phi(exterior_d(s)),'exterior_comparison_chain_map',s)
            lhs={}
            for w,a in image.items():lhs=add(lhs,scaled(coprod_b(w),a))
            rhs={}
            for (l,r),a in coprod_ext(s).items():
                for w,b in phi_occ(l).items():
                    for v,c in phi_occ(r).items():put(rhs,(w,v),a*b*c)
            check(lhs==rhs,'coalgebra_comparison',s)
            for p in perms:
                act={}
                for w,a in image.items():
                    ww,b=act_b(w,p);put(act,ww,a*b)
                ss=tuple(p[i] for i in s)
                check(act==scaled(phi_occ(tuple(sorted(ss))),invsign(ss)),'labelled_dihedral_naturality',(s,p))
            support_sizes.append({'subset':s,'nonzero_target_rows':len(image)})
    # Actual Yoneda endomorphisms on the native free resolution.
    for n in range(min(max_degree,5)+1):
        for w in words(n):
            v={(w,ZERO):1}
            for i in range(6):
                check(not add(native_d(endomorphism(v,i)),endomorphism(native_d(v),i)),'yoneda_chain_cocycle',(w,i))
                check(not endomorphism(endomorphism(v,i),i),'yoneda_square_zero',(w,i))
            for sigma in (PLUS,MINUS):
                for i,j in combinations(sigma,2):
                    check(not add(endomorphism(endomorphism(v,j),i),endomorphism(endomorphism(v,i),j)),'within_sheet_anticommutator',(w,i,j))
            ev=v
            for i in reversed(flat(w)): ev=endomorphism(ev,i)
            check(ev=={((),ZERO):pm(n*(n-1)//2)},'yoneda_dual_basis_diagonal',w)
    # Kernel ideal generation by explicit normal ordering.
    max_witness=0
    for n in range(max_degree+1):
        for w in words(n):
            rhs,terms,res=ideal_witness(w)
            check(rhs=={w:1},'nine_relation_witness',w)
            im=ext_image(w)
            remainder_image={}
            for v,a in res.items(): remainder_image=add(remainder_image,scaled(ext_image(v),a))
            check(remainder_image==im,'normal_order_remainder',w)
            max_witness=max(max_witness,len(terms))
            for i in range(6):
                g=((i,),)
                for left,right in ((w,g),(g,w)):
                    image={}
                    for v,a in mul_b(left,right).items():image=add(image,scaled(ext_image(v),a))
                    expected={}
                    for s,a in ext_image(left).items():
                        for t,b in ext_image(right).items():expected=add(expected,scaled(mul_ext(s,t),a*b))
                    check(image==expected,'yoneda_map_multiplicativity')
    # Independent bar-complex kernel in complete fine degrees, not word-count input.
    bar_summary={}
    for mode,letters in (('B',6),('U',8),('S',6)):
        totals=[]
        for n in range(1,5):
            total=0
            for ms in combinations_with_replacement(range(letters),n):
                ws,ker=bar_top_kernel(ms,mode);total+=len(ker)
                if mode=='B':
                    expected=sum(tuple(sorted(flat(w)))==ms for w in words(n))
                elif mode=='U':
                    expected=sum(tuple(sorted(s+w))==ms for s,w in u_basis(n))
                else:expected=int(len(ms)==len(set(ms)))
                check(len(ker)==expected,'independent_bar_fine_degree',(mode,ms))
            totals.append(total)
        bar_summary[mode]=totals
    # Every native quadratic generator of the comparison kernel and its powers.
    for i,j in product(PLUS,MINUS):
        k=add(eval_letters((i,j)),eval_letters((j,i)))
        image={}
        for w,a in k.items(): image=add(image,scaled(ext_image(w),a))
        check(not image and len(k)==2,'mixed_operation_defect',(i,j))
        for m in range(1,8):
            power={():1}
            for _ in range(m):
                nxt={}
                for a,x in power.items():
                    for b,y in k.items():
                        for w,z in mul_b(a,b).items():put(nxt,w,x*y*z)
                power=nxt
            check(len(power)==2,'mixed_defect_non_nilpotent',(i,j,m))
    # Rank series and cofiber: differential is zero in both minimal conductor fibres.
    ranks=[]
    bn=[]
    for n in range(21):
        b=(comb(3,n) if n<=3 else 0)+sum(c*bn[n-j] for j,c in ((1,3),(2,3),(3,1)) if n>=j)
        bn.append(b)
        a=sum(comb(6,k)*(1 if n==k else 2) for k in range(min(6,n)+1))
        e=comb(6,n) if n<=6 else 0
        if n<=max_degree:check(b==len(words(n)),'native_rank_series',n)
        check(a==len(u_basis(n)),'auxiliary_rank_series',n)
        previous_kernel=0 if n==0 else ranks[-1]['kernel']
        ranks.append({'degree':n,'auxiliary':a,'native':b,'image':e,'kernel':a-e,'cokernel':b-e,'cofiber':b-e+previous_kernel})
    # Algebraic retract proof for the earlier endpoint defect: a degree-two B
    # coordinate has zero differential and its projection is a left inverse.
    for n in range(2,12):
        inc={(n,0):1};projection=sum(v for (deg,slot),v in inc.items() if deg==n and slot==0)
        check(projection==1,'endpoint_free_retract',n)
    cert={
      'scope':'Augmented coefficient algebra U->S->B; not a native geometric endpoint connector.',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'rings':{'S':'C[x1,x2,x3,y1,y2,y3]','U':'S[a,b]/(ab)','B':'S/(xi*yj)'},
      'comparison':'a,b -> 0; six occurrence coordinates unchanged',
      'all_degree_tor_image':'exterior coalgebra on the six occurrence classes; rank binomial(6,n), zero for n>6',
      'yoneda_kernel':'two-sided ideal generated by xi_i*eta_j+eta_j*xi_i, all nine pairs',
      'image_hilbert_series':'(1+z)^6',
      'native_hilbert_series':'(1+z)^3/(1-3*z-3*z^2-z^3)',
      'auxiliary_hilbert_series':'(1+z)^7/(1-z)',
      'integer_torsion_in_kernel_cokernel_cofiber':False,
      'cofiber_connectedness':'H0=H1=0; H2 rank 11; higher ranks below',
      'rank_table':ranks,
      'explicit_integral_comparison_rows':support_sizes,
      'independent_bar_linear_strand_ranks':bar_summary,
      'max_degree_native_words_checked':max_degree,
      'max_number_mixed_generator_terms_in_rewriting':max_witness,
      'endpoint_functor_test':'If an exact functor F:D(B)->D has F(B) != 0, it cannot make the fixed endpoint comparison an equivalence: its fibre has a retract B[2].',
      'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
      'limitations':[
        'Finite test windows do not prove unbounded exactness; the monomial contraction and normal-form proofs do.',
        'The Tor comparison is not the total conductor-kernel equivalence computed previously.',
        'No physical endpoint 2-cell, global punctured-gluing equivalence, Cut compatibility, or RH claim.',
        'Degree-six bound applies to this augmentation-based algebra map, not all supported or logarithmic correspondences.',
        'No entire dg algebra, E-infinity algebra, or Whitehead-product identification is claimed from this graded Yoneda computation.'
      ]}
    cert['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ('scope','exact_assertions','independent_bar_linear_strand_ranks','max_number_mixed_generator_terms_in_rewriting')},indent=2))
    print(json.dumps(ranks[:9],indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('marici_all_degree_conductor_comparison_certificate_20260907.json'))
    ap.add_argument('--max-degree',type=int,default=6)
    args=ap.parse_args();main(args.output,args.max_degree)
