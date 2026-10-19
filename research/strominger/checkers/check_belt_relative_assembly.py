"""Co-construct belt/interface records; distinguish three typed boundary lanes."""
from itertools import product, combinations
from collections import defaultdict, deque
from pathlib import Path
import hashlib,json
from check_belt_axial_witness import (ROOT,BASE,F,read,hashes,decode,mv,mm,add,scale,I,prepare,sub,mean,boundary,push,enc)
from check_belt_directed_incidence import addcell,clean,cross
from assemble_real_complex_arrows import run


def main():
    read('research/strominger/inputs/belt-relative-assembly-protocol-v1.json')
    source=read('research/strominger/inputs/neutron-real-complex-arrows.json')
    geom=read('research/voevodsky/results/four_six_center_cones.json')
    decoded,points0,_=decode(source);R=tuple(tuple(map(F,row)) for row in decoded['generators'][0]['matrix'])
    P=scale(F(1,3),add(I,R,mm(R,R)))
    centers=[mv(P,points0[s['vertex']]) for s in source['seeds']]
    convert=lambda p:(p[2],p[0],p[1])
    axis=convert(sub(centers[1],centers[0]))
    points={k:tuple(map(F,v)) for k,v in geom['belt_scaled_coordinates'].items()}
    faces=geom['belt_faces'];state=prepare(points,faces,axis);signs=state['signs']
    # Native interfaces are computed from the source, never from the defect.
    fresh=run(source);g=fresh['cycle']['geometry'];lookup={v:k for k,v in points.items()}
    labels=[lookup[convert(tuple(map(F,v)))] for v in g['vertices']]
    caps=[tuple(labels[i] for i in f) for f in g['external_interfaces']]
    assert len(caps)==2
    rimedges={tuple(sorted(e)) for f in caps for e in combinations(f,2)}
    assert len(rimedges)==6
    outerkeys={tuple(sorted(f)) for f in faces}
    B={k:v for k,v in state['boundary'].items() if k in outerkeys}
    dB=boundary(B);residual={k:v for k,v in dB.items() if k not in rimedges}
    assert len(residual)==6 and all(abs(v)==2 for v in residual.values())
    assert not (set(residual)&rimedges)
    # The interface enlargement forced by this residual consumes ALL surface
    # edges, so accepting it makes every face-sign pattern a relative cycle.
    surfaceedges={tuple(sorted(e)) for f in faces for e in combinations(f,2)}
    enlarged=rimedges|set(residual)
    assert len(surfaceedges)==12 and enlarged==surfaceedges
    owners=defaultdict(list)
    for i,f in enumerate(faces):
        for e in combinations(f,2):owners[tuple(sorted(e))].append(i)
    adjacency=sorted(tuple(sorted(v)) for v in owners.values() if len(v)==2)
    assert len(adjacency)==6 and all(sum(i in e for e in adjacency)==2 for i in range(6))
    # The alternative has fixed geometric orientation and a +/- polarization
    # fiber, not signs multiplying ordinary geometric 3-chains.
    def transitions(ss):return {(i,j):ss[j]*ss[i] for i,j in adjacency}
    def recover(ts,root):
        vals={0:root};queue=deque([0])
        while queue:
            i=queue.popleft()
            for a,b in adjacency:
                if i not in (a,b):continue
                j=b if i==a else a;value=ts[a,b]*vals[i]
                if j in vals:
                    if vals[j]!=value:raise ValueError('nontrivial holonomy')
                else:vals[j]=value;queue.append(j)
        assert len(vals)==6
        return tuple(vals[i] for i in range(6))
    connection=transitions(signs)
    assert set(connection.values())=={-1}
    assert recover(connection,signs[0])==signs
    assert recover(connection,-signs[0])==tuple(-s for s in signs)
    assert all(signs[j]-connection[i,j]*signs[i]==0 for i,j in adjacency)
    corrupt=dict(connection);edge=adjacency[0];corrupt[edge]*=-1
    try:recover(corrupt,signs[0])
    except ValueError:pass
    else:raise AssertionError('bad holonomy was accepted')
    ordinary_pass=[];enlarged_pass=0;system_pass=0
    for ss in product((-1,1),repeat=6):
        c=defaultdict(int)
        for f,s in zip(faces,ss):addcell(c,tuple(f),s)
        d=boundary(clean(c))
        if not any(k not in rimedges for k in d):ordinary_pass.append(ss)
        if not any(k not in enlarged for k in d):enlarged_pass+=1
        ts=transitions(ss)
        assert recover(ts,ss[0])==ss
        system_pass+=1
    assert set(ordinary_pass)=={(1,)*6,(-1,)*6}
    assert enlarged_pass==system_pass==64
    # Full source C3 preserves the co-generated objects and their incidence.
    perm={k:lookup[convert(mv(R,(v[1],v[2],v[0])))] for k,v in points.items()}
    fidx={frozenset(f):i for i,f in enumerate(faces)}
    fp={i:fidx[frozenset(perm[v] for v in f)] for i,f in enumerate(faces)}
    assert {tuple(sorted((fp[i],fp[j]))):t for (i,j),t in connection.items()}==connection
    assert push(B,perm)==B and push(residual,perm)==residual
    assert {tuple(sorted(perm[v] for v in e)) for e in rimedges}==rimedges
    assert boundary(push(state['chain'],perm))==push(state['boundary'],perm)
    # Gauge trivialization changes the representation of the readout as well.
    # chi'_i=chi_i*chi_i=1 and t'_ij=chi_j*t_ij*chi_i=1.
    # Fixed original polarization reading must decode chi_i*chi'_i.
    gauged=[signs[i]*signs[i] for i in range(6)]
    gt={(i,j):signs[j]*t*signs[i] for (i,j),t in connection.items()}
    assert gauged==[1]*6 and set(gt.values())=={1}
    decoded_signs=[signs[i]*gauged[i] for i in range(6)]
    assert decoded_signs==list(signs) and sum(decoded_signs)==0 and sum(gauged)==6
    # Equal-face signed count is the exact cancellation factor, NOT calibrated charge.
    # Transition -1 above acts on a polarity LABEL, not as a field phase.
    # Test the distinction on all eighteen actual centroid-edge triangles.
    for face in faces:
        vs=[points[k] for k in face];f=mean(vs)
        for j in range(3):
            a,b=vs[j],vs[(j+1)%3]
            r=sub(f,tuple((x+y)/2 for x,y in zip(a,b)))
            s=tuple((x-y)/2 for x,y in zip(a,b))
            area=cross(r,s);assert area!=(0,0,0)
            nr,ns=tuple(-x for x in r),tuple(-x for x in s)
            assert cross(nr,ns)==area  # phase -1 leaves circulation unchanged
            assert cross(r,ns)==tuple(-x for x in area)  # conjugation reverses it
    target=read('research/voevodsky/results/opposite_branch_belt_store.json')
    assert signs==tuple(target['face_signs'])
    checks={'axis_and_signs_constructed_before_target_read':True,'external_interfaces_generated_without_defect_input':True,
      'ordinary_rim_relative_closure_rejected':True,'enlarging_to_full_edge_interface_is_nonselective':True,
      'co_generated_polarization_connection_flat_and_root_recoverable':True,'single_edge_holonomy_hostile_rejected':True,
      'all64_patterns_separate_compatibility_from_selection':True,'source_C3_transports_whole_packet':True,
      'gauge_trivialization_must_transport_polarization_reader':True,
      'polarity_label_flip_is_not_complex_phase_flip':True}
    for path in [Path(__file__),BASE/'checkers/check_belt_axial_witness.py',BASE/'checkers/check_belt_directed_incidence.py',BASE/'checkers/assemble_real_complex_arrows.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']:
        hashes[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    report={'status':'pass','checks':checks,'source_hashes':hashes,'axis':list(map(str,axis)), 'signs':list(signs),
      'generated_external_caps':[list(f) for f in caps],'rim_edges':[list(e) for e in sorted(rimedges)],
      'outer_surface':enc(B),'relative_boundary_residual':enc(residual),'native_face_permutation':fp,
      'polarization_transitions':[[i,j,t] for (i,j),t in connection.items()], 'retained_root_sign':signs[0],
      'pattern_counts':{'tested':64,'rim_relative_cycles':len(ordinary_pass),'enlarged_relative_cycles':enlarged_pass,'co_generated_flat_sign_systems':system_pass},
      'disposition':{'ordinary_geometry':'The declared two rim interfaces do not absorb the six lateral edge defects.',
       'retained_total_boundary':'Consistent co-construction, but d²=0 alone is nonselective.',
       'polarization_local_system':'Consistent conditional co-construction with fixed geometric orientation; exact root recovery and C3 transport.',
       'not_proved':'A full native coefficient-field/seam Hamiltonian restriction map for this local system, physical axial selection, or geometric cancellation of the ordinary signed-chain residual.'}}
    out=BASE/'results/belt-relative-assembly';out.mkdir(parents=True,exist_ok=True)
    (out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'relative_residual_edges':len(residual),'pattern_counts':report['pattern_counts']}))
if __name__=='__main__':main()
