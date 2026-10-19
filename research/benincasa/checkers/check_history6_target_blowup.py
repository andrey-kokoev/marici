#!/usr/bin/env python3
"""Actual CZ inverse and decorated target blowup exceptional residue square."""
import json
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize, target_jac
ROOT=Path(__file__).resolve().parents[3]
RADIAL='research/benincasa/results/history6_radial_resolution.json'
CHART='research/benincasa/results/history6_common_corner.json'
SUPPORT=[0,1,2,4,5,7]


def inverse(N,Z):
    # Only six active rows. Ctilde=N Z_support^{-1} is an actual inverse
    # modulo row gauge, not a reconstruction from tangent data.
    Ctilde=N*Z[SUPPORT,:].inv()
    D=normalize(Ctilde,[0,1]).applyfunc(s.factor)
    scales=[D[1,j] for j in (2,3,4,5)]
    slopes=[s.factor(-D[0,j]/D[1,j]) for j in (2,3,4,5)]
    params=[slopes[0]]+[s.factor(slopes[j]-slopes[j-1]) for j in (1,2,3)]+scales
    return [s.factor(z) for z in params]


def main():
    prior=json.loads((ROOT/RADIAL).read_text());chart=json.loads((ROOT/CHART).read_text())
    for r in (prior,chart):
        assert r['passed']
        for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_radial_resolution.py').read_bytes()).hexdigest()
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    t,r=s.symbols('T R');q=[b1,t,r,b4,b5,b6,b7,b8]
    C=s.Matrix([[s.sympify(v,locals={str(z):z for z in b}) for v in row] for row in chart['source_chart']])
    Cr=C.subs({b2:r*t,b3:t},simultaneous=True)
    g=(b4+r*t+t)/((b4+t)*(r+1));h=s.factor(1-g)
    f0=1/(r+1);fB=r/(r+1)
    # Chart of Bl_{U2=U3=0} target with U the rational inverse coordinates:
    # U2=R*T, U3=T. R is extra exceptional data, not an ordinary function at
    # the blowdown center. The inverse circuit below proves the generic map.
    transform=s.Matrix([b1,b3,b2/b3,b4,b5,b6,b7,b8])
    blowup_jac=transform.jacobian(b)
    assert s.factor(blowup_jac.det())==-1/b3
    source_map=s.Matrix([z.subs({b2:r*t,b3:t},simultaneous=True) for z in b])
    radial_jac=source_map.jacobian(q);assert s.factor(radial_jac.det())==-t
    assert (blowup_jac.subs({b2:r*t,b3:t},simultaneous=True)*radial_jac).applyfunc(s.factor)==s.eye(8)
    # Complementary chart S=U2, V=U3/U2: S=R*T, V=1/R.
    S,V=s.symbols('S V');other=[b1,S,V,b4,b5,b6,b7,b8]
    complementary=s.Matrix([b1,r*t,1/r,b4,b5,b6,b7,b8])
    logtransition=s.diag(*[1/z for z in complementary])*complementary.jacobian(q)*s.diag(*q)
    assert s.factor(logtransition.det())==-1
    g_other=s.factor(g.subs({t:V*S,r:1/V},simultaneous=True))
    assert s.factor(g_other.subs(S,0))==V/(V+1)
    # Top form in target order (b1,T,R,b4,...) has coefficient -g. Moving
    # dT to the front gives +g; residue is f0 / product remaining ordinary
    # coordinates. Source and decorated target are degree-preserving maps.
    remaining=[z for z in q if z!=t];product=s.prod(remaining)
    source0=s.factor(f0/product);sourceB=s.factor(fB/product)
    target0=s.factor(s.residue(g/(t*product),t,0));targetB=s.factor(s.residue(h/(t*product),t,0))
    assert source0==target0 and sourceB==targetB
    assert s.factor(source0+sourceB-1/product)==0
    # Complementary top coefficient +g_other and S deletion parity-1.
    # The seven-form transition dlog R=-dlog V supplies the same minus.
    assert s.factor(-f0.subs(r,1/V)+V/(V+1))==0
    runs=[]
    for old in prior['runs']:
        shift=old['positive_Z_moment_shift']
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        # Full symbolic source-parameter reconstruction, eight free variables.
        generic=inverse(normalize(C*Z,[0,1]),Z)
        assert all(s.factor(x-y)==0 for x,y in zip(generic,b))
        recovered=inverse(normalize(Cr*Z,[0,1]),Z)
        decorated=[recovered[0],recovered[2],s.factor(recovered[1]/recovered[2])]+recovered[3:]
        assert all(s.factor(x-y)==0 for x,y in zip(decorated,q))
        values={z:s.Rational(old['radial_boundary_parameters'][str(z)]) for z in b if str(z) in old['radial_boundary_parameters']}
        values[t]=0;values[r]=s.Rational(old['radial_boundary_parameters']['rho'])
        # Exact inverse along a rational normal arc and a changing direction
        # arc. R is recovered for T!=0 and retained as decoration at T=0.
        tau=s.Symbol('tau');arc=values|{t:tau,r:values[r]+tau}
        arc_recovered=[s.factor(z.subs(arc)) for z in decorated]
        assert arc_recovered==[arc[z] for z in q]
        jac=s.Matrix(decorated).jacobian(q).applyfunc(s.factor);assert jac==s.eye(8)
        assert jac.subs(values).rank()==8 and jac[:,[j for j in range(8) if j!=1]].rank()==7
        blowdownJ,_=target_jac((Cr*Z).subs(values),[Cr.diff(z).subs(values)*Z for z in q],[0,1])
        assert blowdownJ.rank()==7 and blowdownJ[:,[j for j in range(8) if j!=1]].rank()==6
        D0=s.factor(source0.subs(values));DB=s.factor(sourceB.subs(values))
        assert D0==target0.subs(values) and DB==targetB.subs(values) and D0>0 and DB>0
        other_values=values|{S:0,V:1/values[r]}
        otherproduct=s.prod(z for z in other if z!=S)
        otherD0=s.factor(-g_other.subs(S,0)/otherproduct)
        # Convert the ordinary dV density to the R reference using dV/dR.
        pulled=s.factor(otherD0.subs(other_values)*(-1/values[r]**2))
        assert pulled==D0
        assert -2*D0!=0
        runs.append({'positive_Z_moment_shift':shift,'symbolic_inverse_parameters_recovered':8,
            'rational_normal_and_direction_arc_recovered':True,'decorated_full_rank':8,'decorated_exceptional_rank':7,
            'ordinary_blowdown_full_rank':7,'ordinary_blowdown_exceptional_rank':6,
            'source_exceptional_K0_ordinary_density':str(D0),'decorated_target_K0_residue_density':str(D0),
            'source_exceptional_B22_ordinary_density':str(DB),'decorated_target_B22_residue_density':str(DB),
            'complementary_chart_K0_density_pulled_to_R_reference':str(pulled),
            'orientation_flip_K0_defect':str(-2*D0),
            'ordinary_blowdown_residue_disposition':'unavailable_not_zero_preserved'})
    paths=[RADIAL,CHART,'research/benincasa/checkers/check_history6_radial_resolution.py',
        'research/benincasa/checkers/check_three_composite_internal_gluings.py','research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.history6-target-blowup.v1','history_index':6,
        'target_inverse':'Ctilde=N*inverse(Z_support); normalize its active columns1,2; bottom-row entries give b5..b8 and successive negative top/bottom slopes give b1..b4.',
        'target_center':'U2(Y)=U3(Y)=0, U the eight recovered F6 parameters',
        'decorated_target_chart':{'order':[str(z) for z in q],'equations':['U2=R*T','U3=T'],
            'ordinary_inverse_coordinate_transition_determinant':str(s.factor(blowup_jac.det())),
            'radial_forward_coordinate_determinant':str(s.factor(radial_jac.det())),
            'composed_decorated_jacobian':'identity8','exceptional_normal':'T=0',
            'localization':'R>0,b1,b4,b5,b6,b7,b8>0; original quotient lifted coefficient regular after removing common T; R=-1 excluded'},
        'complementary_chart':{'equations':['S=R*T','V=1/R'],'log_transition_determinant':'-1',
            'top_log_coefficient_sign':1,'exceptional_deletion_parity':-1,'seven_form_R_to_V_sign':-1},
        'exceptional_differential_map':{'source_order':[str(z) for z in remaining],
            'target_order':[str(z) for z in remaining],'K0_log_coefficient':str(f0),'B22_log_coefficient':str(fB),
            'source_then_decorated_pushforward_equals_decorated_top_then_residue':True},
        'runs':runs,'passed':True,
        'scope':'Actual rational target blowup and decorated differential square derived from CZ inverse; this changes target space. It does not provide an ordinary blowdown seven-form, a physical supercomponent map, or global weighted descent.',
        'next_action':'Audit the exceptional directional endpoint and R=-1 pole extractions in both target blowup charts, and determine what source-authorized boundary-supercomponent object can retain the extra direction. Do not collapse the decorated boundary map onto its rank6 blowdown.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_target_blowup.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'decorated_ranks':[8,7],'blowdown_ranks':[7,6],
        'complementary_log_transition':'-1','runs':runs},indent=2))

if __name__=='__main__':main()
