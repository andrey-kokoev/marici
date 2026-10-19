"""All ten directed electron five-cycle diagonals under the cycle-isometry rule.

An explicit adapter lists simple directed cycles, maps each to the permutation
fixing other vertices, and retains every resulting generator. Reuses the
existing affine simplex source helper and unchanged geometry/cycle machinery.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
import hashlib
import json
from build_neutrino_seed_candidates import simplex_source
from check_neutrino_arrow_seed_science import rank, group, permutation
from assemble_relative_geometry import assemble, determinant
from evolve_relative_geometry_modes import evolve

ROOT=Path(__file__).resolve().parents[3]


def cycles_of(arrows):
    edges=set(arrows)
    cycles=set()
    for n in range(2,6):
        for c in permutations(range(5),n):
            if all((a,b) in edges for a,b in zip(c,c[1:]+c[:1])):
                cycles.add(min(c[i:]+c[:i] for i in range(n)))
    return sorted(cycles,key=lambda c:(-len(c),c))


def main():
    path=ROOT/'research/voevodsky/inputs/relative-electron.json'
    legacy=json.loads(path.read_text())
    base=[(0,1),(1,2),(2,3),(3,4),(4,0)]
    cases={}
    outputs={}
    for name,extra in [('baseline',[]),('plus_BD',[(1,3)]),('plus_DB',[(3,1)]),
                       ('plus_AD',[(0,3)]),('plus_DA',[(3,0)]),
                       ('plus_AC',[(0,2)]),('plus_CA',[(2,0)]),
                       ('plus_EC',[(4,2)]),('plus_CE',[(2,4)]),
                       ('plus_EB',[(4,1)]),('plus_BE',[(1,4)])]:
        arrows=base+extra
        cycles=cycles_of(arrows)
        source,_=simplex_source(5,[list(c) for c in cycles])
        source['seeds'][0]['role']='attachment_pole'
        assert source['metric']==legacy['metric'] and source['seeds']==legacy['seeds']
        determinants=[str(determinant([[Q(x) for x in row] for row in g['matrix']])) for g in source['generators']]
        incidence=[[int(v==b)-int(v==a) for a,b in arrows] for v in range(5)]
        result={'arrows':[['ABCDE'[a],'ABCDE'[b]] for a,b in arrows],
                'cycles':[''.join('ABCDE'[i] for i in c)+'ABCDE'[c[0]] for c in cycles],
                'source':source,'generator_determinants':determinants,
                'permutation_group_order':len(group(5,[permutation(5,list(c)) for c in cycles])),
                'occurrence_count':len(arrows),'incidence_kernel_dimension':len(arrows)-rank(incidence)}
        try:
            geometry=assemble(source)
            motion=evolve(source)
        except ValueError as error:
            result.update(status='rejected',error=str(error))
        else:
            outputs[name]=(geometry,motion)
            result.update(status='assembled',geometry=geometry,
                          generator_orders=motion['generator_orders'],
                          scheduled_return_steps=motion['scheduled_atomic_steps_to_word_return'],
                          scheduled_word_order=motion['scheduled_word_order'],
                          moving_facets=sum(f['moving_centroid'] for f in motion['facet_states']),
                          fixed_facets=sum(not f['moving_centroid'] for f in motion['facet_states']),
                          recovery=motion['reverse_history_recovers_every_centroid'],
                          cycle=motion)
        cases[name]=result
    checks={
        'baseline_exact_legacy_geometry':outputs['baseline'][0]==assemble(legacy),
        'baseline_exact_legacy_cycle':outputs['baseline'][1]==evolve(legacy),
        'BD_closes_four_cycle':cases['plus_BD']['cycles']==['ABCDEA','ABDEA'],
        'DB_closes_triangle':cases['plus_DB']['cycles']==['ABCDEA','BCDB'],
        'BD_rejected_for_orientation':cases['plus_BD']['status']=='rejected' and cases['plus_BD']['error']=='Generator is not orientation preserving' and cases['plus_BD']['generator_determinants']==['1','-1'],
        'DB_admitted':cases['plus_DB']['status']=='assembled' and cases['plus_DB']['generator_determinants']==['1','1'],
        'DB_same_geometry':outputs['plus_DB'][0]==outputs['baseline'][0],
        'DB_changes_retained_schedule':outputs['plus_DB'][1]['centroid_motion_trace']!=outputs['baseline'][1]['centroid_motion_trace'],
        'DB_recovers_full_centroid_history':cases['plus_DB']['recovery'],
        'both_added_occurrences_retained':cases['plus_BD']['occurrence_count']==cases['plus_DB']['occurrence_count']==6,
        'DB_group_enlarges':cases['baseline']['permutation_group_order']==5 and cases['plus_DB']['permutation_group_order']==60,
    }
    checks.update({
        'AD_closes_triangle':cases['plus_AD']['cycles']==['ABCDEA','ADEA'],
        'DA_closes_four_cycle':cases['plus_DA']['cycles']==['ABCDEA','ABCDA'],
        'AD_admitted':cases['plus_AD']['status']=='assembled' and cases['plus_AD']['generator_determinants']==['1','1'],
        'DA_rejected_for_orientation':cases['plus_DA']['status']=='rejected' and cases['plus_DA']['error']=='Generator is not orientation preserving' and cases['plus_DA']['generator_determinants']==['1','-1'],
        'AD_same_geometry':outputs['plus_AD'][0]==outputs['baseline'][0],
        'AD_same_group_and_period_as_DB':cases['plus_AD']['permutation_group_order']==60 and cases['plus_AD']['scheduled_return_steps']==cases['plus_DB']['scheduled_return_steps']==10,
        'AD_recovers_full_centroid_history':cases['plus_AD']['recovery'],
        'AD_DB_different_labelled_trace':outputs['plus_AD'][1]['centroid_motion_trace']!=outputs['plus_DB'][1]['centroid_motion_trace'],
        'AD_DA_occurrences_retained':cases['plus_AD']['occurrence_count']==cases['plus_DA']['occurrence_count']==6,
    })
    checks.update({
        'AC_closes_four_cycle':cases['plus_AC']['cycles']==['ABCDEA','ACDEA'],
        'CA_closes_triangle':cases['plus_CA']['cycles']==['ABCDEA','ABCA'],
        'AC_rejected_for_orientation':cases['plus_AC']['status']=='rejected' and cases['plus_AC']['error']=='Generator is not orientation preserving' and cases['plus_AC']['generator_determinants']==['1','-1'],
        'CA_admitted':cases['plus_CA']['status']=='assembled' and cases['plus_CA']['generator_determinants']==['1','1'],
        'CA_same_geometry':outputs['plus_CA'][0]==outputs['baseline'][0],
        'CA_group_and_period':cases['plus_CA']['permutation_group_order']==60 and cases['plus_CA']['scheduled_return_steps']==10,
        'CA_recovers_full_centroid_history':cases['plus_CA']['recovery'],
        'CA_distinct_labelled_traces':all(outputs['plus_CA'][1]['centroid_motion_trace']!=outputs[k][1]['centroid_motion_trace'] for k in ('plus_DB','plus_AD')),
        'AC_CA_occurrences_retained':cases['plus_AC']['occurrence_count']==cases['plus_CA']['occurrence_count']==6,
    })
    for edge,cycle,accepted in [('EC','CDEC',True),('CE','ABCEA',False),
                                ('EB','BCDEB',False),('BE','ABEA',True)]:
        key='plus_'+edge
        checks[edge+'_cycle']=cases[key]['cycles']==['ABCDEA',cycle]
        checks[edge+'_occurrence_retained']=cases[key]['occurrence_count']==6
        if accepted:
            checks[edge+'_admitted']=cases[key]['status']=='assembled' and cases[key]['generator_determinants']==['1','1']
            checks[edge+'_geometry']=outputs[key][0]==outputs['baseline'][0]
            checks[edge+'_group_period_recovery']=cases[key]['permutation_group_order']==60 and cases[key]['scheduled_return_steps']==10 and cases[key]['recovery']
        else:
            checks[edge+'_orientation_rejection']=cases[key]['status']=='rejected' and cases[key]['error']=='Generator is not orientation preserving' and cases[key]['generator_determinants']==['1','-1']
            checks[edge+'_permutation_group']=cases[key]['permutation_group_order']==120
    diagonals={(i,j) for i in range(5) for j in range(5) if (j-i)%5 in (2,3)}
    tested={tuple('ABCDE'.index(v) for v in name.removeprefix('plus_')) for name in cases if name!='baseline'}
    checks['all_ten_directed_diagonals_tested']=tested==diagonals
    checks['exactly_five_admitted']=sum(v['status']=='assembled' for k,v in cases.items() if k!='baseline')==5
    # Rejection control: dropping the offending four-cycle would hide the
    # mutation and merely replay baseline. Record that distinction, not a repair.
    checks['dropping_BD_cycle_only_replays_baseline']=assemble(cases['baseline']['source'])==outputs['baseline'][0]
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,
            'conjecture':'Compare all ten directed diagonal additions to the existing electron five-cycle under unchanged shared assembly.',
            'adapter':'All simple directed cycles become permutations fixing unlisted vertices; the original five-cycle is scheduled first. Explicit tested cycle-isometry convention, not an automatic native raw-arrow frontend.',
            'cases':cases,
            'scope':'Full geometric assembly and centroid-cycle measures. No new electron spinor coefficient protocol or photon identity constructed.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,Path(__file__).resolve(),ROOT/'research/strominger/checkers/build_neutrino_seed_candidates.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']}}
    dest=ROOT/'research/strominger/results/electron_diagonal_seeds.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'checks':checks,'cases':{k:{f:v[f] for f in ['status','cycles','generator_determinants','permutation_group_order','scheduled_return_steps','error'] if f in v} for k,v in cases.items()}},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
