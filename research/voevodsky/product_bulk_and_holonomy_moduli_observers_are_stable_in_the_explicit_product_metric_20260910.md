# Product bulk and holonomy-moduli observers are stable in the explicit product metric

## Question

How do stable reconstruction of an infinite-dimensional bulk state and stable reconstruction of finite sewing holonomy combine without treating moduli readout as bulk coercivity?

## Claim boundary

The theorem concerns a direct product of a Hilbert or graph Hilbert source with a metric moduli space. It proves a global lower-Lipschitz bound for a direct-sum observer and a robustness bound for Lipschitz cross-coupling. It does not construct a canonical product metric from physics, identify bulk and moduli variables, or assert that every moduli space admits a finite-dimensional stable embedding.

## Product context

Let \(X\) be a Hilbert space with norm \(\|\cdot\|_X\), and let \((M,d_M)\) be a metric space. Equip

\[
X\times M
\]

with the declared product metric

\[
d_\times\bigl((x,m),(x',m')\bigr)^2
=
\|x-x'\|_X^2+d_M(m,m')^2.
\]

Let

\[
T_X:X\to Z_X
\]

be bounded below with constant \(\delta_X>0\):

\[
\|T_Xx\|\ge\delta_X\|x\|_X.
\]

Let

\[
\Psi:M\to R
\]

be lower Lipschitz with constant \(\delta_M>0\):

\[
\|\Psi(m)-\Psi(m')\|_R
\ge
\delta_M d_M(m,m').
\]

No linear structure on \(M\) is required.

## Product-observer theorem

Define

\[
\mathcal O:X\times M\to Z_X\oplus R,
\qquad
\mathcal O(x,m)=(T_Xx,\Psi(m)).
\]

Then \(\mathcal O\) is lower Lipschitz with constant

\[
\delta_\times=\min(\delta_X,\delta_M).
\]

### Proof

For \((x,m),(x',m')\in X\times M\),

\[
\begin{aligned}
\|\mathcal O(x,m)-\mathcal O(x',m')\|^2
&=\|T_X(x-x')\|^2
 +\|\Psi(m)-\Psi(m')\|^2\\
&\ge \delta_X^2\|x-x'\|_X^2
 +\delta_M^2d_M(m,m')^2\\
&\ge \min(\delta_X^2,\delta_M^2)
 d_\times\bigl((x,m),(x',m')\bigr)^2.
\end{aligned}
\]

This proves the claim.

If \(T_X\) and \(\Psi\) also have upper Lipschitz constants \(L_X\) and \(L_M\), then \(\mathcal O\) has upper constant \(\max(L_X,L_M)\). Thus the product condition number is controlled by the weaker factor rather than by a hidden identification between the factors.

## Cross-coupling robustness

Suppose a mixed implementation has the form

\[
\widetilde{\mathcal O}=\mathcal O+\mathcal R,
\]

where \(\mathcal R:X\times M\to Z_X\oplus R\) is Lipschitz with respect to \(d_\times\), with constant \(\rho\). Then

\[
\|\widetilde{\mathcal O}(z)-\widetilde{\mathcal O}(z')\|
\ge
(\delta_\times-\rho)d_\times(z,z').
\]

Hence stability survives when

\[
\rho<\delta_\times.
\]

This is the required cross-term declaration. Without a bound on \(\mathcal R\), separate stability of the displayed bulk and moduli components does not control cancellation in a mixed codomain.

## Source observer supplied by Phase 2

Let \(V\subseteq X\) be closed and let

\[
T_X=
\begin{pmatrix}
Bp\\D\\K
\end{pmatrix}.
\]

Under quotient control with constant \(a\), essential vertical control repaired to a vertical lower bound \(d\), and finite-kernel injectivity, Phase 2 gives

\[
\|T_Xx\|
\ge
\delta_X\|x\|,
\]

where one explicit admissible constant is

\[
\delta_X=
\frac{d}{
\sqrt{1+\left((d+\|E\|)/a\right)^2}},
\qquad
E=(D,K)^\top.
\]

The product theorem therefore composes the first three constructor roles with the fourth while leaving their constants and proofs separate.

## Sewing-graph holonomy metric

Let \(\Gamma\) be a connected finite graph with first Betti number \(b\). After choosing a cycle basis, its \(U(1)\) sewing moduli are represented by

\[
M_\Gamma\cong U(1)^b.
\]

This basis-dependent coordinate presentation does not alter the underlying gauge quotient. Equip it with the chord product metric

\[
d_{\mathrm{ch}}(z,z')^2
=
\sum_{j=1}^b|z_j-z'_j|^2.
\]

Define the quadrature observer

\[
\Psi_\Gamma(z_1,\ldots,z_b)
=
(\operatorname{Re}z_1,\operatorname{Im}z_1,
\ldots,
\operatorname{Re}z_b,\operatorname{Im}z_b).
\]

Then

\[
\|\Psi_\Gamma(z)-\Psi_\Gamma(z')\|_{\mathbb R^{2b}}
=d_{\mathrm{ch}}(z,z').
\]

Thus \(\Psi_\Gamma\) is an isometric embedding for the declared chord metric, so \(\delta_M=L_M=1\).

The apparent cycle-basis dependence is a presentation issue: a change of integral cycle basis acts on \(U(1)^b\), but it need not be an isometry of this particular chord product metric. Claims of basis-independent stability therefore require either transport of the metric with the coordinates or a separately proved uniform comparison. No such uniform claim is made here.

## Real variance

Complex conjugation acts on each holonomy by

\[
z_j\longmapsto\overline{z_j}.
\]

Under \(\Psi_\Gamma\),

\[
\operatorname{Re}(\overline z_j)=\operatorname{Re}(z_j),
\qquad
\operatorname{Im}(\overline z_j)=-\operatorname{Im}(z_j).
\]

Therefore the real quadrature is Real-even and the imaginary quadrature is Real-odd. Both are required to reconstruct an oriented phase globally; retaining only the even quadrature leaves the conjugate pair unresolved away from the real locus.

## Green--Real radial product observer

Let \(X\) be the radial graph Hilbert source. Use:

- \(Bp\) for the channel controlling the descended quotient;
- a real reciprocal-even thick multiplier \(D_w^+\) for essential vertical bulk control;
- a compact analytic channel \(K\) injective on the finite residual kernel;
- \(M_\Gamma=H^1(\Gamma;U(1))\) for sewing holonomy;
- \(\Psi_\Gamma=(P_1,Q_1,\ldots,P_b,Q_b)\) for moduli observation.

Then

\[
\mathcal O_{\mathrm{rad}}(x,z)
=
\bigl(Bpx,D_w^+x,Kx,\Psi_\Gamma(z)\bigr)
\]

is lower Lipschitz in the explicit product metric with constant

\[
\min(\delta_X,1).
\]

The Green comparison cells \(W_u\), fixed-fiber Real maps \(J_u\), and phase gauges \(G_{u\to v}\) transport the bulk and boundary presentations. Their unitarity does not enter as an additional positive summand in the observer Gramian.

## Omission tests

### Bulk component omitted

Fix \(z\in M_\Gamma\). If \(T_X=0\), then every pair \((x,z),(x',z)\) collides. Exact phase reconstruction supplies no bulk control.

### Moduli component omitted

Fix \(x\in X\). If \(\Psi_\Gamma\) is absent, every pair \((x,z),(x,z')\) collides. Bulk coercivity supplies no holonomy reconstruction.

### Odd quadrature omitted

For nonreal \(z\),

\[
\operatorname{Re}z=
\operatorname{Re}\overline z,
\]

so the Real-even channel alone does not separate orientation-conjugate holonomies.

### Product metric omitted

Separate constants cannot be combined into a numerical stability statement until the relative scaling between bulk and moduli distances is declared.

## Constructor-role consequences

The product theorem is not a promotion of moduli observation into essential observation. It is a direct-sum composition after both factors have independently passed their own lower-bound tests. The source observer retains its Calkin provenance; the moduli observer retains its gauge-invariance and finite metric provenance.

## Disposition

Phase 4 is proved for an explicit product metric. Finite sewing holonomy has an exact isometric quadrature embedding in chord coordinates, and its direct sum with the Phase 2 source observer has lower constant \(\min(\delta_X,1)\). A Lipschitz mixed perturbation is allowed below that margin. Canonical metric selection, basis-independent quantitative bounds, and nonlinear coupling beyond the perturbative Lipschitz estimate remain outside the claim.
