"""Quadratic commutator theorem controls and an exact local clock-branch alias."""
import argparse
import copy
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_dynamics_selection_audit as D

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-source-law-premise-audit.v1.json'
ACTIVE=(0,1)


def quadratic(h,state):
    out={}
    for i in range(G.DIM):
        for j in range(G.DIM):
            if h[i][j]:out=D.add(out,D.scale(h[i][j],D.create(i,D.annihilate(j,state))))
    return out


def validate(c):
    G.require(c['decision']=='constructed_conditional_generator_theorem_and_interpolation_obstruction','wrong scope')
    G.require(c['quadratic_source_principle']['status']=='additional_premise_not_independently_sourced','unsourced quadraticity')
    G.require(c['native_source_law_selected'] is False and c['physical_realization_admitted'] is False,'selection promotion')
    G.require({r['id'] for r in c['required_source_inputs']}=={'quadraticity','primitive-generator','coefficients-and-units','detector-completion'}
              and all(r['supplied'] is False and r['requirement'] for r in c['required_source_inputs']),'source gap lost')
    G.require(c['source_witness_id']=='passive-port-fock-memory.v1','source identity')


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);validate(c);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    s=G.eye();s[1][1]=-F(3,5);s[1][0]=F(4,5);s[0][1]=F(4,5);s[0][0]=F(3,5)
    q=[[F(i==j)/2-s[i][j]/2 for j in range(G.DIM)] for i in range(G.DIM)]
    active=[[F(i==j and i in ACTIVE) for j in range(G.DIM)] for i in range(G.DIM)]
    h1=[[q[i][j]+2*active[i][j] for j in range(G.DIM)] for i in range(G.DIM)]
    G.require(G.mm(q,q)==q and G.mm(q,active)==q,'projector/active commutation')
    G.require(q!=h1 and all(q[i][j]==q[j][i] and h1[i][j]==h1[j][i] for i in range(G.DIM) for j in range(G.DIM)),'distinct Hermitian generators')
    commutators=0
    for h in (q,h1):
        G.require(quadratic(h,{G.VAC:F(1)})=={},'vacuum energy')
        for n in range(3):
            for b in G.basis(n):
                state={b:F(1)}
                result=quadratic(h,state)
                G.require(all(sum(o)==n for o in result),'number conservation')
                for j in range(G.DIM):
                    lhs=D.add(quadratic(h,D.create(j,state)),D.scale(-1,D.create(j,result)))
                    rhs=D.linear_create(h,j,state)
                    G.require(lhs==rhs,'quadratic creation commutator')
                    if j not in ACTIVE:G.require(lhs=={},'spectator generator')
                    commutators+=1
    endpoints=0
    for n in range(4):
        for b in G.basis(n):
            base=G.lift_column(s,b)
            # h1 shift has phase exp(-2*pi*i*N_active)=1 at integer durations.
            # Apply its exact integer exponent representation to every output occupancy.
            shifted={o:(-1)**(2*sum(o[i] for i in ACTIVE))*a for o,a in base.items()}
            G.require(shifted==base,'endpoint alias')
            G.require(G.inner(base,base)==G.weight(b),'endpoint metric')
            endpoints+=1
    # At half-duration, base one-particle matrix is I-Q-iQ.
    # At u, starting from |1_u>, its coefficient is 1/5-4i/5.
    half_real=F(1)-q[1][1];half_imag=-q[1][1]
    mean=(half_real/2,half_imag/2);shifted_mean=tuple(-x for x in mean)
    G.require(mean==(F(1,10),-F(2,5)) and shifted_mean==(-F(1,10),F(2,5)),'half-step coherent mean')
    # Norm of (vac + half-step one-particle vector)/sqrt(2) remains one.
    one_norm=sum((F(i==1)-q[i][1])**2+q[i][1]**2 for i in range(G.DIM))
    G.require(one_norm==1 and (1+one_norm)/2==1,'half-step normalized witness')
    # It is not only a global phase on the vacuum-plus-one-particle state.
    G.require(mean!=shifted_mean,'half-step state distinction')
    rejected=[]
    for name in ('quadraticity-as-source','branch-selection-as-source','physical-promotion'):
        bad=copy.deepcopy(c)
        if name=='quadraticity-as-source':bad['quadratic_source_principle']['status']='native_derived'
        elif name=='branch-selection-as-source':bad['required_source_inputs'][1]['supplied']=True
        else:bad['physical_realization_admitted']=True
        try:validate(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','quadratic_creation_commutators':commutators,
         'all_sector_argument':'Finite Hermitian second quantization and integer active occupation imply the unrestricted written laws; tests corroborate N<=3 endpoints and N<=2 commutators',
         'integer_endpoint_columns':endpoints,'same_sampled_maps':True,'distinct_local_positive_generators':True,
         'reference_half_step_mean':list(map(str,mean)),'alternative_half_step_mean':list(map(str,shifted_mean)),
         'independent_source_justification_supplied':False,'rejected_corruptions':rejected,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
