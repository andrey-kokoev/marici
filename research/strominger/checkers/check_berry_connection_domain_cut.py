"""Exact CP1 connection packet and annular flat-twist control.
Symbolic identities, not an exhaustion theorem for arbitrary Berry domains.
"""
from pathlib import Path
import copy
import hashlib
import json
import sympy as s
from check_oscillator_retained_cone import API, Row, build, triangle_decode
from check_oscillator_fcc_representation import encode, decode

ROOT=Path(__file__).resolve().parents[3]
r=s.symbols('r', positive=True,real=True)
phi=s.symbols('phi', real=True)
alpha=s.symbols('alpha', real=True)


def main():
    uN=s.Matrix([1,r*s.exp(s.I*phi)])/s.sqrt(1+r*r)
    uS=s.Matrix([s.exp(-s.I*phi),r])/s.sqrt(1+r*r)
    transition=s.exp(-s.I*phi)
    simp=lambda x:s.simplify(s.expand_complex(x))
    assert (uS-transition*uN).applyfunc(simp)==s.zeros(2,1)
    PN=(uN*uN.conjugate().T).applyfunc(simp)
    PS=(uS*uS.conjugate().T).applyfunc(simp)
    assert (PN-PS).applyfunc(simp)==s.zeros(2)
    connection=lambda u,x:simp(-s.I*(u.conjugate().T*u.diff(x))[0])
    ANr,ANp=connection(uN,r),connection(uN,phi)
    ASr,ASp=connection(uS,r),connection(uS,phi)
    assert ANr==ASr==0
    assert simp(ANp-r*r/(1+r*r))==0
    assert simp(ASp+1/(1+r*r))==0
    assert simp(ASp-ANp+s.Integer(1))==0
    F=simp(s.diff(ANp,r)-s.diff(ANr,phi))
    FP=simp(-s.I*s.trace(PN*(PN.diff(r)*PN.diff(phi)-PN.diff(phi)*PN.diff(r))))
    assert simp(F-2*r/(1+r*r)**2)==0 and simp(F-FP)==0
    assert s.integrate(F,(r,0,s.oo))==1 # angular integral is 2pi
    # Closed circle r=R: integral uses the actual connection, not endpoints.
    loop_integral=s.integrate(ANp,(phi,0,2*s.pi))
    assert simp(loop_integral-2*s.pi*r*r/(1+r*r))==0
    assert s.simplify(s.exp(s.I*loop_integral.subs(r,1)))==-1
    # Transition winding and gauge-dependent connections are separately retained.
    winding=simp(transition.diff(phi)/(s.I*transition))
    assert winding==-1
    n=s.symbols('n', integer=True)
    assert s.simplify(s.exp(s.I*2*s.pi*n))==1
    fields={
        'north_A_r':ANr,'north_A_phi':ANp,'south_A_r':ASr,'south_A_phi':ASp,
        'transition_NS':transition,'curvature_r_phi':F,
        'north_frame_0':uN[0],'north_frame_1':uN[1],
        'south_frame_0':uS[0],'south_frame_1':uS[1],
    }
    fields.update({f'P_{a}{b}':PN[a,b] for a in range(2) for b in range(2)})
    def packet(data,policy):
        rows=tuple(Row(('field',name),('connection_packet',),('field_port',name),value) for name,value in sorted(data.items()))
        return API['incoming_promotion'](API['incoming_promotion'](rows,1,policy),2,policy)
    def recover_fields(p):
        return {row.label[1]:row.value for row in API['leaves'](p)}
    charts_checked=0
    for policy in ('inherited','common'):
        p=packet(fields,policy)
        # The geometric-coordinate chart is distinct from the Berry parameter chart.
        for chart in ((0,1,2,3),(3,1,0,2)):
            geo=copy.deepcopy(encode(build(p),chart))
            restored=triangle_decode(decode(geo)[1:])
            data=recover_fields(restored)
            assert data==fields
            assert simp(s.diff(data['north_A_phi'],r)-s.diff(data['north_A_r'],phi)-data['curvature_r_phi'])==0
            assert simp(data['south_A_phi']-data['north_A_phi']-winding)==0
            assert s.simplify(s.exp(s.I*s.integrate(data['north_A_phi'].subs(r,1),(phi,0,2*s.pi))))==-1
            charts_checked+=1
        # On an annulus, add a flat central connection; do NOT claim this is
        # a nontrivial flat bundle over the simply connected whole sphere.
        twisted={**fields,'north_A_phi':ANp+alpha,'south_A_phi':ASp+alpha}
        assert simp(s.diff(twisted['north_A_phi'],r)-F)==0
        pt=packet(twisted,policy)
        back=recover_fields(triangle_decode(decode(encode(build(pt),(0,1,2,3)))[1:]))
        ratio=s.simplify(s.exp(s.I*s.integrate(back['north_A_phi']-fields['north_A_phi'],(phi,0,2*s.pi))))
        assert ratio==s.exp(2*s.I*s.pi*alpha)
        assert s.simplify(ratio.subs(alpha,s.Rational(1,2)))==-1
        assert all(twisted[f'P_{a}{b}']==fields[f'P_{a}{b}'] for a in range(2) for b in range(2))
        assert p!=pt
    sources=['research/benincasa/complex-kernel-berry-curvature.md',
             'research/aspect/a-berry-eigenline-falsifies-frozen-v10.md',
             'research/nima/local-berry-response-requires-framing.md',
             'research/strominger/checkers/check_oscillator_retained_cone.py',
             'research/strominger/checkers/check_oscillator_fcc_representation.py',
             str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','domain':'canonical CP1 eigenline connection; separate annular flat-twist control',
            'convention':'A=-i u^dagger du; loop phase exp(i integral A)',
            'north_A_phi':str(ANp),'south_A_phi':str(ASp),
            'transition':str(transition),'transition_winding':-1,
            'curvature':str(F),'curvature_integral_over_2pi':'1',
            'equatorial_loop_phase':'-1','annular_twist_phase_ratio':str(ratio),
            'retained_symbolic_fields':len(fields),'decorated_charts_checked':charts_checked,
            'projector_only_annular_recovery_refuted':True,
            'scope':'Exact symbolic chart/connection representation and circle integrals. No arbitrary Berry family coverage, non-Abelian transport theorem or fresh Agda proof.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/berry-connection-domain-cut/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
