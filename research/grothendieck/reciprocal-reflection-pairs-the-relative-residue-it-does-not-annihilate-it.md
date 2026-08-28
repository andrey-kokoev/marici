# Reciprocal reflection pairs the relative residue; it does not annihilate it

## Reflection action

For the ordered two-atom current

\[
J(w)=ab(w-w^{-1}),
\]

reciprocal reflection acts by the sign character:

\[
J(w^{-1})=-J(w).
\]

Thus the transverse cokernel port is not an ordinary scalar invariant. It is
an anti-invariant section over the reciprocal orbit.

## Hostile reciprocal orbit

The scalar source

\[
X(w)=a+bw
\]

has its zero at `w_+=-a/b`. Its reflected copy has zero at
`w_-=w_+^{-1}=-b/a`. Reciprocal completion can retain the full pair.

At those two zeros,

\[
J(w_+)=b^2-a^2,
\qquad
J(w_-)=a^2-b^2.
\]

Therefore

\[
J(w_+)+J(w_-)=0
\]

even when both residues are nonzero and both zeros lie off the unit seam.

## Consequence for the proposed boundary law

A completed scalar boundary current obtained by summing over the reciprocal
orbit vanishes identically. Such vanishing cannot imply RH: it is the
codiagonal pushforward of an anti-invariant pair.

This is another instance of the durable fiber rule. The quotient orbit has
zero total current, but its fiber contains two nonzero, oppositely oriented
elements. Finite-to-one is not one-to-one.

The correct completed object must retain the coefficient system carrying the
sign representation of reciprocal reflection. In elementary terms, it must
retain the ordered pair

\[
\bigl(J(w),J(w^{-1})\bigr)

\]

or its equivalent relative generator, not only their sum.

## Holomorphic reciprocal fixed points

For holomorphic inversion alone, a fixed point obeys `w=w^{-1}`, so `w=±1`,
and anti-invariance forces

\[
J(w)=-J(w)=0.
\]

Away from those two algebraic branch points, holomorphic inversion transports
a nonzero current to its negative on the other orbit point.

This must not be identified with the full RH seam. The seam `|w|=1` is fixed
by the anti-holomorphic involution `w -> 1/conjugate(w)`. Under that involution
the current obeys `J -> -conjugate(J)`, so a seam value is constrained to be
purely imaginary, not zero. Ledger 3606 records this typing correction.

## Revised RH gate

The prior target

\[
X(z)=0\Longrightarrow J_{\rm total}(z)=0
\]

is too weak if `J_total` means the scalar orbit sum. Reciprocal symmetry makes
that statement true for hostile off-seam pairs.

The required theorem must instead control the anti-invariant fiber before
scalar orbit summation. Holomorphic reciprocity alone cannot do so, and the
anti-holomorphic seam only selects a quadrature rather than annihilating the
fiber.

That is a source-selection theorem, not a consequence of reflection alone.
Its smallest falsifier is the reciprocal completion of the imbalanced
two-atom source.
