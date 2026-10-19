"""Declared Pauli/radial bridge, with exact retained phase charts.
Read-only shared sources. Not a physical Hamiltonian or additional link.
"""
from fractions import Fraction as F
from itertools import product
from functools import cmp_to_key
from pathlib import Path
from math import isqrt
from hashlib import sha256
import json
from check_proton_electron_single_link_potential import ROOT,decode,mat,ginv,neg,parse
from check_electron_tetrahedral_spinor import D,cast,pos,ga,gm,gc,gt,gmm,sm,act,norm,adj,ident,spin,encode,G0,G1
from check_projector_fold_sheets import parameters,verify as verify_atlas
from check_proton_merkle_reassembly import POINTS


def ge(a,b):return a==b or pos(a-b)
def realmode(p,v):
    direction=tuple(sum(v[k]*POINTS[a][j] for k,a in enumerate('ABCD')) for j in range(3))
    return act(p,tuple((x,D()) for x in direction))
def direction(v):return tuple(sum(v[k]*POINTS[a][j] for k,a in enumerate('ABCD')) for j in range(3))
def bloch(z):
    n=cast(norm(z))
    if not pos(n):raise ValueError('nonzero spinor required')
    w=gm(gc(z[0]),z[1]);return (2*cast(w[0])/n,2*cast(w[1])/n,cast(gm(gc(z[0]),z[0])[0]-gm(gc(z[1]),z[1])[0])/n)
def ray_projector(r):
    x,y,z=r
    return sm(F(1,2),(((D(1)+z,D()),(x,-y)),((x,y),(D(1)-z,D()))))
def radial(r):
    s=[sum(POINTS[a][j]*r[j] for j in range(3)) for a in 'ABCD']
    lowest=s[0]
    for x in s[1:]:
        if pos(lowest-x):lowest=x
    alpha=-D(1)/lowest
    return tuple((D(1)+alpha*x)/4 for x in s),alpha

def construct(z,host,ell,p):
    r=bloch(z);v,alpha=radial(r);a=act((ell,),z)[0]
    d=(neg(ell[1]),ell[0]);c=act((tuple(gc(x) for x in d),),z)[0]
    return {'host':host,'potential':v,'radial_certificate':alpha,'norm_squared':cast(norm(z)),
            'link':a,'dark_phase_witness':c if a==G0 else None,'mode':realmode(p,v)}

def reconstruct(record,ell,p):
    v=record['potential'];alpha=record['radial_certificate'];n=record['norm_squared'];a=record['link']
    if len(v)!=4 or sum(v)!=1 or any(not ge(x,D()) for x in v) or not any(x==0 for x in v):raise ValueError('boundary type')
    if not pos(alpha) or not pos(n):raise ValueError('positive radial/norm type')
    u=direction(v)
    if sum(x*x for x in u)!=alpha*alpha:raise ValueError('radial certificate')
    r=tuple(x/alpha for x in u);R=ray_projector(r)
    if record['mode']!=realmode(p,v):raise ValueError('mode mismatch')
    if len(record['host'])!=3 or sum(record['host'])!=1 or any(not ge(x,D()) for x in record['host']):raise ValueError('host type')
    if a!=G0:
        if record['dark_phase_witness'] is not None:raise ValueError('redundant phase chart')
        seed=tuple(gc(x) for x in ell);reading=a
    else:
        seed=(neg(ell[1]),ell[0]);reading=record['dark_phase_witness']
        if reading is None or reading==G0:raise ValueError('dark phase absent')
    z=tuple(gm((n,D()),gm(x,ginv(gc(reading)))) for x in act(R,seed))
    if norm(z)!=n or act((ell,),z)[0]!=a:raise ValueError('incompatible link/norm/ray')
    if bloch(z)!=r:raise ValueError('incompatible ray')
    if a==G0 and act((tuple(gc(x) for x in seed),),z)[0]!=reading:raise ValueError('incompatible dark phase')
    return z

def root_fraction(q):
    if q<0:raise ValueError('negative square')
    a,b=isqrt(q.numerator),isqrt(q.denominator)
    if a*a!=q.numerator or b*b!=q.denominator:raise ValueError('root outside fixture field')
    return F(a,b)
def positive_root(q):
    q=cast(q)
    if not pos(q):raise ValueError('nonpositive square')
    if q.b==0:
        for factor in (1,3):
            try:
                r=root_fraction(q.a/factor);return D(r,0) if factor==1 else D(0,r)
            except ValueError:pass
    else:
        t=root_fraction(q.a*q.a-3*q.b*q.b)
        for sign in (1,-1):
            try:
                c=root_fraction((q.a+sign*t)/2)
                if c:
                    r=D(c,q.b/(2*c));r=r if pos(r) else -r
                    if r*r==q:return r
            except ValueError:pass
    raise ValueError('root outside fixture field')

def reconstruct_from_mode(record,ell,p,normal,recovery):
    # The source-bound bridge aligns the bright ray with -normal/sqrt3.
    # The link INTENSITY, norm and potential mode therefore recover polar
    # coordinate and transverse direction; the complex link adds phase.
    n=record['norm_squared'];a=record['link'];delta=norm(tuple(gc(x) for x in ell))
    beta=D(0,1)*(D(1)-2*cast(gm(gc(a),a)[0])/(delta*n))
    w=tuple(sum(F(x)*z[0] for x,z in zip(row,record['mode'])) for row in recovery)
    transverse=sum(x*x for x in w);denominator=D(1)-beta*beta/3
    if transverse==0:
        if denominator!=0:raise ValueError('mode/intensity mismatch')
        r=tuple(D(x)*beta/3 for x in normal)
    else:
        alpha=positive_root(transverse/denominator)
        r=tuple(x/alpha+D(y)*beta/3 for x,y in zip(w,normal))
    v,alpha=radial(r)
    derived=dict(record,potential=v,radial_certificate=alpha)
    return reconstruct(derived,ell,p),derived

def flag(v):
    order=sorted(range(4),key=cmp_to_key(lambda i,j:0 if v[i]==v[j] else (-1 if pos(v[i]-v[j]) else 1)))
    if v[order[3]]!=0 or not all(pos(v[order[k]]-v[order[k+1]]) for k in range(3)):return None
    return tuple(''.join(map(str,sorted(order[:k]))) for k in (1,2,3)) + ('0123',)
def ser(r):
    return {'host':[str(x.a) for x in r['host']], 'potential':[[str(x.a),str(x.b)] for x in r['potential']],
      'radial_certificate':[str(r['radial_certificate'].a),str(r['radial_certificate'].b)],
      'norm_squared':[str(r['norm_squared'].a),str(r['norm_squared'].b)],'link':encode(r['link']),
      'dark_phase_witness':None if r['dark_phase_witness'] is None else encode(r['dark_phase_witness']),
      'mode':[encode(x) for x in r['mode']]}
def unser(r):
    real=lambda x:D(*map(F,x))
    return {'host':tuple(D(F(x)) for x in r['host']),'potential':tuple(real(x) for x in r['potential']),
       'radial_certificate':real(r['radial_certificate']),'norm_squared':real(r['norm_squared']),
       'link':decode(r['link']),'dark_phase_witness':None if r['dark_phase_witness'] is None else decode(r['dark_phase_witness']),
       'mode':tuple(decode(x) for x in r['mode'])}
def rejects(fn):
    try:fn()
    except (ValueError,ZeroDivisionError):return True
    return False


def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/spinor-potential-link-bridge-v1.json';contract=json.loads(cp.read_text())
    ep=ROOT/contract['electron'];ap=ROOT/contract['potential'];pp=ROOT/contract['proton']
    electron=json.loads(ep.read_text());packet=json.loads(ap.read_text());verify_atlas(packet)
    ports,proton_ops=parse(json.loads(pp.read_text()));port=ports.index(('AB','x'))
    receiver=tuple((D(row[port][0]),D(0,row[port][1])) for row in proton_ops[2]);probe=next(i for i,z in enumerate(receiver) if z!=G0)
    p0,n,recovery=parameters(packet['source']);p=tuple(tuple((D(a),D(0,b)) for a,b in row) for row in p0)
    P=tuple(tuple(tuple(decode(x) for x in row) for row in face) for face in electron['face_projectors']);E=tuple(row for face in P for row in face);ell=E[0]
    d=(neg(ell[1]),ell[0]);b=tuple(gc(x) for x in ell);host=(D(F(1,3)),)*3
    assert gmm(adj(E),E)==sm(2,ident(2))
    ops={s:[[G0]*8 for _ in range(8)] for s in 'LGN'}
    for arrow in electron['arrows']:ops[arrow['stage']][arrow['target']][arrow['source']]=decode(arrow['weight'])
    for A in ops.values():assert gmm(A,E)==E
    # Eigenlines of the actual electron projectors map to the actual potential
    # tetrahedron vertices, with permutation D,C,B,A; no new tetrahedron.
    face_records=[]
    for i,face in enumerate(P):
        seed=tuple(row[0] for row in face);r=construct(seed,host,ell,p)
        assert r['potential']==tuple(D(int(j==3-i)) for j in range(4))
        face_records.append({'electron_face':i,'potential_vertex':'ABCD'[3-i],'bridge':ser(r)})
    samples=[(G1,(D(F(k,den)),D(F(l,den)))) for den in (2,8) for k in range(-16,17) for l in range(-16,17)]
    samples.extend([(G0,G1),d,tuple(gm((D(),D(1)),x) for x in d),b,
        tuple(ga(x,y) for x,y in zip(b,d)),tuple(ga(x,neg(y)) for x,y in zip(b,d))])
    owners={};checks=0
    for seed in samples:
        r=construct(seed,host,ell,p);assert reconstruct(r,ell,p)==seed
        forward=tuple(gm(z,r['link']) for z in receiver)
        assert gm(ginv(receiver[probe]),forward[probe])==r['link']
        c=act((tuple(gc(x) for x in d),),seed)[0]
        assert ga(gm(gc(r['link']),r['link']),gm(gc(c),c))==(norm(d)*norm(seed),D())
        assert reconstruct(unser(json.loads(json.dumps(ser(r)))),ell,p)==seed
        recovered,derived=reconstruct_from_mode(r,ell,p,n,recovery)
        assert recovered==seed and derived['potential']==r['potential'] and derived['radial_certificate']==r['radial_certificate']
        own=flag(r['potential'])
        if own is not None:owners.setdefault(own,{'seed':[encode(x) for x in seed],'bridge':ser(r)})
        phase_seed=tuple(gm((D(),D(1)),x) for x in seed);phase=construct(phase_seed,host,ell,p)
        assert phase['potential']==r['potential'] and phase['mode']==r['mode'] and phase['norm_squared']==r['norm_squared']
        assert phase['link']==gm((D(),D(1)),r['link'])
        if r['dark_phase_witness'] is not None:assert phase['dark_phase_witness']==gm((D(),D(1)),r['dark_phase_witness'])
        checks+=1
    originalowners={tuple(x) for x in packet['record']['original_fold_owners']};assert set(owners)==originalowners and len(owners)==24
    # The previous same-arrow pair is now separated by the potential ray.
    pair=[tuple(ga(x,s(y)) for x,y in zip(b,d)) for s in (lambda y:y,neg)]
    pair_records=[construct(z,host,ell,p) for z in pair]
    assert pair_records[0]['link']==pair_records[1]['link'] and pair_records[0]['norm_squared']==pair_records[1]['norm_squared']
    assert pair_records[0]['potential']!=pair_records[1]['potential']
    dark_records=[construct(z,host,ell,p) for z in (d,tuple(gm((D(),D(1)),x) for x in d))]
    assert all(r['link']==G0 for r in dark_records)
    assert dark_records[0]['potential']==dark_records[1]['potential'] and dark_records[0]['mode']==dark_records[1]['mode']
    assert dark_records[0]['dark_phase_witness']!=dark_records[1]['dark_phase_witness']
    bad=dict(dark_records[0],dark_phase_witness=None);assert rejects(lambda:reconstruct(bad,ell,p))
    bad=dict(pair_records[0],radial_certificate=pair_records[0]['radial_certificate']*2);assert rejects(lambda:reconstruct(bad,ell,p))
    bad=dict(pair_records[0],norm_squared=pair_records[0]['norm_squared']*2);assert rejects(lambda:reconstruct(bad,ell,p))
    assert rejects(lambda:construct((G0,G0),host,ell,p))
    # Transport all24 existing binary actions. Their rotations preserve this
    # same tetrahedron, so they permute the full potential boundary, not only
    # chosen samples; central -1 fixes the ray but changes retained phase.
    quats=set()
    for k in range(4):
        for s in (-1,1):quats.add(tuple(F(s if j==k else 0) for j in range(4)))
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    vertex_seed=[tuple(row[0] for row in P[i]) for i in range(3,-1,-1)];actions=[]
    for q in sorted(quats):
        U=spin(q);perm=[]
        for seed in vertex_seed:
            image=construct(act(U,seed),host,ell,p)['potential'];perm.append(image.index(D(1)))
        assert sorted(perm)==list(range(4))
        for seed in (pair[0],pair[1],d,(G1,(D(2),D(3)))):
            old=construct(seed,host,ell,p);new=construct(act(U,seed),host,ell,p)
            expected=[D()]*4
            for i,j in enumerate(perm):expected[j]=old['potential'][i]
            assert new['potential']==tuple(expected) and new['norm_squared']==old['norm_squared']
            assert reconstruct(new,ell,p)==act(U,seed)
        actions.append({'quaternion':list(map(str,q)),'potential_vertex_permutation':perm})
    minus=construct(tuple(neg(z) for z in pair[0]),host,ell,p)
    assert minus['potential']==pair_records[0]['potential'] and minus['link']==neg(pair_records[0]['link'])
    result={'schema':'marici.spinor-potential-link-bridge.v1','passed':True,'classification':'declared_information_preserving_bridge_not_physical_binding',
      'roundtrip_samples':checks,'native_stage_intertwiners_verified':True,'retained_fold_interiors':len(owners),
      'proton_receiver':{'raw_port':['AB','x'],'projected_column':[encode(z) for z in receiver],'nonzero_probe_index':probe,'link_forward_and_algebraic_readback_verified':True},
      'face_vertex_alignment':face_records,'interior_witness_for_every_fold':[{'owner':list(k),**v} for k,v in sorted(owners.items())],
      'same_link_pair_resolved_by_potential':[ser(r) for r in pair_records],
      'same_potential_same_link_dark_phase_pair':[ser(r) for r in dark_records],
      'binary_tetrahedral_transport':actions,'central_minus_one_phase_retained':True,
      'rejected':['zero_spinor_without_separate_vacuum_stratum','missing_dark_phase','wrong_radial_certificate','incompatible_norm'],
      'global_single_arrow_spinor_recovery':False,'generic_recovery_with_retained_potential_norm_and_complex_link':True,
      'dark_recovery_requires_retained_internal_phase':True,'mode_equal_to_link':False,
      'potential_mode_plus_link_plus_norm_recovers_ray_in_declared_alignment':True,
      'mode_decoder_uses_stored_potential_or_radial_certificate':False,'additional_transfer_arrows_added':0,
      'potential_realization_phase_chart_is_measurement_access':False,'physical_binding_or_hamiltonian_derived':False,
      'scope':contract['scope']}
    paths=[cp,ep,ap,pp,Path(__file__),base/'checkers/check_proton_electron_single_link_potential.py',base/'checkers/check_electron_tetrahedral_spinor.py',base/'checkers/check_projector_fold_sheets.py']
    result['source_hashes']={path.relative_to(ROOT).as_posix():sha256(path.read_bytes()).hexdigest() for path in paths}
    (base/'results/spinor-potential-link-bridge-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('passed','roundtrip_samples','retained_fold_interiors','central_minus_one_phase_retained','global_single_arrow_spinor_recovery','generic_recovery_with_retained_potential_norm_and_complex_link','additional_transfer_arrows_added')},indent=2))
if __name__=='__main__':main()
