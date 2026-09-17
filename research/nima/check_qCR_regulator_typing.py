#!/usr/bin/env python3
"""Typing audit for transported, place, and independent-window q-C-R squares."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ledger=(ROOT/'research/voevodsky/source-derived-fourier-sewing-identification-closure-ledger.md').read_text(encoding='utf-8')
# Exact finite conjugacy fixture. C is invertible, Q=C P C^-1.
C=[[Fraction(1),Fraction(1)],[Fraction(0),Fraction(1)]];Ci=[[Fraction(1),Fraction(-1)],[Fraction(0),Fraction(1)]];P=[[Fraction(1),0],[0,0]];Qnative=[[0,0],[0,Fraction(1)]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
Q=mm(mm(C,P),Ci);strict=mm(Q,C)==mm(C,P);defect=sub(mm(Qnative,C),mm(C,P))
checks={'transported_regulator_square_strict':strict,'independent_native_window_has_defect':any(any(x for x in row) for row in defect),'semilocal_operator_declared_cutoff_natural':'It is unitary, cutoff-natural' in ledger,'ledger_declares_semilocal_cutoff_closed':'semilocal cutoff' in ledger and 'analytically closed' in ledger,'place_and_window_regulators_are_same_unlabelled_arrow':False}
out={'schema':'marici.nima.qCR-regulator-typing.v1','transported_fixture':{'C':[[str(x) for x in r] for r in C],'P':[[str(x) for x in r] for r in P],'Q=CPC^-1':[[str(x) for x in r] for r in Q]},'independent_window_defect':[[str(x) for x in r] for r in defect],'checks':checks,'passed':all(v for k,v in checks.items() if k!='place_and_window_regulators_are_same_unlabelled_arrow'),'disposition':{'transported_regulator':'strict','semilocal_place_cutoff':'strict','independent_sharp_window':'lax'},'architectural_result':'R must retain regulator type, or split into R_place and R_window'}
p=ROOT/'research/nima/results/qCR-regulator-typing.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
