# The reflected physical period column is not in the current marked packet

## Question

Can the period of the reflected component difference \(d_2=r_b(d_1)\) be computed from the existing marked total-energy extension matrix?

## Claim boundary

This is a bounded interface audit of the global reflection and marked-extension packets. It is not a nonexistence theorem for an external period construction.

## Available data

The global surface packet constructs

\[
r_b:[a:b:h:W]\mapsto[a:-b:h:W].
\]

The marked total-energy packet gives one extension matrix at \(E=0\), with source basis

\[
(g_{101},g_{110},g_{111}^{\rm top})
\]

and target coordinates

\[
(e_2,e_4,e_6,v_0).
\]

Its top column is

\[
(0,0,1/(8(x+y)),0)^T.
\]

This identifies the original physical component-difference direction with the \(e_6\) line.

## Missing compatibility

The marked packet contains none of the following:

- an action of \(r_b\) on the three marked source generators;
- an action of \(r_b\) on \((e_2,e_4,e_6,v_0)\);
- an extension matrix at the reflected split fiber;
- an intertwining equation between reflection and the marked extension;
- an integral Betti column for \(r_b(d_1)\).

Substituting \(b\mapsto-b\) into the displayed coefficient matrix does not repair this. The matrix coefficients depend only on \(x,y\), while the marked generators themselves refer to divisor labels whose transport under \(r_b\) is not serialized. Coefficient invariance therefore cannot be promoted to basis invariance.

## Exact first missing object

The first required object is a commutative square

\[
\begin{array}{ccc}
M_{q_+}&\xrightarrow{A_{q_+}}&H_{\rm alg}\\
\downarrow r_b^{M}&&\downarrow r_b^{H}\\
M_{q_-}&\xrightarrow{A_{q_-}}&H_{\rm alg}
\end{array}
\]

with all four bases labelled and

\[
A_{q_-}r_b^{M}=r_b^{H}A_{q_+}.
\]

Applying this square to the source vector representing \(d_1\) produces the requested reflected period column. Its \(v_0\) entry decides whether the reflection orbit plane supplies the second physical response.

## Disposition

The reflected-column test is executable only after the marked reflection square is materialized. Current data construct its geometric vertical map and its original top horizontal column, but not the other three arrows. No coefficient substitution or Weyl invariant determines the missing column.

Verification:

- `research/voevodsky/checkers/check_reflected_marked_period_interface_gate.py`
- `research/voevodsky/results/reflected_marked_period_interface_gate.json`
