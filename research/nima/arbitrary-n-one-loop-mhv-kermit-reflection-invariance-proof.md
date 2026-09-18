# Arbitrary-n reflection invariance of the one-loop MHV Kermit sum

## Theorem

Let `sigma` reverse the cyclic order of the external labels while fixing one chosen anchor. For every `n>=4`,

$$
\sigma\mathcal A_n^{(2),1}=\mathcal A_n^{(2),1}.
$$

Together with cyclic invariance, the pre-integration one-loop MHV integrand is dihedrally invariant.

## Reflected triangulation

Applying `sigma` to every external label sends the sourced Kermit decomposition to another oriented decomposition of the same one-loop MHV positive geometry. It reverses the polygon order but preserves the loop line `(AB)` and the projective line measure.

Every reflected nonlocal anchor facet remains internal. The reflected form of the Kermit involution pairs the two cells adjacent to it with opposite induced orientations, so all such facets cancel.

## Physical boundary orientation

A physical boundary is labelled by an unoriented cyclic edge:

$$
\langle AB\,i(i+1)\rangle=0.
$$

Reflection reverses both endpoint order and the polygon orientation. In the complete four-form these two reversals give the same outward boundary orientation as the corresponding reflected propagator facet. Thus reflection permutes the physical boundary components without changing their canonical boundary forms.

The original and reflected Kermit chains therefore have the same complete oriented boundary.

## Canonical-form uniqueness

Both chains triangulate the same projective positive geometry, have only logarithmic boundary poles, and have no independent pole at infinity. Additivity and uniqueness of canonical forms imply

$$
\Omega(\sigma T_n)=\Omega(T_n).
$$

Equivalently, their difference has zero residue on every internal and physical divisor; projectivity excludes a pole-free top-form remainder.

## Exact finite evidence

`check_one_loop_mhv_kermit_reflection_invariance.py` constructs the rational Kermit sum in the orders

$$
(1,2,\ldots,n)
\quad\text{and}\quad
(1,n,n-1,\ldots,2)
$$

and finds exact equality on generic rational momentum-twistor fixtures for every `4<=n<=9`.

## Claim boundary

This proves reflection and hence dihedral invariance of the sourced pre-integration one-loop MHV integrand. It does not assert parity invariance of individual chiral Kermit terms or invariance of a regulated integrated amplitude.
