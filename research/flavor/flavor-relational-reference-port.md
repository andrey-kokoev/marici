# A flavor reference port defines a new relational experiment (WP55)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Candidate and exact gate

Add a normalized reference ray (r) in left-handed generation space and form

\[
\mathcal O_r(H)=r^\dagger Hr.
\]

For (H=\operatorname{diag}(1,4,9)), (r=e_1), and the exact (3/5,4/5)
rotation (Q), the matrices (H) and (QHQ^\dagger) are on the same
weak-basis orbit. Nevertheless,

\[
\mathcal O_r(H)=1,
\qquad
\mathcal O_r(QHQ^\dagger)=73/25.
\]

Holding (r) fixed therefore makes the readout fail descent on the original
physical quotient.

## Changed groupoid

Descent is restored only on the enlarged state space of pairs:

\[
(H,r)\longmapsto(QHQ^\dagger,Qr),
\qquad
\mathcal O_{Qr}(QHQ^\dagger)=\mathcal O_r(H).
\]

Choosing a fixed reference gauge replaces the full weak-basis groupoid by the
stabilizer groupoid `Stab(r)`. This is a new relational experiment. It is not
recovery of an absolute coordinate or phase of the original experiment.

## Selector and instrument disposition

The port does not select a proper subfamily of the original `physical16`
quotient. It enriches each state with new relational data. Nor is it merely a
sparse-chart rigidifier: its objects are different physical descriptions,
namely `(flavor, reference)` pairs.

No declared flavor instrument prepares or measures an independent generation-
space reference ray. Standard charged-current measurements use the Yukawa
eigenbases themselves and therefore do not supply an external (r). Algebraic
availability of (r^\dagger Hr) is not executable control.

Smallest exact falsifier of original descent: the values (1) and (73/25)
above on one weak-basis orbit. The only repair is simultaneous transformation
of the reference, which explicitly changes the groupoid.

## Verification

`uv run --with sympy python research/flavor/checkers/wp55_relational_reference_port.py`
writes `research/flavor/results/wp55_relational_reference_port.json`.
