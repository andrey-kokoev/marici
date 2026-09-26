"""Independent local chart/kinetic-jet check, conditional on Nima's declared model.
No continuum, quantum-decoupling, or six-point amplitude theorem is claimed.
"""
from pathlib import Path
import hashlib,json
import sympy as s
base=Path(__file__).resolve().parent
root=base.parent.parent
checks={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eq(name,a,b=0):
    checks[name]=s.simplify(s.trigsimp(a-b))==0
    if not checks[name]:raise AssertionError((name,s.simplify(a-b)))
formal_path=base/'action-chart-comparison-formal.json'
formal=json.loads(formal_path.read_text())
checks['fresh_formal_closure']=formal['passed'] and formal['fresh'] and formal['action_charts_mode']
checks['formal_dependencies_current']=all(Path(p).exists() and sha(Path(p))==h for p,h in formal['source_snapshot_hashes'].items())
checks['formal_checker_current']=sha(base/'check_native_radar_formal.py')==formal['checker_sha256']
owner_path=root/'research/nima/results/comparison-kinetic-readout.json'
owner=json.loads(owner_path.read_text())
checks['owner_dependencies_current']=all(sha(root/'research/nima/agda'/f'{m}.agda')==h for m,h in owner['local_formal_import_sha256'].items())
checks['owner_receipt_inputs_current']=all(sha(root/Path(p))==h for p,h in owner['source_sha256'].items())
P=s.zeros(4)
for i,j in enumerate(owner['source_swap_images']):P[i,j]=1
v,x=s.symbols('v x',real=True)
F,U=s.symbols('F U',positive=True)
q=v/F
rt=s.sqrt(2)
probes={
 'angle':s.Matrix([s.cos(q),s.sin(q)/rt,-s.sin(q)/rt,0]),
 'ratio':s.Matrix([1,q/rt,-q/rt,0])/s.sqrt(1+q*q),
 'sine':s.Matrix([s.sqrt(1-q*q),q/rt,-q/rt,0])}
to_angle={'angle':v,'ratio':F*s.atan(q),'sine':F*s.asin(q)}
rows=[]
for name,n in probes.items():
    eq(name+'_unit_probe',n.dot(n),1)
    for i in range(4):
        eq(name+f'_same_state_{i}',probes['angle'][i].subs(v,to_angle[name]),n[i])
    overlap=s.simplify(n.dot(P*n))
    potential=-U*s.log(overlap)/2
    metric=s.simplify(F**2*n.diff(v).dot(n.diff(v)))
    eq(name+'_kinetic_pullback',metric,s.diff(to_angle[name],v)**2)
    eq(name+'_positive_vacuum_norm',metric.subs(v,0),1)
    mass=s.simplify(s.diff(potential,v,2).subs(v,0))
    lp=s.simplify(s.diff(potential,v,4).subs(v,0))
    gp=s.simplify(s.diff(potential,v,6).subs(v,0))
    a=s.simplify(s.diff(metric,v,2).subs(v,0)/4)
    b=s.simplify(s.diff(metric,v,4).subs(v,0)/48)
    le=s.simplify(lp-8*a*mass)
    ge=s.simplify(gp-40*a*lp+352*a*a*mass-144*b*mass)
    eq(name+'_mass',mass,2*U/F**2)
    eq(name+'_quartic',le,16*U/F**4)
    eq(name+'_canonical_sextic',ge,512*U/F**6)
    # Independently transport the quartic-truncated ANGLE action, not a fresh
    # quartic truncation in each chart (which would change the model).
    angle=to_angle[name]/F
    truncated=U*(angle**2+s.Rational(2,3)*angle**4)
    tm=s.simplify(s.diff(truncated,v,2).subs(v,0))
    tl=s.simplify(s.diff(truncated,v,4).subs(v,0))
    tg=s.simplify(s.diff(truncated,v,6).subs(v,0))
    eq(name+'_truncated_mass',tm,mass)
    eq(name+'_truncated_quartic',tl-8*a*tm,le)
    eq(name+'_truncated_canonical_sextic',tg-40*a*tl+352*a*a*tm-144*b*tm,0)
    rows.append(dict(chart=name,metric=str(metric),potential=str(potential),mass=str(mass),potential_quartic=str(lp),a=str(a),b=str(b),potential_sextic=str(gp),canonical_quartic=str(le),canonical_sextic=str(ge),unit_fixture=[str(z.subs({F:1,U:1})) for z in (mass,lp,2*a,gp,le,ge)]))
# Derive the sixth-order normalization formula for a general parity-even jet.
m,l,g,a,b=s.symbols('m l g a b')
canonical_map=v+a*v**3/3+(b/5-a*a/10)*v**5
inverse_map=x-a*x**3/3+(13*a*a/s.Integer(30)-b/5)*x**5
eq('canonical_metric_jet',s.series(s.diff(canonical_map,v)**2-(1+2*a*v*v+2*b*v**4),v,0,6).removeO())
eq('inverse_canonical_jet',s.series(canonical_map.subs(v,inverse_map)-x,x,0,7).removeO())
V=m*v*v/2+l*v**4/24+g*v**6/720
canon=s.series(V.subs(v,inverse_map),x,0,7).removeO()
eq('derived_quartic_formula',s.diff(canon,x,4).subs(x,0),l-8*a*m)
eq('derived_sextic_formula',s.diff(canon,x,6).subs(x,0),g-40*a*l+352*a*a*m-144*b*m)
checks['potential_only_reader_fails']=rows[1]['potential_quartic']=='0' and rows[1]['canonical_quartic']!='0'
checks['constant_quartic_not_authorized_over_scales']=s.diff(16*U/F**4,U)!=0
checks['sextic_refinement_distinguishes_models']=s.simplify(512*U/F**6)!=0
# A sixth-order reader that keeps only a but omits the v^4 metric term is wrong.
for name,gp,lp,a0,b0 in [('ratio',240,0,-1,s.Rational(3,2)),('sine',960,24,s.Rational(1,2),s.Rational(1,2))]:
    checks[name+'_dropping_metric_fourth_order_fails']=gp-40*a0*lp+352*a0*a0*2 !=512
    eq(name+'_metric_fourth_order_restores_sextic',gp-40*a0*lp+352*a0*a0*2-144*b0*2,512)
artifacts=[base/'agda/ActionChartComparison.agda',base/'check_action_chart_comparison.py',formal_path,owner_path,root/'research/nima/comparison-kinetic-readout.md',root/'research/nima/voevodsky-overlap-readout-gates-review.md']
result=dict(passed=all(checks.values()),checks=checks,charts=rows,
 domains={'angle':'|v/F|<pi/4','ratio':'|v/F|<1','sine':'|v/F|<1/sqrt(2)','scales':'F>0,U>0'},
 normalization={'quartic':'lambda_potential-8*a*m2','sextic':'g6_potential-40*a*lambda_potential+352*a^2*m2-144*b*m2','metric':'1+2*a*v^2+2*b*v^4+O(v^6)'},
 source_sha256={str(p.relative_to(root)):sha(p) for p in artifacts},
 scope='Formal fourth-order integer jet equivalences, authorized readers and refinement nonfactorization; symbolic real local chart/kinetic comparison and canonical sixth derivative for supplied analytic model. Not a computed full six-point amplitude or source-derived spacetime/kinetic policy.')
(base/'action-chart-comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print('passed=',result['passed'],'checks=',len(checks))
print('unit rows [m2,lambda_pot,2a,g6_pot,lambda_canonical,g6_canonical]:')
for row in rows:print(row['chart'],row['unit_fixture'])
raise SystemExit(0 if result['passed'] else 1)
