"""Exact source-cycle contrast; controlled-cycle readout is declared, not installed."""
import json
from pathlib import Path
from hashlib import sha256
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/nima'
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
import check_native_spinor_pair_adapter as n
from check_pentachoron_spin_interfaces import A,S5,mm,adj,scale,add
from fractions import Fraction as Q


def require(ok,message):
    if not ok: raise ValueError(message)


def sha(p):return sha256(p.read_bytes()).hexdigest()


def main():
    contract=HOME/'contracts/native-cycle-discriminator.v1.json'
    c=json.loads(contract.read_text())
    paths={contract,Path(__file__)}
    def load(name):
        p=ROOT/name;paths.add(p);r=json.loads(p.read_text())
        require(r['verification_passed'],'native source failed')
        for name,digest in r['source_hashes'].items():
            dep=(ROOT/'research/voevodsky'/name).resolve()
            require(dep.is_relative_to(ROOT) and sha(dep)==digest,'native source drift')
            paths.add(dep)
        return r
    adapter=load(c['adapter_result'])
    identity=n.eye(4);single_identity=n.eye(2)
    rho=scale(A(Q(1,4)),identity)
    effects={};reports=[]
    for row in adapter['adapter_reports']:
        key=(row['chirality'],row['doublet_option'])
        d=n.matrix(row['effective_cycle_D']);w=n.matrix(row['cell_encoding'])
        require(mm(adj(w),w)==single_identity,'single native encoding')
        for cell in range(5):
            block=w[2*cell:2*cell+2]
            require(mm(adj(block),block)==scale(A(Q(1,5)),single_identity),'local cell population distinguishes source')
        u=n.kron(d,n.conjugate_matrix(d))
        require(mm(adj(u),u)==identity,'native pair cycle not unitary')
        require(mm(mm(u,rho),adj(u))==rho,'unpolarized state changes under bare cycle')
        f=scale(A(Q(1,4)),add(scale(A(2),identity),scale(A(-1),add(u,adj(u)))))
        defect=add(identity,scale(A(-1),u))
        require(f==scale(A(Q(1,4)),mm(adj(defect),defect)),'interference effect identity')
        eigen=(A(5)+(-S5 if key[1]==0 else S5))/8
        projector=scale(A(1)/eigen,f)
        require(mm(projector,projector)==projector and adj(projector)==projector and n.trace(projector)==2,'contrast projector')
        require(mm(f,f)==scale(eigen,f),'contrast spectrum')
        probability=n.trace(mm(rho,f))
        require(probability==eigen/2,'unpolarized probability')
        effects[key]=(f,projector,eigen)
        reports.append({'chirality':key[0],'option':key[1],'effect':n.encoded(f),
                        'contrast_projector':n.encoded(projector),'nonzero_effect_eigenvalue':eigen.record(),
                        'unpolarized_minus_probability':probability.record(),
                        'local_single_cell_probability':'1/5','local_pair_cell_probability':'1/25',
                        'bare_cycle_leaves_unpolarized_density_unchanged':True})
    rivals=[]
    for chirality in (-1,1):
        f0,p0,c0=effects[(chirality,0)]
        f1,p1,c1=effects[(chirality,1)]
        weight=c0/(2*c1)
        # From 2<sqrt5<3: 0<c0<c1<1, hence0<weight<1/2.
        require(c0==(A(5)-S5)/8 and c1==(A(5)+S5)/8,'positivity bounds changed')
        alternative=add(scale(weight/2,p1),scale((1-weight)/2,add(identity,scale(A(-1),p1))))
        require(n.trace(alternative)==1 and alternative==adj(alternative),'rival density')
        require(n.trace(mm(f1,alternative))==n.trace(mm(f0,rho)),'preparation rival contrast mismatch')
        rivals.append({'chirality':chirality,'option1_density':n.encoded(alternative),
                       'projector_weight':weight.record(),'eigenvalues_each_multiplicity2':[ (weight/2).record(),((1-weight)/2).record()],
                       'positive_by':'0<c0<c1<1 implies0<weight=c0/(2c1)<1/2',
                       'same_contrast_as_option0_unpolarized':True})
    for visibility in (A(Q(4,5)),A(0)):
        for f,_,_ in effects.values():
            visible=add(scale(A(Q(1,2)),identity),scale(visibility,add(f,scale(A(Q(-1,2)),identity))))
            require(n.trace(mm(rho,visible))==(1-visibility)/2+visibility*n.trace(mm(rho,f)),'visibility/null law')
            if visibility==0:
                require(visible==scale(A(Q(1,2)),identity),'dephasing null')
    notes=c['source_notes']
    paths.update(ROOT/p for p in notes)
    result={'schema':'marici.scattering.native-cycle-discriminator-result.v1','status':'pass',
            'disposition':'scale_independent_cycle_contrast_conditional_on_preparation_and_instrument',
            'reports':reports,'strictly_positive_preparation_rivals':rivals,
            'unit_visibility_probability_formulas':['(5-sqrt5)/16','(5+sqrt5)/16'],
            'unit_visibility_probabilities':[0.17274575140626314,0.45225424859373686],
            'effect_spectra':'0 multiplicity2; (5 minus/plus sqrt5)/8 multiplicity2',
            'unknown_preparation_ranges_overlap':True,
            'known_visibility_control':'p_v=(1-v)/2+v*p checked atv=4/5;v=0 gives1/2 for both',
            'relative_energy_scale_enters':False,
            'bare_cycle_is_sufficient_measurement':False,
            'controlled_cycle_or_equivalent_instrument_supplied':False,
            'full_native_complement_discarded':False,'physical_scattering_explained':False,'root_outcome':None,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)}}
    (HOME/'results/native-cycle-discriminator.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','disposition','unit_visibility_probability_formulas','unknown_preparation_ranges_overlap','controlled_cycle_or_equivalent_instrument_supplied')},indent=2))


if __name__=='__main__':main()
