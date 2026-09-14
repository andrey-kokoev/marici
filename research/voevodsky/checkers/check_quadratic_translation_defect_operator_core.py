#!/usr/bin/env python3
"""Exact polynomial tests of the quadratic translation-defect identity."""
import hashlib,json,platform,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/quadratic_translation_defect_operator_core.v1.json';OUT=ROOT/'research/voevodsky/results/quadratic_translation_defect_operator_core.json';CFG=json.loads(FIX.read_text())
def add(*ps):
 n=max(map(len,ps));return [sum((p[i] if i<len(p) else Q(0)) for p in ps) for i in range(n)]
def scale(c,p):return [c*x for x in p]
def deriv(p):return [Q(i)*p[i] for i in range(1,len(p))] or [Q(0)]
def shift(p,a):
 o=[Q(0)]*len(p)
 for n,c in enumerate(p):
  for k in range(n+1):o[k]+=c*Q(math.comb(n,k))*a**(n-k)
 return o
def A(p):return [Q(0)]+deriv(p)
def P(p):return A(add(A(p),p))
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def eq(a,b):return trim(a[:])==trim(b[:])
def rhs(p,a,with_d2=True):
 d=deriv(p);inside=scale(-2*a,add(A(d),d))
 if with_d2:inside=add(inside,scale(a*a,deriv(d)))
 return shift(inside,a)
degrees=CFG['tested_degrees'];translations=[Q(x) for x in CFG['tested_translations']];tests=[];failed_without=[]
for n in degrees:
 f=[Q(0)]*n+[Q(1)]
 for a in translations:
  lhs=add(P(shift(f,a)),scale(-1,shift(P(f),a)));ok=eq(lhs,rhs(f,a,True));bad=not eq(lhs,rhs(f,a,False))
  tests.append(ok)
  if n>=2:failed_without.append(bad)
checks={'full_identity_all_polynomial_tests':all(tests),'constant_and_linear_cases_included':degrees[:2]==[0,1],'D2_omission_fails_all_degrees_at_least_two':all(failed_without),'multiple_nonzero_translations_tested':len(translations)==4 and all(a!=0 for a in translations),'remaining_composition_not_promoted':'theta summation' in CFG['disposition']['remaining_composition']}
out={'schema':'marici.voevodsky.quadratic-translation-defect-operator-core-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'exact_test_count':len(tests),'deliberate_failure_count':sum(failed_without),'translations':[str(a) for a in translations],'degrees':degrees},'disposition':'The quadratic Duhamel core passes all exact polynomial tests. Removing the even a^2 D^2 channel fails every tested degree at least two. The completed four-front source identity remains downstream.','claim_boundary':CFG['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_quadratic_translation_defect_operator_core.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/CFG['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
