"""Audit fixed-address C3 covariance, then verify a retained moving-frame binding.

No source feature, native metric or pulse Hamiltonian is changed. The moving
frame is an explicit three-valued control record, not a physical clock.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
from collections import Counter
import hashlib,json
from check_neutron_canonical_record_binding import ROOT,dot,vadd,vscale,scalar
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,total,encoded
from check_belt_three_by_twelve import decode
from assemble_relative_geometry import apply
from check_belt_operator_inputs import frame,action,mode


def main():
    paths={k:ROOT/p for k,p in {
        'binding':'research/strominger/results/neutron-canonical-record-binding.json',
        'geometry':'research/voevodsky/results/four_six_center_cones.json',
        'native':'research/voevodsky/results/belt_three_by_twelve_store.json',
        'ambient':'research/voevodsky/results/coupled_six_piece_belt_store.json',
        'rotation':'research/voevodsky/inputs/mode-neutron.json'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items()};binding=data['binding'];checks={}
    assert binding['status']=='passed'
    for p,h in binding['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    ambient=data['ambient'];native=data['native'];geo=data['geometry'];source=data['rotation']
    assert native['source_root']==ambient['root']
    assert hashlib.sha256(paths['geometry'].read_bytes()).hexdigest()==ambient['record']['geometry_sha256']
    checks['fresh_binding_native_geometry_and_rotation']=True
    triangles=[tuple(t) for t in ambient['record']['triangles']];tri_index={t:i for i,t in enumerate(triangles)}
    points={k:tuple(map(F,v)) for k,v in geo['belt_scaled_coordinates'].items()}
    for face in geo['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum(points[v][a] for v in face)/3 for a in range(3))
    inverse_points={v:k for k,v in points.items()}
    g=source['generators'][0];rotation=(tuple(tuple(map(F,row)) for row in g['matrix']),tuple(map(F,g['translation'])))
    rename={k:inverse_points[apply(rotation,v)] for k,v in points.items()}
    tri_perm=[tri_index[tuple(rename[k] for k in t)] for t in triangles]
    # Derive the Cartesian-frame permutation from the actual supplied source
    # rotation, then check every native mode, not merely its triangle labels.
    rotations=[]
    for perm in permutations(range(3)):
        matrix=tuple(tuple(F(j==perm[i]) for j in range(3)) for i in range(3))
        if all(action(matrix,frame(v))==frame(apply(rotation,v)) for v in points.values()):rotations.append(matrix)
    assert len(rotations)==1;cartesian_rotation=rotations[0]
    for i,t in enumerate(triangles):
        re,im=mode(t,points);target_re,target_im=mode(triangles[tri_perm[i]],points)
        assert action(cartesian_rotation,re)==target_re and action(cartesian_rotation,im)==target_im
    coordinates=native['coordinates'];lookup={(c['triangle'],c['axis']):i for i,c in enumerate(coordinates)}
    permutation=[lookup[tri_perm[c['triangle']],c['axis']] for c in coordinates]
    for i,j in enumerate(permutation):
        assert coordinates[i]['d']==coordinates[j]['d']
        assert coordinates[i]['selected_numerator']==coordinates[j]['selected_numerator']
        assert permutation[permutation[j]]==i
    assert permutation!=list(range(36))
    checks['actual_source_rotation_transports_all_18_native_modes']=True
    ports=binding['source_label_to_native_port'];labels=[p['label'] for p in ports];by_triangle={p['triangle_index']:i for i,p in enumerate(ports)}
    port_perm=[by_triangle[tri_perm[p['triangle_index']]] for p in ports]
    assert all(port_perm[port_perm[port_perm[i]]]==i and port_perm[i]!=i for i in range(6))
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    H=[[G[i//4][j//4]*G[i%4][j%4] for j in range(16)] for i in range(16)]
    slots=[p['source_record_feature_slot'] for p in ports]
    D=[[H[a][b]/121 for b in slots] for a in slots]
    def preserves(perm):return all(D[i][j]==D[perm[i]][perm[j]] for i in range(6) for j in range(6))
    autos=[p for p in permutations(range(6)) if preserves(p)]
    def order(p):
        q=list(range(6));k=0
        while True:
            q=[p[i] for i in q];k+=1
            if q==list(range(6)):return k
    orders=Counter(order(p) for p in autos)
    assert len(autos)==8 and not any(order(p)==3 for p in autos)
    assert not preserves(port_perm)
    witness=next((i,j) for i in range(6) for j in range(6) if D[i][j]!=D[port_perm[i]][port_perm[j]])
    # For any fixed bijection of ports to modes the induced action is conjugate
    # to this fixed-point-free order-three permutation. Test all 720 bijections.
    for assignment in permutations(range(6)):
        inv=[assignment.index(i) for i in range(6)]
        conjugated=[inv[port_perm[assignment[i]]] for i in range(6)]
        assert order(conjugated)==3 and not preserves(conjugated)
    checks['all_720_static_bijections_fail_source_Gram_covariance']=True
    checks['phases_cannot_repair_unequal_overlap_magnitudes']=True
    nu=F(binding['rim_mode_squared_norm']);weights=[1/(nu*F(c['d'])) for c in coordinates]
    modes={p['label']:[Z]*36 for p in ports}
    for p in ports:
        for entry in p['native_support']:modes[p['label']][entry['index']]=decode(entry['numerator'])
    features={p['label']:[(R(F(i==p['source_record_feature_slot'],11)),R()) for i in range(16)] for p in ports}
    def rotate(state,t=1):
        out=list(state)
        for _ in range(t%3):
            nxt=[Z]*36+out[36:]
            for i,j in enumerate(permutation):nxt[j]=out[i]
            out=nxt
        return out
    def inner(a,b):
        bank=total(scale(H[i][j],mul(conj(a[36+i]),b[36+j])) for i in range(16) for j in range(16) if a[36+i]!=Z and b[36+j]!=Z)
        return add(dot(a[:36],b[:36],weights),bank)
    directions={(label,t):rotate(modes[label]+vscale((R(-1),R()),features[label]),t) for label in labels for t in range(3)}
    def projector(label,t,state):
        direction=directions[label,t]
        return vscale(scale(F(1,2),inner(direction,state)),direction)
    def pulse(label,t,state,phase=(R(-1),R())):
        return vadd(state,vscale(add(phase,scale(-1,ONE)),projector(label,t,state)))
    def energy(label,t,state):return scalar(norm(inner(directions[label,t],state)))/2
    def budget(state):return scalar(inner(state,state)[0])
    for t in range(3):
        for i,a in enumerate(labels):
            for j,b in enumerate(labels):assert inner(directions[a,t],directions[b,t])==(R(D[i][j]+F(i==j)),R())
    checks['unchanged_source_direction_Gram_in_all_three_frames']=True
    phase=(R(F(-1,2)),R(F(-1,2)))
    for j in range(52):
        state=[ONE if i==j else Z for i in range(52)]
        assert rotate(state,3)==state and budget(rotate(state))==budget(state)
        for t in range(3):
            for label in labels:
                # Projector covariance proves the identity for every angle.
                assert projector(label,(t+1)%3,rotate(state))==rotate(projector(label,t,state))
                assert energy(label,(t+1)%3,rotate(state))==energy(label,t,state)
                after=pulse(label,t,state,phase)
                assert budget(after)==budget(state) and pulse(label,t,after,conj(phase))==state
    checks['all_angle_projector_covariance_on_full_52D_target']=True
    checks['moving_frame_energy_metric_and_inverse_preserved']=True
    # Three-valued frame advances alongside the actual native rotation. Source
    # bank does not rotate. Full occurrence history remains separately retained.
    state=modes['AB']+[Z]*16;initial=list(state);reference=list(state);t=0;history=[]
    endpoints={p['label']:p['source_endpoints'] for p in ports};word=['AB','BA']*3
    assert all(endpoints[a][1]==endpoints[b][0] for a,b in zip(word,word[1:]))
    def snapshot(v):return [encoded(x) for x in v]
    for serial,label in enumerate(word):
        before=list(state);active_triangle=ports[labels.index(label)]['triangle_index']
        for _ in range(t):active_triangle=tri_perm[active_triangle]
        e=energy(label,t,before);after_pulse=pulse(label,t,before)
        state=rotate(after_pulse);reference=pulse(label,0,reference)
        history.append({'occurrence':serial,'label':label,'source_endpoints':endpoints[label],
                        'frame_before':t,'frame_after':(t+1)%3,'actual_native_triangle':list(triangles[active_triangle]),
                        'pulse_energy':str(e),'before':snapshot(before),'after_pulse':snapshot(after_pulse),'after_rotation':snapshot(state)})
        t=(t+1)%3
        assert state==rotate(reference,t) and budget(state)==1
    assert t==0 and state!=initial # No false endpoint reset from frame recurrence.
    for event in reversed(history):
        state=rotate(state,2);assert snapshot(state)==event['after_pulse']
        state=pulse(event['label'],event['frame_before'],state);assert snapshot(state)==event['before']
        t=event['frame_before']
    assert state==initial and t==0
    checks['six_typed_occurrences_with_rotation_recovered_exactly']=True
    checks['frame_recurrence_does_not_erase_source_history']=True
    # The native coherent mode is fixed by C3. Its previously evaluated empty-
    # bank pulse energy is therefore frame-independent, with no retuning.
    coherent=[decode(c['selected_numerator']) for c in coordinates]+[Z]*16
    assert rotate(coherent)==coherent
    old_energy=F(binding['unit_coherent_neutron_empty_record_bank']['each_port_energy'])
    assert all(energy(label,t,coherent)/budget(coherent)==old_energy for label in labels for t in range(3))
    checks['coherent_neutron_pulse_energy_unchanged_in_every_frame']=True
    i,j=witness
    result={'status':'passed','checks':checks,'native_vertex_rotation':rename,'native_coordinate_permutation':permutation,
            'native_port_permutation':{labels[i]:labels[port_perm[i]] for i in range(6)},
            'static_address_obstruction':{'source_Gram_automorphism_count':len(autos),'automorphism_order_counts':dict(orders),
                'all_static_bijections_checked':720,
                'witness':{'ports':[labels[i],labels[j]],'rotated_ports':[labels[port_perm[i]],labels[port_perm[j]]],
                           'source_overlap':str(D[i][j]),'rotated_overlap':str(D[port_perm[i]][port_perm[j]])},
                'scope':'No static bijection with a unitary source-bank action preserving individual port features, even up to phase. Does not exclude mixing operations or a larger port family.'},
            'moving_binding':{'frame_values':[0,1,2],'state_dimension_complex':52,
                'J_t':'J_t(y,r)=(R_neutron^t sum_i v_i r_i,y)',
                'pulse':'U_i,t=Rhat^t U_i,0 Rhat^-t; Rhat=R_neutron direct-sum I_record',
                'covariance':'U_i,t+1 Rhat=Rhat U_i,t',
                'address_rule':'Rotate the native mode address with the retained frame; do not relabel the source port or rotate the bank feature.',
                'control_scope':'Explicit moving interaction frame. The tested interleaving of pulses and free rotations is supplied, not a derived clock or scheduling law.'},
            'unit_coherent_neutron_each_pulse_energy':str(old_energy),'history':history,
            'next_test':'Determine whether the bound pulse interaction closes on the occupied native neutron sector, retaining all emitted native modes and bank amplitudes rather than applying a lossy return projection.'}
    bound=list(paths.values())+[Path(__file__).resolve(),Path(__file__).with_name('check_neutron_canonical_record_binding.py'),ROOT/'research/voevodsky/checkers/check_belt_operator_inputs.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-canonical-rotation-frame.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'native_port_permutation':result['native_port_permutation'],
                      'static_Gram_automorphisms':len(autos),'automorphism_orders':dict(orders),'all_static_bijections_fail':True,
                      'moving_frame_covariance':'passed for all six projectors on all 52 target basis vectors',
                      'unit_coherent_neutron_each_pulse_energy':str(old_energy)},indent=2))

if __name__=='__main__':main()
