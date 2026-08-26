#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/symmetry-selected-actuator-origin.json"

def average_orbit(t, action):
    return (t+action(t))/2

def main():
    reflection=lambda t:-t
    trivial=lambda t:t
    affine=lambda t:1-t
    samples=[Rational(-2),Rational(0),Rational(3,2)]
    assert all(average_orbit(t,reflection)==0 for t in samples)
    assert all(average_orbit(t,trivial)==t for t in samples)
    assert all(average_orbit(t,affine)==Rational(1,2) for t in samples)
    assert reflection(reflection(2))==2 and affine(affine(2))==2
    payload={"schema":"marici.kitaev.symmetry_selected_actuator_origin.v1","status":"pass","reflection_unique_fixed_origin":"0","trivial_action_unique":False,"affine_reflection_fixed_origin":"1/2","affine_fixed_origin_logically_nondisturbing":False,"finite_group_average_mathematical":True,"physical_average_authorized":False,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
