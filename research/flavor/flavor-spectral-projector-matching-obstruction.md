# The physical spectral-projector portal excludes permutation matching

Work package: WP610  
Owner: marici.Figueiredo

## Natural physical ports

On the nondegenerate `physical16` domain, let (P_i^u) and (P_j^d) be the
ordered rank-one spectral projectors of

\[
H_u=Y_uY_u^\dagger,
\qquad
H_d=Y_dY_d^\dagger.
\]

They are polynomial functions of the Hermitian Grams. Under a common-left
weak-basis transformation (Q), both projector families transform by
conjugation. Their overlap matrix

\[
W_{ij}=\operatorname{Tr}(P_i^uP_j^d)=|V_{ij}|^2
\]

is therefore weak-basis invariant. Charged-current transitions provide its
physical instrument. This is the strongest currently authorized realization
of common up/down flavor ports; it is not a texture chart or a detector-added
coordinate alignment.

## Permutation-support theorem

If (W) is a permutation matrix, each up projector has unit overlap with one
down projector and zero overlap with the other two. Rank-one positivity then
forces the paired projectors to be equal. Hence the two spectral resolutions
coincide up to permutation and

\[
[H_u,H_d]=0.
\]

All physical mixing is then trivial up to relabelling, and the Jarlskog
invariant vanishes. This applies equally to the diagonal anchor (I), the
forward permutation (P_+), or any other exact permutation support.

WP609's two relations therefore cannot be reinterpreted as two views of the
single Standard Model charged-current overlap. If either is identified with
that overlap exactly, the proposed source lies on the commuting (J=0)
stratum.

## Exact hostile and ensemble test

An exact Fourier mixing point provides a finite hostile:

\[
W_{ij}={1\over3},
\qquad
J={\sqrt3\over18}.
\]

Its Grams do not commute, and a common weak-basis rotation leaves every entry
of (W) unchanged. Thus the obstruction is physical rather than chart-level.

The complete stored fitted ensemble supplies the observed-domain test. All
1,210 sheets have (J\ne0), with minimum absolute value
(3.1413288219332114\times10^{-5}). Exact permutation matching therefore
fails on every fitted sheet.

## Classification

The spectral-projector construction succeeds as:

- a faithful weak-basis-invariant common-port coordinate;
- an experimentally typed charged-current readout;
- a direct falsifier of exact matching support.

It fails as a realization of WP609's carrier. The Standard Model supplies one
weighted overlap matrix with generic full support, not two independent support
relations (D) and (K). Creating those relations requires additional
source operations and additional mediator records.

Nima's alternating-carrier correction is separate. Eigenvalue ordering gives
stable port names on the nondegenerate stratum, but it does not dynamically
derive an alternating cubic source object that distinguishes the two
orientation orbits. Such an object must arise from the source action rather
than from ordering conventions.

## Executable falsifier

The smallest direct falsifier of permutation support is one calibrated
nonzero off-permutation charged-current overlap. Nonzero (J) is the stronger
weak-basis-invariant falsifier and already excludes the entire commuting
stratum.

Any successor architecture must leave the observed charged-current matrix
intact while adding independently resolved anchor, forward and alternating
source channels. The new channels must share the same spectral-projector port
identities and must carry their own detector calibration and temporal phase
record. Algebraically copying (W) into multiple named relations would not
provide new source operations.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp610_spectral_projector_matching_obstruction.py

The generated result is
research/flavor/results/wp610_spectral_projector_matching_obstruction.json.
