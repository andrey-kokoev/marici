# An inner factor is a sector Toeplitz-index obstruction

## Recovery after the passivity falsifier

The passive Blaschke factor

\[
B(s)=\frac{s-1}{s+1}
\]

has unit modulus on the seam and an interior zero. Scalar boundary energy is
blind to that zero. But the boundary phase is not topologically trivial: after
the Cayley identification of the half-plane boundary with the unit circle,
`B` is the degree-one circle coordinate.

Compression of boundary multiplication to the Hardy sector turns this phase
charge into a Fredholm index.

## Exact Hardy model

On the Hardy basis

\[
1,z,z^2,\ldots,
\]

multiplication by the degree-one inner factor `z` is the unilateral shift

\[
S(1,z,z^2,\ldots)=(z,z^2,z^3,\ldots).
\]

It has

\[
\ker S=0,
\qquad
\dim\operatorname{coker}S=1,
\qquad
\operatorname{ind}S=-1.
\]

The missing constant mode is the operator-valued residue of the interior zero.
Unlike boundary modulus, the index detects the inner factor exactly.

For an inner factor of degree `m`, multiplication is the `m`-step shift and
has index `-m`. Thus sector-resolved zero multiplicity is encoded as a stable
operator obstruction.

## Proposed C2 theorem

Let `u_+(t)` be a source-normalized seam comparison for the right half-plane,
valued in a multiplier algebra where the Hardy compression

\[
T_{u_+}=P_+M_{u_+}P_+
\]

is Fredholm. Construct the reciprocal left-sector operator separately.

The desired source theorem is

\[
\operatorname{ind}T_{u_+}=0
\]

for every admissible finite-height packet and through the completed limit.
Since the completed scalar is entire, it contributes no right-half-plane pole
charge. Under a valid argument-principle bridge, a nonzero sector index would
therefore count off-seam zeros.

This is a genuine higher obstruction rather than ordinary horn fillability:
the central Blaschke multiplier changes the Fredholm class even though it
preserves all boundary norms and homogeneous coherence equations.

## Why global index is insufficient

Reciprocal reflection sends the right-sector Blaschke factor to its inverse in
the left sector. Their indices have opposite signs and cancel globally.
Therefore the functional equation and a single global determinant can have
zero total index while each half-plane carries a nonzero obstruction.

The index must remain sector-resolved until after the exclusion theorem. This
is another precise reason the RH architecture is intrinsically two-sector.

## Immediate hard gates

The formulation is not yet an RH proof. At least six issues can falsify it:

1. The actual seam comparison may vanish at allowed critical-line zeros, so a
   unitary boundary symbol may not be defined without a source-authorized
   factorization or indentation.
2. Infinite height and infinitely many seam zeros may destroy Fredholmness.
3. Primitive and square currents may contribute an anomaly index that cannot
   be discarded.
4. A finite-height index can jump through the horizontal boundary arcs.
5. The source-normalized symbol may differ from the Evans scalar by an
   uncontrolled inner factor.
6. Proving index zero from the absence of zeros would be circular.

## DPC

The route passes only if the source independently constructs:

- the right and left Hardy sector spaces;
- the seam multiplier or relative scattering symbol;
- its treatment at declared seam zeros;
- the Toeplitz or Wiener–Hopf compression;
- Fredholmness at each cutoff and through completion;
- the primitive, square, seam, and archimedean index contributions;
- a null-homotopy or exact sequence forcing the sector index to vanish;
- the argument-principle bridge from off-seam zeros to the same index.

Hostile tests must include:

- the degree-one Blaschke factor;
- reciprocal pairs whose global indices cancel;
- finite-cutoff symbols with index zero but a non-Fredholm limit;
- critical-seam zeros that make the boundary symbol singular;
- a source-preserving central multiplier with nonzero sector winding.

## Verdict

This is the first refined C2 obstruction in the current chain that detects the
passive all-pass hostile rather than merely restating scalar nonvanishing.
Its promise is real: off-seam inner factors become missing Hardy modes. Its
main unresolved problem is constructing a source-normalized Fredholm seam
operator despite the allowed critical-line divisor and infinite completion.

