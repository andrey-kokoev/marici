#!/usr/bin/env python3
"""Exact four-valued survivor projection for the CR1 package coherence rung."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from coherence_pyramid import TypedArrow as A,PathPattern as P,CoherenceLayer as L,CoherencePyramid
from composite_arrow_tests import ArrowPath
arrows=(
 A('PK1_vertices','source','vertices',5),A('PK2_roads','vertices','roads',5),
 A('PK3_Cech','roads','globalMap',8),A('PK4_sixFunctor','globalMap','supportInput',13),
 A('PK5_symmetry','roads','supportInput',8),A('PK6_support','supportInput','supportWitness',10),
 A('PK7_readout','source','readoutWitness',13),
 A('PK8G_zero_from_support','supportWitness','package',5),
 A('PK8A_zero_from_readout','readoutWitness','package',5),
)
paths=(
 ArrowPath('geometric_descent_path',('PK1_vertices','PK2_roads','PK3_Cech','PK4_sixFunctor','PK6_support','PK8G_zero_from_support')),
 ArrowPath('geometric_symmetry_path',('PK1_vertices','PK2_roads','PK5_symmetry','PK6_support','PK8G_zero_from_support')),
 ArrowPath('analytic_readout_path',('PK7_readout','PK8A_zero_from_readout')),
)
layers=(
 L('support_diamond',equal_paths=(('geometric_descent_path','geometric_symmetry_path'),)),
 L('geometric_analytic_zero_diamond',equal_paths=(('geometric_descent_path','analytic_readout_path'),)),
 L('inhabited_package_terminal_polarity',patterns=tuple(P(p.name,'*+') for p in paths)),
)
pyr=CoherencePyramid(arrows,paths,layers,max_assignments=1_000_000);projection=pyr.run()
out={'schema':'marici.conjecture-replay.CR1-physical-source-coherence-survivors.v1','source':'research/conjecture_replay/results/CR1_physical_source_package_coherence.json','semantics':'exact signed-arrow projection only; survivors are formal polarity assignments, not geometric constructions','arrows':[a.__dict__ for a in arrows],'paths':[p.__dict__ for p in paths],'layers':[{'name':x.name,'equal_paths':x.equal_paths,'patterns':[z.__dict__ for z in x.patterns]} for x in layers],'projection':projection,'observed_successful_geometric_paths':0,'passed':projection['survivor_count']>0};p=R/'research/conjecture_replay/results/CR1_physical_source_coherence_survivors.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'initial':projection['initial_assignments'],'survivors':projection['survivor_count'],'layers':projection['layers'],'best_query':projection['best_query']}))
