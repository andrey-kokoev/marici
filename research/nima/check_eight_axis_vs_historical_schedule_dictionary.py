#!/usr/bin/env python3
"""Audit whether historical 0AJPCTEF schedules are permutations of the eight proposed axes."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
historical=('0','A','J','P','C','T','E','F')
transitions=historical[1:]
axes=('H','V','D','q','L','Ccmp','O','R')
meaning={
 '0':'initial source object (not an operation)',
 'A':'semilocal amplification / adjoining conductor places',
 'J':'canonical-dual or primal-contragredient presentation',
 'P':'convolution-square polarization',
 'C':'physical/Fourier cutoff pair and Halmos colligation',
 'T':'semilocal trace and finite-part observation',
 'E':'endpoint-gamma completion',
 'F':'positive apex filler comparing trace and Gram routes',
}
candidates={
 'A':['L','Ccmp'],
 'J':['D','Ccmp'],
 'P':['D'],
 'C':['q','R'],
 'T':['O'],
 'E':['O','R'],
 'F':['Ccmp'],
}
checks={
 'same_factorial_count':len(historical)==len(axes)==8,
 'historical_has_only_seven_transitions':len(transitions)==7,
 'historical_zero_is_object_not_axis':meaning['0'].endswith('(not an operation)'),
 'no_candidate_for_H':all('H' not in xs for xs in candidates.values()),
 'no_candidate_for_V':all('V' not in xs for xs in candidates.values()),
 'ambiguous_compound_matches_exist':any(len(xs)>1 for xs in candidates.values()),
 'source_derived_bijection_exists':False,
}
out={'schema':'marici.nima.eight-axis-vs-historical-schedule-dictionary.v1','historical_symbols':historical,'historical_meanings':meaning,'proposed_axes':axes,'candidate_noncanonical_correspondences':candidates,'checks':checks,'passed':all(v for k,v in checks.items() if k!='source_derived_bijection_exists'),'conclusion':'The common number 40320 is factorially equal but the indexed sets differ: historical schedules permute one initial object plus seven transitions, while the proposed 8-cube permutes eight operation axes. No source-derived bijection exists; H and V are absent and several historical transitions combine q/R/O/Ccmp roles.'}
p=ROOT/'research/nima/results/eight-axis-vs-historical-schedule-dictionary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
