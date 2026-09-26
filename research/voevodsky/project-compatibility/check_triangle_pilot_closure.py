"""Fresh headless closure of exact pilot dependencies; not an analytic proof checker."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
checks=[
 ('check_period_residue_boundary.py','period-residue-boundary.json'),
 ('check_triangle_normalization.py','triangle-normalization.json'),
 ('check_triangle_collinear.py','triangle-collinear.json'),
 ('check_triangle_joint_profile.py','triangle-joint-profile.json'),
 ('check_triangle_moving_collision.py','triangle-moving-collision.json'),
 ('check_triangle_regulator_coefficient.py','triangle-regulator-coefficient.json'),
 ('check_triangle_limit_order.py','triangle-limit-order.json'),
 ('check_triangle_measure_audit.py','triangle-measure-audit.json'),
 ('check_triangle_primary_versions.py','triangle-primary-versions.json'),
 ('check_triangle_volume_dictionary.py','triangle-volume-dictionary.json'),
 ('check_triangle_measure_transport.py','triangle-measure-transport.json'),
 ('check_triangle_cartesian_pole.py','triangle-cartesian-pole.json'),
 ('check_triangle_readout_jet.py','triangle-readout-jet.json'),
 ('check_filtered_comparison_readout.py','filtered-comparison-readout.json')]
paths=sorted(set(HERE.glob('*.md'))|set(HERE.glob('check_*.py'))|{
 ROOT/'temp/arxiv-2408.16386-source/sections'/name
 for name in ('applications.tex','method.tex','cosmologicalintegrals.tex')}|{
 ROOT/f'temp/triangle-measure-primary-2402.06558v{version}{suffix}'
 for version in (1,3) for suffix in ('.tar','-source/IR_Divs.tex')}|{
 ROOT/'temp/triangle-measure-primary-2402.06558v3.html'})
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory();results=[];measure_match=None
for checker,receipt in checks:
    run=subprocess.run([sys.executable,str(HERE/checker)],cwd=ROOT,capture_output=True,text=True,check=True)
    payload=json.loads(run.stdout)
    if 'printed_measure_matches_euclidean' in payload:
        measure_match=payload['printed_measure_matches_euclidean']
    assert payload['passed'] is True and payload['source_unchanged'] is True
    stored=json.loads((HERE/receipt).read_text(encoding='utf-8'))
    assert stored['passed'] is True and stored['source_unchanged'] is True
    results.append({'checker':checker,'receipt':receipt,'passed':True,
        'receipt_sha256':hashlib.sha256((HERE/receipt).read_bytes()).hexdigest()})
assert before==inventory()
assert measure_match is False # successful hostile test, not physical identification
report={'passed':True,'checker_count':len(results),'source_unchanged':True,
 'printed_measure_matches_euclidean':measure_match,
 'input_sha256':before,'results':results,
 'analytic_boundary':'Exact identities/fixtures only. The local uniform Mellin estimates and joint corner law are written conditional proofs in triangle-joint-corner.md, not machine-formalized analytic results.',
 'physical_boundary':'Candidate real reduced family, literal printed normalization, compact0<x<a and small-w cutoff. No physical continuation, owner adoption or global completion certified.'}
(HERE/'triangle-pilot-closure.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='input_sha256'},indent=2))
