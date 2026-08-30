# 1681 — Scalar-Cubic Evolution Is Not Autonomous on the Quadratic Moment Grade

## Dynamic positivity falsifier

Entry 1680 establishes positive Cut pushforward for each finite joint moment
cone. Test whether scalar-cubic evolution defines a tangent vector determined
by one such finite cone.

At the first nontrivial grade, take two positive states supported on (p=q).
The first has atoms

\[
q=-2,0,2
\]

with weights

\[
\frac14,\frac12,\frac14.
\]

The second has atoms

\[
q=-1,2
\]

with weights

\[
\frac23,\frac13.
\]

Both induce exactly the same moments through degree two:

\[
\langle q\rangle=\langle p\rangle=0,
\]

\[
\langle q^2\rangle
=\langle qp\rangle
=\langle p^2\rangle
=2.
\]

Their common Hankel matrix on ((1,q,p)) is

\[
\begin{pmatrix}
1&0&0\\
0&2&2\\
0&2&2
\end{pmatrix},
\]

which is positive semidefinite and singular.

But their third moments are

\[
\langle q^3\rangle=0
\quad\text{and}\quad
\langle q^3\rangle=2.
\]

For the scalar-cubic generator

\[
Dq=p,
\qquad
Dp=-q^2,
\]

one has

\[
D(p^2)=-2pq^2.
\]

Because (p=q) on both supports, the same retained quadratic moment therefore
has derivatives

\[
0
\quad\text{and}\quad
-4.
\]

## Narrow result

\[
\boxed{
\text{scalar-cubic evolution is not autonomous on the finite quadratic Hankel cone.}
}

More generally, the cubic generator raises moment degree and requires the next
filtered grade. Positivity of a finite truncation is preserved by Cut merge,
but its nonlinear time derivative is not determined without higher moments.

This is coefficient-tower nonclosure, not a failure of the carrier or of
finite-grade positivity.

## Durable artifacts

- `research/benincasa/checkers/cubic_generator_finite_hankel_nonclosure.rs`
- `research/benincasa/results/cubic-generator-finite-hankel-nonclosure.json`
- `research/benincasa/cubic-generator-finite-hankel-nonclosure.md`

## Next falsifier

Determine whether any finite-dimensional invariant positive family—Gaussian,
finite atomic, or algebraic moment closure—is preserved by the full
free-plus-cubic flow. A surviving family would provide an exact finite process
coefficient object; failure of all source-declared candidates strengthens the
necessity of the infinite filtered moment module.
