# Smooth prime synthesis lands in the Mellin–de Rham graph domain

## Question

Does the arithmetic rapid-decay test carrier map continuously into the common
graph domain that controls both Fourier leakage directions?

## Constructor order

The atomic incidence

\[
(p,k)\longmapsto \frac1k p^{-k/2}\delta_{k\log p}
\]

lands in a distribution space. It cannot be differentiated as an \(L^2\)
state. Therefore the de Rham graph operator must not be applied directly to
the atomic current.

The correctly typed order is:

```text
prime-labelled test packet
    -> smooth theta synthesis
    -> Mellin/de Rham graph domain
    -> boundary currents by duality
```

## Smooth synthesis theorem

Let \(L_p=\log p\), let \(\tau_L\Phi(q)=\Phi(q-L)\), and define on finite
prime packets

\[
Kc=\sum_p c_p\tau_{L_p}\Phi.
\]

Assume

\[
\Phi\in H^1(\mathbb R),
\qquad
Q\Phi\in L^2(\mathbb R).
\]

Then

\[
\lVert DKc\rVert_2
\le \lVert D\Phi\rVert_2\sum_p|c_p|,
\]

and the translation identity

\[
Q\tau_{L_p}\Phi
=\tau_{L_p}(Q\Phi)+L_p\tau_{L_p}\Phi
\]

gives

\[
\lVert QKc\rVert_2
\le
\sum_p|c_p|
\left(\lVert Q\Phi\rVert_2+L_p\lVert\Phi\rVert_2\right).
\]

For every \(\delta>1/2\), Cauchy–Schwarz against

\[
q_\delta(c)^2=\sum_p p^{2\delta}|c_p|^2
\]

bounds both right-hand sides because

\[
\sum_p p^{-2\delta}(1+\log p)^2<\infty.
\]

Therefore \(K\) extends continuously from the arithmetic rapid-decay test
space into \(\operatorname{Dom}Q\cap\operatorname{Dom}D\) with its graph
topology.

## What this achieves

The arithmetic pro-Gram carrier does exclude the bare translated-packet
hostile after smooth source synthesis. Large prime translation incurs the
correct logarithmic position cost, while source smoothness supplies the
derivative cost.

This constructs the previously missing positive arrow at test-state level:

\[
\mathcal S_{\mathbb P}
\longrightarrow
\operatorname{Dom}Q\cap\operatorname{Dom}D.
\]

It also explains why the atomic current and the analytic state must remain
distinct presentations of one labelled source operation.

## Remaining boundary

The primitive and square arithmetic currents live in the continuous dual of
the test rigging, not in its state space. The theorem does not apply \(Q\) or
\(D\) to those currents as vectors. The next gate is extension by duality to a
common graph correspondence carrying:

- primitive and square covectors;
- seam and endpoint traces;
- reciprocal sewing;
- the completed zero-state domain.

Failure of transpose continuity for any one of those rows blocks the lift.

## Verification

The checker `check_smooth_prime_synthesis_graph_bound.py` verifies the exact
finite weighted Cauchy–Schwarz domination for derivative and position rows on
a prime-labelled fixture, including a hostile deletion of the logarithmic
position weight.

