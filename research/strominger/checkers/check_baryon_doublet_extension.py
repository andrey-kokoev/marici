"""Explicit tensor-doublet candidates; no source-derived spin/charge law is inferred."""
from hashlib import sha256
from pathlib import Path
import json
from fractions import Fraction as F
from check_rank_one_return_packets import LineInterface
from assemble_metric_coefficient_protocol import (ROOT,A,ZERO,ONE,product,sharp,integer_trace)
from electron_packet_interface import ACTIONS

def digest(p):return sha256(p.read_bytes()).hexdigest()
def tensor_identity(M):return {(2*i+a,2*j+a):v for (i,j),v in M.items() for a in range(2)}
def vector_map(M,v):
    rows=max((i for i,j in M),default=-1)+1
    out=[ZERO]*rows
    for (i,j),a in M.items():out[i]+=a*v[j]
    return tuple(out)
def to_field(z):
    c=[F(0)]*16;c[0]=F(z[0]);c[8]=F(z[1]);return A(tuple(c))
def two(U):return {(i,j):to_field(U[i][j]) for i in range(2) for j in range(2) if to_field(U[i][j])!=ZERO}
def transpose(M):return {(j,i):x for (i,j),x in M.items()}
def add(*Ms):
    out={}
    for M in Ms:
        for k,v in M.items():out[k]=out.get(k,ZERO)+v
    return {k:v for k,v in out.items() if v!=ZERO}
def scale(a,M):return {k:a*v for k,v in M.items() if a*v!=ZERO}
I2={(0,0):ONE,(1,1):ONE};epsilon={(0,1):ONE,(1,0):-ONE}
CI=A(tuple(F(i==8) for i in range(16)))

def main():
    prerequisite=ROOT/'research/strominger/results/rank-one-return-packets-v1.json'
    old=json.loads(prerequisite.read_text(encoding='utf-8'));assert old['status']=='pass'
    ep=ROOT/'research/strominger/results/electron-packet-extraction-v1.json'
    electron=json.loads(ep.read_text(encoding='utf-8'));assert electron['status']=='pass'
    for source_receipt in (old,electron):
        assert all(digest(ROOT/p)==h for p,h in source_receipt['source_sha256'].items()),'stale prerequisite'
    pins={**old['source_sha256'],**electron['source_sha256']}
    pins[prerequisite.relative_to(ROOT).as_posix()]=digest(prerequisite)
    pins[ep.relative_to(ROOT).as_posix()]=digest(ep)
    pins[Path(__file__).resolve().relative_to(ROOT).as_posix()]=digest(Path(__file__))
    for rel in ('research/voevodsky/electron-pairing-coupling.md','research/nima/predictive-pair-electron-spin-binding.md'):
        pins[rel]=digest(ROOT/rel)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale source'
    # Actual native electron scaled encoder/decoder, converted without floating point.
    store=json.loads((ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json').read_text(encoding='utf-8'))
    def coefficient(z):
        c=[F(0)]*16
        for value,mask in zip([v for pair in z for v in pair],(0,2,8,10)):c[mask]=F(value)
        return A(tuple(c))
    Ke={(2*f+i,j):coefficient(p[i][j]) for f,p in enumerate(store['face_projectors']) for i in range(2) for j in range(2) if coefficient(p[i][j])!=ZERO}
    De=scale(A(F(1,2)),{(j,i):x.flip(8) for (i,j),x in Ke.items()})
    assert product(De,Ke)==I2
    rotations=[two(U) for U in ACTIONS]
    assert len(rotations)==24
    for U in rotations:assert product(product(transpose(U),epsilon),U)==epsilon
    checks={'native24_bilinear_singlet_invariance_exact':True};carriers={}
    for name in ('proton','neutron'):
        f=LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json')
        K={(2*i+a,a):v for i,v in enumerate(f.column) for a in range(2) if v!=ZERO}
        D={(a,2*i+a):v for i,v in enumerate(f.row) for a in range(2) if v!=ZERO}
        ops={s:tensor_identity(M) for s,M in f.ops.items()}
        metric=tuple(w for w in f.metric for a in range(2))
        assert product(D,K)==I2 and product(K,D)==ops['N'] and integer_trace(ops['N'])==2
        assert sharp(ops['N'],metric)==ops['N']
        gram=product({(a,i):x.flip(8)*A(metric[i]) for (i,a),x in K.items()},K)
        assert gram==scale(f.rho,I2)
        assert product(ops['L'],K)==product(ops['G'],K)==K
        supports=[len(ops[s]) for s in 'LGN']
        assert supports==[2*len(f.ops[s]) for s in 'LGN'] and sum(supports)==3672
        for U in rotations:
            rawU={(2*i+a,2*i+b):x for i in range(36) for (a,b),x in U.items()}
            assert product(rawU,K)==product(K,U)
            assert product(D,rawU)==product(U,D)
        # Actual raw decoder contraction, not just its two logical terms.
        B={}
        for (a,i),x in D.items():
            b=1-a;sign=ONE if a==0 else -ONE
            for (spin,j),y in De.items():
                if spin==b:B[i,j]=sign*x*y
        assert len(B)==576
        for p,e in (((ONE,ZERO),(ZERO,ONE)),((ZERO,ONE),(ONE,ZERO)),((A(F(3,5)),CI*A(F(4,5))),(ONE,ZERO))):
            X=vector_map(K,p);Y=vector_map(Ke,e)
            raw=sum((w*X[i]*Y[j] for (i,j),w in B.items()),ZERO)
            assert raw==p[0]*e[1]-p[1]*e[0]
        # Two supplied magnetic choices, zero and sigma_z, are both unconstrained by
        # the same stage-defect energy on the return. Neutral charge cannot select one.
        sigma_z={(0,0):ONE,(1,1):-ONE}
        Bz={(2*i+a,2*i+b):x for i in range(36) for (a,b),x in sigma_z.items()}
        assert product(Bz,K)==product(K,sigma_z)
        Iraw={(i,i):ONE for i in range(72)}
        H=add(scale(A(2),Iraw),scale(-ONE,ops['L']),scale(-ONE,ops['G']))
        assert not product(H,K) and not product(H,product(Bz,K))
        assert integer_trace(f.ops['N'])==1 and integer_trace(ops['N'])==2
        carriers[name]={'raw_coordinates_before':36,'raw_coordinates_after':72,'return_rank_before':1,'return_rank_after':2,
          'stage_supports_before':[len(f.ops[s]) for s in 'LGN'],'stage_supports_after':supports,'transfers_before':1836,'transfers_after':3672,
          'source_metric':'M tensor I2','normalizer_squared':f.rho.record(),
          'raw_pair_monomials_with_native_electron':len(B),'spin_rotations_tested':24,
          'source_action_binding':'unassigned: I36 tensor U is supplied, not derived from a named geometric generator',
          'charge_and_magnetic_law':'unassigned; neutral charge alone does not choose a magnetic coefficient'}
        checks[name+'_metric_doublet_recovery_and_rank_change']=True
        checks[name+'_all24_raw_logical_spin_squares']=True
        checks[name+'_explicit_stage_support_doubles_to3672']=True
        checks[name+'_actual576_term_pair_decoder_contraction']=True
    # Phase-charge gate for this supplied singlet output convention.
    phase=A(F(3,5))+CI*A(F(4,5));assert phase.flip(8)*phase==ONE
    proton_electron=phase*phase.flip(8)
    neutron_electron=ONE*phase.flip(8)
    assert proton_electron==ONE and neutron_electron!=ONE
    checks['neutral_pair_output_requires_opposite_supplied_phase_weights']=True
    checks['neutron_electron_pair_not_neutral_under_qn0_qe_minus1']=True
    checks['actual_return_rank_change_is_not_a_reindexing']=True
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    checks['all_native_sources_pins_and_receipts_unchanged']=True
    report={'schema':'marici.baryon-doublet-extension.v1','status':'pass','checks':checks,'carriers':carriers,
      'construction':'Explicit chosen tensor extension A_native tensor C2, stages L/G/N tensor I2; not the old native carrier.',
      'coupling_status':'conditional singlet and phase-weight tests only; no source-derived proton/neutron spin actions, electromagnetic or baryonic coupling law supplied',
      'missing_source_maps':['proton geometric generator -> chosen spin action/lift','neutron geometric generator -> chosen spin action/lift','neutral neutron magnetic/internal coupling and resource law','physical charge representation and preparation'],
      'reopening':'Bind actual source-generator action and coupling records to these or another explicit carrier, with changed rank/operations/cost retained.',
      'source_sha256':pins,'formal_proof_recompiled':False,'native_producers_executed':False,'physical_mass_or_coupling_claim':False}
    (ROOT/'research/strominger/results/baryon-doublet-extension-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
