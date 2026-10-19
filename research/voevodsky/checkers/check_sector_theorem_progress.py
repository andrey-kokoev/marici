"""Conditional progress only: do not admit the umbrella or choose the frozen K."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from math import factorial
import json,subprocess,sys
from check_native_spinor_pair_adapter import matrix,transport_matrix
from check_typed_spin_channels import decode,eye,kron,conjugate_matrix
from check_pentachoron_spin_interfaces import A,mm,adj,scale,add
from check_rival_defect_record_rule import generator_blocks

ROOT=Path(__file__).resolve().parents[3]
BASE='research/voevodsky/'

def occupation_bounds():
    # At g=1/2,t=1: p=(1-cos(sqrt(2)))/4. Alternating terms decrease.
    def partial(n):return sum((Fraction((-1)**k*2**k,factorial(2*k)) for k in range(n+1)),Fraction(0))
    return (1-partial(10))/4,(1-partial(11))/4

def audit():
    subprocess.run([sys.executable,str(ROOT/(BASE+'checkers/check_native_spinor_pair_adapter.py'))],check=True,stdout=subprocess.DEVNULL,timeout=300)
    def load(name):return json.loads((ROOT/(BASE+name)).read_text())
    native=load('results/native_spinor_pair_adapter.json');source=load('results/pentachoron_cycle_transport.json');spin=load('results/pentachoron_spin_interfaces.json')
    typed=load('results/typed_spin_channels.json');Ps=matrix(typed['input_scalar_projector']);checks={};cases=[]
    def check(key,value):
        checks[key]=bool(value)
        if not value:raise AssertionError(key)
    check('fresh_native_adapter',native['verification_passed'] is True)
    for row in source['chirality_results']:
        chirality=row['chirality'];extension=row['conditional_cycle_defect_extension']
        encodings=[extension['attachment_encoding'],extension['opposite_lift_attachment_encoding']]
        Ws=[matrix(e['cell_isometry']) for e in encodings]
        low=add(*(mm(W,adj(W)) for W in Ws));low_energy=decode(row['low_energy'])
        high=decode(next(r for r in spin['chirality_results'] if r['chirality']==chirality)['higher_energy'])
        L=add(scale(low_energy,low),scale(high,add(eye(10),scale(A(-1),low))))
        T=transport_matrix(matrix(row['spin_lift']));X=add(scale(A(2),eye(10)),scale(A(-1),add(T,adj(T))))
        for choice,H in [('mismatch_only',L),('optional_cycle_defect',add(L,X))]:
            check(f'self_adjoint_{choice}_{chirality}',adj(H)==H)
            for option,W in enumerate(Ws):
                label=f'{choice}_{chirality}_{option}'
                report=next(r for r in native['adapter_reports'] if r['chirality']==chirality and r['doublet_option']==option)
                energy=low_energy if choice=='mismatch_only' else decode(report['single_conditional_energy'])
                HW=mm(H,W);J=kron(W,conjugate_matrix(W))
                KJ=add(kron(HW,conjugate_matrix(W)),kron(W,conjugate_matrix(HW)))
                check('source_pair_eigenblock_'+label,KJ==scale(2*energy,J))
                # Since K is self-adjoint, KPi=(KJ)Ps Jdagger and PiK=adj(KPi).
                KPi=mm(mm(KJ,Ps),adj(J));Pi=mm(mm(J,Ps),adj(J))
                check('scalar_commutator_zero_'+label,KPi==adj(KPi) and KPi==scale(2*energy,Pi))
                cases.append({'chirality':chirality,'doublet_option':option,'source_choice':choice,'scalar_pair_energy':(2*energy).record()})
    g=A(Fraction(1,2));zero=((A(0),),);one=eye(1)
    check('active_record_generator',generator_blocks(one,g)==(((g,),),((-g,),),((1+g,),)))
    check('dark_record_generator',generator_blocks(zero,g)==(((g,),),zero,((1+g,),)))
    lo,hi=occupation_bounds()
    check('conditional_readout_separated',Fraction(21,100)<lo<hi<Fraction(22,100))
    paths={BASE+'checkers/check_sector_theorem_progress.py',BASE+'checkers/check_rival_defect_record_rule.py',BASE+'contracts/retained-reaggregation-conjecture-net.v1.json',BASE+'contracts/retained-reaggregation-sector-theorem.v1.json',BASE+'native-spinor-pair-adapter.md',BASE+'results/native_spinor_pair_adapter.json',BASE+'results/pentachoron_spin_interfaces.json'}
    paths.update(BASE+p for p in native['source_hashes'])
    return {'schema':'marici.voevodsky.sector-theorem-progress.v1','status':'partial_conditional_progress','scientific_outcome':None,'physical_admission':False,'kernel_verified_analytic_theorem':False,
        'checks':checks,'cases':cases,'conditional_occupation':{'primary_exact':'(1-cos(sqrt(2)))/4','lower':str(lo),'upper':str(hi),'rival':'0','assumptions':'K is one of the two displayed retained pair operators, with zero vacuum extension, no additional sector-mixing terms, and the frozen scalar/ready preparation.'},
        'blockers':['Frozen comparison does not explicitly select mismatch-only K versus optional cycle-defect K or specify any additional orbital terms. The source adapter documents both; relative_native_orbital_unit=1 alone does not select an operator.','The K vacuum energy/reference must be explicitly fixed before full absolute joint energy accounting.','Variable-phase contract and retained post-readout accounting still need a complete scoped proof.'],
        'interpretation':'Eight source-choice/native-case checks support a conditional theorem; they do not establish which K is frozen, admit any consumer, or refute the umbrella.',
        'source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)}}

if __name__=='__main__':
    path=Path(sys.argv[1]);path.write_text(json.dumps(audit(),indent=2)+'\n')
