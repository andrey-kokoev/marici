# The completed puncture module has faithful triangular jet transport

## Theorem

Let `x'=-1/x`.  Since

\[
 \partial_{x'}=x^2\partial_x,
\]

the order-`r` source derivative in the primed chart is

\[
 \boxed{
 (x^2\partial_x)^r
 =\sum_{j=1}^{r}L(r,j)x^{r+j}\partial_x^j,
 \qquad
 L(r,j)=\frac{r!}{j!}\binom{r-1}{j-1}.}
\]

Here `L(r,j)` are the unsigned Lah numbers.  Order zero is the identity.  The
antiholomorphic jet has the conjugate formula, so a mixed source jet transforms
by the tensor product of the two triangular matrices.

For jet bound `J`, order multiindices by total order and then lexicographically.
The transition matrix is triangular with diagonal

\[
 x^{2r}\bar x^{2s}
\]

on the `(r,s)` coordinate.  Its determinant is nonzero for every finite `J`
on the overlap `x!=0,infinity`.  Consequently

\[
 \mathcal H^J_P\simeq\mathcal H^J_{p(P)}
\]

and these isomorphisms commute with the strict inclusions
`H^J -> H^(J+1)`.  They therefore induce an automorphism of the strict LF
union `H^fin`.

## Interpretation

The off-diagonal Lah coefficients are coordinate mixing, not information
loss.  A highest-order jet always has a nonzero highest-order image, and the
lower terms merely change the local presentation.  In system language, chart
inversion is a lossless schema migration whose migration matrix is triangular.

There are three distinct operations:

1. spin-two observation-chart gluing, already exact on `Khat`;
2. triangular source-jet coordinate transport;
3. helicity conjugation, exchanging the two spin components.

All three are invertible.  Therefore none can create a tower, `E_1`, `E_2`,
or any other kernel class.  Such a class can first appear only after a
noninvertible physical readout or quotient.

## Chart boundary

The determinant vanishes if the formula is naively evaluated at `x=0`, but
that is not rank loss of the global module: `x=0` is outside the overlap and
is represented by `x'=infinity`.  The correct statement is atlas-level
faithfulness, not invertibility of one chart matrix at its own boundary.

## Evidence

`checkers/completed_two_chart_parity_module_checks.py` derives the Lah formula,
checks mixed-jet triangularity and finite-stage determinants, verifies
involutivity through the inverse chart operator, and distinguishes overlap
rank from chart-boundary coordinate failure.
