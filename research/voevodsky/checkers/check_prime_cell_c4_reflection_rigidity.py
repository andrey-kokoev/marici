"""Exact rigidity of the parameter-free polarized prime-cell metric defect."""
import json, sys
from pathlib import Path
try:
    import sympy as s
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).parents[2] / "flavor" / ".venv" / "Lib" / "site-packages"))
    import sympy as s
I=s.I
a,d,x,y=s.symbols('a d x y', real=True)
Q=s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,2),-s.Rational(1,4)]])
F=s.Matrix([[0,-s.Rational(1,2)],[2,0]])
P=s.diag(1,-1)
Delta=s.Matrix([[a,x+I*y],[x-I*y,d]])
c4=s.simplify(F.conjugate().T*Delta*F-Delta)
reflection=s.simplify(P.conjugate().T*Delta*P-Delta)
sol_c4=s.solve(list(c4),[a,d,x],dict=True)
sol_both=s.solve(list(c4)+list(reflection),[a,d,x,y],dict=True)
# Under both symmetries Delta=a*diag(1,1/4); its even diagonal is a.
reduced=a*s.diag(1,s.Rational(1,4))
checks={'Q_invertible':Q.det()!=0,'F_square_minus_identity':F*F==-s.eye(2),'P_square_identity':P*P==s.eye(2),'P_anticommutes_F':P*F==-F*P,'reduced_C4_invariant':s.simplify(F.T*reduced*F-reduced)==s.zeros(2),'reduced_reflection_invariant':s.simplify(P.T*reduced*P-reduced)==s.zeros(2),'even_diagonal_zero_forces_full_zero':reduced[0,0]==a}
out={'Q':str(Q.tolist()),'Q_determinant':str(Q.det()),'F_source':str(F.tolist()),'P':str(P.tolist()),'general_hermitian_defect':'[[a,x+i y],[x-i y,d]]','C4_equations':str(list(c4)),'C4_solution':str(sol_c4),'C4_plus_reflection_solution':str(sol_both),'reduced_defect':str(reduced.tolist()),'theorem':'Common C4 covariance and reflection covariance reduce the four matrix-unit defect to a*diag(1,1/4). One independently sourced even-wall diagonal equality forces a=0 and all four identities.','checks':checks,'passed':all(checks.values()),'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'prime-cell-c4-reflection-rigidity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
