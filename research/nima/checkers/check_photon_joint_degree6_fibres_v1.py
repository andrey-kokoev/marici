"""Nonzero-leading joint degree4/5/6 source fibres with unknown quartic contacts."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree6_cut_v1 as six
import check_photon_joint_cut_fibres_v1 as five
p=six.p;base=six.base
CONTRACT=HOME/'contracts/photon-joint-degree6-fibres-v1.json';PROOF=HOME/'photon-joint-degree6-fibres-v1.md'
TEST=HOME/'checkers/test_photon_joint_degree6_fibres_v1.py';MANIFEST=HOME/'scc-models/photon-joint-degree6-fibres-v1.json'
RESULT=HOME/'results/photon-joint-degree6-fibres-v1.json'


def plus(A,B):return tuple(p.add(a,b) for a,b in zip(A,B))
def scale(c,A):return tuple(p.scale(c,a) for a in A)
def flatten(A,diag=False):
    shape=(3,3,4) if diag else (3,3,4,3)
    return tuple(poly[i] if i<len(poly) else Q() for poly,n in zip(A,shape) for i in range(n))


def solve(columns,rhs):
    R,pivots=base.reduced_rows(tuple(tuple(col[i] for col in columns)+(rhs[i],) for i in range(len(rhs))))
    n=len(columns)
    if any(all(x==0 for x in row[:n]) and row[n] for row in R):raise ValueError('cut residual outside retained Born image')
    if tuple(pivots)!=tuple(range(n)):raise ValueError('nonunique quartic chart outside its rank domain')
    return tuple(R[i][n] for i in range(n))


def classify(data45,data6,cases):
    c=five.chart(data45)
    if c['stratum']=='zero-leading':raise NotImplementedError('zero-leading degree-six fibres are a separate stratum')
    d=c['root_square'];g,f,a,b,h=c['base'];normalized=scale(1/d,data6)
    N=tuple(plus(scale(g,cases[i]),scale(f,cases[i+3])) for i in range(3))
    if c['stratum']=='ordinary':
        known=six.combine(cases,(0,0,a,b,h,0,0,0));residual=plus(normalized,scale(-1,known))
        quartic=solve(tuple(flatten(v) for v in N),flatten(residual))
        values=(g,f,a,b,h)+quartic
        if six.combine(cases,values)!=normalized:raise ValueError('inconsistent ordinary data')
        return {'stratum':'ordinary','root_square':d,'base':values,'h_mode':'fixed','h_square':h*h,'oriented_branches':1,'actual_fibre_size':2}
    # On the cancellation chart g=1,f=-6, h is unknown; the diagonals are affine in h^2.
    assert (g,f)==(Q(1),Q(-6))
    known=six.combine(cases,(0,0,a,b,0,0,0,0));residual=plus(normalized,scale(-1,known))
    columns=tuple(flatten(v,True) for v in N)+(flatten(cases[11],True),)
    K,L,M,t=solve(columns,flatten(residual,True))
    if t<0:raise ValueError('negative h3 square has no real Born lift')
    S=10*a+b
    if S:
        observed=normalized[3][1] if len(normalized[3])>1 else Q()
        h=-960*observed/S
        if h*h!=t:raise ValueError('single-minus linear and square data disagree')
        values=(g,f,a,b,h,K,L,M)
        if six.combine(cases,values)!=normalized:raise ValueError('inconsistent cancellation data')
        return {'stratum':'leading-cancellation-resolved','root_square':d,'base':values,'h_mode':'fixed','h_square':t,'oriented_branches':1,'actual_fibre_size':2}
    expected=plus(known,plus(plus(scale(K,N[0]),scale(L,N[1])),plus(scale(M,N[2]),scale(t,cases[11]))))
    if expected!=normalized:raise ValueError('nonzero single-minus data on double cancellation')
    branches=2 if t else 1
    return {'stratum':'double-cancellation','root_square':d,'base':(g,f,a,b,Q(),K,L,M),
            'h_mode':'plus-minus-square-root' if t else 'fixed','h_square':t,'oriented_branches':branches,'actual_fibre_size':2*branches}


def check_source(source,cases):
    source=tuple(map(Q,source));data=five.observe(source[:5]);value=six.combine(cases,source)
    c=classify(data,value,cases);g,f=source[:2];r=abs(g) if g else abs(f);sign=1 if (g if g else f)>0 else -1
    oriented=tuple(sign*x/r for x in source)
    assert c['root_square']==r*r
    if c['h_mode']=='fixed':assert c['base']==oriented
    else:
        assert c['base'][:4]+c['base'][5:]==oriented[:4]+oriented[5:]
        assert c['h_square']==oriented[4]**2 and c['actual_fibre_size']==4
    assert six.combine(cases,tuple(-x for x in source))==value
    return c


def validate(c):
    assert c['schema']=='marici.photon-joint-degree6-fibres.v1' and c['owner']=='marici.Nima'
    assert c['domain']=='nonzero_real_leading_pair;full_coherent_angular_cuts_through_degree6;unknown_three_quartic_Born_contacts'
    for k in ('nonzero_leading_joint_fibres_classified','quartic_Born_nuisance_contacts_reconstructed',
              'double_cancellation_relative_h3_sign_retained','algebraic_h3_square_roots_not_forced_rational'):
        assert c[k] is True,k
    for k in ('zero_leading_fibres_classified','global_unique_physical_source_selected','uniformly_stable_inverse_derived',
              'native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=six.build();_,_,cases=six.inventory()
    counts={};total=0
    sources=list(product((Q(-1),Q(1)),repeat=8))
    sources+= [(Q(),Q(s),Q(2),Q(3),Q(4),Q(1),Q(-2),Q(3)) for s in (-2,2)]
    for quartic in product((Q(-1),Q(1)),repeat=3):
        for h in (Q(-1),Q(),Q(1)):
            sources.append((Q(1),Q(-6),Q(1),Q(),h)+quartic)
            for a in (Q(-1),Q(),Q(1)):sources.append((Q(1),Q(-6),a,-10*a,h)+quartic)
    for source in sources:
        result=check_source(source,cases);counts[result['stratum']]=counts.get(result['stratum'],0)+1;total+=1
    # The nuisance map is injective on both f!=0 and f=0 nonzero-leading charts.
    nuisance_ranks={}
    for g,f in ((1,0),(0,1),(1,2),(1,-6)):
        N=tuple(flatten(plus(scale(Q(g),cases[i]),scale(Q(f),cases[i+3]))) for i in range(3))
        rank=len(base.reduced_rows(tuple(zip(*N)))[1]);assert rank==3;nuisance_ranks[f'{g},{f}']=rank
    # Algebraic branch h=+/-sqrt(2): valid rational data are not restricted to rational source h.
    x=(Q(1),Q(-6),Q(1),Q(-10),Q(),Q(1),Q(-2),Q(3));datum=plus(six.combine(cases,x),scale(Q(2),cases[11]))
    root=classify(five.observe(x[:5]),datum,cases)
    assert root['h_mode']=='plus-minus-square-root' and root['h_square']==2 and root['actual_fibre_size']==4
    try:classify(five.observe(x[:5]),plus(six.combine(cases,x),scale(Q(-1),cases[11])),cases)
    except ValueError:pass
    else:raise AssertionError('negative real square accepted')
    # Boundary h=0 merges the two relative-sign branches.
    zero=classify(five.observe(x[:5]),six.combine(cases,x),cases);assert zero['actual_fibre_size']==2
    # Exact sign-recovery instability near the double cancellation, with nonzero quartic contacts.
    conditioning={}
    for n in (10,100,1000):
        eps=Q(1,n);a=(Q(1),Q(-6),Q(1),-10+eps,Q(1),Q(1),Q(-2),Q(3));b=a[:4]+(-a[4],)+a[5:]
        assert five.observe(a[:5])==five.observe(b[:5])
        A=six.combine(cases,a);B=six.combine(cases,b)
        gap=max(abs(u-v) for u,v in zip(flatten(A),flatten(B)))
        assert gap==eps/480 and 2/gap==960*n
        assert classify(five.observe(a[:5]),A,cases)['actual_fibre_size']==2
        conditioning[str(n)]=str(2/gap)
    # Full overdetermined response constraints matter, not only three fitted rows.
    source=(1,2,3,4,5,1,-2,3);A=six.combine(cases,source);bad=list(A);bad[2]=p.add(bad[2],(Q(),Q(),Q(),Q(1)))
    try:classify(five.observe(source[:5]),tuple(bad),cases)
    except ValueError:pass
    else:raise AssertionError('inconsistent higher mixed wave accepted')
    try:classify((Q(),)*7,((Q(),),)*4,cases)
    except NotImplementedError:pass
    else:raise AssertionError('zero-leading case silently treated as nonzero')
    refused=['fix_quartic_nuisance_to_zero','choose_one_relative_h3_sign_on_double_cancellation','discard_nonsquare_h3_data','infer_uniform_stability_from_exact_inverse']
    for key in ('zero_leading_fibres_classified','global_unique_physical_source_selected','uniformly_stable_inverse_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported degree-six fibre promotion: '+key)
    paths={ROOT/v for v in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-joint-degree6-fibres-receipt.v1','status':'pass',
        'scope':'nonzero_leading_real_joint_cut_fibres_with_unknown_quartic_Born_contacts_not_physical_matching',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'source_checks':total,'stratum_counts':counts,'quartic_nuisance_ranks':nuisance_ranks,
        'ordinary_actual_fibre_size':2,'resolved_cancellation_actual_fibre_size':2,'double_cancellation_nonzero_h_actual_fibre_size':4,
        'double_cancellation_zero_h_actual_fibre_size':2,'nonsquare_h3_square_control':'2',
        'relative_h_sign_inverse_lower_bounds':conditioning,
        'general_real_fibre_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale degree-six fibre receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','source_checks','stratum_counts','double_cancellation_nonzero_h_actual_fibre_size','zero_leading_fibres_classified')}))

if __name__=='__main__':main()
