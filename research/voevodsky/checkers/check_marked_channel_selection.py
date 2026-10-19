"""Exact marked-axis selection and retained symmetric-quotient exclusion.
--record records this initial reviewed version; default validates freshness.
"""
import argparse
import json
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/marked-channel-selection.v1.json'
NOTE='research/voevodsky/marked-channel-selection-v1.md'
OUT='research/voevodsky/results/marked-channel-selection-v1.json'
NET='research/conjecture_net/contracts/rh-realization-work-net.v1.json'


def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(x,msg):
    if not x:raise ValueError(msg)
def clean(p):return {k:v for k,v in p.items() if v}
def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,Q(0))+v
    return clean(c)
def conv(a,b):
    c={}
    for x,v in a.items():
        for y,w in b.items():
            k=tuple(i+j for i,j in zip(x,y));c[k]=c.get(k,Q(0))+v*w
    return clean(c)
def axis(k,D,j):return tuple(k if i==j else 0 for i in range(D))
def embed(b,D,j):return {axis(k[0],D,j):v for k,v in b.items()}
def read(c,j):return {(n[j],):v for n,v in c.items() if all(x==0 for i,x in enumerate(n) if i!=j)}
def push(c,f):
    out={}
    for k,v in c.items():
        n=f(k);out[n]=out.get(n,Q(0))+v
    return clean(out)
def quadratic(n):return sum(x*x for x in n)
def chars(c,theta):return push(c,lambda n:sum(x*y for x,y in zip(n,theta))%1)


def source_paths():
    return [DEF,NOTE,Path(__file__).relative_to(ROOT).as_posix(),
      'research/nima/canonical-channel-tate-torus-fourier-functor.md',
      'research/nima/source-derivation-of-realization-choices.md',
      'research/voevodsky/additive-lattice-fourier-bridge-v1.md',
      'research/voevodsky/checkers/check_additive_lattice_fourier_bridge.py',
      'research/voevodsky/results/additive-lattice-fourier-bridge-v1.json',
      'research/voevodsky/riemann-comb-specialization-v1.md',
      'research/voevodsky/checkers/check_riemann_comb_specialization.py',
      'research/voevodsky/results/riemann-comb-specialization-v1.json']


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--record',action='store_true');args=ap.parse_args()
    s=load(DEF);require(not any(s['boundaries'].values()),'selection promotion')
    checks=[];hostiles=[]
    def check(name,test):require(test,name);checks.append(name)
    for D in (2,3,20,54):
        j=0;k=1;v=axis(1,D,k);zero=axis(0,D,j)
        b={(0,):Q(1),(1,):Q(2),(-2,):Q(-1,3)}
        a={(1,):Q(1),(-1,):Q(3)}
        E=embed(b,D,j);off={v:Q(5)};c=add(E,off)
        r=read(c,j);N=add(c,{n:-w for n,w in embed(r,D,j).items()})
        check(f'reconstruction/D={D}',add(embed(r,D,j),N)==c and read(N,j)=={})
        check(f'axis convolution/D={D}',embed(conv(a,b),D,j)==conv(embed(a,D,j),E))
        check(f'axis unary convolution on whole source/D={D}',read(conv(embed(a,D,j),c),j)==conv(a,read(c,j)))
        theta=tuple(Q(i+1,7) for i in range(D))
        check(f'Fourier character embedding/D={D}',chars(E,theta)==chars(b,(theta[j],)))
        for factor in (2,4,8):
            bond=lambda n:tuple(factor*x for x in n)
            check(f'bonding/D={D}/factor={factor}',read(push(c,bond),j)==push(read(c,j),bond))
            h=Q(1,factor);check(f'physical mesh/D={D}/factor={factor}',all(tuple(h*x for x in bond(n))==n for n in c))
        perm=list(range(D));perm[0],perm[1]=perm[1],perm[0]
        sigma=lambda n:tuple(n[perm.index(i)] for i in range(D))
        check(f'mark covariance/D={D}',read(push(c,sigma),perm[j])==read(c,j))
        check(f'heat restriction/D={D}',all(quadratic(axis(n[0],D,j))==n[0]**2 for n in b))
        # Lost directions can return under operations outside the licensed task.
        w=tuple(-x for x in v)
        require(read(conv({v:Q(1)},{w:Q(1)}),j)=={(0,):Q(1)} and conv(read({v:Q(1)},j),read({w:Q(1)},j))=={},'missing convolution hostile')
        require(read(push({v:Q(1)},sigma),j)!={},'missing frozen mark hostile')
        hostiles += [f'whole-source convolution/D={D}',f'permutation with frozen mark/D={D}']
        kernel=tuple(1 if i==0 else -1 if i==1 else 0 for i in range(D))
        check(f'symmetric sum heat obstruction/D={D}',sum(kernel)==0 and quadratic(kernel)==2 and quadratic(zero)==0)
        check(f'symmetric finite convolution/D={D}',push(conv(c,c),lambda n:(sum(n),))==conv(push(c,lambda n:(sum(n),)),push(c,lambda n:(sum(n),))))
    # Unit l2 packets on an arbitrarily long sum-zero fibre have unbounded image norm.
    ratios=[]
    for m in (1,4,9,16):
        packet={(n,-n):Q(1) for n in range(m)};image=push(packet,lambda n:(sum(n),))
        src=sum(x*x for x in packet.values());dst=sum(x*x for x in image.values())
        check(f'unbounded sum reader/m={m}',dst/src==m);ratios.append(m)
    for D in (2,3,20,54):
        for t in (Q(1,2),Q(1),Q(3)):
            # Exponent accounting for the transverse Gaussian integral in odd chart.
            check(f'one-dimensional theta exponent/D={D}/t={t}',Q(-D,2)+Q(D-1,2)==Q(-1,2))
    for p in ('research/voevodsky/results/additive-lattice-fourier-bridge-v1.json','research/voevodsky/results/riemann-comb-specialization-v1.json'):
        require(load(p)['passed'],'upstream receipt failed')
    result=dict(schema='marici.marked-channel-selection-validation.v1',passed=True,
      selection='constructed_for_explicitly_pointed_source_and_licensed_axis_task',
      symmetric_full_heat_quotient='rejected_for_D_ge_2',
      checks=checks,hostiles_retained=hostiles,sum_reader_squared_norm_ratios=ratios,
      analytic_claims_basis='Owner-local proof in note; exact finite tests are not proofs of infinite theta or l2 bounds.',
      canonical_unmarked_selection=False,physical_selection_admitted=False,source_suites_rerun=False,
      source_sha256={p:sha(p) for p in source_paths()})
    if args.record:
        require(not (ROOT/OUT).exists(),'refusing implicit selection overwrite')
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    else:
        require(load(OUT)==result,'selection source drift')
        by={n['id']:n for n in load(NET)['conjectures']}
        for n,v in [('symmetric-full-heat-selection','rejected'),('marked-axis-source-selection','constructed'),('one-dimensional-source-selection','constructed')]:
            require(by[n]['status']=='resolved' and by[n]['verdict']==v and by[n]['evidence']==['marked-channel-selection'],'selection verdict/evidence mismatch')
    print(json.dumps(dict(passed=True,exact_checks=len(checks),hostiles_retained=len(hostiles),
       symmetric_full_heat_quotient_rejected=True,canonical_unmarked_selection=False,physical_selection_admitted=False),indent=2))


if __name__=='__main__':main()
