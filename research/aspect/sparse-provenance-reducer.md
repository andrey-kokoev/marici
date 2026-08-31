# Sparse provenance reducer prototype

## Question

What is the smallest witness-bearing replacement for the rank-only reduction primitive used by the cosmology Rees census?

## Claim boundary

This packet constructs and checks paired sparse reduction over one finite field on a bounded toy presentation. It does not process the rank-26 matrix, extract a Rees generator, construct a connecting map, or prove a tau lift.

## Construction

A reducer state carries a pair `(module_row, provenance_row)`. The provenance row is indexed by source-relation identity. Pivot subtraction and pivot normalization act on both components with the same coefficient. If the module component becomes zero, the provenance component is a replayable dependency witness.

The prototype checks five invariants over `F_32003`:

1. each emitted dependency replays to the zero module row;
2. normalization preserves the paired relation;
3. corrupting one provenance coefficient gives a nonzero residual;
4. a toy generator not in the special relation span, whose shifted `t` image lies in the dual relation span, is certified as length one;
5. a candidate already in the special span is rejected even when its shifted image is dual-exact.

Thus the bounded length-one selector is explicit: require a nonzero special-quotient residual, a zero dual-quotient residual for the shifted generator, and a zero triple-quotient residual for its second shift. A deliberate incoherent triple presentation omitting the second-shift relation is rejected with its nonzero residual persisted.

The production interface is frozen in `research/aspect/contracts/sparse-provenance-reducer.v1.json`. It requires stable source-row identities and label digests, paired transformations, replay residuals, pivot order, and cross-prime comparison of labelled supports. The reducer emits only certified candidates and failed-residual summaries rather than its full transformation matrix.

A production-stream preflight now enumerates all 9,780 degree-eight source rows over both `F_32003` and `F_32009`. The source-version-bound identity `sha256(source_digest:raw_relations:ordinal)` agrees for every row sequence across the primes. This constructs a stable join key without changing the Benincasa generator. It is not a semantic label independent of source order: any source change invalidates the namespace and requires regeneration. Prime-specific labelled-support digests remain separate from the cross-prime identity digest.

The Python paired reducer has now processed the complete 9,780-row special presentation over `F_32003`, not merely a toy prefix. It produced 4,276 pivots and 5,504 replayable dependencies; every dependency replayed to zero. The largest provenance support had 357 source rows. Prefix runs at 1,024 and 4,096 rows were also persisted, exposing support growth from 24 to 92 to 357. This establishes that full special-layer provenance is computationally feasible.

Full dual-layer paired reduction over `F_32003` also completed: 19,560 layer rows produced 8,559 pivots and 11,001 replayable dependencies, with maximum provenance support 863. Every dependency replayed to zero. A candidate-focused replay then certified all seven shifted generators as dual-exact. Their annihilation witnesses use respectively 215, 235, 188, 182, 517, 540, and 598 dual source rows, and every equation `tg + replay(witness) = 0` checks exactly. This constructs the dual length-one cell over the first prime. Triple coherence does not require an independent full triple reduction: for every one of the 9,780 source relations, shifting the two dual rows gives exactly the first two triple rows. Therefore any coefficientwise dual annihilation witness transports to a triple witness by the index map `2*i+a -> 3*i+a` for `a=0,1`. An all-row checker verifies these identities, so each certified equation for `tg` yields an exact equation for `t^2g`. Second-prime reproduction remains separate.

Seven two-prime syzygy-image fixtures supplied from the Nima locus have passed an independent Aspect acceptance check: sidecar digests, pivot labels, support counts, and special replay certificates agree. Their source-family audit exposes the next interface obstruction. Candidates 0 and 1 use only IBP and Cayley–Menger multiplication, so they carry no principal-wall leg. Candidates 2 through 6 use all five marked families and include `g23` and `g31`. A two-prime projection-kernel calculation strengthens this individual classification to the full seven-dimensional span. The projection of candidates 2 through 6 to the extra-family coordinates `(g23,g31)` has rank five over both fields. Hence the kernel of the extra-family projection is exactly the span of candidates 0 and 1. Those two have zero `g1`, `g2`, and `g3` source support. Therefore no nonzero linear combination of the seven candidates descends to a principal-three-wall source packet by extra-family cancellation. This is a finite-cutoff statement about the materialized candidate span, not an unbounded source theorem. The fixtures also remain in the previously computed p-tangent span, so no normal quotient survivor or tau column is obtained.

A normalization audit separates two quantities that the integer-`gamma` census had conflated. Replacing integer `gamma` by its half-field value changes resolved image ranks by values in `{-1,0,1}` across the tested degrees, but normal/tangent image equality persists over both primes. Hence absolute rank growth is normalization-sensitive, while vanishing of the intrinsic normal quotient is the robust tested property. The degree-16 rank-19 prediction is restricted to integer `gamma` and must not be promoted to a normalization-independent law.

## Disposition

The paired reduction primitive is constructed and replay-checked. Scaling it to the rank-26 stream remains open because the current executable accepts rank-only records and the production Rust source belongs to the Benincasa locus. A new Aspect-owned executable or an authorized owner modification is required.

Checker: `research/aspect/checkers/check_sparse_provenance_reducer.py`

Result: `research/aspect/results/sparse_provenance_reducer.json`
