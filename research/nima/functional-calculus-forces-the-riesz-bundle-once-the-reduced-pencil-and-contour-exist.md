# Functional calculus forces the Riesz bundle once the reduced pencil and contour exist

## Authority correction

The Riesz projection is not an independently fitted source object. Once a source-authorized reduced pencil \(K_X(s)\) and isolating contour \(\Gamma\) are fixed, functional calculus forces
\[
P_X(s)
=
\frac{1}{2\pi i}
\int_\Gamma (z-K_X(s))^{-1}\,dz.
\]
Accordingly, source authority belongs to:

1. the radical-reduced common carrier and graph domain;
2. the operator family \(K_X(s)\) assembled on that domain;
3. the declaration of the spectral cluster tracked by \(\Gamma\);
4. proof that \(\Gamma\) stays uniformly in the resolvent.

The projection bundle, its differentiability, and its induced connection are derived consequences.

This sharpens the preceding audit: the first absent constructor is the common-domain norm-resolvent assembly of the reduced theta pencil with an authorized contour-separated cluster.

## Present pointwise data

The current programme has pointwise candidates:

- the polarized Green form \(B_X(s)\);
- the synthesis defect \(F_X(s)=U_X(s)U_X(s)^*\);
- generalized eigenvalue or Birman–Schwinger expressions near the spectral value \(1\);
- finite radical reductions and carrier-comparison conditions.

These do not yet constitute one operator family. In particular, pointwise formulas do not by themselves prove that all \(K_X(s)\) act on a common reduced domain or that their resolvents vary in norm.

## Missing assembly arrow

The required source arrow is
\[
(B_X(s),F_X(s),\mathcal N_X(s))
\longmapsto
K_X^{\mathrm{red}}(s)
\]
on a carrier whose radical reduction is fixed over the parameter patch. Depending on the geometry, this may be:

- a bounded Birman–Schwinger operator on the Green quotient;
- a generalized pencil \(F_X(s)-\lambda B_X(s)\);
- a sectorial-form operator obtained from a common closed form domain.

The assembly must not use \(B_X(s)^{-1/2}\) where the Green form is only semidefinite. It must first prove radical compatibility and choose the authorized quotient or reachable restriction.

The contract packet is therefore revised to:

    verdict: incomplete
    first_absent_constructor: common_domain_reduced_pencil_assembly
    ambient_mellin_connection: present
    source_authorized_spectral_cluster: absent
    riesz_projection_bundle: derived_after_missing_constructor
    first_failed_degree: null
    equation_evaluation_started: false

## Contour authorization is mathematical data

A contour is not authorized merely because it encloses \(1\). The source theorem must specify which finite spectral cluster represents the defect mechanism and prove:

- finite algebraic multiplicity inside \(\Gamma\);
- no spectrum on \(\Gamma\);
- stability of the same cluster under parameter, cutoff, and reciprocal transport;
- compatibility with the limiting operator;
- no contour choice made retrospectively from a desired zero-free region.

A common contour on a compact parameter patch is precisely the local spectral-separation certificate.

## Derived projection theorem

Suppose:

1. \(K_X(s)\) is a closed operator on a common graph domain \(D_X\);
2. \(s\mapsto K_X(s)\) is graph-norm \(C^1\);
3. \(\Gamma\subset\rho(K_X(s))\) for every \(s\) in the patch;
4. the resolvent and its parameter derivative are uniformly bounded on \(\Gamma\).

Then \(P_X(s)\) is norm-\(C^1\), finite rank, and unique. Its derivative is
\[
\dot P_X(s)
=
\frac{1}{2\pi i}
\int_\Gamma
(z-K_X(s))^{-1}\dot K_X(s)(z-K_X(s))^{-1}\,dz.
\]
No additional source selection of \(P_X\) is permitted or needed.

The ambient Mellin connection \(\nabla^{\mathcal H}\) then induces
\[
\nabla^{\mathcal D}=P_X\nabla^{\mathcal H}P_X.
\]

## Naturality by resolvent calculus

If cutoff inclusion satisfies
\[
\iota_{X,Y}K_X(s)=K_Y(s)\iota_{X,Y}
\]
on the common domains, then for \(z\in\Gamma\),
\[
\iota_{X,Y}(z-K_X(s))^{-1}
=
(z-K_Y(s))^{-1}\iota_{X,Y}.
\]
Contour integration forces
\[
\iota_{X,Y}P_X(s)=P_Y(s)\iota_{X,Y}.
\]

Likewise, if reciprocal transport satisfies
\[
J_X(s)K_X(s)=K_X(\rho(s))J_X(s)
\]
with the required conjugate-linear convention, functional calculus forces reciprocal naturality of \(P_X\). Projection naturality is therefore a theorem inherited from pencil naturality.

## Mandatory hostile

Let \(P_1(s)\) and \(P_2(s)\) be two arbitrary smooth projection fields on the same flat Mellin bundle. Even if both:

- have the same rank;
- respect the ambient connection up to smooth gauge;
- satisfy cutoff-compatible dimensions;
- have reciprocal-looking scalar shadows;

they are inadmissible unless
\[
P_j(s)
=
\frac{1}{2\pi i}\int_\Gamma(z-K_X(s))^{-1}\,dz
\]
for the declared source pencil and contour. Smooth compatibility is not functional-calculus authority.

Conversely, once the pencil and contour are fixed, choosing between \(P_1\) and \(P_2\) is impossible: uniqueness of the Riesz projection rejects the extra freedom.

## Revised decisive theorem

Construct the complete reduced theta pencil family on one common graph domain after Green-radical reduction and prove a compact-local contour theorem around the generalized eigenvalue \(1\). Specifically:

1. radical reduction is stable over the patch;
2. the reduced pencil is closed and norm-resolvent \(C^1\);
3. one source-authorized \(\Gamma\) tracks the defect cluster;
4. cutoff and Real maps intertwine the reduced pencil;
5. the finite family converges spectrally exactly to the completed pencil near \(\Gamma\).

Then every remaining projection, Kato-transport, charge, and determinant-splitting constructor in the tower is forced. The current gap is the reduced pencil assembly itself, not freedom to choose a projection.
