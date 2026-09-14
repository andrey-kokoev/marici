# Prior research: Koszul-to-Green chain-map frontier

Date: 2026-09-08

## Theta complex exists

A superseding packet constructs the theta side canonically from the source Mellin dual section

\[
\tau\in H^0(U,\mathcal L_\theta^*),
\qquad
K_\tau:
0\to\mathcal L_\theta\xrightarrow{\tau}\mathcal O_U\to0.
\]

In a source frame, its determinant is exactly `xi(s)`.  At a zero, its local cohomology is the residue module

\[
\mathcal O_{s_0}/(\xi),
\]

whose length is the zero multiplicity.  Reciprocal sewing acts by chain isomorphisms.  Thus the theta-divisor complex and its multiplicity data are no longer missing.

## Why metric duality fails

The Riesz representative of `tau_s` vanishes when `xi(s)=0`.  Every bounded incidence applied to that representative also vanishes, so it cannot supply the required nonzero Green kernel state.  The comparison must act on the carrier line or Koszul residue, not on the vanishing covector.

The necessary independent incidence has the divisibility form

\[
i_s:\mathcal L_{\theta,s}\to H_s,
\qquad
C(s)i_s=w_s\tau_s,
\]

with `i_s` remaining injective at divisor points.  At a zero, this produces a nonzero carrier-line state in `ker C(s)` without division by `xi`.

## Mapping-cone criterion

The correct comparison is a chain map

\[
K_\tau\longrightarrow C_{\rm FP}
\]

whose cone has a bounded holomorphic contraction.  Acyclicity would provide:

- zero-to-kernel equivalence;
- equality of local module lengths;
- a nowhere-zero determinant torsion factor;
- reciprocal compatibility;
- exclusion of scalar fitting.

## Current exact residual

The latest model audit identifies the unchanged-Evans component of this chain map with

\[
B_\Sigma^\dagger u_z=0
\]

on the Xi divisor, required shell by shell and through completion.  This is the RH-bearing vector identity.  Scalar Evans mismatch does not imply it.

The repository does not yet provide:

1. the independent carrier-line incidence `i_s` satisfying the divisibility square;
2. the prime-shell adjoint residual family proving `B_Sigma^dagger u_z=0`;
3. the holomorphic cone contraction;
4. local module-length preservation under the comparison;
5. an authoritative locator fully defining the conservative Green complex and its boundary sewing.

## Disposition

Prior research closes the theta-complex object-definition problem but not its comparison to the conservative Green pencil.  The earliest constructive target is the independent incidence/divisibility square, not another scalar determinant or Riesz lift.  Its failure criterion is nonzero `B_Sigma^dagger u_z` at any prime shell on a Xi-divisor state.

## Evidence

- `research/nima/the-xi-dual-section-defines-a-canonical-koszul-complex-with-the-correct-divisor.md`
- `research/nima/the-riesz-lift-of-the-xi-dual-section-vanishes-at-the-divisor-and-cannot-be-the-defect-state.md`
- `research/nima/g4-is-equivalent-to-an-acyclic-mapping-cone-between-the-theta-section-complex-and-the-green-boundary-pencil.md`
- `research/nima/current-rh-model-versus-scc-audit-after-the-three-port-and-evans-corrections.md`
- `research/nima/candidate-two-cannot-be-identified-with-g4-from-the-current-scc-witness.md`
