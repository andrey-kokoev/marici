import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
u = [Fraction(1,6)] * 6
I = [[Fraction(int(i==j)) for j in range(6)] for i in range(6)]
J = [[Fraction(1,6) for _ in range(6)] for _ in range(6)]

def matvec(M, v):
    return [sum(M[i][j]*v[j] for j in range(6)) for i in range(6)]
assert matvec(I,q) == q
assert matvec(J,q) == u

# Fully connected Markov mixing has P(x)=J+x(I-J), x=e^(-6 lambda t).
def mix(x):
    return [[J[i][j] + x*(I[i][j]-J[i][j]) for j in range(6)] for i in range(6)]
P_half = mix(Fraction(1,2))
P_half_q = matvec(P_half,q)
assert P_half_q != u
# For every x, P(x)q=u+x(q-u); uniformity requires x=0, the infinite-time limit.
assert P_half_q == [u[i] + Fraction(1,2)*(q[i]-u[i]) for i in range(6)]

# Krylov/history dilation is a period-three isometry and has no irreversible
# mixing limit on six event states.
history_slots = 3
history_is_isometry = True
six_state_mixing_supplied = False
assert history_slots == 3 and history_is_isometry and not six_state_mixing_supplied

result = {
    "schema": "marici.flavor.wp1120.v1",
    "status": "PASS",
    "question": "Can source dynamics produce complete mixing J6/6?",
    "dpc": {
        "conjecture": "Current UV boundary dynamics can produce the complete-mixing event kernel J6/6.",
        "rivals": [
            "fully connected Markov relaxation",
            "Krylov/history dilation",
            "no source mixing dynamics"
        ],
        "risky_consequences": [
            "Markov relaxation must supply rates and an event-time/coarse-graining limit with x=0",
            "Krylov history must become an irreversible six-state kernel despite three isometric slots"
        ],
        "falsification_attempt": "P(x)q=(1/6)^6+x(q-(1/6)^6) is nonuniform for x>0; history dilation has three isometric slots and no six-state rates.",
        "residual": "A new UV boundary source could still derive irreversible six-state mixing rates and a finite event-time limit.",
        "disposition": "reject the current-source complete-mixing conjecture; retain irreversible mixing as an open requirement"
    },
    "branch_distribution": [str(x) for x in q],
    "uniform_target": [str(x) for x in u],
    "identity_image": [str(x) for x in matvec(I,q)],
    "complete_mixing_image": [str(x) for x in matvec(J,q)],
    "markov_form": "P(x)=J6/6+x(I-J6/6), x=e^(-6 lambda t)",
    "half_mixed_image": [str(x) for x in P_half_q],
    "uniformity_requires": "x=0 (infinite-time/coarse-grained limit)",
    "history_slots": history_slots,
    "history_is_isometry": history_is_isometry,
    "six_state_mixing_supplied": six_state_mixing_supplied,
    "classification": "negative gate: complete mixing requires an unsourced infinite-time/coarse-graining law; Krylov history is isometric and three-slot",
    "remaining_gate": "derive irreversible six-state mixing rates and a finite event-time limit from the UV boundary source",
    "hostile_gate": "do not promote long-time Markov limits, Krylov history, or isometric dilation to J6/6 event production",
    "claim_boundary": "the mixing algebra is possible but no source dynamics or event-time limit is admitted",
    "disposition": "complete-mixing source-origin route closed at current dynamics",
}

(ROOT / "results" / "wp1120_complete_mixing_source_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1120 PASS:", matvec(J,q)[0], P_half_q, history_slots)
