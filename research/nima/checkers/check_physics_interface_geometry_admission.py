"""Review integration squares and a gain-robust coherent-mean discriminator."""
import argparse
import json
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-interface-geometry-admission.v1.json'
TEST='research/nima/contracts/physics-phase-discriminator.v1.json'

def require(ok,why):
    if not ok:raise ValueError(why)

def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def sqrt_box(x):
    scale=10**8;n=isqrt(x.numerator*scale*scale//x.denominator)
    lo,hi=F(n,scale),F(n+1,scale)
    require(lo*lo<=x<=hi*hi,'square-root enclosure')
    return lo,hi

def exp_minus(x,n=24):
    require(x>=0 and x<n+2,'exponential domain')
    term=F(1);partial=term
    for k in range(1,n+1):term*=x/k;partial+=term
    first_omitted=term*x/(n+1)
    tail_bound=first_omitted/(1-x/(n+2))
    return 1/(partial+tail_bound),1/partial

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);test=load(TEST)
    paths={CONTRACT,TEST,c['interface'],c['geometry'],c['dynamics_audit'],
        'research/nima/physics-geometric-candidate-v1.md',
        'research/nima/checkers/check_physics_geometric_candidate.py',
        'research/nima/checkers/check_physics_observation_resource_interface.py',
        'research/conjecture_net/contracts/programme-source-interface.v1.json',
        'research/aspect/checkers/finite_dead_time_photodetection_memory_instrument.py'}
    pin=ROOT/c['source_pins']
    if args.pin:
        require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);require(set(pins['source_sha256'])==paths,'pin coverage')
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source drift: '+p)
    require(set(c['accepted_nodes'])=={'observation-resource-interface','geometric-realization-binding'},'admission scope')
    require(c['physical_realization_admitted'] is False,'physical promotion')
    sc=load('research/conjecture_net/contracts/programme-source-interface.v1.json')['source_record_contract']
    for r in c['source_register_supplement']['ingredient_records']:
        require(all(r.get(k) for k in sc['required_fields']) and r['role'] in sc['roles'],'supplement provenance')
        require(all(r['origin'].get(k) for k in sc['origin_required_fields']),'supplement origin')
    # Separate field replay and ten-mode realization for all complex basis directions.
    # Matrices are real here; equality extends separately to imaginary components.
    squares=0
    for j in range(10):
        state=[F(i==j) for i in range(10)];direct=state[:]
        for k in range(3):
            u,v,w=1+3*k,2+3*k,3+3*k
            yr,yt,xn,ye=O.cavity(direct[u],direct[0],direct[v],direct[w])
            direct[u],direct[0],direct[v],direct[w]=yr,xn,yt,ye
            matrix=G.round_map(k);state=[sum(row[i]*state[i] for i in range(10)) for row in matrix]
            require(state==direct,'interface/geometric history square');squares+=1
    b=test['design_calibration_boxes'];l1,h1=map(F,b['lambda1']);l2,h2=map(F,b['lambda2']);rlo,rhi=map(F,b['relative_readout_gain'])
    require(0<l1<=h1<l2<=h2 and 0<rlo<=rhi,'independent nuisance box')
    ref_lo=rlo*sqrt_box(l2/h1)[0]/2;ref_hi=rhi*sqrt_box(h2/l1)[1]/2
    alt_lo=ref_lo*exp_minus(2*(h2-l1))[0];alt_hi=ref_hi*exp_minus(2*(l2-h1))[1]
    eps=F(test['epsilon']);separator=F(test['structural_separator'])
    require(alt_hi+eps<separator<ref_lo-eps,'robust prediction separation')
    require(test['data'] is None,'fixtures promoted to data')
    # Nominal exponential lies inside its independently computed nuisance enclosure.
    nominal=exp_minus(F(3,2));require(alt_lo<=nominal[0]<=nominal[1]<=alt_hi,'nominal enclosure')
    for x in (F(0),F(1,2),F(3,2),F(2)):
        coarse=exp_minus(x,12);fine=exp_minus(x,24)
        require(coarse[0]<=fine[0]<=fine[1]<=coarse[1],'Taylor-tail enclosure consistency')
    # Using an unbounded between-setting gain destroys the separation: choose r=exp(3/2).
    require(F(1)/nominal[1]>rhi,'gain-drift alias outside required calibration box')
    out={'schema':c['schema'],'status':'pass','accepted_nodes':c['accepted_nodes'],
        'independent_three_round_basis_squares':squares,
        'phase_test':{'reference_interval':[str(ref_lo),str(ref_hi)],'rival_interval':[str(alt_lo),str(alt_hi)],
            'display_reference_interval':[float(ref_lo),float(ref_hi)],'display_rival_interval':[float(alt_lo),float(alt_hi)],
            'epsilon':str(eps),'separator':str(separator),'separated_with_error_margin':True,
            'unbounded_gain_alias_detected':True,'acquired_data':False},
        'source_sha256':pins['source_sha256'],'checker_sha256':sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
