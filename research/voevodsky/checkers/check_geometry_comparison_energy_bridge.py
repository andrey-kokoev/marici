"""Map retained comparison slots to actual proton transfers and belt supports.

The comparison-to-proton map uses the retained root A, reference AB, and signed
monomial transport charts. The belt support transpose uses the recorded local
coordinate order, not an assertion of geometric or coefficient equivalence.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
from hashlib import sha256
import json
from check_reversed_coefficient_attachment import SOURCE, verify, weight
from check_belt_three_by_twelve import decode
from check_coupled_six_piece_belt import norm

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent.parent


def main():
    raw = SOURCE.read_bytes()
    packet = json.loads(raw)
    certificate, arrows = verify(packet)
    assert certificate['verified'] and certificate['full_return_operator_verified']
    objects = packet['objects']
    geometry = objects[objects[packet['root']]['geometry']]['payload']
    vertices = 'ABCD'
    remaining = 'BCD'
    edges = [''.join(e) for e in product(vertices,repeat=2) if e[0] != e[1]]
    index = {e:i for i,e in enumerate(edges)}
    rotation = {r['outer_arrow']:tuple(tuple(F(x) for x in row) for row in r['rotation'])
                for r in geometry['triangles_and_transports']}
    points = {'A':(1,1,1),'B':(1,-1,-1),'C':(-1,1,-1),'D':(-1,-1,1)}
    # Each nonroot vertex determines a coordinate axis by its opposite-edge
    # midpoint direction from the tetrahedron center; B,C,D give x,y,z.
    for axis,v in enumerate(remaining):
        assert tuple(F(x+y,2) for x,y in zip(points['A'],points[v])) == tuple(int(i==axis) for i in range(3))
    charts = {}
    for e,r in rotation.items():
        charts[e] = []
        for a in range(3):
            nonzero = [(i,r[i][a]) for i in range(3) if r[i][a]]
            assert len(nonzero) == 1 and abs(nonzero[0][1]) == 1
            charts[e].append(nonzero[0])
    typed = {(tuple(a['source']),tuple(a['target'])):a for a in arrows}
    assert len(typed) == 1836
    phase_pairs = {'L':('raw','local'),'G':('local','aligned'),'N':('aligned','raw')}
    def key(stage,target,ta,source,sa):
        p,q = phase_pairs[stage]
        return ((p,source,'xyz'[charts[source][sa][0]]),(q,target,'xyz'[charts[target][ta][0]]))
    records = []
    for outer in edges:
        for a,b in product(remaining,repeat=2):
            ta,sa = remaining.index(a),remaining.index(b)
            records.append(({'outer':outer,'kind':'state','left':a,'right':b},'L',outer,ta,outer,sa))
        for source,inner in product(edges,repeat=2):
            if inner[0] == 'A':
                a = remaining.index(inner[1])
                records.append(({'outer':outer,'kind':'arrow','left':source,'right':inner},'G',outer,a,source,a))
            else:
                a = remaining.index(inner[0])
                b = a if inner[1] == 'A' else remaining.index(inner[1])
                records.append(({'outer':outer,'kind':'arrow','left':source,'right':inner},'N',outer,a,source,b))
    assert len(records) == 1836
    keys = [key(stage,t,a,s,b) for _,stage,t,a,s,b in records]
    assert len(set(keys)) == 1836 and set(keys) == set(typed)
    assert Counter(stage for _,stage,*_ in records) == {'L':108,'G':432,'N':1296}
    # Reverse the map from actual typed ports and transport-chart axes.
    def inverse(source,target):
        stage = next(s for s,pair in phase_pairs.items() if pair==(source[0],target[0]))
        t,s = target[1],source[1]
        a = next(j for j,(i,_) in enumerate(charts[t]) if 'xyz'[i]==target[2])
        b = next(j for j,(i,_) in enumerate(charts[s]) if 'xyz'[i]==source[2])
        if stage == 'L':
            assert s == t
            return {'outer':t,'kind':'state','left':remaining[a],'right':remaining[b]}
        if stage == 'G':
            assert a == b
            inner = 'A'+remaining[a]
        else:
            inner = remaining[a]+('A' if a==b else remaining[b])
        return {'outer':t,'kind':'arrow','left':s,'right':inner}
    for record,k in zip(records,keys):
        assert inverse(*k) == record[0]
    # Stage-local ports preserve the actual endpoint ownership and coefficient;
    # no weight is inferred from a comparison label alone.
    belt_path = BASE/'results/belt_three_by_twelve_store.json'
    belt_raw = belt_path.read_bytes()
    belt = json.loads(belt_raw)
    belt_rows = {(a['stage'],a['source'],a['target']):a for a in belt['arrows']}
    assert len(belt_rows) == 1836
    swapped = {'L':'G','G':'L','N':'N'}
    # L/G exchange reverses the three-stage cycle: no covariant stage-port
    # map exists. Reversing each arrow gives one consistent contravariant map.
    phases = ('raw','local','aligned')
    direct, reverse = [], []
    for perm in permutations(phases):
        f = dict(zip(phases,perm))
        if all(tuple(f[x] for x in phase_pairs[s]) == phase_pairs[swapped[s]] for s in swapped):
            direct.append(f)
        if all(tuple(f[x] for x in reversed(phase_pairs[s])) == phase_pairs[swapped[s]] for s in swapped):
            reverse.append(f)
    assert not direct and reverse == [{'raw':'aligned','local':'local','aligned':'raw'}]
    port_phase = reverse[0]
    bridge = []
    for record,k in zip(records,keys):
        slot,stage,t,a,s,b = record
        bs,bt = a*12+index[t],b*12+index[s]
        assert (port_phase[k[1][0]],port_phase[k[0][0]]) == phase_pairs[swapped[stage]]
        bk = (swapped[stage],bs,bt)
        assert bk in belt_rows
        row = typed[k]
        bridge.append({'slot':slot,'proton':row,'proton_stage':stage,
                       'co_moving_signs':{'source':int(charts[s][b][1]),'target':int(charts[t][a][1])},
                       'belt':belt_rows[bk]})
    assert len({(b['belt']['stage'],b['belt']['source'],b['belt']['target']) for b in bridge}) == 1836
    counts = {'proton':dict(Counter(b['proton_stage'] for b in bridge)),
              'belt':dict(Counter(b['belt']['stage'] for b in bridge))}
    assert counts['belt'] == {'L':432,'G':108,'N':1296}
    # An explicit coefficient mismatch proves this support transpose is not a
    # coefficient intertwiner. Proton G diagonal=1/12; belt L is nonuniform.
    d = [F(c['d']) for c in belt['coordinates']]
    belt_diag = []
    for i in range(36):
        value = decode(belt_rows['L',i,i]['numerator'])[0]/d[i]
        assert value.b == 0
        belt_diag.append(value.a)
    assert any(x != F(1,12) for x in belt_diag)
    assert len(set(belt_diag[:12])) > 1
    mismatched = next(b for b in bridge if b['proton_stage']=='G' and b['proton']['source'][1:]==b['proton']['target'][1:] and belt_diag[b['belt']['source']] != F(1,12))
    assert weight(mismatched['proton']) == (F(1,12),F(0))
    # Coefficient-quadratic energies are a distinct, fully evaluated control.
    proton_norms = {s:F(0) for s in phase_pairs}
    for b in bridge:
        re,im = weight(b['proton'])
        proton_norms[b['proton_stage']] += re*re+3*im*im
    belt_norms = {s:F(0) for s in phase_pairs}
    for row in belt['arrows']:
        value = norm(decode(row['numerator']))/(d[row['source']]*d[row['target']])
        assert value.b == 0
        belt_norms[row['stage']] += value.a
    assert proton_norms == {'L':12,'G':3,'N':1}
    assert belt_norms == {'L':3,'G':12,'N':1}
    # Frozen-sector dressed-channel energy: each actual stage has one common
    # gap, all slots occupied. Check arbitrary rational gaps without fitting.
    trials = []
    for gaps in [(F(1),F(1),F(1)),(F(101,100),F(1),F(1)),(F(1),F(101,100),F(1))]:
        energies = {name:sum(F(c[s])*gap for s,gap in zip(('L','G','N'),gaps)) for name,c in counts.items()}
        assert energies['belt']-energies['proton'] == 324*(gaps[0]-gaps[1])
        quadratic = {name:sum(c[s]*gap for s,gap in zip(('L','G','N'),gaps)) for name,c in [('proton',proton_norms),('belt',belt_norms)]}
        assert quadratic['belt']-quadratic['proton'] == 9*(gaps[1]-gaps[0])
        trials.append({'gaps':list(map(str,gaps)),'stored_channel_energies':{k:str(v) for k,v in energies.items()},'coefficient_quadratic_energies':{k:str(v) for k,v in quadratic.items()}})
    # Pulling a cost through the support bijection preserves total energy.
    # Keeping the physical stage cost fixed instead compares different roles.
    assert sum(counts['proton'][s]*g for s,g in zip(('L','G','N'),(2,3,5))) == sum(counts['belt'][swapped[s]]*g for s,g in zip(('L','G','N'),(2,3,5)))
    report = {'verification_passed':True,'comparison_slots':1836,'proton_transfers_replayed':1836,'inverse_map_checked':True,
              'counts':counts,'root':'A','reference_transport':'AB','stage_role_transpose':swapped,'support_map_variance':'contravariant: reverse arrows and transpose coordinates',
              'stage_port_map':port_phase,'covariant_stage_role_swap_bridge_exists':False,
              'support_transpose_is_coefficient_intertwiner':False,
              'coefficient_mismatch_witness':{'proton_arrow':mismatched['proton'],'belt_arrow':mismatched['belt'],
                  'proton_diagonal':'1/12','belt_diagonal':str(belt_diag[mismatched['belt']['source']])},
              'proton_coefficient_squared_sums':{k:str(v) for k,v in proton_norms.items()},
              'belt_coefficient_squared_sums':{k:str(v) for k,v in belt_norms.items()},
              'stored_channel_energy_difference':'324*(Delta_L-Delta_G)',
              'coefficient_quadratic_difference':'9*(gamma_G-gamma_L)',
              'trial_energies':trials,'mass_difference_predicted':False,
              'source_sha256':{'proton':sha256(raw).hexdigest(),'belt':sha256(belt_raw).hexdigest()},
              'next_gate':'Select stored-channel versus coherent coefficient energy from the retained dynamics, then derive stage costs and particle-sector readouts.'}
    (BASE/'results/geometry_comparison_energy_bridge.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/geometry_comparison_energy_bridge_store.json').write_text(json.dumps({'source_sha256':report['source_sha256'],'edge_order':edges,'belt_coordinate_order':belt['coordinates'],'records':bridge},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
