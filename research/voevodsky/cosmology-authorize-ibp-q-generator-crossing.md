# IBP and q generator ownership crossing

## Question

Is there durable authority to modify the visible IBP and q seed generators?

## Evidence

Fresh exact-path Git queries returned zero commits for both files. Git status classified each as untracked:

- `research/voevodsky/check_cosmology_IBP_corrected_transport_exact_seeds.py`, SHA-256 `99d1de5ff5a5f528c8f598a89583d8bdc3e41508e6232b6223cb8a19e8f61352`;
- `research/voevodsky/check_cosmology_q_exact_seeds.py`, SHA-256 `e107ac04539cf9981c91684f0e2d252960ed35907cb3f5adc9c5b42f1e7ff6cc`.

The earlier provenance statement that all three generators were tracked was false: the wildcard history match came from the nonmarked-K generator. The provenance packet and checker result were repaired and re-executed successfully.

No owner attribution or explicit cross-locus grant is materialized for the two untracked files. Visibility, compatible content, and use by existing results do not transfer mutation authority.

## Disposition

The crossing is denied. The files remain untouched. To avoid blocking algebraic recovery, construct independently owned certified IBP and q generators from the tracked shared raw-relation, DAG, exact-lift, and solver interfaces, and compare their outputs against the immutable existing summaries.

## Scope

This decision concerns mutation authority only. It neither discredits the existing numerical summaries nor certifies the visible untracked generators.
