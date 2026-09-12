# Asymptotic charges form an exact equivariant quotient on the exponential rigging

## Continuity

On finite kernel packets, use the seminorm

\[
q_1(f)=\sum_i|u_i|e^{|x_i|}.
\]

The two charges obey

\[
|q_+(f)|\le q_1(f),
\qquad
|q_-(f)|\le q_1(f).
\]

Hence

\[
\mathcal O_\infty=(q_-,q_+):\mathcal A_{\exp}\to\mathbb C^2
\]

is continuous in the projective exponential topology.

## Exact quotient

Its kernel is closed. The map is surjective: choose any \(a>0\), set \(y=e^a\), and use the two kernel states \(k_a,k_{-a}\). Their charge matrix is

\[
Q_a=
\begin{pmatrix}
y^{-1}&y\\
y&y^{-1}
\end{pmatrix},
\]

with

\[
\det Q_a=y^{-2}-y^2\ne0.
\]

Therefore

\[
0\to\ker\mathcal O_\infty
\to\mathcal A_{\exp}
\xrightarrow{\mathcal O_\infty}\mathbb C^2
\to0
\]

is a short exact sequence of topological vector spaces.

Choosing \(a\ne0\) gives a continuous finite-rank section. The quotient splits, but not canonically: the section depends on the selected displacement frame.

## Equivariance

Translation by \(b\), with \(z=e^b\), acts by

\[
(q_-,q_+)\mapsto(z^{-1}q_-,zq_+).
\]

Reflection acts by

\[
(q_-,q_+)\mapsto(q_+,q_-).
\]

Thus \(\mathcal O_\infty\) intertwines the full-line translation/reflection action with the hyperbolic residual double exactly.

## Consequence

The relation between the infinite and finite realizations is now precise:

```text
complete Green realization A_exp
→ quotient by the closed two-moment kernel
→ stationary hyperbolic residual type C²
```

The quotient is continuous and symmetry-equivariant on \(\mathcal A_{\exp}\), but not on the middle Hilbert rung \(H^1(\mathbb R)\).

The noncanonical section is the next coherence issue: different choices of \(a\) give different embeddings of the same residual double into the full Green carrier. Their comparison should be tested for contextual equivalence and possible frame dependence.

## Verification

```text
python research/coherence/check_asymptotic_charge_quotient.py
```

Artifacts:

- `check_asymptotic_charge_quotient.py`
- `asymptotic-charge-quotient.v1.json`
