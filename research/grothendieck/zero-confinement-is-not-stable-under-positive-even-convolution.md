# Zero confinement is not stable under positive even convolution

## Exact convolution packet

Let

\[
\nu=\frac25\delta_{-1}+\delta_0+\frac25\delta_1.
\]

This is a positive even measure. Its bilateral Laplace transform is

\[
L_\nu(z)=1+\frac45\cosh z.
\]

At

\[
z=\pm\log 2+(2k+1)\pi i,
\]

one has `cosh(z)=-5/4`, so `L_nu(z)=0`. The packet itself already has an
exact reciprocal quartet of off-seam zeros.

## Monoidal obstruction

Let `mu` be any nonzero positive even measure for which the bilateral Laplace
transform exists. Convolution preserves positivity and evenness, while

\[
L_{\mu*\nu}(z)=L_\mu(z)L_\nu(z).
\]

Therefore convolution with `nu` inserts the displayed off-seam divisor into
the transform of `mu`. If `mu` has a positive even smooth or Schwartz density,
then `mu*nu` has the same regularity because it is a positive finite sum of
translates.

Hence zero confinement is not a monoidal property of positive even sources.
No source category closed under arbitrary positive even convolution can force
all transform zeros onto the seam.

## Constructor meaning

This identifies a source-authority requirement rather than another scalar
inequality. The theta constructor repertoire must reject `nu` as an
unauthorized factor before scalar aggregation. Equivalently, a successful
connected or logarithmic extraction must expose its added primitive divisor.

The forbidden shortcut is:

```text
positive source
+ reciprocal symmetry
+ convolution closure
implies zero confinement
```

The third premise makes the conclusion impossible. Positivity and reciprocal
symmetry may remain, but the admissible source transformations must carry
arithmetic provenance restrictive enough not to admit arbitrary positive
convolution factors.

This does not prove or disprove RH. It gives an exact hostile constructor that
every proposed source category must reject.

## Durable verification

- Checker: `checkers/check_positive_even_convolution_divisor_hostile.py`
- The checker verifies the exact quadratic roots, reciprocal pairing,
  off-seam modulus, and factor cancellation.
