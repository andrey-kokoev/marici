# Grade-three transport is Fredholm on every Sobolev level

## 1. Functional scales

For each spin bundle, define

\[
 \|u\|_{H^s}^2=
 \sum_{l,m}(1+l(l+1))^s|u_{lm}|^2.
\]

On the compact sphere, `C^infinity` is a nuclear Frechet-Schwartz space. Its
strong dual `D'` is a nuclear DFS space. Set-theoretically every distribution
belongs to some negative Sobolev space,

\[
 \mathcal D'=\bigcup_{r>0}H^{-r},
\]

while the finite point-jet source is a much smaller strict LF subspace.

## 2. Fredholm theorem

For every real `s`, the helicity branch

\[
 \mathcal A_3:H^s(L^{2})\longrightarrow H^{s-4}(L^{4})
\]

is bounded and Fredholm. Its kernel is

\[
 \bigoplus_{l=2}^{4}\mathcal H_l^{(+2)},
 \qquad \dim_\mathbb C\ker=21.
\]

Since a spin-four target begins at `l=4` and the `l=4` multiplier vanishes,
the cokernel is

\[
 \mathcal H_4^{(+4)},
 \qquad \dim_\mathbb C\operatorname{coker}=9.
\]

Thus the complex Fredholm index of one branch is

\[
 \operatorname{ind}\mathcal A_3=21-9=12.
\]

The negative-helicity branch has the same data. On the complement of the
kernel there is a uniform elliptic estimate

\[
 \|u\|_{H^s}\leq C_s
 \|\mathcal A_3u\|_{H^{s-4}}.
\]

## 3. Regularity

Elliptic regularity gives

\[
 \operatorname{WF}(u)=\operatorname{WF}(\mathcal A_3u)
\]

microlocally away from the zero section, with the usual inclusion interpreted
through a parametrix. In particular,

\[
 \mathcal A_3u=0\quad\Longrightarrow\quad u\in C^\infty.
\]

This remains true when `u` is initially only a distribution. Hence neither
point singularities, curve conormals, nor infinite-order distributional
singularities can lie in the paired global kernel.

## 4. Threshold examples

- `delta_xi` belongs to `H^{-s}` exactly for `s>1`.
- An order-`k` point derivative needs `s>k+1`.
- A curve delta needs `s>1/2` locally.
- Every smooth `l=2,3,4` kernel mode belongs to all `H^s` and has finite
  angular energy of every Sobolev order.
- A projected ridge delta has characteristic conormal wavefront and fails
  `L2`; its smooth ridge counterpart is locally regular but cannot be compactly
  localized without an inhomogeneous boundary source.

## 5. Range and solvability

The equation `A_3 u=f` is solvable precisely when the `l=4` spin-four
coefficients of `f` vanish. The solution is unique after fixing the 21 input
low modes. This gives a canonical pseudoinverse on `l>=5`, of order `-4`.

The kernel and cokernel are therefore finite initialization data, not an
unbounded characteristic tower.

## Evidence

`checkers/grade_three_fredholm_regularity_checks.py` verifies the spectral
norm equivalence, kernel/cokernel dimensions, index, closed-range inverse,
Sobolev thresholds, and hostile high-`l` bounds.
