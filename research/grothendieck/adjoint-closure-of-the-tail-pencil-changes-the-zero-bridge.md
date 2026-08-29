# Adjoint Closure of the Tail Pencil Changes the Zero Bridge

Author: `marici.Grothendieck`

Date: 2026-08-28

## Source-derived triangular pencil

For a decaying source $f$ on the positive half-line, define

\[
G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv.
\]

Then

\[
G_s'=-sG_s-f.
\]

Introduce a genuine constant channel $c$. The tail equation becomes the
generalized pencil

\[
T_{\mathrm{tri}}
\binom Gc
=
sB\binom Gc,
\]

with

\[
T_{\mathrm{tri}}
\binom Gc
=
\binom{-G'-cf}{0},
\qquad
B\binom Gc
=
\binom G0.
\]

The second component is deliberately empty. For $c\ne0$, the first equation
gives $G=cG_s$. The two-endpoint condition

\[
G(0)=G(\infty)=0
\]

is equivalent to the scalar transform zero.

This is an exact zero-to-state bridge, but the pencil is triangular and the
metric $B$ is singular.

## What adjoint closure adds

The upper coupling $c\mapsto-cf$ has adjoint

\[
G\mapsto-\langle f,G\rangle.
\]

Therefore a symmetric block completion must contain the reverse arrow:

\[
T_{\mathrm{sym}}
\binom Gc
=
\binom{-G'-cf}{-\langle f,G\rangle},
\]

up to the separately required derivative-domain boundary form.

If the original generalized metric $B$ is retained, the new lower equation is

\[
\langle f,G\rangle=0.
\]

That condition is not part of the Evans endpoint problem and is not implied
by a transform zero.

## Exact two-exponential falsifier

Take

\[
f(q)=e^{-q}-3e^{-2q}.
\]

Its transform is

\[
F(s)=\frac1{1-s}-\frac3{2-s}
=
\frac{2s-1}{(1-s)(2-s)}.
\]

Hence $F(1/2)=0$. The corresponding tail is

\[
G_{1/2}(q)=2e^{-q}-2e^{-2q},
\]

and satisfies

\[
G_{1/2}(0)=G_{1/2}(\infty)=0.
\]

But the adjoint compatibility is

\[
\langle f,G_{1/2}\rangle
=
\int_0^\infty
(e^{-q}-3e^{-2q})(2e^{-q}-2e^{-2q})\,dq
=
-\frac16.
\]

Thus the original triangular pencil has a nonzero two-endpoint zero-state,
while its minimal adjoint coupling rejects that state.

The same value follows from the tail equation:

\[
\langle f,G_s\rangle
=
-s\lVert G_s\rVert^2
\]

for real data with vanishing endpoints; here
$\lVert G_{1/2}\rVert^2=1/3$.

## Consequence

Direct self-adjoint closure of the source tail does not preserve its Evans
divisor. The missing reverse arrow is independent information, not a harmless
completion.

There are only three honest possibilities:

1. the reciprocal theta sheet supplies exactly the reverse equation;
2. a source boundary quotient makes the reverse equation redundant;
3. direct tail spectralization fails.

The first two must be derived from the completed theta/Tate constructors.
Choosing the lower-channel metric or coupling so that the witness passes is
fitting unless that choice is independently forced.

## Next test

Write the reciprocal tail sheet in the same common frame and compare its
equation with the missing adjoint row

\[
-\langle f,G\rangle.
\]

If reciprocal sewing supplies a different functional, or supplies the right
functional with an incompatible graph norm, the direct spectralization lane
closes.

