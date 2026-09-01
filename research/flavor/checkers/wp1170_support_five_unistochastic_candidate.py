import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
q=[6/23,8/23,1/23,4/23,2/23,2/23]
u=1/6
S=[
 [0.0,0.45817697275369973,0.17841587689616611,-0.55027661013538387,-0.37644211228438901,0.56011483222692338],
 [-0.63538704398078227,0.0,-0.5094713149644986,-0.48889033968845658,0.0082493604828593001,-0.31247474705885059],
 [-0.27816302374695018,-0.50284017437630824,0.0,-0.058073862348780536,0.46804327630365239,0.66883481498785669],
 [-0.27868928969357498,0.53678304918232644,0.45404147396496292,0.0,0.63517444940278522,-0.1568311056928941],
 [-0.16452984636769791,0.47970294824626064,-0.5501140996228282,0.56876584465731139,0.0,0.3416063549140344],
 [-0.64356106648882616,-0.13774853857409267,0.44702077294594211,0.36237374154093333,-0.48550200252964121,0.0]]
P=[[x*x for x in row] for row in S]
tolerance=1e-7
row_norm_errors=[abs(sum(x*x for x in row)-1) for row in S]
col_norm_errors=[abs(sum(S[i][j]**2 for i in range(6))-1) for j in range(6)]
row_dot_errors=[abs(sum(S[i][j]*S[k][j] for j in range(6))) for i in range(6) for k in range(i+1,6)]
col_dot_errors=[abs(sum(S[i][a]*S[i][b] for i in range(6))) for a in range(6) for b in range(a+1,6)]
fixed_q_errors=[abs(sum(P[i][j]*q[j] for j in range(6))-u) for i in range(6)]
assert all(x == 0 for i,x in enumerate(S[i][i] for i in range(6)))
assert all(S[i][j] != 0 for i in range(6) for j in range(6) if i != j)
assert max(row_norm_errors+col_norm_errors+row_dot_errors+col_dot_errors+fixed_q_errors) < tolerance
assert all(sum(row)-1 < tolerance and 1-sum(row) < tolerance for row in P)
assert all(abs(sum(P[i][j] for i in range(6))-1) < tolerance for j in range(6))
result={
    "schema":"marici.flavor.wp1170.v1",
    "status":"PASS",
    "question":"Does a constrained support-five fixed-q polytope contain a numerical unistochastic candidate?",
    "dpc":{
        "conjecture":"A zero-diagonal support-five carrier has a real unistochastic fixed-q point.",
        "rivals":["polygon-only obstruction","real orthogonal witness","complex phase witness","exact algebraic certificate"],
        "risky_consequences":["zero diagonal","30 nonzero entries","orthonormal rows and columns","row q expectation 1/6"],
        "falsification_attempt":"Adam optimization over real zero-diagonal matrices converged to a candidate with maximum residual below 1e-7.",
        "residual":"The candidate is numerical; exact real-algebraic certification remains open.",
        "disposition":"accept a numerical candidate and select exactification"
    },
    "candidate_matrix":S,
    "maximum_row_norm_error":max(row_norm_errors),
    "maximum_column_norm_error":max(col_norm_errors),
    "maximum_row_dot_error":max(row_dot_errors),
    "maximum_column_dot_error":max(col_dot_errors),
    "maximum_fixed_q_error":max(fixed_q_errors),
    "tolerance":tolerance,
    "classification":"productive numerical gate: constrained support-five search found a real unistochastic fixed-q candidate",
    "remaining_gate":"exactify the numerical orthogonal matrix and certify the algebraic solution",
    "hostile_gate":"do not treat numerical convergence as exact algebraic proof",
    "claim_boundary":"the result is a bounded numerical candidate, not an exact certificate",
    "disposition":"constrained support-five search resolved; exactification rival selected"
}
(ROOT/"results"/"wp1170_support_five_unistochastic_candidate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1170 PASS:",max(row_norm_errors+col_norm_errors+row_dot_errors+col_dot_errors+fixed_q_errors))
