# The order–Mellin commutator is a source-positive domain candidate for prime cancellation

## Question

Does prior Marici research contain a positive arithmetic topology that is neither the zero-derived Hardy norm nor the target Weil form?

## Claim boundary

Yes, at every finite prime-label cutoff. The order–Mellin commutator gives a strict positive norm on conductor-dark coefficient directions and the Mellin jet tower detects every finite complement. This supplies a noncircular candidate domain for prime cancellation. No existing packet proves that the completed prime quadratic form is lower-bounded in this norm or that the finite norms have a radial limit.

## Source-positive finite norm

For distinct logarithmic labels

\[
\lambda_i=\log n_i,
\]

let

\[
\Lambda_{ij}=\lambda_i\delta_{ij},
\qquad
S_{ij}=\operatorname{sgn}(\lambda_j-\lambda_i).
\]

On the zero-sum subspace,

\[
\langle c,[\Lambda,S]c\rangle
=-\sum_{i,j}\overline{c_i}c_j|\lambda_i-\lambda_j|
=2\int_{\mathbb R}
\left|\sum_{\lambda_i>u}c_i\right|^2du>0
\]

for nonzero `c`. If `E` is conditional expectation onto finite conductor fibers, this is strictly positive on `ker E`.

Unlike the Hardy realization, these objects are defined from ordered arithmetic labels before zeros enter.

## Completeness at finite cutoff

Prior Mellin-jet research proves that

\[
(1-E)\Lambda^kE,
\qquad k\ge1,
\]

generates every finite conductor complement when labels inside each fiber are distinct. Nested conductors such as `(N+1)!` make the finite character lifts compatible under refinement. Thus no finite coefficient direction is invisible to the combined conductor and Mellin instruments.

## Possible connection to the present form

The cumulative-sum realization suggests a source Hilbert space

\[
\mathcal H_{\mathrm{ord}}
=\overline{\{c:\sum c_i=0\}}
^{\|c\|_{\mathrm{ord}}},
\]

with

\[
\|c\|_{\mathrm{ord}}^2
=2\int\left|\sum_{\lambda_i>u}c_i\right|^2du.
\]

A viable prime-form route would construct, for each heat polynomial `p`, a source coefficient packet `c_(t,h,p)` from the von Mangoldt labels and prove

\[
\mathcal Q_{\Gamma+P}(t,h;p)
\ge -C_{t,h}\|c_{t,h,p}\|_{\mathrm{ord}}^2,
\]

followed by a comparison of the order norm with a positive archimedean reference form strong enough to give the required lower bound.

The cumulative-sum norm retains cancellation across labels, so it avoids the divergent termwise total-variation estimate.

## Conductor-corona obstruction

Two earlier completion packets already block the ordinary Hilbert-limit version of this proposal. Square-normalized Ramanujan energy retains a unit fluctuation state that escapes every fixed conductor observer, while its ordinary square covariance diverges. The limiting multiplicative Haar presentation is globally singular with respect to additive Haar even though every finite-level Radon–Nikodym comparison exists.

Therefore finite commutator positivity and nested-conductor compatibility do not produce an ordinary radial Hilbert completion. The existing corona completion also fails the present need: its GNS representation retains every fixed Mellin shift but the representation is discontinuous in the shift parameter, so the unbounded generator `Q e_p=(log p)e_p` does not exist there. The order–Mellin commutator and Mellin jets require precisely this lost first-order germ. Moreover, the source-derived relative corona complex is split exact and its cancellation is universal, so it has no zero-selection force.

Any surviving construction must therefore add a differentiable corona boundary channel, not merely the existing Haar corona, and prove how the completed prime form acts on it. The canonical finite-level Hellinger coupling does not supply that channel: for squarefree `Q`, its affinity is

\[
A_Q=\prod_{p\mid Q}\sqrt{1-p^{-1}},
\]

which tends to zero along conductors exhausting the primes. Thus the unrenormalized square-root density embeddings become orthogonal and yield no nonzero bulk–corona cross block. Any renormalization would need independent source authority and control of its divergent scale.

## Exact missing arrows

Four constructions are absent:

1. a canonical map from the infinite von Mangoldt heat packet to the zero-sum conductor complement;
2. convergence of its cumulative sums in the order norm;
3. compatibility of the finite commutator norms under conductor refinement in the radial Hilbert topology;
4. a lower-bound comparison with the completed gamma–prime form.

Finite faithfulness does not prove any of these limits.

## Strongest falsification attempt

The commutator is universal for any distinct ordered labels and therefore contains no theta-specific positivity by itself. It may control only generic label variation while missing the completed prime weights and gamma normalization. If the natural von Mangoldt packets fail to have finite order norm, or if the comparison constant grows without bound under refinement, this route closes.

## Disposition

The ordinary nested-conductor Hilbert-limit route is blocked by corona escape and additive/multiplicative Haar singularity. The existing Haar-corona completion is also blocked because it destroys the Mellin generator, while the relative corona complex is universally split exact. Finite order-norm tests may diagnose escape but cannot establish an infinite source factor. Reopen only with a source-derived differentiable corona channel, a von Mangoldt heat-packet map into it, and a completed-form lower bound including that channel.