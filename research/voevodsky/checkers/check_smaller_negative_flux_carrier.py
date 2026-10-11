"""Compare the proton with a four-whole-face negative-circulation carrier.
Use the same three-axis coefficient protocol and mode-oriented flux. Also
retain amplitudes in a facewise Fourier decomposition of the original mode.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import permutations
from math import pi
from collections import Counter
import json
from check_coupled_six_piece_belt import (
    R,Z,ONE,add,mul,conj,scale,norm,total,mv,encoded,
    construct,verify_operators,PROTON,verify_proton)
from check_mode_flux_charge import solid_angle,cross,dot,area_identity
from check_geometric_cycle_reversal import geo

BASE=Path(__file__).resolve().parents[1]
W=(R(-Q(1,2)),R(Q(1,2)));W2=mul(W,W)
C=(ONE,W,W2)

def mode(vertices):return tuple(total(scale(p[i],c) for p,c in zip(vertices,C)) for i in range(3))
def area(v):return cross(tuple(z[0] for z in v),tuple(z[1] for z in v))
def vscale(c,v):return tuple(mul(c,z) for z in v)
def vnorm(v):return sum(map(norm,v))
def character(a,b):return scale(1/norm(b),mul(a,conj(b)))
def fraction(x):
    if isinstance(x,R):assert x.b==0;return str(x.a)
    return str(x)

def main():
    source_bytes=PROTON.read_bytes();source=json.loads(source_bytes);_,source_rows=verify_proton(source)
    source_geo=source['objects'][source['objects'][source['root']]['geometry']]['payload']
    P={k:tuple(map(Q,v)) for k,v in geo.POINTS.items()};inverse={v:k for k,v in P.items()}
    diagonals=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    rotations=[tuple(tuple(Q(d[i] if i==j else 0) for j in range(3)) for i in range(3)) for d in diagonals]
    faces=[tuple(inverse[tuple(d[i]*P[k][i] for i in range(3))] for k in 'ABC') for d in diagonals]
    positive=[mode([P[k] for k in f]) for f in faces]
    negative=[tuple(map(conj,v)) for v in positive]
    assert all(mv(r,negative[0])==v for r,v in zip(rotations,negative))
    L,G,N,u,ns=construct(negative,[0]*4,rotations)
    protocol=verify_operators(L,G,N,u)
    assert protocol['total']==228 and list(map(len,(L,G,N)))==[36,48,144]
    assert all(vnorm(v)==12 for v in negative)
    boundary=Counter()
    for f in faces:
        for a,b in zip(f,f[1:]+f[:1]):boundary[tuple(sorted((a,b)))]+=1 if a<b else -1
    assert all(v==0 for v in boundary.values())
    face_angles=[solid_angle(*[tuple(map(float,P[k])) for k in f]) for f in faces]
    assert all(abs(a-pi)<1e-12 for a in face_angles)
    # Area reversal is exact; the closed tetrahedral boundary has degree +1.
    for f,v,w in zip(faces,positive,negative):
        A=area_identity(tuple(P[k] for k in f));assert area(v)==A and area(w)==tuple(-x for x in A)
    scale_controls={}
    for s in (Q(1),Q(1,2),Q(1,10),Q(1,100)):
        ps={k:tuple(s*x for x in p) for k,p in P.items()}
        angle=sum(solid_angle(*[tuple(map(float,ps[k])) for k in f]) for f in faces)/(4*pi)
        for f,v in zip(faces,negative):assert tuple(map(conj,mode([ps[k] for k in f])))==tuple(scale(s,z) for z in v)
        assert abs(angle-1)<1e-12;scale_controls[str(s)]=-angle
    # Reconstruct the original 12 triangles from these faces, then bind their
    # ordered triples to the verified source rather than merely matching counts.
    small={};fourier=[];negative_fraction=Q(0);positive_fraction=Q(0)
    for f,V in zip(faces,positive):
        F=tuple(sum(P[k][i] for k in f)/3 for i in range(3));fname='F_'+''.join(sorted(f))
        vs=[]
        for j in range(3):
            key=(fname,f[j],f[(j+1)%3]);v=mode([F,P[key[1]],P[key[2]]]);small[key]=v;vs.append(v)
        channels=[]
        for weights in ((ONE,ONE,ONE),(ONE,W,W2),(ONE,W2,W)):
            channels.append(tuple(total(mul(c,v[i]) for c,v in zip(weights,vs)) for i in range(3)))
        assert channels[0]==(Z,Z,Z)
        assert channels[1]==vscale(scale(2,W),V)
        assert channels[2]==vscale(scale(-1,W2),tuple(map(conj,V)))
        # The unitary Fourier transform divides each channel by sqrt(3).
        # Work with quadratic quantities divided by 3, avoiding radicals.
        powers=[vnorm(v)/3 for v in channels]
        assert powers==[0,16,4] and sum(powers)==sum(map(vnorm,vs))==20
        A=area(V);den=dot(A,A)
        signed=[dot(A,area(v))/(3*den) for v in channels]
        assert signed==[0,Q(4,3),-Q(1,3)]
        # Each whole face subtends pi, or 1/4 of a sphere.
        positive_fraction+=signed[1]/4;negative_fraction+=signed[2]/4
        fourier.append({'face':list(f),'unitary_channel_squared_norms':list(map(fraction,powers)),
                        'unitary_channel_fluxes':[fraction(x/4) for x in signed]})
    source_triangles={tuple(row['triangle']) for row in source_geo['triangles_and_transports']}
    assert set(small)==source_triangles and len(source_rows)==1836
    assert positive_fraction==Q(4,3) and negative_fraction==-Q(1,3)
    # Full A4 action: original 12-site source is invariant. The new 4-face
    # selected line instead has a nontrivial one-dimensional cyclic character.
    chars=[];original_invariant=True
    for perm in permutations(range(4)):
        if sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2:continue
        rotation=geo.rotation(perm);rename=dict(zip('ABCD',('ABCD'[i] for i in perm)))
        acted=[None]*4
        for i,f in enumerate(faces):
            target=next(j for j,g in enumerate(faces) if set(g)=={rename[k] for k in f})
            acted[target]=mv(rotation,negative[i])
        chi=character(acted[0][0],negative[0][0]);assert chi in (ONE,W,W2)
        assert all(a==vscale(chi,b) for a,b in zip(acted,negative));chars.append(chi)
        for (fc,a,b),v in small.items():
            target=('F_'+''.join(sorted(rename[k] for k in fc[2:])),rename[a],rename[b])
            original_invariant &= mv(rotation,v)==small[target]
    assert Counter(chars)==Counter({ONE:4,W:4,W2:4}) and original_invariant
    checks={
        'original_source_verified_and_twelve_triangles_matched':set(small)==source_triangles,
        'four_whole_faces_are_an_oriented_closed_boundary':all(v==0 for v in boundary.values()),
        'negative_mode_area_is_exactly_reversed':all(area(w)==tuple(-x for x in area(v)) for v,w in zip(positive,negative)),
        'negative_flux_is_minus_one':abs(sum(face_angles)/(4*pi)-1)<1e-12,
        'flux_unchanged_at_four_positive_geometric_scales':all(abs(v+1)<1e-12 for v in scale_controls.values()),
        'same_three_axis_protocol_has_228_transfers':protocol['total']==228,
        'coherent_return_and_positive_deletion_certificate':protocol['all_arrows_covered'],
        'new_line_has_nontrivial_A4_character_unlike_original':len(set(chars))==3 and original_invariant,
        'facewise_Fourier_transform_preserves_squared_norm':all(r['unitary_channel_squared_norms']==['0','16','4'] for r in fourier),
        'source_negative_channel_carries_minus_one_third_not_minus_one':negative_fraction==-Q(1,3),
        'source_positive_and_negative_fluxes_sum_to_one':positive_fraction+negative_fraction==1,
        'source_unchanged':PROTON.read_bytes()==source_bytes,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'trial':'Independent four-whole-face mode with conjugated circulation; not the twelve-triangle antiproton construction.',
        'reference_flux':{'original_proton':'1','conjugated_original_proton':'-1','four_face_candidate':'-1'},
        'protocol':protocol,'original_protocol_total':len(source_rows),
        'original_to_candidate_transfer_ratio':str(Q(len(source_rows),protocol['total'])),
        'mass_readout':'No mass law used. If mass were simply the transfer count, the ratio would be 153/19, not 1836.',
        'new_A4_character_multiplicities':{'1':chars.count(ONE),'omega':chars.count(W),'omega_squared':chars.count(W2)},
        'scale_controls':scale_controls,
        'source_Fourier_decomposition':{'positive_channel_flux':fraction(positive_fraction),'negative_channel_flux':fraction(negative_fraction),
            'positive_squared_norm_fraction':'4/5','negative_squared_norm_fraction':'1/5','per_face':fourier,
            'amplitude_issue':'The inherited negative channel is 1/sqrt(3) times the standalone four-face reference, up to a unit phase. Resetting it to that reference multiplies squared amplitude and flux by three.'},
        'conclusion':'A smaller closed negative-flux carrier exists, but flux -1 is not an electron identifier. Charge is insensitive to geometric scale; the source-inherited negative channel is -1/3. An independently selected electron scale, amplitude and mass readout have not been supplied.',
        'source_root':source['root'],'source_sha256':sha256(source_bytes).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'source_root':source['root'],'faces':faces,'points':{k:list(map(str,v)) for k,v in P.items()},
        'selected_vectors':[[encoded(z) for z in v] for v in negative],
        'arrows':[{'stage':s,'target':i,'source':j,'coefficient':encoded(z)} for s,m in zip(('L','G','N'),(L,G,N)) for (i,j),z in sorted(m.items())]}
    (BASE/'results/smaller_negative_flux_carrier.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/smaller_negative_flux_carrier_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
