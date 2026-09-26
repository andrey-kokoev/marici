# Recovered prior physical realizations: correct the programme's missing-input diagnosis

## Finding

The operator's recollection was justified. Prior research contains specific physical-source/readout constructions. A programme-wide claim that physical realization is absent would be wrong. What remains missing for the recent pilot is the precise bridge to its continued collision patch, not every physical readout.

## 1. The same graph family already has a positive-energy finite readout

`research/benincasa/source-authorized-renormalization-provenance.md`, especially its **Graph-local finiteness correction**, and `source-authorized-renormalization-completion.json` record:

- the frozen arXiv:2408.16386v2 three-site graph;
- the fixed physical loop-vector cycle Gamma_l=R^3;
- generic positive nonsoft external energies;
- the weakest four-wall density 1/(q_g1 q_g2 q_g3 q_G23);
- a common convergence strip 2<Re(d)<4 for the density and cubic normal-score tower;
- ordinary evaluation at epsilon=0 for d=3+2epsilon;
- zero graph-local UV counterterm space and identity on the rank-seven interaction quotient.

The prose explains both infinity decay and local integrability, not just a superficial statement that a triangle is UV finite. The source-authorized completion checker aggregates existing receipts; its successful status is not an independent proof of those analytic estimates.

The fixed-cycle score checker directly computes response jets. In this recovery turn we reran its two finite-field samples: response rank10 and rank11 with the constant, at both samples. These are algebraic independence controls, not numerical evaluations of an integrated physical observable or a new proof of scheme independence.

### Why this does not contradict our pole

Our candidate real collision patch has a denominator of the form

    q3=s+t-ell, ell=a+b-E>0.

It can vanish on a segment. The positive-energy source has the corresponding sum-of-norms wall with a positive external energy, so it is bounded away from zero. Taking an external energy negative while keeping a real loop cycle is not automatically the source's prescribed analytic continuation.

Moreover UV finiteness by itself would not exclude the local collision/IR pole. It is the difference of domains and wall positivity that prevents this prior finite-map result from discharging our continuation gate.

**Corrected question:** transport the already existing positive-energy readout through the actual source continuation and normalization. Do not begin by inventing a subtraction for a candidate real patch or by asserting that the source has no finite readout anywhere.

## 2. A more complete, but different, source-to-observer realization exists

`research/benincasa/source-to-observer-transfer-goal-audit.md` explicitly closes the homogeneous three-site contact objective for the declared spectral Gaussian source

    A_g=sqrt(-Delta_g).

Its retained interface is `spectral-gaussian-source-to-observer-complex.json`. It includes occurrence labels, scalar and two tensor ports, finite-q transfer, Ward/gauge/cyclic covariance, supported rank-loss cones, and completion by a direct Gaussian score port.

The direct-score matrix is

    D = [[1,2,0], [1,-1,-1], [1,-1,1]], det(D)=-6.

We freshly recomputed its inverse and its rank2/rank12 external-product determinants. The historical interface reports that tensor transfer loses rank at the existing Gram wall, while the completed observer recovers the missing data through the direct-score port. This is a concrete prior candidate for the next singular-comparison/readout test; a new abstract toy should not replace it.

Scope: this is a frozen covariant source model, not universality over all curved-metric covariantizations, not the one-loop collision patch, and not an internal identification of occurrence labels with marked-wall generators. The audit expressly excludes those stronger claims.

## 3. Action-level and tensor-vertex boundaries were also already identified

`action-level-renormalization-source-bridge.md` retains a separate action-level object R7 plus background and mass-mode directions, reduced by [I7|0|0] under declared normalization conditions. Finite nonlocal external-leg dressing remains a further source-derived map, not arbitrary scheme freedom.

`finite-q-tensor-vertex-ports.json` gives primary equation pointers in arXiv:2005.04234v3 for the local scalar-scalar-tensor vertex and both helicities. Its warning matters: this local vertex does not by itself construct the complete gravitational one-loop connection; eta weighting and Ward contact terms must still be transported.

## Programme decision

1. Reuse the existing spectral contact observer as the concrete realization for the selected structural comparison branch.
2. Reconstruct its source-derived tensor/direct-score comparison at the Gram wall and audit precisely which completion and norms the recovery uses.
3. Keep the triangle branch open but narrow its blocker to the positive-energy-to-continued-chain and normalization bridge. The physical readout is not globally absent.
4. Do not mutate Benincasa's artifacts or infer new owner adoption while he is offline.

This search is bounded, not an exhaustive census of all prior sector realizations. It already suffices to reject repeating a generic search for whether any realization exists.

## Fresh verification

Run `uv run --with sympy python research/voevodsky/project-compatibility/check_prior_physical_realizations.py`.

The plain Python environment lacks SymPy; the isolated uv environment succeeds. The audit hashes the inspected owner evidence, recomputes both modular score samples and the exact direct-score invariants, and verifies those source files are unchanged. Only our own `prior-physical-realizations.json` is written. Prior analytic/source-authority claims are identified as prior evidence, not freshly re-proved.
