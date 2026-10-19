#!/usr/bin/env python3
"""Positive radial resolution and actual contracted exceptional target image."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize, target_jac
from check_paired_composite_corner_residues import raw_bracket
ROOT=Path(__file__).resolve().parents[3]
PRIOR='research/benincasa/results/history6_b3_boundary.json'
CHART='research/benincasa/results/history6_common_corner.json'
WEIGHT='research/benincasa/results/history6_quotient_boundary.json'


def main():
    prior=json.loads((ROOT/PRIOR).read_text());chart=json.loads((ROOT/CHART).read_text());weight=json.loads((ROOT/WEIGHT).read_text())
    for receipt in (prior,chart,weight):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    t,r=s.symbols('t rho');variables=[b1,t,r,b4,b5,b6,b7,b8]
    C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])
    g=s.sympify(weight['source_c6'],locals={str(z):z for z in b})
    change={b2:r*t,b3:t};Cr=C.subs(change,simultaneous=True)
    gr=s.factor(g.subs(change,simultaneous=True));hr=s.factor(1-gr)
    source_map=s.Matrix([z.subs(change,simultaneous=True) for z in b])
    logJ=s.diag(*[1/z for z in source_map])*source_map.jacobian(variables)*s.diag(*variables)
    logdet=s.factor(logJ.det());assert logdet==-1
    # Transformed top coefficient -1; delete t at index1, parity-1.
    exceptional=s.factor((-1)*(-1))
    f0=s.factor(gr.subs(t,0));fB=s.factor(hr.subs(t,0))
    assert f0==1/(r+1) and fB==r/(r+1) and s.factor(f0+fB-1)==0
    assert s.diff(f0,r)!=0
    corner=Cr.subs(t,0);assert corner.diff(r)==s.zeros(2,8)
    assert Cr.diff(r)==t*C.diff(b2).subs(change,simultaneous=True)
    assert s.factor(s.residue((-gr)/t,t,0))==-f0
    # Signs above refer to coefficient in the transformed top order;
    # exceptional residue additionally has deletion parity-1.
    runs=[]
    for shift,values in enumerate(([2,0,3,7,11,13,17,19],[3,0,5,11,13,17,19,23])):
        v=dict(zip(variables,map(s.Integer,values)))
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        Cn=Cr.subs(v);N=normalize(Cn*Z,[0,1])
        assert all(Cn[:,list(I)].det()>=0 for I in itertools.combinations(range(8),2))
        J,coords=target_jac(Cn*Z,[Cr.diff(z).subs(v)*Z for z in variables],[0,1])
        free=[j for j in range(8) if j!=1]
        assert J[:,free].rank()==6 and J.rank()==7
        assert J[:,2]==s.zeros(8,1)
        assert len(J[:,free].nullspace())==1
        # The original (unblown) germ at the same source corner is regular
        # eight-dimensional; the exceptional contraction is the blowdown.
        oldv={b1:v[b1],b2:0,b3:0,b4:v[b4],b5:v[b5],b6:v[b6],b7:v[b7],b8:v[b8]}
        Jold,_=target_jac(C.subs(oldv)*Z,[C.diff(z).subs(oldv)*Z for z in b],[0,1]);assert Jold.rank()==8
        alt=v|{r:v[r]+1};assert normalize(Cr.subs(alt)*Z,[0,1])==N
        assert gr.subs(v)!=gr.subs(alt)
        pulls={str(q):s.factor(raw_bracket(Cr,Z,q)) for q in ((1,2,6,8),(1,2,3,8),(5,8,1,2),(6,1,2,3))}
        assert all(q.subs(t,0)==0 for key,q in pulls.items() if key!=str((6,1,2,3)))
        assert pulls[str((6,1,2,3))].subs(v)!=0
        assert f0.subs(v)>0 and fB.subs(v)>0
        # No invertible 8x8 normal chart Jacobian exists on the blowdown
        # exceptional boundary: its rank is7 and boundary rank6.
        assert J.det()==0
        runs.append({'positive_Z_moment_shift':shift,'radial_boundary_parameters':{str(z):str(q) for z,q in v.items()},
            'exceptional_source_form_dimension':7,'exceptional_target_rank':6,'radial_full_germ_target_rank':7,
            'original_unblown_germ_rank':8,'rho_target_tangent':'zero','positive_same_target_fiber':{
                'rho_values':[str(v[r]),str(alt[r])],'K0_weights':[str(gr.subs(v)),str(gr.subs(alt))],
                'B22_weights':[str(hr.subs(v)),str(hr.subs(alt))]},
            'raw_bracket_pullbacks':{key:str(q) for key,q in pulls.items()},
            'ordinary_target_exceptional_seven_form_residue':'unavailable_rank6_not_zero',
            'corner_scalar_coefficient_descent':'fails_rho_dependence_on_actual_positive_fiber'})
    # Exceptional pole rho=-1 lies outside rho>0 but has nonzero split
    # residues; signs include deletion of rho from seven-coordinate order.
    pole0=s.factor(-s.residue(f0/r,r,-1));poleB=s.factor(-s.residue(fB/r,r,-1))
    assert pole0==1 and poleB==-1
    u=s.Symbol('u');inverse0=s.factor(f0.subs(r,1/u));inverseB=s.factor(fB.subs(r,1/u))
    assert inverse0.subs(u,0)==0 and inverseB.subs(u,0)==1
    paths=[PRIOR,CHART,WEIGHT,'research/benincasa/checkers/check_history6_b3_boundary.py',
        'research/benincasa/checkers/check_three_composite_internal_gluings.py','research/benincasa/checkers/check_paired_composite_corner_residues.py']
    out={'schema':'marici.benincasa.history6-radial-resolution.v1','history_index':6,
        'source_change':{'b2':'rho*t','b3':'t','ordered_coordinates':[str(z) for z in variables],
            'eight_log_transition_determinant':str(logdet),'t_deletion_parity':-1},
        'resolved_weight':str(gr),'resolved_B22_weight':str(hr),
        'exceptional_source_residue':{'remaining_order':[str(z) for z in variables if z!=t],
            'transported_coefficient':str(exceptional),'K0_coefficient':str(f0),'B22_coefficient':str(fB),
            'localization':'rho>0; b1,b4,b5,b6,b7,b8>0; t=0 in the resolved chart; rho=-1 excluded'},
        'exceptional_meromorphic_pole':{'normal':'rho+1','K0_six_log_residue_coefficient':str(pole0),
            'B22_six_log_residue_coefficient':str(poleB),'sum':'0'},
        'direction_endpoints':{'rho0_weights':['1','0'],'rho_infinity_weights':['0','1'],
            'infinity_orientation':'dlog rho=-dlog u for u=1/rho; coefficient values alone are not signed endpoint residues'},
        'runs':runs,'passed':True,
        'scope':'Actual resolved positive source chart and blowdown target rank/fiber; no ordinary target exceptional seven-form or arbitrary integration over the lost rho direction is invented.',
        'next_action':'Construct the actual target blowup using the regular unblown F6 inverse: t=b3(Y), rho=b2(Y)/b3(Y), plus six surviving inverse source coordinates. Verify inverse arcs and a residue square on this decorated target, separately from the unavailable ordinary blowdown residue and physical supercomponent map.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_radial_resolution.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'resolved_weight':str(gr),'exceptional_weights':[str(f0),str(fB)],
        'rank_dispositions':[[r['exceptional_target_rank'],r['radial_full_germ_target_rank'],r['original_unblown_germ_rank']] for r in runs],
        'ordinary_target_residue':'unavailable_not_zero'},indent=2))

if __name__=='__main__':main()
