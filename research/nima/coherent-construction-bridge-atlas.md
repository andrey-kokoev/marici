# Coherent Construction Bridge Atlas

## Central law

Let

\[
\Gamma_n=\sum_{h\in\mathcal H_n}\epsilon_h\,\mathcal C_h
\]

be the oriented eight-dimensional history-cell chain in `G_+(2,n)`, and let

\[
\Phi_Z(C)=CZ.
\]

The Coherent Construction Law is

\[
\Omega_{n,2,4}
=
\sum_{h\in\mathcal H_n}
\epsilon_h(\Phi_Z)_*\omega_{\mathcal C_h}.
\]

## Exact bridge chain

### 1. Complete history shells as matrix algebras

For the newly created shell at cutoff `N`,

\[
W_N
\cong
\bigoplus_{r=1}^{N-5}M_r(\mathbb C).
\]

A history is a matrix unit `E_pq`. Left-nested histories occupy the diagonal and upper triangle; right-nested histories occupy the strict lower triangle.

### 2. Pair groupoids and dagger

\[
E_{pq}E_{qr}=E_{pr},
\qquad
E_{pq}^{\dagger}=E_{qp}.
\]

Hence

\[
M_r(\mathbb C)
\cong
\mathbb C[\operatorname{Pair}(U_r)].
\]

The counting metric becomes the Hilbert–Schmidt metric.

### 3. Frobenius/TQFT structure

\[
m(E_{ij}\otimes E_{kl})=\delta_{jk}E_{il},
\]

\[
\Delta(E_{il})=\sum_jE_{ij}\otimes E_{jl},
\]

\[
m\circ\Delta=r\,\mathrm{id}.
\]

Every shell block is a normalized special symmetric dagger-Frobenius algebra.

### 4. AF/Wedderburn tower

With `m=N-5`, the accumulated history algebra has spectrum

\[
\mathfrak A_N
\cong
\bigoplus_{r=1}^{m}M_r(\mathbb C)^{\oplus(m-r+1)}.
\]

Therefore

\[
\dim\mathfrak A_N=|\mathcal H_N|,
\]

and

\[
\dim Z(\mathfrak A_N)
=
\operatorname{rank}K_0(\mathfrak A_N)
=
\frac{m(m+1)}2.
\]

### 5. Selected component as radial center

The supported endpoint pair maps canonically to a simple block:

\[
(b_1,b_2)
\longmapsto
(S,a,r)
=
(b_1+1,b_1-b_2+2,b_2-4).
\]

The isometric radial basis map is

\[
T_{b_1,b_2}
\longmapsto
\frac{I_r}{\sqrt r}.
\]

It preserves Hilbert–Schmidt norm and scalar augmentation, but it changes multiplication from triangular incidence convolution to commutative central multiplication.

### 6. Minimal Hilbert module and readout

At each new shell, the selected `(2,3)` support is a first-row minimal right ideal:

\[
eM_r
=
\operatorname{span}\{E_{3q}\}.
\]

For

\[
\psi=\sum_qw_qE_{3q},
\]

\[
\|\psi\|^2=\sum_q|w_q|^2.
\]

Scalar augmentation is uniform-mode evaluation:

\[
\epsilon(\psi)=\sum_qw_q.
\]

With

\[
\rho=\psi^\dagger\psi,
\qquad
P_+=\frac{|1\rangle\langle1|}{r},
\]

\[
\operatorname{Tr}(\rho P_+)
=
\frac{|\sum_qw_q|^2}{r}.
\]

### 7. Type-A roots and quivers

For `m=N-5`, selected histories are all positive roots of `A_m`:

\[
(b_1,b_2)
\longmapsto
[i,j]=[b_2-4,b_1-4]
\longmapsto
\alpha_i+\cdots+\alpha_j.
\]

They are also indecomposable interval representations of the linearly oriented `A_m` quiver. Boundary-update histories are exactly the simple roots `i=j`.

### 8. Cluster and associahedron completion

\[
[i,j]
\longmapsto
(i,j+2)
\]

identifies positive roots with polygon diagonals. Adding the negative-simple reference fan completes the cluster variables of type `A_m`. Mutation is diagonal flip. Every rank-two coherence face is either a commuting square or a Mac Lane pentagon.

### 9. Causal interval space

The same labels define discrete null coordinates

\[
(u,v)=(i,j),
\qquad
u\le v.
\]

The two causal covers are

\[
[i,j]\to[i-1,j],
\qquad
[i,j]\to[i,j+1].
\]

Causal path counts are binomial.

### 10. Möbius inversion as wave operator

The zeta transform sums over containing intervals. Its exact inverse is

\[
\Box_d f(i,j)
=
f(i,j)-f(i-1,j)-f(i,j+1)+f(i-1,j+1).
\]

Thus

\[
\Box_d=\Delta_u\Delta_v.
\]

### 11. Continuum de Sitter kinematic space

\[
ds^2
=
\frac{4\,du\,dv}{(v-u)^2},
\qquad
R=2.
\]

Its projective isometry is simultaneous fractional-linear endpoint action by `PSL(2,R)`, locally `SO^+(2,1)`.

### 12. Entropy and hyperbolic geodesics

\[
S(u,v)=\frac c3\log\frac{v-u}{\epsilon},
\]

\[
\partial_u\partial_vS
=
\frac{c}{3(v-u)^2}.
\]

The discrete sign-reversed Möbius curvature is positive conditional mutual information:

\[
I_L
=
\log\frac{(L+1)^2}{L(L+2)}
>0.
\]

Writing

\[
x=\frac{u+v}{2},
\qquad
R=\frac{v-u}{2},
\]

each interval is an oriented geodesic of `H^2`, and

\[
ds^2=\frac{dx^2-dR^2}{R^2}.
\]

### 13. Plücker, Ptolemy, and cluster exchange

For

\[
C_i=(1,x_i),
\qquad
\Delta_{ij}=x_j-x_i,
\]

\[
\Delta_{ac}\Delta_{bd}
=
\Delta_{ab}\Delta_{cd}
+
\Delta_{ad}\Delta_{bc}.
\]

This one equation is simultaneously the `G_+(2,n)` Plücker relation, type-A cluster exchange, ideal-hyperbolic Ptolemy theorem, and lambda-length mutation.

### 14. Tropical classical shadow

In logarithmic coordinates,

\[
p_{ac}+p_{bd}
=
\operatorname{LSE}(p_{ab}+p_{cd},p_{ad}+p_{bc}).
\]

The deformation

\[
\operatorname{LSE}_\beta(A,B)
=
\frac1\beta\log(e^{\beta A}+e^{\beta B})
\]

has tropical limit

\[
\operatorname{LSE}_\beta(A,B)\to\max(A,B).
\]

Coherent positive addition becomes winner-take-all max-plus construction; mutation walls retain equal competing resolutions.

## Unified diagram

\[
\begin{array}{ccccc}
G_+(2,n)&\longleftrightarrow&\text{Plucker/Ptolemy}&\longleftrightarrow&\text{cluster flips}\\
&&\downarrow&&\downarrow\\
\text{history cells}&\longrightarrow&\text{type-A intervals}&\longrightarrow&\text{associahedral coherence}\\
\downarrow&&\downarrow&&\downarrow\\
\text{matrix/groupoid algebra}&\longrightarrow&\text{causal interval space}&\longrightarrow&\text{de Sitter/Crofton geometry}\\
\downarrow&&\downarrow&&\downarrow\\
\text{Hilbert module}&\longrightarrow&\text{Möbius wave operator}&\longrightarrow&\text{entropy/geodesic readout}
\end{array}
\]

## Physical-weight audit at `n=8`

The bridge structures above organize history labels and carriers. Testing the exact canonical weights sharpens which structures are physically respected.

### Amplitude operator, not state

The exact selected kernel satisfies

\[
K\ne K^\dagger,
\qquad
[K,K^\dagger]\ne0.
\]

It is a non-normal amplitude operator. The canonical positive completion is

\[
\rho=K^\dagger K\ge0,
\]

but its Born readout is a new quadratic observable, not the original linear amplitude.

After operator-norm normalization,

\[
M=K/\sigma_{\max}(K),
\qquad
E=M^\dagger M,
\qquad
0\le E\le I,
\]

so `K` naturally defines a postselected Kraus/filter operation and a two-outcome POVM after complementing by `I-E`.

### Entry positivity does not imply total positivity

All nonzero entries of `K` are positive, but one `2 by 2` minor is negative. Therefore physical weights are not a totally nonnegative planar-network matrix and are not positive cluster lambda lengths.

Boundary transport creates this sign:

\[
R
=
K_{[1,2]}K_{[2,3]}
-
K_{[1,3]}K_{\alpha_2}.
\]

Without transported boundary replacement, `R>0`; with it, `R<0`. The `alpha_2` simple-root correction alone controls this crossing.

The crossing occurs at

\[
t_c
=
\frac{131129689099878491691}{36521212871898366916264},
\]

along `K(t)=K_0+t(K-K_0)`. Since `det K(t_c)` is nonzero and the rank remains full, this is an oriented-matroid/correlation wall crossing, not a spectral phase transition.

### Reflow, resolvents, and fermionic propagation

Eliminating the middle endpoint gives the Schur complement

\[
K_{\mathrm{eff}}(7,5)
=
K(7,5)-\frac{K(7,6)K(6,5)}{K(6,6)}.
\]

Boundary transport reverses its sign. Equivalently, the longest-range entry of `K^{-1}` flips sign while nearest-neighbor inverse couplings retain theirs.

The inverse has an alternating directed-path expansion. It is also the propagator of the exact fermionic Gaussian system

\[
S_F=\bar\psi K\psi,
\qquad
Z_F=\det K,
\qquad
\langle\psi_i\bar\psi_j\rangle=(K^{-1})_{ij}.
\]

The diagonal boundary correction is a self-energy insertion satisfying

\[
\frac{d}{dt}\log\det K(t)
=
\operatorname{Tr}(K(t)^{-1}B).
\]

### Polar rotation and spin gate

The unique polar decomposition

\[
K=UP,
\qquad
U\in SO(3),
\qquad
P=\sqrt{K^\dagger K}
\]

separates coherent endpoint rotation from attenuation. Although `U` has an `SU(2)` double-cover lift, the sourced deformation path remains in a contractible principal-angle chart, is open, and carries no `2 pi` or `4 pi` winding.

### Exact weighted wave equation

The physical kernel weights satisfy

\[
\Box_d f=g,
\qquad
f=Zg.
\]

Boundary transport changes both field and source only on simple-root events. Scalar augmentation is the causal-past volume moment

\[
S
=
\sum_J\operatorname{Vol}(\operatorname{Past}J)g(J),
\qquad
\operatorname{Vol}(\operatorname{Past}[i,j])=\frac{L(L+1)}2.
\]

Every field is reconstructed uniquely from two characteristic boundary traces plus interior curvature. The transform is unimodular. Consequently, two channels alone exhaust only the source-free sector; the general physical field requires

\[
\text{lower null data}
\oplus
\text{upper null data}
\oplus
\text{bulk curvature}.
\]

## Established versus open

Established exactly:

- shell matrix-block decomposition and dagger;
- pair-groupoid, Frobenius, and AF/Wedderburn structures;
- selected-center radial bijection and isometry;
- positive-root, quiver, cluster, and associahedron combinatorics;
- causal interval poset and Möbius wave operator;
- projective de Sitter metric and entropy Hessian;
- Plücker/Ptolemy/cluster identity;
- tropical log-sum-exp limit.

Still open:

- proof that physical canonical-form weights define normalized positive states;
- derivation of the observed `n^-2` coefficient from the wave/entropy geometry;
- physical realization of Frobenius sewing by amplituhedron facets;
- arbitrary-`n` history-to-positroid compiler;
- derivation of quantum measurement, spacetime, or holography from the construction law rather than structural equivalence;
- extension of the exact physical-weight audit beyond the current `n=8` kernel and chosen rational kinematics.

Ruled out for the tested kernel:

- canonical weights themselves forming a Hermitian positive state;
- canonical weights being totally nonnegative cluster lambda lengths;
- the minor-sign threshold being a spectral phase transition;
- the sourced boundary path carrying a nontrivial `4 pi` winding;
- two scalar channels reconstructing a general field without bulk-curvature data.

## Evidence index

- `research/nima/results/nnmhv-shell-matrix-blocks.json`
- `research/nima/results/nnmhv-pair-groupoid-bridge.json`
- `research/nima/results/nnmhv-shell-dagger-structure.json`
- `research/nima/results/nnmhv-shell-frobenius-tqft-bridge.json`
- `research/nima/results/nnmhv-af-wedderburn-tower.json`
- `research/nima/results/nnmhv-selected-center-radial-transform.json`
- `research/nima/results/nnmhv-weighted-radial-intertwiner.json`
- `research/nima/results/nnmhv-component-minimal-right-ideal.json`
- `research/nima/results/nnmhv-augmentation-uniform-quantum-readout.json`
- `research/nima/results/nnmhv-type-a-root-bridge.json`
- `research/nima/results/nnmhv-associahedron-cluster-bridge.json`
- `research/nima/results/nnmhv-associahedral-coherence-faces.json`
- `research/nima/results/nnmhv-interval-causal-diamond-bridge.json`
- `research/nima/results/nnmhv-mobius-wave-operator-bridge.json`
- `research/nima/results/nnmhv-projective-interval-desitter-bridge.json`
- `research/nima/results/nnmhv-entanglement-crofton-bridge.json`
- `research/nima/results/nnmhv-hyperbolic-geodesic-rt-bridge.json`
- `research/nima/results/nnmhv-plucker-poincare-cluster-bridge.json`
- `research/nima/results/nnmhv-tropical-construction-bridge.json`
- `research/nima/results/nnmhv-physical-kernel-star-gate.json`
- `research/nima/results/nnmhv-kernel-kraus-filter-bridge.json`
- `research/nima/results/nnmhv-kernel-total-positivity-gate.json`
- `research/nima/results/nnmhv-boundary-coherence-threshold.json`
- `research/nima/results/nnmhv-simple-root-interference-control.json`
- `research/nima/results/nnmhv-cluster-exchange-weight-gate.json`
- `research/nima/results/nnmhv-inverse-kernel-long-range-coupling.json`
- `research/nima/results/nnmhv-schur-reflow-bridge.json`
- `research/nima/results/nnmhv-inverse-path-sum-bridge.json`
- `research/nima/results/nnmhv-fermionic-gaussian-bridge.json`
- `research/nima/results/nnmhv-coherence-wall-nonsingular.json`
- `research/nima/results/nnmhv-kernel-polar-filter-rotation.json`
- `research/nima/results/nnmhv-endpoint-rotation-spin-lift.json`
- `research/nima/results/nnmhv-spin-path-topology-gate.json`
- `research/nima/results/nnmhv-physical-kernel-wave-sources.json`
- `research/nima/results/nnmhv-scalar-causal-source-moment.json`
- `research/nima/results/nnmhv-two-channel-null-solution-bridge.json`
- `research/nima/results/nnmhv-characteristic-boundary-reconstruction.json`
