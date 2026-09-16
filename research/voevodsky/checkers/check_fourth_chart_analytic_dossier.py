"""Conformance audit separating response, retained-graph, Hilbert, and radial fourth charts."""
import json
from pathlib import Path
ROOT=Path(__file__).parents[1];P=ROOT/'fourth-chart-analytic-dossier.json';OUT=ROOT/'results'/'fourth-chart-analytic-dossier.json'
def main():
 d=json.loads(P.read_text());c=d['charts'];checks={'response_retains_source_coordinate':c['complete_response']['components']['B_g(a)']=='g(a)','response_inverse_is_projection':c['complete_response']['inverse']=='R4(B,Q,A,C)=B','response_chart_valid':c['complete_response']['classification']=='valid_analytic_chart','retained_graph_valid':c['retained_graph']['classification']=='valid_graph_chart','source_forgetting_hilbert_chart_refused':c['source_forgetting_hilbert_record']['classification']=='not_a_valid_bounded_hilbert_chart','radial_bound_not_promoted':c['radial_augmented_record']['classification']=='valid_radial_observer_not_labelled_chart_inverse','physical_positive_completion_separate':d['selection_rule']['physical_positive_completion']=='requires separate Mosco/Douglas/Schur analysis','sources_exist':all((Path(s)).exists() for s in d['authoritative_sources'])}
 out={'schema':'marici.voevodsky.fourth-chart-analytic-dossier-check.v1','checks':checks,'passed':all(checks.values()),'disposition':{'presentation_chart':'complete_response','graph_chart':'retained_graph','rejected_promotion':'source_forgetting_hilbert_record','separate_frontier':'physical_positive_completion'}};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
