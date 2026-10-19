#!/usr/bin/env python3
"""Fresh subprocess closure of local current suite, with physical source gate audit."""
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/benincasa/contracts/history6-current-contour-admission.v1.json'
SOURCE='research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'
SUITE=['boundary_berezin_current','current_covariance','current_contour_lattice','current_normal_link',
       'current_split_divisors','current_ordered_lifts','current_projective_lattice',
       'current_gl3_transport','current_contour_admission','current_external_boundary']


def main():
    runs=[];paths=[CONTRACT,SOURCE]
    for name in SUITE:
        checker=f'research/benincasa/checkers/check_history6_{name}.py'
        receipt=f'research/benincasa/results/history6_{name}.json'
        result=subprocess.run([sys.executable,str(ROOT/checker)],cwd=ROOT,capture_output=True,text=True,timeout=300)
        if result.returncode!=0:
            raise RuntimeError(f'{checker}: {result.returncode}\n{result.stdout[-4000:]}\n{result.stderr[-4000:]}')
        evidence=json.loads((ROOT/receipt).read_text());assert evidence['passed']
        assert evidence['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
        for p,h in evidence['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        runs.append({'checker':checker,'receipt':receipt,'fresh_subprocess_returncode':0,
            'passed':True,'receipt_sha256':sha256((ROOT/receipt).read_bytes()).hexdigest(),
            'stderr':result.stderr[-1000:]})
        paths.extend([checker,receipt])
    contract=json.loads((ROOT/CONTRACT).read_text());selection=contract['physical_selection']
    assert selection['status']=='not_admitted'
    missing=[key for key,value in selection.items() if value is None]
    assert len(missing)==7
    # Audit exact scoped source claims; do not misread Gamma as a chosen
    # exceptional cycle or generic Cauchy/real-loop rules as its selection.
    lines=(ROOT/SOURCE).read_text(encoding='utf-8').splitlines()
    anchors=[]
    for role,needle in [('canonical_form',r'\label{cyclic_minor_top_form}'),
                        ('Gamma_is_cell',r'cell $\Gamma_\sigma\!\in\!G(k,n)$'),
                        ('kernel',r'\label{general_on_shell_function_momentum_twistors}'),
                        ('extra_nonconsecutive_poles','new, unwanted singularities for the top-cell'),
                        ('generic_residue_dimension',r'any $(4k\pl1)$-dimensional cell'),
                        ('physical_loop_contour',r'restricts each loop-momentum to be {\it real}')]:
        hits=[(i+1,line) for i,line in enumerate(lines) if needle in line];assert len(hits)==1,(role,hits)
        number,line=hits[0];anchors.append({'role':role,'line':number,'text':line})
    admission=json.loads((ROOT/'research/benincasa/results/history6_current_contour_admission.json').read_text())
    external=json.loads((ROOT/'research/benincasa/results/history6_current_external_boundary.json').read_text())
    assert not admission['physical_admitted'] and not external['physical_admitted']
    out={'schema':'marici.benincasa.history6-current-closure.v1','history_index':6,
        'fresh_local_suite':runs,'fresh_suite_count':len(runs),'passed':True,
        'constructed_scope':['Localized degree7 direction-retaining holomorphic incidence-current extension with actual Jacobian and full fermionic normalization2880.',
            'Kernel/pivot, scalar/GL2 and triple GL3 normal covariance with determinant/orientation hostiles.',
            'Canonical-versus-split Plucker divisor classification and oriented source normal-link wall crossing.',
            'Integral P1 and P2 period/cycle lattices, full class transport and both integral P1 tube maps.',
            'Conditional source-word/full-cycle contour preflight and correctly graded singular-support period currents.',
            'Typed conditional external-normal boundary anticommutation, two actual incidence fixtures and68 component route cases.'],
        'owning_source_audit':anchors,
        'physical_admitted':False,'physical_selection_status':'not_admitted',
        'missing_physical_selection_inputs':missing,
        'physical_gate_analysis':'Canonical source class1 has a Z3 family of decorated lifts; successful covariance and even the observed split period pair cannot choose its full integral class. Source Gamma is the cell; canonical/Cauchy/real-loop passages do not supply this exceptional weighted lift or external constraint prescription. Conditional algebraic external compatibility is not a reviewed physical prescription.',
        'conditional_example':contract['conditional_append_b3'],
        'ordinary_blowdown_status':'unavailable_not_zero',
        'scientific_promotion':False,
        'claim_boundary':'Fresh headless local closure and scoped source/admission audit, not physical contour completion or global weighted theorem.',
        'next_action':'Supply or derive and review an explicit owning physical cycle rule/full integral lift, external constraint/normal contour prescription and boundary-program attachment. Then materialize a versioned successor admission contract and replay its actual contour/current square. Further identical local replays cannot select those missing data.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_closure.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'fresh_subprocess_checks':len(runs),'physical_admitted':False,
        'missing_physical_selection_inputs':missing,'scientific_promotion':False},indent=2))

if __name__=='__main__':main()
