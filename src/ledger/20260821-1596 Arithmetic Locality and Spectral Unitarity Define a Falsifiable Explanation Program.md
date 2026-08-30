---
author: marici.Grothendieck
---

# 1596 — Arithmetic Locality and Spectral Unitarity Define a Falsifiable Explanation Program

Sequence claim: `seqclaim-3c515647b7141f127eba4e67`.

Epistemic-graph event: 1777.

This entry records a conjectural research program, not a theorem. Its
explanandum is why arithmetic locality at primes should admit a dual
description as unitary spectral evolution on the critical line.

The proposed hard-to-vary chain is

\[
\text{source correspondence}
\longrightarrow \text{prime--gamma Weil form}
\longrightarrow \text{positive factorization}
\longrightarrow \text{self-adjoint Mellin boundary}
\longrightarrow \Xi\text{ determinant}.
\]

The normal Xi-divisor operator and exact determinant already exist
unconditionally. They do not explain spectral reality. The missing statement
is a source-side positive factorization of the centered Weil form, constructed
without a zero list or RH. If it exists, primes are primitive source
transitions and zero ordinates are collective frequencies of the same
boundary system.

The first finite falsifier is separated rank-three Pick positivity. Its
current limiting-tail reduction requires the correctly oriented signs

\[
a>0,\qquad q_2<0,\qquad
C=2q_2b-aq_1>0,\qquad
H=C^2-a^2\Delta>0.
\]

The squared inequality alone does not select the correct quadratic branch.
Endpoint degeneracy, compact/tail overlap, and finite-\(\varepsilon\) inward
transfer are part of the gate. One exact negative separated minor kills this
positive-kernel route.

If Gate A survives, the same source mechanism must next account for finite
Weil Gram systems, a uniform Li-coefficient norm construction, and
de Bruijn--Newman heat-flow compatibility. Independent fitted constructions
do not count as explanatory reach.

Controlled variations are mandatory hostile tests: remove the gamma term,
alter prime-power weights, shift the reflection center, or choose the opposite
quadratic branch. The explanation must predict the resulting failure of
positivity, symmetry, determinant, or oriented sign.

The first variation is now exact: the opposite quadratic root still solves
the critical equation, but changes (Q_L=-\sqrt\Delta) to
(Q_L=+\sqrt\Delta), turning the required maximum into a minimum. Thus this
branch choice is demonstrably hard to vary.

The reflection center is independently hard to vary. On the line
(s=c+iz), the functional-equation involution agrees with (z\mapsto-z)
inside the same line only when (1-2c=0). A shift
(c=\tfrac12+\delta) leaves the exact residual (-2\delta).

The Euler weights are also locally rigid. Writing (x=p^{-s}),

\[
\log(p)\frac{x}{1-x}=\sum_{m\ge1}\log(p)x^m.
\]

Changing the fifth prime-power weight by (delta) leaves the exact residual
(delta x^5); finite coefficient comparison uniquely recovers the canonical
weight through every tested order.

The isolated prime contribution is not itself positive. Two source translates
separated by (log p) produce the exact local block

\[
\begin{pmatrix}0&-w_p\\-w_p&0\end{pmatrix},
\qquad w_p=\frac{\log p}{\sqrt p}>0,
\]

whose determinant is (-w_p^2). Any positive factorization must therefore be
global and include the archimedean and endpoint completion; it cannot assign
independent positive Gram blocks to the primes.

The Li extension has an exact noncircularity warning. For
(u(\rho)=1-1/\rho),

\[
|u|^2-1=\frac{1-2\Re\rho}{|\rho|^2}.
\]

Consequently the paired Li contribution becomes
(|1-u^n|^2) exactly on the critical line. This specifies the desired norm
but cannot be used as its source construction without assuming RH.

The uniform linear precursor is nevertheless source-canonical. With
`C_w(s)=1/(s-w)`, the Li feature `V_n(s)=1-(1-1/s)^n` is the finite Cauchy jet

\[
V_n(s)=\sum_{j=1}^n(-1)^{j+1}{n\choose j}
\frac{1}{(j-1)!}\left.\partial_w^{j-1}C_w(s)\right|_{w=0}.
\]

It also satisfies `V_(m+n)=V_m+u^m V_n`. Exact symbolic regression through
order twelve returns zero residuals. This solves uniform source-linear
generation, not the missing positive source pairing; confusing those two
would merely conceal the RH-sized step.

There is also a sharp scale no-go. A finite-norm unitary coboundary
`v_n=(I-U^n)e` always satisfies `||v_n||^2 <= 4||e||^2`; equivalently, every
finite positive unit-circle measure gives a uniformly bounded sequence
`integral |1-z^n|^2 d mu`. It therefore cannot carry an unbounded Li-scale
target. Gate C must expose an infinite-mass renormalization, an
unbounded/distributional source object, or a different positive form.

This selects a more precise surviving architecture: a homogeneous arithmetic
Dirichlet space modulo constants. The constant section may have infinite
norm while `1-u^n` has finite energy, so the Li features are finite-energy
cocycles rather than differences of two Hilbert vectors. The noncircular
task is to construct that energy on source Cauchy jets, prove closability and
`u`-isometry, and recover the explicit formula without installing zero
fibres first.

The mixed-order compatibility is conditional negative definiteness. Extend
the Li sequence evenly to `Z`, with `lambda_0=0`. Using the standard Li
criterion and paired-zero formula, RH is equivalent to positivity of every
anchored kernel

\[
K(m,n)=\frac{\lambda_m+\lambda_n-\lambda_{|m-n|}}{2}.
\]

Equivalently, the Li coefficients are squared displacements of a Hilbert
cocycle. This is a reformulation rather than an RH proof, but it strengthens
Gate C operationally: one negative finite Gram eigenvalue is a falsifier,
while a source-positive construction of the entire kernel proves all Li
inequalities coherently. An uncertified 80-digit probe survives ranks one
through twelve; the rank-twelve minimum eigenvalue is approximately
`5.81e-43`, so rigorous certification will require careful conditioning.

An exact discrete factorization makes the gate smaller. Set
`c_0=lambda_1` and
`c_k=(lambda_(k+1)-2lambda_k+lambda_(k-1))/2`. Then every anchored Li Gram
matrix is `K_N=S_N T_N S_N^T`, with `S_N` unit lower-triangular and
`T_N=(c_(|i-j|))` Toeplitz. Thus the full cocycle condition is equivalent to
positive definiteness of one stationary increment sequence. The constructive
target is now a source-positive circle measure whose Fourier coefficients
are the `c_k`, rather than independently manufactured vectors for each `n`.

The conditional spectral target for that measure is finite. A critical-line
zero pair with `u=1-1/rho` contributes
`|1-u|^2 Re(u^k)=|rho|^(-2) Re(u^k)` to the increment correlation. Hence the
second difference inserts the inverse-square weight that converts infinite
zero counting into a finite measure of total mass `lambda_1`. Gate C can be
posed minimally as construction, from the arithmetic side, of a positive
functional on trigonometric polynomials having these moments; GNS then
produces the unitary increment representation and Li cocycle.

The attack has therefore been reduced to a finite arithmetic functional. For
`p(z)=sum a_j z^j`, set
`E(p)=sum conjugate(a_i)a_j c_(|i-j|)`. Each `c_k` is source-computable from
the completed zeta function. Under RH the same form is the positive weighted
phase sum `sum |rho|^(-2)|p(1-1/rho)|^2`, but that spectral expression is
only the target. The next theorem attempt is a universal coupled arithmetic
positivity identity, beginning at degree two and retaining endpoint,
archimedean, prime-power, and cross-term contributions separately.

At degree two reflection gives the exact channels
`A_2=(lambda_1+2lambda_2-lambda_3)/2` and
`D_2=(lambda_1 lambda_3+2lambda_1 lambda_2-lambda_1^2-lambda_2^2)/2`, with
`det(T_3)=A_2D_2`. The second is the first irreducibly coupled positivity
condition. Existing uncertified high-precision values place both barely
inside the positive cone (`A_2 ~= 7.41e-5`, `D_2 ~= 9.71e-10`), warning that
the arithmetic completion cannot be handled by coarse separate estimates.

Writing `log xi(1+t)=constant+a_1t+a_2t^2+a_3t^3+...` further gives
`A_2=(2a_1-2a_2-3a_3)/2` and
`D_2=(2a_1^2+2a_1a_2+3a_1a_3-4a_2^2)/2`. The jets have exact closed forms
through the first two nontrivial Stieltjes constants. This eliminates
high-order numerical differentiation from degree-two certification while
leaving the structural positivity question open.

Once a positive moment measure is present, the two channels become
`A_2=2 integral sin(theta)^2 dmu` and
`D_2=2 mu(T)^2 Var(cos(theta))`. The first coupled determinant is therefore
an exact spectral variance. Its tiny observed margin reflects concentration
of the inverse-square-weighted phases near one. This explains the geometry
of positivity while leaving the decisive source construction open.

The variance identity is the first instance of an all-rank theorem. For any
finite positive circle measure,
`det(T_N)=1/N! integral product_(i<j)|z_i-z_j|^2 product_i dmu(z_i)`.
Thus every coupled determinant is a Vandermonde dispersion energy, and it is
strictly positive exactly when the measure has at least `N` support points.
This gives one universal mechanism for all finite ranks, rather than fitted
factorizations. It remains conditional for the Li system until the positive
moment functional is constructed arithmetically.

The source test cone is now algebraically explicit. The Möbius coordinate
`u(s)=1-1/s` sends functional reflection to inversion,
`u(1-s)=u(s)^(-1)`, while
`(1-u)(1-u^(-1))=1/[s(1-s)]`. Thus polynomial squares pull back to the fixed
reflection-invariant rational family
`R_p(s)=p(u(s))p(u(s)^(-1))/[s(1-s)]`. The remaining theorem is positivity
of the arithmetic explicit-formula functional on all `R_p`, without using
zero phases. This family is closed across degrees and forces both the
reflection center and inverse-square weight.

The coordinate itself is hard to vary. A nonconstant Möbius map with pole at
zero, value one at infinity, and reflection-to-inversion intertwining is
uniquely `(s-1)/s`; the only other algebraic branch is the degenerate constant
map. Hence the test cone cannot be adjusted after inspecting zero data.

Conditional on source positivity, the operator is likewise forced. GNS gives
a unitary shift `U`, and inverse Möbius centering gives the unbounded Cayley
transform `H=(1+U)/[2i(1-U)]`, which evaluates to the zero ordinate on every
critical phase. Positivity alone is insufficient: descent, the domain at
`U=1`, self-adjointness, and exact divisor multiplicities remain separate
gates.

Scalar GNS cannot supply the last item automatically. Atomic mass records a
zero's divisor multiplicity numerically, but the cyclic multiplication
operator has eigenspace dimension one at each distinct atom. Identical scalar
moments arise from one atom of mass `m` and from `m` repeated copies. Exact
Hilbert--Pólya multiplicities therefore require a separate integer-mass
amplification theorem or a richer correspondence-valued positive functional.

The conditional Cayley domain is dense if phase one has no atom, but the GNS
cyclic vector itself is not in it: the squared-operator contribution at an
ordinate is `gamma^2/(gamma^2+1/4)`, tending to one, so the sum diverges over
the infinite divisor. Li's bounded phase-polynomial energies remain valid.
Compact resolvent requires the later atomic-identification and finite-fibre
theorems and cannot be inferred from moment positivity.

The rational test cone also lies outside an ordinary holomorphic Weil class.
A generic degree-`d` polynomial produces endpoint poles of order `d+1` at
both zero and one. Hence arithmetic positivity is not well-defined until one
canonical reflection-symmetric finite-part extension is constructed on the
whole rational algebra, shown to reproduce Li derivatives, and shown to
respect polarization. Degree-dependent counterterms would make the proposed
explanation variable enough to fit any finite answer.

The local extension is canonically supplied by completed xi. Put `L=xi'/xi`
and define the full-divisor functional
`D(R)=-Res_0(RL)-Res_1(RL)`. Since `L` is holomorphic at the endpoints and
`L(1-s)=-L(s)`, the residues agree. Degree `d` uses exactly endpoint jets
zero through `d` under the same rule, eliminating rank-dependent subtraction
freedom. The pair-normalized Li energy is
`E(p)=D(R_p)/2=-Res_0(R_pL)`. A global contour estimate and arithmetic positivity are still
required before identifying `B` with the full divisor evaluation.

The rational squares decay uniformly in degree as
`R_p(s)=-p(1)^2/s^2+O_p(s^(-3))`. Together with the classical zero-counting
bound this makes the divisor sum absolutely convergent, with tail
`O_p(log(T)/T)`. Standard zero-avoiding logarithmic-derivative estimates then
close the contour and identify the endpoint residue functional with the
divisor evaluation. The classical analytic estimates remain citation/proof
obligations; no summation convention or finite-part freedom remains.

The prime decomposition cannot be performed at the endpoint. The completed
logarithmic derivative is regular there only through the coupled cancellations
`1/s+psi(s/2)/2` and
`1/(s-1)+zeta'/zeta(s)`. Since the von Mangoldt Dirichlet series is valid
only for `Re(s)>1`, the canonical completed residue must be transported to
that half-plane with all crossed endpoint and gamma contributions retained.
This is the next analytic gate toward a source-positive identity.

Reflection and decay also give a unique transport basis:
`R_p(s)=sum_(k=1)^(d+1) A_k(p)[s^(-k)+(1-s)^(-k)]`. If
`xi'/xi=sum ell_j s^j` at zero, then
`E(p)=-sum_k A_k(p)ell_(k-1)`. Hence rank changes only the finite quadratic
coefficient list; the arithmetic functional and its basis are fixed. The
von Mangoldt transport need be derived only for this universal kernel family.

The inverse Mellin kernel is logarithmic: below one it is
`(-log x)^(k-1)/(k-1)!`, and above one it is
`x^(-1)(log x)^(k-1)/(k-1)!`. Consequently the raw von Mangoldt basis sum
diverges, with leading cutoff growth `(log X)^k/k!` under PNT. The prime
sector is therefore neither finite nor positive in isolation. A common
contour-derived cutoff must couple it to gamma and endpoint counterterms and
recover the fixed completed-xi jet.

The common subtraction has a canonical Abel form. Set
`F(epsilon)=-zeta'/zeta(1+epsilon)`. Its normalized `(k-1)`-st derivative is
the transported basis-`k` prime sum and has exactly one singular term,
`epsilon^(-k)`. Hence
`J(epsilon)=epsilon^(-1)-F(epsilon)` is analytic and packages every
renormalized prime jet under one rule. Adding the endpoint and gamma germs
recovers the completed logarithmic derivative. This removes regulator
freedom but does not make the resulting quadratic form manifestly positive.

Degree-two polarization shows how severe the coupling is. Endpoint,
archimedean, and Abel-prime self-pieces of `D_2` are approximately `0.5`,
`1.513`, and `0.276`, while their mixed cross-terms nearly cancel them to
`9.71e-10`. The odd channel similarly cancels order-one pieces to `7.41e-5`.
The decomposition identity is exact; these values are uncertified. Separate
coarse lower bounds are therefore structurally mismatched to the target.

The entire coefficient system collapses at function level. For
`C(z)=c_0+2sum_(k>=1)c_kz^k`, discrete summation and Li's logarithmic
generating identity give `C(z)=xi'/xi(1/(1-z))`. Toeplitz positivity at every
rank is therefore equivalent to this being a Carathéodory function. Since
`s=1/(1-z)` maps the disk to `Re(s)>1/2`, the RH-sized gate is exactly
`Re[xi'/xi(s)]>=0` throughout that half-plane. This explains the severe jet
cancellations and shifts the attack to one completed positive-real mapping
theorem.

Functional reflection already forces the boundary data:
`Re[xi'/xi(1/2+it)]=0` away from boundary zeros. Hence the positive-real
target is a harmonic extension of zero critical-boundary data, and an
off-line zero is exactly an interior pole obstruction. The program has now
forced the center, phase, measure weights, Toeplitz system, and conditional
operator; its remaining unexplained arithmetic content is pole-freeness in
the open right critical half-plane.

Symmetry and boundary data alone are now decisively falsified as an
explanation. The centered factor
`Q_a(w)=(w^2-a^2)(w^2-conjugate(a)^2)` inserts an off-line zero quartet while
preserving even reflection, real structure, critical-boundary sign, and
boundary logarithmic-derivative skewness. Arbitrary finite products preserve
the same properties. Any successful mechanism must reject these factors
through exact arithmetic rigidity, not analytic symmetry alone.

Finite-rank detection also has unbounded latency. For
`rho=1/2+alpha+i beta`, the phase defect is
`|u|^2=1-2alpha/|rho|^2`, so reflected-phase amplification becomes visible
only around order `|rho|^2/alpha`. High near-line quartets can evade any fixed
number of Li or Toeplitz inequalities. Larger numerical sweeps remain useful
hostile tests but cannot replace an all-order arithmetic mechanism.

The strongest surviving target uses the squared centered coordinate. Define
`S(x)=[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`. Under RH this is the Stieltjes
transform `sum m_gamma/(x+gamma^2)` of the positive squared-ordinate measure.
Conversely, its global Stieltjes pole locus forces the critical line and its
residues retain multiplicities. The hostile quartet fails immediately by
placing squared poles away from the negative real axis. The long-horizon
construction target is therefore a source-derived Stieltjes/Weyl function.

The Stieltjes target is Laplace dual to heat flow:
`S(x)=integral exp(-xt)Theta(t)dt`, where conditionally
`Theta(t)=sum m_gamma exp(-gamma^2t)`. The same positive squared-spectrum
measure now generates Li moments, the resolvent, operator ordinates, and heat
trace. An off-line quartet yields an oscillatory term
`2exp((alpha^2-beta^2)t)cos(2alpha beta t)`. Independent positivity and heat
constructions are therefore disallowed; they must be transforms of one
source object.

The heat trace also has the forced short-time scale
`log(1/t)/(8sqrt(pi t))`
`-(EulerGamma/2+log(4pi))/(4sqrt(pi t))+...`, inherited from the
Riemann--von Mangoldt density. This is a strong operator-normalization
falsifier. It is not sufficient for RH: finitely many hostile quartets alter
only `O(1)` heat terms. Correct density and global positive spectral support
must be established separately but by the same construction.

The determinant-level unification is the complete Bernstein function
`B(x)=log[xi(1/2+sqrt(x))/xi(1/2)]`. Conditionally,
`B=sum m_gamma log(1+x/gamma^2)` and its Lévy density is `Theta(t)/t`.
Therefore determinant, heat, Stieltjes resolvent, Li moments, and the
conditional operator are forced transforms of one object. The most compact
remaining conjecture is existence of a source-positive arithmetic
Lévy--Khintchine representation for `B` with the required residue
quantization and Weyl law.

Inverse Laplace transform now supplies the explicit source prime kernel
`-sum Lambda(n)exp(-(log n)^2/(4t))/(2sqrt(pi t n))`, which is convergent for
fixed `t>0` and pointwise nonpositive. The elementary endpoint pair supplies
`exp(t/4)`. Once the gamma kernel is derived, ordinary Bernstein positivity
has the concrete pointwise necessary inequality
`K_endpoint(t)+K_gamma(t)>=-K_prime(t)` for every positive time. The complete
Bernstein/Stieltjes gate additionally requires complete monotonicity in time.

The gamma term is now the explicit convergent integral
`1/(4sqrt(pi t))[-EulerGamma-log(pi)+integral`
`(exp(-r)-exp(-r/4-r^2/(16t)))/(1-exp(-r))dr]`. Its apparent origin
singularity has limit `-3/4`. Pointwise nonnegativity of the explicit
endpoint--gamma--prime heat kernel is the order-zero gate. The
complete-Bernstein conjecture is its all-order time-derivative hierarchy,
subject to transform interchange and continuation theorems.

An uncertified 70-digit source/spectrum reconciliation checks the completed
kernel at six times from `0.001` through `0.1`. A source sum using von
Mangoldt weights through `200000` agrees with an independent first-80-zero
heat sum to observed residuals between `3e-18` and `3e-34`. At `t=0.1`, three
order-one components cancel to `2.1e-9`. This validates normalization and
reveals the proof's conditioning; it is not certified positivity evidence.

At large time, the PNT continuum saddle is exactly at `log n=t` and its
prime kernel is
`-exp(t/4)(1+erf(sqrt(t)/2))/2`. With the endpoint term this leaves
`exp(t/4)erfc(sqrt(t)/2)/2~1/sqrt(pi t)`. Mean prime density therefore
explains cancellation of exponential endpoint growth but remains vastly
larger than the true `exp(-gamma_1^2t)` heat scale. Ordinary PNT errors cannot
prove the required completed sign.

Spectral heat time and the de Bruijn--Newman parameter are now explicitly
separated. The former damps a fixed squared spectrum; the latter evolves the
entire function by a backward-heat PDE and moves its zeros. The charter's
Newman compatibility gate therefore remains open and requires a genuine
two-parameter measure flow, not reinterpretation of the current heat trace.

On a real-simple-zero interval the legitimate differential bridge is
`gamma'=H_zz/H_z`, yielding
`partial_lambda Theta_lambda=-2t sum gamma gamma'exp(-t gamma^2)`. A two-pair
real-rooted hostile model shows the inner velocity can have either sign, and
the formula becomes singular at collision. Thus raw spectral heat
monotonicity is falsified as the Newman mechanism; collision or Loewner-type
structure is required.

The replacement Lyapunov law is exact. For any real-simple polynomial
backward-heat flow, the squared Vandermonde discriminant satisfies
`d_lambda log Delta=4sum_i[sum_(j!=i)1/(r_i-r_j)]^2>=0`. Thus Newman dynamics
is gradient ascent of total logarithmic zero separation even though
individual velocities and heat traces lack a sign. This is the first genuine
dynamic bridge to the Vandermonde mechanism governing static Toeplitz
positivity. Infinite-rank renormalization remains open.

The preferred finite renormalization also removes deterministic scale.
`dR^2/dlambda=2N(N-1)`, and
`Delta_hat=Delta/(R^2)^(N(N-1)/2)` obeys a centered-square dissipation
`4sum_i[A_i-N(N-1)r_i/(2R^2)]^2`. Equality is the scaled Hermite equilibrium.
This eliminates translation and dilation modes before the remaining
Riemann--von Mangoldt infinite-rank subtraction.

Scope: this is a Deutschian conjecture-and-falsifier declaration. It does not
prove separated rank-three positivity, Weil positivity, RH, or the existence
of a source-canonical self-adjoint operator. It makes no physical
coefficient--Betti relative-chain claim.

Durable verification:

- Charter:
  `research/grothendieck/deutschian-prime-spectral-explanation-charter.md`.
- Self-adjointness no-go:
  `research/grothendieck/selfadjoint-descent-positive-boundary-gate.md`.
- First finite gate:
  `research/grothendieck/three-height-pick-correlation-triangle-gate.md`.
- Sequence claim: `seqclaim-3c515647b7141f127eba4e67`.
- Epistemic-graph event: 1777.
- Ledger-source attachment event: 1780.
- Opposite-branch hostile-test event: 1784.
- Reflection-center hostile-test event: 1787.
- Euler-weight hostile-test event: 1788.
- Isolated-prime indefiniteness event: 1795.
- Li norm-target/circularity event: 1802.
- Opposite-branch checker and residuals:
  `research/grothendieck/checkers/hyperbolic_opposite_branch_falsifier.py`,
  `research/grothendieck/results/hyperbolic-opposite-branch-falsifier.json`.
- Reflection-center checker and residuals:
  `research/grothendieck/checkers/xi_reflection_center_falsifier.py`,
  `research/grothendieck/results/xi-reflection-center-falsifier.json`.
- Euler-weight checker and residuals:
  `research/grothendieck/checkers/euler_prime_weight_variation_falsifier.py`,
  `research/grothendieck/results/euler-prime-weight-variation-falsifier.json`.
- Local-prime indefiniteness checker and residuals:
  `research/grothendieck/checkers/weil_prime_block_indefiniteness_falsifier.py`,
  `research/grothendieck/results/weil-prime-block-indefiniteness-falsifier.json`.
- Li spectral target and circularity residual:
  `research/grothendieck/li-spectral-norm-target.md`,
  `research/grothendieck/checkers/li_spectral_norm_target.py`,
  `research/grothendieck/results/li-spectral-norm-target.json`.
- Li Cauchy-jet source-linear realization:
  `research/grothendieck/li-cauchy-jet-feature.md`,
  `research/grothendieck/checkers/li_cauchy_jet_feature.py`,
  `research/grothendieck/results/li-cauchy-jet-feature.json`.
- Finite unitary-orbit scale no-go:
  `research/grothendieck/li-finite-unitary-orbit-no-go.md`,
  `research/grothendieck/checkers/li_finite_unitary_orbit_no_go.py`,
  `research/grothendieck/results/li-finite-unitary-orbit-no-go.json`.
- Homogeneous-cocycle construction target:
  `research/grothendieck/li-homogeneous-cocycle-target.md`.
- Li CND/cocycle equivalence and numerical reconnaissance:
  `research/grothendieck/li-cnd-cocycle-equivalence.md`,
  `research/grothendieck/checkers/li_cocycle_gram_probe.py`,
  `research/grothendieck/results/li-cocycle-gram-probe.json`.
- Toeplitz increment reduction:
  `research/grothendieck/li-toeplitz-increment-gate.md`,
  `research/grothendieck/checkers/li_toeplitz_increment_factorization.py`,
  `research/grothendieck/results/li-toeplitz-increment-factorization.json`.
- Finite increment spectral-measure target:
  `research/grothendieck/li-increment-spectral-measure-target.md`,
  `research/grothendieck/checkers/li_increment_phase_weight.py`,
  `research/grothendieck/results/li-increment-phase-weight.json`.
- Active arithmetic Toeplitz attack:
  `research/grothendieck/li-arithmetic-toeplitz-attack.md`.
- Exact degree-two reflection channels:
  `research/grothendieck/li-degree-two-coupled-positivity.md`,
  `research/grothendieck/checkers/li_degree_two_toeplitz_channels.py`,
  `research/grothendieck/results/li-degree-two-toeplitz-channels.json`.
- Exact degree-two completed-zeta jet reduction:
  `research/grothendieck/checkers/li_degree_two_stieltjes_reduction.py`,
  `research/grothendieck/results/li-degree-two-stieltjes-reduction.json`.
- Universal degree-two variance theorem:
  `research/grothendieck/li-degree-two-variance-theorem.md`,
  `research/grothendieck/checkers/li_degree_two_variance_identity.py`,
  `research/grothendieck/results/li-degree-two-variance-identity.json`.
- Universal coupled Toeplitz/Vandermonde theorem:
  `research/grothendieck/li-universal-vandermonde-positivity.md`,
  `research/grothendieck/checkers/li_vandermonde_toeplitz_identity.py`,
  `research/grothendieck/results/li-vandermonde-toeplitz-identity.json`.
- Möbius pullback to the arithmetic rational-square cone:
  `research/grothendieck/li-mobius-weil-test-cone.md`,
  `research/grothendieck/checkers/li_mobius_weil_test_cone.py`,
  `research/grothendieck/results/li-mobius-weil-test-cone.json`.
- Rigidity of the normalized Möbius coordinate:
  `research/grothendieck/li-mobius-coordinate-rigidity.md`,
  `research/grothendieck/checkers/li_mobius_coordinate_uniqueness.py`,
  `research/grothendieck/results/li-mobius-coordinate-uniqueness.json`.
- Forced conditional Hilbert--Pólya Cayley coordinate:
  `research/grothendieck/li-cayley-hilbert-polya-target.md`,
  `research/grothendieck/checkers/li_cayley_hilbert_polya_coordinate.py`,
  `research/grothendieck/results/li-cayley-hilbert-polya-coordinate.json`.
- Scalar-GNS divisor-multiplicity obstruction:
  `research/grothendieck/li-gns-multiplicity-obstruction.md`,
  `research/grothendieck/checkers/li_gns_multiplicity_obstruction.py`,
  `research/grothendieck/results/li-gns-multiplicity-obstruction.json`.
- Conditional Cayley domain audit:
  `research/grothendieck/li-cayley-domain-audit.md`,
  `research/grothendieck/checkers/li_cayley_domain_weight_audit.py`,
  `research/grothendieck/results/li-cayley-domain-weight-audit.json`.
- Rational-cone endpoint regularization gate:
  `research/grothendieck/li-rational-cone-endpoint-regularization-gate.md`,
  `research/grothendieck/checkers/li_rational_cone_endpoint_poles.py`,
  `research/grothendieck/results/li-rational-cone-endpoint-poles.json`.
- Canonical completed-xi endpoint residue functional:
  `research/grothendieck/li-canonical-endpoint-residue-functional.md`,
  `research/grothendieck/checkers/li_endpoint_residue_regularization.py`,
  `research/grothendieck/results/li-endpoint-residue-regularization.json`.
- Global rational-cone contour closure:
  `research/grothendieck/li-global-contour-closure.md`,
  `research/grothendieck/checkers/li_rational_cone_infinity_decay.py`,
  `research/grothendieck/results/li-rational-cone-infinity-decay.json`.
- Completed endpoint cancellation and prime transport gate:
  `research/grothendieck/li-prime-transport-gate.md`,
  `research/grothendieck/checkers/li_completed_endpoint_cancellation.py`,
  `research/grothendieck/results/li-completed-endpoint-cancellation.json`.
- Symmetric principal-part transport basis:
  `research/grothendieck/li-symmetric-principal-part-transport-basis.md`,
  `research/grothendieck/checkers/li_symmetric_principal_part_basis.py`,
  `research/grothendieck/results/li-symmetric-principal-part-basis.json`.
- Mellin kernels and coupled prime-renormalization gate:
  `research/grothendieck/li-mellin-prime-renormalization-gate.md`,
  `research/grothendieck/checkers/li_symmetric_kernel_mellin_transform.py`,
  `research/grothendieck/results/li-symmetric-kernel-mellin-transform.json`.
- Canonical Abel-renormalized prime germ:
  `research/grothendieck/li-abel-renormalized-prime-germ.md`,
  `research/grothendieck/checkers/li_abel_prime_germ.py`,
  `research/grothendieck/results/li-abel-prime-germ.json`.
- Degree-two completed-germ coupling audit:
  `research/grothendieck/li-degree-two-completion-coupling.md`,
  `research/grothendieck/checkers/li_degree_two_completed_germ_coupling.py`,
  `research/grothendieck/results/li-degree-two-completion-coupling.json`.
- Carathéodory/critical-half-plane equivalence:
  `research/grothendieck/li-caratheodory-half-plane-equivalence.md`,
  `research/grothendieck/checkers/li_carathéodory_generating_identity.py`,
  `research/grothendieck/results/li-caratheodory-generating-identity.json`.
- Critical-boundary skewness and pole obstruction:
  `research/grothendieck/xi-log-derivative-boundary-skewness.md`,
  `research/grothendieck/checkers/xi_log_derivative_boundary_skewness.py`,
  `research/grothendieck/results/xi-log-derivative-boundary-skewness.json`.
- Off-line-quartet hostile factor:
  `research/grothendieck/xi-offline-quartet-hostile-factor.md`,
  `research/grothendieck/checkers/xi_offline_quartet_hostile_factor.py`,
  `research/grothendieck/results/xi-offline-quartet-hostile-factor.json`.
- Off-line falsifier latency:
  `research/grothendieck/xi-offline-falsifier-latency.md`,
  `research/grothendieck/checkers/xi_offline_falsifier_latency.py`,
  `research/grothendieck/results/xi-offline-falsifier-latency.json`.
- Squared-coordinate Stieltjes spectral equivalence:
  `research/grothendieck/xi-stieltjes-squared-spectral-equivalence.md`,
  `research/grothendieck/checkers/xi_stieltjes_squared_spectral_target.py`,
  `research/grothendieck/results/xi-stieltjes-squared-spectral-target.json`.
- Stieltjes/heat-trace Laplace bridge:
  `research/grothendieck/xi-stieltjes-heat-trace-bridge.md`,
  `research/grothendieck/checkers/xi_stieltjes_heat_trace_bridge.py`,
  `research/grothendieck/results/xi-stieltjes-heat-trace-bridge.json`.
- Logarithmic heat Weyl law and limitation:
  `research/grothendieck/xi-heat-weyl-law-and-limit.md`,
  `research/grothendieck/checkers/xi_heat_weyl_asymptotic.py`,
  `research/grothendieck/results/xi-heat-weyl-asymptotic.json`.
- Complete-Bernstein determinant unification:
  `research/grothendieck/xi-complete-bernstein-equivalence.md`,
  `research/grothendieck/checkers/xi_complete_bernstein_bridge.py`,
  `research/grothendieck/results/xi-complete-bernstein-bridge.json`.
- Explicit prime and endpoint heat kernels:
  `research/grothendieck/xi-prime-heat-kernel-and-coupling.md`,
  `research/grothendieck/checkers/xi_prime_heat_kernel_transform.py`,
  `research/grothendieck/results/xi-prime-heat-kernel-transform.json`.
- Explicit archimedean heat kernel:
  `research/grothendieck/xi-gamma-heat-kernel.md`,
  `research/grothendieck/checkers/xi_gamma_heat_kernel.py`,
  `research/grothendieck/results/xi-gamma-heat-kernel.json`.
- Completed source/spectral heat reconciliation:
  `research/grothendieck/xi-completed-heat-kernel-reconciliation.md`,
  `research/grothendieck/checkers/xi_completed_heat_kernel_reconciliation.py`,
  `research/grothendieck/results/xi-completed-heat-kernel-reconciliation.json`.
- Large-time PNT saddle cancellation:
  `research/grothendieck/xi-prime-heat-large-time-saddle.md`,
  `research/grothendieck/checkers/xi_prime_heat_saddle_main_term.py`,
  `research/grothendieck/results/xi-prime-heat-saddle-main-term.json`.
- Spectral heat versus de Bruijn--Newman audit:
  `research/grothendieck/xi-spectral-heat-vs-newman-flow.md`,
  `research/grothendieck/checkers/xi_two_heat_parameters_audit.py`,
  `research/grothendieck/results/xi-two-heat-parameters-audit.json`.
- Newman simple-zero velocity and heat derivative:
  `research/grothendieck/xi-newman-zero-velocity-and-heat-flow.md`,
  `research/grothendieck/checkers/xi_newman_zero_velocity.py`,
  `research/grothendieck/results/xi-newman-zero-velocity.json`.
- Newman discriminant Lyapunov theorem:
  `research/grothendieck/newman-discriminant-lyapunov-theorem.md`,
  `research/grothendieck/checkers/newman_discriminant_lyapunov.py`,
  `research/grothendieck/results/newman-discriminant-lyapunov.json`.
- Scale-normalized Newman discriminant:
  `research/grothendieck/newman-scale-normalized-discriminant.md`,
  `research/grothendieck/checkers/newman_scale_normalized_discriminant.py`,
  `research/grothendieck/results/newman-scale-normalized-discriminant.json`.
- Hermite-relative Newman entropy:
  `research/grothendieck/newman-hermite-relative-entropy.md`,
  `research/grothendieck/checkers/newman_hermite_relative_entropy.py`,
  `research/grothendieck/results/newman-hermite-relative-entropy.json`.
- Finite-window exterior entropy flux:
  `research/grothendieck/newman-window-entropy-flux.md`,
  `research/grothendieck/checkers/newman_window_entropy_flux.py`,
  `research/grothendieck/results/newman-window-entropy-flux.json`.
- Symmetric-window radial flux cancellation:
  `research/grothendieck/newman-symmetric-window-flux-cancellation.md`,
  `research/grothendieck/checkers/newman_symmetric_window_flux.py`,
  `research/grothendieck/results/newman-symmetric-window-flux.json`.
- Xi-window reference-shape falsifier and Weyl correction:
  `research/grothendieck/xi-window-hermite-reference-falsifier.md`,
  `research/grothendieck/checkers/xi_window_reference_shape.py`,
  `research/grothendieck/results/xi-window-reference-shape.json`.
- Affine-normalized Newman-flow rigidity:
  `research/grothendieck/newman-affine-normalization-rigidity.md`,
  `research/grothendieck/checkers/newman_affine_normalization_rigidity.py`,
  `research/grothendieck/results/newman-affine-normalization-rigidity.json`.
- Newman coordinate-change anomaly and affine rigidity:
  `research/grothendieck/newman-coordinate-change-anomaly.md`,
  `research/grothendieck/checkers/newman_coordinate_change_anomaly.py`,
  `research/grothendieck/results/newman-coordinate-change-anomaly.json`.
- Weyl-coordinate anomaly entropy balance:
  `research/grothendieck/newman-weyl-anomaly-entropy-balance.md`,
  `research/grothendieck/checkers/newman_weyl_anomaly_entropy.py`,
  `research/grothendieck/results/newman-weyl-anomaly-entropy.json`.
- Divided-difference coordinate cocycle and positivity no-go:
  `research/grothendieck/newman-divided-difference-cocycle.md`,
  `research/grothendieck/checkers/newman_divided_difference_cocycle.py`,
  `research/grothendieck/results/newman-divided-difference-cocycle.json`.
- Weyl-lattice arithmetic fluctuation entropy:
  `research/grothendieck/xi-weyl-lattice-fluctuation-entropy.md`,
  `research/grothendieck/checkers/xi_weyl_lattice_fluctuation.py`,
  `research/grothendieck/results/xi-weyl-lattice-fluctuation.json`.
- Tangent-renormalized Weyl-lattice coupled positivity:
  `research/grothendieck/xi-weyl-lattice-tangent-divergence.md`,
  `research/grothendieck/checkers/xi_weyl_lattice_tangent_divergence.py`,
  `research/grothendieck/results/xi-weyl-lattice-tangent-divergence.json`.
- Complex continuation no-go and Hermitian requirement:
  `research/grothendieck/xi-complex-lattice-divergence-no-go.md`,
  `research/grothendieck/checkers/xi_complex_lattice_divergence_no_go.py`,
  `research/grothendieck/results/xi-complex-lattice-divergence-no-go.json`.
- Convergent Hermitian RH reflection defect:
  `research/grothendieck/xi-hermitian-reflection-defect.md`,
  `research/grothendieck/checkers/xi_hermitian_reflection_defect.py`,
  `research/grothendieck/results/xi-hermitian-reflection-defect.json`.
- Self-adjoint Hilbert--Schmidt RH defect operator:
  `research/grothendieck/xi-reflection-defect-operator.md`,
  `research/grothendieck/checkers/xi_reflection_defect_operator.py`,
  `research/grothendieck/results/xi-reflection-defect-operator.json`.
- Conjugation-graph Mackey correspondence and C2 norm:
  `research/grothendieck/xi-conjugation-graph-correspondence.md`,
  `research/grothendieck/checkers/xi_conjugation_graph_correspondence.py`,
  `research/grothendieck/results/xi-conjugation-graph-correspondence.json`.
- Hermitian RH-defect heat bridge:
  `research/grothendieck/xi-hermitian-defect-heat-bridge.md`,
  `research/grothendieck/checkers/xi_hermitian_defect_heat_bridge.py`,
  `research/grothendieck/results/xi-hermitian-defect-heat-bridge.json`.
- Conjugation-graph separable-rank no-go:
  `research/grothendieck/xi-graph-projector-separable-rank-no-go.md`,
  `research/grothendieck/checkers/xi_graph_projector_separable_rank.py`,
  `research/grothendieck/results/xi-graph-projector-separable-rank.json`.
- Twisted spectral-copy dagger-Frobenius correspondence:
  `research/grothendieck/xi-spectral-copy-correspondence.md`,
  `research/grothendieck/checkers/xi_spectral_copy_correspondence.py`,
  `research/grothendieck/results/xi-spectral-copy-correspondence.json`.
- Fourier-dual spectral-copy/source-difference correspondence:
  `research/grothendieck/fourier-dual-copy-difference-correspondence.md`,
  `research/grothendieck/checkers/fourier_dual_copy_difference.py`,
  `research/grothendieck/results/fourier-dual-copy-difference.json`.
- Noncompact difference-correspondence Haar-volume obstruction:
  `research/grothendieck/difference-correspondence-noncompact-obstruction.md`,
  `research/grothendieck/checkers/difference_correspondence_noncompact.py`,
  `research/grothendieck/results/difference-correspondence-noncompact.json`.
- Relative difference quotient and arithmetic coefficient gate:
  `research/grothendieck/relative-difference-quotient-and-arithmetic-weight-gate.md`,
  `research/grothendieck/checkers/relative_difference_quotient.py`,
  `research/grothendieck/results/relative-difference-quotient.json`.
- Von Mangoldt divisor pushforward and logarithmic quotient cocycle:
  `research/grothendieck/von-mangoldt-divisor-cocycle.md`,
  `research/grothendieck/checkers/von_mangoldt_divisor_cocycle.py`,
  `research/grothendieck/results/von-mangoldt-divisor-cocycle.json`.
- Divisor-pushforward Hilbert norm obstruction:
  `research/grothendieck/divisor-pushforward-Hilbert-norm-obstruction.md`,
  `research/grothendieck/checkers/divisor_pushforward_hilbert_norm.py`,
  `research/grothendieck/results/divisor-pushforward-hilbert-norm.json`.
- Prime-exponent Euler-factorized divisor Hilbert metric:
  `research/grothendieck/prime-exponent-divisor-Hilbert-metric.md`,
  `research/grothendieck/checkers/prime_exponent_divisor_metric.py`,
  `research/grothendieck/results/prime-exponent-divisor-metric.json`.
- Odd-source skew-adjoint vanishing mechanism:
  `research/grothendieck/odd-source-skew-adjoint-vanishing-mechanism.md`,
  `research/grothendieck/checkers/odd_source_skew_adjoint.py`,
  `research/grothendieck/results/odd-source-skew-adjoint.json`.
- Translation-invariant compact-resolvent no-go:
  `research/grothendieck/translation-invariant-compact-resolvent-no-go.md`,
  `research/grothendieck/checkers/translation_invariant_compact_resolvent_no_go.py`,
  `research/grothendieck/results/translation-invariant-compact-resolvent-no-go.json`.
- Archimedean confinement plus odd-arithmetic coupling:
  `research/grothendieck/archimedean-confinement-odd-arithmetic-coupling.md`,
  `research/grothendieck/checkers/archimedean_confinement_coupling.py`,
  `research/grothendieck/results/archimedean-confinement-coupling.json`.
- Archimedean 7/8 boundary-phase gate:
  `research/grothendieck/archimedean-boundary-phase-gate.md`,
  `research/grothendieck/checkers/archimedean_boundary_phase.py`,
  `research/grothendieck/results/archimedean-boundary-phase.json`.
- Boundary real-structure phase-selection no-go:
  `research/grothendieck/boundary-real-structure-phase-no-go.md`,
  `research/grothendieck/checkers/boundary_real_structure_phase.py`,
  `research/grothendieck/results/boundary-real-structure-phase.json`.
- Metaplectic signature-one eighth-phase candidate:
  `research/grothendieck/metaplectic-eighth-phase-candidate.md`,
  `research/grothendieck/checkers/metaplectic_eighth_phase.py`,
  `research/grothendieck/results/metaplectic-eighth-phase.json`.
- Even-oscillator zeta determinant for the full gamma factor:
  `research/grothendieck/gamma-factor-even-oscillator-determinant.md`,
  `research/grothendieck/checkers/gamma_even_oscillator_determinant.py`,
  `research/grothendieck/results/gamma-even-oscillator-determinant.json`.
- Prime Fredholm determinant and critical-line Schatten gate:
  `research/grothendieck/prime-fredholm-determinant-and-critical-line-gate.md`,
  `research/grothendieck/checkers/prime_fredholm_determinant.py`,
  `research/grothendieck/results/prime-fredholm-determinant.json`.
- Third regularized prime determinant information gate:
  `research/grothendieck/prime-third-determinant-information-gate.md`,
  `research/grothendieck/checkers/prime_third_determinant.py`,
  `research/grothendieck/results/prime-third-determinant.json`.
- Smoothed prime Hermitian norm and phase-blindness gate:
  `research/grothendieck/smoothed-prime-Hermitian-norm-gate.md`,
  `research/grothendieck/checkers/smoothed_prime_hermitian_norm.py`,
  `research/grothendieck/results/smoothed-prime-Hermitian-norm.json`.
- Prime-valuation phase energy and zero-set no-go:
  `research/grothendieck/prime-valuation-phase-energy-no-go.md`,
  `research/grothendieck/checkers/prime_valuation_phase_energy.py`,
  `research/grothendieck/results/prime-valuation-phase-energy.json`.
- Euler-local zero-production no-go:
  `research/grothendieck/Euler-local-zero-no-go.md`,
  `research/grothendieck/checkers/euler_local_zero_no_go.py`,
  `research/grothendieck/results/Euler-local-zero-no-go.json`.
- Paired archimedean--arithmetic gluing determinant:
  `research/grothendieck/paired-gluing-determinant-mechanism.md`,
  `research/grothendieck/checkers/paired_gluing_determinant.py`,
  `research/grothendieck/results/paired-gluing-determinant.json`.
- Global transfer contractivity conjecture and hostile quartet:
  `research/grothendieck/global-transfer-contractivity-conjecture.md`,
  `research/grothendieck/checkers/global_transfer_contractivity.py`,
  `research/grothendieck/results/global-transfer-contractivity.json`.
- de Branges--Rovnyak transfer-kernel positivity target:
  `research/grothendieck/de-branges-transfer-kernel-target.md`,
  `research/grothendieck/checkers/de_branges_transfer_kernel.py`,
  `research/grothendieck/results/de-branges-transfer-kernel.json`.
- Canonical xi log-derivative Herglotz kernel:
  `research/grothendieck/xi-log-derivative-Herglotz-kernel.md`,
  `research/grothendieck/checkers/xi_log_derivative_herglotz_kernel.py`,
  `research/grothendieck/results/xi-log-derivative-Herglotz-kernel.json`.
- Completed source Herglotz-kernel sign and transport gate:
  `research/grothendieck/completed-source-Herglotz-kernel-gate.md`,
  `research/grothendieck/checkers/completed_source_herglotz_kernel.py`,
  `research/grothendieck/results/completed-source-Herglotz-kernel.json`.
- Krein graph completion and null-state determinant theorem:
  `research/grothendieck/Krein-graph-completion-theorem.md`,
  `research/grothendieck/checkers/Krein_graph_completion.py`,
  `research/grothendieck/results/Krein-graph-completion.json`.
- Positive gluing determinant square-root/Pfaffian gate:
  `research/grothendieck/positive-gluing-determinant-square-root-gate.md`,
  `research/grothendieck/checkers/positive_gluing_square_root_gate.py`,
  `research/grothendieck/results/positive-gluing-square-root-gate.json`.
- Pfaffian noncircularity and global-orientation gate:
  `research/grothendieck/pfaffian-noncircularity-gate.md`,
  `research/grothendieck/checkers/pfaffian_noncircularity_gate.py`,
  `research/grothendieck/results/pfaffian-noncircularity-gate.json`.
- Finite-cutoff algebraic Pfaffian-lift no-go:
  `research/grothendieck/finite-cutoff-pfaffian-lift-no-go.md`,
  `research/grothendieck/checkers/finite_cutoff_pfaffian_lift_no_go.py`,
  `research/grothendieck/results/finite-cutoff-pfaffian-lift-no-go.json`.
- Quaternionic square-forcing mechanism and Xi-reflection falsifier:
  `research/grothendieck/quaternionic-square-forcing-gate.md`,
  `research/grothendieck/checkers/quaternionic_square_forcing_gate.py`,
  `research/grothendieck/results/quaternionic-square-forcing-gate.json`.
- Oriented first-order factorization and chiral self-adjoint target:
  `research/grothendieck/oriented-first-order-factorization-target.md`,
  `research/grothendieck/checkers/oriented_first_order_factorization.py`,
  `research/grothendieck/results/oriented-first-order-factorization.json`.
- Relative-complement incidence factorization of the Mackey defect:
  `research/grothendieck/relative-complement-incidence-factorization.md`,
  `research/grothendieck/checkers/relative_complement_incidence_factorization.py`,
  `research/grothendieck/results/relative-complement-incidence-factorization.json`.
- Rank-one Parseval phase explanatory no-go:
  `research/grothendieck/rank-one-parseval-phase-no-go.md`,
  `research/grothendieck/checkers/rank_one_parseval_phase_no_go.py`,
  `research/grothendieck/results/rank-one-parseval-phase-no-go.json`.
- Minimal two-channel four-cycle interference target:
  `research/grothendieck/two-channel-cycle-interference-target.md`,
  `research/grothendieck/checkers/two_channel_cycle_interference.py`,
  `research/grothendieck/results/two-channel-cycle-interference.json`.
- Operator-valued type correction for the two-channel square:
  `research/grothendieck/two-channel-operator-valued-type-correction.md`,
  `research/grothendieck/checkers/two_channel_operator_rank_no_go.py`,
  `research/grothendieck/results/two-channel-operator-valued-type-correction.json`.
- Conjugation-graph determinant-class and Schatten gate:
  `research/grothendieck/conjugation-graph-determinant-class-gate.md`,
  `research/grothendieck/checkers/conjugation_graph_determinant_class.py`,
  `research/grothendieck/results/conjugation-graph-determinant-class.json`.
- Two low-order prime channels isolated by the third determinant:
  `research/grothendieck/two-low-order-channel-anomaly-target.md`,
  `research/grothendieck/checkers/two_low_order_channel_anomaly.py`,
  `research/grothendieck/results/two-low-order-channel-anomaly.json`.
- Quadratic prime channel as a degree-two Mackey anomaly:
  `research/grothendieck/quadratic-prime-channel-mackey-anomaly.md`,
  `research/grothendieck/checkers/quadratic_prime_channel_mackey_anomaly.py`,
  `research/grothendieck/results/quadratic-prime-channel-mackey-anomaly.json`.
- Finite norm-torsion quadratic-exponential no-go:
  `research/grothendieck/finite-norm-torsion-quadratic-exponential-no-go.md`,
  `research/grothendieck/checkers/finite_norm_torsion_quadratic_exponential_no_go.py`,
  `research/grothendieck/results/finite-norm-torsion-quadratic-exponential-no-go.json`.
- Gaussian quadratic-channel and Cameron--Martin gate:
  `research/grothendieck/gaussian-quadratic-channel-cameron-martin-gate.md`,
  `research/grothendieck/checkers/gaussian_quadratic_channel_gate.py`,
  `research/grothendieck/results/gaussian-quadratic-channel-cameron-martin-gate.json`.
- Logarithmic prime--oscillator relative covariance cancellation:
  `research/grothendieck/logarithmic-prime-oscillator-covariance-cancellation.md`,
  `research/grothendieck/checkers/logarithmic_prime_oscillator_covariance.py`,
  `research/grothendieck/results/logarithmic-prime-oscillator-covariance-cancellation.json`.
- Prime--oscillator diagonal-intertwiner no-go:
  `research/grothendieck/prime-oscillator-intertwiner-no-go.md`,
  `research/grothendieck/checkers/prime_oscillator_intertwiner_no_go.py`,
  `research/grothendieck/results/prime-oscillator-intertwiner-no-go.json`.
- Prime--oscillator semigroup incidence kernel:
  `research/grothendieck/prime-oscillator-semigroup-incidence-kernel.md`,
  `research/grothendieck/checkers/prime_oscillator_semigroup_incidence.py`,
  `research/grothendieck/results/prime-oscillator-semigroup-incidence-kernel.json`.
- Semigroup-kernel Schur-weight mismatch and paired-resolvent correction:
  `research/grothendieck/semigroup-kernel-schur-weight-mismatch.md`,
  `research/grothendieck/checkers/semigroup_kernel_schur_weight_mismatch.py`,
  `research/grothendieck/results/semigroup-kernel-schur-weight-mismatch.json`.
- Finite Euler cross-Weyl positivity and infinite diagonal no-go:
  `research/grothendieck/finite-euler-cross-weyl-positivity-and-diagonal-no-go.md`,
  `research/grothendieck/checkers/finite_euler_cross_weyl_positivity.py`,
  `research/grothendieck/results/finite-euler-cross-weyl-positivity.json`.
- Von Mangoldt metric divergence-matching gate:
  `research/grothendieck/von-mangoldt-metric-divergence-matching-gate.md`,
  `research/grothendieck/checkers/von_mangoldt_metric_divergence_matching.py`,
  `research/grothendieck/results/von-mangoldt-metric-divergence-matching-gate.json`.
- Weighted coefficient--Betti Mackey adjunction gate:
  `research/grothendieck/weighted-coefficient-betti-mackey-adjunction-gate.md`,
  `research/grothendieck/checkers/weighted_coefficient_betti_mackey_adjunction.py`,
  `research/grothendieck/results/weighted-coefficient-betti-mackey-adjunction-gate.json`.
- Valuation normalization deriving the von Mangoldt metric:
  `research/grothendieck/valuation-normalization-derives-von-mangoldt-metric.md`,
  `research/grothendieck/checkers/valuation_normalized_von_mangoldt_metric.py`,
  `research/grothendieck/results/valuation-normalization-derives-von-mangoldt-metric.json`.
- Prime-ray incomplete tensor-product sector obstruction:
  `research/grothendieck/prime-ray-incomplete-tensor-sector-obstruction.md`,
  `research/grothendieck/checkers/prime_ray_incomplete_tensor_sector.py`,
  `research/grothendieck/results/prime-ray-incomplete-tensor-sector-obstruction.json`.
- Prime--gamma rank/trace incompatibility:
  `research/grothendieck/prime-gamma-rank-trace-incompatibility.md`,
  `research/grothendieck/checkers/prime_gamma_rank_trace_incompatibility.py`,
  `research/grothendieck/results/prime-gamma-rank-trace-incompatibility.json`.
- Quarter-shifted prime-shell trace-class correspondence:
  `research/grothendieck/quarter-shifted-prime-shell-trace-class-correspondence.md`,
  `research/grothendieck/checkers/quarter_shifted_prime_shell_correspondence.py`,
  `research/grothendieck/results/quarter-shifted-prime-shell-trace-class-correspondence.json`.
- Rank-one prime-shell height-dynamics no-go:
  `research/grothendieck/single-radial-shell-height-dynamics-no-go.md`,
  `research/grothendieck/checkers/single_radial_shell_height_dynamics.py`,
  `research/grothendieck/results/single-radial-shell-height-dynamics-no-go.json`.
- Fixed finite-rank prime-shell height-dynamics no-go:
  `research/grothendieck/fixed-finite-rank-shell-height-dynamics-no-go.md`,
  `research/grothendieck/checkers/fixed_finite_rank_shell_height_no_go.py`,
  `research/grothendieck/results/fixed-finite-rank-shell-height-no-go.json`.
- Growing prime-shell moment-rank summability schedule:
  `research/grothendieck/growing-shell-rank-summability-schedule.md`.
- Universal positive determinant of shell-kernel leakage:
  `research/grothendieck/shell-kernel-coupled-positivity-theorem.md`,
  `research/grothendieck/checkers/shell_kernel_coupled_positivity.py`,
  `research/grothendieck/results/shell-kernel-coupled-positivity.json`.
- Two-ray native shell determinant falsifier:
  `research/grothendieck/two-ray-shell-schur-determinant-falsifier.md`,
  `research/grothendieck/checkers/two_ray_shell_schur_falsifier.py`,
  `research/grothendieck/results/two-ray-shell-schur-determinant-falsifier.json`.
- Zero-free spectral role of the positive shell-leakage factor:
  `research/grothendieck/shell-leakage-positive-factor-zero-free-gate.md`.
- Quarter-shifted retained moment Jacobi generator:
  `research/grothendieck/quarter-shifted-moment-jacobi-operator.md`,
  `research/grothendieck/checkers/quarter_shifted_moment_jacobi.py`,
  `research/grothendieck/results/quarter-shifted-moment-jacobi.json`.
- Riemann--von Mangoldt shell-rank density gate:
  `research/grothendieck/riemann-weyl-law-forces-logarithmic-shell-rank.md`,
  `research/grothendieck/checkers/riemann_weyl_shell_rank.py`,
  `research/grothendieck/results/riemann-weyl-shell-rank.json`.
- Cumulative integer Weyl-rank allocation and constant-term gate:
  `research/grothendieck/cumulative-weyl-shell-rank-allocation.md`,
  `research/grothendieck/checkers/cumulative_weyl_shell_ranks.py`,
  `research/grothendieck/results/cumulative-weyl-shell-ranks.json`.
- Quarter-shift derivation of the seven-eighths Weyl constant:
  `research/grothendieck/quarter-shift-derives-seven-eighths-boundary-constant.md`,
  `research/grothendieck/checkers/quarter_shift_seven_eighths.py`,
  `research/grothendieck/results/quarter-shift-seven-eighths.json`.
- Prime-coupling spectral-shift target:
  `research/grothendieck/prime-coupling-spectral-shift-target.md`,
  `research/grothendieck/checkers/finite_spectral_shift_phase.py`,
  `research/grothendieck/results/finite-spectral-shift-phase.json`.
- Localization of the zero-producing spectral shift to the first two prime
  channels:
  `research/grothendieck/spectral-shift-localizes-to-two-channel-anomaly.md`.
- Identically-zero gluing determinant for normalized isometric shell maps:
  `research/grothendieck/isometric-shell-gluing-identically-zero-no-go.md`,
  `research/grothendieck/checkers/isometric_shell_gluing_no_go.py`,
  `research/grothendieck/results/isometric-shell-gluing-no-go.json`.
- Full moment-generator boundary leakage no-go and growing-rank scope
  correction:
  `research/grothendieck/growing-moment-generator-boundary-no-go.md`,
  `research/grothendieck/checkers/growing_moment_generator_boundary_no_go.py`,
  `research/grothendieck/results/growing-moment-generator-boundary-no-go.json`.
- Weyl-rank versus soft-cutoff Hilbert--Schmidt tradeoff:
  `research/grothendieck/soft-moment-cutoff-weyl-tradeoff-no-go.md`,
  `research/grothendieck/checkers/soft_moment_cutoff_weyl_tradeoff.py`,
  `research/grothendieck/results/soft-moment-cutoff-weyl-tradeoff.json`.
- Acyclic auxiliary-tail cancellation and Schur self-energy:
  `research/grothendieck/acyclic-tail-schur-self-energy-mechanism.md`,
  `research/grothendieck/checkers/acyclic_tail_schur_self_energy.py`,
  `research/grothendieck/results/acyclic-tail-schur-self-energy.json`.
- Single-Schur-operator derivation of the linear and quadratic anomaly
  coefficients:
  `research/grothendieck/schur-logarithm-unifies-two-prime-channels.md`,
  `research/grothendieck/checkers/schur_logarithm_two_channels.py`,
  `research/grothendieck/results/schur-logarithm-two-channels.json`.
- Quadratic shell-phase resonance lattice:
  `research/grothendieck/quadratic-shell-phase-resonance-lattice.md`,
  `research/grothendieck/checkers/quadratic_shell_phase_resonance.py`,
  `research/grothendieck/results/quadratic-shell-phase-resonance.json`.
- Linear--quadratic odd-resonance parity no-go:
  `research/grothendieck/linear-quadratic-shell-resonance-parity-no-go.md`,
  `research/grothendieck/checkers/linear_quadratic_resonance_parity.py`,
  `research/grothendieck/results/linear-quadratic-resonance-parity.json`.
- Adams-doubling alignment of the two shell anomaly channels:
  `research/grothendieck/adams-doubling-aligns-shell-anomaly-channels.md`,
  `research/grothendieck/checkers/adams_doubling_shell_anomaly.py`,
  `research/grothendieck/results/adams-doubling-shell-anomaly.json`.
- Regulator-invariant relative finite part at the Adams boundary:
  `research/grothendieck/adams-boundary-relative-finite-part-regulator-invariance.md`,
  `research/grothendieck/checkers/adams_boundary_relative_finite_part.py`,
  `research/grothendieck/results/adams-boundary-relative-finite-part.json`.
- Gamma-resolvent versus shell-time-phase type correction:
  `research/grothendieck/gamma-resolvent-versus-shell-time-phase-type-correction.md`.
- Log-time Fourier bridge from prime atoms to gamma resolvents:
  `research/grothendieck/log-time-fourier-bridge-prime-atoms-gamma-resolvent.md`,
  `research/grothendieck/checkers/log_time_fourier_gamma_resolvent.py`,
  `research/grothendieck/results/log-time-fourier-gamma-resolvent.json`.
- Identification of the completed log-time bridge with the Weil form and
  restoration of the prime-two gluing gate:
  `research/grothendieck/log-time-bridge-identifies-weil-form-and-prime-two-gate.md`.
- Edgewise contraction versus three-cell Weil gluing no-go:
  `research/grothendieck/edgewise-weil-contractions-do-not-glue-triangles.md`,
  `research/grothendieck/checkers/edgewise_contraction_triangle_no_go.py`,
  `research/grothendieck/results/edgewise-contraction-triangle-no-go.json`.
- Three-cell Adams composition-defect positivity theorem:
  `research/grothendieck/three-cell-adams-defect-positivity-theorem.md`,
  `research/grothendieck/checkers/three_cell_adams_defect_positivity.py`,
  `research/grothendieck/results/three-cell-adams-defect-positivity.json`.
- One-prime all-length Adams tower positivity theorem:
  `research/grothendieck/one-prime-adams-tower-positive-gluing-theorem.md`,
  `research/grothendieck/checkers/one_prime_adams_tower_positivity.py`,
  `research/grothendieck/results/one-prime-adams-tower-positivity.json`.
- Coprime Adams/Mackey tensor-gluing theorem and mixed-prime gate:
  `research/grothendieck/coprime-adams-tensor-gluing-theorem.md`,
  `research/grothendieck/checkers/coprime_adams_tensor_gluing.py`,
  `research/grothendieck/results/coprime-adams-tensor-gluing.json`.
- Mixed-prime rectangle parity positivity theorem:
  `research/grothendieck/mixed-prime-rectangle-parity-positivity-theorem.md`,
  `research/grothendieck/checkers/mixed_prime_rectangle_parity.py`,
  `research/grothendieck/results/mixed-prime-rectangle-parity.json`.
- Squarefree prime-cube Walsh positivity theorem:
  `research/grothendieck/squarefree-prime-cube-walsh-positivity-theorem.md`,
  `research/grothendieck/checkers/squarefree_prime_cube_walsh.py`,
  `research/grothendieck/results/squarefree-prime-cube-walsh.json`.
- Von Mangoldt support obstruction to arithmetic tensor interchange:
  `research/grothendieck/von-mangoldt-support-falsifies-arithmetic-tensor-interchange.md`,
  `research/grothendieck/checkers/von_mangoldt_tensor_interchange_no_go.py`,
  `research/grothendieck/results/von-mangoldt-tensor-interchange-no-go.json`.
- Graph admission certifies policy-valid shared memory, not mathematical
  truth.
### Additive squarefree-edge budget

The logarithmic derivative does not realize coprime tensor interchange:
`Lambda(pq)=0` for distinct primes although both prime edges are present. On a
squarefree cube with only identity and single-prime correlations, exact Walsh
diagonalization gives

```
lambda_eta = 1 + sum_j (-1)^(eta_j) r_j,
```

so positivity is equivalent to the sharp shared budget
`sum_j |r_j|<=1`. This replaces the false intuition that separately
contractive prime edges glue automatically. Since raw von Mangoldt edge
weights are not `l1` over primes, the archimedean/endpoint sector must supply
scale-dependent diagonal energy, legitimate mixed Schur correlations, or
test-geometric cancellation. The finite falsifier is any normalized prime
set whose absolute edge sum exceeds one.

The abstract completion problem is nevertheless exact and favorable. With
diagonal `D`, prescribed single-prime edges admit a positive squarefree-cube
completion iff `max_j |r_j|<=D`; a product completion supplies all higher
mixed correlations and factors every Walsh eigenvalue. The explanatory gap is
therefore no longer generic matrix positivity. It is the source question of
whether gamma/endpoint or mapping-cone terms canonically supply those mixed
coefficients while the arithmetic summand continues to satisfy
`Lambda(pq)=0`. This separates a solved finite extension theorem from the
still-open completed-Weil realization theorem.

There is also a natural non-product completion aligned with the gamma
resolvent. Put all prime contractions over one positive latent log-time scale
and define each mixed coefficient as the moment of the product of its prime
features. Walsh eigenvalues then factor pointwise inside a positive integral.
For features `p^(-u)`, mixed coefficients belong to the continuous
archimedean sector, not to von Mangoldt support. Bounded cutoffs of the gamma
Laplace density realize this theorem exactly. What remains is the decisive
source gate: absorb its logarithmic endpoint divergence and the negatively
signed prime evaluations together into a positive Schur dilation.
### Endpoint-centered gamma defect space

The singular gamma log-time density becomes a canonical positive Hilbert
sector after replacing constants by differences `v_n(u)=1-n^(-u)`. These
vectors are square-integrable at both endpoints, and their Gram cross term
contains `(pq)^(-u)` by polarization. Thus a mixed squarefree correlation is
source-derived from the continuous archimedean sector without changing
`Lambda(pq)=0`. The remaining gate is to realize the negatively signed prime
evaluation map as a contraction, or as part of a positive Schur compression,
relative to this centered gamma space.
### First prime-coupling falsifier

Typing each von Mangoldt weight as an independent negative diagonal penalty
on the endpoint-centered gamma prime vectors fails immediately. Although the
individual `2` and `3` diagonal energies remain positive, their coupled
determinant is approximately `-1.9565`, with a controlled series-tail error.
This does not test the actual Weil form; it rules out the orthogonal-penalty
surrogate. Any viable source model must preserve the coupled prime-power
translation or incidence operator before taking its Schur complement.
### Correct source type of the prime term

The von Mangoldt contribution is a self-adjoint paired-translation adjacency,
not a negative norm with one orthogonal coordinate per prime. Its finite
Fourier symbol is a cosine polynomial, and the squarefree Walsh norm is the
sum of the absolute prime-edge weights. Prime powers remain harmonics of the
same phase. Consequently the decisive comparison is
`H_arch-A_prime>=0` on one common log-time representation (or a dilation of
that difference), with endpoint terms retained.
### Euler-ray resummation and global typing

The entire Adams tower over one prime resums to a rational Poisson-type
cosine symbol. Its positive and negative extrema are unequal, so the
squarefree `C2` quotient is only a first-power diagnostic. At finite global
cutoff every prime-power phase aligns at `t=0`, attaining the sum of all
weights; this grows without bound. Therefore the global target cannot be a
bounded difference of separately defined gamma and prime multipliers. It must
be the completed quadratic-form or relative-operator limit under one common
smoothing and endpoint prescription.
### Smoothed adjacency and the scalar heat gate

The log-Gaussian cutoff makes the paired prime adjacency bounded at every
positive heat time. Its norm is attained at the zero translation character,
and the known negative prime heat kernel is exactly this zero-character value
times the inverse-Laplace prefactor. This identifies the common arithmetic
object while separating two claims: all-time scalar heat complete
monotonicity is the Stieltjes/RH route, whereas a self-adjoint translation
construction requires positivity across every Fourier character or an
equivalent dilation. Scalar pointwise positivity alone is weaker.
### Full Gaussian Weil character kernel

Gaussian smoothing of the complete centered Weil distribution yields a
two-variable character kernel. On the spectral side under RH it is the
positive mixture `(1/2)sum_(gamma signed) m_gamma
exp(-t(xi-gamma)^2)`; the earlier positive-ordinate heat trace is exactly its
zero-character slice. On the arithmetic side the prime
term is the Gaussian-damped cosine adjacency. All-character positivity, with
the limiting test-space argument supplied, is therefore another
RH-equivalent Weil formulation and is the correct GNS kernel target. The next
calculation is the nonzero-character endpoint-plus-gamma source formula.
### Explicit shifted-Gaussian source identity

The nonzero-character completion is now written entirely in source terms.
Its endpoint is `e^(t/4-t xi^2)cos(t xi)`, its gamma term is the shifted
Gaussian average of the digamma boundary symbol, and its arithmetic term is
the damped von Mangoldt cosine sum. The spectral normalization is half the
signed symmetric divisor, recovering the positive-ordinate heat trace at
`xi=0`. Proving this completed source sum nonnegative for all `(t,xi)` is the
sharpened Weil/GNS target; positivity itself remains open.
### Weil Gaussian smoothing threshold

Writing `sigma=1/(4t)` turns the full character kernel into forward Gaussian
convolution of the Weil spectral distribution. Positivity is monotone toward
larger variance, whereas the RH-relevant sharp limit is the backward-heat
direction. The exact signed model `delta_-1+delta_1-delta_0` becomes positive
only for `sigma>=1/(4 log 2)`, showing why broad heat positivity cannot see a
negative spectral atom. This motivates a source-defined smoothing threshold;
RH is its zero-threshold case, not an identification with Newman time.
### First-contact reduction

If a nonzero completed Gaussian kernel has a positive smoothing threshold and
the loss of positivity is attained at finite character, it must occur through
`Theta=partial_xi Theta=0`; heat curvature and the variance derivative are
nonnegative there. At every broader variance strict positivity follows from
Gaussian convolution. The source program can therefore target simultaneous
value/derivative zeros, provided broad positivity and non-escape of the
minimizing character are independently established.
### Archimedean character confinement

At fixed positive smoothing time, the shifted digamma average grows like
`log|xi|/(4sqrt(pi t))`. The endpoint term decays and the smoothed prime
adjacency is uniformly bounded in character. The full source kernel is thus
coercive and attains its minimum at finite `xi`. This removes escape to
spectral infinity from the first-contact alternatives; broad positivity and
exclusion of a finite double contact remain the active gates.
### Uniform broad-smoothing positivity

For sufficiently small inverse time `t`, the shifted gamma average is
uniformly dominated by the positive Weyl term
`log(1/t)/(8sqrt(pi t))`. The endpoint remains bounded and the entire prime
cosine series is exponentially suppressed by the first displacement
`log 2`. Thus the all-character source kernel is unconditionally positive in
a broad-smoothing regime. Together with character confinement, any failure of
RH must now appear as a finite double contact at a positive smoothing
threshold.
### Off-line quartet contact mechanism

An off-critical quartet contributes a real oscillatory Gaussian multiplied by
`e^(t alpha^2)`. It has an exact negative lobe at every scale, and that lobe
ceases to be exponentially suppressed near `t alpha^2=pi/2`. Thus Gaussian
character smoothing detects distance from the line on an `alpha^(-2)` scale,
unlike Li-rank tests. In the full kernel, broad positivity can initially hide
the lobe, but continuity and confinement force its eventual appearance
through the finite double-contact mechanism.
### Prime moment ellipse at contact

The positive smoothed von Mangoldt measure constrains its cosine value and
sine derivative by
`R^2/M_0^2+I_1^2/(M_0M_2)<=1`. A completed double contact prescribes both
quantities from the endpoint-plus-gamma value and slope, so violation of the
resulting archimedean ellipse excludes contact without resolving individual
prime phases. This attacks nonzero characters; the zero character
automatically saturates the ellipse and remains the scalar heat gate.

A fourth-moment covariance bound additionally traps the second cosine moment
that enters `partial_xi^2 Theta`. Since first contact requires nonnegative
heat curvature, this supplies a second exclusion layer after the value--slope
ellipse. Any surviving contact must satisfy all three moment conditions.
A full prime-phase moment hierarchy now contains the ellipse and curvature
tests. At every order, ordinary and character-twisted von Mangoldt moments
form a positive block Hankel Gram matrix. Archimedean contact jets partially
specify this matrix; infeasible positive completion excludes contact. This is
a nested exact falsifier hierarchy, not a proof from finite truncation.

The hierarchy has an exact variance flow. The scalar prime load is completely
monotone; all even moments are its alternating derivatives. Its normalized
squared displacement decreases by the variance of `(log n)^2`, and every
Hankel block decreases in Loewner order as smoothing broadens. This gives the
contact program one canonical arithmetic evolution rather than unrelated
cutoffs.

The total negative mass of the completed character kernel is a canonical
defect entropy. It is finite by archimedean confinement and nonincreasing
under forward heat smoothing. At a generic first tangency it is born on the
sharp side with a universal `3/2` power law determined by contact curvature.
This provides a robust quantitative falsifier beyond pointwise sign scans.

Degenerate contacts resolve by universal Hermite profiles. A first nonzero
spatial jet of order `2m` yields negative-mass onset
`(sigma_*-sigma)^(m+1/2)`. Hence the defect entropy distinguishes generic
double tangency from higher-order fine tuning and connects the Weil contact
lane to Hermite collision normal forms without conflating its heat parameter
with Newman deformation.

### Scalar heat positivity correction

Pointwise positivity of the zero-character heat kernel is only the ordinary
Bernstein gate. The Stieltjes/RH gate requires complete monotonicity in heat
time. A strictly positive oscillatory kernel can have conjugate off-axis
Laplace poles, so a clean scalar sign scan cannot certify RH. This correction
does not affect the full all-character Gaussian criterion, whose positivity
at every variance recovers a positive Weil distribution by an approximate
identity.

The corrected scalar source target is an explicit Laguerre hierarchy.
The `k`th alternating time derivative of each prime log-Gaussian contains
`k!L_k^(-1/2)((log n)^2/(4t))`; endpoint and gamma terms must be differentiated
and combined at the same order. These polynomials change sign, so no sector
has an independent positivity interpretation. RH requires the completed
inequality at every order, not merely the heat-kernel sign.

The derivative sequence must also come from one common positive measure.
Accordingly its ordinary and shifted Hankel matrices must be positive. The
first determinant is the completed heat trace squared times the variance of
the tilted squared spectrum, yielding strict log-convexity and a nonlinear
source test stronger than entrywise derivative signs. Higher Hankel minors
provide the coupled scalar hierarchy.

The continuous heat-time quantifier can be removed. Complete ordinary and
shifted Hankel positivity for the derivative sequence at one chosen `t_0`,
together with exponential moment convergence up to radius `t_0`, reconstructs
the positive Laplace measure and hence complete monotonicity on all positive
times. The scalar attack is now one all-order source Gram problem plus one
growth theorem.

In the Xi source class, right-half-plane holomorphy supplies that growth
theorem automatically: the Taylor radius at `t_0` reaches the boundary
`t=0`, and positive Hankel diagonals turn Taylor convergence into the needed
exponential moment bound. Hence one complete ordinary/shifted Hankel
hierarchy at one chosen time is the scalar RH-equivalent target.

High derivative order is what restores sensitivity lost by scalar heat
positivity. A tiny off-axis exponential is multiplied by the modulus of its
complex rate to the `k`th power and eventually forces a negative derivative;
the latency is logarithmic in inverse defect amplitude. The corresponding
Laguerre source term probes primes out to
`exp[O(sqrt(k t_0))]`, so fixed-time localization does not remove arithmetic
depth—it organizes it subexponentially by order.

The one-time hierarchy directly constructs a canonical positive Jacobi
operator: complete polynomials in the Hankel inner product and close
multiplication by the squared coordinate. Exponential determinacy makes the
closure self-adjoint; Xi meromorphy identifies the untwisted spectral support
with squared ordinates. The first Hankel determinant is the square of the
first Jacobi off-diagonal coefficient. This realizes a conditional
Hilbert--Polya operator while preserving the scalar multiplicity obstruction.

Equivalently, the whole scalar hierarchy is reflection positivity of the
time-addition kernel `Theta(t_0+s+u)` and its generator-shifted companion
`-Theta'(t_0+s+u)`. A single semigroup Gram factorization with positive
generator proves all Hankel minors and constructs the Jacobi operator. Its
smallest falsifier is a negative two-time determinant.

The endpoint term isolates the role of the shifted kernel. Its heat factor
`e^(t/4)` is an ordinary rank-one positive Gram but corresponds to spectral
value `-1/4`; `-partial_t` makes its shifted Gram negative immediately. The
completed prime--gamma system must therefore cancel a negative generator
direction, not merely add positive ordinary sectors.

That cancellation has a canonical source cone. The endpoint resolvent pole at
`x=1/4` and the principal pole of `zeta'/zeta` carry opposite residues; the
two-term identity complex is acyclic, while a regular finite coupling remains.
On the reflected zero branch, the elementary pole pairs with the gamma pole;
both charts describe the same completed squared-coordinate cancellation.
The ordinary and shifted Grams must be formed only after this pole-pair
reduction. This is an algebraic/analytic mapping cone, not a claimed physical
relative-chain pushforward.

After pole reduction, the finite boundary coupling is fixed exactly:
`S(1/4)=1+EulerGamma/2-log(2sqrt(pi))`, about `0.0230957`. Its small positive
value is the remainder of order-one endpoint, zeta, gamma, and pi terms and
admits no adjustable counterterm. It is now a normalization checkpoint for
the reduced reflection-positive/Jacobi construction.

At that same quarter point, the complete Taylor jet transforms to a compact
Hausdorff moment problem: `A_k=(-1)^kS^(k)(1/4)/k!` is the `k`th moment of
`u=1/(1/4+lambda)` on `[0,4]`. Ordinary, lower-support, and upper-support
Hankel localizers are jointly equivalent to the Stieltjes/RH property. Compact
support gives determinacy automatically, making this the preferred scalar
one-point Gram target.

The first source jets have closed formulas. They give approximately
`A_1=3.7101e-5`, `A_2=1.4368e-7`, and first Hankel determinant
`1.9419e-9`, all positive after cancellation among Stieltjes, gamma, pi, and
zeta(3) constants. This is encouraging but only a low-order regression; the
small determinant is not yet interval-certified and finite positivity cannot
establish RH.

The fourth quarter-point jet completes the first lower- and upper-support
Hausdorff localizers. Their binary-float determinants are approximately
`3.8367e-15` and `3.1031e-8`, respectively. The exceptionally small lower
margin supplies a concrete next falsifier: certify its sign with directed
rounding, then extend the localizer corner. These finite checks remain far
short of RH; the decimal signs are not interval-certified. See
`research/grothendieck/quarter-point-first-localizer-determinants.md` and its
checker/result pair.

Exact-rational interval propagation further shows that independent radius
`10^-12` enclosures of the four completed source coefficients force both
localizer signs. This is a conditional arithmetic certificate, not yet an
analytic one: rigorous enclosures for the Stieltjes-derived inputs remain to
be supplied.

Those inputs have now been reduced from Laurent data to regular Dirichlet eta
jets. Multiplication by `1-2^(1-s)` cancels the zeta pole algebraically, and a
triangular coefficient system reconstructs `gamma_0,...,gamma_3` from
`eta(1),...,eta^(4)(1)` and `log 2`. The next rigorous step is a
directed-rounding monotone-tail enclosure of this regular eta jet.

The unaccelerated route is infeasible: its elementary fourth-derivative
alternating remainder requires a cutoff near `3.31e18` for `10^-12` accuracy.
Certification therefore needs an accelerated tail with an explicit remainder
theorem, such as alternating Euler--Maclaurin.

A finite Euler acceleration now supplies that theorem. Exact derivative-sign
polynomials show that 60 transforms beginning at `N=10000` bound every eta-jet
tail through order four by less than `10^-100`. The astronomical raw cutoff
has therefore collapsed to a finite logarithmic prefix; only its
directed-rounding transcendental enclosure remains.

That finite enclosure is now implemented: correctly rounded 80-digit decimal
logs, outward arithmetic, and the proved Euler remainder enclose all eta
derivatives through order four in boxes narrower than `2.5e-75`. No zero
locations or imported Stieltjes constants enter. Composing these intervals
through the triangular and completed-source formulas is the remaining step to
an end-to-end first-localizer certificate.

The end-to-end composition is now complete. Exact-rational Machin and Apery
enclosures supply `pi` and `zeta(3)`; outward arithmetic carries the eta boxes
through the Stieltjes constants, completed jets, moments, and localizers. The
certified determinant intervals have positive lower bounds
`3.83670803159143268259e-15` and `3.103052637561763441065e-8`. This is the
first unconditional complete finite Hausdorff corner, obtained without zero
locations. It is not RH: the conjecture requires every localizer order.

The same certification architecture reaches the inputs for the order-two
corner: eta derivatives through order six retain exact derivative signs with
`N=10000` and only 15 Euler transforms, whose largest remainder is below
`1.15e-52`. Higher matrix order therefore does not yet create a tail-cost
barrier; generic interval series composition for `A_4,A_5` is next.

The eta jet through order six is now evaluated with directed rounding. All
seven certified boxes have width below `5e-52`, so the regular analytic input
for `A_4,A_5` is complete. The remaining order-two work is generic truncated
interval-series composition, not further transcendental estimation.

Generic interval composition now closes the order-two corner. It derives
`A_4~3.19389e-12` and `A_5~1.57589e-14`; the ordinary, lower, and upper `3x3`
determinants have certified positive lower bounds near `2.15e-22`, `3.08e-31`,
and `1.38e-20`. An initial normalization regression correctly rejected direct
composition of `Xi'/Xi`; the squared-coordinate function requires division by
`2s-1`. Two complete finite corners now pass without zero locations, while RH
still requires the unbounded hierarchy.

The order-three input crosses the first scaling threshold. Derivative order
eight cannot retain the old `log N>9` sign proof, but increasing the finite
prefix to `N=100000` restores exact positivity with eight Euler transforms;
all tails are below `4e-36`. Thus the method survives, at a measured tenfold
prefix cost rather than an uncontrolled asymptotic failure.

The enlarged eta jet is now evaluated in one pass, reusing each certified
prefix logarithm for all nine derivative orders. Every interval through
`eta^(8)(1)` is narrower than `9e-36`; the regular analytic input for
`A_6,A_7` is therefore complete without zero data.

The generic degree-seven composition closes the `4x4` corner. Certified
ordinary, lower, and upper determinant lower bounds are about `1.16e-41`,
`9.08e-54`, and `2.97e-39`. The lower determinant remains positive, although
its relative enclosure width has grown to roughly `4.1e-5`; this is the first
clear signal that subsequent corners need adaptive precision. Three complete
finite Hausdorff corners now pass, still far short of the unbounded RH gate.

The three ordinary determinants also determine the first three monic Jacobi
off-diagonal squares. Certified values are approximately `3.64e-6`, `1.32e-6`,
and `4.86e-7`, so the first three source-derived Lanczos steps do not break
down. This is a finite recurrence segment, not an infinite self-adjoint
operator or a spectral proof.

Interval Lanczos completes the first `4x4` Jacobi compression. Its certified
diagonal is approximately `(0.0016064,0.0034962,0.0017975,0.0012167)`, and its
norm ratios agree with the independently extracted off-diagonal squares. The
three localizer families provide the corresponding finite form bounds
`0<=J<=4`. This is the first concrete source-derived symmetric operator
segment, still not an infinite Hilbert--Polya construction or RH.

Blind diagonalization of the source-derived compression predicts ordinates
`14.13510,21.54984,33.63891,110.22215`. No zero locations enter construction;
only afterward does comparison reveal that the first estimate is within about
`3.7e-4` of the standard first ordinate. The later nodes are coarse tail
quadrature, not recovered consecutive zeros. Convergence of the extremal node
under increasing certified order is now a sharp falsifiable operator test.

Nested Ritz theory fixes the direction of that test. Largest compact-coordinate
nodes increase with compression size, so transformed ordinate estimates
decrease from above: `24.9452,14.6084,14.1520,14.1351`. Identifying the limit
with the first Riemann ordinate still needs the full positive-measure hierarchy.

For the next `5x5` corner, exact analysis moves the eta prefix threshold to
`N=500000`. Ten Euler transforms bound every derivative tail through order ten
below `6e-50`. The program remains finite, but prefix growth identifies
reusable certified logarithm tables as the next engineering optimization.

The one-pass order-ten eta evaluation is now complete. At 90 decimal digits,
all eleven derivative boxes have width at most `1.2e-49`; the half-million
prefix runs in about 43 seconds. Thus the regular input for `A_8,A_9` is
certified, leaving degree-nine composition and the `5x5` determinant test.

Degree-nine composition closes that test. Ordinary, lower, and upper `5x5`
determinants have positive lower bounds near `1.92e-67`, `7.68e-83`, and
`1.96e-64`. Four complete finite corners now pass without zero input, still
not the unbounded RH hierarchy.

The fifth Jacobi compression has certified `b_4~3.07e-7` and a resolved `a_4`.
Blind diagonalization predicts `gamma_1~14.1347310037`, about `5.9e-6` above
the standard first ordinate and roughly 64 times closer than size four. No
zero enters construction; limit identification remains conditional.

Interval Sturm inertia certifies the fifth finite edge itself:
`gamma_hat in [14.1347310022873,14.1347310051871]`. The box is only `2.9e-9`
wide, so the `5.9e-6` external discrepancy is overwhelmingly finite-compression
error rather than numerical uncertainty.

The fifth Gaussian weight independently estimates the top atom's multiplicity:
`w_max/u_max~1.00001069`. No zero or multiplicity data enter construction.
This is a striking blind residue-one prediction, but it is numerical and does
not by itself prove an eigenspace dimension, zero simplicity, or RH.

Christoffel interval arithmetic upgrades that residue estimate to
`[1.0000106856271,1.0000106950984]`. This certifies the finite quadrature
prediction, not an exactly unit limiting ratio or first-zero simplicity.

The Jacobi construction is equivalently the `[n-1/n]` Stieltjes--Pade
approximant to the quarter-point resolvent. Its nodes give reciprocal negative
Pade poles, explaining why a finite source jet predicts the nearest spectral
singularity. The fifth Gaussian measure reproduces `A_0,...,A_9` numerically;
the all-order Stieltjes property remains the RH-equivalent missing theorem.

The four certified corners now invoke the degree-nine truncated Hausdorff
theorem: a positive measure on `[0,4]` exists unconditionally and reproduces
`A_0,...,A_9`. The five-node quadrature is one atomic realization. This finite
measure is nonunique and is not the all-order Riemann spectral measure.

The Sommerfeld attack is now explicit. The infinite source Jacobi operator
must be positive compact, so `a_n,b_n->0`; a free constant tail is ruled out by
the desired discrete spectrum. Its WKB counting law must reproduce the
compact-coordinate Riemann--von Mangoldt asymptotic, with gamma supplying the
smooth action and the Euler prime term the phase defect. This is a falsifiable
asymptotic program, not a proof from five coefficients.

The first Sommerfeld obstruction is explicit: the raw Euler phase converges
absolutely only for `Re(s)>1`, whereas the boundary condition is needed at
`Re(s)=1/2`. The phase must cross a canonical regularized Abel boundary and
match the Jacobi Weyl function. Simply inserting `arg zeta` would restate the
spectral problem rather than explain it.

Finite Jacobi--Pade denominators bypass that obstruction canonically:
`arg det(I+hJ_n)` has one `pi` jump at each real negative Pade pole, with prime
information entering through regular completed moments. The unresolved global
gate is convergence of these finite phases to a self-adjoint Weyl function
whose resolvent is the completed Xi source.

Schur-complement order supplies the safe infinite limit: compatible positive
Jacobi extensions obey `0<R_n(h)<=R_(n+1)(h)<=A_0` for every `h>0`. Hence all-
order positivity would already give pointwise positive-axis Weyl convergence.
The remaining work is analytic identification with the completed source and
controlled continuation to the negative-axis phase.

Compact support upgrades the conditional limit: successively moment-matching
Gaussian measures have a unique weak limit by Hausdorff determinacy, and their
Weyl functions converge locally uniformly off the fixed cut. Their common jet
identifies the analytic source limit. Thus all-order positivity is the
existence bottleneck; WKB remains the explanation of spectral counting.

Hausdorff's theorem now linearizes that bottleneck. With `m_k=A_k/4^k`, the
infinite compact-measure condition is exactly
`(-1)^j Delta^j m_k>=0` for all `k,j`. All 55 available inequalities through
total degree nine are interval-positive. This does not prove RH, but replaces
the universal determinant search by a cleaner source-linear positivity target.

These inequalities assemble into one bivariate generator, explicitly a
fractional combination of two completed-source resolvent evaluations. Under a
positive squared spectrum its coefficients are mixed monomials
`x^k(1-x)^j`; source-side coefficient positivity of this single function is
now the universal Gram/factorization target.

That generator further collapses to the Loewner divided-difference kernel of
`F(t)=(4t-1)S(t)`. A nonnegative squared spectrum gives an explicit rank-one
Gram decomposition with weights `m_lambda(1+4lambda)`. Direct source proof of
this one kernel's positivity would imply the linear hierarchy, localizers,
unique Weyl limit, and reconstructed self-adjoint Jacobi operator together.

Loewner's theorem reduces this kernel target to `Im F(t)>=0` in the upper half-
plane. In completed `s` coordinates the endpoint poles cancel exactly to the
constant `4`, leaving a single coupled gamma--prime Pick inequality. Neither
gamma nor the oscillatory Euler sector is positive separately; their completed
coupling is the hard universal theorem.

A first zero-free complex eta/digamma scan finds no violation of the reduced
Pick inequality on 117 broad samples. The smallest imaginary part is about
`7.34e-4` near the positive real boundary. This is numerical reconnaissance,
not interval evidence; adaptive certified boxes are the next falsifier.

After dividing out the trivial boundary height, a 57-point scan over seven
decades finds `F'(x)>0` throughout the positive axis sample. This clears the
diagonal Loewner gate numerically but not the genuinely coupled `2x2` kernel
determinants, which are the next hostile test.

That `2x2` scan is robustly positive for widely separated points. Nearby pairs
produce tiny raw negatives at the evaluator's error floor; the positive
five-node control predicts true margins smaller than the current numerical
noise. This is a conditioning obstruction, not a credible Pick counterexample;
shared interval kernel evaluation is next.

The diagonal conditioning problem has an exact local resolution at `x=1/4`.
Taylor expansion identifies the first coupled curvature as
`16(A_0 A_2-A_1^2)`, so the previously certified first Hankel determinant gives
a strict interval-positive Loewner contact coefficient without using any zero.
This is a structural identification, not merely another successful scan: the
first local coupled kernel obstruction and first moment-covariance obstruction
are identical. Positivity at general pairs and RH remain unproved.

A direct attempt to scan the analogous curvature over four decades is
numerically unresolved. Its baseline is positive, but a step/depth control
changes sign and misses the independently certified quarter-point coefficient
by roughly 86 percent. This falsifies the current finite-difference evaluator,
not the Pick conjecture. Further progress requires directed interval automatic
differentiation, ball arithmetic, or a source-side covariance identity.

The curvature now has a simpler exact interpretation. If `g=F'>0`, then
`C>=0` is equivalent to concavity of `g^(-1/2)`. In the proposed spectral
model, `C=M_2M_4-M_3^2` and symmetrizes to a positive pairwise square. This is
the sought covariance identity, conditional on the representation. It also
shows why scalar complete monotonicity cannot finish the proof: the completely
monotone test function `exp(-x)` has negative curvature. The next source-side
goal is therefore reciprocal-square-root concavity, not merely more derivative
signs.

Using this geometry avoids the failed third-derivative method. A zero-free
eta/digamma scan tested 36 arithmetic-midpoint chords of `1/sqrt(F')` between
`0.01` and `100`. Every chord is concave in independent height/depth runs; the
smallest gap remains about `1.71e-9` after subtracting the largest discrepancy
between runs. This is the first numerically stable coupled source test beyond
the quarter point. It remains finite and non-interval, so it is evidence and a
better falsifier—not RH.

The chord attack now spans fourteen decades, from `10^-6` to `10^8`. Its
archimedean tail is robustly concave: for left endpoints at least one, the
smallest gap is about `3.41e-4` and the two controls agree to about `8e-15`.
Small raw negatives occur only near `x=0` and are dominated by the evaluator's
`7.71e-8` control discrepancy, so none is a credible counterexample. This
localizes the next rigorous attack to a central-coordinate interval expansion
at the zero boundary.

That central-boundary attack now succeeds numerically at high precision. A
coupled Decimal evaluator tests 21 chords from `10^-8` through `10^-2`; the
corrected smallest exploratory gap is about `3.65e-20`, while simultaneous changes in
precision, Euler depth, and differentiation step alter results by at most
`1.84e-26`. The earlier binary64 negatives were cancellation artifacts.
Reciprocal-slope concavity has therefore survived controlled scans across
sixteen decades, but explicit outward-rounded remainder bounds are still
required before this becomes a certificate.

The central certification deficit is now decomposed. The eta-value Euler tail
is rigorously at most `2^-120`; even pessimistically amplified at `t=10^-8`,
its budget is about `1.13e-21`, below the revised smallest observed chord gap. Only two
correlated analytic bounds remain for this finite certificate: the
differentiated Euler tail for `eta'`, and derivative-aware propagation of the
digamma remainder.

The eta-prime item is now closed analytically. Differentiating the positive
Laplace representation of the Euler differences and splitting at unit time
gives `|d_k'|<=3/k+1/k^2` uniformly for `1/2<=s<=3/5`. Consequently the
depth-120 differentiated tail is below `1.90e-38`; even an inflated propagated
budget is about `2.83e-22`, safely beneath the chord margin. Only correlated
digamma remainder propagation remains in this finite certification budget.

That last correlation proof can be bypassed by better conditioning. Recurring
digamma to argument 100 rather than 20 suppresses the first omitted `z^-18`
term by `5^18`, making even independent stencil propagation smaller than the
observed margin. The analytic eta, eta-prime, and digamma tails are now all
budgeted. Directed rounding of the nonlinear computation and a rigorous
finite-difference truncation bound remain.

Finite differences are no longer necessary. Analytic differentiation of the
coupled source carries `eta,eta',eta''` together with `digamma,trigamma` and
reproduces the corrected positive margins. The new depth-120 eta-double-prime
tail is rigorously below `1.63e-37`, or about `2.45e-21` after an inflated
boundary budget. Outward-rounded nonlinear propagation is now the only
remaining implementation step for the 21 finite central chords.

That finite step is now complete. Directed 90-digit intervals, including eta
tails through second derivative and digamma/trigamma asymptotic remainders,
certify all 21 central chord gaps. The weakest is
`[3.6492372625e-20,3.6501288511e-20]`. The work also repaired consequential
default-Decimal-context defects in Bernoulli construction and unary negation.
This is unconditional finite source evidence without zero locations; global
concavity, Loewner positivity, and RH remain open.

The directed mesh has now been densified by inserting `3*10^k` between powers
of ten. All 78 resulting central chords are strictly interval-positive. The
new weakest enclosure is `[1.7964066809e-21,1.8106786499e-21]` on
`[10^-8,3*10^-8]`. This substantially tightens the hostile finite test while
leaving continuum concavity and RH open.

The continuum gate has now been reduced without central cancellation. Put
`ell(t)=log Xi(1/2+sqrt(t))`; reflection symmetry makes this analytic in `t`
and gives the exact identities `S=ell'` and `F=(4t-1)ell'`. The desired local
concavity is therefore the fourth-order polynomial inequality
`2F'F'''-3(F'')^2>=0`, expressed through `ell',...,ell''''`. This turns the next
step into interval Taylor models on `t`-boxes rather than ever-denser chord
sampling.

Quadratic normalization shows the dense certificate has a substantial
continuum margin. The weakest `~1.8e-21` chord gap corresponds to a directed
triangular average of `H''` in approximately
`[-3.621e-5,-3.593e-5]`. A continuum Taylor box on that cell therefore needs
only bound curvature oscillation below `3.59e-5`, together with boxwise
positivity of `F'`; it does not need to resolve curvature at the raw chord-gap
scale.

The continuum oscillation gate is also exact. Writing `g=F'`, the third
derivative of `H=g^(-1/2)` is
`(18gg'g''-4g^2g'''-15(g')^3)/(8g^(7/2))`. In the reduced Xi-log coordinate
this uses derivatives only through `ell'''''`. A box bound for this expression
times cell width, compared with the certified `3.59e-5` average-curvature
margin, is sufficient for pointwise concavity on that cell.

The fifth-derivative reconnaissance says the existing mesh should suffice. On
the hardest cell `[10^-8,3*10^-8]`, `H'''` is numerically about `3.82`, giving
a full-width oscillation budget `7.64e-8`; the certified average-curvature
margin is `3.59e-5`. This factor-of-470 separation means a moderately coarse
interval fifth-jet enclosure can close the continuum cell without additional
subdivision. The estimate itself remains non-interval.

An analytic fourth-order source jet now replaces that finite-difference
estimate. It gives `H''~-3.60653e-5`, `H'''~3.76186`, and width-times-derivative
`7.524e-8` on the hardest cell. A failed first draft exposed a necessary type
distinction: `zeta'/zeta` consumes the partial derivative `eta_s`, not the
composed `t` derivative. With separate eta and eta-s jets, the nonlinear
architecture needed for an interval fifth-jet model is now operational.

All eta tails needed by that interval jet are now controlled uniformly. A
Cauchy circle of radius `0.1`, a crude Weierstrass bound `|1/Gamma|<4`, and the
positive Euler integral yield
`|R_(N,j)|<=4 j! 10^j 2^-N/(N+0.4)`. At depth 300 every derivative tail through
order six is below `5e-83`. This replaces separate low-order tail arguments and
clears the eta sector for directed fifth-jet propagation.

The gamma sector is now cleared as well. Differentiating the positive-real
Stieltjes remainder gives
`|R^(j)(z)|<=|B_18|(18)_j/(18 z^(18+j))`; recurring digamma to argument 1000
puts all required remainders through order six below `3.06e-54`, including the
`s/2` chain factors. The interval jet no longer needs correlated cancellation
between eta and gamma truncation errors.

The centered coefficient parity audit falsified that first differentiated
gamma bound as too optimistic. A safe replacement uses a complex Cauchy disk:
the remainder derivative costs `j! 2^(18+j)/z^j`, with `2^-j` cancelled by the
`s/2` chain. At recurrence 1000 the corrected errors remain below `8.01e-49`
and can honestly enclose the reflection-forced even coefficients.

The centered directed jet now closes its full parity audit through even order
12. Repairing a rounded Decimal accumulator for the exact Euler denominators
was the final arithmetic gate. The resulting intervals certify
`H''(0)~-3.6043843454e-5<0` and `H'''(0)~4.4659254461e-7>0`. This is a rigorous
source-curvature result at the central boundary, not yet on a positive-width
cell; interval series remainders are next.

A high-order real remainder can be replaced by one coarse complex estimate.
If `|F'|>=1/16` on the disk `|t|<=1/4`, then `H=(F')^-1/2` is analytic with
`|H|<=4`, and Cauchy bounds `|H'''|<1536.001`. The first-cell chord margin only
requires `<1796.4`, so this disk gate would certify pointwise concavity with
about `5.21e-6` remaining margin. The disk modulus inequality is now the next
falsifiable target.

The natural interval-jet implementation is now falsified as a viable route.
On the first cell it expands `F'~0.09246` to an enclosure near
`[-1.84e10,1.90e10]`, before analytic tails are even added. This is dependency
blow-up from multiplying the singular central prefactor by a vanishing coupled
source. Precision and tail improvements cannot fix it; the interval model must
construct the reflection-even `ell(t)` series first and only then form
`F=(4t-1)ell'`.

The cancellation-free centered Xi series has now resolved the derivative
discrepancy. Oddness of `Xi'/Xi` produces `ell'(t)` directly and gives
`H''(0)~-3.60438e-5`, `H'''(0)~4.47e-7`. Series values at `10^-8`, `2e-8`, and
`3e-8` lie inside the independent directed slope intervals. Consequently the
earlier finite-difference and unreduced point-jet claims `H'''~3.8` are
retracted as cancellation artifacts. The true boundary oscillation appears
about seven orders smaller, pending interval series remainders.

The centered coefficient intervals also show that the quarter-disk target has
ample room. The degree-four `F'` polynomial has radial modulus lower bound
`0.0923826193` on `|t|<=1/4`, versus the target `0.0625`. An omitted-tail
supremum below `0.0298826193` therefore suffices. The next obligation is a
coarse Cauchy bound for the remaining centered Xi-log series.

That tail bound reduces further to a loose unit-disk source estimate. If `F'`
is analytic with `sup<=20` on `|t|<=1`, Cauchy bounds the degree-five-and-up
tail on the quarter disk by `20/768~0.0260417`, below the `0.0298826` allowance
with margin `0.00384095`. The next target is therefore a compact enclosure of
the completed source on `|s-1/2|<=1`.

A 96-point unit-circle source scan finds maximum `|F'|~0.09275656`, at `t=-1`,
with control discrepancy `4.45e-10`. The proposed rigorous bound 20 therefore
has numerical safety factor above 215; even a bound of one appears generous.
The unresolved work is rigorous complex analyticity and enclosure between
samples, preferably in the reflection-even Xi coordinate.

Analyticity on that disk has a source-only Rouché reduction. Theta-kernel
positivity implies
`|Xi(1/2+q)-Xi(1/2)|<=Xi(3/2)-Xi(1/2)` for `|q|<=1`; thus the single real
inequality `Xi(3/2)<2Xi(1/2)` proves no zeros occur in the disk. Its numerical
margin is near `0.4855`, so a directed evaluation at two real arguments should
close analyticity without importing any zero locations.

The real Rouché inequality is now certified. Directed Euler-transform terms
and elementary gamma bounds yield `Xi(1/2)>0.434455` and `Xi(3/2)<0.75`, so the
comparison margin exceeds `0.1189`. Theta positivity therefore proves that
`Xi` is zero-free on `|s-1/2|<=1` with no zero-location input. Analyticity of
the unit `t`-disk source is closed; the remaining outer-disk obligation is the
coarse modulus bound `|F'|<=20`.

That final complex bound has now become a real moment inequality. Positivity
of the theta coefficients makes `sup|Y'|=Y'(1)` and `sup|Y''|=Y''(1)` for
`Y(t)=Xi(1/2+sqrt(t))`. Together with the Rouché lower bound this yields the
explicit unit-disk estimate
`|F'|<=4A/m+5(B/m+(A/m)^2)`, where `m`, `A`, and `B` use only Xi and its first
two derivatives at the real endpoints. Reconnaissance gives `0.102201`, versus
the sufficient target 20. The next and apparently final gate in this chain is
a directed real certificate for those endpoint derivatives.

The endpoint-derivative gate admits a simpler elementary closure. Coefficient
positivity bounds the first two moments at `t=1` by `Y(9)/9` and `2Y(9)/81`.
The identity `Y(9)=Xi(7/2)`, Gamma log-convexity, a zeta integral estimate,
and `pi>3.1` give `Y(9)<3/4`. Directed propagation with the existing Rouché
margin proves `sup_|t|<=1 |F'(t)|<6.038308`, closing the requested bound 20.
The resulting quarter-disk Taylor tail is below `0.007863`; combined with the
certified degree-four modulus, it proves `|F'|>1/16` there. The one-circle
Cauchy argument therefore upgrades the first central chord certificate to
pointwise reciprocal-slope concavity throughout `[10^-8,3*10^-8]`. This is
the first positive-width continuum cell, not a proof of RH.

The local result now extends across the entire tested central domain. A
directed centered Xi-log jet through order 61 produces the degree-11 Taylor
polynomial of `H=(F')^(-1/2)`. The certified quarter-disk bound gives
`|H|<3.5`, so on `t<=0.01` the omitted Cauchy tail has geometric ratio at most
`0.04`. Directed evaluation upgrades every one of the 78 chord averages to
pointwise `H''<0`; the separately certified boundary jet closes the sliver at
zero. Thus `H''(t)<0` for all `0<=t<=0.01`. The weakest residual margin remains
above `3.5928e-5`. This is a continuum coupled-positivity theorem, not RH.

The Deutsch--Popper target is now arithmetic Loewner kernel completion: a
zero-free source factorization `K_F(x,y)=R(x)^*R(y)` must generate one
compatible Hilbert completion, its canonical self-adjoint resolvent, the
completed-Xi determinant, and the prime-power trace formula. The first
separated rank-three central falsifier survives: at `(0,0.005,0.01)` the
directed Loewner determinant lies in `[8.0788e-34,9.3302e-34]`. Achieving this
resolution exposed and repaired an omitted highest `F'` coefficient in the
earlier degree-11 implementation; the continuum theorem was rerun and remains
certified. Arbitrary separated positivity and the source Gram factorization
remain open, so RH is not proved.

The separated rank-three test now covers all 165 triples on the central
`0.001` grid. Every directed determinant is strictly positive. The weakest is
at `(0.008,0.009,0.01)`, in
`[5.5699262074e-38,5.5699262200e-38]`. Degree-23 source coefficients reduce the
common divided-difference tail below `6.10e-46`. This is finite compression
evidence; positivity between grid points and higher-rank completion remain
open.

The grid has now been upgraded to a continuum rank-three theorem. Newton
divided-difference elimination identifies the determinant divided by the
squared Vandermonde with a regular `3x3` mixed-divided-difference determinant.
A single directed derivative box over `[0,0.01]^2`, including all degree-23
tails, gives normalized determinant interval
`[1.3413135748e-20,1.4441125285e-20]`. Hence every distinct central triple has
strictly positive Loewner determinant, with nonnegative collision limits.
The next finite obstruction is rank four; RH remains open.

The first rank-four whole-box attempt is unresolved rather than negative. Its
normalized determinant enclosure is approximately
`[-1.118e-36,1.124e-36]`, while midpoint evaluation is positive near
`3.020e-39`. The degree-23 analytic tail is negligible; independent entry
boxes lose the mixed-divided-difference correlations. The next implementation
must use correlated `LDL*` pivots or subdivide the ordered simplex.

Exact Newton divided differences repair the rank-four correlation loss on the
hostile grid. Monomial divided differences are evaluated as complete
homogeneous symmetric polynomials, avoiding near-node subtraction. All 330
quadruples on `{0,0.001,...,0.01}` have directed-positive normalized
determinants. The weakest is `(0.007,0.008,0.009,0.01)`, in
`[3.0190646591e-39,3.0190702736e-39]`. Continuum rank four remains open.

Continuum rank four is now closed. The anchor family was enlarged to all 1001
nondecreasing grid quadruples, including repeated nodes; the weakest is the
fully confluent upper endpoint, above `3.0187703238e-39`. Global directed
coordinate derivatives bound monotone nearest-grid transport by
`3.66295e-41`, leaving `Q_4>2.9821408391e-39` on the full ordered simplex.
Every distinct central rank-four minor is therefore strictly positive, with
nonnegative collision limits. Rank five is next; RH remains open.

Rank five required a deeper source jet rather than finer interval algebra.
The degree-23 tail in the eighth mixed derivative was `2.10e-22`, larger than
the true fifth `LDL*` pivot near `6.67e-26`. Extending `F` through degree 29
reduces the tail to `1.84e-33`. All 462 distinct central grid quintuples then
have directed-positive Newton--`LDL*` pivots; the weakest final pivot exceeds
`6.6652565650e-26`. Confluent anchors and continuum rank five remain open.

The complete rank-five anchor audit now passes: all 3003 nondecreasing
quintuples, including collisions, have positive directed Newton--`LDL*`
pivots. The weakest final pivot exceeds `6.6651134944e-26`; the corresponding
normalized determinant exceeds `2.0120465530e-64`. A global adjugate derivative
bound costs `3.28366e-60` over half a grid step, four orders too large. This
falsifies determinant transport as the continuum mechanism; differentiated
`LDL*` pivot transport is next.

Differentiating the Newton--`LDL*` recursion at the weakest confluent anchor
validates that replacement. The fifth-pivot half-grid linearized cost is below
`9.185e-31`, versus margin `6.665e-26`, giving safety factor above 72,000.
The remaining proof obligation is a derivative enclosure over each cell, not
just at its anchor. The helper import was also repaired so derivative probes
no longer rerun the entire 462-case grid implicitly.

The first full-cell pivot enclosure rejects natural interval arithmetic as the
continuum carrier. On `[0.0095,0.01]^5` the fifth pivot expands to about
`[-2.91e-21,1.97e-23]`, five orders beyond its true positive scale. Uniform
subdivision would require widths near `1e-8`. The next implementation must be
a centered affine/Taylor `LDL*` model retaining the shared node variables.

The centered five-variable `LDL*` Taylor model is now implemented through
degree five. Half-grid budgets are `8.99e-31`, `6.76e-36`, `3.75e-41`,
`1.71e-46`, and `6.86e-52`, leaving margin `6.66502e-26`. The near-geometric
`5e-6` decay makes the continuum gate plausible. This remains midpoint
reconnaissance; directed coefficient boxes and a rigorous rational tail
majorant are next.

Directed sparse-jet arithmetic now certifies every centered pivot coefficient
through degree five for the degree-29 source polynomial. The rigorous finite-
polynomial margin is `6.6650237584e-26`, with the same geometric budget decay
seen in reconnaissance. This does not yet include the omitted analytic source
tail or the infinite rational tail from `LDL*` inversions; those are the two
remaining rank-five continuum obligations.

The omitted analytic source tail is now injected into every Taylor
coefficient through degree five using directed Cauchy/falling-factorial
bounds. Coarse allowances raise the higher-degree budgets only to
`2.4e-32`--`4.3e-32`, leaving rigorous margin `6.6650083764e-26`. The sole
remaining rank-five continuum gate is an all-orders majorant from degree six.

The all-orders endpoint-cell majorant is now certified. Directed positive-
coefficient sums give omitted-source remainder `4.6293e-32` and known-
polynomial remainder `3.4635e-35`; a common `1e-30` matrix-entry allowance
propagates through residual-certified reciprocals to final rational remainder
`1.0167e-30`. Hence `d_5>6.6649067122e-26` throughout
`[0.0095,0.01]^5`. Uniformizing this Taylor model over the remaining ordered
cells is the sole central rank-five obligation.

The preferred uniformization route is now coordinatewise pivot monotonicity.
A hostile binary finite-difference sweep gives negative signs at all 15,015
anchor-coordinate pairs, but its former extremal range is withdrawn because
subtraction of pivots near `10^-26` loses accuracy at derivative scale.
Differentiating the directed Newton--`LDL*` recursion analytically at the
cancellation-sensitive anchor `(0.003,0.003,0.003,0.01,0.01)` proves all five
derivatives strictly negative, including analytic source tails; their upper
endpoints lie between `-1.35e-28` and `-1.22e-27`. An all-anchor directed audit
followed by derivative Taylor transport would reduce the whole simplex to the
already certified upper endpoint cell.

The all-anchor analytic derivative audit is complete. Directed Newton--`LDL*`
differentiation with Cauchy source tails proves all 15,015 derivatives at all
3003 nondecreasing anchors strictly negative. The closest interval upper
endpoint is `-1.3533618854e-28`, attained at the fully confluent upper endpoint
in coordinate 3; the most negative lower endpoint is `-1.2342190e-27` at the
fully confluent zero endpoint in coordinate 5. The remaining rank-five gate is
therefore sharply quantitative: certify that derivative variation inside each
ordered half-grid cell is below `1.35336e-28`. This is still not continuum
rank five, and RH is not proved.

The first transport norm is deliberately rejected. Absolute differentiation
of the existing endpoint Taylor box costs `2.08e-28`, exceeding the derivative
sign margin. Yet direct directed evaluations at every ordered endpoint-cell
vertex stay negative, with closest upper endpoints varying only about
`2.5e-33`. The discrepancy identifies repeated tail allowances and discarded
ordered-simplex correlation as the loss. The next certificate will propagate
the fifth-pivot Hessian directly and use its row sums for cellwise mean-value
transport.

Direct Hessian propagation exposed and repaired a source-depth bottleneck.
The degree-29 Cauchy tail produced a useless `2.94e-22` Hessian row-sum bound.
Extending the directed centered Xi-log jet from order 61 to 81 supplies `F`
through degree 39. At the fully confluent upper anchor, the resulting Hessian
row sums are only `4.32e-30`--`4.56e-29`, so their half-grid products are at
most `2.28e-32`, thousands of times below the derivative sign margin. This
does not yet bound the Hessian throughout the cell; that supremum enclosure is
the next rank-five obligation. RH is not proved.

The deeper Hessian audit also passes all six ordered endpoint-cell vertices.
Their largest row sum changes only from `4.556095e-29` to `4.556191e-29`, and
every half-grid mean-value cost is below `2.278096e-32`. This strongly
localizes the remaining proof obligation to a third-derivative interior
remainder; it is not evidence of a hidden vertex sign failure.

The degree-39 correlated Taylor jet now bounds the finite interior Hessian
variation. Degrees 3--5 contribute at most `6.4271477454e-34` to any Hessian
row sum, with degreewise maxima `6.43e-34`, `6.02e-39`, and `7.42e-43`.
Consequently the finite jet perturbs the anchor Hessian by only about one part
in 70,000. The unique endpoint-cell gate is the degree-six-and-higher Hessian
remainder; continuum rank five and RH remain open.

The correlated jet has been extended through degree seven. The two new
Hessian-row budgets are `1.1395e-42` and `1.4252e-42`, leaving total finite-jet
variation `6.4271477711e-34`. Their small rebound is the independently injected
analytic-tail floor. The remaining degree-eight-and-higher bound must aggregate
that source tail once through the rational `LDL*` recurrence; it cannot infer
convergence by summing those repeated interval boxes.

The aggregated all-orders `C^2` Taylor model succeeds. Maximum matrix-entry
remainders are `2.78e-46` in value, `4.45e-42` in total gradient, and
`6.23e-38` in total Hessian. After rational Newton--`LDL*` propagation, the
fifth-pivot Hessian remainder is only `1.6707041856e-41`. Together with the
anchor Hessian and degree-3--7 variation, this bounds half-cell derivative
transport below `2.279e-32`, versus sign margin `1.35336e-28`. All fifth-pivot
coordinate derivatives are therefore strictly negative throughout the full
endpoint cell. Uniformization over the remaining ordered cells is open;
continuum rank five and RH are not proved.

All eleven fully confluent grid anchors have also passed a directed Hessian
scan. Their maximum row sum decreases monotonically from `4.5580195e-29` at
zero to `4.5560947e-29` at `0.01`, with relative variation only `4.2e-4`.
This rules out boundary curvature inflation but does not cover mixed anchors;
the latter are now the precise uniformization target.

All 462 distinct-node grid anchors now pass the directed Hessian audit. The
hostile distinct anchor is `(0,0.001,0.002,0.003,0.004)`, with maximum row sum
`4.5573544585e-29`, below the fully confluent zero value. Mixed collision
patterns are the remaining discrete Hessian family.

The collision audit now covers all 231 anchors with at most two distinct grid
values and every multiplicity split. The hostile case is the fully confluent
zero anchor with row sum `4.5580195455e-29`. Combining these with the 462
distinct anchors closes 693 Hessian anchors; only three- and four-value
collision patterns remain in the discrete audit.

The exactly-three-value collision stratum is complete: all 990 anchors pass,
with hostile anchor `(0,0,0,0.001,0.002)` and row sum
`4.5577067841e-29`. Only the 1,320 exactly-four-value anchors remain before the
complete 3003-anchor Hessian ceiling is known.

The exactly-four-value audit closes the final discrete stratum: all 1,320
anchors pass, with hostile case `(0,0,0.001,0.002,0.003)` at
`4.5575360646e-29`. Across all `231 + 990 + 1320 + 462 = 3003` anchors, the
global directed Hessian ceiling is `4.5580195455e-29`, attained at the fully
confluent zero anchor. Only a uniform between-anchor Hessian enclosure remains
before coordinatewise monotonicity can close continuum rank five.

The remaining bound is quantitatively loose. Cell `l1` radius is at most
`0.0025`, so the derivative margin permits Hessian row sums up to
`5.4134e-26`, about 1,188 times the audited anchor maximum. A uniform
third-derivative row bound below `2.16e-23` suffices to carry the anchor
Hessian ceiling through every cell. This coarse global third-derivative
majorant is the next and final monotonicity falsifier.

Post-restart, natural interval propagation over the full endpoint cell was
tested and rejected: its Hessian row bound is `4.9184e-21`, five orders above
the permitted ceiling. A refreshed all-anchor pivot audit now records that all
five coordinatewise pivot minima occur at the fully confluent upper endpoint;
the first four denominator lower bounds are `9.2454e-2`, `3.3771e-7`,
`4.4596e-13`, and `2.1680e-19`. Therefore the endpoint rational Taylor model
already has the worst discrete conditioning. The remaining continuum task is
to certify safe within-cell allowances for these four denominators and then
propagate one uniform third-derivative majorant.

The first-four denominators are now globally certified without cellwise pivot
transport. The whole-domain rank-two determinant is
`[3.1217673843e-8,3.1234369675e-8]`; determinant quotients and Hadamard bounds
give floors `9.2454e-2`, `3.3764e-7`, `2.5127e-13`, and `4.3406e-21` for the
first four pivots. A hostile cancellation-free `C^3` propagation nevertheless
returns `3.53e112` against target `2.16e-23`. This falsifies global absolute
Schur norms and leaves correlated cell-centered Taylor algebra as the only
surviving continuum carrier.

The first correlated `C^3` implementation succeeds at the zero/upper
confluent anchors and the hostile mixed Hessian anchors. Directed third-tensor
`l1` bounds are `1.80024e-30`--`1.80091e-30`, versus sufficient ceiling
`2.16e-23`. Degree-four extreme-cell jets contribute variation only
`3.29394e-35`. These are anchor/finite-jet theorems, not yet the all-orders
uniform cell bound; degree-five-and-higher remainder control and efficient
center uniformization remain.

## Rank-five continuum closure (2026-08-22)

The correlated carrier has passed its first global continuum test. Six binary
macro-charts, rather than 3,003 point charts, cover the ordered rank-five
simplex. The maximum certified degree-five-and-higher third-tensor remainder
is `1.312984329805715e-29`, and the maximum full tensor `l1` norm is
`1.493074357349845e-29`. The induced derivative transport
`1.140438057835099e-31` is strictly below the weakest directed anchor margin
`1.353361885365659e-28`. Hence every coordinate derivative of the fifth
central pivot is negative throughout the ordered simplex for this source.

The explanatory gain is structural: order turns a nominal `2^5` box cover
into six patterns, while correlated Taylor algebra preserves cancellations
destroyed by natural intervals. A single global chart was falsified at
`1.17397e-17`, so the six-chart subdivision does essential work.

RH is not proved.
