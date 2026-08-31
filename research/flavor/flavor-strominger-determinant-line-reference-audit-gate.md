# Strominger determinant-line reference audit: WP1082

## Question

Does the existing Strominger determinant-line packet supply WP1081's volume
reference \(\rho\)?

## Orientation-line result

The cited Strominger packet types its determinant as a section of

\[
(\det V_+)^{\otimes3}\otimes(\det V_-)^{\otimes3},
\]

not as a canonical scalar. Its coordinate transforms by

\[
(\det S_+)^3(\det S_-)^3.
\]

For an allowed chart with

\[
\det S_+=-1,\qquad \det S_-=1,
\]

the character is \(-1\). A coordinate \(D=4\) becomes \(D'=-4\). Nonvanishing
is intrinsic, but sign is not.

## Audit

The packet supplies the determinant-line obstruction. It does not supply:

- an orientation of that determinant line;
- a reduction to an orientation-preserving gauge group;
- WP1081's reference \(\rho\) of phase weight \(-3\);
- \(\rho\)'s transformation law;
- its temporal scope;
- its comparison node with the Krylov history determinant.

## Boundary

This audit does not transport the Strominger determinant line into the Krylov
volume line. It records only that the existing orientation packet is not
\(\rho\).

## Classification

Negative determinant-line audit. The direct Strominger handoff remains the
correct route for either a source-derived coorientation/reference or an exact
no-go.

Checker: `research/flavor/checkers/wp1082_strominger_determinant_line_reference_audit_gate.py`

Result: `results/wp1082_strominger_determinant_line_reference_audit_gate.json`
