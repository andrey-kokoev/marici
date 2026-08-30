# Fredholm discreteness at one is a separate gate before contour isolation

## Ordered correction

A common-domain reduced form pencil is not enough to define a finite-dimensional defect bundle. Relative \(b_s\)-boundedness of \(f_s\) gives a closed form realization, but it does not exclude
\[
1\in\sigma_{\mathrm{ess}}(K_s).
\]
If \(1\) lies in essential spectrum, no sufficiently small contour around it yields a finite-rank Riesz projection, even though every finite cutoff has only discrete spectrum.

The analytic gate order is therefore:

1. common-domain reduced form pencil;
2. relative compactness and Fredholmness near \(1\);
3. resolvent annulus around \(1\);
4. finite-rank Riesz/Kato bundle;
5. completion spectral exactness.

## Relative compactness package

After stable Green-radical reduction, let \(\mathcal V\) be the common closed form domain equipped with the Green graph norm
\[
\|u\|_{\mathcal V,s}^2=b_s[u,u]+\|u\|^2.
\]
A sufficient package is either:

- compactness of the embedding
  \[
  \mathcal V\hookrightarrow\mathcal H^{\mathrm{red}};
  \]
  or
- \(b_s\)-compactness of \(f_s\): every sequence bounded in the Green form norm and weakly convergent there has an \(f_s\)-image converging strongly in the appropriate dual or represented carrier.

Uniformity on compact parameter sets is required. Pointwise compactness alone does not prevent the compactness margin from collapsing with \(s\) or cutoff.

When \(b_s\) becomes coercive on the reduced carrier, the represented arithmetic action defines a compact Birman–Schwinger operator \(K_s\). In the merely semidefinite presentation, this statement is made only after quotient reduction; no inverse square root is used on the unreduced space.

## Type-(a) dependence

Require \(b_s\) and \(f_s\) to form a holomorphic or norm-\(C^1\) common-domain family of closed forms in Kato's type-(a) sense:

- the form domain \(\mathcal V\) is independent of \(s\);
- \(s\mapsto b_s[u,v]\) and \(s\mapsto f_s[u,v]\) have the declared regularity for all \(u,v\in\mathcal V\);
- form norms are compact-locally equivalent;
- relative bounds and compactness estimates are compact-locally uniform.

The representation theorem then yields the corresponding resolvent regularity for the associated operators or generalized pencil.

## Fredholm consequence

Relative compactness makes the arithmetic part a compact perturbation in the reduced Green geometry. Hence for \(\lambda\ne0\), generalized spectral points of
\[
f_s[u,v]=\lambda b_s[u,v]
\]
are discrete with finite algebraic multiplicity, accumulating only at the permitted boundary point of the compact model. In particular, if \(1\) is spectral, its root space is finite-dimensional and the pencil is Fredholm near \(1\).

This establishes finiteness, not exclusion. RH-strength work begins only after proving that \(1\) is absent from the relevant off-seam component.

## Isolation gate

Fredholmness does not itself provide a gap. One must next prove a compact-local annulus
\[
0<|z-1|\le\delta_C
\]
contained in the resolvent except possibly at the finite cluster at \(1\). Only then does functional calculus define the finite-rank projection
\[
P_s=\frac{1}{2\pi i}\int_{|z-1|=\delta}(z-K_s)^{-1}\,dz.
\]

Thus two distinct questions remain:

- **discreteness:** is the defect cluster finite-dimensional?
- **isolation/exclusion:** is it isolated, and is its Riesz rank zero off the seam?

They must not be merged.

## Mandatory essential-spectrum hostile

Let
\[
\mathcal H=\ell^2(\mathbb N),
\qquad
b[u,v]=\langle u,v\rangle,
\qquad
f[u,v]=\langle u,v\rangle.
\]
Then \(f\) is \(b\)-bounded with relative bound \(1\), and the normalized action is
\[
K=I.
\]
Therefore
\[
1\in\sigma_{\mathrm{ess}}(K)
\]
with infinite multiplicity. Every finite truncation \(K_N=I_N\) has a finite contour packet of rank \(N\), but the completed contour projection is the identity of infinite rank. There is no finite-dimensional completed defect complex.

This directly falsifies the inference:
\[
\text{relative boundedness}+\text{finite-cutoff discreteness}
\Longrightarrow
\text{completed finite-rank Riesz bundle}.
\]

A softer hostile uses diagonal eigenvalues converging to \(1\). Each finite cutoff admits a small contour separating its nearby eigenvalues, while no cutoff-independent annulus survives completion.

## Completion spectral exactness remains later

Even uniform relative compactness of the completed family does not prove that finite cutoffs approximate its spectral packet correctly. One still needs collectively compact or norm-resolvent convergence near the contour. The completion gate must verify:

- no spectral pollution near \(1\);
- convergence of contour resolvents;
- convergence and eventual rank stability of Riesz projections;
- compatibility with cutoff and reciprocal transport.

Fredholmness makes the target packet finite. Spectral exactness proves finite approximants actually converge to it.

## Revised missing packet

    missing_pencil_assembly:
      common_invariant_form_domain
      stable_radical_reduction
      type_a_form_family
      associated_reduced_pencil

    missing_fredholm_discreteness:
      uniform_relative_form_compactness
      or_compact_form_domain_embedding
      finite_algebraic_multiplicity_near_1

    missing_gap_isolation:
      compact_local_resolvent_annulus_around_1

    missing_completion_exactness:
      collectively_compact_or_norm_resolvent_convergence
      no_spectral_pollution
      riesz_rank_stability

The first absent constructor remains pencil assembly. The new result is that even after assembly, Fredholm discreteness is the next independent theorem, not an automatic consequence.

## Decisive next estimate

Prove on the complete source test core that the arithmetic synthesis form factors through a compact boundary embedding relative to the polarized Green graph norm, uniformly on compact parameter patches and compatibly with radical reduction.

That estimate is the first plausible bridge from typed theta boundary incidence to a genuinely finite defect complex at the generalized eigenvalue \(1\).
