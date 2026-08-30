# Primitive atomicity is basis-invariant but not composition-closed

## Result

The local atomicity criterion survives authorized changes of presentation, but it does not ascend through composition.

For the elementary response family

\[
E(a)=I+aN,
\qquad
N^2=0,
\]

the invariant is the determinantal content ideal

\[
\mathfrak c(E)=\operatorname{Fitt}_1(E-I)
             =\gcd\{(E-I)_{ij}\}\,\mathbb Z.
\]

Here \(\mathfrak c(E(a))=|a|\mathbb Z\). For unimodular presentation changes \(P,Q\),

\[
\mathfrak c\bigl(P(E(a)-I)Q\bigr)=|a|\mathbb Z.
\]

Thus “primitive transvection” means \(\mathfrak c(E)=\mathbb Z\), an intrinsic integral statement rather than a preferred-coordinate statement.

The hostile composition is

\[
E(2)=E(1)E(1).
\]

Each factor is primitive, while the effective composite has content ideal \(2\mathbb Z\). Primitive-factor authority therefore cannot be promoted to primitive-composite authority.

## Free-group side

For a tail \(x^n\), the Fox derivative contains \(|n|\) monomials. It is a group-ring unit exactly when \(|n|=1\). Consequently, concatenating two primitive letters produces

\[
\partial_x(x^2)=1+x,
\]

which is not a unit. The integer augmentation shadow is the primitive-row ideal, and that ideal is invariant under tested unimodular Nielsen shadows.

The full source statement should be formulated using the Fox chain rule: a Nielsen change acts through an invertible Fox Jacobian. “This coordinate derivative is a unit” is not invariant language; “the relevant Fox row is unimodular” is.

## Endpoint sector

If \(J\alpha=-\alpha\), then under an integral basis change \(U\),

\[
J'=UJU^{-1},
\qquad
\alpha'=U\alpha
\]

still satisfy \(J'\alpha'=-\alpha'\). The anti-invariant line is therefore equivariant data, not an accidental vector such as \((1,-1)\) in one frame.

## Classification

The square-law stratum now has three intrinsic conditions:

1. the response content ideal is the unit ideal;
2. the tail Fox row is unimodular;
3. the tail class lies in the anti-invariant endpoint eigenspace.

These conditions are invariant under authorized presentation changes. None is automatically inherited merely because every node in a chosen factorization possesses it.

This resolves Deutsch’s hostile question in two parts:

- atomicity is objective under presentation;
- atomicity is local to a constructor slot and is not closed under composition.

A compiler must recompute the effective invariant after every composition. Retaining only certificates attached to the factors permits authority laundering.

## Evidence

The deterministic checker tests:

- 216 left/right unimodular presentations of response content;
- exact factorizations for \(a=\pm1,\pm2,\pm3\);
- the \(E(1)E(1)=E(2)\) laundering hostile;
- Fox support for powers \(\pm1,\pm2,\pm3\);
- unimodular augmentation shadows of Nielsen changes;
- equivariant transport of the endpoint anti-invariant line.

All seven aggregate gates pass.

The bounded computation is evidence for the finite family. The ideal invariance under unimodular multiplication and the nilpotent factorization are exact algebraic identities.
