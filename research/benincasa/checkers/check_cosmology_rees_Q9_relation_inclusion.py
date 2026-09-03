#!/usr/bin/env python3
"""Construct Q9 source relations and verify exact inclusion from Q8."""
import contextlib,hashlib,io,json,runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r8=g['construct'](8);r9=g['construct'](9);missing=[k for k in r8 if k not in r9];mismatch=[k for k,v in r8.items() if k in r9 and r9[k]!=v];assert not missing and not mismatch
families=Counter(k[1][0] for k in r9);digest=hashlib.sha256('\n'.join(sorted(map(repr,r9))).encode()).hexdigest()
out={'schema':'marici.benincasa.cosmology-rees-Q9-relation-inclusion.v1','Q8_relation_rows':len(r8),'Q9_relation_rows':len(r9),'Q8_missing_in_Q9':len(missing),'Q8_mismatched_in_Q9':len(mismatch),'Q9_family_counts':dict(families),'Q9_label_digest':digest,'tau_representative_fixed':True,'Q9_tau_nonzero_tested':False,'exact_residual':'Q9 is constructed and contains every Q8 source-labelled relation identically; the rank/nonmembership reduction remains outstanding','passed':True};(R/'cosmology_rees_Q9_relation_inclusion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
