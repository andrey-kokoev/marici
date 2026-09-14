# The quarter twist is integral only on the linked normal curve

## Question

Does the mathematically available quarter-exponent local system preserve the selected rank-three integral lattice in a punctured neighborhood of the three relative divisors?

## Claim boundary

This tests local monodromy integrality. It does not rule out the one-dimensional linked normal contour, on which the combined residue is integral.

## Individual residues

At the three vanishing factors \(B=X_1-Y\), \(C=X_2+Y\), and \(E=X_1+X_2\), the selected residue matrices satisfy

\[
R_B^2=R_B,
\qquad
R_C^2=R_C,
\qquad
R_E^2=2R_E.
\]

Thus \(R_B\) and \(R_C\) each have one eigenvalue one, while \(R_E\) has one eigenvalue two.

At quarter twist, the monodromies about \(B\) and \(C\) have eigenvalue

\[
\exp(2\pi i/4)=i.
\]

Explicitly,

\[
M_B=I+(i-1)R_B,
\qquad
M_C=I+(i-1)R_C.
\]

These matrices are not defined over \(\mathbb Z\), or even over \(\mathbb Q\). A one-dimensional \(i\)-eigenspace cannot carry a rank-one integral lattice because the only units of \(\mathbb Z\) are \(\pm1\). Its minimal integral realization requires rank two over \(\mathbb Z\), or coefficients extended to \(\mathbb Z[i]\).

## Linked normal curve

On the wall-labelled normal maps,

\[
B=E_{\rm cond},
\qquad
C=E_{\rm cond},
\qquad
E=2E_{\rm cond},
\]

so one loop in the conductor normal coordinate winds around all three relative factors together. The pullback connection has the combined residue

\[
R_{\rm eq}=R_B+R_C+R_E,
\]

whose quarter-twisted monodromy is the integral involution already shown conjugate to \(M_1M_2\).

Hence integrality is recovered only after restricting to this linked one-dimensional contour. It does not extend to independent loops around \(B\) and \(C\) in the ambient relative arrangement.

## Non-normal-crossing warning

The three residues do not commute pairwise. Since \(E=B+C\), the triple intersection is not a coordinate normal crossing with three independent loop generators. The combined monodromy must be computed from the pulled-back residue on the chosen normal curve; it cannot be replaced by an unordered product of three independent divisor monodromies.

## Consequence

The Cayley–Menger formalism permits complex exponent parameters, so a quarter twist is mathematically definable. But the selected integral pairing survives only on the linked conductor-normal curve, not as a rank-three integral local system over the full punctured relative neighborhood.

This identifies the exact contour requirement: a physical or source-derived contour must map to the linked loop \(B=C\sim E\), preserving their common winding. Independent encirclement of either endpoint divisor leaves the integral category.

## Disposition

The quarter-twist local system is mathematically available over complex or Gaussian coefficients, while its integral rank-three descent exists only after linked-normal pullback. Physical authority for that linked contour remains absent.
