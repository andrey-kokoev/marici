# Implications of the six-point NMHV replication

## Question

What has the replicated identity changed in the amplitude realization programme, and what remains to be proved?

## Established consequence

For the six-point NMHV tree benchmark, positive-cell combinatorics and the source five-bracket realization produce two distinct presentations of the same color-stripped momentum-twistor function. Internal facet labels cancel in the oriented chains, the generic bosonic and super rational identities hold, and the surviving facets exhaust the source-listed physical poles.

This validates one bounded segment of the realization ladder:

\[
\text{positive-cell presentation}
\longrightarrow
\text{canonical rational form}
\longrightarrow
\text{NMHV momentum-twistor function}.
\]

The result does not validate the entire amplitude ladder. External-state preparation, loop integration, infrared treatment, and detector records are outside this theorem.

## Conceptual implication

The benchmark supports treating a BCFW expansion as a presentation of one amplitude object rather than as the object itself. Spurious poles depend on the chosen presentation; the source amplitude does not. The nine physical poles survive changes of triangulation, while the six internal facets differ between presentations.

This is evidence against a category whose objects are individual BCFW terms with equality inferred only after rational simplification. The more faithful finite structure is an oriented cellular chain equipped with a coefficient realization. Rzk-style directed composition and Cubical-Agda-style filler equality are not needed to state this benchmark.

## Residue naturality theorem

The missing naturality square is now checked. In homogeneous barycentric coordinates, use

\[
\Omega_n=\sum_i(-1)^i
\frac{d\alpha_0\wedge\cdots\widehat{d\alpha_i}\cdots\wedge d\alpha_n}
{\prod_{j\ne i}\alpha_j}.
\]

Writing the logarithmic normal `d(alpha_k)/alpha_k` last gives

\[
\operatorname{Res}_{\alpha_k=0}(\Omega_4)=(-1)^k\Omega_{F_k},
\]

which is exactly the simplicial boundary sign. The checker verifies this term by term for all 30 cell-facet incidences. Moving the normal first instead is rejected in all 30 cases, so the sign test is discriminating.

## Implication

The benchmark now exhibits an actual chain map from oriented cellular boundaries to canonical-form residues. Internal facets cancel as differential forms, not merely as labels, and the surviving residue loci are the source-matched physical poles. This establishes the local-boundary explanation for the six-point NMHV tree identity.

The result supports a cellular realization model: an oriented positive-cell chain is sent to a logarithmic differential form by a residue-compatible map. It does not establish that every amplitude identity arises from such a chain map, nor does it justify importing Rzk or Cubical Agda into this benchmark. The next scientific test must change structure rather than increase samples—for example, a non-simplicial or loop-level cell decomposition where residue compatibility can fail.
