"""Symmetrize a fixed six-formula selector; certify the exact three-formula threshold."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from verify_selector_approximation import check,distance,boundary_bound,digest
from checked_retirement_interface import migrate,freeze
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
def compile_program(packet):
    table=[];indices=[]
    for ids in packet['triangles']:
        matrix=[[Q(x) for x in packet['vertices'][i]]+[Q(1)]+list(map(Q,packet['source_lifts'][i])) for i in ids]
        for col in range(3):
            pivot=next(i for i in range(col,3) if matrix[i][col]);matrix[col],matrix[pivot]=matrix[pivot],matrix[col]
            v=matrix[col][col];matrix[col]=[x/v for x in matrix[col]]
            for i in range(3):
                if i!=col:
                    factor=matrix[i][col];matrix[i]=[x-factor*y for x,y in zip(matrix[i],matrix[col])]
        f=[[str(matrix[j][3+i]) for j in range(3)] for i in range(3)]
        if f not in table:table.append(f)
        indices.append(table.index(f))
    return {'migration_binding':packet['migration_binding'],'vertices':copy.deepcopy(packet['vertices']),
      'triangles':copy.deepcopy(packet['triangles']),'formulas':table,'cell_formula_ids':indices}
def main():
    proposal_path=OUT/'rank-two-provider-substitution.json';prior=json.loads(proposal_path.read_text())
    # The previously specified alternative is fixed BEFORE construction.
    # Its old report is not treated as authority: fresh owning checks follow.
    reference=copy.deepcopy(prior['alternative_section']);scope=prior['polygon'];center=prior['center']
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');plan=plans[i]
    assert prior['plan']==plan;state=migrate(plan,cases[i],retain_lift=True)
    compressed=copy.deepcopy(reference)
    assert reference['vertices'][-1]==center and len(reference['vertices'])==7
    compressed['source_lifts'][-1]=[str((Q(x)+Q(y))/2) for x,y in zip(reference['source_lifts'][0],reference['source_lifts'][3])]
    programs=[compile_program(p) for p in (reference,compressed)]
    assert len(programs[0]['formulas'])==6 and len(programs[1]['formulas'])==3
    error=distance(reference,compressed);assert error['maximum_atom_error']=='129/1000'
    lower=boundary_bound(plan,scope,reference,center);assert lower['three_formula_error_lower_bound']==error['maximum_atom_error']
    epsilons=['0','1/1000','1/10','129/1000','1/5'];packets=[];reports=[]
    for epsilon in epsilons:
        selected=1 if Q(epsilon)>=Q(error['maximum_atom_error']) else 0
        packet={'reference_digest':digest(reference),'epsilon':epsilon,'section':copy.deepcopy((reference,compressed)[selected]),
                'program':copy.deepcopy(programs[selected]),'distance':distance(reference,(reference,compressed)[selected])}
        metrics=check(state,scope,reference,epsilon,packet['section'],packet['program'],packet['distance'])
        packets.append(packet);reports.append({'epsilon':epsilon,**metrics,**packet['distance']})
    rejected=[]
    for defect in ('insufficient-budget','raw-norm-understatement','corrupt-formula','false-formula-sharing','inadmissible-lift','wrong-reference'):
        bad=copy.deepcopy(packets[-1])
        if defect=='insufficient-budget':bad['epsilon']='1/10'
        if defect=='raw-norm-understatement':bad['distance']['maximum_atom_error']='1/1000'
        if defect=='corrupt-formula':bad['program']['formulas'][0][0][2]=str(Q(bad['program']['formulas'][0][0][2])+1)
        if defect=='false-formula-sharing':bad['program']['formulas']=bad['program']['formulas'][:1];bad['program']['cell_formula_ids']=[0]*6
        if defect=='inadmissible-lift':bad['section']['source_lifts'][-1][0]='-1'
        if defect=='wrong-reference':bad['reference_digest']=digest(compressed)
        try:
            assert bad['reference_digest']==digest(reference)
            check(state,scope,reference,bad['epsilon'],bad['section'],bad['program'],bad['distance'])
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('bad approximation certificate accepted')
    paths=[Path(__file__),Path(__file__).with_name('verify_selector_approximation.py'),Path(__file__).with_name('full_polygon_checkpoint.py'),
      Path(__file__).with_name('verify_scalar_envelope_band.py'),ROOT/'research/voevodsky/checkers/migration_section_checkpoint.py',
      ROOT/'research/voevodsky/checkers/checked_retirement_interface.py',proposal_path,G/'audit-elimination-contract.json',G/'audit-elimination.json.gz']
    contract={'expected_plan':plan,'scope':scope,'reference':reference,'reference_digest':digest(reference),'center':center,
      'epsilons':epsilons,'metric':'original three-atom infinity norm at the same public point',
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    cp=OUT/'selector-approximation-contract.json';pp=OUT/'selector-approximation-packets.json'
    cp.write_text(json.dumps(contract,indent=2)+'\n');pp.write_text(json.dumps(packets,indent=2)+'\n')
    result={'passed':True,'cases':reports,'lower_bound_certificate':lower,'rejections':rejected,
      'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'packets_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),
      'scope':'Optimal three-formula uniform error for this fixed reference; six-cell geometry retained; no four/five-formula optimality claim.'}
    (OUT/'selector-approximation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'budgets':len(packets),'reference_formulas':6,'compressed_formulas':3,
      'triangular_cells_each':6,'optimal_three_formula_error':error['maximum_atom_error'],'rejections':len(rejected),
      'program_bytes':[r['program_bytes'] for r in (reports[0],reports[-1])]},indent=2))
if __name__=='__main__':main()
