#!/usr/bin/env python3
"""Expand genuine quotient-kernel DAGs to faithful A4 quotient coordinates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';files=['cosmology_rees_first_quotient_kernel_candidate.json','cosmology_rees_first_quotient_kernel_candidate_p103.json','cosmology_rees_first_quotient_kernel_candidate_p107.json']
def expand(d):
 p=d['coefficient_prime'];nodes=d['reachable_quotient_checkpoints'];memo={}
 def add(v,k,a):v[k]=(v.get(k,0)+a)%p
 def node(i):
  if str(i) in memo:return memo[str(i)]
  n=nodes[str(i)];key=(n['grade'],n['label']);v={key:1}
  for _,a,owner in n['steps']:
   if owner[0]=='quotient':
    for k,x in node(owner[1]).items():add(v,k,-a*x)
  inv=n['pivot'][1];v={k:inv*x%p for k,x in v.items() if inv*x%p};memo[str(i)]=v;return v
 c=d['candidate'];v={(c['grade'],c['label']):1}
 for _,a,owner in c['steps']:
  if owner[0]=='quotient':
   for k,x in node(owner[1]).items():add(v,k,-a*x)
 return {k:x for k,x in v.items() if x}
data=[json.loads((R/f).read_text()) for f in files];vectors=[expand(d) for d in data];supports=[set(v) for v in vectors];same=supports[0]==supports[1]==supports[2]
serial=[{'prime':d['coefficient_prime'],'vector':{f'{k[0]}|{k[1]}':v[k] for k in sorted(v)}} for d,v in zip(data,vectors)]
out={'schema':'marici.benincasa.cosmology-rees-expanded-faithful-kernel-coordinates.v1','problem':'compare genuine transition-kernel candidates in faithful A4 quotient coordinates','bold_conjecture':'prime-dependent reduction DAGs expand to one common quotient-coordinate support','risky_consequences':'all normalized vectors must have the same faithful labelled support','strongest_falsification_attempt':{'vectors':serial,'support_matches':same,'support_sizes':[len(x) for x in supports]},'exact_residual':('all supports match; coefficients require reconstruction' if same else 'faithful quotient supports differ across primes'),'conjecture_disposition':('retained' if same else 'falsified'),'scope':'three modular quotient vectors; no rational lift','passed':True};(R/'cosmology_rees_expanded_faithful_kernel_coordinates.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
