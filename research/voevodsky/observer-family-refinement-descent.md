# Observer-family refinement descent

## Question

Do the rank, mesh, and base-point observer families merely report to the all-rank cone, or do they carry exact observation maps between one another?

## Claim boundary

There is a nontrivial one-way mesh-refinement map compatible with rank restriction and base-point translation. It lets sufficiently many shifted fine-mesh observers certify a coarse-mesh observer. It does not provide the reverse arrow or all-rank uniformity.

## Three observer operations

For

\[
d_q(t,\delta)
=
H(t+q\delta)-H(t+(q+1)\delta),
\]

define the fine-mesh Hankel observer

\[
D_M(t,\delta)
=
(d_{i+j}(t,\delta))_{i,j<M}.
\]

The three operations are:

1. rank restriction by principal compression;
2. base-point translation \(t\mapsto t+r\delta\);
3. mesh coarsening \(\delta\mapsto h=m\delta\).

## Telescoping arrow

For the coarse difference,

\[
\begin{aligned}
b_n(t,h)
&=H(t+nh)-H(t+(n+1)h)\\
&=\sum_{r=0}^{m-1}
d_{mn+r}(t,\delta).
\end{aligned}
\]

Therefore

\[
B_N(t,m\delta)
=
\sum_{r=0}^{m-1}
\left(d_{m(i+j)+r}(t,\delta)ight)_{i,j<N}.
\]

For each \(r\), the summand is the principal compression indexed by

\[
0,m,2m,\ldots,(N-1)m
\]

of the shifted fine observer

\[
D_{m(N-1)+1}(t+r\delta,\delta).
\]

Consequently,

\[
D_{m(N-1)+1}(t+r\delta,\delta)\geq0
\quad
(0\leq r<m)
\]

implies

\[
B_N(t,m\delta)\geq0.
\]

This is an exact observation map from a finite family of shifted fine observers to one coarse observer.

## Coherence

Rank restriction commutes with this construction because all maps are principal compressions. Base-point translation by one coarse step equals translation by \(m\) fine steps. Successive refinements by \(m_1\) and \(m_2\) telescope to the same map as refinement by \(m_1m_2\).

Thus the lower observers form a directed refinement system rather than an unrelated list.

## What it buys

A positivity theorem on a fine mesh and all its first \(m\) shifts propagates automatically to the coarser mesh. One does not need to prove the coarse inequality independently.

This may connect the fixed-rank small-heat theorem to a larger parameter region if its positivity neighborhood contains every shifted fine observer required by the telescoping formula.

## What remains missing

The arrows are one-way:

\[
\text{shifted fine positivity}
\Longrightarrow
\text{coarse positivity}.
\]

Coarse positivity does not reconstruct the fine observers. Moreover, the current small-heat theorem gives a threshold depending on \(N\) and \(\kappa=h/t\). Refinement increases the fine rank to \(m(N-1)+1\) and changes the scaled mesh at every shifted base point. Without quantitative threshold control, the descent arrow does not yet enlarge the proved region.

## Disposition

The operator intuition identifies a real structure: rank, mesh, and translation observers do observe one another through coherent compression and telescoping maps. The first executable test is whether the known small-heat thresholds survive the rank inflation and shifted ratios required by refinement descent.

## Verification

- `research/voevodsky/checkers/check_observer_family_refinement_descent.py`
- `research/voevodsky/results/observer_family_refinement_descent.json`
