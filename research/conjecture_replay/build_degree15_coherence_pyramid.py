#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from coherence_pyramid import *
from composite_arrow_tests import ArrowPath
arrows=(TypedArrow('R_exact_degree15','problem','exact_packet',8),TypedArrow('D_direct_physical_pairing','exact_packet','physical_class',3),TypedArrow('X_exchange_transport','exact_packet','exchange_packet',.2),TypedArrow('B_signed_minor_restriction','exchange_packet','boundary_packet',2),TypedArrow('G_relative_gluing','boundary_packet','physical_class',5))
paths=(ArrowPath('direct',('R_exact_degree15','D_direct_physical_pairing')),ArrowPath('factored',('R_exact_degree15','X_exchange_transport','B_signed_minor_restriction','G_relative_gluing')))
layers=(
 CoherenceLayer('rung1_object_typing'),
 CoherenceLayer('rung2_terminal_solution',(('direct','factored'),),(PathPattern('direct','*+'),PathPattern('factored','*+'))),
)
r=CoherencePyramid(arrows,paths,layers).run();assert r['survivor_count']==16 and r['best_query']['arrow']=='X_exchange_transport'
out={'schema':'marici.conjecture-replay.degree15-coherence-pyramid.v1','typed_arrows':[a.__dict__ for a in arrows],'paths':[{'name':p.name,'arrows':p.arrows} for p in paths],'projection':r,'interpretation':'The first genuine pyramid adds object-level typing without inventing scientific equations; the terminal commuting face reproduces the 16 survivors. No further honest pruning is available until one constituent arrow is observed.','recommendation':'Test X_exchange_transport first: its four-way partition is maximally balanced over the 16 survivors and its declared cost is lowest. Then rebuild the next coherence rung conditionally.','metric_projection':{'base':'previous 16-survivor polarity projection','percent_change_from_previous_base':{'survivor_count':0.0,'typed_arrow_contract_coverage':None,'estimated_next_test_cost':-97.5},'zero_base_note':'typed contract coverage rose from zero, so percentage is undefined rather than infinite','absolute_values_omitted_by_policy':True},'passed':True};p=R/'research/conjecture_replay/results/degree15_coherence_pyramid.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'survivors':16,'best_query':r['best_query'],'percent_delta':out['metric_projection']['percent_change_from_previous_base']}))
