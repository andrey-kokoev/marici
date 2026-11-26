"""Executable implication net, for the saved (3,6) core corpus. Exact combinatorial certificate matching, before reading exact outcomes. Runtime excludes graph I/O. Test implications concern PASS predicates; failure travels backward."""
from itertools import combinations
from pathlib import Path
import json,time
P=Path(__file__).resolve().parents[1]/'results';cores=json.loads((P/'ramsey_core_capacity_36.json').read_text());mins=json.loads((P/'ramsey_capacity_fixed_degree.json').read_text());edges=[('integer_feasible','fractional_feasible'),('fractional_feasible','four_K4_capacity'),('fractional_feasible','size_class_capacity')];cases=[]
for idx,row in enumerate(cores):
 a=row['core'];n=len(a);start=time.perf_counter();I=[m for m in range(1<<n) if not any(m>>i&1 and m&v for i,v in enumerate(a))];S=[m for m in I if not any(m!=v and m&v==m for v in I)];Q=[m for m in I if m.bit_count()==4];hits={q:sum(1<<i for i,s in enumerate(S) if q&s) for q in Q};prep=time.perf_counter()-start
 for d in sorted({row['degree'],5}):
  start=time.perf_counter();cert=None
  # For four K4s at target (3,6), demand is 4*(d-1). If no support hits all four, supply <=3*d. The template rejects only on strict inequality.
  if 4*(d-1)>3*d:
   for q in combinations(Q,4):
    if not hits[q[0]]&hits[q[1]]&hits[q[2]]&hits[q[3]]:cert=q;break
  sec=time.perf_counter()-start;truth=row['sat'] if d==row['degree'] else False if any(v['core_index']==idx for v in mins) else None
  if cert is not None:assert truth is not True
  cases.append(dict(index=idx,d=d,screen='reject' if cert else 'undecided',known_feasibility=truth,certificate=cert,prep_seconds=prep,screen_seconds=sec))
relations=[dict(source=u,target=v,kind='one_way_implication',basis='proved',direction='pass') for u,v in edges]+[dict(source='labeled_edge_coloring',target='ordered_support_tuple',kind='witness_translation_commutes_with_restriction',basis='proved',inverse='color edge red exactly on support membership'),dict(source='ordered_support_tuple',target='integer_feasible',kind='same_verdict',basis='proved',reason='enlarge supports to maximal supports; expand integer counts into repeated neighbors'),dict(source='sizes_34',target='sizes_1234',kind='same_verdict',basis='observed_only',scope='16 stored order-11 cores at degree 5',conjecture='R36-CORE11-34',generalization_status='refuted',counterexamples='ramsey_distill_unseen_replay.json')]
print([(r['index'],r['d'],r['screen']) for r in cases]);(P/'ramsey_test_net.json').write_text(json.dumps(dict(pass_implications=edges,relations=relations,rejection_signature_audit='ramsey_rejection_signatures.json',template_discovery_core=4,cases=cases),indent=1)+'\n')
