# Realization-invariant conditioning

Work package: WP555  
Owner: marici.Figueiredo

## Question

Is WP554's unweighted singular spectrum invariant under equivalent state-space
realizations of the same source resolvent?

## Similarity equivalence

Let \((A,B,c)\) realize a scalar source kernel

\[
F(z)=c(zI-A)^{-1}B.
\]

For any invertible state transformation \(T\), define

\[
A'=TAT^{-1},\qquad B'=TB,\qquad c'=cT^{-1}.
\]

Then

\[
c'(zI-A')^{-1}B'=F(z)
\]

exactly. At the six WP540 nodes the context matrix transforms as \(C'=TC\).
Its rank is unchanged, but its unweighted singular values need not be.

## Exact hostile pair

Because the WP540 context matrix is invertible, choose \(T=C^{-1}\). The
transformed context matrix is exactly \(I_6\), with spectral condition number
one. A second legal diagonal similarity that multiplies the first state
coordinate by \(10^6\) gives a condition number above \(3.4\,10^{11}\), while
the scalar transfer function and context rank remain unchanged.

Therefore WP554's raw value near \(1.27\,10^7\) is a property of the chosen
companion presentation and Euclidean state norm. It cannot by itself define a
physical resolution floor or contextual equivalence class.

## Metric repair

Let \(G\) be the admitted positive source-coordinate metric. Under the same
similarity it must transform as

\[
G'=T^{-T}GT^{-1}.
\]

Then the context Gram matrix is invariant:

\[
(TC)^TG'(TC)=C^TGC.
\]

After also whitening the observation covariance, the physically meaningful
response is metric-relative. Its singular values are invariant only when the
source and observation metrics are transported with the realization.

## Correction to WP554

WP554 correctly demanded a covariance-whitened response and declared source
norm. Its quoted unweighted condition numbers remain valid diagnostics of one
companion chart. The stronger statement that a unit source displacement is
physically lost at a \(10^{-6}\) floor is withdrawn until the source metric is
defined independently of that chart.

The smallest exact falsifier of raw-condition authority is \(T=C^{-1}\): the
same physical kernel changes from the WP554 condition number to exactly one.

## Status

WP555 is a quotient correction and invariant metric gate. It neither repairs
the missing WP542 data nor supplies a selector. Physical faithfulness requires
an experimentally typed observation covariance and a source-generated metric
or admitted displacement domain.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp555_realization_invariant_conditioning.py

The generated result is
research/flavor/results/wp555_realization_invariant_conditioning.json.
