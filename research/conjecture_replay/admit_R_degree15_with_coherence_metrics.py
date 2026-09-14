#!/usr/bin/env python3
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'));from event_log import *
from coherence_pyramid import *
from composite_arrow_tests import ArrowPath
prior=json.loads((R/'research/conjecture_replay/results/X_exchange_admitted_percent_metrics.json').read_text());p=prior['projection'];src=R/'research/benincasa/results/G12_exact_degree15_reconstruction.json';x=json.loads(src.read_text())
arrows=(TypedArrow('R_exact_degree15','problem','exact_packet',8),TypedArrow('D_direct_physical_pairing','exact_packet','physical_class',3),TypedArrow('X_exchange_transport','exact_packet','exchange_packet',.2),TypedArrow('B_signed_minor_restriction','exchange_packet','boundary_packet',2),TypedArrow('G_relative_gluing','boundary_packet','physical_class',5))
paths=(ArrowPath('direct',('R_exact_degree15','D_direct_physical_pairing')),ArrowPath('factored',('R_exact_degree15','X_exchange_transport','B_signed_minor_restriction','G_relative_gluing')))
layers=(
 CoherenceLayer('solution',(('direct','factored'),),(PathPattern('direct','*+'),PathPattern('factored','*+'))),
 CoherenceLayer('X',arrow_domains=(('X_exchange_transport',frozenset({'+-'})),)),
 CoherenceLayer('R',arrow_domains=(('R_exact_degree15',frozenset({'++'})),)),
)
cp=CoherencePyramid(arrows,paths,layers).run();assert cp['survivor_count']==2
s1=digest({'parent':p['state_id'],'R_exact_degree15':'++'});ev=ResolutionEvent('R_exact_degree15',digest({'degree':15,'exact_field':'Q','verification_rows':1330}),p['graph_digest'],p['state_id'],'++',('+-','-+','--'),(f'{src.relative_to(R).as_posix()}#{digest(x)}',),8.,(('runtime_seconds',str(x['elapsed_seconds'])),('solver','FLINT fmpq')),StateDelta(add_interfaces=('exact_degree15_coefficient_packet',),add_facts=('R_exact_degree15=++',)),(('R_exact_degree15=++','entails','exact degree-15 weighted-overlap identity over Q'),),(),s1,'2026-09-11T00:01:23Z');log=EventLog(p['graph_digest'],p['state_id']).append(ev);pct={'survivor_count':-50.,'remaining_formal_entropy_bits':-50.,'execution_cost_vs_previous_arrow':3900.};out={'schema':'marici.conjecture-replay.R-degree15-admitted-coherence-metrics.v1','event':{'event_id':ev.event_id,**asdict(ev)},'projection':asdict(log.project()),'coherence_projection':cp,'forced_by_two_survivors':{'D_direct_physical_pairing':'++'},'remaining_alternatives':[{'B_signed_minor_restriction':'-+','G_relative_gluing':'++'},{'B_signed_minor_restriction':'--','G_relative_gluing':'-+'}],'metric_projection':{'base':'immediately previous X-conditioned projection','percent_change_from_previous_base':pct,'absolute_values_omitted_by_policy':True},'next_recommendation':'B_signed_minor_restriction','passed':True};(R/'research/conjecture_replay/results/R_degree15_admitted_coherence_metrics.json').write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'outcome':'++','survivors':2,'forced':out['forced_by_two_survivors'],'percent_delta':pct,'next':out['next_recommendation']}))
