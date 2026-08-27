# Full Lie rank can hide a collapsing bridge margin

Owner: `marici.Kitaev`

## Question

If every nonzero electric bridge Hamiltonian enlarges the braid Lie algebra to
the full qutrit algebra, what distinguishes an executable bridge from an
arbitrarily weak algebraic perturbation?

The missing coordinate is the normalized off-block bridge margin. For the
braid-invariant line projector `P_u`, define

\[
\beta(H)
=
\|(I-P_u)HP_u\|.
\]

This is exactly the operator-norm distance from `H` to the Hermitian
Hamiltonians preserving the one-plus-two block. Algebraic controllability asks
only whether `beta` is nonzero. Robust and uniform controllability require a
positive lower bound after fixing the Hamiltonian strength budget.

For every positive `beta`, the Lie algebra may be full while the minimum time
to transfer the invariant line into its complement is at least

\[
\frac{\pi}{2\beta}.
\]

Thus full Lie rank at every finite stage does not imply bounded synthesis cost
or completion-stable control.

## Claim boundary

The speed limit applies to closed-system unitary dynamics with a frozen
operator-norm bridge bound. It is a necessary condition, not a general
optimal-control synthesis theorem.

The exact distance formula uses one Hermitian generator and the declared
one-plus-two decomposition. Multi-generator controls, amplitude constraints,
locality, leakage, and stochastic faults are kept as additional typed
coordinates rather than compressed into `beta`.

## Frozen block decomposition

Let

\[
P=P_u,
\qquad
Q=I-P.
\]

The continuously pulsed electric braid algebra preserves both subspaces and
has the form

\[
\mathfrak g_0
=
\mathfrak u(1)_P
\oplus
\mathfrak{su}(2)_Q.
\]

A Hermitian bridge `H` removes the exact invariant projector precisely when

\[
QHP\neq0.
\]

The scalar bridge strength in the frozen operator norm is

\[
\beta(H)=\|QHP\|.
\]

Because `P` has rank one, `QHP` is a vector-valued coupling from the invariant
line into the doublet.

## Exact distance to the obstruction

Let

\[
\mathcal B_P
=
\{K=K^*:[K,P]=0\}
\]

be the real vector space of block-preserving Hermitian Hamiltonians.

For every `K` in this space,

\[
Q(H-K)P=QHP,
\]

so

\[
\|H-K\|\geq\|QHP\|=\beta(H).
\]

Choose the block-diagonal truncation

\[
K_0=PHP+QHQ.
\]

Then

\[
H-K_0=PHQ+QHP.
\]

The self-adjoint off-block matrix has operator norm `beta`. Therefore

\[
\operatorname{dist}_{\|\cdot\|}
(H,\mathcal B_P)
=
\beta(H).
\]

The bridge margin is not merely a convenient matrix entry. It is the exact
distance to restoration of the conserved projector.

## Perturbation radius

The Hermitian perturbation

\[
\Delta H
=
-PHQ-QHP
\]

has norm

\[
\|\Delta H\|=\beta(H)
\]

and makes

\[
H+\Delta H
=
PHP+QHQ
\]

block preserving.

Consequently, an uncertainty ball of radius at least `beta` contains an
exactly uncontrollable block-preserving implementation. If the certified
operator uncertainty is `delta`, a necessary robust-bridge condition is

\[
\beta(H)>\delta.
\]

For `delta` below `beta`, the reverse triangle inequality gives the guaranteed
residual bound

\[
\|Q(H+\Delta H)P\|
\geq
\beta(H)-\delta.
\]

This does not bound leakage or pulse-calibration error in other directions.

## Cross-block speed limit

Let a normalized state obey

\[
i\frac{d}{dt}|\psi(t)\rangle
=
H(t)|\psi(t)\rangle.
\]

Write

\[
\|P\psi(t)\|=\cos\theta(t),
\qquad
\|Q\psi(t)\|=\sin\theta(t),
\]

with

\[
0\leq\theta(t)\leq\frac\pi2.
\]

Differentiating the block population gives

\[
\left|
\frac{d}{dt}
\langle\psi(t)|P|\psi(t)\rangle
\right|
\leq
2\|QH(t)P\|
\|P\psi(t)\|
\|Q\psi(t)\|.
\]

Hence

\[
|\dot\theta(t)|
\leq
\|QH(t)P\|.
\]

Any protocol taking a state entirely in the invariant line to a state
entirely in the doublet must change `theta` from zero to `pi/2`. Therefore

\[
\int_0^T\|QH(t)P\|\,dt
\geq
\frac\pi2.
\]

If the admitted control schedule obeys

\[
\|QH(t)P\|\leq\beta_{max},
\]

then

\[
T\geq\frac{\pi}{2\beta_{max}}.
\]

Arbitrarily strong block-diagonal controls cannot improve this bound because
they do not change the cross-block norm in the corresponding interaction
frame.

## Saturating hostile family

Fix a unit vector `w` in the doublet and define

\[
H_\varepsilon
=
\varepsilon
\left(
|u\rangle\langle w|
+
|w\rangle\langle u|
\right),
\qquad
\varepsilon>0.
\]

Then

\[
\beta(H_\varepsilon)=\varepsilon.
\]

Together with the braid block algebra, every positive `epsilon` gives full
Lie closure. Yet

\[
e^{-itH_\varepsilon}|u\rangle
=
\cos(\varepsilon t)|u\rangle
-
i\sin(\varepsilon t)|w\rangle,
\]

so exact transfer first occurs at

\[
T_\varepsilon
=
\frac{\pi}{2\varepsilon}.
\]

This family saturates the speed limit. As `epsilon` tends to zero,

- the finite-stage Lie algebra remains full for every positive `epsilon`;
- the bridge robustness radius tends to zero;
- the exact transfer time diverges;
- the limiting Hamiltonian restores the conserved projector.

This is the control analogue of finite injectivity with a collapsing smallest
singular value.

## Normalization is mandatory

The number `beta` has units of energy and changes under rescaling of the total
Hamiltonian. Freeze an admitted strength budget

\[
\|H(t)\|\leq\Lambda.
\]

The dimensionless bridge fraction is

\[
\widehat\beta
=
\frac{\beta}{\Lambda}.
\]

Its reciprocal

\[
\kappa_{\mathrm{bridge}}
=
\frac{\Lambda}{\beta}
\]

is a condition number for cross-block actuation in the declared norm and
energy budget. Quoting a nonzero bridge without its normalization makes no
uniform control claim.

## Finite rank versus completion stability

Let a family of finite systems have bridge margins

\[
\beta_N>0.
\]

The Lie algebra can equal the full unitary algebra at every `N`. Uniform
cross-block controllability nevertheless requires at least

\[
\inf_N\widehat\beta_N>0.
\]

If

\[
\widehat\beta_N\longrightarrow0,
\]

then the normalized transfer-time lower bound diverges. The completion has an
emergent uniform-control obstruction even though no finite stage has an exact
algebraic block. An exact invariant block appears at completion only when the
completed generators exist in the declared topology and their off-block parts
converge to zero.

This necessary condition is not sufficient for a uniform compiler. Word
length, locality, bandwidth, pulse precision, and fault correction may still
diverge.

## Leakage remains an independent coordinate

Let `Pi` project onto the accepted total-`C` code space. Inside that code let

\[
P=P_u,
\qquad
Q=\Pi-P.
\]

For a microscopic candidate `H`, distinguish

\[
\beta_{\mathrm{code}}
=
\|QH P\|
\]

from the leakage strength

\[
\ell
=
\|(I-\Pi)H\Pi\|.
\]

A large algebraic bridge with uncontrolled `ell` is not an accepted logical
constructor. The source must establish a lower bound on `beta_code`, an upper
bound on `ell`, and a fault model for both. Their ratio may be useful for one
hardware comparison, but it should not replace the two typed bounds.

## Fault exposure under slow bridges

Long synthesis time creates a separate failure channel. Under the hostile
model in which fatal faults arrive as a Poisson process of rate `lambda`, the
no-fault probability is

\[
p_{\mathrm{nf}}(T)=e^{-\lambda T}.
\]

The speed limit implies

\[
p_{\mathrm{nf}}
\leq
\exp
\left(
-\frac{\lambda\pi}{2\beta_{max}}
\right).
\]

This bound belongs only to that explicit fatal-fault model. Its structural
lesson is broader: algebraic controllability can become operationally useless
when the bridge margin collapses faster than error correction suppresses
time-integrated faults.

## Control claim hierarchy

The electric bridge now has seven distinct gates.

### Algebraic bridge

\[
\beta>0.
\]

The exact conserved projector is removed and the finite Lie closure is full.

### Robust bridge

\[
\beta>\delta.
\]

The admitted uncertainty ball excludes restoration of the exact block.

### Uniform bridge

\[
\inf_N\widehat\beta_N>0.
\]

The normalized cross-block speed limit does not diverge with size.

### Selective logical bridge

The code-space bridge is bounded below while leakage is independently bounded
above.

### Local bridge

The microscopic interaction has admitted support and a bounded propagation
cone.

### Synthesizable bridge

A pulse or instrument compiler realizes the desired qutrit gates with bounded
word length and precision cost.

### Fault-tolerant bridge

The complete gadget satisfies the declared one-fault and scaling contracts.

No arrow in this hierarchy is automatic in the reverse direction.

## Hostile fixtures

### Rank-complete weak bridge

Use `H_epsilon` with positive `epsilon` tending to zero. Lie rank remains full
while transfer time and condition number diverge.

### Uncertainty cancellation

Allow an operator uncertainty ball of radius `epsilon`. It contains the
perturbation cancelling the complete off-block term.

### Unnormalized strength claim

Multiply every Hamiltonian by a large scalar and quote the resulting bridge
norm without freezing the energy budget. No implementation comparison is
defined.

### Strong leaky bridge

Choose a microscopic interaction with large code-space off-block incidence and
larger incidence out of the code. Lie rank improves while logical control
fails.

### Slow noisy bridge

Keep algebraic universality but let the bridge time exceed the physical error
timescale. Reachability survives as a formal statement and executable fidelity
collapses.

## Falsifiers

- Nonzero bridge incidence is called uniformly bounded control.
- Full Lie rank is used as an upper bound on synthesis time.
- The bridge norm is compared across systems without a frozen Hamiltonian
  normalization.
- An uncertainty radius at least as large as `beta` is said to exclude the
  block-preserving model.
- Block-diagonal controls are claimed to beat the cross-block speed limit.
- Code leakage is absorbed into the desired bridge norm.
- The Poisson hostile bound is promoted to a universal fault theorem.
- A uniform bridge margin is called a complete local fault-tolerant compiler.
- Finite-stage universality is promoted through completion while
  `beta_N` tends to zero.

## Disposition

The electric control frontier now has a quantitative margin. The off-block
norm is exactly the distance to the braid-preserving obstruction and controls
a sharp cross-block speed limit. An arbitrarily weak bridge changes the finite
Lie algebra discontinuously but cannot hide its diverging time, sensitivity,
and fault exposure.

The next physical source packet must therefore report more than a nonzero
projected matrix element. It must freeze the energy normalization and establish
bridge strength, uncertainty radius, code leakage, locality, synthesis cost,
and fault scaling as separate coordinates.

No checker, build, or Git operation was run for this research-only packet.
