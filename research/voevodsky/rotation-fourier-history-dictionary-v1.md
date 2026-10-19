# Two distinct ticks on the shared-seed retained-history extension

Contract: `research/conjecture_net/contracts/rotation-fourier-history-dictionary.v1.json`.
Checker: `research/voevodsky/checkers/check_rotation_fourier_history_dictionary.py`.
Receipt: `research/voevodsky/results/rotation-fourier-history-dictionary-v1.json`.
Run: `uv run research/voevodsky/checkers/check_rotation_fourier_history_dictionary.py`.

## Frozen generator dictionary

Start from either shared framed-quadrilateral triangulation, its supplied mark and mesh, full seed carrier and decoded packet. Keep the original geometric seed immutable. Maintain two distinct current-state records: a native carrier C12^r x_seed and an analytic channel history W delta_(h v_seed). A chronological record states which generators were used; the carrier alone is not claimed to summarize W.

R is native geometric rotation: it applies C12 to the current carrier and swaps the two diagonal coordinates in the channel state, moving the mark simultaneously. F is separately supplied full additive Fourier on the channel history; it leaves the native carrier unchanged and records the analytic step. Positive isotropic H and marked translation T are licensed channel operations, not derived native carrier controls. They also leave the native carrier record unchanged. Hence the current carrier may no longer encode the current analytic channel state; it records native rotations of the seed, while the retained seed plus W supplies analytic queries.

This is an explicit history extension, not a covert assertion that C12 implements every operation. On the initial seed image R agrees through both geometric maps as previously checked. For subsequent analytic histories, the record distinguishes geometric provenance from the current distribution.

## Composition, mark and query law

Full Fourier and isotropic heat commute with coordinate permutation R. Marked translations must move their axis under R. When recording T, store the CURRENT coordinate index, not merely the initial mark. Reverse query transport uses that stored index and negates the translation parameter. R's test transpose is the inverse coordinate permutation (the same swap in this quadrilateral case); F and H use the bilinear transposes already specified.

Carrier rotation has order four; its action on the two diagonal coordinates has order two. Fourier has order four on general analytic states. Coinciding order bounds do not identify these operators. R F=F R is a commuting two-generator relation, not R=F.

For any finite word, query the terminal analytic state by transporting its final test backwards and evaluating on the full retained seed packet. The general equality follows from the transpose composition law. The checker tests all 84 words of lengths one through three in R,F,H,T on unequal Gaussian coordinate states/tests, verifies the commuting relations and rejects a frozen marked axis. Gaussian regressions do not prove arbitrary-domain access or native implementability.

An independent shared-seed atom hostile makes conflation visible: use delta_(h,0), h=1/3, and test exp(-pi x²-2pi y²). R gives exp(-2pi h²). F gives exp(-pi h²)/sqrt(2). These differ. Thus executing R when an analytic Fourier query was requested is detectably wrong even at the common geometric seed.

## Scoped disposition

Constructed: an explicitly declared two-tick history dictionary and ordered observer protocol on the bounded shared seed, with native versus added generators separated. Unmatched: native implementations of the analytic/channel generators, general polygon construction and physical access. No live parent verdict is changed.

The next decision is scope acceptance: is a native geometric seed plus added analytic/channel history sufficient for the intended bounded source task, or must all generators be native to one original constructor? Under the latter requirement this result remains a partial binding, not a completed source map. This decision must precede further declarations that merely add more operations by definition.
