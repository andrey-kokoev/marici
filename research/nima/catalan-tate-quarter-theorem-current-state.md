# Catalan–Tate quarter theorem: current state

## Theorem

Let `n` be divisible by four and let `H_n` be the complex vector space on triangulations of the labelled `n`-gon.

### A. Intrinsic Catalan quarter

Quarter-polygon rotation defines `q_n^4=1`. Its character projectors satisfy

\[
\frac{\dim H_n^{(j)}}{\dim H_n}\longrightarrow\frac14
\qquad (j=0,1,2,3).
\]

More precisely,

\[
\dim H_n^{(0)}=\dim H_n^{(2)}
=\frac14\left(C_{n-2}+\binom{n-2}{(n-2)/2}\right),
\]

\[
\dim H_n^{(1)}=\dim H_n^{(3)}
=\frac14\left(C_{n-2}-\binom{n-2}{(n-2)/2}\right).
\]

The forced-channel projection has normalized trace

\[
\frac{C_{n-3}}{C_{n-2}}
=\frac{n-1}{2(2n-5)}
\longrightarrow\frac14.
\]

### B. Canonical Tate-torus realization

For the diagonal set `D_n`, define

\[
L_n=\mathbb Z^{D_n},
\qquad \mathbb T_n=\operatorname{Hom}(L_n,U(1)).
\]

A triangulation maps to its incidence atom

\[
T\longmapsto\delta_{v_T},
\qquad v_T=\sum_{d\in T}e_d.
\]

This map is injective and sends compatible channel union to convolution. Pontryagin Fourier transport gives

\[
\delta_{v_T}\to\chi_{-v_T}\to\delta_{-v_T}
\to\chi_{v_T}\to\delta_{v_T}.
\]

The graded chart lift satisfies

\[
\widetilde{\mathcal F}^{\,4}=\Sigma.
\]

### C. Full seventh-edgewise-subdivision realization

The source manifest contains every nondegenerate cell of `esd_7(Delta^3)`:

\[
(f_0,f_1,f_2,f_3)=(120,560,784,343).
\]

For each simplex `sigma`, set

\[
\mathfrak R(\sigma)
=N_*\mathbb C[\sigma]\widehat\otimes V.
\]

The source-recorded Freudenthal increment flags provide cone triangles and canonical octahedra. Rotation and reciprocal reversal act as signed chain maps. This is a coherent bounded cone-valued indexing model on the full finite source. Its simplex-face cones are contractible, so it does not recover the nonzero kernel/cokernel defects of the historical graph-domain packages.

### D. Regulator-independent quarter trace

For any positive trace-class regulator `R` transported by chart conjugacy,

\[
R_i=W^iRW^{-i},
\]

the four chart projections satisfy

\[
\frac{\operatorname{Tr}(P_iR_{tot})}
{\operatorname{Tr}(R_{tot})}=\frac14.
\]

For any radial channel regulator `f(N)`, the restriction to `H_n` is scalar because

\[
\lVert v_T\rVert^2=n-3.
\]

Therefore the normalized forced-channel and character traces equal their unregularized finite-rank ratios. Their quarter limits are regulator-independent.

## Proven interfaces

- exact Catalan ratio and limit;
- exact polygon-rotation character multiplicities;
- injective channel-incidence realization;
- convolution/pointwise Fourier chart cycle;
- canonical channel lattice and dual torus;
- graded fourth-power suspension;
- complete `esd_7` cell manifest with signed `rho` and `omega` actions;
- bounded closed-package cone and octahedral indexing for the all-cell profile, with acyclic simplex-face cones;
- heat-trace and general conjugacy-invariant quarter formulas.

## Scope

The exact chart quarter and the asymptotic Catalan quarter are different statements joined by one realization framework. The first follows from four transported chart copies. The second follows from Catalan counting and vanishing normalized nonidentity rotation traces.

The canonical Catalan/channel model has an ordinary positive Hilbert realization on alternating `ell2(Z^D)` and `L2(T^D)` charts, with unitary Pontryagin transport and positive Hilbert cone norms. Historical raw eight-leg convergence and positivity of the signed Weil/Tate form remain separate arithmetic questions.

The normalized quarter requires no spectral equality between the historical rotor regulator and the channel heat operator. Conjugate chart transport suffices.

## Residual comparison questions

1. The direct identification with the oriented log-radial Fourier carrier has been rejected: log-lattice Pontryagin Fourier has kernel `exp(-2 pi i m u)`, while physical additive Fourier conjugated through `x=exp(u)` has kernel `exp(-2 pi i exp(m+u))`. The carriers share a finite-packet embedding, but the operators do not intertwine.
2. The simplex cones are admitted bounded closed graph-domain packages, but objectwise identification with historical nonzero-defect cones is rejected by homology. A historical edge-operator assignment over the geometric registry is required.
3. Ordinary positive-Hilbert promotion is constructed for the canonical Catalan/Tate model. It does not imply strong convergence of the historical raw eight-leg filler or annihilation of the negative spectral leg of the signed Weil/Tate form.

The rejected direct identification narrows the theorem's terminology: its analytic chart operator is the log-lattice Pontryagin successor. The finite Catalan formulas and regulator-independent normalized quarter theorem are unchanged.
