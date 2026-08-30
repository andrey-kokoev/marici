# Finite grammar identification (WP399)

## Bounded question

Once a finite mediator grammar is independently frozen, can calibrated
contexts identify its response and support a decisive withheld test?

## One-pole response class

Take the normalized one-pole family

\[
r(c)=\frac{a_0+a_1c}{1+b_1c},
\]

with denominators nonzero on the admitted contexts. Cross-multiplication makes
each calibrated record linear in the three unknown coefficients.

For the exact benchmark

\[
r(c)=\frac{1+2c}{1+c},
\]

the records at $c=0,1,2$ are $1$, $3/2$, and $5/3$. Their design matrix is
invertible and uniquely reconstructs

\[
(a_0,a_1,b_1)=(1,2,1).
\]

The frozen grammar then predicts the withheld value

\[
r(3)=\frac74.
\]

Deleting one calibration context leaves rank two and one unresolved parameter
direction.

## Withheld falsifier

The higher-complexity completion

\[
r_{\mathrm{alt}}(c)=r(c)+\epsilon c(c-1)(c-2)
\]

matches every calibration record and shifts the withheld value by
$6\epsilon$. Comparing the predicted and hostile projective response vectors
gives the exact joint determinant

\[
36\epsilon^2.
\]

Thus the withheld context discriminates the frozen one-pole grammar from this
specific enlargement without refitting.

## Authority boundary

The three calibration records identify coefficients inside the declared
family. They do not explain those coefficients or authorize the family. The
mediator count, pole structure, numerator degree, context map, and denominator
support must come from source dynamics fixed before calibration.

An executable experiment must prepare all four contexts in one calibrated
frame and reserve the fourth outcome. If the response class or parallelization
is changed after seeing that outcome, the falsifier is lost.

## Disposition

WP399 supplies the positive finite-test architecture missing after WP398:
source grammar first, enough contexts for exact identification second, and a
withheld response test third. It tests a constructor family but remains
distinct from a numerical source selector.

The next gate is a concrete finite flavor mediator model whose elimination
actually yields a bounded rational response family and whose fourth context
has a physical instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp399_finite_grammar_identification.py` to regenerate
the result.
