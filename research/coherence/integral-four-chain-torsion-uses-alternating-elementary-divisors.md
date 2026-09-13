# Integral four-chain torsion uses alternating elementary divisors

## Four-point chain

For integer gaps \(x,y,z\), the upper entries of the chain skew matrix are

\[
x,xy,xyz,y,yz,z.
\]

Its first alternating elementary divisor is

\[
d_1=\gcd(x,y,z).
\]

The full Pfaffian is

\[
\operatorname{Pf}M=xz.
\]

Hence the second alternating elementary divisor is

\[
d_2=\frac{|xz|}{d_1}.
\]

Since \(d_1\) divides both \(x\) and \(z\), one has \(d_1\mid d_2\), as required by alternating Smith normal form.

Thus the integral normal form is

\[
H(d_1)\oplus H(d_2),
\]

not generally the prescribed adjacent form

\[
H(x)\oplus H(z).
\]

## Example

For gaps \((2,3,4)\),

\[
(d_1,d_2)=(1,8),
\]

while the adjacent block weights are \((2,4)\). Both products equal the Pfaffian \(8\), but their framed block decompositions differ.

The middle gap \(y\), although absent from the scalar Pfaffian, can redistribute integral prime factors through the gcd of all matrix entries.

## Arithmetic residual

Over \(\mathbb Z\), the cokernel of the skew map is controlled by

\[
(\mathbb Z/d_1)^2\oplus(\mathbb Z/d_2)^2.
\]

This integral torsion module retains more structure than the scalar Pfaffian product \(d_1d_2=|xz|\).

After localizing the selected gaps, the framed adjacent decomposition becomes available, but it is not the integral Smith decomposition. These are different normal forms answering different questions:

```text
integral Smith form:
  classifies the abelian cokernel

localized adjacent form:
  preserves ordered pair framing

Pfaffian scalar:
  records only the product of block weights
```

## Consequence

A coefficient-portable rank-reset target should retain an integral torsion module before localization, not only a determinant scalar. Localization may then map that module to the framed adjacent hyperbolic certificate.

This adds an arithmetic layer to the residual type whenever gap weights are nonunits.

## Verification

```text
python research/coherence/check_integral_four_chain_alternating_invariants.py
```

The checker computes exact invariants for five integral four-point chains.

Artifacts:

- `check_integral_four_chain_alternating_invariants.py`
- `integral-four-chain-alternating-invariants.v1.json`
