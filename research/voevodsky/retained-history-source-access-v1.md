# Retained-history source access and geometric archive update binding

Contract: `research/conjecture_net/contracts/retained-history-source-access.v1.json`.
Executable bounded reference: `research/voevodsky/checkers/check_retained_history_source_access.py`.
Receipt: `research/voevodsky/results/retained-history-source-access-v1.json`.
Run with `uv run research/voevodsky/checkers/check_retained_history_source_access.py`.

## Exactly what can be queried

A retained finite channel packet is a contribution list (n,w,seed_id,lineage), with n in Z^D, positive rational mesh h, supplied marked coordinate j, and immutable geometric seed records. Contributions remain separate even when their current coordinates collide: aggregated weights give the distribution, but aggregation is not deletion of lineage.

For an explicit tensor Gaussian test psi, the accessible bilinear observation is

    sum_terms w psi(h n).

Finite linear combinations are evaluated termwise. Gaussian widths must be positive rational; linear coefficients may be complex rational. Exact values are symbolic expressions, not certified floating approximations. On this class, Fourier, translation, modulation and nonnegative Gaussian heat transpose transport preserve Gaussian form. Finite axis convolution makes a finite sum of translated tests; coordinate relabelling permutes test factors. These supply an executable query class, not access to every arbitrary Schwartz functional or tempered input.

A history query stores the original finite packet and an ordered analytic operation word. The executor transports the final test in REVERSE chronological order, then evaluates it on that stored packet. Full Fourier is allowed in this history representation: it does not pretend Fourier of a finite atom packet is another finite atom packet. After entering that representation, packet-only mutations are rejected unless an explicit conversion is supplied. Finite sums of history queries are evaluated linearly.

This access is available because the full original packet, weights and lineage are present. Twelve-arrow coordinates and their hidden Nx archive alone do NOT supply this geometric packet or its query evaluator. No implicit oracle, archive restoration, or arbitrary infinite sum is introduced.

## Archive updates bound to channel generators

Let each contribution carry its own lineage path, and record each operation with parameters in the ordered history. Current axis/off-axis membership is recomputed relative to the current mark; no current or original off-axis data is dropped.

| Operation | Current contribution update | Archive and context update |
|---|---|---|
| Axis shift by k | n -> n+k e_j, weight unchanged | Append operation; update off-axis terms too; pull test back by physical shift -hk |
| Character multiplier alpha | w -> exp(2pi i alpha dot n) w | Retain coordinates and seed; equivalent physical modulation alpha/h |
| Full local heat t>=0 | w -> exp(-pi t h² ||n||²) w | Retain every contribution, not just axis image; multiply full test by same heat |
| Finite axis convolution a | For each term and each k, branch to n+k e_j with weight a_k w | Each child retains seed and parent path plus branch index; transpose query is sum_k a_k psi(x+hk e_j), without conjugating a_k |
| Dyadic bonding | n -> 2n, h -> h/2 | Physical positions and query values unchanged; append refinement, mark fixed |
| Relabelling sigma | n'_(sigma(i))=n_i, j'=sigma(j) | Permute coordinate metadata and tests; preserve original seed records and history |
| Full analytic Fourier | No atom-list materialization | Append to history; transpose test by full Fourier, retaining full transverse factors |

All materialized channel updates above are within the pointed-channel license. Fourier is a declared analytic history extension, not an operation newly shown native to the twelve-arrow source. Off-axis shifts remain unlicensed for this contract. Arbitrary permutations are channel-index relabellings: they are not assumed to be polygon automorphisms.

## Geometry is provenance, not invented output geometry

The fixture has a pentagon diagonal lattice (D=5), a two-diagonal triangulation incidence seed and a separately supplied axis lattice seed. The latter is not a primitive triangulation. Heat/modulation change weights; shifts and convolution can produce coordinates that are not incidence vectors of any triangulation. Original geometric seed records remain immutable. Transformed terms retain their origin and operation word, but are NOT relabelled as new triangulations.

A real polygon symmetry may separately act on the geometric record if its vertex/diagonal action is supplied and checked. Arbitrary channel permutations in this contract provide no such geometric action. Any operation requiring new geometric reconstruction or restoration therefore has an unmatched geometric cell, rather than a fabricated witness.

## Verification and remaining source-map gate

The checker tests reconstruction of the contribution partition after every generator, lineage branching, physical mesh invariance, heat/shift/convolution source-versus-query squares, simultaneous mark/query relabelling, and full Fourier followed by heat against a direct Gaussian integral. It rejects negative heat, off-axis shifts, and packet-only mutations of a history state. These are exact bounded regressions, not proof of universal computability or physical access.

This specifies and implements the previously missing bounded access policy and binds its off-axis archive updates. It does not identify the twelve-arrow native constructor with the geometric constructor. The remaining source-map obligation is now concrete: supply a shared seed constructor and a twelve-arrow/retained-history representation that actually carries these channel contribution records and evaluators, or explicitly accept a narrower source-task interface. Existing K=JP and Nx do not by themselves carry them. Keep `rh:channel-carrier-source-map` open pending that review.
