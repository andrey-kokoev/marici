# Polynomial-stable function classes cannot fix the common divisor

## The residual gauge

Let two nonzero chart sections \(D_+\) and \(D_-\) have fixed transition

\[
\tau=D_+/D_-.
\]

For any entire common factor \(h\), the pair \((hD_+,hD_-)\) has the same transition wherever the quotient is defined. The transition therefore determines a line bundle and a projective section, not its common divisor.

## Exact polynomial hostile

Choose distinct points \(a\) and \(z_0\), and define

\[
p_{a,z_0}(z)=\frac{z-a}{z_0-a}.
\]

Then \(p_{a,z_0}\) is entire, has the normalization \(p_{a,z_0}(z_0)=1\), and inserts a common zero at \(a\). Multiplication by this factor preserves:

- the chart transition;
- any prescribed value at \(z_0\);
- finite order;
- exponential type;
- Cartwright-class membership when the original sections satisfy the usual logarithmic-integrability condition.

The last three statements follow because multiplication by a polynomial changes logarithmic growth only by \(O(\log |z|)\). It does not change the exponential indicator or exponential type.

## No-go theorem

Any proposed admissible section class that is closed under multiplication by normalized nonconstant polynomials cannot determine the common divisor from transition data and point normalization.

Consequently, naming a broad class such as finite-order entire, exponential type, or Cartwright is not yet a determinant normalization theorem. Each admits finite divisor gauge unless an additional source law removes it.

## What would close the gauge

At least one non-polynomial-stable datum is required. Viable forms include:

1. a source-defined Fredholm or relative determinant with a fixed regularization prescription;
2. a complete asymptotic expansion whose constant and inverse-power terms are fixed strongly enough to detect polynomial degree;
3. a canonical outer factor together with source-fixed inner and singular factors;
4. a universal property that selects one section rather than only its line;
5. a global boundedness condition strong enough to make every admissible common factor constant.

The requirement is not merely growth control. It is a source-derived gauge fixing that is not stable under insertion of a finite divisor.

## Combined gate

The earlier axial hostile and the polynomial hostile are complementary:

- axial normalization without a tight growth class admits \(1+\varepsilon e^{z^2}\);
- standard growth classes plus point normalization admit \(p_{a,z_0}\).

A successful theorem must control their intersection. It must prove, from the completed theta/Tate construction, that every admissible normalized common factor is constant or at least zero-free.

