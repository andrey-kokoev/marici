# RH positive seam graph still needs a faithful evaluation wall

## Result

A positive graph inside the reciprocal double forbids full carrier cancellation for one ordered port, but it does not by itself forbid a scalar endpoint zero.

Let the admissible relation be

\[
y=Hx
\]

with \(H\) positive. For the sum-oriented carrier port,

\[
x+y=(I+H)x.
\]

Since \(-1\) is not in the spectrum of a positive \(H\), full antipodal cancellation is impossible:

\[
(I+H)x=0
\quad\Longrightarrow\quad
x=0.
\]

This remains stable even if \(H\) becomes unbounded, provided it remains a positive self-adjoint relation: the resolvent \((I+H)^{-1}\) is contractive on its range.

## Two independent failures

### Ordered-port failure

For the difference port,

\[
x-y=(I-H)x,
\]

a positive graph may still cancel whenever \(1\) is an eigenvalue of \(H\). Positivity does not choose sum versus difference. The ordered endpoint convention requires source authority.

### Evaluation-wall failure

Even when the full sum vector is nonzero, a scalar covector may annihilate it.

The exact checker takes \(H=I\), \(x=(1,-1)\), and scalar evaluation \(\ell=(1,1)\). Then

\[
x+Hx=(2,-2)\ne0,
\]

but

\[
\ell(x+Hx)=0.
\]

Thus relationship-level noncancellation does not imply scalar-readout noncancellation.

## Required bordered lift

The missing +1 wall is an evaluation constructor that converts a scalar endpoint null into a typed carrier statement. It must prove that, on the admissible source state space,

\[
\ell(x+y)=0
\]

forces either

\[
x+y=0
\]

or a nonzero state in a separately typed defect channel that can be ruled out by source structure.

Because a scalar functional cannot be injective on an unrestricted infinite-dimensional carrier, this lift must use the full boundary equations, not the covector alone. This is precisely the role of a bordered Evans or Schur system.

## Cross-sector synthesis

The current architecture now separates cleanly:

1. reciprocal doubling creates the conserved split carrier;
2. the moving positive seam graph forbids full antipodal sum cancellation;
3. the evaluation wall must lift scalar zero to full carrier cancellation or a typed defect;
4. completion must preserve the graph relation and the bordered lift.

Kitaev's 3+1 pattern has the same typing: three relative carrier directions plus one evaluation, normalization, and return authority. The +1 is not another state coordinate.

## DPC verdict

Candidate: positive seam graph alone proves endpoint nonvanishing.

Verdict: rejected by the scalar evaluation hostile.

Candidate: positive graph plus an assumed faithful scalar covector.

Verdict: impossible on the unrestricted infinite moment carrier.

Surviving candidate: a source-derived bordered evaluation system whose kernel equation upgrades scalar zero into full antipodal carrier cancellation or an independently controlled defect state.

## Finite falsifier

At cutoff \(X\), form the bordered evaluation matrix and compute its kernel under the scalar-zero boundary condition. A nonzero kernel vector with nonzero sum carrier and no declared defect type disproves the lift. Rank success at finite cutoffs must then be strengthened to a uniform completion estimate.
