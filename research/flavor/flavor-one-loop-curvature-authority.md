# One-loop curvature authority (WP267)

## Candidate radiative repair

Let a source mode have invariant-dependent squared mass

\[
m^2(x)=M^2+kx
\]

and contribute the one-loop term

\[
V_1(x)=A,m^4(x)
\left(\log\frac{m^2(x)}{\mu^2}-c\right).
\]

At \(x=0\), its exact curvature is

\[
V_1''(0)=Ak^2
\left(2\log\frac{M^2}{\mu^2}-2c+3\right).
\]

Thus a loop determinant can produce positive curvature, unlike the stable
linear-source envelopes closed by WP266. But the isolated loop contribution
does not have a presentation-independent sign.

## Hostile matching scales

For the exact subtraction packet \(c=3/2\), the curvature becomes

\[
V_1''(0)=2Ak^2\log\frac{M^2}{\mu^2}.
\]

The same field-content grammar gives positive, zero, and negative curvature
when the logarithm is respectively \(1\), \(0\), and \(-1\). Choosing the
matching scale to make the curvature positive is not a source prediction.

A local counterterm \(c_2x^2\) contributes curvature \(2c_2\). Only the total
renormalized coefficient, with a boundary condition and scheme transport, can
carry physical authority. Fixing that boundary from the observed mixing point
would merely relocate the fit.

## Classification

Radiative matching reopens the sign obstruction mathematically but does not by
itself close coefficient authority. A complete UV packet must derive the field
content, statistics, thresholds, renormalized counterterm boundary, and scheme
transport before flavor readout. This result does not deny that such a theory
could predict the coefficient; it denies authority to the isolated loop term
or scale choice.

Run `uv run --with sympy python
research/flavor/checkers/wp267_one_loop_curvature_authority.py` for the exact
curvature, hostile scale packets, counterterm dependence, and loop-only
selector failure.
