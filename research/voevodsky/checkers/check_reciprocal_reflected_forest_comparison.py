#!/usr/bin/env python3
"""Exact obstruction to a reflection-fixed oriented greedy forest."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/reciprocal_reflection_does_not_preserve_an_oriented_greedy_forest_20260911.md'
GRADE=ROOT/'research/voevodsky/contracts/arithmetic-interval-edge-grade.v1.json'
FOREST=ROOT/'research/nima/a-greedy-global-forest-completes-the-cycle-observer-on-the-projective-edge-source.md'
RESULT=ROOT/'research/voevodsky/results/reciprocal_reflected_forest_comparison.json'
g=json.loads(GRADE.read_text()); checks={}
# Two reciprocal oriented edges on two vertices.
boundary=s.Matrix([[-1,1],[1,-1]]); R=s.Matrix([[0,1],[1,0]])
T=s.Matrix([[1,0]]); RT=s.Matrix([[0,1]])
checks['reciprocal_action_involution']=R*R==s.eye(2)
checks['boundary_cycle_rank_one']=2-boundary.rank()==1
checks['minimal_forests_distinct']=T!=RT
checks['reflection_exchanges_forests']=T*R==RT and RT*R==T
# No one-edge spanning tree is fixed by the free swap.
checks['no_reflection_fixed_spanning_tree']=all(v*R!=v for v in (T,RT))
cycle=s.Matrix([1,1]); checks['cycle_space_reflection_canonical']=boundary*cycle==s.zeros(2,1) and R*cycle==cycle
# Chord coordinates in T and RT both recover the same cycle coefficient.
ZT=s.Matrix([[0,1]]); ZRT=s.Matrix([[1,0]])
checks['reflected_chord_comparison']=ZT*cycle==ZRT*R*cycle==s.Matrix([1])
w=s.symbols('w',positive=True); W=s.diag(w,w); Q=(cycle.T*W*cycle)[0]
checks['reflection_invariant_edge_form']=R.T*W*R==W
checks['cycle_metric_preserved']=Q==2*w
checks['grade_reflection_invariant']=g['grade']['reciprocal_invariance']=='W_star(n,p,q)=W_star(n,q,p)'
checks['order_claim_only_adjacency']=g['ordering']['reciprocal_policy'].startswith('reciprocal pair is adjacent')
checks['prior_packet_left_reflection_open']='whether reciprocal reflection preserves it' in FOREST.read_text()
# Hostile inference explicitly fails.
checks['adjacent_pair_does_not_imply_fixed_forest']=checks['minimal_forests_distinct'] and checks['no_reflection_fixed_spanning_tree']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.reciprocal-reflected-forest-comparison.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'grade':hashlib.sha256(GRADE.read_bytes()).hexdigest(),'prior_forest':hashlib.sha256(FOREST.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'refuted':'reflection-fixed oriented greedy forest from adjacent reciprocal ordering','retained':'reciprocal-invariant grade, projective cycle space, and reflected-forest coordinate comparison','replacement':'forest-presentation groupoid with integral transition maps and metric congruence'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'fixed_forests':0,'cycle_rank':1}))
raise SystemExit(0 if result['passed'] else 1)
