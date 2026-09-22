"""Exact audit of the actual chosen source lift for O2 plus 270 private rows.

The normalized old functional is -A*early+B*late. A,B are fixed ideal
coefficients, not rational midpoint replacements. No new detector is installed.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
import importlib.util
import json
import hashlib

ROOT=Path(__file__).resolve().parents[1];OTHER=ROOT.parent/'voevodsky'
spec=importlib.util.spec_from_file_location('source',OTHER/'certificates/verify_filtered_obstruction.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)


def encode(col):
    return [{'word':list(word),'marks':list(marks),'coefficient':str(value)}
            for (word,marks),value in sorted(col.items())]


def main():
    problem_path=OTHER/'results/filtered-obstruction-problem.json'
    cert_path=OTHER/'results/filtered-obstruction-certificate.json'
    p,cert=s.load(problem_path),s.load(cert_path)
    structural=s.verify(p,cert)
    b0=s.relation((2,3),0)
    x=s.multiply({((0,1),(0,1)):F(1)},b0)
    v2=s.multiply(s.relation((0,1),1),b0)
    c1=s.relation((4,5),1)
    vy=s.multiply(v2,c1)
    oldrows=[tuple(tuple(edge) for edge in row) for row in p['old_seams']]
    def old_coefficients(source):
        values=s.vacuum_rows(0,15,source,2)
        return [values.get(row,F(0)) for row in oldrows]
    assert old_coefficients(x)==[0,1] and old_coefficients(v2)==[1,1]
    assert not s.rho_column(0,x)
    # D1 retains the potential-word buffers: its vacuum projection can vanish.
    def first_jet(source):
        out={}
        for (word,marks),coefficient in source.items():
            states=[0]
            for event in word:states.append(states[-1]|(1<<event))
            for cut in range(len(word)):
                left=s.record(0,word[:cut],marks[:cut])
                right=s.record(states[cut+1],word[cut+1:],marks[cut+1:])
                for lw,a in left.items():
                    for rw,b in right.items():
                        key=(lw,('e',states[cut],states[cut+1],marks[cut]),rw)
                        out[key]=out.get(key,F(0))+coefficient*a*b
        return {key:value for key,value in out.items() if value}
    first=first_jet(x);assert first and not first_jet(v2)
    private=[]
    for entry in cert['prefixes']:
        rest=tuple(i for i in range(6) if not entry['end']&(1<<i))
        for suffix in (0,1):
            kinds=tuple(entry['kinds'])+(suffix,)
            if sum(kinds)!=2:continue
            state=0;pivot=[]
            for pair,keep in zip(tuple(map(tuple,entry['pairs']))+(rest,),kinds):
                pivot.append(('e',state,state|(1<<min(pair)),keep))
                state|=sum(1<<i for i in pair)
            private.append(tuple(pivot))
    assert len(private)==len(set(private))==270
    contexts=[]
    for word in permutations((4,5)):
        for marks in product((0,1),repeat=2):
            extended=s.multiply(x,{(word,marks):F(1)})
            image=s.vacuum_rows(0,63,extended,3)
            values=[image.get(row,F(0)) for row in private]
            assert all(value==0 for value in values)
            contexts.append({'word':list(word),'marks':list(marks),'private_nonzero_count':0})
    target=tuple(tuple(edge) for edge in p['private_seams'])
    assert s.vacuum_rows(0,63,s.multiply(x,c1),3).get(target,F(0))==0
    assert s.vacuum_rows(0,63,vy,3).get(target,F(0))==1
    # Exact Laurent-polynomial arithmetic in formal fixed coefficients A,B.
    def multiply(a,b):
        out={}
        for (i,j),x0 in a.items():
            for (k,l),y0 in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),F(0))+x0*y0
        return {power:coef for power,coef in out.items() if coef}
    C={(0,0):F(1),(1,-1):F(-1)};B={(0,1):F(1)}
    assert multiply(C,B)=={(0,1):F(1),(1,0):F(-1)}
    assert sum(abs(a) for a in x.values())==2
    report={'verified':True,'protocol':'original lower observer plus the 270 first-seam private rows',
        'structural_reverification':structural,
        'source_x':{'definition':'path(2_forgotten,3_retained) forgotten(5,7)',
            'event_indices':p['event_primes'],'expanded_terms':encode(x),'path_l1_cost':'2',
            'recorder_zero':True,'first_jet_nonzero':True,
            'first_jet_nonzero_entry':{'left_buffer':list(next(iter(first))[0]),
                'seam':list(next(iter(first))[1]),'right_buffer':list(next(iter(first))[2]),
                'coefficient':str(next(iter(first.values())))},
            'first_jet_of_v2_zero':True,'old_sector_coefficients':['0','1']},
        'source_v2':{'old_sector_coefficients':['1','1']},
        'normalization':{'old_functional_after_common_prefactor':'-A*early+B*late',
            'fixed_ideal_coefficients':'A=mu_A1-L, B=mu_A2-L',
            'c':'1-A/B','verified_identity':'c*B=B-A',
            'hypotheses':['B is nonzero','the fixed ideal coefficients and old detector are those of the owning calibration'],
            'no_midpoint_substitution':True},
        'right_contexts':contexts,'private_rows_per_context':270,'coefficient_checks':2160,
        'scope_of_support_argument':'No nonidentity left context starts before the initial vertex. All contributing right contexts fill precisely the remaining two events. Old rows vanish on positive-length contexts by endpoints.',
        'chosen_lift':{'u':'Obs_2(v2)','z':'c*Obs_3(x)','j':'j(u)=z',
            'H':'B_ev-j*w*q','pi_j':'identity on Q=span(u)',
            'H_i':'f','pi_H':'0',
            'status':'source-equivariant unfiltered lift, conditional on the owning compatible evaluation and source-extension hypotheses'},
        'filtration_boundary':{'P_y_of_x_times_c1':'0','P_y_of_v2_times_c1':'1',
            'owning_prefix_identity':'P_y(m*c1)=1 for every m in I E over u',
            'consequence':'z is outside I E; H is not a lift into N=K intersect I E',
            'not_admitted_as':'a filtration-preserving face witness in the previous tetrahedral fixture'},
        'gain_transport':{'operation':'scale the entire private raw family by two; freeze the old observer',
            'c':'unchanged','source_x':'unchanged','identity':'U*j_old=j_new and U*H_old=H_new by source-compatible evaluation',
            'status':'symbolic naturality under the declared whole-source gain theorem; not a full actual-observer matrix export'},
        'not_covered':['additional detector families beyond the declared old-plus-270 protocol',
            'new physical measurements','all-depth completion','identification of all four productization towers'],
        'evidence_sha256':{'structural_problem':hashlib.sha256(problem_path.read_bytes()).hexdigest(),
                           'structural_certificate':hashlib.sha256(cert_path.read_bytes()).hexdigest()}}
    (ROOT/'results/actual-private-source-lift.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:report[key] for key in ('verified','coefficient_checks','normalization','filtration_boundary')},indent=2))


if __name__=='__main__':main()
