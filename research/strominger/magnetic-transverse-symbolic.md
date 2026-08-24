# The transverse response is a one-pivot local Schur complement

At the even chart divisor, the alternate row `3` sees exactly one interior
column:

\[
(a,m)=(g+6,3)_+.
\]

Indeed, an interior plus support is

\[
[g+8-a,2g+9-a].
\]

Reaching row `3`, respecting even pole depth, and excluding the endpoint
`a=g+8` leaves `a=g+6` uniquely.  Minus supports end below row `3`.

This column is penultimate in the source-oriented triangular core.  The final
interior minus column has support

\[
[-2g-8,-g-7],
\]

so it couples neither to the penultimate row `2` nor to the reflected plus
endpoint.  Therefore the full inverse in the endpoint Schur complement
collapses to one scalar pivot:

\[
\tau_g=E-C\frac{B}{A}.
\]

Here `A` is the diagonal coefficient of `(g+6,3)_+`, `C` its row-`3`
coefficient, while `B,E` are the row-`2` and row-`3` coefficients of the
endpoint `(g+8,1)_+`.  The path formula gives

\[
A=-3(g+6)^{\overline g}.
\]

Substitution of the four coefficients and elementary rising-factorial
cancellation yields

\[
\boxed{
\tau_g=
-\frac{8(2g+3)(g^2-g-26)(2g+1)!}
{3(g+5)(g+6)(g+7)(g-1)!}.
}
\]

This includes `tau_2=320/3` and proves directly the previously discovered
grade-two recurrence.  Since every factor other than `g^2-g-26` is positive
and that quadratic has nonsquare discriminant `105`,

\[
\boxed{\tau_g\ne0\quad\text{for every even }g\ge2.}
\]

Thus the alternate chart is nonzero at every even chart divisor, assuming
only the already-proved triangular-core support theorem.  The transverse
response is not a growing determinant invariant: it is a four-coefficient,
one-pivot boundary calculation.
