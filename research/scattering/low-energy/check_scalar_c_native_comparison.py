"""Exact two-point, full-visible error floor for constant small-hidden surrogates."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_three_port_upper_edge as algebra
from check_native_port_bound_spectrum import inertia

ROOT=algebra.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/scalar-c-native-comparison.v1.json'
PROOF=HOME/'SCALAR-C-NATIVE-COMPARISON.md'
RESULT=HOME/'results/scalar-c-native-comparison.v1.json'
F,mm,eye,inverse=algebra.F,algebra.mm,algebra.eye,algebra.inverse


def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(c,A):return [[c*v for v in r] for r in A]
def encoded(A):return [[v.encoded() for v in row] for row in A]
def shifted_gram(D,h,delta):
    return [[h[i]*(D[i][j]-F(delta*int(i==j))) for j in range(len(D))] for i in range(len(D))]
def certify(D,h,delta):
    counts=inertia(shifted_gram(D,h,delta));assert counts==(3,0,0),'unsupported secant floor'
    return list(counts)


def validate_contract(c):
    assert c['schema']=='marici.scattering.scalar-c-native-comparison.v1'
    assert c['native_visible_coordinates']==[0,1,2] and c['native_hidden_coordinates']==list(range(3,11))
    assert c['literal_visible_coordinates']==['E','2','3'] and c['literal_hidden_coordinate']=='C'
    assert c['spectral_points_in_stored_K_units']==['-1','-2']
    assert c['candidate_class']['hidden_dimension_maximum']==2
    assert Q(c['secant_floor'])==Q(1,4096) and Q(c['endpoint_error_floor'])==Q(1,8192)
    assert c['target_bound']=='For every candidate, max_j ||K_eff(z_j)-F(z_j)||_Hport >= 1/8192.'
    assert c['literal_source']=='research/voevodsky/braid-composition-effective-shape-interaction-operators.md'
    for key in ('live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    source_audit=algebra.lower.audit()
    assert ROOT/c['native_source']==algebra.lower.SOURCE
    src=json.loads(algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=[[F(*v) for v in row] for row in src['joint_generator']]
    h=[F(*v) for v in src['gram_diagonal']];hp=h[:3];hq=h[3:]
    assert len(K)==11 and hp==[F('1196/15'),F(20),F(20)]
    H=[r[3:] for r in K[3:]];B=[r[:3] for r in K[3:]];C=[r[3:] for r in K[:3]]
    assert inertia([[hq[i]*H[i][j] for j in range(8)] for i in range(8)])==(8,0,0)
    rank=algebra.lower.Span(3)
    for i,row in enumerate(B):rank.add(row,{'row':i})
    assert len(rank.rows)==3
    J=[]
    for s in (1,2):
        A=add(H,scale(F(s),eye(8)));G=inverse(A)
        assert mm(A,G)==mm(G,A)==eye(8);J.append(G)
    secant=mm(mm(C,add(J[0],scale(F(-1),J[1]))),B)
    assert secant==mm(mm(mm(C,J[0]),J[1]),B)
    pp=[r[:3] for r in K[:3]]
    effective=[add(pp,scale(F(-1),mm(mm(C,G),B))) for G in J]
    assert add(effective[1],scale(F(-1),effective[0]))==secant
    delta=Q(c['secant_floor']);counts=certify(secant,hp,delta)
    assert delta/2==Q(c['endpoint_error_floor'])
    # Constant D may fit exactly at one point; it cannot fit the secant.
    one_point_fit=effective[0]
    assert add(effective[0],scale(F(-1),one_point_fit))==[[F()]*3 for _ in range(3)]
    assert add(effective[1],scale(F(-1),one_point_fit))==secant
    # Independent literal four-state Schur/full inverse controls, with hidden C.
    fixtures=[]
    for a,b,t in ((1,2,3),(2,1,1)):
        toy=[[F(v) for v in row] for row in ((0,a,0,0),(a,0,b,0),(0,b,0,t),(0,0,t,0))]
        for z in (-1,-2):
            visible=[0,2,3];v=[F(a),F(b),F()]
            eff=[[toy[i][j]+v[ii]*v[jj]/F(z) for jj,j in enumerate(visible)] for ii,i in enumerate(visible)]
            full_inv=inverse([[F(z*int(i==j))-toy[i][j] for j in range(4)] for i in range(4)])
            reduced_inv=inverse([[F(z*int(i==j))-eff[i][j] for j in range(3)] for i in range(3)])
            assert [[full_inv[i][j] for j in visible] for i in visible]==reduced_inv
            fixtures.append({'a':a,'b':b,'c':t,'z':z,'full_Schur_inverse_verified':True})
    controls=[]
    for name in ('reverse-secant-sign','omit-visible-metric','inflate-bound'):
        try:
            if name=='reverse-secant-sign':certify(scale(F(-1),secant),hp,delta)
            elif name=='omit-visible-metric':certify(secant,[F(1)]*3,delta)
            else:certify(secant,hp,Q(1))
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile comparison accepted: '+name)
    paths={ROOT/p for p in source_audit['source_sha256']}
    paths.update((CONTRACT,PROOF,Path(__file__),Path(algebra.__file__),ROOT/c['literal_source'],
                  HOME/'test_scalar_c_native_comparison.py'))
    return {'schema':'marici.scattering.scalar-c-native-comparison-receipt.v1','status':'pass',
        'scope_verdict':'quantitative_obstruction_in_declared_class',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'native_visible_dimension':3,'native_hidden_dimension':8,'hidden_coupling_rank':len(rank.rows),
        'spectral_points':['-1','-2'],'visible_metric':[v.encoded() for v in hp],
        'native_effective_operators':[encoded(A) for A in effective],'native_secant':encoded(secant),
        'secant_floor':str(delta),'shifted_Gram_inertia':counts,'endpoint_error_floor':str(delta/2),
        'candidate_hidden_dimension_maximum':2,'constant_visible_block_freely_refitted':True,
        'one_point_constant_fit_succeeds':True,'literal_Schur_controls':fixtures,
        'physical_band_error_bound_proved':False,'all_reductions_excluded':False,
        'analytic_argument_machine_formalized':False,'native_owner_solver_replayed':False,
        'historical_ancestor_freshness_claimed':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale scalar-C/native comparison'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','scope_verdict','hidden_coupling_rank','endpoint_error_floor','candidate_hidden_dimension_maximum','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
