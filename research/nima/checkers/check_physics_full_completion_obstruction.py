"""A continuum of CP completions with identical adaptive classical-record laws."""
import argparse
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_dynamics_selection_audit as D
import check_physics_observation_resource_interface as O

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-full-completion-obstruction.v1.json'


def maps():
    vr=D.transition(0,0,F(1));ds=D.transition(2,2,F(4,5))
    click=[D.transition(2,1,F(3,5))]
    rest=[D.transition(0,1,F(4,5)),D.transition(0,2,F(3,5)),D.transition(0,3,F(3,5)),D.transition(2,3,F(4,5))]
    return {'C':click,'N':[vr,ds]+rest},{'C':click,'N':[D.matadd(vr,ds)]+rest}


def mix(lam,a,b):return [[(1-lam)*x+lam*y for x,y in zip(row,other)] for row,other in zip(a,b)]


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    G.require(c['decision']=='reject_full_CP_identification_from_classical_records'
              and c['physical_realization_admitted'] is False and c['empirical_exclusions']==[],'scope promotion')
    reference,alternative=maps();lambdas=[F(i,8) for i in range(9)]
    table={};diagonal_checks=0
    for lam,y,i in itertools.product(lambdas,'CN',range(4)):
        rho=D.transition(i,i,F(1));a=D.apply(reference[y],rho);b=D.apply(alternative[y],rho)
        G.require(a==b,'endpoint diagonal alias')
        result=mix(lam,a,b)
        G.require(result==a,'completion parameter leaks to classical map')
        G.require(all(result[j][k]==0 for j,k in itertools.product(range(4),repeat=2) if j!=k),'classical algebra not preserved')
        table[lam,y,i]=(result[0][0],result[2][2]);diagonal_checks+=1
    for lam in lambdas:
        for i in range(4):G.require(sum(sum(table[lam,y,i]) for y in 'CN')==1,'family normalization')
    coherent=D.zero()
    for i,j in itertools.product((0,2),repeat=2):coherent[i][j]=F(1,2)
    a=D.apply(reference['N'],coherent);b=D.apply(alternative['N'],coherent)
    for lam in lambdas:
        output=mix(lam,a,b)
        G.require(output[0][2]==F(2,5)*lam and output[0][2]+output[2][0]==F(4,5)*lam,'distinct completion family')
    # All deterministic public-record input policies over depth three: seven bits.
    cases=0
    for policy,ready,lam in itertools.product(range(128),(F(0),F(1,2),F(1)),lambdas):
        total=F(0)
        for word in itertools.product('CN',repeat=3):
            state=(ready,1-ready);expected=state;index=0
            for y in word:
                n=(policy>>index)&1;r,d=state
                rr,rd=table[lam,y,n];dr,dd=table[lam,y,2+n]
                state=(r*rr+d*dr,r*rd+d*dd)
                expected=O.step(n,y,expected)
                G.require(state==expected,'adaptive policy alias fails')
                index=2*index+1+int(y=='N')
            total+=sum(state);cases+=1
        G.require(total==1,'adaptive complete-word normalization')
    # Exact polynomial endpoint risk identity, independent of the record distribution.
    risk_controls=0
    for t in (F(i,8) for i in range(-8,17)):
        average=(t*t+(t-1)**2)/2
        G.require(average==(t-F(1,2))**2+F(1,4)>=F(1,4),'minimax endpoint bound')
        risk_controls+=1
    G.require(max(F(1,2)**2,(F(1,2)-1)**2)==F(1,4),'constant estimator sharpness')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','disposition':c['decision'],
         'completion_parameters_tested':len(lambdas),'diagonal_outcome_maps':diagonal_checks,
         'all_depth_three_deterministic_policies':128,'adaptive_complete_word_cases':cases,
         'channel_family_distinct':True,'classical_record_law_constant_in_parameter':True,
         'worst_case_squared_error_lower_bound':'1/4','sharp_constant_estimator':'1/2',
         'risk_polynomial_controls':risk_controls,'physical_realization_admitted':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
