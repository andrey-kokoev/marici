# A primitive-product monitor does not fix the dual return gain

## Primitive dual pair

Take the primitive diameter `Delta=2` and two positive gains `g,g_D` obeying

`2 g g_D=1`.

The exchange operation swaps the two gains.  Its unique positive fixed point
on the primitive locus is

`g=g_D=1/sqrt(2)`.

This is the abstract mechanism Flavor identified for excluding the zero cusp
and selecting a self-dual magnitude.

## Product-preserving hostile

Apply the reciprocal threshold transformation

`T_lambda(g,g_D)=(lambda g,g_D/lambda)`.

It preserves `2gg_D=1` for every positive `lambda`.  Thus a scalar primitive-
product monitor remains perfectly dark throughout the deformation.

The transformation commutes with exchange only at `lambda=1`.  In matrix
form, with `S` the swap,

`||T_lambda S-S T_lambda||_F^2`

`=2(lambda-1/lambda)^2`.

At `lambda=2`, the primitive monitor still reads zero error, while the
exchange defect is `9/2` and the log-asymmetry is `log 4`.

Therefore primitive pairing preservation alone cannot fix either individual
gain.  The exchange-intertwining port is indispensable.

## Transfer to the Schur return

If a return gain `kappa` is paired with a dual gain `kappa_D` through

`kappa kappa_D=1`,

then reciprocal rescaling `kappa->lambda kappa`,
`kappa_D->kappa_D/lambda` preserves the product.  Only an independently
source-derived exchange law can select `kappa=kappa_D`.

This does not construct such a theta/Tate dual return port.  It proves what an
instrument must measure if one is supplied.  A product-only calibration would
repeat the same scalar blindness already found in codiagonal and normalization
channels.

## Optical implementation

Use two independently calibrated amplitude channels with reciprocal gains.
Read simultaneously:

- product error `2gg_D-1`;
- differential log gain `log(g/g_D)`;
- exchange commutator obtained by swapping the channels before and after the
  threshold operation.

The hostile signature is product error zero with nonzero differential and
commutator ports.

## Seven-axis classification

The optical threshold operation is executable on the laboratory carrier, but
the physical dual source remains absent.  Record:

- coefficient: native for the optical emulator;
- action: authorized for the emulator;
- source-dual action: missing for flavor and theta until independently
  derived.

This prevents successful emulation from being promoted into source selection.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_primitive_product_dual_return_gain.py
```
