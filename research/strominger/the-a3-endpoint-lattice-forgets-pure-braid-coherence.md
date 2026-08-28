# The A3 Endpoint Lattice Forgets Pure-Braid Coherence

## Question

Does the \(A_3/S_4\) zero packet remain complete when the four zero positions
vary through configuration space?

## Endpoint projection

In a disk chart containing the four zeros, configuration paths form the Artin
braid group \(B_4\). Forgetting the path and retaining only the endpoint
relabeling gives

\[
B_4\longrightarrow S_4.
\]

The \(A_3\) redistribution lattice sees the subsequent Weyl action of
\(S_4\). Therefore its path action factors as

\[
B_4\longrightarrow S_4\longrightarrow GL(A_3).
\]

This factorization kills every pure braid.

## Smallest hostile

The word \(\sigma_1^2\) has identity endpoint permutation and acts identically
on \(A_3\), because the Weyl image of \(\sigma_1\) is an involution. But
\(\sigma_1^2\) is not the identity braid. Its exponent sum is two, whereas the
identity has exponent sum zero.

Thus the identity path and a nontrivial pure braid are indistinguishable to
both endpoint labels and all three \(A_3\) period coordinates.

## Required higher witness

Path coherence requires a dependent record such as

```text
BraidWitness
  configuration_path_class
  Artin_word
  endpoint_permutation
  pure_braid_class
  attachment_holonomy
```

For four local strands, the abelianization of pure-braid information has six
pairwise winding coordinates, one for each unordered pair. These six
coordinates do not classify the full nonabelian pure braid group, but they are
already strictly richer than the three static \(A_3\) coordinates.

## Relation to the 3+2+1 apparatus

Aspect's \(3+2+1\) instrument counts the static defect periods, phase
quadratures, and direct source ray. The present theorem does not identify its
six ports with the six pairwise braid windings. It predicts that static
faithfulness does not automatically imply configuration-path faithfulness.
Any such identification requires an explicit source-derived path-holonomy
map.

## Claim boundary

The theorem is local to a disk chart. Global motion on \(S^2\) obeys additional
spherical braid relations and requires a separate global presentation. The
pure-braid hostile already exists locally, so those extra relations cannot be
ignored when globalizing.

## Disposition

The \(A_3\) lattice closes static redistribution but not coherence among
redistribution presentations. The next level is a braid or path-holonomy
witness above the endpoint Weyl action.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/pure_braid_a3_coherence_checks.py
```
