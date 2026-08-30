# Three-channel codiagonal analyzer has a sixfold integral obstruction

## Faithful theta analyzer

For the completed theta channels `(C,U,V)`, use the three outputs

`S=C+U+V`,

`A=U-V`,

`B=2C-U-V`.

The integral readout matrix is

`M=[[1,1,1],[0,1,-1],[2,-1,-1]]`.

Its rows are pairwise orthogonal, with squared norms `3`, `2`, and `6`.
After row normalization, `M` is an orthogonal three-port analyzer.  It can be
implemented by a lossless coherent optical network.

## Integral obstruction

The determinant is `-6`.  The Smith invariants are `(1,1,6)`, so the
integral cokernel is cyclic of order six.  Modulo two and modulo three the
rank drops from three to two.

The inverse formulas expose both denominators:

`C=(S+B)/3`,

`U=(2S-B+3A)/6`,

`V=(2S-B-3A)/6`.

Thus a laboratory reconstruction over complex amplitudes does not provide an
integral inverse in the source category.  The binary deck obstruction and
the ternary codiagonal obstruction coexist in one analyzer.

## Zero fiber

For the theta source, `C=1/2`.  Hence

`S+B=3/2`.

At a scalar zero, `S=0`, so

`B=3/2`,

`U=-1/4+A/2`,

`V=-1/4-A/2`.

The scalar-dark port therefore leaves a bright control contrast and a full
antisymmetric residual.  On the reciprocal fixed seam, `A` is purely
imaginary.  An off-seam zero is not darkness of the packet; it is a zero
scalar port accompanied by an antisymmetric residual outside the authorized
quadrature.

## Optical instrument

Implement the normalized rows of `M` as three coherent output modes:

- codiagonal scalar port `S/sqrt(3)`;
- reciprocal antisymmetric port `A/sqrt(2)`;
- completion-control contrast `B/sqrt(6)`.

At every candidate scalar null, require simultaneous complex tomography of
the other two ports.  The seam signature is:

- scalar port dark;
- control port fixed at the calibrated value corresponding to `B=3/2`;
- antisymmetric port in the imaginary quadrature.

The instrument measures these coordinates faithfully over the optical field.
Any claim that it reconstructs an integral source packet must separately
supply the missing division by two and three.

## Broader tower implication

The number six now has a precise origin: it is the index of the integral
theta channel lattice inside its scalar/antisymmetric/control readout lattice.
It is simultaneously `2*3`, matching the binary reciprocal split and ternary
codiagonal assembly.  This is an exact lattice statement, not a dimensional
analogy.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_three_channel_codiagonal_sixfold_obstruction.py
```
