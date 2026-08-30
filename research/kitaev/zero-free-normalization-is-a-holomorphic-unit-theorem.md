# Zero-Free Normalization Is a Holomorphic Unit Theorem

Suppose a completed scalar Tate section \(Z(s)\) is related to a typed
Fredholm determinant \(D(s)\) by

\[
Z(s)=u(s)D(s)
\]

on a connected domain \(\Omega\). Equality of zero divisors is transported
only after proving that \(u\) is a unit of \(\mathcal O(\Omega)\):

\[
u\in\mathcal O(\Omega),
\qquad
u^{-1}\in\mathcal O(\Omega).
\]

Then \(u\) has no zeros, so \(Z\) and \(D\) have exactly the same zeros with
the same multiplicities. This is a theorem about the normalization channel,
not a gauge convention.

On a simply connected domain, the unit condition is equivalent to

\[
u=e^h
\]

for some holomorphic \(h\). On a non-simply-connected domain, a zero-free unit
need not possess a single-valued holomorphic logarithm; winding is an
additional torsor datum. Zero-freeness itself remains the required property.

## Base normalization is insufficient

The condition \(u(s_0)=1\) fixes a scalar frame only at \(s_0\). For example,

\[
u(s)=1+s
\]

satisfies \(u(0)=1\) but vanishes at \(-1\). A canonical vacuum value cannot
transport a zero divisor without a global unit theorem.

Functional-equation symmetry does not repair this. The factor

\[
u(s)=16(s-1/4)(3/4-s)
\]

obeys \(u(1-s)=u(s)\) and \(u(1/2)=1\), yet inserts symmetric zeros at
\(1/4\) and \(3/4\). Thus symmetry plus central normalization still permits
hostile off-seam zero pairs.

## Equality up to a unit still forgets operator data

Even a proved unit identifies only the determinant zero divisor. It does not
recover the kernel vector, sheet character, seam action, inverse norm, or
operator-valued lift. Those remain in the operator channel established in the
preceding determinant theorem.

## Minimal source proof obligations

For theta/Tate scalarization, Grothendieck must derive:

1. the ratio \(u=Z/D\) on a nonempty region where \(D\ne0\);
2. holomorphic extension of \(u\) across determinant zeros;
3. holomorphic extension of \(u^{-1}\), or an equivalent nonvanishing theorem;
4. compatibility with the frozen Fourier–Tate normalization and sheet
   transport.

Matching at one point or matching functional equations supplies neither the
second nor third item.

## Falsifiers

- The normalization is checked only at a vacuum/base point.
- Functional-equation symmetry is treated as zero-freeness.
- A meromorphic ratio is silently promoted to a holomorphic unit.
- Zeros of the ratio are canceled against determinant poles without typed
  divisor accounting.
- Equality of scalar zero divisors is used to identify operator kernels.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to type the phrase “up to zero-free normalization.”

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The missing arrow is now exactly a unit theorem, and base-value plus
functional-symmetry hostiles show why canonical normalization alone is
insufficient.
