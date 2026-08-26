# Heterogeneous domain selector (WP286)

## Local criterion

Let the domain energy on a finite graph be

\[
E=-\sum_{(i,j)}J_{ij}s_i s_j-\sum_i h_i s_i,
\qquad J_{ij},h_i>0.
\]

For vertex $i$, define its incident wall budget

\[
W_i=\sum_{j:(i,j)\in E(G)}J_{ij}.
\]

The worst minus-to-plus flip cost is $2(W_i-h_i)$. Therefore every minus
flip lowers energy in every configuration, and every reverse flip raises it,
if and only if

\[
h_i>W_i
\]

at every vertex. Under these inequalities, flipping remaining minus spins in
any order reaches the favored uniform state by a strictly descending path.

## Hostile weighted triangle

Take edge tensions $J_{01}=1$, $J_{12}=2$, and $J_{02}=3$. The incident
budgets are $(4,3,5)$. Biases $(3,5/2,4)$ have positive total bias but fail
the local condition at every vertex. Exhaustive evaluation shows that the
wrong uniform state remains a strict local minimum.

Thus neither total bias nor an averaged $h/J$ ratio is a faithful selector
certificate. The certificate must retain the spatially resolved source frame.

## Classification

The operation is a conditional local branch selector, not yet a selector of a
`physical16` point. Physical admission requires source-derived and jointly
calibrated $h_i$, $J_{ij}$, dynamics, uncertainties, and a branch-to-flavor
map. Treating their aggregate as sufficient would introduce the same kind of
projection kernel already excluded for measured-ten flavor coordinates.

Run `uv run --with sympy python
research/flavor/checkers/wp286_heterogeneous_domain_selector.py` to regenerate
the exact result.
