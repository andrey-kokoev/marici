"""Test 5346/3 + 54 structurally, without inserting a target count.
Distinguishes arrow-history orbits from unique coefficient-port pairs.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from collections import Counter
import json
from check_coupled_six_piece_belt import R,Z,add,mul,scale,conj,encoded,verify_operators
from check_belt_operator_inputs import frame,action,mean

BASE=Path(__file__).resolve().parents[1]

def decode(z):
    a,b,c,d=map(Q,z);return (R(a,b),R(c,d))
def canonical(x,p):return min(x,p(x),p(p(x)))
def product(a,b):
    byrow={}
    for (i,j),z in b.items():byrow.setdefault(i,[]).append((j,z))
    out={}
    for (i,k),z in a.items():
        for j,w in byrow.get(k,[]):out[i,j]=add(out.get((i,j),Z),mul(z,w))
    return {k:v for k,v in out.items() if v!=Z}

def main():
    store_path=BASE/'results/coupled_six_piece_belt_store.json';geo_path=BASE/'results/four_six_center_cones.json'
    raw=store_path.read_bytes();packet=json.loads(raw);record=packet['record']
    assert sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()==packet['root']
    geo_raw=geo_path.read_bytes();geometry=json.loads(geo_raw)
    assert sha256(geo_raw).hexdigest()==record['geometry_sha256']
    triangles=list(map(tuple,record['triangles']));index={t:i for i,t in enumerate(triangles)}
    points={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
    for face in geometry['belt_faces']:points['F_'+'_'.join(sorted(face))]=mean([points[k] for k in face])
    coordinates={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coordinates.items()}
    rotation=((Q(0),Q(0),Q(1)),(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)))
    rename={k:inverse[action(rotation,v)] for k,v in coordinates.items()}
    triangle_perm=[index[tuple(rename[k] for k in t)] for t in triangles]
    axis_perm=[next(i for i in range(3) if rotation[i][j]==1) for j in range(3)]
    perm=[3*triangle_perm[i//3]+axis_perm[i%3] for i in range(54)]
    assert sorted(perm)==list(range(54)) and all(perm[perm[perm[i]]]==i and perm[i]!=i for i in range(54))
    classes=sorted({tuple(sorted((i,perm[i],perm[perm[i]]))) for i in range(54)})
    qid={i:q for q,c in enumerate(classes) for i in c};representatives={c[0] for c in classes}
    matrices={s:{} for s in ('L','G','N')}
    for arrow in record['arrows']:
        source,target=arrow['source'],arrow['target'];i=3*target[1]+'xyz'.index(target[2]);j=3*source[1]+'xyz'.index(source[2])
        assert (i,j) not in matrices[arrow['stage']]
        matrices[arrow['stage']][i,j]=decode(arrow['coefficient'])
    u=tuple(decode(z) for z in record['collective_vector'])
    equivariant={s:all(matrix.get((perm[i],perm[j]),Z)==z for (i,j),z in matrix.items()) for s,matrix in matrices.items()}
    assert all(equivariant.values()) and all(u[perm[i]]==u[i] for i in range(54))
    quotient={};history_counts={};histograms={};history_rows=[]
    for stage,matrix in matrices.items():
        edge_action=lambda e:(perm[e[0]],perm[e[1]])
        orbits={canonical(e,edge_action) for e in matrix}
        assert len(orbits)*3==len(matrix)
        multiplicities=Counter((qid[i],qid[j]) for i,j in orbits)
        histograms[stage]=dict(sorted(Counter(multiplicities.values()).items()))
        history_counts[stage]=len(orbits)
        reduced={}
        # Abar is defined by A E = E Abar. Sum over the input port orbit,
        # using one output representative; never count parallel terms as
        # different nonzero entries of a scalar coefficient matrix.
        for (i,j),z in matrix.items():
            if i in representatives:
                e=(qid[i],qid[j]);reduced[e]=add(reduced.get(e,Z),z)
        reduced={e:z for e,z in reduced.items() if z!=Z}
        quotient[stage]=reduced
        for i,j in sorted(orbits):history_rows.append({'stage':stage,'original_representative':[i,j],'quotient_endpoints':[qid[i],qid[j]]})
    qu=tuple(u[c[0]] for c in classes)
    quotient_proof=verify_operators(quotient['L'],quotient['G'],quotient['N'],qu)
    # Derived interface maps. E replicates quotient data to all original
    # ports; Q averages three original ports. Both have 54 nonzero entries.
    ONE=(R(1),R());E={(i,qid[i]):ONE for i in range(54)}
    A={(qid[i],i):(R(Q(1,3)),R()) for i in range(54)}
    identity={(i,i):ONE for i in range(18)}
    assert product(A,E)==identity
    intertwining={s:product(matrix,E)==product(E,quotient[s]) and product(A,matrix)==product(quotient[s],A) for s,matrix in matrices.items()}
    assert all(intertwining.values())
    assert product(product(E,quotient['N']),A)==matrices['N']
    # A competing interpretation cycles the three patches inside every face,
    # retaining axis names. Unlike the spatial rotation, it is not a symmetry.
    family_perm=[3*(3*(i//9)+(i//3+1)%3)+i%3 for i in range(54)]
    family_equivariance={s:all(matrix.get((family_perm[i],family_perm[j]),Z)==z for (i,j),z in matrix.items()) for s,matrix in matrices.items()}
    checks={
        'actual_spatial_C3_is_free_on_all_54_coefficient_ports':len(classes)==18 and all(len(c)==3 for c in classes),
        'all_original_stages_are_exactly_C3_equivariant':all(equivariant.values()),
        'collective_mode_is_C3_invariant':all(u[perm[i]]==u[i] for i in range(54)),
        'spatial_rotation_preserves_not_cycles_the_three_seed_families':all(record['orbit_owners'][triangle_perm[i]]==record['orbit_owners'][i] for i in range(18)),
        'naive_three_seed_patch_cycle_is_not_a_stage_symmetry':not all(family_equivariance.values()),
        'arrow_history_orbits_number_1782':sum(history_counts.values())==1782,
        'parallel_G_and_N_histories_share_quotient_endpoints':histograms=={'L':{1:54},'G':{3:252},'N':{3:324}},
        'unique_quotient_coefficient_support_is_630':quotient_proof['total']==630,
        'quotient_already_has_exact_rank_one_return_and_deletion_certificate':quotient_proof['cycle_trace_sum']=='1' and quotient_proof['all_arrows_covered'],
        'actual_average_and_replication_adapters_each_have_54_transfers':len(A)==len(E)==54,
        'adapters_intertwine_every_stage':all(intertwining.values()),
        'both_adapters_recover_original_complete_return_on_all_inputs':product(product(E,quotient['N']),A)==matrices['N'],
        'one_adapter_total_is_684_not_1836':quotient_proof['total']+len(E)==684,
        'both_adapter_total_is_738_not_1836':quotient_proof['total']+len(E)+len(A)==738,
        'historical_source_packets_unchanged':store_path.read_bytes()==raw and geo_path.read_bytes()==geo_raw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'original_root':packet['root'],'original_support':{s:len(m) for s,m in matrices.items()},
        'arrow_history_orbits':history_counts,'parallel_history_multiplicities':histograms,
        'quotient':quotient_proof,'port_classes':classes,
        'adapter_support':{'average_original_to_quotient':len(A),'replicate_quotient_to_original':len(E)},
        'totals':{'history_orbits':sum(history_counts.values()),'unique_quotient_arrows':quotient_proof['total'],
                  'quotient_with_one_adapter':684,'quotient_with_original_input_and_output':738,
                  'mixed_history_plus_single_adapter_arithmetic':1782+54},
        'candidate_outcome':'The actual threefold symmetry quotient exists, and 54-transfer interface adapters exist. But 1782 counts quotient arrow histories, not unique coefficient pairs. The matching coefficient count is 630, so the proposed 1782+54=1836 mixes accounting conventions.',
        'scope':'Rejects this natural C3 quotient plus adapter route under the existing unique-coefficient counting rule; does not rule out every possible new completion contract.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    artifact={'source_root':packet['root'],'port_classes':classes,'arrow_history_orbits':history_rows,
        'quotient_arrows':[{'stage':s,'target':i,'source':j,'coefficient':encoded(z)} for s,m in quotient.items() for (i,j),z in sorted(m.items())],
        'averaging_arrows':[{'target':i,'source':j,'coefficient':encoded(z)} for (i,j),z in sorted(A.items())],
        'replication_arrows':[{'target':i,'source':j,'coefficient':encoded(z)} for (i,j),z in sorted(E.items())]}
    (BASE/'results/belt_threefold_quotient_store.json').write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/belt_threefold_quotient.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='port_classes'},indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
