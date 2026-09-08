"""Exact algebraic controls for the punctured-cone obstruction."""
import json
from pathlib import Path
from sympy import symbols,diff,Matrix
r=Path('research/nima/results');p=json.loads((r/'boundary_pivot_charts.json').read_text());assert p['status']=='passed'
a,b,c,d=symbols('a b c d');f=a*d-b*c
assert [diff(f,x) for x in (a,b,c,d)]==[d,-c,-b,a]
# Pic(P1 x P1) modulo the removed zero-section class (1,1).
quotient=Matrix([[1,-1]])
assert quotient*Matrix([1,1])==Matrix([0])
assert quotient*Matrix([-1,0])==Matrix([-1])
# Common scaling is killed, but the row tautological class is not.
assert quotient*Matrix([-1,-1])==Matrix([0])
out={'status':'passed','singular_locus':'a=b=c=d=0','cone_dimension':3,'removed_vertex_codimension':3,'row_tautological_class_in_Z':-1,'diagonal_class_in_Z':0,'scope':'Symbolic controls only. Normality, Hartogs extension and Picard localization arguments are stated in the packet, not certified by sampling.'}
(r/'punctured_face_gluing.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
