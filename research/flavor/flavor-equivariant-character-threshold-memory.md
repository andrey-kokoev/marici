# Equivariant Character Can Carry the Diameter through a Threshold

## Question

Can a source-derived threshold remainder preserve WP841's ultraviolet charge
diameter after an extremal charged state decouples?

## Ordinary anomaly data is too coarse

For the primitive spectrum (S=\{1,2,3\}), the linear and cubic charge sums
are

\[
A_1=6,
\qquad A_3=36,
\qquad \Delta(S)=2.
\]

Add the vectorlike pair ({4,-4}). Both odd anomaly sums remain 6 and 36,
but the diameter becomes 8. Therefore ordinary linear and cubic anomaly
matching is not faithful on the diameter needed by WP841.

## Representation-valued threshold remainder

Instead retain the full equivariant character

\[
\chi_S(z)=z+z^2+z^3.
\]

When charge one decouples,

\[
\chi_{\rm active}(z)=z^2+z^3,
\qquad
\chi_{\rm heavy}(z)=z,
\]

and

\[
\chi_S=\chi_{\rm active}+\chi_{\rm heavy}.
\]

The active character alone has support diameter one. The sewn character has
support ({1,2,3}) and reconstructs the ultraviolet diameter two exactly.
If WP841's beta law is typed against this completed character rather than the
active particle list, its selected coordinate remains (x_*=1/2) across the
threshold.

This is an algebraic repair of the diameter carrier. It does not assert that
ordinary Wilsonian matching automatically retains the full representation
character.

## Finite holonomy probe

On the declared support (q\in\{0,1,2,3}), four holonomy evaluations at

\[
z\in\{1,-1,i,-i}
\]

form an invertible discrete Fourier matrix. They reconstruct every character
coefficient and therefore the support and its diameter. This is a finite
faithful probe family on the bounded character packet.

The probe is relational. Coupling the flavor source to a background holonomy
adds a reference port and changes the physical groupoid to the stabilizer of
that background. It does not reveal an absolute phase of the original flavor
experiment. A real instrument would require controlled background-flavor
holonomy, phase-resolved records, and a calibrated map to detector units.

## Source and matching authority

Known anomaly matching guarantees selected polynomial anomaly data, not the
whole character. Promoting (chi_{\rm heavy}) to a physical threshold memory
requires a source theorem—such as an equivariant index or background-
holonomy effective action—whose finite matching retains every coefficient.
Without that theorem the character remainder is an added bookkeeping port.

## Disposition

Progressive conditional threshold repair. The full equivariant character is
faithful enough to preserve the ultraviolet diameter and admits a finite
four-port reconstruction on the declared bounded support. Ordinary anomaly
matching is insufficient. Source authority for representation-valued
matching and a physical holonomy-resolved instrument remain open.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp846_equivariant_character_threshold_memory.py
```
