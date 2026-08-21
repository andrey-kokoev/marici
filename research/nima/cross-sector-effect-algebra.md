# Scattering and flavor share a finite effect-algebra interface

## Common construction

Let \(\rho\) be a positive normalized state and let
\(\{E_i\}\) be pairwise orthogonal effects satisfying

\[
E_iE_j=\delta_{ij}E_i,\qquad \sum_iE_i=1.
\]

Then

\[
p_i=\operatorname{Tr}(\rho E_i)
\]

is a probability state. A deterministic coarse-graining along a partition
\(\pi:\Omega\to\bar\Omega\) is implemented internally by

\[
\bar E_{\bar\omega}
=\sum_{\pi(i)=\bar\omega}E_i.
\]

This supplies the operational refinement structure missing from a mere
positive decomposition.

## Scattering realization

The fixed-kinematics Cut and partial trace give a reduced helicity density
state \(\rho_L\). The two helicity projectors are exhaustive effects. Summing
them gives the unpolarized effect, and their Born pairings give the Schmidt
probabilities.

## Flavor realization

For a selected up-type mass eigenstate,

\[
\rho_i=P_i^u,
\qquad
E_j=P_j^d,
\]

and therefore

\[
\operatorname{Tr}(P_i^uP_j^d)=|V_{ij}|^2.
\]

The down-type spectral projectors are exhaustive effects on the common
left-handed flavor space. Grouping physical flavor labels is literally
addition of effects.

## Result

The exact rational checker verifies positivity, completeness, orthogonality,
normalization, and coarse-effect additivity in both sectors. Hence the shared
structure is sharper than a generic projective-positive cone:

\[
\boxed{
\text{state}
+\text{finite commutative effect algebra}
+\text{state--effect pairing}
+\text{effect refinement}.}
\]

Shannon entropy is the refinement cocycle of the induced classical state on
this effect algebra.

## Boundary

This does not identify the scattering Hilbert space with flavor space or
construct a physical bridge between sectors. They independently realize the
same diagram shape. Cosmology still lacks the decisive ingredient: a
source-declared exhaustive family of physical effects separating its positive
summands.
