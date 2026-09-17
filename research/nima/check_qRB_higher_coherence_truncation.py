#!/usr/bin/env python3
"""Finite hostile/control test for contractibility of higher qRB coherencers."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eq(a,b):return a==b
I=[[F(1),F(0)],[F(0),F(1)]];U0=I;U1=[[F(1),F(0)],[F(0),F(-1)]]
# One-coordinate observer cannot distinguish two positive isometries.
B=[[F(1),F(0)]];BFULL=I
checks={'distinct_coherencers':not eq(U0,U1),'both_preserve_positive_gram':eq(mm(U0,U0),I) and eq(mm(U1,U1),I),'nonfaithful_observer_identifies_them':eq(mm(B,U0),mm(B,U1)),'faithful_observer_separates_them':not eq(mm(BFULL,U0),mm(BFULL,U1)),'current_source_faithfulness_gate_open':True}
out={'schema':'marici.nima.qRB-higher-coherence-truncation.v1','hostile':{'state_space':'Q^2','positive_gram':'I_2','observer':'B(x1,x2)=x1','coherencers':['I_2','diag(1,-1)'],'result':'distinct positive coherencers have identical observation; higher identity space is not forced contractible'},'control':{'observer':'identity on Q^2','result':'the same coherencers are separated'},'criterion':'jointly faithful B plus uniqueness of q- and R-compatible fillers implies proposition-valued equality of completed coherencers; contractibility additionally requires existence','checks':checks,'current_disposition':'truncation_not_yet_admitted','missing':['joint source-observer faithfulness at completion','uniqueness of symmetry-compatible regulator comparison fillers','existence of the completed positive filler'],'passed':all(checks.values()),'rh_proved':False}
p=ROOT/'research/nima/results/qRB-higher-coherence-truncation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
