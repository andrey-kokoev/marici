"""Exact rational empty-bin continuation obstruction; no acquisition or fitting."""
import json
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
NOTE='research/voevodsky/neutral-record-detector-binding-obstruction-v1.md'
OUT='research/voevodsky/results/neutral-record-detector-binding-obstruction-v1.json'

def require(ok,msg):
    if not ok:raise ValueError(msg)
def main():
    # cos(sqrt(2)): alternating terms 2^k/(2k)! decrease strictly.
    partial=lambda n:sum((Q((-1)**k*2**k,factorial(2*k)) for k in range(n+1)),Q(0))
    low,high=partial(9),partial(10)
    require(Q(3,20)<low<high<Q(4,25),'cosine enclosure')
    # f(c)=c(1-c)/2 increasing on this interval; exact structural margin.
    margin=low*(1-low)/2
    require(margin>Q(3,50),'continuation gap')
    p1low,p1high=(1-high)/4,(1-low)/4
    p2low,p2high=(1-high*high)/2,(1-low*low)/2
    require(p1low>0 and p2low>2*p1high,'two-step hostile')
    # Any classical recovery parameter: q2=2q1-q1^2 <=2q1.
    for gamma in (Q(0),Q(1,4),Q(1,2),Q(1)):
        q2=2*gamma-gamma*gamma
        require(0<=q2<=1 and q2<=2*gamma,'recovery constraint')
    require(margin>3*Q(1,100),'two-time tolerance separation')
    net=json.loads((ROOT/'research/voevodsky/results/retained_reaggregation_conjecture_net.json').read_text())
    require(net['validation_passed'] and net['target_outcome']=='++' and not net['physical_admission'],'conditional source state')
    paths=[NOTE,'research/voevodsky/retained-comparison-closure.v1.md',
           'research/voevodsky/contracts/retained-reaggregation-source-k.v1.json',
           'research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json',
           'research/nima/physics-detector-law-inverse-v1.md',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.neutral-record-detector-binding-obstruction.v1',passed=True,
                candidate='basis-label bijection to classical readiness with unchanged empty-bin continuation and fixed gamma',
                verdict='rejected_at_declared_model_scope',both_label_assignments_rejected=True,
                cosine_interval=[str(low),str(high)],p1_interval=[str(p1low),str(p1high)],
                p2_interval=[str(p2low),str(p2high)],p2_minus_2p1_lower_bound=str(margin),
                epsilon_one_over_100_bridge_rejected=True,
                larger_or_driven_quantum_memory_refuted=False,physical_admission=False,
                proof_level='written two-state law argument plus exact rational alternating-series bounds',
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
