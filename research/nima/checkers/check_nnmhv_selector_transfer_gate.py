"""Fail-closed typing audit of polyhedral selector certificates against NNMHV artifacts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
N=ROOT/'research/nima'
def load(name):return json.loads((N/'results'/name).read_text())
def main():
 seed=load('nnmhv-positroid-seed.json');match=load('seven-point-history-parity-cell-matching.json');tail=load('nnmhv-long-exponent-two-limit.json');approx=load('selector-approximation-contract.json');compiled=load('seven-point-positroid-compiler.json');chart=load('seven-point-positive-chart.json');overlap=load('seven-point-chart-overlap.json')
 assert seed['six_point_seed']['dimension']==8
 requests=seed['seven_point_cell_requests'];matches=match['matches'];assert len(requests)==len(matches)==6
 assert {x['history_index'] for x in requests}=={x['history_index'] for x in matches}==set(range(6))
 assert all(x['full_canonical_form_ratio']=='1' for x in matches)
 assert compiled['passed'] and len(compiled['cells'])==6 and chart['history_index']==0
 assert len(overlap['samples'])==2 and all(all(x['status']=='OUTSIDE_POSITIVE_CELL' for x in sample['candidate_fibres'][1:]) for sample in overlap['samples'])
 assert tail['model']=='S_n=L+c2/n^2+c3/n^3' and len(tail['families'])>=2
 ref=approx['reference'];assert len(approx['scope'])==6 and len(ref['source_lifts'][0])==3
 gates={
  'common_fixed_projection':{'status':'MISSING','reason':'Six-point top G_+(2,6) and seven-point history/canonical-form matches do not provide a single affine source-to-public projection shared across n.'},
  'positive_cell_compiler':{'status':'PRESENT_N7_ONLY','reason':'A later n=7 positroid compiler supplies six rank tables; an explicit positive chart now gives a locally full-dimensional CZ image for history 0. Neither establishes arbitrary-n compilation or canonical-form equality of this chart.'},
  'common_refinement_overlap':{'status':'LOCAL_FIBRE_SEPARATION_ONLY','reason':'For one positive moment-curve Z, two exact points in the history-zero chart have no positive lift in the other five compiled charts. This is local separation, not global coverage or n-to-n+1 refinement.'},
  'uniform_norm_and_rate':{'status':'MISSING','reason':'The n^-2 record is a fitted scalar full-history component on selected kinematic families, not a uniform-in-n bound in a norm of canonical forms on a fixed domain.'},
  'existing_selector_certificate':{'status':'PRESENT_BUT_DIFFERENT_TYPE','reason':'A rational three-atom polygon section has whole-domain infinity error, but is not a map into G(2,6) and is not a rational differential canonical form.'}}
 assert all(x['status']=='MISSING' for k,x in gates.items() if k not in ('existing_selector_certificate','positive_cell_compiler','common_refinement_overlap'))
 report={'schema':'marici.nima.nnmhv-selector-transfer-gate.v1','passed':True,'n6_dimension':8,'n7_matched_histories':len(matches),'n7_ratios_one':True,'selector_scope_vertices':len(approx['scope']),'selector_source_atoms':3,'fitted_tail_families':sorted(tail['families']),'gates':gates,'conclusion':'Seven-point rank-table compiler, one explicit positive CZ chart, and local fibre separation now exist. Canonical-form comparison, global overlaps/coverage, arbitrary-n extension and uniform tail bounds remain open.'}
 p=N/'results/nnmhv-selector-transfer-gate.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
