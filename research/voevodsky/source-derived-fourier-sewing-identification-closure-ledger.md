# Source-derived Fourier sewing identification closure ledger

## Objective

Identify oriented radial Fourier sewing with the canonical--dual semilocal spectral operator and the admissible external G4 radial interface by symbolic analytic verification, while keeping endpoint atoms, parity sectors, and topology explicit.

## Closed analytic chain

### Additive to oriented radial

The unitary half-density chart

$$
(Uf)_\epsilon(u)=e^{u/2}f(\epsilon e^u)
$$

conjugates additive Fourier to the oscillatory Hankel operator with kernel

$$
K_{\epsilon',\epsilon}(v,u)
=e^{(u+v)/2}e^{-2\pi i\epsilon\epsilon'e^{u+v}}.
$$

Orientation is essential: absolute radialization collapses the odd sectors.

### Oriented radial to spectral

Logarithmic Mellin transform gives spectral reflection multiplied by

$$
G(t)=
\begin{pmatrix}m_+(t)&m_-(t)\\m_-(t)&m_+(t)\end{pmatrix},
$$

$$
m_\sigma(t)
=(2\pi)^{-1/2+it}\Gamma(1/2-it)
 e^{-i\sigma\pi(1/2-it)/2}.
$$

Parity diagonalization produces the exact real trivial/sign Tate factors. Euler reflection proves

$$
G(t)G(-t)=W_1,
$$

and unitarity on the real spectral line.

### Finite places

The standard unramified seed is not Fourier fixed. Instead

$$
\sigma_p
=\mathbf1_{\mathbb Z_p}-p^{-1}\mathbf1_{p^{-1}\mathbb Z_p}
\quad\xleftrightarrow{\mathcal F_p}\quad
\tau_p
=\mathbf1_{\mathbb Z_p}-\mathbf1_{p\mathbb Z_p}.
$$

Their local zeta sections give

$$
\gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}}.
$$

Ramified unit-shell character seeds give the conductor monomial and normalized Gauss epsilon phase, with reflected product \(\chi_p(-1)\).

### Semilocal operator

The complete characterwise operator is

$$
(\mathbb F_Sh)_\chi(t)
=\gamma_S(\chi,t)h_{\chi^{-1}}(-t).
$$

It is unitary, cutoff-natural, and obeys

$$
\mathbb F_S^2=\text{additive reflection},
\qquad
\mathbb F_S^4=I.
$$

There is no residual scalar phase or unsupported block-unitary choice.

### External radial G4 relation

The actual quarter turn is not the declared reciprocal swap. It is the explicit metaplectic lift

$$
\widetilde W_u=C_u\mathcal FC_u^{-1},
$$

satisfying

$$
\widetilde W_u^2=W_u,
\qquad
\widetilde W_u^4=I.
$$

This refines the current radial amendment without violating its prohibition against identifying quarter turn with swap.

### Comb ports and Gram test

The shifted comb maps to the ordered Hurwitz pair

$$
(\zeta(s,a),\zeta(s,1-a)),
$$

and its character image maps, after separating the zero atom, to the ordered periodic-polylogarithm pair. Harmonic-oscillator regularization gives exact orbit-Gram equality at every positive scale. The raw zero-scale comb remains distributional.

### Complete response and fourth chart

The seam-uniform response

$$
\mathscr R(g)=(B_g,Q_g,A_g,C_g)
$$

retains value, Fourier value, causal history, and principal-value history. It has intrinsic topology

$$
\mathcal S\oplus\mathcal S
\oplus\mathcal H_{\rm rel}^2
\oplus\mathcal H_{\rm rel}^2,
$$

and inverse

$$
C_{41}^{\rm resp}(B,Q,A,C)=B.
$$

Its unitary Fourier graph is a canonical maximal-isotropic sewing relation containing every source-generated complete response.

### Differentiated Weil connection

The logarithmic connection

$$
a_S=-i\gamma_S^{-1}\partial_t\gamma_S
$$

is self-adjoint, commutes with \(\mathbb F_S\), and adds under place cutoffs. Thus Fourier and cutoff coherence survive differentiation from scattering to the uncompressed Weil operator.

## Corrected statements

The following tempting assertions are false and have been removed:

1. absolute radialization is faithful;
2. the old four-scalar history port is quarter-turn closed;
3. the primary even Sonin domain carries \(\pm i\) sectors;
4. \(\sigma_p\) is individually Fourier fixed;
5. the spectral square identity is \(G(t)G(-t)=I\) in orientation coordinates;
6. raw combs possess an unregularized Hilbert Gram matrix.

## Exact residual frontier

The source-derived sewing objective is complete on the common test/Hilbert/strong-dual carriers. What remains is not another sewing normalization problem.

For the unchanged Evans state, admission to the constructed maximal-isotropic response graph is equivalent to the existing prime-shell residual family

$$
B_\Sigma^\dagger\partial_z^ju(\cdot;z_0)=0,
\qquad 0\le j<m.
$$

Prior work proves that this condition is already RH-bearing and cannot be cancelled by an available auxiliary source coordinate. Neither unitary sewing, determinant agreement, nor abstract maximal isotropy proves this membership identity.

## Disposition

The oriented radial, spectral Tate, external radial-swap lift, finite local, semilocal cutoff, comb-port, and complete-response sewing identifications are source-derived and analytically closed. The next unresolved theorem is the prime-shell Evans membership/cancellation identity, which is the declared RH frontier rather than a continuation of the Fourier sewing normalization task.