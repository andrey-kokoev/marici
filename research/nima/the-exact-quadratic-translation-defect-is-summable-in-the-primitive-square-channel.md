# The exact quadratic translation defect is summable in the primitive-square channel

## Gaussian source seed

Let

\[
f_0(x)=e^{-\pi x^2},
\qquad
f_j(x)=x^jf_0(x).
\]

The two derivative terms in the exact translation defect are

\[
(A+1)Df_0
=
-4\pi f_1+4\pi^2f_3,
\]

and

\[
D^2f_0
=
-2\pi f_0+4\pi^2f_2.
\]

Hence both have fixed finite \(L^2(\mathbb R_+)\) norms. Write

\[
C_1=2\|(A+1)Df_0\|,
\qquad
C_2=\|D^2f_0\|.
\]

These constants are independent of the prime.

Their values can be expressed exactly from

\[
\langle f_j,f_k\rangle
=
\frac12
(2\pi)^{-(j+k+1)/2}
\Gamma\left(\frac{j+k+1}{2}\right).
\]

No asymptotic estimate is needed locally.

## Prime defect bound

For \(L=\log p\),

\[
\mathcal R_p
=
U_L
\left[
-2L(A+1)D+L^2D^2
\right].
\]

Since \(U_L\) is unitary in the comoving ray frame,

\[
\|\mathcal R_pf_0\|
\le
C_1\log p+C_2(\log p)^2.
\]

Thus the exact finite-transport correction costs only a quadratic logarithm.

## Arithmetic mixed weight

The primitive and square endpoint coefficients are

\[
p^{-1/2-\sigma-it},
\qquad
\frac12p^{-1-2it}.
\]

Their product has magnitude

\[
\frac12p^{-3/2-\sigma}.
\]

Therefore the diagonal mixed series is dominated by

\[
\frac12
\sum_p
p^{-3/2-\sigma}
\left[
C_1\log p+C_2(\log p)^2
\right].
\]

This converges absolutely at \(\sigma=0\), hence uniformly for
\(\sigma\ge0\) on the seam-closed diagonal channel.

## Consequence

The new \((\log p)^2D^2\) term does not reopen the primitive seam
divergence in the mixed Adams block. The square endpoint contributes the
extra factor \(p^{-1}\), and every fixed logarithmic power remains
summable against \(p^{-3/2}\).

Thus prime-weighted assembly of the exact one-label Gaussian defect is
analytically closed, conditional only on exact prime diagonality and the
source incidence using these frozen endpoint coefficients.

## Theta-label transport

Under half-density transport,

\[
D\longmapsto n^{-1}T^{(1)},
\qquad
D^2\longmapsto n^{-2}T^{(2)}.
\]

Hence the second-order defect is additionally suppressed by \(n^{-2}\) in
theta label. Any standard theta Gaussian weight makes the label sum
absolutely convergent on the source seed.

The first-order term has only \(n^{-1}\), but the theta exponential decay
still dominates it.

## Cutoff naturality

For a finite prime cutoff \(X\), define

\[
B_X
=
\bigoplus_{p\le X}
\frac12p^{-3/2-\sigma}
\mathcal R_p
\]

on the prime-diagonal source packet. Absolute convergence implies

\[
B_X\to B
\]

in operator norm on the one-seed direct sum, and

\[
B_Y|_X=B_X
\qquad
(X\le Y).
\]

Therefore the exact local defects form a cutoff-compatible completed mixed
operator.

## Scope qualification

This theorem controls the source Gaussian seed and its declared finite
endpoint packet. It does not prove uniform bounds on the entire infinite
cyclic completion. A general vector can carry high polynomial grade whose
\(D^2\) norm grows.

The full theorem needs either:

- a weighted cyclic graph norm making the same bound uniform;
- a Hilbert--Schmidt estimate after theta label synthesis;
- or a rigged-form completion.

## Cross-prime qualification

The norm convergence above uses exact prime diagonality. If the bulk
incidence mixes distinct primes, the one-index summability estimate is
insufficient and a two-index Schur bound is required.

## Frontier

For the actual primitive-square source seed, both new analytic costs are now
harmless:

\[
(\log p)^2
\quad\text{and}\quad
n^{-2}.
\]

The remaining quadratic Green theorem is local to each prime and concerns
form identification and radical descent, not divergence of the exact
translation defect.
