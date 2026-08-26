# Three-projector coefficient authority (WP348)

## Source intervention

WP326 fixed the up-sector lift at (Y_u=I+P+2Q+3R). WP348 promotes the
coefficient of (R) to a source input:

\[
Y_u(x)=I+P+2Q+xR.
\]

With the down sector frozen as in WP326, three exact physical invariants are

\[
\operatorname{Tr}H_u=x^2+4x+16,
\]

\[
\det H_u=\frac{25(2x+3)^2}{9},
\]

and

\[
\operatorname{Tr}([H_u,H_d]^3)
=\frac{3647i}{9}(x-10)(4x-5)(12x^2+92x+165).
\]

At the WP326 benchmark (x=3), all three derivatives are nonzero. The CP-odd
response is exactly (-71353555i/9).

## Authority disposition

The coefficient survives to weak-basis-invariant `physical16` readouts. It is
not a gauge, chart, or detector-null input. WP326 therefore proves generic
three-family capability but not a numerical prediction.

The same family also contains CP-conserving points at (x=5/4) and (x=10).
Choosing the benchmark from its observed readout would be target fitting.

## Successor gate

A source selector must derive (x) and the remaining affine coefficients before
flavor readout, with zero physical response to every residual unfixed input.
Only then does an ensemble comparison test a prediction rather than select a
member of the capability family.

Run `uv run --with sympy python
research/flavor/checkers/wp348_three_projector_coefficient_authority.py` to
regenerate the exact intervention audit.
