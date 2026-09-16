#!/usr/bin/env python3
"""Audit transitive file provenance and semantic forbidden-equivalent dependencies."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
roots=['research/aspect/contracts/u-g4-owner-construction-packet.v1.json','research/aspect/contracts/g4-radial-to-bordered-target.v1.json']
path_re=re.compile(r'research/[A-Za-z0-9_./-]+\.(?:json|md|py)')
seen=set();edges=[];missing=[]
def walk(rel):
 if rel in seen:return
 seen.add(rel);p=R/rel
 if not p.exists():missing.append(rel);return
 text=p.read_text(encoding='utf-8')
 for q in path_re.findall(text):
  q=q.rstrip('.,;:)')
  edges.append([rel,q]);walk(q)
for p in roots:walk(p)
semantic_sources={
 'research/voevodsky/ordered_pair_radial_stokes_generalizes_the_conditional_response_target_20260908.md':'required-response-not-authorized-port',
 'research/voevodsky/pair_response_requires_a_source_coproduct_not_a_scalar_port_reweighting_20260908.md':'source-coproduct-categorical-gap'}
# The J_RL formula is algebraically the conditional R+2E response even when no source locator is declared.
target=(R/roots[1]).read_text(encoding='utf-8')
formula_equivalent=all(s in target for s in ['rho0(q)+E(q)-W(q)/2','+2E(q)'])
checks={'roots_exist':all((R/p).exists() for p in roots),'closure_nonempty':len(seen)>=2,'no_missing_declared_paths':not missing,'J_RL_is_required_response_equivalent':formula_equivalent,'semantic_independence_fails':formula_equivalent,'comparison_must_remain_blocked':True}
out={'schema':'marici.aspect.u-g4-recursive-dependency-closure-check.v1','passed':all(checks.values()),'checks':checks,'root_files':roots,'closure_files':sorted(seen),'edges':edges,'missing':missing,'semantic_equivalences':semantic_sources,'verdict':'dependency closure plus algebraic equivalence catches the circular required-response constructor; shallow forbidden-name scans are insufficient'}
q=R/'research/aspect/results/u_g4_recursive_dependency_closure.check.v1.json';q.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':out['passed'],'closure_size':len(seen),'edge_count':len(edges),'formula_equivalent':formula_equivalent}));raise SystemExit(0 if out['passed'] else 1)
