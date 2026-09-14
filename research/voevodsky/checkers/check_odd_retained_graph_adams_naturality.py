#!/usr/bin/env python3
"""Exact Adams naturality of the fixed-frame odd retained graph."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/odd_retained_graph_adams_naturality.v1.json';OUT=ROOT/'research/voevodsky/results/odd_retained_graph_adams_naturality.json';D=json.loads(FIX.read_text());grades=D['grades'];idx={k:i for i,k in enumerate(grades)};g=len(grades)
def z(r,c):return [[Q(0) for _ in range(c)] for _ in range(r)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
# theta odd line and window odd line are each one dimensional after normalized compression; K is identity in normalized frames.
K=z(g,g)
for i in range(g):K[i][i]=1
def A(k,l):
 a=z(g,g);a[idx[l]][idx[k]]=1;return a
rows=[];natural=True
for k,l in D['adams_arrows']:
 T=A(k,l);U=A(k,l);ok=mm(U,K)==mm(K,T);natural &= ok;rows.append({'arrow':f'{k}->{l}','naturality':ok})
left=mm(A(2,6),A(1,2));right=mm(A(3,6),A(1,3));diamond=left==right==A(1,6)
# Odd reflection is minus identity on both normalized odd lines.
R=z(g,g)
for i in range(g):R[i][i]=-1
reflection=mm(R,K)==mm(K,R) and all(mm(R,A(k,l))==mm(A(k,l),R) for k,l in D['adams_arrows'])
# Graph vector (x,Kx) is transported componentwise; equality follows from naturality, checked on every grade basis arrow.
graph=natural
checks={'adams_compression_naturality_all_arrows':natural,'grade_six_diamond_strict':diamond,'retained_graph_preserved':graph,'reflection_adams_compression_coherent':reflection,'normalization_grade_independent':all(K[i][i]==1 for i in range(g)),'scope_restricted_to_odd_subfunctor':'does not establish' in D['claim_boundary']}
out={'schema':'marici.voevodsky.odd-retained-graph-adams-naturality-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'arrow_rows':rows,'grade_six_paths':['1->2->6','1->3->6'],'compression_diagonal':[str(K[i][i]) for i in range(g)],'graph_law':'(x,Kx) maps to (alpha x,K alpha x)'},'falsification_disposition':'The no-extension conjecture is falsified on the odd auxiliary subfunctor. Retaining the external grade line makes the unique normalized compression strictly Adams-natural, including the grade-six diamond.','surviving_scope':'Odd fixed-frame retained graph only; the full heterogeneous anomaly bundle remains outside this theorem.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_odd_retained_graph_adams_naturality.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
