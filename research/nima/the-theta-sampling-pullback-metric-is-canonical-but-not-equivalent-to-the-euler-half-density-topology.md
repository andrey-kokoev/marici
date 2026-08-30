# The theta-sampling pullback metric is canonical but not equivalent to the Euler half-density topology

## Result

The Euler-to-theta incidence canonically defines a pullback metric in which the sampling map is isometric onto its range.

However, that metric is not uniformly equivalent to the pre-existing Euler half-density metric, because the sampling coefficients satisfy

\[
\eta_p\to0
\]

superexponentially.

Therefore the pullback metric closes local observer faithfulness but cannot silently replace the Euler source topology. Completion requires a two-metric correspondence or an explicitly authorized change of object.

## Diagonal incidence

Let \(\mathcal E_{\mathrm{Euler,alg}}\) be the algebraic prime-label space with basis \(e_p\), normalized in the intrinsic Euler odd coordinate.

The Euler-to-theta incidence is diagonal:

\[
S_\theta e_p
=
\eta_p e_p,
\]

where

\[
\eta_p
=
2(1-p^{-1/2})
\sum_{k\ge1}
p^{-(k-1)/2}\Phi'(k\log p)<0.
\]

Every \(\eta_p\) is nonzero, but

\[
|\eta_p|\to0
\]

superexponentially.

## Canonical pullback metric

Let the target theta-control line over each prime carry its source-fixed scalar metric. Pulling it back through \(S_\theta\) gives

\[
G_\theta
=
S_\theta^*S_\theta.
\]

On algebraic vectors,

\[
\left\|
\sum_pc_pe_p
\right\|_\theta^2
=
\sum_p|\eta_p|^2|c_p|^2.
\]

Then

\[
\|S_\theta c\|_{\mathrm{target}}
=
\|c\|_\theta.
\]

Thus the sampling map is exactly isometric from the pullback completion onto the closure of its range. This metric is source-derived: it comes from an independently constructed incidence and target metric, not from rescaling after a failed estimate.

Prime truncations remain contractive and converge strongly in this weighted completion.

## Failure of equivalence

Let the intrinsic Euler half-density metric be denoted by

\[
\|c\|_E^2
=
\sum_p w_p|c_p|^2,
\]

where \(w_p\) contains the frozen Euler/Fock half-density scale. Normalize basis vectors by

\[
u_p=w_p^{-1/2}e_p.
\]

Then

\[
\|u_p\|_E=1,
\]

while

\[
\|u_p\|_\theta
=
|\eta_p|w_p^{-1/2}.
\]

After the Euler normalization has been absorbed into the coordinate, this ratio is precisely the additional theta-sampling factor \(|\eta_p|\), which tends to zero.

Hence there is no constant \(m>0\) such that

\[
m\|c\|_E
\le
\|c\|_\theta
\]

for all finite prime packets. The inverse identity map from the theta pullback completion to the Euler completion is unbounded.

The upper comparison is harmless because \((\eta_p)\) is bounded. The lower comparison fails decisively.

## Compactness

On the Euler-normalized Hilbert direct sum, the diagonal map

\[
S_\theta=\operatorname{diag}(\eta_p)
\]

is compact because \(\eta_p\to0\).

Depending on the exact decay and target multiplicities, it lies in every Schatten class allowed by

\[
\sum_p|\eta_p|^q<\infty.
\]

Superexponential sampling gives this summability for every \(q>0\).

Thus the Euler-to-theta incidence is not a uniformly invertible comparison. It is a strongly smoothing, compact source-to-control map.

This is structurally appropriate for an incidence into a theta test packet, but it cannot carry a coercivity margin backward to the full Euler source norm.

## Categorical typing

The correct diagram contains two Hilbert or rigged objects:

\[
\mathcal E_{\mathrm{Euler}}
\xrightarrow{S_\theta}
\mathcal H_{\theta\text{-pullback}}
\xrightarrow{\cong}
\overline{\operatorname{ran}S_\theta}.
\]

The first arrow is compact and injective. The second is the isometric realization obtained after changing the source metric to the pullback metric.

Treating the composite as a unitary automorphism of one source object would erase the topology change.

Therefore the pullback metric may be used for:

- local observer normalization;
- determinant or compact-incidence analysis;
- defining the completed theta-control range.

It may not be used without further authority for:

- inverse Euler reconstruction;
- a common bi-bounded constructor frame;
- transporting global Green coercivity back to the intrinsic Euler topology;
- declaring a uniform odd margin on the original prime source.

## Consequence for the RH architecture

The odd incidence arrow now has the exact profile

\[
\text{Euler odd source}
\;\xrightarrow{\text{compact injective sampling}}\;
\text{theta scalar control}
\;\xrightarrow{\text{bounded analytic propagation}}\;
\text{Wronskian/seam-normal line}.
\]

The arrow is faithful but smoothing.

A compact injective map can identify every finite source coordinate while creating arbitrarily small singular values at completion. Therefore it cannot by itself support the earlier global demand for a cutoff-uniform observer lower bound on the entire Euler source.

There are three legitimate resolutions:

1. the global Green system needs only the theta-control completion, not inverse Euler recovery;
2. another arithmetic port jointly observes the compactly suppressed directions;
3. the source restricts the admitted Euler incidence domain to a topology already carrying the theta pullback weights.

## Next gate

The next categorical question is:

> Which object is the declared domain of the mixed Adams edge: the intrinsic Euler half-density completion, the theta-sampling pullback completion, or a graph intersection carrying both metrics?

Until that object is frozen, “uniform odd faithfulness” is ambiguous. In the intrinsic Euler topology it is false; in the pullback topology it is tautologically exact; in a graph intersection it becomes a genuine closed-range theorem.
