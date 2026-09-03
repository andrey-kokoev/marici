#!/usr/bin/env python3
"""Construct Q10 source relations and verify exact inclusion from Q9."""
import contextlib,hashlib,io,json,runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r9=g['construct'](9);r10=g['construct'](10);missing=[k for k in r9 if k not in r10];mismatch=[k for k,v in r9.items() if k in r10 and r10[k]!=v];assert not missing and not mismatch
families=Counter(k[1][0] for k in r10);digest=hashlib.sha256('\n'.join(sorted(map(repr,r10))).encode()).hexdigest();out={'schema':'marici.benincasa.cosmology-rees-Q10-relation-inclusion.v1','Q9_relation_rows':len(r9),'Q10_relation_rows':len(r10),'Q9_missing_in_Q10':len(missing),'Q9_mismatched_in_Q10':len(mismatch),'Q10_family_counts':dict(families),'Q10_label_digest':digest,'tau_representative_fixed':True,'Q10_tau_nonzero_tested':False,'exact_residual':'Q10 contains every Q9 source-labelled relation identically; checkpointed rank/nonmembership remains outstanding','passed':True};(R/'cosmology_rees_Q10_relation_inclusion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
