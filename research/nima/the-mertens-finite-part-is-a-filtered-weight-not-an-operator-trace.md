# The Mertens finite part is a filtered weight, not an operator trace

## Question

Is the prime-labelled Mertens finite part a functional of the observed operator
\(D=\operatorname{diag}(1/p)\) alone?

## Cutoff dependence

Let \(P_X\) project onto the prime labels \(p\leq X\). The primitive cutoff
current is

\[
W_X(D,P_X)=\operatorname{Tr}(P_XDP_X).
\]

The Mertens finite part subtracts a reference determined by the same prime
cutoff:

\[
\operatorname{FP}_{\mathrm{M}}(D,P)
=\lim_{X\to\infty}
\left(W_X(D,P_X)-\log\log X-B_1\right).
\]

Thus the input is the filtered pair \((D,(P_X)_X)\), not the unfiltered
operator \(D\).

## Naturality theorem

For a unitary transport \(U\), compare two operations.

Transporting only the operator gives

\[
W_X(UDU^*,P_X),
\]

which generally differs from \(W_X(D,P_X)\).

Transporting the entire filtered object gives

\[
W_X(UDU^*,UP_XU^*)=W_X(D,P_X)
\]

by finite trace cyclicity.

Therefore the finite part is natural only for morphisms that carry the cutoff
filtration with the operator. Arbitrary basis transport is not an admitted
symmetry when the prime filtration is frozen.

## Exact finite witness

Take

\[
D=\operatorname{diag}(1/2,1/3,1/5,1/7)
\]

and let \(P\) select the first two labelled coordinates. Then

\[
\operatorname{Tr}(PDP)=\frac56.
\]

Let \(U\) exchange the first and fourth coordinates. If \(D\) moves but \(P\)
does not, the cutoff trace becomes

\[
\frac17+\frac13=\frac{10}{21}.
\]

If both \(D\) and \(P\) move, the value remains \(5/6\).

The full operator spectrum is identical in all cases. The difference is
entirely filtered incidence.

## Categorical consequence

The primitive carrier belongs in a category whose objects contain:

- the observed operator;
- the directed prime-cutoff projections;
- bonding maps between cutoffs;
- the double-logarithmic subtraction scale;
- endpoint and gamma boundary actions.

Morphisms must preserve or explicitly transform all these fields. Forgetting
the filtration before completion erases the authority needed to define the
Mertens finite part.

This also sharpens the Beck--Chevalley gate. The comparison is not between two
functors on bare operator ideals. It is between functors on filtered,
boundary-bearing source objects. The completion 2-cell must be natural with
respect to filtration-preserving transports.

## Hostile

A proposed proof that diagonalizes or unitarily reorganizes the primitive
carrier while retaining the old prime cutoff may preserve the spectrum,
Schatten class, and every unfiltered determinant. It can still change the
Mertens current. Such a proof fails before any RH-strength inference.

## Verdict

The primitive Mertens operation is a source-labelled filtered weight, not a
trace of \(D\) alone. The prime cutoff is part of the state and must cross
theta--Tate completion together with the carrier. The next gate is a common
filtered boundary lift whose completion transports \((D,P_X)\) without
changing the finite-part weight.

