# Six-point worldsheet universal factorization: novelty audit

## Candidate claim

Let `K` be the generic six-point kinematic field, `V_6` the 24-dimensional DDM ordering module, and `B_6` its rank-18 BCJ submodule. Let

\[
W_6:V_6\longrightarrow A_{\mathrm{SE}}
\]

send an ordering to its Parke–Taylor class in the six-point scattering-equation algebra. Then, on the Zariski-open locus where the scattering solutions are simple,

\[
\ker W_6=B_6,
\qquad
V_6/B_6\cong A_{\mathrm{SE}}.
\]

The isomorphism commutes with all stable-boundary residues of `Mbar_0,6`. Hence every `K`-linear cross-order color descent that annihilates BCJ and commutes with factorization residues factors uniquely through `W_6`.

This statement does not assert uniqueness of the worldsheet as a geometric presentation of the quotient.

## Prior-art families that directly threaten novelty

The following literature families are already known to contain most ingredients. Bibliographic metadata below are candidate locators from established amplitude literature and require external verification before citation.

1. Cachazo, He, and Yuan, *Scattering of Massless Particles in Arbitrary Dimensions* (arXiv:1307.2199 and sequels): scattering equations, Parke–Taylor factors, and Yang–Mills/biadjoint localization.
2. Cachazo, He, and Yuan, *Scattering Equations and Kawai–Lewellen–Tye Orthogonality* (arXiv:1306.6575): the `(n-3)!` solution-space rank and KLT orthogonality.
3. Mizera, *Combinatorics and Topology of Kawai–Lewellen–Tye Relations* (arXiv:1706.08527): moduli-space and twisted-cycle interpretation of KLT structures.
4. Mizera, *Scattering Amplitudes from Intersection Theory* (arXiv:1711.00469): Parke–Taylor twisted cocycles, intersection pairings, and BCJ-basis structures.
5. Arkani-Hamed, Bai, He, and Yan, *Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet* (arXiv:1711.09102): projective scattering forms, Jacobi relations, worldsheet associahedra, and factorization.

If these works already state that Parke–Taylor classes present the BCJ quotient and that boundary residues are natural, the candidate theorem is a six-point specialization and exact verification, not a novel theorem.

## Local corpus search

A repository-wide search for twisted cohomology, Parke–Taylor bases, BCJ kernels, KLT orthogonality, scattering forms, and scattering equations found no primary-source corpus adequate for comparison. The only matching local source was a talk annotation mentioning associahedral decomposition. Existing six-point source files cover Grassmannian residues and amplituhedron triangulations, not the required CHY/twisted-cohomology prior art.

## Preliminary novelty disposition

Novelty is unverified and presently unlikely. The quotient dimension `(n-3)!`, BCJ reduction, Parke–Taylor worldsheet realization, and factorization behavior are central established results. Recasting their six-point instance as a universal property may be new wording without new mathematical content.

A defensible new result would need at least one distinction absent from the cited families:

- a categorical initiality theorem for residue-compatible descent, with an explicitly defined category of admissible realizations;
- a proof that every such realization factors naturally through the scattering-equation algebra, rather than merely through an abstract isomorphic quotient;
- a new obstruction or minimality theorem comparing amplituhedron chains with worldsheet classes.

The current computation proves a finite/generic six-point presentation and complete boundary audit. It does not yet establish categorical initiality among competing geometric realizations.

## External search performed

With operator authorization for shell web search, the arXiv API and INSPIRE API were queried for combinations of `Parke-Taylor`, `BCJ`, `twisted cohomology`, `scattering equations`, `boundary divisors`, and `factorization`. Exact arXiv metadata was verified for 1306.6575, 1307.2199, 1706.08527, 1711.00469, and 1711.09102. Full-text keyword inspection was performed on 1706.08527 and 1711.09102.

The search found no title or abstract stating the exact phrase “universal residue-compatible quotient.” That absence does not establish novelty. The full text of 1711.09102 explicitly joins all substantive ingredients: the worldsheet Parke–Taylor form, its pushforward to kinematic scattering forms, BCJ color–kinematics structure, and factorizing boundaries. The full text of 1706.08527 treats a BCJ-sized basis, worldsheet moduli, twisted period relations, and factorization channels. Papers 1306.6575 and 1711.00469 supply the `(n-3)!` rank/perfect-pairing mechanism underlying quotient factorization.

## Search for a publishable residual

A second search queried arXiv for Parke–Taylor residues, scattering-form pushforwards, stable curves, BCJ cohomology bases, operadic structures, and amplituhedron/worldsheet comparisons. The closest additional source is Arkani-Hamed, Bai, He, and Yan, *Scattering Forms, Worldsheet Forms and Amplitudes from Subspaces* (arXiv:1803.11302). Its abstract states a general construction from arbitrary `(n-3)`-dimensional kinematic subspaces and proves that scattering-equation pushforward sends the corresponding worldsheet forms to scattering forms. Its full text contains BCJ, factorization, residue, and boundary analyses. This removes the pushforward/factorization formulation as a plausible novelty gap.

The search leaves three differentiated residuals:

1. **Not publishable alone:** the exact six-point rank and boundary census. It is a reproducibility result for established general theorems.
2. **Potentially publishable if proved:** a nonexistence theorem showing that a specified amplituhedron/Grassmannian cross-order residue carrier cannot admit a residue-natural comparison to the BCJ/worldsheet quotient. The theorem must name the carrier, admissible maps, and an invariant obstruction; the current simplex counterexample is only one failed presentation.
3. **Potentially publishable if constructed:** an explicit chain-level comparison from six-point NMHV Grassmannian residue classes to twisted cohomology that intertwines all boundary maps and explains the BCJ quotient. Searches for `amplituhedron + scattering equations`, `amplituhedron + worldsheet + color`, and `positive Grassmannian + Parke-Taylor + BCJ` returned no directly matching construction beyond broad reviews and arXiv:1711.09102. Absence from these queries is not priority proof.

The strongest next novelty test is therefore not another quotient computation. Define the source residue complex and target twisted de Rham complex, then test whether the known six-point cross-order map lifts to a chain map. A proved obstruction or a nontrivial lift would differ from the pushforward theorem of arXiv:1803.11302. Failure to define the source complex canonically stops the branch.

## Novelty verdict

The broad mathematical claim is not novel enough to advertise as a new theorem: its kernel/rank, worldsheet realization, and factorization components are established, and the universal factorization through a quotient follows formally once the kernel equality is known. The exact six-point exhaustive boundary audit appears to be a new computation relative to the searched papers, but it verifies a known general structure rather than introducing one.

A potentially novel claim remains unverified: initiality of the scattering-equation algebra in a precisely defined category containing competing cross-order geometric carriers, with morphisms required to preserve every stable residue. The present theorem does not prove that stronger statement because factorization through an abstract quotient is invariant under non-worldsheet presentations. An arXiv draft should therefore be framed as a computational audit or should first prove this stronger categorical comparison theorem.
