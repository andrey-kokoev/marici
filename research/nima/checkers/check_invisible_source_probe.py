"""A genuine invisible source direction and an admitted vacuum probe."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction as Q
from math import factorial,comb
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def main():
    certificate=load('certified_source','certify_observer_source_lift.py')
    certificate.main() # fresh actual-theta bounds and source-column audit
    t=load('observer_tower','check_all_depth_observer_tower.py')
    f=t.f
    k=f['chain_product']([f['relation']((2*i,2*i+1),0) for i in range(3)])
    assert len(k)==8 and all(abs(c)==1 for c in k.values())
    assert all(sum(marks)==0 and len(word)==6 for word,marks in k)
    for order in (1,2):assert not t.ordered(0,k,order)
    image=t.ordered(0,k,3)
    key=((('e',0,1,0),('e',3,7,0),('e',15,31,0)),((),(),(),()))
    assert image[key]==1 and not f['balanced_boundary'](image)
    for selected,weight in t.selected(3):assert image.get(selected,0)==0
    v0=f['chain_product']([f['relation']((0,1),1),f['relation']((2,3),1),f['relation']((4,5),0)])
    vx=f['chain_product']([f['relation']((0,2),1),f['relation']((1,3),1),f['relation']((4,5),0)])
    assert t.ordered(0,v0,3).get(key,0)==0
    assert t.ordered(0,vx,3).get(key,0)==0
    assert not set(k).intersection(v0) and not set(k).intersection(vx)
    # Audit real path suffix contexts. The first required feature is absent
    # even when the suffix has enough retained events for total degree to fit.
    contexts=0;degree_sufficient=0
    for r in (3,4,5):
        suffix_events=tuple(range(6,2*r))
        for suffix in permutations(suffix_events):
            for flags in product((0,1),repeat=len(suffix)):
                for (word,marks),coefficient in k.items():
                    fullword=word+suffix;fullmarks=marks+flags
                    positions={j:i for i,j in enumerate(fullword)}
                    assert fullmarks[positions[0]]==fullmarks[positions[1]]==0
                if sum(flags)>=r-1:degree_sufficient+=1
                contexts+=1
    assert degree_sufficient>0
    ctx.prec=192;pi=arb.pi();q0=4*pi
    H=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
    tail=sum((arb(comb(10,j)*factorial(j))*q0**(10-j)/2**(j+1)
              for j in range(11)),arb(0))
    complete_bound=8*pi**(-arb(9)/2)*H**2*(-2*q0).exp()*tail
    assert complete_bound<arb(1)/4
    perturbation=Q(1,10**10)
    assert factorial(6)*sum(abs(c) for c in k.values())==5760
    assert 5760*perturbation<=Q(7,8*2**16)
    for R in range(1,33):
        assert 5760*perturbation*R**6<=Q(7,8)*Q(R**8,2**16)
    epsilon=Q(1,4)*perturbation
    assert epsilon<perturbation-epsilon
    result={'passed':True,'actual_forgotten_product_terms':len(k),
        'vacuum_probe_value':image[key],'finite_right_contexts_audited':contexts,
        'contexts_with_sufficient_total_feature_degree':degree_sufficient,
        'complete_H4_squared_bound':str(complete_bound),
        'source_perturbation_coefficient_per_w_seam':str(perturbation),
        'sufficient_scalar_noise_per_w_seam':str(epsilon),
        'claims':['same_specified_residual_tower_observations',
                  'both_sources_fit_the_original_all_radius_budgets',
                  'existing_vacuum_coordinate_separates_them'],
        'scope':'All-depth invisibility uses the proved first-retained-seam support obstruction. The probe requires additional labelled vacuum-record acquisition; it is not recovered from the old measurements.'}
    out=HERE.parent/'results/invisible-source-probe.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
