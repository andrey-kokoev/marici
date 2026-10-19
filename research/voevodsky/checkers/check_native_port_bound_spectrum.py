"""Exact above-band bound-mode count, brackets, and preparation overlaps.
Uses monotone metric inertia, not numerical root finding or a finite lead cutoff.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_native_adapter_collective_closure import F,Span,closure,orthogonalize,restricted,inner,unit,apply

BASE=Path(__file__).resolve().parents[1]


def inertia(matrix):
    """Symmetric congruence elimination over Q(sqrt(151)), including zero pivots."""
    A=[list(row) for row in matrix];n=len(A);positive=negative=0
    assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
    for k in range(n):
        j=next((j for j in range(k,n) if A[j][j]),None)
        if j is None:
            pair=next(((i,j) for i in range(k,n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None:return positive,negative,n-k
            i,j=pair
            for t in range(k,n):A[i][t]=A[i][t]+A[j][t]
            for t in range(k,n):A[t][i]=A[t][i]+A[t][j]
            j=i
        A[k],A[j]=A[j],A[k]
        for row in A:row[k],row[j]=row[j],row[k]
        pivot=A[k][k];positive+=int(pivot.positive());negative+=int(not pivot.positive())
        inverse=pivot.inverse()
        for i in range(k+1,n):
            for j in range(i,n):
                A[i][j]=A[i][j]-A[i][k]*inverse*A[k][j];A[j][i]=A[i][j]
    return positive,negative,0


def sparse(A):return [{j:x for j,x in enumerate(row) if x} for row in A]
def energy(r):return Q(2)+r+1/r

def secular_gram(K,metric,ports,r):
    E=energy(r)
    return [[metric[i]*((F(E) if i==j else F())-K[i][j]-(F(1+r) if i==j and i<ports else F())) for j in range(len(K))] for i in range(len(K))]


def isolate(K,metric,ports,energy_tolerance=Q(1,10000000)):
    cache={};minor_cache={}
    def counts(r):
        if r not in cache:cache[r]=inertia(secular_gram(K,metric,ports,r))
        return cache[r]
    def minors(r):
        if r not in minor_cache:
            A=secular_gram(K,metric,ports,r)
            minor_cache[r]=[inertia([[A[i][j] for j in range(len(A)) if j!=port] for i in range(len(A)) if i!=port]) for port in range(ports)]
        return minor_cache[r]
    lo=Q(1,32);hi=Q(1)
    assert counts(lo)==(len(K),0,0)
    assert counts(hi)[2]==0
    work=[(lo,hi,0)];brackets=[]
    while work:
        low,high,depth=work.pop();left=counts(low);right=counts(high)
        assert left[2]==right[2]==0
        count=right[1]-left[1];assert count>=0
        if not count:continue
        if count==1 and energy(low)-energy(high)<=energy_tolerance:
            ml,mh=minors(low),minors(high)
            # A principal submatrix is also strictly monotone in energy. Equal
            # inertias at the bracket ends exclude a cofactor zero throughout.
            if all(a[1]==b[1] and a[2]==b[2]==0 for a,b in zip(ml,mh)):
                brackets.append({'decay_interval':[str(low),str(high)],
                    'energy_interval':[str(energy(high)),str(energy(low))],
                    'energy_midpoint_decimal':float((energy(high)+energy(low))/2),
                    'negative_counts_low_high_decay':[left[1],right[1]],
                    'visible_minor_inertias_low_decay':[list(a) for a in ml],
                    'visible_minor_inertias_high_decay':[list(a) for a in mh],
                    'simple_root_count':1,'all_active_port_overlaps_nonzero':True})
                continue
        if depth>=64:raise RuntimeError('Unresolved coincident root or overlap; do not guess')
        # Avoid an exactly singular rational split point rather than losing a
        # root at an interval endpoint. There are only finitely many such roots.
        middle=None
        for divisor in range(2,17):
            candidate=low+(high-low)/divisor
            if counts(candidate)[2]==0:middle=candidate;break
        if middle is None:raise RuntimeError('No regular subdivision point')
        work.extend([(low,middle,depth+1),(middle,high,depth+1)])
    brackets.sort(key=lambda b:Q(b['energy_interval'][0]))
    assert len(brackets)==counts(hi)[1]
    return {'threshold_inertia':list(counts(hi)),'upper_energy_cutoff':str(energy(lo)),
        'upper_cutoff_inertia':list(counts(lo)),'brackets':brackets,
        'exact_inertia_evaluations':len(cache),'minor_inertia_evaluations':sum(len(v) for v in minor_cache.values())}


def null_vector(A):
    span=Span(len(A))
    for i,row in enumerate(A):span.add(row,{'row':i})
    free=[i for i in range(len(A)) if i not in span.pivots]
    assert len(free)==1
    out=[F() for _ in A];out[free[0]]=F(1)
    for row,pivot in reversed(list(zip(span.rows,span.pivots))):
        out[pivot]=-sum((x*out[j] for j,x in enumerate(row) if j!=pivot),F())
    assert not any(apply(sparse(A),out))
    return out


def main():
    scattering_path=BASE/'results/native_port_scattering.json';joint_path=BASE/'results/native_joint_generator_resolvent.json'
    scattering=json.loads(scattering_path.read_text(encoding='utf-8'));source=json.loads(joint_path.read_text(encoding='utf-8'))
    for receipt in (scattering,source):
        assert receipt['verification_passed']
        for name,digest in receipt['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    K=[[F(*x) for x in row] for row in source['joint_generator']];metric=[F(*x) for x in source['gram_diagonal']]
    assert len(K)==11
    P=[[F(int(i==j and i<3)) for j in range(11)] for i in range(11)]
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    # Rational and radical parts preserve the same preparation blocks; building
    # them separately yields rational bases and avoids needlessly large radicals.
    rational=sparse([[F(x.a) for x in row] for row in K]);radical=sparse([[F(x.b) for x in row] for row in K])
    e0,e1,e2=[unit(11,i) for i in range(3)]
    plus=[a+b for a,b in zip(e1,e2)];minus=[a-b for a,b in zip(e1,e2)]
    sectors=[]
    for label,seeds,dimension,ports in [('symmetric',[e0,plus],5,2),('antisymmetric',[minus],6,1)]:
        span=closure(seeds,{'rational':rational,'radical':radical},11)
        check(label+'_dimension',len(span.rows)==dimension)
        basis,norms=orthogonalize(span.rows,metric)
        smallK=restricted(sparse(K),basis,metric,norms)
        smallP=restricted(sparse(P),basis,metric,norms)
        check(label+'_contact_projector',all(smallP[i][j]==int(i==j and i<ports) for i in range(dimension) for j in range(dimension)))
        sectors.append((label,basis,norms,smallK,ports))
    check('preparation_blocks_orthogonal',all(inner(a,b,metric)==0 for a in sectors[0][1] for b in sectors[1][1]))
    check('preparation_blocks_exhaust_central_space',sum(len(s[1]) for s in sectors)==11)
    full_top=inertia(secular_gram(K,metric,3,Q(1)))
    full_high=inertia(secular_gram(K,metric,3,Q(1,32)))
    check('five_above_band_roots_counted_by_full_inertia',full_top==(6,5,0) and full_high==(11,0,0))
    # dM/dE=I+r^2/(1-r^2)P is strictly positive for 0<r<1. Thus
    # inertia gives a global root count, including multiplicity, not a scan.
    check('secular_derivative_positive_at_exact_controls',all(1+r*r/(1-r*r)>0 for r in (Q(1,32),Q(1,8),Q(1,2),Q(7,8))))
    # Algebraic tail norm: lead state psi_n=(-r)^n u_port.
    check('tail_norm_derivative_identity',all((-1/(1-1/(r*r)))==r*r/(1-r*r) for r in (Q(1,32),Q(1,8),Q(1,2))))
    reports=[]
    for label,basis,norms,smallK,ports in sectors:
        print('Isolating '+label+' bound modes...',flush=True)
        audit=isolate(smallK,norms,ports)
        reports.append({'sector':label,'dimension':len(basis),'active_ports':ports,
            'basis':[[v.encoded() for v in row] for row in basis],
            'gram_diagonal':[v.encoded() for v in norms],
            'generator':[[v.encoded() for v in row] for row in smallK],**audit})
    counts={r['sector']:len(r['brackets']) for r in reports}
    check('sector_bound_counts_sum_to_five',sum(counts.values())==5)
    check('each_sector_root_simple_and_port_visible',all(b['simple_root_count']==1 and b['all_active_port_overlaps_nonzero'] for r in reports for b in r['brackets']))
    ordered_intervals=sorted((Q(b['energy_interval'][0]),Q(b['energy_interval'][1])) for r in reports for b in r['brackets'])
    distinct=all(a[1]<b[0] for a,b in zip(ordered_intervals,ordered_intervals[1:]))
    check('five_certified_energy_intervals_are_disjoint',distinct)
    # Negative energies are excluded by the positive total energy form. Also
    # check the below-band secular sign at explicit decaying-sheet controls.
    below=[]
    for r in (Q(1,2),Q(1,4)):
        E=2-r-1/r
        gram=[[metric[i]*((F(E) if i==j else F())-K[i][j]-(F(1-r) if i==j and i<3 else F())) for j in range(11)] for i in range(11)]
        below.append(inertia(gram)==(0,11,0))
    check('below_band_secular_controls_strictly_negative',all(below))
    # K has one zero mode, but its nonzero constant lead tails are not square
    # summable. A central null vector alone is not a bound state of the leads.
    ground=null_vector(K);port_norm=sum((metric[j]*ground[j]*ground[j] for j in range(3)),F())
    check('zero_threshold_mode_has_nonzero_lead_tails',port_norm.positive())
    check('upper_threshold_not_a_secular_root',full_top[2]==0)
    # Incoming scattering cannot populate these bound states in a stationary
    # autonomous model; initially central states can already overlap them.
    check('belt_input_orthogonal_to_entire_antisymmetric_block',all(inner(e0,v,metric)==0 for v in sectors[1][1]))
    check('carrier_inputs_split_into_plus_minus_blocks',all(e1[i]==Q(1,2)*(plus[i]+minus[i]) and e2[i]==Q(1,2)*(plus[i]-minus[i]) for i in range(11)))
    # Optional exact threshold reflection: it is a limit, not a finite-flux
    # scattering assignment at E=0.
    limit=[[F(int(i==j))-2*ground[i]*metric[j]*ground[j]/port_norm for j in range(3)] for i in range(3)]
    check('zero_threshold_limit_is_metric_unitary',all(sum((limit[k][i]*metric[k]*limit[k][j] for k in range(3)),F())==(metric[i] if i==j else 0) for i in range(3) for j in range(3)))
    probabilities=[[metric[i]/metric[j]*limit[i][j]*limit[i][j] for j in range(3)] for i in range(3)]
    check('zero_threshold_limit_probabilities_normalized',all(sum((probabilities[i][j] for i in range(3)),F())==1 for j in range(3)))
    result={'verification_passed':all(checks.values()),'checks':checks,'continuum_band':['0','4'],
        'total_above_band_bound_modes':5,'sector_bound_counts':counts,
        'all_five_energy_brackets_disjoint':distinct,
        'full_upper_threshold_inertia':list(full_top),'full_upper_cutoff_inertia':list(full_high),
        'secular_equation':'[E I-K-(1+r)P]u=0, E=2+r+1/r, 0<r<1',
        'tail':'psi_j,n=(-r)^n u_j',
        'full_bound_norm':'u* H u + [r^2/(1-r^2)] sum_j h_j |u_j|^2',
        'root_count_method':'Strict Loewner monotonicity in E and exact inertia; no numerical root cutoff or finite lead approximation.',
        'sector_reports':reports,
        'preparation_overlap_counts':{'native_belt_character':counts['symmetric'],'carrier_sum':counts['symmetric'],'carrier_difference':counts['antisymmetric'],'proton_port':5,'electron_port':5},
        'zero_threshold':{'central_null_vector':[v.encoded() for v in ground],'port_norm':port_norm.encoded(),
            'disposition':'bounded constant-tail resonance, not a square-summable bound state',
            'limiting_S':[[v.encoded() for v in row] for row in limit],
            'limiting_probabilities':[[v.encoded() for v in row] for row in probabilities]},
        'qualifications':['Nonzero overlap is certified; numerical retained probability weights have not been computed.',
            'These are high-energy localized modes above a declared finite-band lead continuum, not negative-energy binding below the vacuum.',
            'Stationary incoming propagating states and initially localized central states are different preparations.',
            'Complete-channel asymptotic wave packets, full spinor coupling and the multi-object photon dictionary remain open.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (scattering_path,joint_path,Path(__file__),BASE/'checkers/check_native_adapter_collective_closure.py')}}
    (BASE/'results/native_port_bound_spectrum.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'bound_counts':counts,
        'energies':{r['sector']:[b['energy_midpoint_decimal'] for b in r['brackets']] for r in reports},
        'preparation_overlap_counts':result['preparation_overlap_counts']},indent=2))

if __name__=='__main__':main()
