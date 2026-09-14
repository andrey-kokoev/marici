#!/usr/bin/env python3
"""Exact doubled-shift Green identity with both finite boundary defects."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_doubled_bordered_colligation_green_identity.v1.json';SRC=ROOT/'research/voevodsky/fixtures/prime_two_bordered_valuation_colligation.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_doubled_bordered_colligation_green_identity.json';D=json.loads(FIX.read_text());N=D['depth'];n=N+1
def eye(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def tp(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mv(a,v):return [sum(r[j]*v[j] for j in range(len(v))) for r in a]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
S=[[Fraction(0) for _ in range(n)] for _ in range(n)]
for k in range(N):S[k+1][k]=1
St=tp(S);I=eye(n);P0=sub(I,mm(S,St));PN=sub(I,mm(St,S));G=sub(P0,PN);pullback=sub(mm(St,S),mm(S,St))
# L=[S;S*], J=diag(I,-I), computed blockwise as S*S-(S*)*S*=S*S-SS*.
q=Fraction(1,2);x=[q**k for k in range(n)];lhs=dot(mv(S,x),mv(S,x))-dot(mv(St,x),mv(St,x));rhs=dot(x,mv(G,x));expected=1-q**(2*N)
# Bilinear hostile: deleting terminal endpoint fails on e_N.
eN=[Fraction(i==N) for i in range(n)];deleted_rhs=dot(eN,mv(P0,eN));true_rhs=dot(eN,mv(G,eN))
checks={'operator_green_identity':pullback==G,'source_defect_rank_one':sum(P0[i][i] for i in range(n))==1,'terminal_defect_rank_one':sum(PN[i][i] for i in range(n))==1,'resolvent_green_identity_at_exact_q':lhs==rhs==expected,'endpoint_formula_exact':expected==Fraction(63,64),'delete_terminal_defect_deliberate_failure':deleted_rhs==0 and true_rhs==-1,'completion_not_promoted':D['completion_gate']['status']=='conditional','next_labelled_map_retained':'common labelled defect object D_X' in D['disposition']['first_missing_typed_datum']}
out={'schema':'marici.voevodsky.prime-two-doubled-bordered-colligation-green-identity-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'green_boundary_diagonal':[str(G[i][i]) for i in range(n)],'q':'1/2','resolvent_lhs':str(lhs),'resolvent_rhs':str(rhs),'expected':'63/64','terminal_deletion_hostile':{'deleted_rhs':str(deleted_rhs),'true_rhs':str(true_rhs)}},'disposition':'The doubled direct/dual colligation has exact Green pullback P0-PN. The backward map now reaches a two-endpoint defect object; transport into the full labelled D_X remains missing.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_doubled_bordered_colligation_green_identity.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
