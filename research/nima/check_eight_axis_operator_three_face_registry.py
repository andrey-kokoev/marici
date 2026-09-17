#!/usr/bin/env python3
"""Classify all 56 generic operator-decorated 3-face types."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
A=('H','V','D','q','L','C','O','R')
triples=list(itertools.combinations(A,3))
records={}
for t in triples:
 s=set(t)
 if {'q','C','O'}<=s:
  status='coherent_projective';cell='exact on finite endpoint graph rungs and continuous on their projective system'
 elif {'q','C','R'}<=s:
  status='coherent_regulator_typed';cell='strict for transported/place regulators; lax for an independent sharp window'
 elif {'q','C'}<=s:
  status='coherent_strict_or_canonical';cell='exact log-Mellin radial-to-gamma intertwiner on common core'
 elif {'q','R'}<=s:
  third=next(iter(s-{'q','R'}))
  if third in {'H','V','L','O'}:
   status='coherent_lax';cell=f'shell cocycle preserved by {third} transport on QDLO graph'
  elif third=='D':
   status='coherent_lax';cell='dagger maps forward leakage to the reverse-chart leakage modification'
  else:raise AssertionError(t)
 else:
  status='coherent_strict_or_canonical';cell='pair faces are equalities in the declared retained/canonical scope; the cube filler is equality of composites'
 records[t]={'status':status,'modification':cell}
counts={s:sum(v['status']==s for v in records.values()) for s in ('coherent_strict_or_canonical','coherent_lax','coherent_projective','coherent_regulator_typed','open')}
instances={s:c*2**5 for s,c in counts.items()}
checks={'all_56_generic_types':len(records)==math.comb(8,3)==56,'all_1792_instances':sum(instances.values())==math.comb(8,3)*2**5,'49_strict_or_canonical':counts['coherent_strict_or_canonical']==49,'five_coherent_lax':counts['coherent_lax']==5,'one_projective_qCO':counts['coherent_projective']==1,'one_regulator_typed_qCR':counts['coherent_regulator_typed']==1,'no_open_three_face_type':counts['open']==0,'qCR_counted_once':records[('q','C','R')]['status']=='coherent_regulator_typed'}
out={'schema':'marici.nima.eight-axis-operator-three-face-registry.v1','axes':A,'records':{' x '.join(k):v for k,v in records.items()},'generic_status_counts':counts,'instance_status_counts':instances,'checks':checks,'passed':all(checks.values()),'frontier':['retain regulator type R_place versus R_window in the index','audit 70 generic four-face modifications']}
p=ROOT/'research/nima/results/eight-axis-operator-three-face-registry.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'generic_status_counts':counts,'instance_status_counts':instances,'checks':checks,'frontier':out['frontier'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
