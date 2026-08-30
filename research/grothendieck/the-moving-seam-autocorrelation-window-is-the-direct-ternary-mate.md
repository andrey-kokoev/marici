# The Moving-Seam Autocorrelation Window Is the Direct Ternary Mate

## Source-defined three-way cell

For the completed positive theta source \(\Phi\), define the moving-seam
autocorrelation window

\[
W_L(d)=2\int_0^L\Phi(q)\Phi(q+d)\,dq
\]

and its odd spectral transform

\[
\mathcal K_L(z)=\int_0^\infty W_L(d)\sinh(zd)\,dd.
\]

This object is constructed before selecting a zero or inspecting the Green
residual. It retains three native inputs simultaneously:

1. moving boundary position \(L\);
2. ordered source separation \(d\), hence the two source points;
3. centered spectral character \(z\).

It is therefore a direct ternary incidence rather than an iterated scalar
primitive.

## Exact boundary identity

Differentiating only the moving boundary gives

\[
\partial_LW_L(d)=2\Phi(L)\Phi(L+d).
\]

If the reciprocal half-tail difference is

\[
H_+(L,z)-H_-(L,z)
=2\int_0^\infty\Phi(L+d)\sinh(zd)\,dd,
\]

then

\[
\partial_L\mathcal K_L(z)
=\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr).
\]

The right side is exactly the local relative forcing response in the doubled
Green identity, with orientation fixed by the declared order of the reciprocal
tails.

Thus the moving-seam window supplies the direct ternary boundary whose absence
forced the nonterminating binary antiderivative tower.

## Why this bypasses the raising wall

The failed binary method first formed a primitive of \(\Phi\), paired it with
an already transported state, and differentiated the product. That ordering
generated a new common-path residual at every level.

The window instead correlates the two source points and applies the spectral
character before taking the moving-boundary derivative. The three inputs are
never separately totalized. Consequently the derivative produces the desired
relative response in one step, with no higher primitive row.

This is an operation-order theorem as much as an arity theorem:

```text
source pair + spectral character + moving seam
    -> ternary window
    -> boundary derivative
    -> relative Green response
```

## What remains

The continuous local Green forcing is now a genuine source boundary current.
Two global gates remain.

### Arithmetic incidence

Prime-scale constructors provide seam positions \(L=k\log p\), not the full
continuous boundary parameter. No source-derived quadrature or cellular
incidence law has yet shown that those discrete samples reconstruct the full
window variation.

### Endpoint orientation

The integrated window current must enter the completed reciprocal Green form
with the exact endpoint signs and must retain the primitive, square, and
archimedean grades. A scalar equality after aggregation is insufficient.

Therefore the local ternary obstruction is closed, but RH is not. The next
falsifier is a finite prime-power seam packet whose typed window increments do
not assemble into the declared global boundary current.

## Meaning

The post-factum explanation is now precise: the direct relation was hidden
because we repeatedly integrated one leg at a time. The theta source already
carried the required three-way object as an ordered autocorrelation window.
Binary decomposition created an infinite tower that the undecomposed ternary
cell never had.

