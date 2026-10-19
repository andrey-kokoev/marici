"""Source-fixed common-gain/witness child test; coefficient observability, not controllability."""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
import joint_defect_audit as joint
from source_overlap_screen import nullspace
CONTRACT=HOME/'contracts/native-mixed-probe-protocol.v1.json'
RESULT=HOME/'results/native-mixed-probe-sufficiency-v1.json'
PROTOCOL_SHA256='532ed091aaf6b591eae9b35b63c90490be15e8f081dfd4604c47ad4fef59f95a'


def rows(values):return [[v[a][b] for v in values] for a in range(2) for b in range(2)]


def projection(legs,edges,add,scale,zero):
    groups=defaultdict(list)
    for key in legs:
        tag,role,i=key;groups[tag,role,edges[i][1] if tag=='a' else i].append(key)
    out={}
    for keys in groups.values():
        total=zero
        for key in keys:total=add(total,legs[key])
        mean=scale(F(1,len(keys)),total)
        out.update({key:mean for key in keys})
    return out


def validate(c):
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest()==PROTOCOL_SHA256,'prospective protocol drift'
    assert c==json.loads(CONTRACT.read_text(encoding='utf-8')),'substituted protocol semantics'
    assert c['schema']=='marici.native-mixed-probe-protocol.v1'
    assert c['target_preparations_are_licensed_controls'] is False
    assert c['prospective_dimension_bound']=={'structural_joint_rank':55,'polynomial_rows_at_most':12,'augmented_observation_rank_at_most':67,'target_separation_rank':137}
    assert len(c['allowed_operations'])==3
    for path,digest in c['source_sha256'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'source drift: '+path


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    source=joint.source_interfaces();m=source['rung_source']['m'];edges=source['rung_source']['E']
    add,scale,mul=m['add'],m['scale'],m['mul'];zero=scale(F(),m['I'])
    sub=lambda x,y:add(x,scale(-1,y))
    legs={(tag,role,i):m['values'][f'{tag}{role}{i}'] for tag,n in (('a',11),('s',4)) for role in ('x','y') for i in range(n)}
    P=projection(legs,edges,add,scale,zero);Q={k:sub(v,P[k]) for k,v in legs.items()}
    assert projection(P,edges,add,scale,zero)==P
    assert all(v==zero for v in projection(Q,edges,add,scale,zero).values())
    coeff=[[],[],[]]
    for kind,i,j in source['slots']:
        tag='a' if kind=='arrow' else 's';left=(tag,'x',i);right=(tag,'y',j)
        coeff[0].append(sub(mul(P[right],P[left]),source['reference']))
        coeff[1].append(add(mul(P[right],Q[left]),mul(Q[right],P[left])))
        coeff[2].append(mul(Q[right],Q[left]))
    evaluate=lambda q:[add(v0,add(scale(q,v1),scale(q*q,v2))) for v0,v1,v2 in zip(*coeff)]
    def direct(q,values=legs):
        p=projection(values,edges,add,scale,zero)
        values={k:add(p[k],scale(q,sub(v,p[k]))) for k,v in values.items()}
        banks=[[values[tag,role,i] for i in range(n)] for tag,n in (('a',11),('s',4)) for role in ('x','y')]
        return source['boundary_source']['residuals'](*banks,source['reference'])
    for q in (F(),F(1,4),F(1,2),F(3,4),F(1)):assert direct(q)==evaluate(q)
    for a in (F(),F(1,2),F(1)):
        first={k:add(P[k],scale(a,Q[k])) for k in legs}
        for b in (F(),F(1,2),F(1)):assert direct(b,first)==evaluate(a*b)
    # Common S3 conjugation commutes with P; all output entries are already retained.
    witnesses=[]
    for tail in permutations((1,2,3)):
        h=(0,)+tail;rho=tuple(tuple(F((h[j]==i)-(h[3]==i)) for j in (1,2)) for i in (1,2))
        det=rho[0][0]*rho[1][1]-rho[0][1]*rho[1][0]
        inv=((rho[1][1]/det,-rho[0][1]/det),(-rho[1][0]/det,rho[0][0]/det))
        conjugate=lambda v:mul(mul(rho,v),inv)
        moved={k:conjugate(v) for k,v in legs.items()}
        assert conjugate(source['reference'])==source['reference']
        assert projection(moved,edges,add,scale,zero)=={k:conjugate(v) for k,v in P.items()}
        for q in (F(),F(1,2),F(1)):assert direct(q,moved)==[conjugate(v) for v in evaluate(q)]
        witnesses.append((rho,inv))
    poly_rows=sum((rows(values) for values in coeff),[])
    structural=source['assembly']+source['incidence'];observations=structural+poly_rows
    assert joint.rank(structural)==55
    rank=joint.rank(observations);kernel=nullspace(observations)
    assert rank<=67<137 and len(kernel)==137-rank
    v=min(kernel,key=lambda v:(sum(bool(x) for x in v),tuple(v)))
    assert all(x==0 for x in joint.act(observations,v)) and any(v)
    for rho,inv in witnesses:
        for values in coeff:
            moved=[mul(mul(rho,a),inv) for a in values]
            assert all(x==0 for x in joint.act(rows(moved),v))
    # Coefficientwise zero proves blindness for all q, not just these controls.
    for q in (F(),F(1,7),F(1,2),F(1)):
        assert source['boundary_source']['evaluate']({i:x for i,x in enumerate(v) if x},evaluate(q))==zero
    # The target family was frozen independently of the nullspace; select one of its existing coordinates.
    index=next(i for i,x in enumerate(v) if x)
    probe=joint.source_probe(source,source['slots'][index])
    response=source['boundary_source']['evaluate']({i:x for i,x in enumerate(v) if x},probe)
    expected=scale(v[index],mul(source['boundary_source']['K'],source['boundary_source']['H']))
    assert response==expected and response!=zero
    # The whole all-gain row space is attainable with the monotone prefix gains1,1/2,0; no reset.
    samples=structural+rows(evaluate(F(1)))+rows(evaluate(F(1,2)))+rows(evaluate(F()))
    assert joint.rank(samples)==rank
    refused=['replace_conditional_common_gain_by_independent_leg_controls','add_target_reader_after_finding_kernel',
             'identify_137_coefficients_with_548_response_coordinates','infer_observability_from_preparation_Jacobian_rank',
             'promote_the_restricted_protocol_rejection_to_all_native_operations_or_physical_impossibility',
             'close_parent_observation_feedback_gate_from_child_rejection']
    return {'schema':'marici.native-mixed-probe-sufficiency-receipt.v1','status':'pass','candidate_verdict':'rejected',
        'protocol_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'structural_rank':55,'all_gain_and_common_witness_rank':rank,'blind_dimension':137-rank,
        'target_separation_rank':137,'protocol_contains_all_native_operations':False,
        'independent_leg_target_preparations_are_licensed_controls':False,'physical_actuation_or_readout_authorized':False,
        'parent_gate_resolved':False,'formal_outcome_admitted':False,
        'all_gain_proof':'three coefficient matrices vanish exactly; P idempotent and commutes with common witness; gains compose by multiplication',
        'gain_degree':2,'common_witness_controls':len(witnesses),'no_reset_three_record_rank':joint.rank(samples),
        'blind_coefficient_chain':joint.sparse(v),'target_probe_slot':index,'target_probe_source_slot':list(source['slots'][index]),
        'target_probe_response':[[str(x) for x in row] for row in response],
        'hostile_promotions_refused':refused,
        'source_sha256':c['source_sha256']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale mixed-probe receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','candidate_verdict','all_gain_and_common_witness_rank','blind_dimension','parent_gate_resolved')}))

if __name__=='__main__':main()
