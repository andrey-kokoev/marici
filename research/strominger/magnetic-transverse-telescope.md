# The transverse quadratic is transported, not repeatedly regenerated

The proposed even-grade recurrence for the alternate-chart response contains
the quotient

\[
\frac{g^2-g-26}{g^2-5g-20}.
\]

Set

\[
Q(g)=g^2-g-26.
\]

Then the denominator is exactly

\[
g^2-5g-20=Q(g-2).
\]

Consequently the recurrence character splits as

\[
\frac{\tau_g}{\tau_{g-2}}
=P(g)\frac{Q(g)}{Q(g-2)},
\]

where

\[
P(g)=
\frac{4g(g+3)(g+4)(2g+1)(2g+3)}
{(g-2)(g+6)(g+7)}
>0
\]

for every even `g>=4`.  Iteration telescopes:

\[
\boxed{
\tau_g
=\tau_2
\left(\prod_{h=4,6,\ldots,g}P(h)\right)
\frac{Q(g)}{Q(2)}.
}
\]

Thus the discriminant-105 factors do not describe a fresh possible
singularity at every grade.  They are one boundary state transported from
`g-2` to `g`; all internal copies cancel in the determinant character.

Since `Q(2)=-24`, `Q(4)=-14`, and `Q(g)>0` for every even `g>=6`, the formula
immediately explains the observed sign law:

\[
\tau_2,\tau_4>0,
\qquad
\tau_g<0\quad(g\ge6\text{ even}).
\]

It also reduces nonvanishing to the endpoint statement `Q(g) != 0` on the
even lattice.  This packet remains conditional on the symbolic derivation of
the recurrence itself.  Its advance is explanatory: the exceptional
quadratic is a transported boundary character, not an unexplained arithmetic
factor in a fitted product.

The positive product also closes explicitly.  With `g=2n`, elementary
cancellation of the even and odd strings gives

\[
\boxed{
\tau_{2n}
=-
\frac{32}{3}
\frac{n,4^{n-1}(4n+3)!!}{(n+3)(2n+5)(2n+7)}
\bigl(4n^2-2n-26\bigr).
}
\]

This formula includes the base case `n=1` and reproduces the proposed
recurrence by direct division.  The outstanding Schur calculation may now
target this single closed expression instead of discovering a recurrence and
then solving it.
