"""Replay the existing canonical six-port pulse energy, with no new dynamics.

Exact rational reconstruction of the source metric, centered projector,
Hamiltonian flow, action primitive and retained AB preparation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_source_pulse_particle_intertwiners import ROOT,PACKETS,eye,mm,transpose,difference
from check_belt_interface_response import inverse


def mv(M,v):return [sum(x*y for x,y in zip(row,v)) for row in M]
def add(*matrices):return [[sum(M[i][j] for M in matrices) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]
def scale(s,M):return [[s*x for x in row] for row in M]
def block(a,b):return [r+[F(0)]*len(b) for r in a]+[[F(0)]*len(a)+r for r in b]
def quadratic(M,v):return sum(x*y for x,y in zip(v,mv(M,v)))
def enc(M):return [list(map(str,row)) for row in M]


def main():
    root=ROOT/'research/strominger/results';priorpath=root/'source-pulse-particle-intertwiners.json'
    prior=json.loads(priorpath.read_text());assert prior['status']=='passed'
    for p,h in prior['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    labels=[a for a,_,_ in PACKETS];n=len(labels);ab=labels.index('AB')
    # f_ab=e_(a,b)/11 in (10I+ones) tensor (10I+ones).
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    indices=[('ABCD'.index(a),'ABCD'.index(b)) for _,a,b in PACKETS]
    D=[[G[a][c]*G[b][d]/121 for c,d in indices] for a,b in indices]
    K=add(eye(n),D);Ki=inverse(K)
    assert enc(K)==prior['source']['active_metric'] and mm(K,Ki)==eye(n)
    s=[D[i][ab] for i in range(n)];b=mv(Ki,s);mu=F(1)-sum(x*y for x,y in zip(s,b));assert mu>0
    metric=[[F(1)]+[-x for x in s]]+[[-s[i]]+K[i] for i in range(n)]
    center=[[F(1)]+[F(0)]*n]+[[b[i]]+eye(n)[i] for i in range(n)]
    assert mm(mm(transpose(center),metric),center)==block([[mu]],K)
    Z=[[F(0)]*n for _ in range(n)];J=[Z[i]+eye(n)[i] for i in range(n)]+[[-x for x in eye(n)[i]]+Z[i] for i in range(n)]
    budget=block(K,scale(F(1,4),Ki));Hs={};As={};endpoints={};checks={}
    for i,label in enumerate(labels):
        E=[[F(a==i and b==i) for b in range(n)] for a in range(n)]
        projector=scale(F(1,2),mm(E,K))
        assert mm(projector,projector)==projector
        # u=q+i Ki p/2, h=u* K projector u. Mixed imaginary terms cancel.
        realH=mm(K,projector)
        assert realH==transpose(realH)
        imaginaryH=scale(F(1,4),mm(mm(Ki,realH),Ki))
        H=block(realH,imaginaryH)
        assert H==block(scale(F(1,2),mm(mm(K,E),K)),scale(F(1,8),E))
        A=scale(F(2),mm(J,H));A2=mm(A,A)
        assert mm(A2,A)==scale(F(-1),A)
        assert add(mm(transpose(A),J),mm(J,A))==[[F(0)]*(2*n) for _ in range(2*n)]
        assert add(mm(transpose(A),H),mm(H,A))==[[F(0)]*(2*n) for _ in range(2*n)]
        assert add(mm(transpose(A),budget),mm(budget,A))==[[F(0)]*(2*n) for _ in range(2*n)]
        R=difference(eye(n),mm(E,K));endpoint=add(eye(2*n),scale(F(2),A2))
        assert endpoint==block(R,transpose(inverse(R)))
        assert enc(R)==prior['source']['active_pulses'][label]
        # Continuous complex intertwiner C A=-i projector C, C=I+i Ki/2.
        Cr=[r+[F(0)]*n for r in eye(n)]
        Ci=[[F(0)]*n+r for r in scale(F(1,2),Ki)]
        assert mm(Cr,A)==mm(projector,Ci)
        assert mm(Ci,A)==scale(F(-1),mm(projector,Cr))
        Hs[label]=H;As[label]=A;endpoints[label]=endpoint
        checks[label+'_source_projector_energy_flow_endpoint']=True
    assert mm(As['AB'],As['BA'])!=mm(As['BA'],As['AB'])
    checks['chronology_cannot_be_replaced_by_summed_flow']=True
    # Fixed reference c=1, only AB record initially occupied, y=0.
    # q=e_AB-b=Ki e_AB, p=0. Full source budget Q=1.
    q=[F(i==ab)-b[i] for i in range(n)];p=[F(0)]*n;initial=q+p
    assert q==[Ki[i][ab] for i in range(n)]
    assert mu+quadratic(budget,initial)==1
    expected_energy={label:F(label=='AB',2) for label in labels}
    assert {label:quadratic(H,initial) for label,H in Hs.items()}==expected_energy
    # Retain full canonical coordinates at each pulse start, midpoint and end.
    states=[];current=initial;endpoint_history=[]
    for step,label in enumerate(('AB','BA','AB','BA')):
        A=As[label];A2=mm(A,A);mid=mv(add(eye(2*n),A,A2),current);after=mv(endpoints[label],current)
        h=quadratic(Hs[label],current)
        assert quadratic(Hs[label],mid)==quadratic(Hs[label],after)==h
        assert all(mu+quadratic(budget,v)==1 for v in (current,mid,after))
        assert mv(endpoints[label],after)==current
        endpoint_history.append((label,current,after))
        states.append({'step':step,'port':label,'pulse_energy':str(h),
                       'start':list(map(str,current)),'midpoint':list(map(str,mid)),'end':list(map(str,after)),
                       'all_port_energies_at_start':{k:str(quadratic(H,current)) for k,H in Hs.items()},
                       'all_port_energies_at_end':{k:str(quadratic(H,after)) for k,H in Hs.items()}})
        current=after
    recovered=current
    for label,before,after in reversed(endpoint_history):
        recovered=mv(endpoints[label],recovered);assert recovered==before
    assert recovered==initial
    checks['retained_four_occurrence_history_exactly_reversed']=True
    checks['active_pulse_energy_conserved_at_exact_midpoints']=True
    checks['full_source_budget_one_at_every_snapshot']=True
    # Source action primitive in a fixed reference: -Im(u* K du)
    # = p dq - d(q^T p)/2. Check coefficient matrices, not endpoint values.
    Cr=[r+[F(0)]*n for r in eye(n)];Ci=[[F(0)]*n+r for r in scale(F(1,2),Ki)]
    primitive=difference(mm(mm(transpose(Ci),K),Cr),mm(mm(transpose(Cr),K),Ci))
    expected=[[F(0)]*(2*n) for _ in range(2*n)]
    for i in range(n):expected[n+i][i]=F(1,2);expected[i][n+i]=F(-1,2)
    assert primitive==expected
    checks['action_primitive_boundary_term_retained']=True
    Hsum=add(*Hs.values())
    assert quadratic(Hsum,initial)!=quadratic(Hsum,mv(endpoints['AB'],initial))
    checks['summed_port_energy_not_the_conserved_budget']=True
    result={'status':'passed','checks':checks,'labels':labels,'source_metric_K':enc(K),'anchor_mu':str(mu),
            'canonical_energy':'h_i=(Kq)_i^2/2+p_i^2/8; h=x^T H_i x and xdot=2J H_i x',
            'conserved_full_budget':'Q=mu |c|^2+q^T K q+p^T K^-1 p/4',
            'action_primitive':'p dq-Q dphi-d(q^T p)/2; fixed reference replay checks p dq-d(q^T p)/2',
            'source_preparation':'c=1, y=0, r=e_AB; supplied original preparation',
            'initial_active_budget':str(quadratic(budget,initial)),'initial_full_budget':'1',
            'initial_port_energies':{k:str(v) for k,v in expected_energy.items()},
            'pulse_hessians':{k:enc(scale(F(2),v)) for k,v in Hs.items()},'canonical_generators':{k:enc(v) for k,v in As.items()},
            'history':states,
            'interpretation':'This is the already source-bound canonical pulse energy, not a new particle Hamiltonian. Budget, active pulse Hamiltonian and a summed Hamiltonian are different observables. Parameter is pulse angle; no physical time/action conversion is supplied.'}
    paths=[Path(__file__).resolve(),Path(__file__).with_name('check_source_pulse_particle_intertwiners.py'),priorpath,ROOT/'research/nima/checkers/check_natural_tower_return.py',ROOT/'research/nima/checkers/check_relative_anchor_canonical_chart.py',ROOT/'research/voevodsky/checkers/check_belt_interface_response.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    dest=root/'canonical-source-energy.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','check_count':len(checks),'anchor_mu':str(mu),'initial_active_budget':result['initial_active_budget'],
                      'initial_port_energies':result['initial_port_energies'],'ordered_pulse_energies':[s['pulse_energy'] for s in states]},indent=2))

if __name__=='__main__':main()
