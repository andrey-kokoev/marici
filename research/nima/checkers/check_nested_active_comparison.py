"""Nested whole-composite comparison using the prior reversible projection lift.

Coordinates are comparison data, not electron positions/energies. The rule and
Euclidean pairing are declared inputs, not a native physical attachment law.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
R=(F(1),F(-1),F(0))
S=(F(1),F(1),F(-2))
RP=(F(1),F(0),F(-1))
SP=(F(1),F(-2),F(1))


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def lift(q,r,z=F(0)):
    n=dot(r,r);a=dot(r,q)/n
    out=tuple(x+v*(z-a) for x,v in zip(q,r))
    assert dot(out,out)+n*a*a==dot(q,q)+n*z*z
    return out,a


def route(q,r,s):
    assert dot(r,s)==0
    middle,a=lift(q,r)
    end,b=lift(middle,s)
    assert dot(r,middle)==dot(r,end)==dot(s,end)==0
    assert end==(sum(q)/3,)*3
    # Inverse uses the retained record: no mismatch is erased.
    recovered_middle,empty_b=lift(end,s,b)
    recovered,empty_a=lift(recovered_middle,r,a)
    assert recovered_middle==middle and recovered==q
    assert empty_a==empty_b==0
    costs=(dot(r,r)*a*a,dot(s,s)*b*b)
    assert dot(q,q)==dot(end,end)+sum(costs)
    return middle,end,(a,b),costs


def main():
    count=0
    for values in product(range(-2,3),repeat=3):
        q=tuple(map(F,values))
        _,end,(a,b),costs=route(q,R,S)
        _,other,(ap,bp),other_costs=route(q,RP,SP)
        assert end==other
        assert ap==(a+3*b)/2 and bp==(a-b)/2
        assert (ap+3*bp)/2==a and (ap-bp)/2==b
        assert 2*ap*ap+6*bp*bp==2*a*a+6*b*b
        assert sum(costs)==sum(other_costs)
        count+=1
    # Exact basis checks certify the linear maps, not merely sampled inputs.
    for q in ((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))):
        assert route(q,R,S)[1]==(F(1,3),)*3
        assert route(q,RP,SP)[1]==(F(1,3),)*3
    q=(F(1),F(2),F(4))
    middle,end,records,costs=route(q,R,S)
    other_middle,other_end,other_records,other_costs=route(q,RP,SP)
    assert middle!=other_middle and records!=other_records
    assert costs==(F(1,2),F(25,6)) and other_costs==(F(9,2),F(1,6))
    # Counterexample to replacing the whole composite by its original core:
    # the second pairwise equality reopens the first comparison.
    seed=(F(1),F(0),F(0))
    first,_=lift(seed,R)
    wrong,_=lift(first,RP)
    right=route(seed,R,S)[1]
    assert dot(R,wrong)==F(-1,4) and dot(R,right)==0
    assert wrong!=right
    # Common geometric criterion in this declared projection realization:
    # r.s=0 means the second correction preserves the first hyperplane.
    assert dot(R,S)==0 and dot(R,RP)==1
    result=dict(schema='marici.nima.nested-active-comparison.v1',status='pass',
                obligation='whole-composite attachment compatibility and invertible transport of retained mismatch records',
                source_rule='comparison-update-dynamics-and-energy-normalization.md: exact memory lift of projection',
                data_type='three real comparison coordinates (core, first witness, second witness), rational fixtures',
                constraints={'first':'x0-x1=0','second_whole_composite':'x0+x1-2*x2=0'},
                lift='a=(r.q)/(r.r); q_next=q+r*(z-a); z_next=a, with fresh z=0 for forward comparisons',
                tests=count,linear_basis_tests=3,
                fixture=dict(input=list(map(str,q)),first_middle=list(map(str,middle)),
                             reverse_middle=list(map(str,other_middle)),common_output=list(map(str,end)),
                             first_records=list(map(str,records)),reverse_records=list(map(str,other_records)),
                             first_budget_split=list(map(str,costs)),reverse_budget_split=list(map(str,other_costs))),
                record_transport=[['1/2','3/2'],['1/2','-1/2']],
                transport_metric=[['2','0'],['0','6']],
                bad_core_only_second_comparison_residual='-1/4',
                disposition='Whole-composite comparison preserves the first agreement; both orders reach the same barycenter. Distinct stage records are related by an explicit involutive isometry, not erased.',
                residual='The Euclidean comparison law is supplied. Preserved quadratic budget is not physical energy, and neither binding nor an electron attachment rate is inferred. No unique native selection of this law is proved.')
    (ROOT/'results/nested-active-comparison.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
