#!/usr/bin/env python3
"""Replace hand-authored PS1 metrics with graph-derived authoritative metrics."""
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from graph_metrics import *
latest=json.loads((R/'research/conjecture_replay/results/PS1C1a_corrected_replan.json').read_text());interfaces=frozenset(latest['projection']['interfaces'])
actions=(
 MetricAction('PS1A0_axis_incidence',requires=frozenset({'degree15_algebraic_relative_class'})),
 MetricAction('PS1A_alternate_signed_minor_specialization',frozenset({'PS1A0_axis_incidence'}),terminal=True),
 MetricAction('PS1B0_current_specialization',requires=frozenset({'degree15_algebraic_relative_class'})),
 MetricAction('PS1B_nearby_cycle_specialization',frozenset({'PS1B0_current_specialization'}),terminal=True),
 MetricAction('PS1C0_source_admissibility',status='resolved'),
 MetricAction('PS1C1a_central_residue_totalization',frozenset({'PS1C0_source_admissibility'}),status='resolved'),
 MetricAction('PS1C1a1_higher_normal_relative_coefficient_lift',frozenset({'PS1C1a_central_residue_totalization'}),frozenset({'central_wall_residue_totalization'})),
 MetricAction('PS1C1b_orientation_twisted_GM_connection',frozenset({'PS1C1a1_higher_normal_relative_coefficient_lift'}),frozenset({'moving_wall_residue_totalization'})),
 MetricAction('PS1C1c_source_Leray_tube_pairing',frozenset({'PS1C1b_orientation_twisted_GM_connection'}),frozenset({'orientation_twisted_GM_connection'})),
 MetricAction('PS1C_modified_operation_specialization',frozenset({'PS1C1c_source_Leray_tube_pairing'}),terminal=True),
)
graph=MetricGraph(actions,interfaces,(frozenset({'PS1A_alternate_signed_minor_specialization','PS1B_nearby_cycle_specialization','PS1C_modified_operation_specialization'}),));metrics=graph.metrics()
legacy=[]
for p in (R/'research/conjecture_replay/results').glob('*.json'):
 try:x=json.loads(p.read_text())
 except:continue
 mp=x.get('metric_projection',{})
 if mp.get('percent_change_from_previous_base') and 'derived_metric_schema' not in mp:legacy.append(p.relative_to(R).as_posix())
out={'schema':'marici.conjecture-replay.authoritative-graph-derived-metrics.v1','metric_definition':'research/conjecture_net/graph_metrics.py','graph_snapshot':{'actions':[asdict(a) for a in actions],'interfaces':sorted(interfaces),'coherence_constraints':[sorted(x) for x in graph.coherence_constraints]},'metrics':metrics,'authority':{'this_snapshot':'authoritative for the explicitly materialized PS1 subgraph','legacy_hand_authored_percent_artifacts':'non-authoritative engineering annotations','legacy_artifact_count':len(legacy),'legacy_artifacts':legacy,'global_history':'not claimed until pre-VC2 segment-local ledgers are reconstructed'},'reporting_rule':'Future percentage changes must call graph_metrics.percent_change on two materialized MetricGraph.metrics() snapshots; scripts may not embed before/after metric numbers manually.','passed':True};p=R/'research/conjecture_replay/results/authoritative_PS1_graph_metrics.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'metrics':metrics,'legacy_percent_artifacts_demoted':len(legacy)}))
