# The Second Burnside Mark Is Odd-Sector Acyclicity

## Permutation module of a reciprocal packet

Let \(X\) be a finite reciprocal zero packet and let \(V_X\) be its complex
permutation module. Reciprocal reflection acts by an involution \(J\).

The total and fixed Burnside marks become

\[
m_{\rm total}(X)=\dim V_X,
\qquad
m_{\rm fixed}(X)=\operatorname{tr}(J|V_X).
\]

A fixed orbit contributes a one-dimensional even representation. A free
two-point orbit decomposes as one even line and one odd line.

## Exact deficit identity

Writing

\[
V_X=V_X^+\oplus V_X^-,
\]

gives

\[
\dim V_X-\operatorname{tr}(J|V_X)=2\dim V_X^-.
\]

Therefore the reciprocal packet contains no free orbit exactly when its odd
part vanishes.

This converts the missing fixed-point mark into a concrete operator target:
construct the source-derived zero module and prove that its sign-isotypic
component is zero.

## Complex formulation

Suppose a source-derived \(C_2\)-equivariant Fredholm or Koszul complex
\(K^\bullet\) has cohomology equal to the completed zero module, with
multiplicity. Then the desired theorem is not acyclicity of the entire
complex. It is

\[
H^\bullet(K^-) = 0,
\]

where \(K^-\) is the odd character projection.

The even cohomology may remain: it represents seam zeros. Free reciprocal
orbits necessarily contribute odd cohomology and are excluded.

## Why this is sharper than the earlier puncture programme

The earlier contraction target attempted to eliminate all off-seam
cohomology by constructing separate half-plane contractions. The Burnside
decomposition shows that the minimal requirement is only a contraction of
the odd reciprocal sector:

\[
d h^-+h^-d=1_{K^-}.
\]

This contraction must be constructed from labelled theta/Tate operations
before scalar divisor extraction. Constructing \(K\) backward from the zeros
would be circular.

## Finite falsifier

For a two-point free orbit, the permutation matrix of \(J\) has trace zero,
while the module has dimension two. Its odd projector has rank one. Any
claimed source contraction must fail on that odd line if the hostile orbit is
admitted.

For two fixed points, \(J\) is the identity, trace and dimension both equal
two, and the odd projector has rank zero.

## Source theorem now required

The route survives only if the programme can construct:

1. a source-derived equivariant complex whose cohomology carries the zero
   packet with correct multiplicity;
2. a continuous contracting homotopy on its odd component through restricted
   product completion;
3. an index or trace theorem identifying the cohomological character with the
   reciprocal divisor action.

The first and third steps are the zero-to-state bridge. The second is the
fixed-point-sensitive law. Together they would compute the second Burnside
mark without locating zeros.

