"""Audit and sharpen the fixed gamma=1 bulk squared norms.

Whole frequency cells, not samples. Same 80-bit response identities, evaluated
with exact rational cancellations; finer cells and sharper infinite-tail bounds.
No detector or theta-window change.
"""
from pathlib import Path
from fractions import Fraction as Q
import runpy,json
from flint import arb,acb,acb_series,ctx

HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
NEW_BANDS=[(0,16,4096),(16,128,1024),(128,2048,64),(2048,8192,8)]

def endpoints(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def encode(x):
    a,b=endpoints(x)
    return {'lower':str(a),'upper':str(b),'display':x.str(24)}
def ball(q):return arb(q.numerator)/q.denominator

def refine():
    old_bands={rate:[arb(0),arb(0)] for rate in (2048,512,32)}
    def visit(j,rate,plus,minus):
        for i,x in enumerate((plus,minus)):old_bands[rate][i]+=abs(x)**2/rate
    old=runpy.run_path(str(HERE/'certify_even_response_norm.py'),init_globals={'CELL_VISITOR':visit})
    assert old['Y']==3 and old['GAMMA']==1 and old['BETA']==arb(3)/2 and old['S']==arb(7)/2
    assert old['T']==2048 and old['BANDS']==[(0,16,2048),(16,128,512),(128,2048,32)]
    ctx.prec=80
    pi=old['PI'];beta=old['BETA'];s=old['S']
    c=1/s+1/(s-1)-old['Ls'].real
    # Exact rational identities after clearing q(q-1)(q+s-1), respectively
    # q(q-1)(q-s). Coefficients of L(q) and L(s) already agree.
    sq=Q(7,2);c0=1/sq+1/(sq-1)
    assert (sq-1)/sq+(sq-2)/(sq-1)==2-c0
    assert -sq/(sq-1)-(sq+1)/sq==-2-c0
    def profiles(q):
        zz=acb_series([q,1],2).zeta()
        D=((q/2).digamma()-pi.log())/2+zz[1]/zz[0]
        return (c-D)/(q+s-1),(c+D)/(q-s)
    for frequency in (0,1,16,128,2048,8192):
        q=acb(beta,frequency)
        assert all((a-b).contains(0) for a,b in zip(profiles(q),old['profiles'](q)))
    total=[arb(0),arb(0)];prefix=[arb(0),arb(0)];extension=[arb(0),arb(0)];bands=[]
    for lo,hi,rate in NEW_BANDS:
        sums=[arb(0),arb(0)];counts={'evaluations':0,'accepted_cells':0,'bisected_cells':0}
        def cell(a,b,depth=0):
            counts['evaluations']+=1
            values=profiles(acb(beta,ball(a).union(ball(b))))
            if not all(x.is_finite() for x in values):
                assert depth<20, 'Unresolved frequency enclosure'
                counts['bisected_cells']+=1;mid=(a+b)/2
                cell(a,mid,depth+1);cell(mid,b,depth+1);return
            counts['accepted_cells']+=1
            width=ball(b-a)
            for i,x in enumerate(values):sums[i]+=width*abs(x)**2
        for j in range(lo*rate,hi*rate):cell(Q(j,rate),Q(j+1,rate))
        for i in range(2):
            total[i]+=sums[i]
            if hi<=2048:prefix[i]+=sums[i]
            else:extension[i]+=sums[i]
        bands.append({'range':[lo,hi],'initial_cells_per_unit':rate,**counts,
                      'norm_contributions':[encode(x/pi) for x in sums]})
    T=arb(8192)
    cL=old['Pbeta']+3/T-(2*pi).log()/2+pi/4+(1+(beta/T)**2).log()/4
    A=cL+abs(old['Ls'])+1/s+1/(s-1)
    if isinstance(A,acb):A=A.real
    value=A+T.log()/2
    common_tail=(value*value+value+arb(1)/2)/(pi*T)
    assert 0<common_tail<old['tail']
    tails=[]
    for sign in (-1,1):
        # D(q)=1/2 log(q/(2pi))+zeta'/zeta(q)+error, |error|<=1/t.
        # Retain the real/imaginary log-vector geometry and the cancelled c.
        base=-(2*pi).log()/2+sign*c
        assert T.log()/2+base>0
        delta=(1+(beta/T)**2).log()/4
        u=T.log()/2+base+delta
        K=base+delta+(pi/4)**2/(2*u)+old['Pbeta']+1/T
        Qtail=T.log()/2+K
        tail=(Qtail**2+Qtail+arb(1)/2)/(pi*T)
        assert 0<tail<common_tail
        tails.append(tail)
    new=[x/pi+arb(0).union(arb(tail.upper())) for x,tail in zip(total,tails)]
    baseline=[old['plus_sq'],old['minus_sq']]
    audit=[]
    for i,(a,b) in enumerate(zip(baseline,new)):
        al,au=endpoints(a);bl,bu=endpoints(b)
        assert al<bl<bu<au
        old_finite=old['integral'].real/pi if i==0 else old['integral'].imag/pi
        # Counterfactual keeps the OLD spectral tail and only sharpens finite cells.
        finite_only=prefix[i]/pi+arb(0).union(arb(old['tail'].upper()))
        resolved_only=total[i]/pi+arb(0).union(arb(common_tail.upper()))
        assert finite_only.upper()<a.upper() and resolved_only.upper()<finite_only.upper() and b.upper()<resolved_only.upper()
        finite_drop=Q(str(a.upper().fmpq()))-Q(str(finite_only.upper().fmpq()))
        tail_drop=Q(str(finite_only.upper().fmpq()))-Q(str(resolved_only.upper().fmpq()))
        algebra_drop=Q(str(resolved_only.upper().fmpq()))-Q(str(b.upper().fmpq()))
        assert min(finite_drop,tail_drop,algebra_drop)>0 and finite_drop+tail_drop+algebra_drop==au-bu
        audit.append({'old_squared_norm':encode(a),'new_squared_norm':encode(b),
                      'old_finite_part':encode(old_finite),'new_finite_prefix':encode(prefix[i]/pi),
                      'new_frequency_extension':encode(extension[i]/pi),
                      'finite_only_upper_bound':str(Q(str(finite_only.upper().fmpq()))),
                      'resolved_tail_only_upper_bound':str(Q(str(resolved_only.upper().fmpq()))),
                      'upper_bound_drop_from_finite_refinement':str(finite_drop),
                      'upper_bound_drop_from_resolved_tail':str(tail_drop),
                      'upper_bound_drop_from_sharper_tail_algebra':str(algebra_drop),
                      'meaning':'Drops are differences of certified upper bounds, not errors of the actual norm.'})
    report={'schema':'marici.grothendieck.bulk-response-norm-refinement.v1','passed':True,
            'parameters':{'y':3,'gamma':1,'beta':'3/2','arithmetic_bits':80,
                          'old_frequency_cutoff':2048,'new_frequency_cutoff':8192},
            'old_finite_bands':[{'cells_per_unit':rate,'norm_contributions':[encode(x/pi) for x in sums]}
                                for rate,sums in old_bands.items()],
            'new_finite_bands':bands,'old_tail_bound':encode(old['tail']),
            'old_formula_at_new_cutoff':encode(common_tail),
            'new_tail_bounds':[encode(tail) for tail in tails],
            'profile_identity':'c=1/s+1/(s-1)-L(s); D(q)=psi(q/2)/2-log(pi)/2+zeta_prime(q)/zeta(q); H_plus=(c-D)/(q+s-1); H_minus=(c+D)/(q-s)',
            'sides':audit,
            'scope':'Same fixed damped response. Whole-frequency cells, cancellation-preserving profile identities, and a log-vector digamma/Euler-line tail majorant. No physical cutoff or acquisition accuracy change.'}
    (OUT/'bulk-response-norm-refinement.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return [arb(x.upper()) for x in new],report

if __name__=='__main__':
    bounds,report=refine()
    print(json.dumps({'passed':True,'new_upper_bounds':[x.str(24) for x in bounds],
                      'old_tail':report['old_tail_bound']['display'],'new_tails':[x['display'] for x in report['new_tail_bounds']]},indent=2))
