# RH star confinement requires a zero-to-dagger promotion constructor

## Equalizer formulation

Let \(\mathsf{Rec}\) and \(\mathsf{Adj}\) be reciprocal transport and Hilbert
adjunction on the complete continuous boundary-cocycle category. Their
equalizer consists of the objects on which the two transports agree.

The source calculation already identifies this equalizer with the critical
seam.

Let \(\mathcal Z\) be the subcategory of completed zero-induced boundary
states. A reciprocal-to-adjoint comparison on every zero state is precisely a
factorization

\[
\mathcal Z\longrightarrow
\operatorname{Eq}(\mathsf{Rec},\mathsf{Adj})
\longrightarrow
\mathcal C.
\]

Since the equalizer is the seam, constructing this factorization is already
the categorical RH statement. It cannot be inferred merely from the
existence of the two transports.

## The missing constructor

The required new operation has type

```text
zero-induced summability upgrade
    -> star-compatible continuous boundary state
```

Call it the zero-to-dagger promotion. Its output is stronger than a convergent
packet, a continuous extension, or reciprocal symmetry. It equips the state
with a comparison cell between reciprocal and adjoint mates.

Like every authority-bearing constructor, it needs:

- a source-defined domain;
- an output signature carrying the dagger comparison;
- a support and completion contract;
- naturality under cutoff restriction;
- a coherence law with Fourier–Tate sewing;
- finite and completion falsifiers.

The scalar condition `completed readout equals zero` is evidence presented to
the constructor. It is not authority to manufacture the output comparison
cell.

## Hostile symmetric multiplier

The polynomial

\[
H(z)=z^2+1
\]

is even and compatible with complex conjugation. It has off-seam zeros at
(z=\pm i). Attach it at the scalar readout level while leaving the continuous
boundary cocycle unchanged. At (z=i), the scalar readout vanishes while the
exact boundary fixture has star residual one half.

This hostile does not claim to be the theta source. It proves a logical
no-go: scalar reflection symmetry, real structure, and nullity do not generate
the dagger comparison. A valid source theorem must reject the multiplier at
the constructor level before reading its zeros.

## DPC

The promotion proposal has five possible verdicts.

1. Source promotion: a named theta/Tate operation constructs the dagger cell
   on every zero-induced state without using zero locations.
2. Domain mismatch: zero-induced states do not lie in the operator domain on
   which the comparison is defined.
3. Support loss: the promotion factors through scalar aggregation and cannot
   act on the complete boundary carrier.
4. Hostile survival: an off-seam symmetric multiplier preserves every input
   accepted by the promotion while retaining nonzero star residual.
5. Circular equalizer restriction: the constructor domain is defined by
   reciprocal-adjoint equality, so the seam is assumed in advance.

## What could genuinely supply promotion

Only a source operation coupling the zero boundary condition to the dagger
structure can advance this route. Plausible forms are:

- a Green identity whose vanishing endpoint flux forces the star residual to
  vanish;
- an Evans or relative-determinant boundary system in which kernel formation
  automatically produces adjoint-compatible mates;
- a reflection-positive completion functor proved to preserve the
  zero-to-state complex;
- a source-derived antiunitary acting on the full representation-valued
  packet, together with a theorem that zero states lie in its fixed locus.

Each formulation is the same missing promotion at a different level. Merely
naming an antiunitary or dagger category does not construct the fixed-locus
factorization.

## Consequence

The star-extension route has reached the same structural boundary as the
mixed Green route. Both require one new source law connecting scalar
zero-state formation to a stronger relational structure. All presently
derived transport, completion, and interval coherence explains the objects
on either side but does not construct that arrow.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_zero_to_dagger_promotion.py
```
