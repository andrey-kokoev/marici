#!/usr/bin/env python3
"""Audit the Lean polygon-diagonal carrier against the executable CR convention."""
from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parents[3];p=R/'research/buzzard/marici_formal/MariciFormal/CoherentResolutionTransport.lean';t=p.read_text(encoding='utf-8');build=subprocess.run(['lake','build'],cwd=p.parents[1],capture_output=True,text=True)
def old_pred(n,a,b):return a!=b and a+1!=b and b+1!=a
def new_pred(n,a,b):return a<b and (a+1)%n!=b and (b+1)%n!=a
def expected(n,a,b):return a<b and b!=a+1 and not(a==0 and b==n-1)
rows=[]
for n in range(4,9):
 rows.append({'n':n,'expected_count':n*(n-3)//2,'new_count':sum(new_pred(n,a,b) for a in range(n) for b in range(n)),'old_count':sum(old_pred(n,a,b) for a in range(n) for b in range(n)),'new_matches_expected_pointwise':all(new_pred(n,a,b)==expected(n,a,b) for a in range(n) for b in range(n))})
checks={'lean_build_passes':build.returncode==0,'modular_adjacency_present':'(a.val + 1) % n ≠ b.val' in t and '(b.val + 1) % n ≠ a.val' in t,'canonical_endpoint_order_present':'a.val < b.val' in t,'old_wraparound_counterexample_confirmed':old_pred(4,0,3),'new_rejects_wraparound':not new_pred(4,0,3),'new_rejects_reverse_duplicates':not new_pred(6,4,1),'counts_match_all_tested':all(x['new_count']==x['expected_count'] and x['new_matches_expected_pointwise'] for x in rows)}
out={'schema':'marici.nima.lean-polygon-diagonal-alignment.v1','checks':checks,'passed':all(checks.values()),'rows':rows,'repaired_mismatch':'The previous Lean predicate admitted the wrap-around boundary edge (0,n-1), both endpoint orientations, and therefore did not define the same diagonal carrier as the Python CR construction. Modular adjacency plus a<b repairs the carrier-level mismatch.','remaining_gap':'The Lean structure still defines partial triangulations and transport lemmas, but not yet the strict-chain augmented complex, alternating differential, cone homotopy, or arbitrary-m exactness theorem.','claim_boundary':'This validates the polygon-diagonal object convention and build only; it does not close the remaining chain-complex formalization.'}
outp=R/'research/nima/results/lean-polygon-diagonal-alignment.json';outp.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
