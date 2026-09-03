#!/usr/bin/env python3
"""Expand prime-dependent checkpoint DAGs to labelled source-coordinate vectors."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';files=['cosmology_rees_first_modular_kernel_candidate.json','cosmology_rees_first_modular_kernel_candidate_p103.json','cosmology_rees_first_modular_kernel_candidate_p107.json']
def expand(d):
 p=d['coefficient_prime'];nodes=d['reachable_source_checkpoints'];memo={}
 def add(v,k,a):v[k]=(v.get(k,0)+a)%p
 def node(i):
  if str(i) in memo:return memo[str(i)]
  n=nodes[str(i)];key=(n['grade'],n['label']);v={key:1}
  for _,a,owner in n['steps']:
   if owner[0]=='source':
    for k,x in node(owner[1]).items():add(v,k,-a*x)
  inv=n['pivot'][1];v={k:inv*x%p for k,x in v.items() if inv*x%p};memo[str(i)]=v;return v
 c=d['candidate'];v={(c['grade'],c['label']):1}
 for _,a,owner in c['steps']:
  if owner[0]=='source':
   for k,x in node(owner[1]).items():add(v,k,-a*x)
 return {k:x for k,x in v.items() if x}
data=[json.loads((R/f).read_text()) for f in files];vectors=[expand(d) for d in data];supports=[set(v) for v in vectors];same_support=supports[0]==supports[1]==supports[2];assert same_support
serial=[{'prime':d['coefficient_prime'],'vector':{f'{k[0]}|{k[1]}':v[k] for k in sorted(v)}} for d,v in zip(data,vectors)]
out={'schema':'marici.benincasa.cosmology-rees-expanded-kernel-source-coordinates.v1','problem':'compare prime-dependent kernel DAGs after expansion to source-labelled coordinates','bold_conjecture':'different operation DAGs expand to one common labelled source support suitable for coefficient reconstruction','rivals':['prime-107 topology changes the source vector','DAG differences are presentation-only','supports match but coefficients have no bounded rational reconstruction'],'risky_consequences':'all expanded vectors must have identical labelled support under the canonical unit coefficient normalization','strongest_falsification_attempt':{'vectors':serial,'support_matches':same_support,'support_size':len(supports[0])},'exact_residual':'all three DAGs expand to the same three labelled source coordinates; field coefficients remain to be classified','conjecture_disposition':'retained for source support','coefficient_reconstruction_executed':False,'next_test':'CRT and rationally reconstruct the four normalized coefficients, then reduce the candidate exactly against A5 relations','passed':True};(R/'cosmology_rees_expanded_kernel_source_coordinates.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
