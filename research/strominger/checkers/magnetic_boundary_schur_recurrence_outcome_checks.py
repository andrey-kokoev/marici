import json, math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];prefix=ROOT/"research/strominger/checkers/capcl_magnetic_chart_r8_outcome_checks.py"
ns={"__file__":str(prefix)};exec(compile(prefix.read_text().split("cols=component")[0],str(prefix),"exec"),ns)
rf=lambda x,n:math.prod(x+i for i in range(n))
def schur(r):
 g=2*r;cs=ns["component"](g,g//2+4,2*g+8);rows=[3 if x==1 else x for x in ns["hall_rows"](cs)]
 total=ns["det_bareiss"]([[c.get(x,0) for c in cs] for x in rows]);labs=([(0,"+")]+[(a,s) for a in range(2,g+9,2) for s in ("-","+")])[:-1]
 core=math.prod([-(2*g+9)*rf(4,g) if a==0 else (-(3*g+7+a)*rf(a,g) if s=="-" else -(g+9-a)*rf(a,g)) for a,s in labs]);return Fraction(total,core)
def predicted(r):
 return Fraction(8*(r+1)*(r+2)*(r+3)*(2*r+5)**2*(4*r+5)*(4*r+11)*(2*r*r+3*r-12),r*(r+4)*(2*r+9)*(2*r*r-r-13))
def fraction_rising(value,count): return math.prod((value+i for i in range(count)),start=Fraction(1))
def closed(r):
 return Fraction(70400,3)*2*2**(8*(r-1))*Fraction(math.factorial(r)*math.factorial(r+1)*math.factorial(r+2),math.factorial(r-1)*math.factorial(r+3))*fraction_rising(Fraction(7,2),r-1)**2*fraction_rising(Fraction(9,4),r-1)*fraction_rising(Fraction(15,4),r-1)/fraction_rising(Fraction(11,2),r-1)*Fraction(2*r*r-r-13,-12)
values={r:schur(r) for r in range(20,31)};records=[]
for r in range(20,30):
 actual=values[r+1]/values[r];expected=predicted(r);records.append({"r":r,"g_next":2*(r+1),"matches":actual==expected,"nonzero":actual!=0})
closed_matches=all(values[r]==closed(r) for r in values)
passed=all(x["matches"] and x["nonzero"] for x in records) and closed_matches
result={"schema":"marici.strominger.prediction-outcome.v1","prediction_id":"magnetic-boundary-schur-recurrence-004","outcome":"confirmed_in_declared_range" if passed else "falsified","passed":passed,"records":records,"closed_hypergeometric_character_matches":closed_matches,"closed_character_nonzero_reason":"positive_factorials_and_Pochhammers_times_quadratic_with_discriminant_105","first_falsifier":next((x for x in records if not x["matches"] or not x["nonzero"]),None)}
(ROOT/"research/strominger/results/magnetic_boundary_schur_recurrence_outcome.json").write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
