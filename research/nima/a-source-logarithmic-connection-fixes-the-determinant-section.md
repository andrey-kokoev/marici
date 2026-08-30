# A source logarithmic connection fixes the determinant section

## Upgrade from transition authority

A two-chart transition determines how local representatives compare. It does not determine their common divisor. The missing datum is a connection on the determinant line.

For a nonzero meromorphic section \(\Delta\), its logarithmic connection form is

\[
J_\Delta(z)\,dz=d\log\Delta(z).
\]

In a relative-determinant construction this form is derived from a resolvent trace. In the unregularized trace-class case the model law is

\[
\frac{d}{dz}\log\Delta(z)
=-operatorname{Tr}\left((A-z)^{-1}-(A_0-z)^{-1}\right).
\]

For a Schatten-three construction, the right side must include the exact first- and second-order counterterm currents associated with the regularization. The primitive, square, and connected-tail grades are therefore not optional corrections to a scalar determinant. Together they are coordinates of its connection law.

## Uniqueness theorem

Let \(\Delta_1\) and \(\Delta_2\) be nonzero meromorphic sections on a connected domain. Assume their logarithmic derivatives agree as meromorphic one-forms:

\[
d\log\Delta_1=d\log\Delta_2.
\]

Then their quotient \(h=\Delta_1/\Delta_2\) satisfies

\[
d\log h=0.
\]

The quotient is therefore a nonzero constant. One source-fixed base value determines that constant. Unlike transition data, the logarithmic connection detects every nonconstant common factor, including normalized polynomials and axial factors.

Equality as meromorphic forms also forces equality of divisors: the residue at a point is the zero or pole multiplicity. A purported common zero insertion changes the residue and is rejected locally.

## Existence is a separate gate

An arbitrary proposed current \(J(z)\,dz\) does not automatically integrate to a global determinant section. Source-derived existence requires:

1. meromorphicity on the declared chart domain;
2. integral residues at every singularity;
3. periods in \(2\pi i\mathbb Z\), so exponentiated path integrals are single-valued;
4. the declared reciprocal transition law on chart overlaps;
5. a source basepoint and normalization;
6. convergence and cutoff compatibility of the regularized trace current.

These gates prevent reconstructing a desired section backward from its scalar values. The current, its residue data, and its periods must arise from the labelled operator family before comparison with \(\Xi\).

## Schatten-three interpretation

The earlier three-grade filtration now has a precise possible role:

- grades \(k\ge3\) form the convergent logarithm of a third-order regularized determinant;
- grade \(k=1\) is the primitive trace anomaly coordinate;
- grade \(k=2\) is the square trace anomaly coordinate.

Discarding the first two grades leaves a well-defined regularized scalar but loses the full connection law needed to compare finite Euler cutoffs. Retaining them as typed boundary currents can restore section authority without pretending that they are trace-class bulk terms.

## Decisive source test

At each finite cutoff, derive the operator family and compute both sides of the regularized logarithmic derivative identity. Record the typed residual

\[
R_X(z)=d\log\Delta_X(z)-J_X^{\mathrm{tail}}(z)-J_X^{\mathrm{primitive}}(z)-J_X^{\mathrm{square}}(z)-J_X^{\infty}(z).
\]

The route survives only if \(R_X\) vanishes before scalar completion, the currents compose under cutoff inclusion, and their completed periods remain integral. One nonzero source-typed residual, nonintegral residue, or cutoff-dependent normalization falsifies the proposed determinant constructor.

## Scope

This theorem fixes which determinant section the source constructs. It does not prove that its zeros lie on the critical seam. Its gain is narrower and essential: once the connection law is established, hostile common factors can no longer change the divisor without changing a source-observable current.

