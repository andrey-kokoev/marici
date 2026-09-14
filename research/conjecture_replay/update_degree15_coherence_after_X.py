#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from coherence_pyramid import *
from composite_arrow_tests import ArrowPath
obs=json.loads((R/'research/benincasa/results/X_exchange_transport.json').read_text());assert obs['observed_outcome']=='+-'
arrows=(TypedArrow('R_exact_degree15','problem','exact_packet',8),TypedArrow('D_direct_physical_pairing','exact_packet','physical_class',3),TypedArrow('X_exchange_transport','exact_packet','exchange_packet',.2),TypedArrow('B_signed_minor_restriction','exchange_packet','boundary_packet',2),TypedArrow('G_relative_gluing','boundary_packet','physical_class',5))
paths=(ArrowPath('direct',('R_exact_degree15','D_direct_physical_pairing')),ArrowPath('factored',('R_exact_degree15','X_exchange_transport','B_signed_minor_restriction','G_relative_gluing')))
layers=(
 CoherenceLayer('terminal_solution',(('direct','factored'),),(PathPattern('direct','*+'),PathPattern('factored','*+'))),
 CoherenceLayer('observed_X',arrow_domains=(('X_exchange_transport',frozenset({'+-'})),)),
)
r=CoherencePyramid(arrows,paths,layers).run();assert r['survivor_count']==4 and r['best_query']['arrow']=='B_signed_minor_restriction'
out={'schema':'marici.conjecture-replay.degree15-coherence-after-X.v1','observed_arrow':{'X_exchange_transport':'+-'},'projection':r,'metric_projection':{'base':'previous 16-survivor coherence projection','percent_change_from_previous_base':{'survivor_count':-75.0,'remaining_formal_entropy_bits':-50.0,'observed_arrow_cost_vs_previous_reconstruction':-97.5},'absolute_values_omitted_by_policy':True},'interpretation':'X supplied the predicted two combinatorial bits: four assignments remain (two formal bits).','best_formal_separator':'B_signed_minor_restriction','availability_note':'B requires the exact degree-15 packet and is not executable yet.','next_recommendation':'R_exact_degree15','passed':True};p=R/'research/conjecture_replay/results/degree15_coherence_after_X.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'survivors':4,'best_query':r['best_query'],'percent_delta':out['metric_projection']['percent_change_from_previous_base']}))
