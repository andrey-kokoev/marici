# Hadamard readout detects but does not split the integral deck extension

## Two coherent output ports

For direct and reciprocal route amplitudes `A` and `B`, define

`D=A-B`

and

`S=A+B`.

The forward readout is the integral matrix

`H=[[1,-1],[1,1]]`.

Benincasa's infinity packet has `A=B` after the two independent reflection
signs are paired.  Therefore `D=0` while `S=2A` remains nonzero.  The dark
port certifies coherence closure; the bright port retains the physical
period.

## The inverse changes coefficient category

The determinant of `H` is two, and

`H^(-1)=(1/2)[[1,1],[-1,1]]`.

Thus the optical readout is invertible over the real or complex amplitude
field, but not unimodular over the integral source lattice.  Reconstructing
the individual routes from `(D,S)` requires

`A=(S+D)/2`, `B=(S-D)/2`.

This is exactly the half-sum forbidden by the nonsplit integral deck
extension.  The beam combiner measures the rationalized extension; it does
not supply an integral equivariant section.

Modulo two, the two output rows coincide and the readout has rank one.  Its
integral cokernel has order two.  The missing bit is therefore structural,
not detector noise.

## Apparatus protocol

Record both `D` and `S`, not the dark port alone.  Apply the following
interpretation gates:

- `D=0`, `S!=0`: coherent route equality with surviving physical output;
- `D!=0`: failed coherence or a missing typed reflection factor;
- reconstruction of `A,B`: valid as complex metrology only;
- claim of an integral sheet selector: rejected unless an independent source
  operation supplies the required half-sum or breaks deck symmetry.

An optical `50:50` beamsplitter implements the normalized complex matrix
`H/sqrt(2)`.  Its physical availability cannot be transported backward as
authority for division by two in the arithmetic source category.

## Cross-sector implication

Whenever a Marici comparison port is built from sum and difference channels,
the determinant of its integral readout matrix must be audited.  A perfectly
unitary laboratory basis change can conceal torsion or a nonsplit extension
in the source lattice.  The apparatus then detects the obstruction precisely
because it operates after scalar extension; it does not erase the
obstruction upstream.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_hadamard_integral_deck_extension.py
```
