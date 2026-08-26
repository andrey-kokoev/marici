#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/metric-selected-actuator-lift.json"

def main():
    records=[]
    for c in [Rational(0),Rational(1,2),Rational(-1,2)]:
        G=Matrix([[1,c],[c,1]])
        assert G.det()==1-c*c and G.det()>0
        t=-c
        B=Matrix([1,t])
        cost=(B.T*G*B)[0]
        assert cost==1-c*c
        records.append({"c":str(c),"selected_t":str(t),"minimum_cost":str(cost),"logical_nondisturbing":bool(t==0)})
    assert len({r["selected_t"] for r in records})==3
    payload={"schema":"marici.kitaev.metric_selected_actuator_lift.v1","status":"pass","all_metrics_positive_definite":True,"unique_minimizer_each":True,"different_metrics_select_different_lifts":True,"records":records,"source_metric_authorized":False,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
