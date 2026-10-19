# Nonparallel patterns in the source spin loom

## Question, boundary and disposition

The source-derived loom is coherently curved but has no globally parallel spinor
on a triangular loop. Which nonparallel patterns does its ALREADY DECLARED
squared seam-mismatch functional support?

This changes the question, not the failed zero-mismatch result. We reuse
H=C* C from the prior spin-interface constructor, with equal seam weights and
unit total norm. No new energy weight, physical scale or admissibility threshold
is fitted. A positive minimum cost is not a proof that a configuration is
forbidden. Execution disposition is under `results/nonparallel-spin-loom/`.

Scope: existing five-cell geometric spin interface, both chiralities, not a
unified native P/N/E comparison law or molecular model. Obligation: forward
realization of a source quadratic form and exact spectral/attachment covariance.

## Frozen finite test

Use the regenerated, source-pinned fold matrices from the source-spin-loom
receipt. Validate every transitive source hash before accepting them. For every
nonempty subset of the five available fittings, include every internal seam
and form the ACTUAL mismatch matrix C with rows s_j-U_ij s_i. There are 31
subsets per chirality, 62 cases in total. No matrix or face sign is fitted.

For kappa=sqrt(6)/3, the predicted minimum and its multiplicity are:

| Number of fittings, complete seam graph | Minimum mismatch | Multiplicity |
|---|---|---:|
| 1 | 0 | 2 |
| 2 | 0 | 2 |
| 3 | 1-kappa | 2 |
| 4 | 3-3kappa | 2 |
| 5 | 4-3kappa | 4 |

The full spectra are frozen in the fixture. Construct every exact spectral
projector by polynomial functional calculus. Verify orthogonal idempotence,
Hermiticity, eigenvalue equations, multiplicities and completeness. Explicitly
export a nonzero lowest-mode pattern and all of its seam mismatch vectors;
verify its Rayleigh cost directly from those vectors.

Positive roots imply 4/5<kappa<5/6 (compare their squares with 2/3). This proves
the stated eigenvalue ordering and nonnegative lower bounds; decimals are not
used to certify a minimum.

For the full group, regenerate the inherited constant rank-two projector C0
and complementary rank-two B=P_low-C0. Verify they are orthogonal subspaces of
the SAME lowest eigenspace. Recover their two-column isometric encodings from
the source attachment cell and export actual patterns in both sectors. Every
cell receives a faithful scaled two-component encoding in either doublet.
There is no selected unique doublet or pattern.

Conjugate the whole five-cell problem by the source-rooted independent unitary
fitting frames. Rebuild the seam form from changed edges and compare it with
the conjugated form. Retain the transported ground modes; cost is frame
invariant, while apparent twisting of coordinate components is not.

## DPC at the explanatory boundary

1. Problem: excluding all globally parallel states did not exclude coherent
   nonparallel patterns. A flatness test could manufacture a hard construction
   limit that the source functional does not support.
2. Candidate: the inherited mismatch rule supports explicit least-cost nonparallel
   patterns on all available fitting groups, with the frozen spectra above.
3. Rivals: closure eliminates every pattern; a positive mismatch is automatically
   forbidden; the rule selects one doublet; five input cells establish a physical
   size limit; coordinate twisting is a gauge-invariant observable.
4. Risk: verify ALL source subsets and both chiralities against the predicted
   spectral projectors, preserve seam-level residuals, and expose degeneracy.
5. Strongest test: full exact spectral decomposition, direct vector mismatch
   costs, transitive source pins, independent-frame covariance and retention of
   both full-group doublets. Any failed spectral identity rejects this finite
   realization; do not tune seam weights to rescue it.
6. Disposition criterion: nonzero ground projectors demonstrate surviving
   nonparallel patterns, not bound molecules. Positive cost does not give a size
   limit without an independently supplied occupation/threshold or stability law.

## Reproduce and stopping boundary

    python research/aspect/scc/scc.py check nonparallel-spin-loom-v1 --verbose

The checker uses exact native algebraic arithmetic and writes all operators,
projectors, representative patterns and seam residuals. No stored shared source
receipt is rewritten. Extending beyond the input five-cell geometry or deriving
real-world limits requires new source geometry, native interfaces and a physical
selection law; these are recorded boundaries, not waiting-only successor tasks.
