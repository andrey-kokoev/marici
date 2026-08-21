# The naive all-places scaling colimit cannot acquire the Xi spectrum

Sequence claim: `seqclaim-bc180db10f45c7a986404e99` (1400).

Epistemic-graph event: 1446.

## Setup

For every finite set of places `S` containing the archimedean place, the CCM
Hardy--Titchmarsh transform identifies the semilocal scaling pair with

`(M_s, xi_S)` on `L^2(R,dm_S)`,

where `M_s` is multiplication by the real variable and

`dm_S(s)=c_S |product_(v in S) L_v(1/2-is)|^2 ds`

for a harmless positive normalization `c_S`.  At every real `s`, each finite
Euler factor is finite and nonzero because `|p^(-1/2+is)|=p^(-1/2)<1`; the
archimedean gamma factor is also finite and nonzero on this line.

## Spectral-type theorem

The measure `dm_S` is mutually absolutely continuous with Lebesgue measure.
Multiplication by its positive square-root gives a unitary

`U_S:L^2(R,dm_S) -> L^2(R,ds)`

which commutes with multiplication by `s`.  Therefore every finite-place
scaling operator is unitarily equivalent to the same operator `M_s` on
Lebesgue `L^2`.

It follows that, for every finite `S`, the scaling operator has spectrum `R`,
has no eigenvalues, is purely absolutely continuous, and has noncompact
resolvent.  Enlarging `S` changes the cyclic vector/spectral weight but not
this operator's unitary equivalence class.

Consequently, any directed system whose crossing maps are the canonical
multiplication identifications and intertwine scaling cannot turn the ambient
scaling generator into a discrete-spectrum operator.  Even if an inductive
limit exists, it remains a multiplication representation with continuous
spectral type (possibly with increased multiplicity).  Discreteness can only
enter through an additional nonunitary operation: a radical quotient,
compression, boundary condition, or conditioning limit.

## The raw Euler multiplier has no critical-line colimit

Let `S_P` contain infinity and all primes at most `P`.  At the central spectral
point `s=0`, its finite Euler multiplier contains

`Z_P(1/2)=product_(p<=P)(1-p^(-1/2))^(-1)`.

Since `-log(1-x)>=x` for `0<x<1`,

`log Z_P(1/2) >= sum_(p<=P) p^(-1/2)
                 >= sum_(p<=P) p^(-1)`.

Euler's theorem that the sum of reciprocals of the primes diverges therefore
gives `Z_P(1/2)->infinity`.  Completed Xi is finite and nonzero at its central
point.  Thus the unrenormalized finite-place multipliers cannot converge
pointwise there, hence cannot converge locally uniformly to the completed Xi
factor on any neighborhood of that point.

A scalar normalization `c_S` can hide this one value in the measure, but it is
new data and does not produce an analytic determinant.  A valid construction
would still have to specify the normalization canonically and prove
simultaneous convergence of domains, resolvents, and determinant ratios.

## Falsifier

The smallest spectral falsifier already occurs at `S={infinity}`.  Its scaling
operator is multiplication by `s` against a positive gamma-weighted density,
so it has no point spectrum.  Adding one prime multiplies the density by a
bounded positive function on the real axis and yields an equivalent measure;
the operator still has no point spectrum.  Repeating this finite step never
creates an eigenvalue.

The smallest colimit falsifier is the central value above: each added prime
strictly enlarges `Z_P(1/2)`, and the product diverges.

## Consequence for the Xi program

The semilocal family is useful as source-derived arithmetic input, but its
ambient Hilbert colimit is not the desired operator.  The surviving lane is

`finite-place source maps -> global Weil form -> radical quotient/boundary`.

Only after that nonunitary quotient may one seek a self-adjoint
compact-resolvent realization.  Positivity of the resulting boundary is still
the RH-equivalent Pick/Weil gate identified earlier.  The conditional
determinant theorem cannot be attached before that gate.

## Scope

This is a no-go theorem for the naive ambient scaling colimit and the
unrenormalized critical-line Euler product.  It does not exclude a
source-derived renormalized quotient, a prolate conditioning limit, or a
de Branges/Pick boundary construction.
