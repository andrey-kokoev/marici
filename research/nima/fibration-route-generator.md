# Input/output route defects: flat regrouping versus additional transport

## Prior-work scope correction

The flat-regrouping theorem below concerns row-based observations only. Existing
`whole-package-generators.md`, `observer-higher-groupoid-fragment.md` and
`native-table-equivalence.md` already supply retained histories, witnessed comparisons,
higher comparisons and next-source reification. They must not be replaced by the row
projection or described as absent because that projection has zero defect.
The polynomial transport below is an illustration, not the first available
comparison structure. Investigation of physical generating functions must resume
from the existing complete native comparison packages.

## Question

The operator asks whether a generating function can be a derivative of the
difference between input-then-output and output-then-input fibration routes.
The second phrase is interpreted as the reversed composition order, not physical
time. SCC obligation: route/coherencer compatibility, followed by readout descent.

The candidate is a mixed derivative of an operator-composition defect. It is not
the difference of ordinary mixed partials of an already defined scalar function.

## Actual bare fibration test

For a table with rows R and endpoint maps s:R->S and t:R->T, the two fibers at
fixed endpoints are

\[
\sum_{(r,p)\,\in\,\operatorname{fib}_s(a)}(t(r)=b),
\qquad
\sum_{(r,q)\,\in\,\operatorname{fib}_t(b)}(s(r)=a).
\]

The map `((r,p),q) -> ((r,q),p)` is an isomorphism. It retains the row and both
endpoint witnesses. `agda/FibrationRouteInterchange.agda` constructs it using the
actual `TableFibrationCycle.fibrate`, proves both inverse laws, and proves that
every row-based readout commutes with it. No finite census is needed.

Thus regrouping the same table in these two orders supplies no nonzero scalar
route defect to differentiate. This does not identify separately retained
operation histories or rule out a history-sensitive observer. Such an observer
would require extra data beyond a function on rows.

## Nontrivial transport candidate

To test the proposed mechanism rather than merely stop at regrouping, declare the
polynomial fibration `(x,y,r) -> (x,y)` with two lifts:

\[
I_a(x,y,r)=(x+a,y,r),\qquad
O_b(x,y,r)=(x,y+b,r+bV(x)).
\]

Here r is a scalar fiber coordinate. It is not declared to be physical action or
phase. The two composed routes have the same base endpoint `(x+a,y+b)`, so their
vertical values can be compared without an untyped subtraction:

\[
\Delta_{a,b}r=(O_b I_a-I_a O_b)_r
=b\bigl(V(x+a)-V(x)\bigr).
\]

The notation on the left subtracts only the displayed scalar coordinates, not
points or arbitrary fibration morphisms. The closed rectangle also returns the
base to `(x,y)` with this same vertical displacement.

The mixed infinitesimal defect is

\[
\mathcal C(x)=\left.\partial_a\partial_b\Delta_{a,b}r\right|_{a=b=0}
=V'(x).
\]

The horizontal lifts are `partial_x` and `partial_y+V(x)partial_r`; their bracket
is `V'(x)partial_r`. We use the vertical-bracket sign convention for the curvature
coefficient in this abelian presentation. The potential is a primitive of that coefficient in the chosen
frame, not the derivative of the route defect itself:

\[
V(x)=V(x_0)+\int_{x_0}^{x}\mathcal C(u)\,du.
\]

For the quartic potential `V(x)=lambda*x^4/24`,

\[
\mathcal C(x)=\lambda x^3/6,\qquad
\partial_x^3\mathcal C=\lambda.
\]

This is a potential example; the scalar Lagrangian's interaction term is `-V`.
The calculation supplies neither a path integral `Z[J]` nor its logarithm. Calling
this coefficient a physical action or a generating functional requires a further
source/readout identification.

## Falsification and disposition

Conjecture: nonzero input/output route mismatch can supply the missing scalar
interaction data. Rivals are flat regrouping, independently supplied curved
transport, and a scalar whose ordinary mixed partials commute.

Risky test: compute the actual fiber interchange before assigning weights, and
then compute the first route derivative for independently declared lifts.

Results:

- Actual endpoint regrouping is row-readout-flat, by fresh safe/cubical proof.
- The additional polynomial transport has the displayed nonzero defect, checked
  symbolically for a general degree-at-most-four V.
- Ordinary mixed partials of the same scalar commute; substituting their difference
  for the composition defect gives zero.
- The defect cannot recover the constant term of V.
- Couplings 3/5 and 6/5 still give distinct admissible toy connections. Choosing
  `O_b` using an already desired V would merely move the supplied interaction into
  the transport definition.

The proposed mechanism is therefore correctly typed as **route defect -> response/
curvature -> potential reconstruction**, subject to a specified frame and base
value. It is not yet a derivation of physical weights. The first missing source
object is a justified input/output transport on the actual retained fibration;
no further abstract selection criterion is substituted for that missing object.

## Evidence

Through structured-command:

```text
pwsh -NoProfile -File research/nima/checkers/check_fibration_route_interchange.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_fibration_route_generator.py
uv run --with sympy python research/aspect/scc/scc.py check nima-fibration-route-generator
```

Receipts: `results/agda-FibrationRouteInterchange.json` and
`results/fibration-route-generator.json`. The checker verifies fresh formal source
hashes as well as the symbolic hostiles. The toy connection is not an Agda model
of additional physical transport. New files and evidence remain uncommitted;
no existing source was edited, no computation is active, and no physical
interpretation, independent review, commit or push is claimed.
The stimulus/report event `ev-000000015607-b812af03-db60-4ca4-818a-40c522f13f2f`
at sequence 15607 is admitted but uncommitted. Earlier arithmetic/action reports
15601, 15604 and 15605 retain their separately recorded uncommitted state.
