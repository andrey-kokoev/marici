"""Separate source-native projective rival, not a repaired faithful quotient."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as cartesian
import json
from pathlib import Path
from check_port_incidence_conjectures import (
    ROOT, ZERO, ONE, A, read_operator, product, transpose, factor,
    identity, integer_trace, encode, digest, pivot_columns, serial)
from assemble_metric_coefficient_protocol import decode, plus, scaled

CONTRACT=ROOT/'research/strominger/contracts/port-incidence-small-family.v1.json'
RESULT=ROOT/'research/strominger/results/port-incidence-small-family-v1.json'


def parse(rows):
    return {(r['target'],r['source']):decode(r['coefficient']) for r in rows}


def main():
    contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
    prior_path=ROOT/contract['prerequisite_receipt']
    prior=json.loads(prior_path.read_text(encoding='utf-8'))
    assert prior['status']=='pass' and all(prior['checks'].values())
    pins=dict(prior['source_sha256'])
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite'
    for p in (CONTRACT,prior_path,Path(__file__).resolve()):
        pins[p.relative_to(ROOT).as_posix()]=digest(p)
    checks={};carriers={}
    for name,stage in (('proton','G'),('neutron','L')):
        old=prior['native_stage_interfaces'][name]
        source=json.loads((ROOT/old['native_source']).read_text(encoding='utf-8'))
        n=old['raw_coordinates']
        P=read_operator(source['operators'][stage],n)
        N=read_operator(source['operators']['N'],n)
        assert product(P,N)==product(N,P)==N
        objects={}
        for key,source_stage in (('three',stage),('one','N')):
            f=old['factors'][source_stage]
            objects[key]={k:parse(f[k]) for k in ('encoder','decoder','metric')}
            objects[key]['rank']=f['rank']
            assert product(objects[key]['decoder'],objects[key]['encoder'])==identity(f['rank'])
        assert [objects[k]['rank'] for k in ('three','one')]==[3,1]
        maps={};rows=[]
        for source_key,target in cartesian(('three','one'),repeat=2):
            a,b=objects[source_key],objects[target]
            T=product(b['decoder'],product(N,a['encoder']))
            maps[target,source_key]=T
            assert product(b['encoder'],T)==product(N,a['encoder'])
            assert product(b['encoder'],product(T,a['decoder']))==N
            r=len(pivot_columns(T,b['rank'],a['rank']))
            assert r==1
            assert len(T)==a['rank']*b['rank']
            rows.append({'input_channels':a['rank'],'output_channels':b['rank'],
                'support':len(T),'rank':r,'matrix':encode(T)})
        assert [[r['input_channels'],r['output_channels']] for r in rows]==contract['construction']['predicted_shapes']
        assert [r['support'] for r in rows]==contract['construction']['predicted_nonzero_supports']
        for c,b,a in cartesian(('three','one'),repeat=3):
            assert product(maps[c,b],maps[b,a])==maps[c,a]
        for (b,a),T in maps.items():
            assert product(transpose(T,True),objects[b]['metric'])==product(objects[a]['metric'],maps[a,b])
        assert maps['one','one']==identity(1)
        assert maps['three','three']!=identity(3)
        Q=plus(P,scaled(-ONE,N))
        assert integer_trace(Q)==2 and product(Q,Q)==Q
        assert not product(N,Q) and product(P,Q)==Q
        D1=objects['one']['decoder']
        assert not product(D1,Q)
        j=min(j for i,j in Q)
        column={(i,0):x for (i,k),x in Q.items() if k==j}
        assert column and not product(D1,column) and product(P,column)==column
        reader=min(i for i,k in column)
        carriers[name]={'three_channel_source_stage':stage,'interfaces':rows,
            'composition_triples':8,'metric_adjoint_equations':4,
            'identities':'F11=I1; F33 is a rank-one projector, not I3. This is a projective protocol, not reversible transport on all three channels.',
            'full_three_channel_recovery':False,
            'kernel_hostile':{'source_column':j,'rank_P3_minus_N':2,
                'raw_state':encode(column),'one_channel_readout':'zero, equal to zero input',
                'three_channel_reader_coordinate':reader,'reader_value':column[reader,0].record()},
            'main_codimension_attachment':None}
        checks[name+'_all_four_shapes_supports_ranks_and_raw_recoveries']=True
        checks[name+'_all_eight_compositions_and_four_metric_adjoint_equations']=True
        checks[name+'_rank_two_kernel_refutes_full_three_channel_recovery']=True
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.port-incidence-small-family-check.v1','status':'pass','checks':checks,
        'carriers':carriers,'source_sha256':pins,
        'resolution':'All four3/1 native projective interfaces constructed for both baryon fixtures. They are not faithful quotients or reversible three-channel connections.',
        'geometric_or_physical_species_assignment':False,'native_producers_executed':False,'formal_proof_recompiled':False}
    RESULT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','checks':len(checks),'supports':[9,3,3,1],
        'rank_each':1,'composition_triples_per_carrier':8,'full_three_channel_recovery':False},indent=2))


if __name__=='__main__':
    main()
