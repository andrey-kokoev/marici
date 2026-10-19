"""C5: fresh exact preparation-sector/cofactor checks for the analytic retention limit."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3];HOME=ROOT/'research/scattering/low-energy';OWNER=ROOT/'research/voevodsky'
sys.path.insert(0,str(OWNER/'checkers'))
from check_native_adapter_collective_closure import F,closure,orthogonalize,restricted,inner,unit,apply
from check_native_port_bound_spectrum import inertia,secular_gram,sparse
from check_three_port_completeness import audit as completeness_audit
PROOF=HOME/'BOUND-RETENTION-PROOF.md';RESULT=HOME/'results/bound-retention.v1.json'


def audit():
    complete=completeness_audit()
    assert complete==json.loads((HOME/'results/three-port-completeness.v1.json').read_text(encoding='utf-8'))
    source=json.loads((OWNER/'results/native_joint_generator_resolvent.json').read_text(encoding='utf-8'))
    reported=json.loads((OWNER/'results/native_port_bound_spectrum.json').read_text(encoding='utf-8'))
    K=[[F(*x) for x in row] for row in source['joint_generator']];h=[F(*x) for x in source['gram_diagonal']]
    P=[[F(int(i==j and i<3)) for j in range(11)] for i in range(11)]
    rational=sparse([[F(x.a) for x in row] for row in K]);radical=sparse([[F(x.b) for x in row] for row in K])
    e0,e1,e2=[unit(11,i) for i in range(3)]
    plus=[a+b for a,b in zip(e1,e2)];minus=[a-b for a,b in zip(e1,e2)]
    sectors=[];records=[];counts={}
    for label,seeds,dimension,nports in [('symmetric',[e0,plus],5,2),('antisymmetric',[minus],6,1)]:
        span=closure(seeds,{'rational':rational,'radical':radical},11);assert len(span.rows)==dimension
        basis,norms=orthogonalize(span.rows,h)
        smallK=restricted(sparse(K),basis,h,norms);smallP=restricted(sparse(P),basis,h,norms)
        assert all(smallP[i][j]==int(i==j and i<nports) for i in range(dimension) for j in range(dimension))
        for A,small in ((K,smallK),(P,smallP)):
            for j,b in enumerate(basis):
                image=apply(sparse(A),b)
                reconstructed=[sum((basis[i][k]*small[i][j] for i in range(dimension)),F()) for k in range(11)]
                assert image==reconstructed
        # The first orthogonalized basis vectors are the named preparations.
        assert basis[0]==seeds[0]
        if nports==2:assert basis[1]==seeds[1]
        candidates=next(r for r in reported['sector_reports'] if r['sector']==label)['brackets']
        for candidate in candidates:
            ends=list(map(Q,candidate['decay_interval']));full=[inertia(secular_gram(smallK,norms,nports,r)) for r in ends]
            assert full[0][2]==full[1][2]==0 and full[1][1]-full[0][1]==1
            minors=[]
            for port in range(nports):
                pair=[]
                for r in ends:
                    A=secular_gram(smallK,norms,nports,r)
                    pair.append(inertia([[A[i][j] for j in range(dimension) if j!=port] for i in range(dimension) if i!=port]))
                assert pair[0]==pair[1] and pair[0][2]==0
                minors.append({'port':port,'endpoint_inertias':[list(x) for x in pair]})
            records.append({'sector':label,'decay_interval':candidate['decay_interval'],'full_endpoint_inertias':[list(x) for x in full],'active_port_minors':minors})
        counts[label]=len(candidates);sectors.append(basis)
    assert counts=={'symmetric':2,'antisymmetric':3}
    assert all(inner(a,b,h)==0 for a in sectors[0] for b in sectors[1])
    assert len(sectors[0])+len(sectors[1])==11
    for i in range(11):assert e1[i]==(plus[i]+minus[i])*Q(1,2) and e2[i]==(plus[i]-minus[i])*Q(1,2)
    paths=set(complete['source_sha256'])|{PROOF.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),'research/scattering/low-energy/results/three-port-completeness.v1.json'}
    return {'schema':'marici.scattering.bound-retention.v1','status':'pass','C5_disposition':'established',
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)},
            'sector_dimensions':[5,6],'actual_K_and_P_invariance_verified':True,'fresh_bracket_and_minor_checks':records,
            'preparation_overlap_counts':{'belt':2,'carrier_sum':2,'carrier_difference':3,'proton_port':5,'electron_port':5},
            'retention_identity':'lim_R lim_T (1/T) integral_0^T ||P_R exp(-itH)psi||² dt = ||P_b psi||² > 0 for every named normalized preparation',
            'escaping_squared_norm':'1-||P_b psi||²','numerical_retained_fraction_claimed':False,
            'instantaneous_central_limit_claimed':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C5 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C5 exact overlap counts 2/2/3/5/5; ordered-limit retention proof supplied.')


if __name__=='__main__':main()
