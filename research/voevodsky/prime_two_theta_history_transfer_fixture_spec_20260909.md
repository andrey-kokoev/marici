# Prime-two theta-to-history transfer fixture specification

Date: 2026-09-09

## Question

What is the smallest finite source-derived object that can test a proposed local theta-pair-to-Green-history transfer without replacing the history by the Adams scalar coefficient?

## Claim boundary

The first fixture must carry one ordered completed-theta label pair, one nontrivial shell with two labelled endpoints, its reciprocal mate, the radial state, endpoint current, function-valued Wronskian current, wall trace, and a finite jet boundary. Adams doubling supplies only the grade-two arithmetic label and coefficient. This specification does not construct the transfer or identify the fixture with the canonical G4 object.

## Bold conjecture

For prime `p=2`, a source-authorized local transfer can be tested first on the ordered pair `(n,m)=(1,2)` and shell `[a,b]` by requiring a morphism from the completed-theta pair datum

\[
(A,C(t),Y_-,Y_+)
=
(\pi,4\pi e^{2t},e^{2a},e^{2b})
\]

into an Adams-grade-two history object while retaining the functions

\[
\rho(t)=\int_a^b\Phi_1(u)\Phi_2(u+t)\,du,
\]

\[
e(t)=\frac12\left[\Phi_1(b)\Phi_2(b+t)-\Phi_1(a)\Phi_2(a+t)\right],
\]

and

\[
w(t)=\int_a^b\left[\Phi_1'(u)\Phi_2(u+t)-\Phi_1(u)\Phi_2'(u+t)\right]du.
\]

The target incidence must satisfy

\[
D_t\rho=e-\frac12w,
\qquad
\gamma_0\rho=\rho(0).
\]

The arithmetic grade-two coordinate is independently fixed by

\[
w_{2,2}^2=\frac1{16},
\]

with endpoint-relative comparison target

\[
-\frac1\pi w_{2,2}^2=-\frac1{16\pi}.
\]

It is a labelled coordinate of the target, not a replacement for \(\rho,e,w\).

## Named rivals

1. A bare Adams line retaining only \(-1/(16\pi)\).
2. An unordered pair quotient identifying `(1,2)` with `(2,1)`.
3. A scalar Mellin comparison retaining only the completed Euler section.
4. A wall-only model retaining \(\rho(0)\) but deleting \(w(t)\).
5. A model identifying Hermitian adjoint and analytic transpose by notation.

## Risky consequences

A valid fixture and transfer must pass all of the following.

1. **Ordered orientation:** for a symbolic positive separation, the `(1,2)` kernel and `(2,1)` kernel remain distinct; they agree at zero separation.
2. **Two endpoints:** deleting either endpoint changes the endpoint current.
3. **Wronskian coefficient:** symbolic differentiation of the radial state gives exactly \(e-w/2\); replacing \(-1/2\) by zero leaves a nonzero residual.
4. **Wall versus incidence:** \(w(0)=0\) while the generic wall derivative is \(e(0)\), so the Wronskian trace cannot replace the wall coordinate.
5. **Jet boundary:** the fixture retains \(\rho^{(j)}(0),e^{(j)}(0),w^{(j)}(0)\) for a declared cutoff `0 <= j <= J`; equality of only the zeroth scalar is rejected.
6. **Adams noncollapse:** changing any history coordinate while leaving \(-1/(16\pi)\) fixed is detected.
7. **Reciprocal sewing:** the reciprocal copy is labelled separately and its analytic-transpose sign is independently testable.

## Strongest falsification attempt and residual

The bare Adams rival passes the grade support and leading coefficient checks. It fails consequence 6 because infinitely many distinct shell densities share that single coordinate. The unordered-pair rival passes at `t=0` but fails consequence 1 for positive separation because the dilation is attached to the second label. The wall-only rival passes `w(0)=0` but fails consequence 4 whenever

\[
\Phi_1(b)\Phi_2(b)-\Phi_1(a)\Phi_2(a)\ne0.
\]

The first unresolved typed row is the actual target formula for the arithmetic loading and codiagonal. No source currently maps the retained tuple

\[
(\rho,e,w,\rho(0),\text{reciprocal mate},\text{jets})
\]

to the SCC Green carrier.

## Disposition

The finite fixture is source-defined and executable up to symbolic verification of its internal theta-history identities. It can reject scalarization, lost orientation, missing endpoints, the wrong Wronskian coefficient, and truncated jet claims. It cannot certify a theta-to-G4 transfer until the SCC supplies an owner-reviewed arithmetic loading and codiagonal. The next implementation step is an exact symbolic checker for consequences 1–6, with deliberate-failure residuals.

## Sources

- `research/nima/the-correct-completed-theta-pair-shell-density-is-an-explicit-incomplete-gamma-kernel.md`
- `research/nima/the-minimal-diagonal-response-is-a-first-order-radial-history-graph-with-wall-trace-and-wronskian-incidence.md`
- `research/nima/the-adams-two-range-is-a-source-authorized-carrier-for-the-divisible-by-four-diagonal-delay-grades.md`
- `research/nima/distinct-shell-endpoints-make-the-entire-projective-diagonal-source-codiagonally-faithful.md`
- `research/voevodsky/prior_research_additive_multiplicative_crossing_audit_20260908.md`
