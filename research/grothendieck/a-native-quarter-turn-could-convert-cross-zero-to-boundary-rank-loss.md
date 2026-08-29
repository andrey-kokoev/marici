# A native quarter-turn could convert cross zero to boundary rank loss

Author: marici.Grothendieck

Date: 2026-08-28

## Orthogonality versus degeneracy

The passive two-port Weyl determinant measures the Gram geometry of source
and observer. It vanishes when the two transported ports become linearly
dependent. The physical scalar readout instead vanishes when one cross
pairing is zero.

These are different events:

- Gram determinant zero means dependence;
- cross coefficient zero means orthogonality.

This explains why passive completion is nonzero at a theta cross zero.

## Two-dimensional quarter-turn

Let \(V\) be an oriented real two-plane with metric and canonical
quarter-turn

\[
J^2=-I,
\qquad J^*=-J.
\]

Its symplectic form is

\[
\omega(u,v)=\langle u,Jv\rangle.
\]

In dimension two, \(\omega(u,v)=0\) if and only if \(u\) and \(v\) are
linearly dependent.

Thus a scalar cross zero becomes a full boundary-rank loss if the physical
pairing is not the passive inner product but the source-derived symplectic
pairing on a two-dimensional boundary port plane.

## Theta placement

The natural candidate plane is the value--flux boundary space of the
first-order tail system. Its Green form already carries a skew boundary
pairing. If that form supplies a canonical \(J\) and the theta readout can
be derived as

\[
X(s)=\omega\bigl(u_s,v_s\bigr),
\]

then \(X(s)=0\) would be a boundary transversality failure rather than an
ordinary Hilbert-space orthogonality.

This recovers the 90-degree intuition in a typed way. The quarter-turn must
come from the Green boundary form, endpoint orientation, and reciprocal
sewing. It may not be imported as a Fresnel or Maslov phase.

## Sharp gates

The construction succeeds only if:

1. the full source and observer data descend faithfully to one
   two-dimensional boundary plane;
2. the Green form determines \(J\) before examining \(X\);
3. the Evans scalar equals the symplectic determinant up to a nowhere-zero
   unit;
4. off-seam self-adjoint or definite boundary transport forbids
   transversality loss;
5. hostile symmetric multipliers fail to lift to the same boundary system.

If the boundary port has dimension greater than two, symplectic
orthogonality does not imply dependence and the reduction fails. If the
quarter-turn is chosen after seeing the cross response, it is tautological.

## Next calculation

Compute the exact value--flux trace of the doubled theta tail system and its
Green matrix. Determine its rank before scalar aggregation. Then test whether
the Evans border \((\delta_0,f)\) is the pullback of the canonical
symplectic determinant on that trace space.
