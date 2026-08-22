# Arithmetic locality and spectral unitarity: an explanation charter

## Explanandum

The program is not merely to prove that the nontrivial zeros of zeta lie on
the critical line. It is to explain why arithmetic locality at the prime
places should admit a dual description as unitary spectral evolution.

> The theta endpoint and prime-power source distributions determine a single
> reflection-positive boundary correspondence. Its positive completion
> carries the Mellin coordinate as a self-adjoint generator. Primitive
> arithmetic loci are the indivisible source transitions, while zero
> ordinates are the collective frequencies of the same system.

The proposed forced chain is

`source correspondence -> prime--gamma Weil form -> positive factorization`

`-> Hilbert completion -> self-adjoint Mellin boundary -> Xi determinant`.

The completed Xi determinant and its normal jet operator are already
unconditional. The first unknown arrow is the source-side positive
factorization of the Weil form. It is equivalent in strength to RH and may
not be inferred from the already known zero divisor.

## Hard-to-vary contract

An acceptable explanation must satisfy all of the following.

1. The source transform is defined without a zero list, RH, or a fitted
   spectral measure.
2. The archimedean endpoint and prime-power terms occur with coefficients
   forced by theta completion and the explicit formula.
3. The positive form, its radical, and the operator domain descend from the
   same correspondence; they are not independently chosen to repair signs.
4. The Mellin coordinate is essentially self-adjoint or has a unique
   source-canonical self-adjoint realization with compact resolvent.
5. The regularized determinant and trace formula recover completed Xi and its
   prime terms with no extra spectrum.
6. The mechanism extends functorially to at least one nontrivial family of
   completed L-functions.

Changing a structural ingredient must have a predicted cost. Removing the
gamma term should destroy global positivity; changing prime-power weights
should break the explicit formula; shifting the reflection center should
break the involution; choosing the opposite quadratic branch should reverse
an oriented finite-rank inequality. If arbitrary changes can be absorbed by
new metrics or counterterms, the proposal is not yet an explanation.

## Present evidence and no-go results

- The source-saturated Mellin quotient canonically produces the Xi divisor,
  multiplicity jets, a closed normal compact-resolvent operator, and the exact
  modified determinant.
- Ordinary Hilbert quotient descent from the native dilation representation
  is zero; a new positive boundary form is necessary.
- The centered Weil explicit formula is the canonical global prime--gamma
  boundary morphism. Its positivity is precisely the unresolved gate.
- Rank-two Xi Pick positivity and universal confluent rank-three positivity
  are proved.
- Separated rank-three positivity remains open. Its limiting hyperbolic
  family has exact endpoint, geometry, and substantial compact/tail
  certificates, but the final graph-correlated sign and finite-epsilon
  transfer are incomplete.

These facts motivate the explanation but do not establish it.

## Theorem ladder

### Gate A: separated rank-three positivity

Close or falsify the first genuinely separated Pick determinant. The current
tail target requires the oriented signs

`a>0`, `q2<0`, `C=2 q2 b-a q1>0`,

`H=C^2-a^2 Delta>0`

on the selected critical branch. The squared inequality alone is
insufficient. Endpoint degeneracy, compact/tail overlap, and finite-epsilon
inward transfer are mandatory parts of the theorem.

### Gate B: finite source Gram system

For a growing family of source-derived Mellin tests, identify their Weil Gram
matrices with the Pick matrices. Every finite matrix must use the same
prime--gamma transform. One negative minor falsifies that transform.

### Gate C: Li norms

Derive vectors or trace classes `v_n` from the source side satisfying a
uniform identity such as `lambda_n=<v_n,v_n>`. Separate identities fitted for
finitely many `n` do not count.

### Gate D: heat-flow compatibility

Construct the de Bruijn--Newman deformation of the same boundary form and
test whether it is intertwined by a positivity-preserving semigroup. The
deformation may not introduce a new metric at each time.

### Gate E: positive completion and operator

Only after the finite gates share one mechanism, construct the radical
quotient, prove closability and domain invariance, classify self-adjoint
realizations, and identify the determinant and prime trace terms.

## Falsifiers and stop conditions

Revise or abandon the proposed mechanism if an exact separated Pick minor is
negative; positivity presupposes RH; the metric or boundary condition contains
the zero divisor; null invariance or closability fails; self-adjointness loses
the arithmetic determinant or adds spectrum; the prime term has the wrong
weight or sign; Li and heat-flow tests require unrelated constructions; or a
controlled variation survives where the explanation predicts failure.

## Evidence discipline

Exact symbolic identities, directed interval enclosures, and deliberate
failure tests are theorem evidence. Floating profiles are discovery only.
Every result must state whether it is finite-cutoff, limiting, source-typed,
or unbounded. The algebraic Xi boundary remains separate from the unavailable
physical coefficient--Betti relative-chain pushforward.

No success at finite rank proves RH. The explanation earns reach only when
one independently derived source mechanism forces several consequences not
inserted into its definition.

## First variation result

The opposite-quadratic-branch variation is now an exact hostile control. On
`1/3<t<1`,

`q2=t(t-1)(t+1)(3t-1)(3t+1)/4<0`.

The selected root has `Q_L=-sqrt(Delta)` and is the required maximum; the
opposite root has `Q_L=+sqrt(Delta)` and is not a maximum. Thus branch choice
cannot be varied while preserving the local critical geometry. The exact
checker and residual record are
`checkers/hyperbolic_opposite_branch_falsifier.py` and
`results/hyperbolic-opposite-branch-falsifier.json`.

The reflection-center variation is also exact. For the vertical spectral line
`s=c+i z`, the completed functional-equation involution gives

`1-s=(1-c)-i z`.

This equals the centered reversal `c-i z` only when `1-2c=0`, hence uniquely
at `c=1/2`. Shifting to `c=1/2+delta` leaves the nonzero residual `-2delta`.
Thus the critical center is forced by the involution before any claim about
zero reality. The checker and result are
`checkers/xi_reflection_center_falsifier.py` and
`results/xi-reflection-center-falsifier.json`.

The local prime-power weights are likewise forced. With `x=p^-s`, the local
Euler logarithmic derivative is

`log(p) x/(1-x)=sum_(m>=1) log(p) x^m`.

Coefficient comparison through order eight uniquely returns `log(p)` in
every prime-power degree. Perturbing the fifth weight by `delta` leaves the
exact residual `delta x^5`. The identity itself supplies the all-order
statement; the finite checker is its hostile regression test. Artifacts:
`checkers/euler_prime_weight_variation_falsifier.py` and
`results/euler-prime-weight-variation-falsifier.json`.

Finally, the arithmetic term cannot be factorized positively prime by prime.
For two disjoint test translates separated by `log(p)`, the isolated local
prime contribution has the exact block

`[[0,-w_p],[-w_p,0]]`, `w_p=log(p)/sqrt(p)>0`.

Its determinant is `-w_p^2` and its eigenvalues are `+/-w_p`. The symmetric
direction is strictly negative. Thus an isolated prime mode is not a Hilbert
Gram block: positivity, if true, must arise only after global combination
with the archimedean and endpoint completion. This does not yet prove that
deleting the gamma term alone while retaining every endpoint term is
indefinite. Artifacts:
`checkers/weil_prime_block_indefiniteness_falsifier.py` and
`results/weil-prime-block-indefiniteness-falsifier.json`.

## Li gate normalization

The conditional spectral norm has now been isolated without promoting it to a
source proof. For `u(rho)=1-1/rho` and `rho=sigma+i gamma`,

`|u|^2-1=(1-2 sigma)/(sigma^2+gamma^2)`.

Hence `u` is unitary exactly on the critical line. Only there does a
functional-equation pair contribute

`2-u^n-u^(-n)=|1-u^n|^2`.

This identifies both the desired Li feature and the circularity trap: using
the spectral squared norm before constructing source-side unitarity assumes
the conclusion. Gate C must produce the vectors before zero fibres are known.
See `li-spectral-norm-target.md`, its checker, and its results JSON.

The source-linear part of Gate C is now uniform. Put

`V_n(s)=1-(1-1/s)^n` and `C_w(s)=1/(s-w)`. Then

`V_n(s)=sum_(j=1)^n (-1)^(j+1) binom(n,j)/(j-1)! * partial_w^(j-1) C_w(s)|_(w=0)`.

Thus every Li feature is a finite jet of one fixed Cauchy kernel, with
coefficients determined by `n`, not fitted to the zero divisor. The family
also obeys the cocycle law `V_(m+n)=V_m+u^m V_n`, where `u=1-1/s`.
This clears the uniform linear-realization subgate. It does not clear the
quadratic subgate: no source-side positive pairing has yet been constructed
whose norm square is the Li coefficient. See `li-cauchy-jet-feature.md`, its
checker, and its exact regression result.

A scale obstruction now narrows the quadratic subgate. If a unitary `U` and
a finite-norm vector `e` gave `v_n=(I-U^n)e`, then
`||v_n||^2 <= 4||e||^2` for every `n`. The same bound holds for a finite
positive unit-circle measure. Hence this elementary unitary-coboundary model
cannot represent an unbounded Li-scale target. Any viable source norm must
make its noncompactness explicit through infinite-mass renormalization, an
unbounded/distributional source object, or a genuinely different positive
form. See `li-finite-unitary-orbit-no-go.md` and its exact checker result.

The surviving architecture is consequently homogeneous rather than an
ordinary finite-vector orbit. Constants may have infinite norm while the
coboundaries `1-u^n` have finite energy and obey the same cocycle law as the
Cauchy jets. Gate C is now sharpened to constructing a source-defined
arithmetic Dirichlet form on Cauchy jets modulo constants, proving
closability and `u`-isometry, and identifying its coboundary energies with
the Li coefficients. The zero-indexed counting-measure realization is only
the conditional target and is disallowed as source data. See
`li-homogeneous-cocycle-target.md`.

The compatibility condition has now been made exact. Extending
`lambda_(-n)=lambda_n` and `lambda_0=0`, RH is equivalent (via the standard
Li criterion and paired-zero formula) to conditional negative definiteness
of `n -> lambda_n` on `Z`, hence to positive semidefiniteness of every
anchored kernel

`K(m,n)=(lambda_m+lambda_n-lambda_(|m-n|))/2`.

Schoenberg's construction then identifies `lambda_n` with the squared
displacement of a Hilbert cocycle. This is an exact reformulation, not an RH
proof; its value is to expose mixed-order finite falsifiers and the precise
kernel a source energy must produce. An uncertified 80-digit probe finds
positive minimum eigenvalues through anchored rank twelve, with severe
near-degeneracy at the top rank. See `li-cnd-cocycle-equivalence.md` and the
probe result.

The CND kernel further reduces exactly to stationary increments. Define
`c_0=lambda_1` and
`c_k=(lambda_(k+1)-2lambda_k+lambda_(k-1))/2`. At rank `N`, the anchored
Gram factors as `K_N=S_N T_N S_N^T`, where `T_N=(c_(|i-j|))` is Toeplitz and
`S_N` is unit lower-triangular summation. Therefore `K_N>=0` exactly when
`T_N>=0`. Gate C can now target one source-positive correlation measure with
Fourier coefficients `c_k`; discrete integration then supplies every mixed
Li inner product. See `li-toeplitz-increment-gate.md` and its exact symbolic
checker.

The two required mechanisms are abstractly compatible. If an archimedean
self-adjoint `H_0` has compact resolvent and the transported prime
interaction `V` is symmetric with relative bound below one, then `H_0+V`
remains self-adjoint with compact resolvent and `i(H_0+V)` is a discrete
skew-adjoint zero-coordinate candidate. The classical region
`x>=a,p>=b,xp<=E` has area `E log(E/(ab))-E+ab`; choosing `ab=2pi` reproduces
the two leading Riemann--von Mangoldt terms after division by `2pi`. Its
constant is `1`, exposing the required `-1/8` boundary/Maslov correction.
This is a compatibility theorem, not an Xi operator or determinant identity.
See `archimedean-confinement-odd-arithmetic-coupling.md` and its checker.

The missing constant is now an exact boundary-phase gate. Stirling's formula
gives the gamma contribution `-pi/8` to `theta(T)`, hence the Xi counting
constant `7/8`. A quasiperiodic first-order boundary condition shifts the
smooth count by `-alpha`, so the required value is `alpha=1/8`, with phase
`exp(i*pi/4)`. But the self-adjoint extension family permits every phase;
choosing this one after seeing Xi is curve fitting. A valid explanation must
derive it from the gamma real structure, a Maslov/metaplectic index, or
compatibility with the arithmetic correspondence. See
`archimedean-boundary-phase-gate.md` and its checker.

Elementary real structures do not select that phase. Plain conjugation
preserves a quasiperiodic boundary domain only for phases `+1` and `-1`, so
it excludes `exp(i*pi/4)`. Conjugation combined with endpoint reflection
preserves every unit phase and therefore selects nothing. The
functional-equation involution alone cannot derive the `1/8` in this model;
a metaplectic/Maslov lift, corner condition, or arithmetic-boundary coupling
is genuinely required. See `boundary-real-structure-phase-no-go.md` and its
checker.

The metaplectic escape route has the correct discrete arithmetic. Canonical
continuation of the positive Gaussian to a signature-one Fresnel form gives
`exp(i*pi/4)`, hence boundary offset `1/8`; subtracting it from the elementary
phase-space constant yields `7/8`. General signatures give eighth roots
`exp(i*pi*sigma/4)`, replacing a freely tuned `U(1)` phase by an integer
Maslov index. Orientation reversal changes the sign, so the completed gamma
structure must select both signature and orientation. No Xi symplectic
boundary correspondence has yet been constructed. See
`metaplectic-eighth-phase-candidate.md` and its checker.

The full gamma factor now has a concrete compact-resolvent auxiliary
operator, not merely an asymptotic phase. The harmonic oscillator restricted
to even parity and divided by four has spectrum `k+1/4`; its zeta-regularized
shifted determinant is `sqrt(2pi)/Gamma(1/4+z)`. Thus parity and zero-point
energy canonically select the quarter shift, while Stirling recovers the
eighth-phase constant. This oscillator is not Hilbert--Polya: its own
spectrum is linear, and the Xi `T log T` term comes from determinant phase.
The next gate is a prime relative determinant compatible with the
incidence-derived Hilbert metric. See
`gamma-factor-even-oscillator-determinant.md` and its exact checker.

The Euler factor also has an exact auxiliary determinant in its honest
domain. On `l2(primes)`, `P_s e_p=p^(-s)e_p` is trace class for `Re(s)>1`
and `zeta(s)=det_F(I-P_s)^(-1)`; its logarithmic derivative produces the
von Mangoldt series. But on `Re(s)=1/2`, `sum_p|p^(-s)|^2=sum_p1/p`
diverges, so `P_s` is not even Hilbert--Schmidt and the same Fredholm
determinant does not exist. Analytic continuation must not be relabeled as
that determinant. The next gate is a combined prime--gamma--endpoint
relative regularization compatible with the adjoint symmetry. See
`prime-fredholm-determinant-and-critical-line-gate.md` and its checker.

Schatten regularization reaches the critical line but exposes an information
gate. Since `P_s` belongs to `S_3` for `Re(s)>1/3`, the third determinant
`det_3(I-P_s)` is canonical there and removes prime repetitions `k=1,2`.
It is nonvanishing throughout `Re(s)>0`, so it carries no Riemann zeros.
Every zero-producing feature is displaced into the analytically regularized
low-order counterterm. Thus `det_3` is a useful high-repetition factor but
cannot be called the zeta determinant. The hard target is a canonical joint
construction of those two channels with gamma and endpoint anomalies. See
`prime-third-determinant-information-gate.md` and its checker.

The removed quadratic channel is exactly the divergent Hermitian prime norm.
On the critical line, amplitudes `p^(-1/2-iT)` have squared norm
`sum_p1/p`. Gaussian damping in `log p` makes the norm finite, matching the
natural source heat regularization, but the diagonal norm is independent of
`T` and cannot locate zeros. Spectral height survives only in off-diagonal
terms `exp[-iT(log p-log q)]`, so the relative difference correspondence is
essential rather than decorative. A paired source theorem must combine a
renormalized diagonal with this off-diagonal kernel. See
`smoothed-prime-Hermitian-norm-gate.md` and its checker.

The incidence-derived valuation metric restores height dependence but cannot
itself be the spectral equation. For one prime its reference-subtracted
energy is
`2p^(-1/2)[1-cos(T log p)]/(1-p^(-1))`, and a Gaussian-smoothed sum over
primes is nonnegative and vanishes only at `T=0`. Hence this metric is a
legitimate phase-sensitive control norm, but termwise positive prime energy
cannot generate the nonzero Xi ordinates. Signed determinant interference or
archimedean coupling remains essential. See
`prime-valuation-phase-energy-no-go.md` and its checker.

Zero production is necessarily global. Every local Euler factor is nonzero
for `Re(s)>0`, the gamma factor has no zeros, and any locally absolutely
convergent product of nonzero holomorphic local determinants remains
nonzero. Therefore Xi zeros cannot originate prime by prime or from a
termwise positive Euler energy. They must be created by the failure of local
absolute convergence and its global repair: analytic continuation, a
relative-determinant anomaly, or a boundary condition coupling infinitely
many primes to the archimedean sector. See `Euler-local-zero-no-go.md` and
its checker.

A concrete global zero-production mechanism now survives the local no-go.
For positive invertible local blocks `A,B` and coupling `C`, the block
determinant factors as `det(A)det(B)det(I-T*T)`, with
`T=A^(-1/2)CB^(-1/2)`. Local determinants can remain nonzero while the
coupled determinant vanishes exactly when a singular value of `T` reaches
one; block positivity is equivalent to contractivity. Holomorphically, a
paired family `F(s)=det[I-C(1-s)C(s)]` restricts on the critical line to
`det[I-C(s)*C(s)]` under the real structure. This reconciles global
holomorphy with line-wise Hermitian control. No Xi coupling or off-line
invertibility theorem is yet constructed. See
`paired-gluing-determinant-mechanism.md` and its checker.

The remaining RH-strength statement is now isolated as global transfer
contractivity. A determinant representation
`xi(s)=E(s)det[I-K(s)]` with critical-line form
`K=C(s)*C(s)` would imply RH if the spectral radius of `K(s)` were strictly
below one off the line. This says prime--archimedean feedback is lossy away
from reflection balance and reaches unit gain only at Hermitian threshold
resonances. Symmetry alone does not suffice: the scalar paired family
`1-(w^2+sqrt(2)w+2)(w^2-sqrt(2)w+2)` has a genuine quartet with real parts
`+-0.605...` and imaginary parts `+-1.168...`, despite the correct line-wise
norm form. See `global-transfer-contractivity-conjecture.md` and its hostile
checker.

Contractivity now reduces to one concrete coupled positivity target. For a
holomorphic transfer family `C(s)` on `Re(s)>1/2`, positivity of the
de Branges--Rovnyak kernel
`[I-C(w)*C(s)]/[s+conj(w)-1]` is equivalent to the Schur bound; strict
diagonal positivity gives strict off-line contraction. Boundary unit-gain
resonances remain possible because the denominator collapses at the fixed
line. A positive-real/Herglotz source family yields the same condition by
Cayley transform, reconnecting to the earlier `xi'/xi` Caratheodory target.
The new falsifiers are finite kernel Gram minors. No arithmetic Xi transfer
kernel is yet constructed. See `de-branges-transfer-kernel-target.md` and
its checker.

The abstract kernel target is now tied canonically to Xi. With
`Xi(z)=xi(1/2+z)` and `F=Xi'/Xi`, the kernel
`[F(z)+conj(F(w))]/[z+conj(w)]` is RH-equivalently positive on the right
half-plane. Under RH, each boundary zero `i gamma` contributes the rank-one
Cauchy Gram feature
`1/[(z-i gamma)(conj(w)+i gamma)]`; conversely, an off-line zero creates an
interior pole and positivity/holomorphy fail. This is the completed two-point
form the source correspondence must reproduce, with endpoint, gamma, and
prime pieces coupled before taking positivity. See
`xi-log-derivative-Herglotz-kernel.md` and its checker.

The honest source-region decomposition has a strict sign and transport gate.
Each prime-power contribution to the canonical Herglotz kernel has negative
diagonal at real `z>1/2`, so no prime-by-prime positive Gram decomposition is
possible. At `s=1`, the endpoint pole cancels the pole of `zeta'/zeta`, while
the raw prime series itself diverges; endpoint and prime kernels cannot be
continued independently or placed in an ordinary orthogonal sum. The source
realization must be a completed relative Gram construction, plausibly an
indefinite local bookkeeping space followed by a positive quotient or Schur
complement. See `completed-source-Herglotz-kernel-gate.md` and its checker.

The local sign obstruction now has a canonical algebraic completion. Put the
archimedean and prime bookkeeping sectors in a Krein direct sum with signs
`+` and `-`, and restrict to the graph `(a,Ca)` of their coupling. The
induced metric is `I-C*C`; it is positive exactly for a contraction, becomes
null at a unit singular value, and has Gram determinant `det(I-C*C)`. Thus
negative prime diagonals, global contractivity, completed positivity, and
threshold determinant zeros are four faces of one graph theorem. At a zero,
quotienting the null state restores a Hilbert space while recording
multiplicity. This remains algebraic: Xi source spaces and the physical
relative-chain pushforward are unavailable. See
`Krein-graph-completion-theorem.md` and its checker.

Positive gluing loses determinant orientation. On the critical line,
`det(I-C*C)` is nonnegative and every isolated analytic zero has even order;
a generic unit-singular-value contact is quadratic. It therefore naturally
models `xi(1/2+iT)^2` or an absolute square, not the signed Xi function with
its actual multiplicities. Recovering `xi` requires an oriented determinant
line or Pfaffian: the elementary skew block has determinant `T^2` but
Pfaffian `T`. The metaplectic/Maslov orientation is a candidate source for
this square-root datum. Any model must explicitly distinguish `xi` from its
square. See `positive-gluing-determinant-square-root-gate.md` and its checker.

The determinant-line issue is now narrower. A nonzero nonnegative analytic
function on a connected interval has an analytic square root unique up to one
global sign, so a genuine squared-Xi construction would need only base-point
normalization, not independent choices at every zero. But the elementary
skew block `[[0,f],[-f,0]]` realizes any preselected analytic `f` as a
Pfaffian; setting `f=Xi` is therefore circular. The next gate is a
cutoff-compatible skew lift built entrywise from archimedean and prime data,
whose determinant identity precedes any identification with Xi. See
`pfaffian-noncircularity-gate.md` and its checker.

The finite-cutoff skew-lift target meets a universal algebraic obstruction.
Every skew determinant is a square, whereas the smallest scalar transfer
determinant is `1-x^2`, which has simple roots and is not a polynomial square.
Canonical block skew-doubling has Pfaffian equal to the original determinant,
not its square root. Thus contractivity alone cannot supply signed Xi: a
separate source symmetry must force square factorization at every cutoff.
The scalar specialization is the hostile falsifier. See
`finite-cutoff-pfaffian-lift-no-go.md` and its checker.

There is one precise square-forcing mechanism: Kramers/quaternionic symmetry. If
an antiunitary `Theta` squares to `-I` and commutes with each Hermitian
transfer Gram operator, every eigenvalue has even multiplicity and the
complex determinant is the square of its Moore determinant. On a positive
analytic Gram family this over-doubles zeros: a vanishing nonnegative
eigenvalue has even order, and its Kramers-paired determinant contribution
has order divisible by four, not the order two required by `Xi^2` at a
simple zero. Moreover, critical-line
conjugation and functional-equation reflection square to `+I`; the real
diagonal hostile model shows that this does not force a square. The revised
only remaining version of this target must live on the indefinite
pre-quotient rather than the final positive Gram space. See
`quaternionic-square-forcing-gate.md` and its checker.

The minimal surviving square-root architecture is instead first order. A
source-defined oriented boundary map `Q` gives the positive composite
`B=Q*Q`, with `det B=|det Q|^2`; a simple signed zero of `det Q` becomes the
required double Gram zero without Kramers over-doubling. The chiral block
`[[0,Q*],[Q,0]]` is self-adjoint automatically. But the construction order is
essential: factoring a completed `B` by a matrix square root or Cholesky
decomposition is tautological. The sharpened target is a relative boundary
map satisfying `I-C_P*C_P=Q_P*Q_P` from source geometry at every cutoff. See
`oriented-first-order-factorization-target.md` and its checker.

The paired Mackey correspondence supplies the first non-tautological `Q` in
finite rank. A normalized regular incidence `U` is an isometry; splitting its
source correspondence into admitted and relative-complement parts gives
`C=P_in U`, `Q=P_out U`, and the exact identity
`I-C*C=Q*Q`. Thus `Q` is omitted incidence, not a post-hoc square root. The
hostile `C2` difference quotient also exposes the limit: a fixed unweighted
split gives only the constant defects `0`, `1/2`, or `1`, with no analytic
height dependence, and `Q` is generally rectangular. The remaining target
is an oriented determinant-class relative complex with source-derived
archimedean weights preserving the Parseval identity. See
`relative-complement-incidence-factorization.md` and its checker.

Rank-one analytic weighting is too universal to explain a zero set. Parseval
reduces it to `c=cos(theta)`, `q=sin(theta)`; equivalently the rational circle
parametrization imports the zeros of an arbitrary analytic input `u` directly
into `q`. The independently known gamma phase gives only smooth Gram-type
levels, while multiplying the canonical prime and archimedean scalar phases
collapses to the functional-equation identity. Hence scalar weighting either
misses the zeros or inserts them. The smallest surviving interference target
is a two-channel oriented relative map with independently source-derived
entries. See `rank-one-parseval-phase-no-go.md` and its checker.

Rank two supplies the first genuine interference invariant. For
`Q=[[a,b],[c,d]]`, the determinant `ad-bc` can vanish while every entry is
nonzero, and `ad/(bc)` is invariant under row and column gauge rescaling: it
is the holonomy of the smallest bipartite four-cycle. In the Hermitian real
form this becomes `AD-|P|^2`, with a self-adjoint chiral lift and the correct
simple-root/double-Gram-root pattern. At a genuine interference zero both
matching products must remain nonzero; otherwise rank two hides scalar
encoding. The next construction must realize the matchings as independently
normalized prime and archimedean routes. See
`two-channel-cycle-interference-target.md` and its checker.

The two-channel square requires a type correction. Exact conjugation matching
on `N` atoms has rank `N`, whereas any fixed family of separable scalar traces
has bounded rank. Thus the four-cycle cannot be one numerical `2x2` matrix;
it must be `2x2` over an operator or correspondence algebra whose internal
rank grows with the cutoff. The zero-divisor copy map has the right rank but
is tautological on the source side. A valid construction must instead build
finite source incidence squares and specify a compatible ordinary, Fredholm,
or torsion determinant before scalarization. See
`two-channel-operator-valued-type-correction.md` and its checker.

The growing graph also fails the naïve determinant-class gate. With `m`
conjugate pairs its swap operator has trace norm `2m` and Hilbert--Schmidt
norm squared `2m`; the infinite unweighted correspondence is unitary and
noncompact. Its finite determinant is `(1-z^2)^m`, which does not stabilize.
Weighted blocks admit an ordinary Fredholm determinant only for `l1` weights
and a regularized `det_2` for `l2` weights. A relative determinant instead
requires a reference whose difference is determinant class. Thus the next
source obligation is a proved Schatten decay estimate plus independent
regularization normalization. See
`conjugation-graph-determinant-class-gate.md` and its checker.

The prime Schatten threshold isolates exactly two anomalous channels. The
canonical `det_3(I-P_s)` retains repetitions `k>=3` and is nonvanishing;
Euler bookkeeping removes precisely `C_1=sum_p p^-s` and
`C_2=(1/2)sum_p p^-2s`. Their forced coefficients match the minimal
two-channel square, but independent analytic scalar exponentials cannot
create the omitted zeros. The two channels must be jointly renormalized with
gamma and endpoint sectors as a determinant-line anomaly before
scalarization. This is a structural match, not a construction. See
`two-low-order-channel-anomaly-target.md` and its checker.

The quadratic low-order channel is itself the second Adams operation:
`C_2=(1/2)Tr(P_s^2)`. This meets the earlier Mackey obstruction exactly. An
`n`th power commutes with a kernel correspondence only when
`gcd(n,exp K)=1`; for `C2->1`, the second power gives
`q_![2]^*delta_0=2` but `[2]^*q_!delta_0=1`. The logarithmic factor `1/2`
does not repair the square because averaging changes the frozen selector.
Thus any shared realization must treat the quadratic channel as a
degree-two descent anomaly, plausibly in the norm complex `(N,2-N)`, rather
than a strict Mackey morphism. The analytic torsion identity remains open.
See `quadratic-prime-channel-mackey-anomaly.md` and its checker.

The finite norm complex cannot by itself supply the analytic quadratic
counterterm. Ordinary torsion of a finite complex with algebraic dependence
on `x=p^-s` is rational in `x`, whereas `exp(+-x^2/2)` is not rational: its
logarithmic-derivative equation has a two-degree contradiction. Thus
`(N,2-N)` correctly types the second-Adams descent anomaly but cannot produce
its exact exponentiation. A Gaussian/Fock enlargement, determinant anomaly,
or infinite regularized torsion is unavoidable and must still be derived
before coupling to gamma and endpoints. See
`finite-norm-torsion-quadratic-exponential-no-go.md` and its checker.

Gaussian exponentiation explains the otherwise mysterious half coefficient:
the second cumulant of the prime source is
`(1/2)sum_p p^-2s`. But the positive Fock norm on the critical line is
`sum_p|p^-s|^2=sum_p1/p`, so the source is not Cameron--Martin at any height.
Wick ordering subtracts exactly the required quadratic channel, and heat
smoothing leaves a height-blind variance diverging as smoothing is removed.
The algebraic symplectic double does not select the missing covariance or
vacuum. Only a relative prime--gamma--endpoint Gaussian construction whose
positive divergences cancel before the boundary limit survives. See
`gaussian-quadratic-channel-cameron-martin-gate.md` and its checker.

The even oscillator supplies a canonical relative covariance subtraction.
Prime variance through `P` is `log log P+B_1+o(1)`; the inverse covariance of
the gamma oscillator levels `k+1/4` through `K` is
`log K-psi(1/4)+o(1)`. Since prime source positions are `log p`, the shared
cutoff `K=floor(log P)` cancels the leading divergence and leaves
`B_1+psi(1/4)`. The quarter shift fixes the finite archimedean term, while a
rescaling `K=floor(c log P)` would visibly shift it by `-log c`. This is a
relative/Krein subtraction, not a positive covariance, and it does not yet
retain the height-dependent bilinear phase. See
`logarithmic-prime-oscillator-covariance-cancellation.md` and its checker.

The covariance match is not a mode duality. Prime height phases are generated
by `diag(log p)`, while gamma oscillator modes are `k+1/4`. A strict
intertwiner would require `log p=k+1/4` for every nonzero matrix coefficient,
which is impossible by Lindemann--Weierstrass; hence the intertwiner is zero.
Pairing `p` with `floor(log p)` therefore destroys exact phase information.
The completed coupling must be a non-diagonal integral correspondence, and
its commutator `AX-XL_prime` must participate in the Schur complement rather
than vanish. See `prime-oscillator-intertwiner-no-go.md` and its checker.

A concrete non-diagonal coupling passes the first analytic gates. Evaluating
the even-oscillator semigroup at `u_p=log p` and multiplying by the critical
prime amplitude gives `X_T(k,p)=p^{-(k+3/4)-iT}`. Both `X_T` and
`AX_T-X_TL_prime` are Hilbert--Schmidt. Finite square cutoffs are scaled
Vandermonde matrices in `1/p`, hence have full growing rank. Their determinant
is always nonzero, so this is only an incidence leg; zeros must arise from
the completed Schur complement. The next falsifier is exact recovery of the
Euler-region prime Green matrix element. See
`prime-oscillator-semigroup-incidence-kernel.md` and its checker.

The semigroup kernel fails its first proposed Schur identification. A
self-adjoint Schur correction is quadratic in coupling weights; for `X_T` its
lowest diagonal exponent is `p^-3/2` and off-diagonal terms carry products
and ratio phases. The exact Euler Green term is linear in
`Lambda(n)n^(-1/2-y)` and includes all prime powers. No scalar normalization
can reconcile them. The Euler contribution must remain an off-diagonal
boundary-to-source resolvent entry, preserving coefficient and Betti legs;
`X_T` can only be a separate Schatten comparison transform. The revised
target is a two-boundary Weyl matrix with the exact linear Euler cross entry
and gamma-renormalized diagonal covariances. See
`semigroup-kernel-schur-weight-mismatch.md` and its checker.

The corrected paired Weyl matrix has an exact finite theorem. The free
logarithmic resolvent kernel `exp(-y|u-v|)/(2y)` gives a positive Green Gram
matrix for the boundary point `0` and the truncated von Mangoldt source at
`log n`; its oriented cross entry is exactly
`+-(1/(2y))sum Lambda(n)n^(-1/2-y)`, including all prime powers. But the
source diagonal contains `sum Lambda(n)^2/n` and diverges even where the cross
entry converges. Hence the raw infinite positive matrix does not exist.
Gamma/endpoint cancellation must occur at the indefinite form level before a
positive quotient, while preserving the linear cross term. See
`finite-euler-cross-weyl-positivity-and-diagonal-no-go.md` and its checker.

The raw diagonal cannot be canceled by the gamma oscillator: the exact
von-Mangoldt source gives `(1/2)(log P)^2` growth, whereas the quarter-shift
oscillator under `K=floor(log P)` gives only `log log P`. Among local source
metrics `(log p)^(-alpha)`, the prime number theorem shows that `alpha=2` is
the unique exponent reducing the diagonal to harmonic-prime size. This is the
candidate metric `||e_p||^2=1/Lambda(p)^2`, which preserves Lambda on the
linear coefficient leg while canceling it quadratically. It is not yet
source-derived and changes adjunction, so a weighted coefficient--Betti
pairing theorem is the next gate. See
`von-mangoldt-metric-divergence-matching-gate.md` and its checker.

Weighted adjunction now exposes the cost of that metric. For basis densities
`mu`, the adjoint of pullback is the density-ratio fiber sum and pull--push is
the weighted degree `sum_fiber(mu_G)/mu_H`, not automatically `|ker q|`.
Ordinary degree survives exactly under fiber balance. In the hostile `C2`
fiber, degree-two normalization and frozen delta transfer coexist only when
the two weights are equal. Thus `1/Lambda^2` cannot be installed on the
existing Mackey object without deriving balanced fibers or accepting a new
modular degree. See `weighted-coefficient-betti-mackey-adjunction-gate.md`
and its checker.

The reciprocal metric is source-derived on each prime-power ray. The
dimensionless valuation coordinate `a=log(p^a)/log p` divides primitive
logarithmic coefficients by `log p`, so pulling back its standard metric gives
`1/(log p)^2`. The von Mangoldt vector then has unit norm per exponent site,
and its critical quadratic mass is `sum_a p^-a=1/(p-1)`, of harmonic-prime
size. Coefficient scale `1/log p` and Betti scale `log p` remain dual. Because
the weight is constant along a fixed prime ray, cardinality Mackey norms
survive colorwise; fibers mixing distinct primes fail balance. The next object
is therefore a prime-colored incomplete tensor product, not a color-forgetting
quotient. See `valuation-normalization-derives-von-mangoldt-metric.md` and its
checker.

That prime-colored incomplete tensor product does not lie in the product
vacuum sector. Each normalized `p`-ray displacement has squared norm
`1/(p-1)`, whose prime sum diverges, so the coherent product has zero vacuum
overlap. Tensoring an independent positive gamma Fock factor cannot cancel
this because norms add. The completion must compare quasi-free sectors
relatively, use a nonvacuum representation, or begin in a Krein-Fock
pre-space and take a positive quotient, while retaining the linear Euler
cross functional. See `prime-ray-incomplete-tensor-sector-obstruction.md` and
its checker.

The simple gamma oscillator also fails rank/trace compatibility for a
relative quasi-free comparison. Prime cutoff `P` has `pi(P)` colored rays,
while covariance matching uses only `floor(log P)` oscillator modes; their
support-projection Hilbert--Schmidt gap is bounded below by the divergent rank
difference. Raising the oscillator cutoff to `pi(P)` repairs rank but changes
covariance growth from `log log P` to `log P`. Scalar trace cancellation is
therefore not Bogoliubov implementability. A surviving reference needs a
weighted many-to-one shell correspondence, source multiplicities, or a
nonunitary relative/Krein determinant. See
`prime-gamma-rank-trace-incompatibility.md` and its checker.

The many-to-one shell repair has a canonical quarter shift. For shells
`exp(k+c)<=p<exp(k+1+c)`, reciprocal-prime mass is
`log((k+1+c)/(k+c))=1/k-(c+1/2)/k^2+...`; matching the gamma covariance
`1/(k+1/4)=1/k-(1/4)/k^2+...` uniquely gives `c=-1/4`. With these shifted
shells the relative covariance ratio differs from identity by `O(k^-2)` plus
summable PNT error, hence is trace class; unshifted shells are only
Hilbert--Schmidt. Weighted incidence isometricly identifies each oscillator
mode with the shell-radial prime vector, leaving an orthogonal fluctuation
sector to retain exact prime phases. See
`quarter-shifted-prime-shell-trace-class-correspondence.md` and its checker.

Rank-one shell compression fails once height dynamics is retained. In the
asymptotic coordinate `r in [-1/4,3/4]`, projection of `exp(-iTr)` onto the
constant radial mode leaves fraction `1-sinc(T/2)^2`; multiplying by shell
mass `1/k` gives a harmonic divergence for generic `T`. Choosing a moving
radial vector does not help: its optimally gauged derivative has variance
`1/12` per shell, again weighted by `1/k`. Hence the analytic comparison needs
a multi-mode, naturally `L2` shell fiber. The constant mode still carries the
trace-class gamma covariance match; nonconstant modes must be controlled
separately. See `single-radial-shell-height-dynamics-no-go.md` and its checker.

The obstruction holds at every fixed finite shell rank. Distinct exponential
height vectors are linearly independent, so a rank-`m` fiber contains them at
only `m` heights, never on an interval. For the first `m` moment modes the
small-height residual begins at
`T^(2m)/[(m!)^2(2m+1)binom(2m,m)^2]`; any positive residual still multiplies
the harmonic shell mass. The live target is a growing-rank or full `L2` fiber
with locally uniform determinant bounds. See
`fixed-finite-rank-shell-height-dynamics-no-go.md` and its exact checker.

There is a constructive escape requiring far less than a full infinite fiber
in each finite shell. On every compact height set, centered Taylor/moment
rank `m_k=ceil(c log log k/log log log k)` makes the discarded phase mass
summable whenever `c>1/2`; factorial approximation beats the harmonic shell
weight and remains locally uniform under any fixed number of height
derivatives. This is a sufficient schedule, not an optimality theorem. The
operator target is now a quarter-shifted, slowly growing moment bundle with
weighted Mackey maps and a relative determinant. See
`growing-shell-rank-summability-schedule.md`.

The shell-kernel determinant is not discarded. The growing-rank estimate
makes the off-diagonal height leakage `B:V_shell->K_shell`
Hilbert--Schmidt. Its oriented double
`J_B=[[0,-B*],[B,0]]` then satisfies the universal identity
`det_2(I+J_B)=det(I+B*B)>0`: the quadratic kernel correction is trace class
and canonically positive. This is precisely why the Hilbert--Schmidt threshold
is structurally sufficient. It controls, rather than trivializes, Nima's
missing kernel determinant. Identifying the positive correction with any
piece of completed zeta remains an open source-derived comparison problem.
See `shell-kernel-coupled-positivity-theorem.md` and its exact checker.

The smallest native block test prevents overinterpreting that positivity.
For two equal-weight prime rays, height multiplication in the
constant/difference basis is `[[a,b],[b,a]]`; its exact determinant factors
as `a(a-b^2/a)=z_1z_2`. The auxiliary positive correction `1+|b|^2` is not
this Schur factor (`z_1=1,z_2=i` gives respectively `3/2` and a native full
determinant `i`). Thus growing-rank compression controls leakage but does not
source the oriented double. Coupled positivity becomes relevant only if the
coefficient--Betti/Mackey system independently supplies `B,-B*`. See
`two-ray-shell-schur-determinant-falsifier.md` and its exact checker.

The positive leakage factor is also spectrally incapable of carrying the
target zeros. On real height,
`det(I+B(T)*B(T))=product_j(1+s_j(T)^2)>=1`, so it is strictly zero-free. In
any proposed factorization `Xi=D_ret det(I+B*B)`, every critical-line zero
must come from `D_ret`. Coupled positivity is therefore a stability theorem
excluding spurious real zeros from the mapping-cone defect, not the
Hilbert--Polya spectral determinant itself. The retained quarter-shifted
moment bundle must still supply a canonical self-adjoint generator. See
`shell-leakage-positive-factor-zero-free-gate.md`.

The retained growing-moment bundle does carry a canonical self-adjoint
compact-resolvent generator: compress multiplication by `log p` to each
weighted shell moment space. In the PNT/Legendre model its block is a Jacobi
matrix with constant diagonal `k+1/4` and off-diagonal
`n/[2sqrt((2n-1)(2n+1))]`; the exact discrete version is the Jacobi matrix of
the reciprocal-prime shell measure. Its eigenvalues are translated Gaussian
quadrature nodes, not Riemann ordinates. Hence self-adjointness is constructible
without fitting, but spectral identification still fails. A nonlocal
coefficient--Betti Schur coupling would be required to rearrange the spectrum.
See `quarter-shifted-moment-jacobi-operator.md` and its exact checker.

The Riemann--von Mangoldt counting law rules out using the minimal
Hilbert--Schmidt rank as the spectral multiplicity. A shell-local operator has
`N_ret(T)=sum_(k<=T)m_k+O(m_T)`, so matching
`N_zeta(T)~T log(T)/(2pi)` forces average
`m_k~log(k/(2pi))/(2pi)`. The earlier
`log log k/log log log k` schedule is determinant-class but spectrally too
sparse. Thus the Weyl law fixes the leading shell rank, the quarter shift
fixes the block center, and the missing nonlocal coupling must rearrange the
Jacobi nodes without changing their density. See
`riemann-weyl-law-forces-logarithmic-shell-rank.md` and its diagnostic.

Integer shell dimensions must be derived from the cumulative Weyl count, not
by independently flooring its density. Local rounding loses an order-one
fraction per shell and creates an `O(T)` error that changes the linear Weyl
coefficient. The stable rule is
`m_k=floor(F(k+1))-floor(F(k))`, which telescopes with uniformly bounded
error. Taking `F` with constant `7/8` would still be fitted: phase-space area
gives constant `1`, so a source boundary/Maslov mechanism must derive the
missing `-1/8`. See `cumulative-weyl-shell-rank-allocation.md` and its checker.

The `-1/8` is now derived rather than fitted. Stirling's phase for the
completed gamma argument `1/4+iT/2` contributes
`(1/4-1/2)/2=-1/8` to `theta(T)/pi`; the separate argument-principle base
term `+1` yields `7/8`. Thus the same quarter-shifted archimedean datum fixes
both the Jacobi block centers and the smooth-count constant. The remaining
unexplained term is exactly `S(T)`, which the nonlocal prime coupling must
generate. See `quarter-shift-derives-seven-eighths-boundary-constant.md` and
its checker.

With the smooth count closed, the prime interaction has one exact target.
For `H=H_0+V`, its spectral shift must equal `-S(T)` (up to convention), and
the boundary phase of its perturbation determinant must reproduce the zeta
argument. This creates symmetry, determinant-class, phase, and no-inverse-fit
gates. A self-adjoint pair with the completed-zeta determinant would already
be a strengthened Hilbert--Polya realization; the reformulation alone proves
nothing. The hard content is deriving `V` from primes before knowing the
zeros. See `prime-coupling-spectral-shift-target.md` and its finite checker.

Schatten theory localizes that hard coupling. The canonical
`D_3=det_3(I-P_s)` is defined and nonzero on the critical line and contains
all prime repetitions `k>=3`; it supplies a smooth background phase but no
zero jump. After removing gamma and this background, every zero-producing
spectral shift is forced into the jointly renormalized channels
`C_1=sum_p p^-s` and `C_2=(1/2)sum_p p^-2s`. Independent scalar
exponentiation cannot vanish, so the two channels must form a coupled
determinant-line anomaly before scalarization. See
`spectral-shift-localizes-to-two-channel-anomaly.md`.

The canonical normalized shell map cannot itself be the paired gluing
operator. It is an isometry `W*W=I`, so
`det(I-W*W)=0` identically; unitary prime/gamma height dressing preserves this
degeneracy. Unnormalized mass comparison is height-independent and likewise
cannot produce the zero set. The required resonance variable is therefore a
source-derived nonunitary dynamical defect—continuation, supported resolvent,
mapping cone, or kernel-retaining Schur complement—inserted before
normalization. See `isometric-shell-gluing-identically-zero-no-go.md` and its
exact checker.

The common Adams-boundary divergence has a regulator-invariant relative
finite part. Sharp cutoffs give prime/gamma constants `B_1` and `-psi(a)`;
Abel cutoffs shift both by `-EulerGamma`, giving `B_1-EulerGamma` and
`-psi(a)-EulerGamma`. Their difference is `B_1+psi(a)` in either scheme, and
at `a=1/4` equals `B_1-EulerGamma-pi/2-3log2`. This closes the `T=0`
logarithmic finite part only; full height continuation still requires the
resolved mapping cone. See
`adams-boundary-relative-finite-part-regulator-invariance.md` and its exact
checker.

A type correction limits the shell-resonance branch. Gamma is represented by
the spectral resolvent/determinant of the oscillator, involving
`(k+1/4+iT/2)^(-1)`, not by unitary phases `exp[-iT(k+1/4)]`. The sinc and
odd-pi results remain valid aliasing theorems for radial prime phase
compression, and `C_2(s)=(1/2)C_1(2s)` remains exact; none exhibits a gamma
or Xi singularity. The next block must pair exact prime phases with
gamma/Jacobi resolvents through a non-diagonal kernel. See
`gamma-resolvent-versus-shell-time-phase-type-correction.md`.

The corrected functional calculi have a canonical log-time Fourier bridge:
`1/(a+iT/2)=2 integral_0^infinity e^(-2au)e^(-iTu)du`. Prime phases are
Fourier transforms of atoms at `u=log(p^m)`, while summing the gamma
resolvents gives continuous density `2e^(-u/2)/(1-e^(-2u))du` plus endpoint
distributions. The non-diagonal comparison must therefore act on measures or
currents before Fourier transformation. Shell moments are quadrature data,
not oscillator eigenmode matches. See
`log-time-fourier-bridge-prime-atoms-gamma-resolvent.md` and its checker.

After reflection and endpoint completion, this log-time current is exactly
the centered Weil explicit-formula distribution already constructed in the
program. Its positivity on convolution squares is equivalent to RH, so the
measure bridge must not be advertised as a positive factorization. The first
open source-only test returns to short-support gluing: for cells narrower than
`log2`, the initial arithmetic edge is prime two, and positivity requires the
normalized cross operator to be a contraction. The new mapping-cone machinery
is relevant only if it derives that inequality or a dilation implying it.
See `log-time-bridge-identifies-weil-form-and-prime-two-gate.md`.

Even universal two-cell contractions would not prove global Weil positivity.
The exact correlation matrix with diagonal `1` and every off-diagonal
`-3/4` has all `2x2` minors `7/16>0` but eigenvalue `-1/2` and determinant
`-49/32`. The first arithmetic cycle gate should therefore use cells at
`0,log2,2log2`, where two prime-two steps and the prime-four repetition must
obey an Adams/Mackey coherence constraint. Pairwise prime-edge numerics are
only the first gate. See `edgewise-weil-contractions-do-not-glue-triangles.md`
and its exact checker.

Exact Adams composition closes every cycle in a one-prime repetition tower.
If the normalized first edge is `r` and the `m`-step edge is `r^m`, the cells
`0,logp,...,nlogp` have Gram kernel `r^|i-j|`, positive for `|r|<=1`, with
determinant `(1-r^2)^n`. More general towers are controlled by successive
Schur/Verblunsky defect contractions, beginning with the triangle defect.
Thus one edge contraction plus a source composition theorem can replace
infinitely many prime-power positivity tests. Mixed-prime rectangles remain
open. See `one-prime-adams-tower-positive-gluing-theorem.md` and its checker.

Exact coprime Mackey interchange would close those mixed cycles. If exponent
vectors have kernel `product_p r_p^|alpha_p-beta_p|`, every finite prime
lattice is a tensor product of positive one-prime kernels. The first rectangle
then has determinant `(1-|r_p|^2)^2(1-|r_q|^2)^2`. Euler additivity does not
imply this factorization for the completed Weil form because gamma and
endpoints are global. The mixed falsifier must compare the direct `pq` edge
with both ordered Mackey routes. See
`coprime-adams-tensor-gluing-theorem.md` and its checker.

The first mixed rectangle has an exact nonfactorized test. With prime-edge
correlations `r,s` and diagonal-route correlations `c,d`, diagonal parity
splits the `4x4` Gram matrix into blocks
`[[1+c,r+s],[r+s,1+d]]` and
`[[1-c,r-s],[r-s,1-d]]`. Positivity is exactly the pair of contraction
inequalities `(1+c)(1+d)>=(r+s)^2` and
`(1-c)(1-d)>=(r-s)^2`. Exact interchange `c=d=rs` recovers the tensor theorem;
the holonomy `(c-d)/2` is now directly measurable. See
`mixed-prime-rectangle-parity-positivity-theorem.md` and its exact checker.

For a route-independent squarefree `d`-prime cube, the mixed-prime problem
has a complete finite Fourier criterion. Translation-compatible correlations
form convolution by `f` on `(C2)^d`; the Gram eigenvalues are the Walsh
coefficients `sum_x f(x)(-1)^(eta dot x)`, and positivity is equivalent to
their nonnegativity. Exact tensor interchange factors them as
`product_j[1+(-1)^eta_j r_j]`. Route holonomy must be eliminated before this
test; it cannot be averaged away. See
`squarefree-prime-cube-walsh-positivity-theorem.md` and its checker.

The exact tensor target is falsified for the arithmetic Weil block itself.
Von Mangoldt support is prime-power-only: for distinct primes,
`Lambda(p),Lambda(q)>0` but `Lambda(pq)=0`, while the product of the two edge
weights is nonzero. Euler multiplicativity becomes additive prime-power
support after logarithmic differentiation; it does not yield coprime Gram
factorization. Any completed rectangle positivity must therefore arise from
a gamma/endpoint or auxiliary Schur defect while preserving the missing
mixed-composite arithmetic atom. See
`von-mangoldt-support-falsifies-arithmetic-tensor-interchange.md` and its
checker.

The three-cell gate has an exact coupled-positivity factorization. For edge
correlations `a,b` and direct edge `c`,
`det G=(1-|a|^2)(1-|b|^2)-|c-ab|^2`. Hence pairwise contraction plus the
Adams/Mackey defect bound
`|c-ab|^2<=(1-|a|^2)(1-|b|^2)` is necessary and sufficient for triangle
positivity; exact composition makes it automatic. For the
`0,logp,2logp` scalar translation block this becomes
`|c_p2-a_p^2|<=1-|a_p|^2`. The operator extension is a defect-space
Parrott/Schur completion. See `three-cell-adams-defect-positivity-theorem.md`
and its exact checker.

The parity obstruction identifies the missing source map. The determinant
channels obey the exact Adams identity
`C_2(s)=(1/2)C_1(2s)`. On `s=1/2+iT`, the radial defect of the linear channel
at doubled argument is
`[sinc(T)-1]e^(-2iTk-iT/2)/k`, exactly the quadratic defect at `T`; the factor
`1/2` is forced by the logarithmic determinant. Thus the two-channel object
must be a relative cone over `s->2s`, not a same-height scalar matrix. This
aligns every odd-pi resonance but does not yet provide the finite part at the
`Re(2s)=1` boundary. See
`adams-doubling-aligns-shell-anomaly-channels.md` and its exact checker.

The scalar linear channel cannot cancel the quadratic resonance lattice. At
odd `T=(2j+1)pi`, the quadratic shell phase is `1` and its discrepancy sums
harmonically, whereas the linear shell phase is `(-1)^k` and its discrepancy
is bounded by alternating convergence. Analytic gamma/endpoint factors cannot
supply the missing logarithm. Hence even a coupled numerical `2x2` radial
determinant fails; cancellation requires operator-valued within-shell or
mapping-cone frequency mixing before scalarization. See
`linear-quadratic-shell-resonance-parity-no-go.md` and its exact checker.

The quadratic relative trace is dynamically singular despite its static
trace-class match. Shell averaging multiplies the centered gamma phase by
`sinc(T)`, leaving leading discrepancy
`[sinc(T)-1]e^(-2iTk-iT/2)/k`. It is only conditionally summable for generic
height and diverges harmonically at every nonzero `T=npi`. Since Xi is entire,
these artificial logarithmic resonances must cancel inside the joint
linear/quadratic mapping-cone determinant before scalarization. This is a
sharp new reason the two anomalous traces cannot be renormalized separately.
See `quadratic-shell-phase-resonance-lattice.md` and its diagnostic.

The acyclic-tail Schur mechanism also derives the anomalous coefficients.
For one operator `X`,
`log det(I-X)=-Tr X-(1/2)Tr X^2-sum_(n>=3)Tr(X^n)/n`; hence the linear and
quadratic prime channels with coefficients `1` and `1/2` are forced shadows
of a single Schur correspondence, not two adjustable counterterms. At the
critical line only these first two traces fail for an `S_3` prime operator;
the mapping cone must define their joint relative supertraces while leaving
a nontrivial physical Schur class. See
`schur-logarithm-unifies-two-prime-channels.md` and its exact checker.

An acyclic auxiliary tail supplies a concrete escape. Pair identical
superlogarithmic smoothing blocks `H_A` in even and odd degree, and couple the
physical Jacobi block only to the even copy. The auxiliary determinants and
Weyl multiplicities cancel in the graded count, while the physical determinant
retains the Schur self-energy
`-C(H_A-z)^(-1)C*`. This can regularize the moment boundary and create a
nonlocal zero-producing interaction without overcounting physical states.
Its legitimacy now depends on deriving the pair and coupling from the
coefficient--Betti mapping cone, rather than inserting ghost modes. See
`acyclic-tail-schur-self-energy-mechanism.md` and its exact checker.

Softening the moment boundary within the physical Weyl rank also fails. A
taper dropping from one to zero across `L_k` modes satisfies the sharp lower
bound `sum(delta w)^2>=1/L_k`; since Jacobi boundary coefficients have square
at least `1/16`, global leakage requires `sum_k1/(kL_k)<infinity`. The
Weyl-sized choice `L_k=O(log k)` leaves the divergent series
`sum 1/(k log k)`. A superlogarithmic smoothing tail can converge but would
overcount physical states unless it lies in a coefficient--Betti/Krein null
sector. Thus a mapping-cone cancellation is structurally forced for this
class of repairs. See `soft-moment-cutoff-weyl-tradeoff-no-go.md` and its
exact checker.

The growing-rank conclusion has been scope-corrected. Factorial moment
approximation controls the distinguished Euler source vector, but the full
generator leakage has top Jacobi coefficient
`a_m=m/[2sqrt((2m-1)(2m+1))] -> 1/4`. Hence its shell-mass-weighted square
still dominates `(1/16)sum_k1/k` for every hard rank schedule. No full
operator Hilbert--Schmidt or Fredholm conclusion follows from growing rank
alone; the coupled-positivity theorem remains conditional on independently
supplying such a `B`. See `growing-moment-generator-boundary-no-go.md` and its
exact checker.

Skew-adjointness and discreteness are now separated by a functional-analytic
no-go. Pure translation-invariant convolution on the noncompact logarithmic
line Fourier-diagonalizes as multiplication on a nonatomic space, whose
nonzero resolvent cannot be compact. The exact finite-grid shadow retains
arbitrarily many orthogonal modes with resolvent norm at least `1/sqrt(2)`.
Thus oddness can force an imaginary spectral axis but cannot produce the
discrete Xi ordinates. A successful operator needs an additional
archimedean/geometric confinement mechanism that preserves the adjoint
symmetry. See `translation-invariant-compact-resolvent-no-go.md` and its
checker.

The naïve infinite-rank Hermite reference is now falsified by global shape.
Riemann--von Mangoldt counting implies that Xi ordinates in `[-T,T]`, scaled
by `T`, converge to the uniform measure on `[-1,1]`; scaled Hermite roots
converge to the semicircle measure. Their unit-support second moments are
respectively `1/3` and `1/4`, so affine normalization cannot reconcile them.
The corrected candidate reference is the uniform log-gas potential
`V_U(x)=(1+x)log(1+x)+(1-x)log(1-x)`, or an equivalent Weyl-counting
coordinate. Its compatibility with Newman flow is the next derivation gate.
See `xi-window-hermite-reference-falsifier.md` and its exact checker.

Affine normalization cannot implement that correction. For a centered
closed rank-`N` Newman system, radius-normalized coordinates and time satisfy
`dx_i/dtau=A_i(x)-p x_i`, with `p=N(N-1)/2`; normalized discriminant
production is exactly `2 sum_i(A_i-px_i)^2`. Thus quadratic confinement and
Hermite stationarity are forced by the chain rule. A uniform Weyl reference
requires a nonlinear counting coordinate, the surviving exterior field, or
a density-dependent normalization. See
`newman-affine-normalization-rigidity.md` and its exact checker.

Nonlinear Weyl coordinates also carry an unavoidable dynamics anomaly. For
`z_i=f(r_i)`, the transformed velocity equals the inverse-gap force in `z`
plus the explicit divided-difference defect
`2 sum_j[f'(r_i)/(r_i-r_j)-1/(f(r_i)-f(r_j))]`. A coordinate change
conjugates every Newman system back to closed inverse-gap form, even up to a
global time factor, only when it is affine. Thus the Weyl-coordinate anomaly
is the required carrier of arithmetic density, and its entropy contribution
must be analyzed rather than dropped. See
`newman-coordinate-change-anomaly.md` and its exact checker.

The transformed entropy balance is now explicit. With mobility
`m_i=f'(r_i)^2`, Weyl-coordinate discriminant production is
`4 sum m_i A_i^2 + 2 sum A_i C_i[f]`. The first term is positive; the
coordinate-anomaly flux has unrestricted sign, with exact hostile and
reinforcing examples. Infinitesimally, for `f=r+epsilon h`, its pair kernel
is `(h_i-h_j)/(r_i-r_j)^2-h_i'/(r_i-r_j)` and begins locally at
`-h_i''/2`: coordinate curvature, not slope, is the leading source. The
research target is therefore a canonical Jacobian/potential correction that
completes a square with this flux. See
`newman-weyl-anomaly-entropy-balance.md` and its exact checker.

There is a canonical but conservative cure for the anomaly. The pairwise
divided-difference functional
`J_f=2 sum_{i<j} log|(f(r_i)-f(r_j))/(r_i-r_j)|` satisfies the composition
cocycle law and exactly gives
`log Delta(f(r))-J_f(r)=log Delta(r)`. Its derivative cancels the coordinate
anomaly identically. This proves both covariance and a no-go result: a Weyl
coordinate plus its canonical cocycle creates no new positivity. Any advance
must add a separately justified arithmetic fluctuation or exterior-field
potential. See `newman-divided-difference-cocycle.md` and its exact checker.

The first genuinely arithmetic remainder has now been isolated. Smooth Weyl
flattening gives `z_n=n-1/2-S(gamma_n)`, so its relative lattice entropy is
`2 sum_{i<j} log|1-(S_j-S_i)/(j-i)|`. It has unrestricted global sign: exact
three-point configurations yield ratios `9` and `9/64`. Its finite-window
linear variation is an explicit antisymmetric harmonic boundary field;
after removing that field, the quadratic bulk variation is the negative
nonlocal Dirichlet form
`-sum_{i<j}(epsilon_j-epsilon_i)^2/(j-i)^2`. This identifies arithmetic
rigidity but leaves higher-order and near-collision control open. See
`xi-weyl-lattice-fluctuation-entropy.md` and its exact checker.

The harmonic boundary field admits a canonical global renormalization.
For `z_i=i+epsilon_i`, put
`u_ij=(epsilon_j-epsilon_i)/(j-i)`. Ordering gives `u_ij>-1`, and the
tangent-renormalized divergence
`D_N=2 sum_{i<j}[u_ij-log(1+u_ij)]` is nonnegative term by term. Equality
holds exactly for translations of the integer lattice, its quadratic germ
is the positive nonlocal Dirichlet energy, and flattened collisions have
infinite cost. For Xi, `u_ij=-(S_j-S_i)/(j-i)`. This is the first universal
coupled positivity theorem in the Weyl-fluctuation lane, but it presupposes
real ordered zeros; a source-side continuation through nonreal zeros is the
next gate. See `xi-weyl-lattice-tangent-divergence.md` and its checker.

The source-side continuation gate has a sharp complex no-go. The direct
holomorphic continuation of the scalar gap divergence, followed by real
part, equals `-log 2` at the nonzero multiplier `1+i`. More generally, the
open-mapping theorem forbids a nonconstant holomorphic function from being
real nonnegative on an open complex domain. A radial Hermitian repair
`|w|^2-1-log|w|^2` is positive but blind to rigid phase rotation. Hence a
valid off-line extension must be both Hermitian and phase-sensitive, using
the critical-line reflection involution rather than gap moduli alone. See
`xi-complex-lattice-divergence-no-go.md` and its hostile checker.

A precise Hermitian spectral target is now fixed:
`H_Xi=sum_rho (Re(rho)-1/2)^2/[1+|rho-1/2|^2]`. It converges absolutely by
the critical-strip bound and Riemann--von Mangoldt counting, is nonnegative,
and vanishes exactly under RH. The smallest functional-equation-compatible
off-line quartet contributes strictly positively (`4/81` at
`beta=3/4,T=2`). This is only a spectral restatement; its value is that it
specifies the nonlinear quantity a doubled explicit formula or paired
coefficient--Betti correspondence must realize on the source side. See
`xi-hermitian-reflection-defect.md` and its exact checker.

The reflection defect now has a canonical operator form. On the divisor
Hilbert space let `Z e_rho=(rho-1/2)e_rho` and
`A_Xi=Re(Z)(I+Z*Z)^(-1/2)`. This is bounded, self-adjoint, and
Hilbert--Schmidt; its squared Hilbert--Schmidt norm is exactly `H_Xi`, so RH
is equivalent to `A_Xi=0`. The hostile quartet has spectrum
`{1/9,1/9,-1/9,-1/9}` in the concrete test. This is not Hilbert--Polya and
not a proof because `Z` is built from the zero divisor. It sharpens the
source target to constructing the same normal operator and real structure
arithmetically, with an independent vanishing identity. See
`xi-reflection-defect-operator.md` and its exact checker.

The required pairing is now a precise Mackey/correspondence object. The
bivariate rational kernel
`K(rho,sigma)=[((rho-1/2)+(sigma-1/2))/2]^2/[1+(rho-1/2)(sigma-1/2)]`,
restricted to the graph `sigma=conj(rho)`, has trace exactly `H_Xi`. An
independent product trace is not equivalent: in the hostile quartet it is
`102670472/9783585` instead of `4/81`. For the free conjugation quotient,
fiber-sum after pullback gives `q_*q^*=2I`; a fixed point changes this to the
orbit-cardinality operator `diag(1,2)`. These are algebraic finite-divisor
identities only. The prime-side graph projector and physical relative-chain
pushforward remain unavailable. See
`xi-conjugation-graph-correspondence.md` and its hostile `C_2` checker.

The graph trace has an exact positive heat representation. With
`X=Re Z`, define `Theta_H(t)=Tr[X^2 exp(-tZ*Z)]`. It is finite and
nonnegative for every positive `t`, its Laplace transform is `H_Xi`, and
vanishing at even one time is equivalent to RH. The hostile quartet gives
`exp(-65t/16)/4` and Laplace mass `4/81`. This sharply separates the needed
Hermitian semigroup `exp(-tZ*Z)` from the existing holomorphic heat object
`exp(-tZ^2)`; they differ already in the smallest off-line test. The next
source gate is an arithmetic construction of the paired positive semigroup.
See `xi-hermitian-defect-heat-bridge.md` and its exact checker.

The conjugation graph cannot be synthesized by a fixed finite family of
ordinary scalar tests. On an `N`-point conjugation-stable truncation its
matching kernel is a permutation matrix of rank `N`; a sum of `m` separable
one-variable channels has rank at most `m`. Exact realization therefore
requires `m>=N`, and no fixed finite scalar reduction survives growing
windows. The hostile quartet already has graph rank four. This leaves
operator-valued, reproducing-kernel, Hilbert-module, or infinite-channel
source correspondences viable. See
`xi-graph-projector-separable-rank-no-go.md` and its exact checker.

The graph projector is now formalized as a twisted spectral-copy
correspondence. On the atomic divisor basis,
`C_J e_rho=e_rho tensor e_conj(rho)` satisfies `C_J* C_J=I` and
`C_J C_J*=P_Gamma`; compressing the bivariate kernel through `C_J` gives the
RH defect trace. A real structure alone does not choose this copy map:
different real orthonormal bases give different diagonal subspaces. The
source object must therefore include an atomic commutative dagger-Frobenius
algebra, or an equivalent maximal abelian spectral refinement, in addition
to a normal operator and conjugation. Graph-copy normalization is `I`, while
orbit-quotient pull--push normalization is `2I`; these correspondences must
not be conflated. See `xi-spectral-copy-correspondence.md` and its checker.

Finite Fourier duality now supplies the exact source model for spectral
copying. For a finite abelian group `G`, conjugation-twisted character copy
transports to the normalized difference correspondence
`|x> -> |G|^(-1/2) sum_{a-b=x}|a,b>`. Its unnormalized incidence satisfies
`I_diff* I_diff=|G|I`, deriving the kernel/fiber norm rather than postulating
it; normalization restores an isometry. Exact cyclic checks pass for orders
two, three, and four. This makes convolution/difference fibers the preferred
source attack direction, while remaining separate from the unavailable Xi
physical relative-chain transform. See
`fourier-dual-copy-difference-correspondence.md` and its checker.

The infinite-source limit has a Haar-volume obstruction. For a locally
compact group, difference pullback satisfies formally
`||Df||^2=vol(G)||f||^2`. It is an isometry for normalized compact Haar
measure, but unbounded on a noncompact group. The exact hostile `Z` test
takes `f=delta_0`: its image is the infinite diagonal, with squared norm
`2M+1` in `[-M,M]^2`. Thus logarithmic prime space needs a compact quotient,
relative tensor product, semifinite trace per volume, compatible weight, or
controlled finite-quotient limit. Dividing by an infinite formal kernel size
is not admissible. See `difference-correspondence-noncompact-obstruction.md`
and its checker.

The center-of-mass divergence has a canonical abstract repair. Diagonal
translation identifies `(GxG)/diag(G)` with `G` by `[a,b] -> a-b`, making
relative difference pullback unitary for the transported quotient Haar
measure. But arithmetic coefficients do not automatically descend: pairs
`(2,3)` and `(10,15)` represent the same ratio while their von Mangoldt
product weights are respectively `log(2)log(3)` and zero. Thus geometry can
be quotiented, but a separate coefficient cocycle or module is mandatory to
retain prime information. This proves the abstract relative theorem while
leaving the physical relative-chain pushforward unavailable. See
`relative-difference-quotient-and-arithmetic-weight-gate.md` and its checker.

The first viable arithmetic coefficient repair is exact. Divisor-poset
pushforward sends the von Mangoldt function to the logarithmic potential,
`sum_{d|n}Lambda(d)=log n`; its pair difference `log(m/n)` is invariant under
common scaling and therefore descends to the relative ratio quotient.
Möbius inversion recovers `Lambda` when the divisor incidence is retained,
so the passage need not erase prime data. This produces a concrete paired
system: von Mangoldt coefficients, divisor pushforward, and a quotient-
compatible logarithmic cocycle. Identifying its norm with the Hermitian Xi
defect remains open, as does any physical chain realization. See
`von-mangoldt-divisor-cocycle.md` and its exact checker.

The Hilbert norm audit blocks a premature positivity claim. On
`{1,...,N}`, the divisor-zeta matrix has Gram entries
`(B*B)_(d,e)=floor(N/lcm(d,e))`; its Möbius inverse is not its adjoint. No
positive diagonal site weighting can orthogonalize divisor columns, because
every common multiple contributes a strictly positive overlap. Polar
normalization produces an isometry only through the nonlocal operator
`(B*B)^(-1/2)`, whose Euler-product meaning is unknown. Thus exact
coefficient recovery survives, but local Hilbert pull--push and the
Hermitian Xi norm do not yet follow. See
`divisor-pushforward-Hilbert-norm-obstruction.md` and its checker.

Prime-exponent coordinates give a canonical positive repair. On a finite
Euler box the divisor-zeta transform factors as tensor products of chain
summation matrices; its inverse factors as first differences. Equipping the
potential side with `M_E=(B^-1)*B^-1` makes divisor pushforward exactly
unitary. Each one-prime factor is a tridiagonal discrete Dirichlet metric,
so the correction is non-diagonal in integer sites but nearest-neighbor in
valuation and Euler-factorized. Exact checks pass on chain shapes `2`, `3`,
`2x3`, and `2x2x2`. Infinite tensor convergence, archimedean coupling, the
Hermitian Xi identification, and physical relative-chain pushforward remain
open. See `prime-exponent-divisor-Hilbert-metric.md` and its checker.

A candidate vanishing law has finally emerged. A real source kernel odd
under leg exchange/difference inversion defines a skew-adjoint convolution
operator; under Fourier transform its multiplier is purely imaginary, so
the Hermitian real-part defect vanishes identically. The relative arithmetic
cocycle `log(m/n)` has exactly this antisymmetry. Exact cyclic models at
orders three, four, and five verify the mechanism. The hostile `C_2` audit
shows that every real odd kernel there is trivial, so finite two-branch
quotients can erase the logarithmic direction. The decisive missing theorem
is a unitary operator-level identification of the Xi zero coordinate with
this source operator, including noncompact domains and discrete-spectrum
confinement. See `odd-source-skew-adjoint-vanishing-mechanism.md` and its
checker.

A universal finite-rank Newman Lyapunov theorem has survived. For real simple
zeros under backward heat, `r_i'=2sum_(j!=i)(r_i-r_j)^(-1)`, and the squared
Vandermonde discriminant obeys
`d_lambda log Delta=4sum_i[sum_(j!=i)(r_i-r_j)^(-1)]^2>=0`. Individual roots
and heat traces need not be monotone, but total logarithmic separation is.
This dynamically matches the Vandermonde mechanism behind static Li Toeplitz
positivity. The next Newman gate is a source-canonical renormalized infinite
discriminant compatible with Weyl density and collision detection. See
`newman-discriminant-lyapunov-theorem.md`.

Removing deterministic dilation yields a sharper Lyapunov object. The root
second moment satisfies `dR^2/dlambda=2N(N-1)`. For
`Delta_hat=Delta/(R^2)^(N(N-1)/2)`, one has
`d log Delta_hat=4sum_i[A_i-N(N-1)r_i/(2R^2)]^2>=0`. This is a centered
repulsion square; equality selects the scaled Hermite equilibrium. The
translation and dilation null modes are removed before any infinite Weyl
subtraction, making `Delta_hat` the preferred Newman renormalization seed.
See `newman-scale-normalized-discriminant.md`.

The conditional two-parameter differential bridge is now exact. A real
simple Newman zero obeys `gamma'=H_zz/H_z`, hence
`partial_lambda Theta_lambda(t)=-2t sum gamma gamma' exp(-t gamma^2)`.
There is no automatic sign: in the exact model
`(z^2-a^2)(z^2-b^2)`, the inner-zero velocity changes direction as the ratio
`b/a` crosses `sqrt(5)`. The velocity also blows up at a multiple-zero
collision. Newman compatibility must therefore use a collision discriminant,
Loewner order, or determinant convexity—not naïve heat-trace monotonicity.
See `xi-newman-zero-velocity-and-heat-flow.md`.

The spectral heat time must remain separate from the de Bruijn--Newman
parameter. `Theta(t)=Tr exp(-tH^2)` damps a fixed divisor, whereas the Newman
family obeys `partial_lambda H_lambda=-partial_z^2H_lambda` and moves its
zeros. Fixed-spectrum heat positivity does not imply a Newman-constant
statement. Compatibility requires a proved two-parameter measure flow
`Theta_lambda(t)`, after the fixed-divisor complete-Bernstein gate is crossed.
See `xi-spectral-heat-vs-newman-flow.md`.

All surviving lanes now integrate into one complete-Bernstein target. Define
`B(x)=log[xi(1/2+sqrt(x))/xi(1/2)]`. Under RH,
`B(x)=sum m_gamma log(1+x/gamma^2)` and
`B(x)=integral (1-exp(-xt))Theta(t)dt/t`. Thus `B` is the determinant
logarithm, `B'` the Stieltjes resolvent, and `Theta/t` its positive Lévy
density; Möbius transport yields Li moments and GNS/Cayley yields the
conditional operator. The central missing source object is a positive
Lévy--Khintchine density derived from arithmetic completion. See
`xi-complete-bernstein-equivalence.md`.

The first source Lévy components are now explicit. In the region
`s=1/2+sqrt(x)>1`, inverse Laplace transform sends each Euler-product term to
the negative log-Gaussian kernel
`-Lambda(n)exp(-(log n)^2/(4t))/(2sqrt(pi t n))`. The elementary endpoint
pair gives the positive kernel `exp(t/4)`. The prime sum converges for fixed
positive time but is pointwise nonpositive; completion positivity must be the
coupled inequality `K_endpoint+K_gamma>=-K_prime`. The gamma kernel and
large-time cancellation are the next derivation. See
`xi-prime-heat-kernel-and-coupling.md`.

The archimedean kernel is now explicit as well:
`K_gamma(t)=1/(4sqrt(pi t))[-EulerGamma-log(pi)+integral_0^infinity`
`(exp(-r)-exp(-r/4-r^2/(16t)))/(1-exp(-r))dr]`. Its integrand has removable
limit `-3/4` at zero. Together with `exp(t/4)` and the negative prime
log-Gaussian sum, this produces a concrete completed heat kernel. The
order-zero source target is its pointwise nonnegativity for every positive
time, with Fubini and analytic-continuation control. See
`xi-gamma-heat-kernel.md`.

An uncertified 70-digit reconciliation now validates the completed heat
normalization. Using von Mangoldt weights only through `200000`, the explicit
source kernel agrees with an independent 80-zero heat sum at six times from
`0.001` to `0.1`, with observed residuals between about `3e-18` and `3e-34`.
At `t=0.1`, order-one endpoint, gamma, and prime terms cancel to about
`2.1e-9`, demonstrating extreme conditioning. The data support the identity
but do not prove positivity or truncation error. See
`xi-completed-heat-kernel-reconciliation.md`.

The large-time mean-prime cancellation is exact. Replacing `dpsi(x)` by
`dx`, the log-Gaussian saddle lies at `log n=t` and gives
`K_prime^cont=-exp(t/4)(1+erf(sqrt(t)/2))/2`. Adding the endpoint leaves
`exp(t/4)erfc(sqrt(t)/2)/2~1/sqrt(pi t)`. Thus PNT main density explains the
exponential cancellation but not the true heat scale
`exp(-gamma_1^2t)`. Ordinary PNT remainder bounds are far too coarse for
all-time positivity; prime fluctuations must be reorganized through the
positive squared spectrum. See `xi-prime-heat-large-time-saddle.md`.

The source heat trace has a forced logarithmic Weyl scale. The leading
Riemann--von Mangoldt density gives
`Theta(t)~log(1/t)/(8sqrt(pi t))`
`-(EulerGamma/2+log(4pi))/(4sqrt(pi t))+...`. A candidate geometric operator
with a different heat scale is falsified. But a finite hostile quartet adds
only `2+O(t)`, leaving both leading terms unchanged. Weyl matching controls
density and normalization, not critical-line positivity. Both the Weyl law
and a positive squared spectral measure must arise from one source object.
See `xi-heat-weyl-law-and-limit.md`.

Finite-rank detection has unbounded latency. For an off-line zero
`rho=1/2+alpha+i beta`, the phase satisfies
`|u|^2=1-2alpha/|rho|^2`, while its reflected partner has inverse phase.
The exponential defect becomes order one only around
`k~|rho|^2/alpha`. A sufficiently high or near-line quartet can therefore
evade any prescribed finite number of Li or Toeplitz tests. Computation is a
falsifier within a sensitivity window, not a proof by extrapolation. See
`xi-offline-falsifier-latency.md`.

The strongest surviving all-order target is a Stieltjes function in the
squared centered coordinate. With `w=s-1/2` and
`S(x)=[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`, RH gives
`S(x)=sum m_gamma/(x+gamma^2)`. Conversely, the global Stieltjes pole locus
forces all zeros onto the line, while positive integer residues retain
divisor multiplicity. Its complete-monotonicity hierarchy is a real-axis
shadow. The hostile quartet is rejected because it contributes poles at
`a^2` and `conjugate(a)^2`, off the required negative axis. See
`xi-stieltjes-squared-spectral-equivalence.md`.

The Stieltjes and heat-flow gates are Laplace dual. Under the conditional
positive squared spectrum,
`S(x)=integral_0^infinity exp(-xt)Theta(t)dt` with
`Theta(t)=sum m_gamma exp(-gamma^2t)`. Its moments give the complete
monotonicity hierarchy. An off-line quartet contributes the oscillatory term
`2exp((alpha^2-beta^2)t)cos(2alpha beta t)`, failing positive heat behavior.
Li moments, the Stieltjes resolvent, the Cayley operator, and heat flow must
therefore be constructed as transforms of one source-positive measure, not
as independent explanations. See `xi-stieltjes-heat-trace-bridge.md`.

Reflection also fixes the boundary data of the positive-real target. Since
`L(1-s)=-L(s)` and `L(conjugate(s))=conjugate(L(s))`, one has
`Re L(1/2+it)=0` wherever xi is nonzero. Thus the Carathéodory condition is a
positive harmonic extension of forced zero boundary data; an off-line zero
is exactly an interior pole obstruction. This exposes the no-free-lunch
boundary: the machinery unifies every positivity and self-adjointness
condition, but the remaining arithmetic theorem is precisely pole-freeness
in the open right critical half-plane. See
`xi-log-derivative-boundary-skewness.md`.

An exact hostile deformation now falsifies any symmetry/boundary-only
explanation. In centered coordinate `w=s-1/2`, the factor
`Q_a(w)=(w^2-a^2)(w^2-conjugate(a)^2)` inserts an off-line quartet while
remaining even, real-structured, strictly positive on the critical boundary,
and boundary-skew in its logarithmic derivative. Finite products insert
arbitrarily many quartets with the same preserved properties. The missing
mechanism must therefore use arithmetic rigidity changed by `Q_a`, not merely
reflection or boundary sign. See `xi-offline-quartet-hostile-factor.md`.

The degree-two determinant has now been polarized across the canonical
endpoint, archimedean, and Abel-prime germs. Its three self-pieces are all
positive at approximately `0.5`, `1.513`, and `0.276`, but large mixed-sign
cross-terms leave a total near `9.71e-10`. The odd channel similarly cancels
`1-1.64507+0.64514` to about `7.41e-5`. These values are uncertified, while
the polarization identity is exact. The result rules out coarse sectorwise
dominance as a plausible proof strategy: completion coupling must be kept at
full precision or repackaged by a universal square identity. See
`li-degree-two-completion-coupling.md`.

The coefficient system now collapses to one analytic function. If
`C(z)=c_0+2sum_(k>=1)c_kz^k`, then the Li generating identity gives exactly
`C(z)=xi'/xi(1/(1-z))`. Positive definiteness of every Toeplitz rank is
equivalent to `Re C(z)>=0` in the disk, and the inverse Möbius map sends that
disk to `Re(s)>1/2`. Thus the scalar RH gate is the positive-real mapping
property `Re[xi'/xi(s)]>=0` throughout the open right critical half-plane.
This is an equivalence, not a proof. It redirects the source attack from
ill-conditioned coefficient estimates to a function-level Herglotz theorem.
See `li-caratheodory-half-plane-equivalence.md`.

The prime renormalization is canonically realized by an Abel germ. With
`F(epsilon)=-zeta'/zeta(1+epsilon)`, the basis-`k` prime sum is its normalized
`(k-1)`-st derivative and has the unique singular term `epsilon^(-k)`.
Therefore `J(epsilon)=epsilon^(-1)-F(epsilon)` is analytic, with
`J(0)=EulerGamma`, and packages every finite prime jet through one
degree-independent pole cancellation. Coupled with the endpoint and gamma
germs it reconstructs `xi'/xi` at one. Positivity and equivalence with a
sharp-cutoff finite part remain open. See `li-abel-renormalized-prime-germ.md`.

The rational cone now has a unique transport basis. Every degree-`d` test is
`R_p(s)=sum_(k=1)^(d+1) A_k(p)[s^(-k)+(1-s)^(-k)]`, and its pair-normalized
energy is `-sum_k A_k(p) ell_(k-1)` for the Taylor jets `ell_j` of `xi'/xi`
at zero. Reflection and decay prove uniqueness. The analytic prime transport
can therefore be derived once for these universal symmetric kernels rather
than separately at every rank. See
`li-symmetric-principal-part-transport-basis.md`.

The inverse Mellin basis is explicit. The kernel for
`s^(-k)+(1-s)^(-k)` is `(-log x)^(k-1)/(k-1)!` below one and
`x^(-1)(log x)^(k-1)/(k-1)!` above one. At prime powers this produces the
formal sum `sum Lambda(n)n^(-1)(log n)^(k-1)/(k-1)!`, which diverges with
leading cutoff growth `(log X)^k/k!` under the prime number theorem. Hence
prime transport necessarily requires a common contour-derived
prime/gamma/endpoint renormalization; the isolated prime term is neither
positive nor finite. See `li-mellin-prime-renormalization-gate.md`.

On the conditional critical-line model, the Toeplitz sequence is the moment
sequence of a finite measure. A zero pair with phase `u=1-1/rho` contributes
`|1-u|^2 Re(u^k)` to `c_k`, and `|1-u|^2=1/|rho|^2`. Thus discrete second
difference converts the infinite zero-counting measure into a finite
inverse-square-weighted phase measure of total mass `c_0=lambda_1`. The most
economical Gate C target is now a source-defined positive functional on
trigonometric polynomials with these moments. Its GNS construction would
generate the Hilbert increments and cocycle automatically. See
`li-increment-spectral-measure-target.md` and its exact identity checker.

The active attack is consequently the arithmetic Toeplitz functional
`E(p)=sum conjugate(a_i)a_j c_(|i-j|)`. Its coefficients are source-computable
from the completed zeta function, whereas its conditional zero-side form is
the positive inverse-square phase sum. The first constructive target is the
degree-two form from `lambda_1,lambda_2,lambda_3`, decomposed into endpoint,
archimedean, prime-power, and their required coupling terms. Any rule must
extend without degree-dependent fitting. See `li-arithmetic-toeplitz-attack.md`.

The degree-two form now has an exact reflection-channel theorem. Its odd
channel is
`A_2=(lambda_1+2lambda_2-lambda_3)/2`; the determinant of its remaining
coupled block is
`D_2=(lambda_1 lambda_3+2lambda_1 lambda_2-lambda_1^2-lambda_2^2)/2`, and
the full determinant is `A_2 D_2`. Uncertified 80-digit inputs give
`A_2 ~= 7.41e-5` and `D_2 ~= 9.71e-10`, revealing very small positivity
margins. See `li-degree-two-coupled-positivity.md` and its exact checker.

Both channels have also been reduced exactly to the first three Taylor jets
`a_j` of `log xi(1+t)`: `A_2=(2a_1-2a_2-3a_3)/2` and
`D_2=(2a_1^2+2a_1a_2+3a_1a_3-4a_2^2)/2`. Those jets use only Euler's
constant, `gamma_1`, `gamma_2`, `pi`, `zeta(3)`, and logarithms. This removes
unstable numerical differentiation from finite-rank certification, though it
does not yet explain positivity structurally.

The degree-two channels now have a universal geometric interpretation after
a positive moment measure is supplied:
`A_2=2 integral sin(theta)^2 dmu` and
`D_2=2 mu(T)^2 Var(cos(theta))`. Hence the coupled determinant is exactly a
Cauchy--Schwarz variance, with equality when the cosine of the phase is
constant almost everywhere. This explains the observed near-degeneracy but
does not construct the arithmetic measure. See
`li-degree-two-variance-theorem.md` and its exact checker.

The coupled positivity mechanism now extends uniformly to every rank. For a
finite positive circle measure, the `N`-th Toeplitz determinant is
`1/N!` times the `N`-fold integral of
`product_(i<j)|z_i-z_j|^2`. This Gram--Andreief/Vandermonde identity makes
positivity squared alternation of evaluation and strict positivity equivalent
to at least `N` support points. It is the first universal coupled positivity
theorem for the Li moment architecture. Applied to zero phases it remains
conditional; the arithmetic construction of the positive functional is
still the decisive gate. See `li-universal-vandermonde-positivity.md`.

The exact arithmetic test cone is now fixed by the Möbius coordinate
`u(s)=1-1/s`. Functional reflection satisfies `u(1-s)=u(s)^(-1)`, and the
coboundary weight is
`(1-u)(1-u^(-1))=1/[s(1-s)]`. Hence every circle polynomial square pulls
back to the reflection-invariant rational test
`R_p(s)=p(u(s))p(u(s)^(-1))/[s(1-s)]`. Gate C is precisely positivity of the
arithmetic explicit-formula functional on this one degree-independent cone.
See `li-mobius-weil-test-cone.md` and its exact checker.

This Möbius coordinate is rigid. Among nonconstant Möbius maps, the three
requirements “pole at `0`,” “value `1` at infinity,” and
“`u(1-s)=u(s)^(-1)`” uniquely force `u(s)=(s-1)/s`. The discarded algebraic
branch is the constant map `u=1`. Thus the critical circle, reflection center,
inverse-square weight, and rational-square cone cannot be tuned after seeing
the spectrum. See `li-mobius-coordinate-rigidity.md` and its exact checker.

If source positivity is achieved, the associated Hilbert--Pólya operator is
also fixed rather than guessed. GNS supplies a unitary `U`, and inverse
Möbius centering forces the Cayley transform
`H=(1+U)/[2i(1-U)]`. On a critical phase this recovers exactly the zero
ordinate `gamma`. This remains conditional on positivity, descent/domain
control, and identification of the GNS spectral measure with the zeta
divisor; the singular phase `U=1` must be controlled. See
`li-cayley-hilbert-polya-target.md`.

A scalar-GNS multiplicity obstruction is now explicit. At an atom, scalar
moments encode divisor multiplicity as mass, but the cyclic multiplication
operator has one-dimensional eigenspace regardless of that mass. One atom of
mass `m` and `m` identical copies have the same scalar moments but different
operator multiplicities. Thus scalar positivity may prove RH and yield a
cyclic spectral model without producing the completed-zeta divisor as an
operator spectrum with multiplicities. That stronger target needs an integer
mass/amplification theorem or a matrix/correspondence-valued source
functional. See `li-gns-multiplicity-obstruction.md`.

The Cayley domain has also been audited conditionally. Multiplication by the
real Cayley coordinate is self-adjoint on its maximal dense domain when phase
`1` carries no atom, even though phases accumulate there. But the GNS cyclic
vector is not in that domain: its squared-`H` summand is
`gamma^2/(gamma^2+1/4)`, which tends to one and diverges over an infinite
divisor. Compact resolvent additionally requires discrete measure
identification, finite amplified multiplicities, and escape of ordinates.
See `li-cayley-domain-audit.md`.

The rational-square cone has a prior endpoint-admissibility gate. For generic
degree `d`, `R_p(s)` has poles of order `d+1` at both `0` and `1`; it is not
an ordinary holomorphic Weil test. Before positivity is meaningful, the
explicit-formula functional must receive one reflection-symmetric,
degree-compatible finite-part extension that agrees with the Li derivative
definition and respects polarization. Rank-dependent endpoint counterterms
are disallowed because they could manufacture positivity. See
`li-rational-cone-endpoint-regularization-gate.md`.

The local endpoint extension is now canonical. With `L=xi'/xi`, define the
full-divisor functional `D(R)=-Res_0(RL)-Res_1(RL)`. Completed xi is nonzero at both endpoints, so
`L` is holomorphic there; reflection gives `L(1-s)=-L(s)` and makes the two
residues equal. The pair-normalized Li energy is
`E(p)=D(R_p)/2=-Res_0(R_pL)`. A degree-`d` polynomial samples exactly jets `0` through `d`
of `L` under one common residue rule. This removes counterterm freedom.
Global contour decay/convergence and positivity remain separate gates. See
`li-canonical-endpoint-residue-functional.md`.

The global contour reduction is also fixed. Every rational square has
degree-independent decay
`R_p(s)=-p(1)^2/s^2+O_p(s^(-3))`. With the classical
`N(T)=O(T log T)` estimate, its divisor sum converges absolutely with tail
`O_p(log(T)/T)`. Standard zero-avoiding bounds for `xi'/xi` then close the
argument-principle contour and identify the canonical endpoint residues with
the global divisor evaluation. Those classical analytic estimates must be
cited or reproduced in a publication proof. See `li-global-contour-closure.md`.

Arithmetic splitting has a transport gate. In `xi'/xi`, the pairs
`1/s+psi(s/2)/2` at zero and
`1/(s-1)+zeta'/zeta(s)` at one cancel their singularities. The prime
Dirichlet series for `-zeta'/zeta` is not valid at either endpoint. Therefore
the completed residue must first be transported to a line `Re(s)>1`, with
every crossed endpoint and gamma term retained, before introducing the von
Mangoldt expansion. See `li-prime-transport-gate.md` and its cancellation
checker.

The finite Newman flow now has a canonical scale-free entropy reference.
For `N` real simple roots, normalize the discriminant by the quadratic
radius. The unique equality configurations are affine copies of the roots
of the probabilists' Hermite polynomial, for which
`R_H^2=N(N-1)` and `Delta_H=product_(k=1)^N k^k`. Hence
`E_N=log(widehatDelta_H/widehatDelta)` is nonnegative and
its derivative is minus four times the squared centered-repulsion defect.
This is a universal finite-rank theorem; applying it to growing Xi windows
still requires a canonical truncation and a controlled infinite-rank limit.
See `newman-hermite-relative-entropy.md` and its exact checker.

Finite Xi windows introduce an exact exterior-flux obstruction. If the
window roots satisfy `r_i'=2A_i+b_i`, then the normalized discriminant
production is `4 sum q_i^2 + 2 sum b_i q_i`, where
`q_i=A_i-[N(N-1)/(2R^2)]r_i`. The exterior term has unrestricted sign; an
exact hostile example reverses the closed-system Lyapunov direction. Thus
the next real gate is a canonical global renormalization or a lower bound on
this scalar flux, not another finite-window positivity check. See
`newman-window-entropy-flux.md` and its exact checker.

Reflection symmetry removes the leading part of that obstruction. An
omitted pair `+-y` exerts `4r/(r^2-y^2)`, whose leading tail is the radial
force `-4r/y^2`. The scale-normalized defect is orthogonal to the radius
vector, so this entire inverse-square term contributes zero entropy flux.
The first surviving term is cubic in the window root and fourth order in
the exterior ordinate. This makes a smooth-window or boundary-layer limit
substantially more plausible, while leaving the adjacent-root boundary
layer open. See `newman-symmetric-window-flux-cancellation.md` and its exact
checker.

The arithmetic squarefree-cube model has now been corrected at source level.
Because the logarithmic derivative has prime-power support, all mixed
squarefree von Mangoldt edges vanish. A cube retaining only its identity and
single-prime edges has Walsh spectrum
`1+sum_j (-1)^(eta_j)r_j`, hence is positive exactly when
`sum_j |r_j|<=1`. Individual prime contractions therefore share one global
budget and cannot be tensored independently. Raw `log(p)/sqrt(p)` edges are
not `l1`, so any successful completed construction must derive compensating
diagonal or mixed Schur energy from the gamma/endpoint source rather than
inventing squarefree arithmetic atoms. See
`von-mangoldt-support-falsifies-arithmetic-tensor-interchange.md` and
`additive-prime-edge-budget-theorem.md`.

The corresponding finite completion problem is solved exactly. Given
diagonal energy `D` and single-prime correlations `r_j`, some
translation-invariant positive completion exists iff every `|r_j|<=D`.
The canonical product completion has mixed coefficient
`D product_(j in S)(r_j/D)` and nonnegative product Walsh spectrum. Hence the
source problem is now localized to the gap between the sparse `l1` condition
and the completed `l-infinity` condition: the archimedean/endpoint or
mapping-cone sector must supply the mixed correlations, without rebranding
them as forbidden von Mangoldt atoms. See
`squarefree-positive-completion-theorem.md`.

A source-shaped sufficient mechanism is now explicit. If all prime features
are contractions depending on one positive latent log-time variable, then
their subset correlations are moments of products and every Walsh eigenvalue
is an integral of nonnegative factors. Taking `x_p(u)=p^(-u)` matches the
Laplace variable in the gamma-resolvent bridge and supplies mixed continuous
correlations without asserting `Lambda(pq)>0`. The unresolved step is exactly
the singular `u=0` finite part plus the negative prime-power coupling: these
must descend together as a Schur compression of a positive dilation. See
`latent-log-time-squarefree-completion-theorem.md`.

The gamma endpoint divergence can be removed canonically on a defect sector.
Although its log-time density has infinite mass at zero, the vectors
`v_n(u)=1-n^(-u)` are square-integrable. Their Gram pairing is finite,
positive, and polarizes to a mixed `(pq)^(-u)` term without creating a
von Mangoldt atom at `pq`. The remaining obstruction is therefore the norm
of the negatively signed prime evaluation map relative to this centered
gamma Hilbert space, not positivity of the gamma block itself. See
`endpoint-centered-gamma-defect-gram-theorem.md`.

The first naive prime coupling has been falsified. Subtracting independent
diagonal costs `(log p)/sqrt(p)` from the centered gamma Gram passes each
one-prime test but already makes the `{2,3}` determinant strictly negative.
The gamma prime-vectors are too correlated for orthogonal penalties. The
prime contribution must retain its off-diagonal translation/incidence map
inside a common Schur complement. See
`orthogonal-prime-penalty-two-prime-no-go.md`.

The corrected arithmetic operator is a paired translation adjacency:
`A=sum w_(p^k)(S_(k log p)+S_(k log p)^*)`. It is self-adjoint but
sign-indefinite, with Fourier symbol `2 sum w_(p^k)cos(t k log p)`. On a
squarefree first-power cube its Walsh norm is exactly the `l1` sum of visible
edge weights, recovering the additive budget from the source operator.
Prime powers are harmonics of one prime phase, as required by Adams maps, not
independent coordinates. The next gate must compare this adjacency with the
archimedean operator in their common translation representation. See
`prime-power-translation-adjacency-theorem.md`.

Each full prime-power ray now has an exact Euler resummation. Its positive
zero-phase extremum is `2 log(p)p^(-1/2)/(1-p^(-1/2))`, while its negative
phase extremum has denominator `1+p^(-1/2)`; higher Adams harmonics therefore
break the squarefree sign symmetry. Globally all rays reinforce at zero
phase, and the raw adjacency norm diverges with cutoff. Hence gamma and prime
symbols cannot be compared as separate bounded multipliers: only the
completed quadratic form with common smoothing and endpoint convention is
well typed. See
`euler-ray-adjacency-resummation-and-zero-phase-divergence.md`.

Gaussian smoothing reconciles the adjacency and heat-kernel lanes exactly.
The smoothed prime adjacency is bounded, its norm is attained at the trivial
translation character, and the negative prime heat kernel is that
zero-character value times the universal inverse-Laplace factor. Completed
heat positivity therefore controls a scalar character, not automatically the
full translation operator. The scalar Stieltjes route and the stronger
all-character operator route are now explicitly separated. See
`gaussian-smoothed-prime-adjacency-zero-character-theorem.md`.

The full completed character kernel is now identified: Gaussian smoothing of
the centered Weil distribution and Fourier transformation gives, under RH,
`Theta(t,xi)=sum_gamma m_gamma exp(-t(xi-gamma)^2)`. The known spectral heat
trace is its `xi=0` slice, while the source prime term becomes the damped
cosine adjacency at arbitrary `xi`. Positivity for every `(t,xi)`, with the
Gaussian limit justified on the Weil test space, is equivalent to Weil
positivity rather than stronger than RH. The immediate source target is to
derive the matching nonzero-character endpoint and gamma formulas. See
`two-variable-weil-gaussian-kernel-equivalence.md`.

The complete shifted-Gaussian source formula is now explicit. The endpoint
becomes `e^(t/4-t xi^2)cos(t xi)`; the gamma term is a shifted Gaussian
average of `Re psi(1/4+iu/2)` plus its pi constant; and the prime term is the
damped cosine sum. A factor-of-two audit fixes the spectral side as one half
of the signed zero mixture, so the zero slice counts positive ordinates once.
This is the first fully stated all-character source inequality. See
`explicit-two-variable-weil-heat-source-formula.md`.

In variance `sigma=1/(4t)`, the character kernel is ordinary Gaussian
convolution of the Weil spectral distribution and obeys the forward heat
semigroup. Positivity at one variance propagates to all broader smoothings,
but not toward the sharp spectral limit. A three-atom signed model has the
exact threshold `sigma=1/(4 log 2)`, proving that broad positivity can hide a
negative atom. This suggests a Weil smoothing threshold whose vanishing is
RH-equivalent, while remaining distinct from Newman flow. See
`weil-gaussian-positivity-semigroup-and-threshold.md`.

A finite positive smoothing threshold, if attained at a finite character,
must occur through a double contact: `Theta=partial_xi Theta=0`, with
nonnegative curvature equal to the forward variance derivative. Strict
Gaussian convolution makes the kernel positive everywhere above the
threshold. Thus, after proving a broad positive regime and excluding escape
in `xi`, the RH gate reduces to ruling out finite simultaneous zeros of the
explicit source kernel and its character derivative. See
`weil-gaussian-first-contact-rigidity.md`.

Character escape is now excluded at every fixed positive smoothing scale.
The shifted gamma average grows as
`log(|xi|/(2pi))/(4sqrt(pi t))`, while the endpoint decays and the smoothed
prime cosine series is uniformly bounded. Hence the completed kernel is
coercive in `xi` and attains its global minimum at finite character. A finite
threshold must therefore create the double contact predicted above. See
`weil-gaussian-character-coercivity-theorem.md`.

The broad-smoothing regime is unconditionally positive uniformly in
character. After rescaling, the gamma term has leading growth
`log(1/t)/(8sqrt(pi t))`; the translated logarithmic Gaussian has a finite
global minimum, the endpoint is bounded, and the first prime displacement is
exponentially suppressed. Combined with semigroup monotonicity and
coercivity, this reduces the remaining RH-equivalent obstruction to a finite
double contact of the explicit source kernel. See
`broad-smoothing-uniform-weil-positivity-theorem.md`.

The spectral anatomy of a failed threshold is explicit. A zero quartet at
horizontal displacement `alpha` contributes an amplified oscillatory
Gaussian with a strictly negative lobe at every smoothing scale. Its first
lobe becomes unsuppressed around `t alpha^2=pi/2`, giving an inverse-time
latency primarily of order `alpha^(-2)`, distinct from Li-rank latency.
Against the broad-positive completed background this defect must emerge
through the finite double contact above. See
`offline-quartet-gaussian-negative-lobe-and-latency.md`.

Nonzero double contacts now face a source-only moment obstruction. Positivity
of the Gaussian-damped von Mangoldt coefficients forces their cosine value
`R` and sine derivative moment `I_1` into
`R^2/M_0^2+I_1^2/(M_0M_2)<=1`. At contact these are fixed by the
archimedean value and slope, yielding an explicit exclusion inequality using
only `A`, `partial_xi A`, `M_0`, and `M_2`. The zero character saturates this
ellipse and remains the scalar hard case. See
`prime-moment-ellipse-double-contact-obstruction.md`.

The contact filter now includes curvature. A weighted covariance inequality
traps the second prime cosine moment `R_2` using `M_0,M_2,M_4` and the contact
value `R`; first-contact heat curvature supplies a lower requirement on that
same `R_2`. Candidate contacts must pass value, slope, and curvature moment
constraints simultaneously.

These scalar bounds extend to an all-order block Hankel hierarchy. Ordinary
prime moments `H_r` and phase-twisted moments `Z_r` form the Gram block
`[[H_r,Z_r^*],[Z_r,H_r]]>=0`, equivalently a moment-metric contraction.
Contact jets prescribe successive real and imaginary entries, so failed
semidefinite completion excludes a candidate region. Finite passage remains
necessary rather than sufficient and must not erase fixed prime support. See
`prime-phase-block-hankel-contact-hierarchy.md`.

The prime hierarchy evolves canonically in Gaussian variance. Its twisted
zero moment solves the heat equation, all even moments are alternating
variance derivatives of `M_0`, and the effective squared log displacement
`M_2/M_0` dissipates at exactly minus the variance of `(log n)^2`. Hankel
blocks decrease in Loewner order under broader smoothing. This supplies a
single monotone arithmetic load for continuation from the unconditional
positive regime. See `prime-heat-moment-flow-and-variance-dissipation.md`.

The integrated negative part of the completed character kernel is a finite,
monotone defect entropy under forward Gaussian smoothing. A generic first
contact creates negative mass on the sharper side with universal law
`N~(8sqrt(2)/3)kappa(sigma_*-sigma)^(3/2)`. This gives a stable
falsification observable and a local signature for contact multiplicity. See
`weil-negative-mass-entropy-and-contact-onset.md`.

Higher-order contacts have now been classified. If the first spatial jet has
order `2m`, backward heat produces the scaled physicists' Hermite polynomial
`delta^m H_(2m)(x/(2sqrt(delta)))`, and negative mass begins with exponent
`m+1/2`. The observed defect-entropy slope therefore determines contact
multiplicity and signals how many moment-jet constraints must vanish. This is
a shared heat normal form, not an identification with Newman time. See
`higher-contact-hermite-negative-mass-law.md`.

A scalar-lane implication has been corrected. Pointwise positivity of
`Theta(t)` makes `B` Bernstein but does not make `B` complete Bernstein or
`B'` Stieltjes. The missing condition is complete monotonicity
`(-1)^k partial_t^k Theta>=0` for every `k`. The explicit positive kernel
`e^(-t)(1+epsilon cos(bt))` has off-axis Laplace poles and falsifies the
weaker claim. Full all-character Gaussian positivity remains RH-equivalent
through the approximate-identity recovery of the Weil distribution. See
`scalar-heat-positivity-is-not-stieltjes-no-go.md`.

The corrected scalar gate is now source-explicit at every derivative order.
Differentiating a prime log-Gaussian produces
`t^(-k-1/2)e^(-y)k!L_k^(-1/2)(y)`, while the endpoint alternates and the gamma
integral differentiates under the same common convention. Thus Stieltjes
positivity is an all-order completed Laguerre hierarchy; order zero is only
its first necessary inequality. See
`scalar-heat-complete-monotonicity-laguerre-hierarchy.md`.

Derivative signs still omit common-measure correlations. Under a positive
squared spectrum, the alternating heat derivatives form ordinary and shifted
Stieltjes Hankel matrices. The first determinant is normalized spectral
variance and forces log-convexity of `Theta`; all entries can be positive while
this determinant is negative. Substitution of the completed Laguerre source
formula gives a stronger nested falsifier hierarchy. See
`scalar-heat-stieltjes-hankel-variance-hierarchy.md`.

The scalar continuum can be reduced to one heat time. If the complete
ordinary/shifted Hankel hierarchy holds for
`D_k=(-1)^kTheta^(k)(t_0)` and its exponential moment series converges for
every radius below `t_0`, the Stieltjes moment theorem and analytic
continuation reconstruct one positive squared-spectral measure for all
`t>0`. Thus the corrected source target is an all-order Gram construction at
one convenient `t_0`, plus growth control. See
`one-time-stieltjes-moment-reconstruction-theorem.md`.

For the completed Xi kernel, the growth clause follows from its natural
holomorphy on `Re(t)>0`: the Taylor disk at `t_0` has radius `t_0`, and Hankel
positivity makes its alternating coefficients nonnegative. Subject to the
standard source interchange proof, the entire scalar RH target is therefore
the ordinary and shifted Hankel hierarchy at one chosen heat time.

The one-time hierarchy retains off-axis sensitivity through derivative
amplification. A complex heat rate of modulus `R` contributes a factor `R^k`
at order `k`; if it exceeds the background rate, its oscillatory phase forces
a negative derivative after the explicit logarithmic latency. On the source
side, order `k` samples Laguerre turning scales
`n=exp[O(sqrt(k t_0))]`, so no fixed small `t_0` makes all orders uniformly
prime-free. See `one-time-derivative-off-axis-amplification-latency.md`.

If the one-time hierarchy is proved, it canonically constructs the squared
Hilbert--Polya operator. The moments define a polynomial Hilbert space;
multiplication by the squared coordinate closes to a positive self-adjoint
Jacobi operator, and untwisting plus Xi meromorphy identifies its support with
squared ordinates. Doubling `+/-sqrt(J)` gives signed support. Scalar atom
weights still do not create eigenspace multiplicity, so the simplicity/jet
obstruction remains. See
`one-time-hankel-jacobi-hilbert-polya-construction.md`.

The all-order scalar hierarchy is equivalently local reflection positivity of
two time-addition kernels:
`K(s,u)=Theta(t_0+s+u)` and
`K^+(s,u)=-Theta'(t_0+s+u)`. A coherent factorization
`K=<e^(-sA)v,e^(-uA)v>` with `A>=0` proves every ordinary and shifted Hankel
minor at once and directly supplies the Jacobi generator. This is now the
cleanest source-derived coupled positivity target. See
`time-addition-reflection-positivity-stieltjes-theorem.md`.

The endpoint explains why both reflection-positive kernels are required.
`e^(t/4)` is an ordinary rank-one positive kernel but represents the forbidden
spectral atom `lambda=-1/4`; its generator-shifted kernel is negative. Thus
ordinary positivity reconstructs only a bilateral Laplace measure, while the
shifted kernel enforces nonnegative support. Completion must cancel the
endpoint's negative generator direction through coupled gamma--prime terms.
See `endpoint-negative-energy-atom-shifted-kernel-gate.md`.

The forbidden endpoint direction has a canonical acyclic partner. In squared
coordinate, `1/(x-1/4)` from the elementary factors and the principal pole of
`zeta'/zeta` have opposite residues and cancel before positivity. They form a
source-derived two-term mapping cone associated with `(s-1)zeta(s)`; only its
regular finite part survives. The reflected `s->0` chart pairs `1/s` with the
gamma pole, giving the second presentation of the same squared-coordinate
cancellation. Reflection positivity must be imposed after
this reduction. This remains algebraic/analytic and does not assert the
unavailable physical relative-chain pushforward. See
`endpoint-zeta-pole-acyclic-mapping-cone.md`.

The reduced pole pair leaves the exact finite coupling
`S(1/4)=1+EulerGamma/2-log(2sqrt(pi))`, approximately `0.0230957`. It is
unconditionally positive but results from tight cancellation of elementary,
zeta, gamma, and pi constants. This fixes a no-counterterm normalization that
every reduced operator must reproduce; its positive zero-sum interpretation
remains conditional on Stieltjes positivity. See
`reduced-endpoint-finite-coupling-constant.md`.

The canonical quarter point yields a more compact scalar equivalence. The
jets `A_k=(-1)^kS^(k)(1/4)/k!` are moments of
`u=1/(1/4+lambda)` on `[0,4]` exactly under RH. Conversely, positivity of the
ordinary, `u`-shifted, and `(4-u)`-localizing Hankel families reconstructs a
unique compact measure and hence the global Stieltjes resolvent. This removes
the separate growth/determinacy clause and makes the reduced endpoint jet the
new preferred scalar target. See
`quarter-point-hausdorff-moment-rh-equivalence.md`.

The first nontrivial quarter-point jets are now explicit in
`gamma_0,gamma_1,gamma_2,pi,zeta(3)`. Numerically
`A_1~3.71e-5`, `A_2~1.44e-7`, and
`A_0A_2-A_1^2~1.94e-9`, all positive without using zero locations. The tiny
coupled margin confirms severe completed cancellation. Exact formulas are
proved; the decimal signs are not yet interval-certified. See
`quarter-point-first-hausdorff-jets.md`.

Adding the fourth jet closes the first nontrivial lower- and upper-endpoint
Hausdorff localizers. Both numerical determinants are positive, but the lower
one is only about `3.84e-15`; it is the sharpest early source-side falsifier
found in this lane and now demands interval certification. See
`quarter-point-first-localizer-determinants.md`.

Exact-rational interval propagation shows that independent `10^-12` boxes
around the four printed source coefficients already force both first
localizer determinants positive. The remaining certification problem has
therefore been isolated to rigorous analytic enclosures for those four
coefficients, rather than unstable matrix arithmetic.

The remaining certification can avoid Laurent-pole numerics: the identity
`eta(s)=(1-2^(1-s))zeta(s)` triangularly reconstructs the first four
Stieltjes constants from the regular jet `eta(1),...,eta^(4)(1)` and `log 2`.
A directed-rounding monotone-tail enclosure of that eta jet would close the
first localizer certificate entirely on the source side. See
`eta-jet-certification-reduction.md`.

Naive eta certification is computationally falsified: the elementary
fourth-derivative alternating remainder needs about `3.31e18` terms at
`10^-12`. The certifier must use a rigorously accelerated tail. See
`eta-naive-tail-certification-no-go.md`.

The replacement tail is now finite and rigorous: starting at `N=10000`, 60
Euler transforms have exact-rational remainder bounds below `10^-100` for all
eta derivatives through order four. Only directed-rounding evaluation of the
finite logarithmic prefix remains. See `eta-euler-tail-certification-theorem.md`.

The finite transcendental step is now enclosed at 80 decimal digits using
correctly rounded logarithms and outward arithmetic. All five eta-jet boxes
have width below `2.5e-75`, including the proved Euler remainder and no zero
data. See `eta-jet-directed-rounding-certificate.md`.

Composing those boxes through the eta--Stieltjes triangle, exact-rational
Machin and Apery enclosures, the completed source jets, and the moment maps
now certifies both first localizer determinants strictly positive. This is the
first unconditional complete finite Hausdorff corner in the program. It uses
no zero locations and does not prove RH. See
`quarter-point-first-localizer-interval-certificate.md`.

The certification architecture scales to the order-two corner without a
larger prefix. Exact sign polynomials show that eta derivatives through order
six at `N=10000` need only 15 Euler transforms, with all remainders below
`1.15e-52`. The next task is generic interval series composition for
`A_4,A_5`. See `eta-order-six-tail-extension.md`.

The corresponding directed-rounding evaluation now encloses the full eta jet
through order six in boxes narrower than `5e-52`. Thus every regular analytic
input for the order-two corner is certified; only generic formal interval
composition remains. See `eta-order-six-directed-rounding-certificate.md`.

That generic composition now certifies `A_4,A_5` and all three order-two
Hausdorff determinants positive. The ordinary, lower, and upper determinants
are respectively about `2.15e-22`, `3.08e-31`, and `1.38e-20`. The mandatory
`(2s-1)^(-1)` normalization is guarded by the known `A_1>0` regression. This
is the second unconditional finite corner, not RH. See
`quarter-point-order-two-interval-certificate.md`.

The order-three corner meets the first prefix threshold. Eta derivatives
through order eight cannot use the previous `log N>9` sign proof, but
`N=100000` gives exact positivity with only eight Euler transforms and tail
bounds below `4e-36`. The architecture survives with a tenfold finite-prefix
cost. See `eta-order-eight-tail-scaling.md`.

A one-pass directed evaluator now certifies eta derivatives through order
eight in intervals narrower than `9e-36`, reusing each prefix logarithm across
all derivative orders. Thus the regular input for `A_6,A_7` is complete. See
`eta-order-eight-directed-rounding-certificate.md`.

Degree-seven interval composition now certifies all three `4x4` Hausdorff
determinants positive. Their scales are approximately `1.16e-41`, `9.08e-54`,
and `2.97e-39`. The lower determinant's relative interval width has grown to
about `4.1e-5`, marking the first real precision-pressure signal while still
excluding zero. See `quarter-point-order-three-interval-certificate.md`.

The three ordinary corners now yield a certified finite Jacobi segment via
`b_n=Delta_n Delta_(n-2)/Delta_(n-1)^2`. The first three off-diagonal squares
are about `3.64e-6`, `1.32e-6`, and `4.86e-7`; these are source-derived
nonbreakdown coefficients and better-conditioned observables than the tiny raw
determinants. Their infinite-operator interpretation remains conditional. See
`quarter-point-jacobi-coefficient-segment.md`.

Interval Lanczos now supplies the Jacobi diagonal through `a_3`, approximately
`0.0016064,0.0034962,0.0017975,0.0012167`. Together with the certified `b_n`,
this is a source-derived symmetric `4x4` compression. Norm-ratio identities
cross-check the determinant coefficients, while the localizers encode its
finite quadratic-form bounds `0<=J<=4`. See
`quarter-point-finite-jacobi-compression.md`.

Blind numerical diagonalization of that compression predicts transformed
ordinates `14.13510,21.54984,33.63891,110.22215`. Only afterward, comparison
shows the first lies about `3.7e-4` above the standard first ordinate, despite
no zero location entering construction. Later nodes expose finite-rank tail
compression rather than consecutive zeros. Extremal-node convergence is now
a concrete operator-program test. See `quarter-point-jacobi-blind-spectrum.md`.

Nested Ritz theory fixes the direction of that test: largest `u` nodes
increase with compression order, hence transformed first-ordinate estimates
decrease from above. Sizes one through four give
`24.9452,14.6084,14.1520,14.1351`. Limit identification remains conditional.
See `quarter-point-extremal-ritz-convergence-theorem.md`.

The `5x5` corner moves the eta prefix threshold to `N=500000`. Exact sign
polynomials and ten Euler transforms bound every derivative tail through order
ten below `6e-50`. The method survives, while prefix growth now motivates
reusable certified log tables. See `eta-order-ten-tail-scaling.md`.

The one-pass 90-digit evaluation now certifies eta derivatives through order
ten with maximum interval width `1.2e-49`. The half-million-term prefix
completes in about 43 seconds, leaving degree-nine composition as the remaining
input to the `5x5` corner. See `eta-order-ten-directed-rounding-certificate.md`.

Degree-nine composition now certifies all three `5x5` determinants positive,
at scales `1.92e-67`, `7.68e-83`, and `1.96e-64`. The lower relative enclosure
improves to about `1.5e-6`, showing that adaptive tail precision controls the
conditioning pressure. See `quarter-point-order-four-interval-certificate.md`.

The fifth Jacobi compression gives blind edge estimate `14.1347310037`, only
about `5.9e-6` above the standard first ordinate and roughly 64 times more
accurate than size four. Its `b_4~3.07e-7` is interval-positive; no zero enters
construction. See `quarter-point-fifth-ritz-edge.md`.

Interval Sturm inertia upgrades that edge to a certified finite-matrix
eigenvalue: `gamma_hat in [14.1347310022873,14.1347310051871]`. Its `2.9e-9`
width is far below the finite-rank discrepancy. See
`quarter-point-fifth-ritz-interval-certificate.md`.

The fifth Gaussian quadrature weight also gives a blind top-atom multiplicity
estimate `w_max/u_max~1.00001069`. This strongly predicts residue one without
zero or multiplicity input, but remains a numerical mass estimate rather than
an eigenspace-dimension proof. See `quarter-point-blind-multiplicity-estimate.md`.

Christoffel interval evaluation certifies the estimator in
`[1.0000106856271,1.0000106950984]`. Its excess above one is finite-tail
contamination; convergence to one remains a test, not a simplicity proof. See
`quarter-point-multiplicity-interval-certificate.md`.

The finite operator now has an equivalent analytic explanation: its resolvent
is the `[n-1/n]` Stieltjes--Pade approximant to the quarter-point source jet,
and Jacobi nodes are reciprocal negative Pade poles. At size five the Gaussian
measure reproduces all ten input moments. Positivity turns pole extraction into
nested real Ritz convergence. See `quarter-point-pade-jacobi-explanation.md`.

The certified leading minors through size five satisfy the degree-nine
truncated Hausdorff theorem. Hence a positive measure on `[0,4]` unconditionally
represents `A_0,...,A_9`; the five-node quadrature is one atomic realization.
It is finite and nonunique, not the full RH measure. See
`quarter-point-degree-nine-truncated-measure-theorem.md`.

The Sommerfeld attack now targets a decaying compact Jacobi recurrence, not
more determinants for their own sake. A nonzero constant tail is incompatible
with the required pure-point spectrum accumulating at zero. The desired WKB
law is the compact-coordinate transform of Riemann--von Mangoldt, with the
gamma factor as smooth action and primes as phase defect. See
`sommerfeld-compact-jacobi-quantization-program.md`.

The raw Euler prime phase cannot yet serve as the WKB boundary condition: its
series is source-defined only for `sigma>1`, not on the critical line. A
canonical regularized Abel boundary must agree with the Jacobi Weyl function;
otherwise the quantization rule smuggles in `arg zeta`. See
`sommerfeld-prime-phase-abel-boundary-obstruction.md`.

The finite Jacobi denominator supplies a canonical phase bypass:
`arg det(I+hJ_n)` jumps by `pi` at each real Pade pole. Prime data enter through
regular source moments, avoiding the divergent raw critical-line Euler phase.
Infinite Weyl-function convergence is the remaining gate. See
`sommerfeld-jacobi-pade-phase-bypass.md`.

Compatible positive Jacobi extensions have monotone bounded positive-axis
resolvents by Schur-complement order. Thus the infinite Weyl limit exists
pointwise on `h>0` if all corners continue; analytic identification and the
negative-axis boundary remain. See
`jacobi-positive-axis-monotone-resolvent-theorem.md`.

Compact support closes the conditional convergence argument: subsequential
Gaussian limits share all moments, and Hausdorff determinacy makes the limit
unique. Weyl functions converge locally uniformly off the cut and identify
with the source by their jet. See
`jacobi-gaussian-measure-to-weyl-limit-theorem.md`.

Hausdorff's theorem linearizes the all-order target. For
`m_k=A_k/4^k`, RH is equivalently the nonnegativity of every binomial finite
difference `(-1)^j Delta^j m_k`, subject to the completed-source analytic
identification. All 55 boxes through total degree nine are certified positive.
The next universal proof target is a positive source representation of these
linear combinations. See `quarter-point-linear-hausdorff-rh-equivalence.md`.

The hierarchy is encoded by one bivariate generator, a fractional combination
of `S((1-z)/4)` and `S(1/(4(1-w)))`. Proving coefficientwise positivity of
this completed-source function is now the universal Gram target. See
`hausdorff-bivariate-source-generator-theorem.md`.

The generator collapses to a Loewner kernel:
`G(z,w)=y(F(y)-F(x))/(y-x)` for `F(t)=(4t-1)S(t)`. Under nonnegative squared
spectrum it has an explicit positive rank-one Gram decomposition. Proving this
kernel positive directly from the reduced gamma--prime source would establish
all positivity families and reconstruct self-adjointness at once. See
`loewner-kernel-universal-coupled-positivity-theorem.md`.

Loewner positivity is equivalently a Pick condition for `F`. In `s` coordinates
the elementary poles cancel exactly to `4`, leaving one coupled gamma--prime
imaginary-part inequality. Neither sector has a sign alone. See
`reduced-gamma-prime-pick-target.md`.

A zero-free eta/digamma hostile scan finds no Pick violation on 117 broad
upper-half-plane samples; the minimum is positive but small near the positive
real boundary. Interval adaptive scanning is next. See
`reduced-source-pick-first-hostile-scan.md`.

The diagonal boundary condition `F'(x)>=0` also survives a zero-free scan over
57 points from `10^-3` to `10^4`. This is weaker than coupled Loewner
positivity; `2x2` divided-difference determinants are next. See
`reduced-source-pick-boundary-slope-scan.md`.

The first coupled `2x2` Loewner scan stays robustly positive for point ratios
at least 100, but nearby pairs hit `10^-12` cancellation and cannot be resolved
by the current complex evaluator. A shared interval kernel evaluation is now
required. See `reduced-source-loewner-two-point-conditioning.md`.

The near-diagonal gate is nevertheless settled at the canonical quarter point:
`D(c,c+delta)/delta^2 -> 16(A_0 A_2-A_1^2)>0`, with strict positivity inherited
from the certified first Hankel determinant. Thus local coupled Loewner contact
and moment positivity are literally the same obstruction there. Global
two-point positivity remains open. See
`quarter-point-loewner-diagonal-curvature.md`.

Attempting to extend that curvature test across `10^-2<=x<=10^2` exposes a
hard numerical limit: baseline signs are positive, but step/depth controls
change sign and fail the certified quarter-point regression by about 86
percent. Third finite differences of the double-precision eta source are
therefore inadmissible. The next viable attack is interval automatic
differentiation or a direct covariance kernel. See
`reduced-source-loewner-diagonal-curvature-conditioning.md`.

The unstable third-derivative target has an exact geometric form. For
`g=F'>0`, diagonal curvature is nonnegative exactly when `g^(-1/2)` is
concave. Under the desired spectral representation it equals
`M_2 M_4-M_3^2`, a pairwise square covariance. Complete monotonicity alone
does not imply it: `g=exp(-x)` fails. This sharply separates the genuinely
coupled Stieltjes-order-two requirement from easy scalar sign alternation. See
`loewner-curvature-reciprocal-concavity-theorem.md`.

The reciprocal-square-root formulation yields a stable derivative-light
falsifier. Across 36 arithmetic-midpoint chords with endpoints from `0.01` to
`100`, two independent height/depth runs give positive concavity gaps; the
smallest controlled margin remains about `1.71e-9` after subtracting the
largest run discrepancy. This is finite numerical evidence, not an interval
proof, but it survives the control that defeated direct third differentiation.
See `reduced-source-reciprocal-slope-concavity-scan.md`.

A fourteen-decade extension localizes the remaining numerical danger. All
tail chords with left endpoint at least one are strongly positive and agree
between controls to about `8e-15`. Tiny raw negatives occur only near `x=0`
and are smaller than the baseline/control discrepancy; none is robust. The
next proof-quality target is therefore a central-coordinate interval expansion
at the `t=0` boundary, not a broader floating scan. See
`reduced-source-reciprocal-slope-broad-boundary-scan.md`.

The central boundary has now survived a high-precision attack. A coupled
70--80 digit evaluator tests 21 chords from `10^-8` to `10^-2`; every gap is
positive, with the corrected smallest exploratory margin about `3.65e-20` and the largest
precision/depth/step discrepancy about `1.84e-26`. This resolves the earlier binary64 negatives
as cancellation. Explicit outward-rounded transform remainders remain needed
for certification. See `reduced-source-central-decimal-concavity-resolution.md`.

The certification budget is now explicit. The depth-120 eta-value tail is at
most `2^-120` and remains only about `1.13e-21` after a pessimistic boundary
slope amplification, below the revised chord margin. The remaining work is
precisely a differentiated Euler-tail bound for `eta'` plus derivative-aware
propagation of the digamma remainder. See
`central-concavity-certification-error-budget.md`.

The differentiated eta tail is now bounded uniformly on the central interval.
A positive Laplace representation and a split at unit Laplace time give
`|d_k'|<=3/k+1/k^2`; the depth-120 tail is below `1.90e-38`, or about
`2.83e-22` after a deliberately inflated boundary budget. The remaining
finite-certificate remainder is the correlated digamma derivative error. See
`eta-derivative-euler-tail-bound.md`.

The digamma correlation problem is avoided by recurrence conditioning: moving
the asymptotic evaluation point from 20 to 100 shrinks the omitted `z^-18` term
by `5^18`. Even independent hostile-stencil propagation then lies below the
observed gap. Both analytic transform tails are now budgeted; outward rounding
and finite-difference truncation remain before a certificate.

Analytic source differentiation removes the finite-difference gate entirely.
Carrying `eta,eta',eta''` and `digamma,trigamma` reproduces the positive chord
margins. A second Laplace split bounds the depth-120 eta-double-prime tail
below `1.63e-37`, still below the corrected margin after hostile amplification.
Only outward-rounded nonlinear propagation remains for this finite central
certificate. See `central-analytic-slope-and-eta-second-tail.md`.

Directed 90-digit propagation now completes that finite step. All 21 central
chords are strictly interval-positive; the weakest enclosure is
`[3.6492372625e-20,3.6501288511e-20]`. Exact rational Bernoulli coefficients
and exact Decimal negation were required to remove two default-context defects.
This is a finite unconditional source certificate, not continuum concavity or
RH. See `central-reciprocal-slope-interval-certificate.md`.

Inserting `3*10^k` between the power-of-ten endpoints densifies the directed
central certificate from 21 to 78 chords. Every enclosure remains strictly
positive. The new weakest gap, on `[10^-8,3*10^-8]`, is
`[1.7964066809e-21,1.8106786499e-21]`. The denser hostile mesh therefore
survives with a resolved margin rather than merely repeating the old points.

The continuum upgrade now has the correct cancellation-free coordinate. With
`ell(t)=log Xi(1/2+sqrt(t))`, reflection symmetry gives `S=ell'` and exactly
`F=(4t-1)ell'`. Hence reciprocal-slope concavity is the fourth-order source
inequality `2F'F'''-3(F'')^2>=0`, with all three `F` derivatives polynomial in
`ell',...,ell''''`. Outward-rounded Taylor models of `ell` can therefore cover
intervals without square-root dependency blow-up. See
`central-xi-log-curvature-continuum-reduction.md`.

The weakest dense chord already fixes the continuum error scale. Its
`~1.8e-21` midpoint gap on a width-`2e-8` cell corresponds to a certified
triangularly weighted `H''` average between about `-3.621e-5` and `-3.593e-5`.
Thus a Taylor box only needs to control curvature oscillation below `3.59e-5`,
while also proving `F'>0` on the cell. See
`central-chord-average-curvature-margin.md`.

The required oscillation bound is explicit. For `g=F'`,
`H'''=(18gg'g''-4g^2g'''-15(g')^3)/(8g^(7/2))`; in the cancellation-free Xi
coordinate this requires `ell` only through fifth derivative. Bounding this on
each cell and multiplying by cell width upgrades the negative weighted
curvature average to pointwise concavity.

A 90-digit fifth-derivative reconnaissance indicates the current mesh is
already sufficient. The largest estimated cell oscillation is `7.64e-8` on
`[10^-8,3*10^-8]`, against a certified `3.59e-5` average-curvature margin—a
safety factor about 470. The rigorous fifth-jet box may therefore be coarse;
no further mesh refinement is presently indicated. See
`central-h-third-derivative-oscillation-reconnaissance.md`.

Analytic fourth-order Taylor propagation now removes finite differences from
that estimate. At the hardest midpoint it gives `H''~-3.60653e-5` and
`H'''~3.76186`, hence oscillation `7.524e-8`. The jet architecture explicitly
separates `eta_s` from the composed `t` derivative, repairing a failed first
draft and providing the template for directed interval jets. See
`central-source-analytic-fourth-jet.md`.

The eta tail hierarchy needed by interval jets now has one uniform theorem.
Cauchy radius `0.1`, an elementary reciprocal-gamma bound below four, and the
Euler integral give `|R_(N,j)|<=4 j! 10^j 2^-N/(N+0.4)`. At depth 300 all
tails through derivative order six are below `5e-83`, sufficient for the
fifth-jet architecture. See `eta-high-jet-cauchy-tail-theorem.md`.

The gamma tail hierarchy is now equally uniform. The differentiated Stieltjes
remainder after `B_16` obeys
`|R^(j)(z)|<=|B_18|(18)_j/(18 z^(18+j))`. Recurrence to argument 1000, including
the `s/2` chain factors, puts every required order through six below `3.06e-54`.
No gamma--eta error cancellation is needed. See
`digamma-high-jet-remainder-theorem.md`.

The coefficient parity audit found the initial differentiated gamma remainder
bound too optimistic. A complex Cauchy disk repairs it, costing a safe `2^18`
factor after the `s/2` chain cancellation. Recurrence 1000 still leaves all
required derivative errors below `8.01e-49` and makes reflection parity an
internal enclosure check.

The centered directed jet now passes that parity check at every even order
through 12 and certifies `H''(0)<0`, `H'''(0)>0` in narrow intervals. A final
arithmetic defect was caught: the Euler `2^k` accumulator had been rounded by
the default Decimal context; using an integer restores exact denominators.
This is the first rigorous curvature certificate at the central boundary. See
`central-xi-log-boundary-jet-interval-certificate.md`.

The first positive-width cell now reduces to one coarse complex-disk gate. If
`|F'|>=1/16` on `|t|<=1/4`, then `|H|<=4` and Cauchy gives
`sup|H'''|<1536.001`, below the `1796.4` threshold forced by the certified
average curvature. This would prove `H''<0` on `[10^-8,3*10^-8]` with margin
about `5.21e-6`. See `central-first-cell-one-circle-cauchy-gate.md`.

The first natural interval-jet probe decisively fails conditioning. On
`[10^-8,3*10^-8]` it encloses `F'` in roughly `[-1.84e10,1.90e10]` although the
point value is about `0.09246`. Analytic tails are irrelevant at this scale.
This rules out interval propagation through the unreduced singular prefactor;
the next implementation must build the even `ell(t)` jet directly. See
`natural-central-interval-jet-conditioning-no-go.md`.

The reflection-even Xi series now supersedes both earlier `H'''~3.8`
reconnaissances. Expanding the odd centered logarithmic derivative and dividing
by `2q` gives the analytic `ell'(t)` series directly. It yields
`H''(0)~-3.60438e-5` and `H'''(0)~4.47e-7`, while its values at three boundary
points lie inside independent directed intervals. The earlier high derivative
values were cancellation artifacts and are retracted. See
`central-xi-log-even-series-construction.md`.

The certified centered coefficients make the quarter-disk gate forgiving. The
known degree-four `F'` polynomial has modulus at least `0.0923826193` on
`|t|<=1/4`; the target is only `0.0625`. Thus the entire omitted tail may be as
large as `0.0298826193`. What remains is a coarse Xi-log series tail bound, not
fine boundary cancellation. See
`central-F-prime-quarter-disk-polynomial-budget.md`.

Cauchy reduces that tail allowance to a coarse outer-disk target. If `F'` is
analytic and bounded by 20 on `|t|<=1`, then its degree-at-least-five tail on
`|t|<=1/4` is at most `20/768~0.0260417`, leaving margin `0.00384095` inside
the certified allowance. See
`central-F-prime-unit-disk-Cauchy-reduction.md`.

A 96-point hostile unit-circle scan finds maximum `|F'|~0.09275656` at `t=-1`;
step/depth controls differ by at most `4.45e-10`. The proposed bound 20 thus
has sampled safety factor above 215. The remaining issue is rigorous complex
analyticity/enclosure, not numerical size. See
`reduced-source-F-prime-unit-circle-reconnaissance.md`.

Unit-disk analyticity itself reduces to one real theta inequality. Positivity
of the Riemann kernel gives
`|Xi(1/2+q)-Xi(1/2)|<=Xi(3/2)-Xi(1/2)` for `|q|<=1`. Hence
`Xi(3/2)<2Xi(1/2)` proves zero-freeness by Rouché, without zero locations. The
numerical margin is enormous; directed real-point evaluation is next. See
`xi-centered-unit-disk-theta-Rouche-reduction.md`.

That Rouché inequality is now unconditional: directed Euler terms and coarse
elementary gamma bounds give `Xi(1/2)>0.434455`, `Xi(3/2)<0.75`, leaving margin
above `0.1189`. Hence `Xi` has no zeros on `|s-1/2|<=1` without importing any
zero locations. The analyticity half of the outer-disk gate is closed; only
the coarse `|F'|` upper bound remains. See
`xi-centered-unit-disk-Rouche-certificate.md`.

Theta-moment positivity now collapses that remaining complex-disk bound to
four real endpoint quantities. With
`m=2Xi(1/2)-Xi(3/2)`, `A=Xi'(3/2)/2`, and
`B=(Xi''(3/2)-Xi'(3/2))/4`, one has
`|F'|<=4A/m+5(B/m+(A/m)^2)` on the unit disk. Numerical reconnaissance gives
only `0.102201`, nearly 196 times below the sufficient target 20. A directed
real endpoint evaluation is the sole remaining certification step. See
`central-F-prime-unit-disk-theta-moment-reduction.md`.

An elementary domination avoids even the endpoint derivative computation.
Positive coefficients give `Y'(1)<=Y(9)/9` and `Y''(1)<=2Y(9)/81`, while
log-convexity of Gamma, the zeta integral test, and `pi>3.1` give
`Y(9)=Xi(7/2)<3/4`. With the certified Rouché margin `m>0.1189`, directed
arithmetic yields `sup|F'|<6.038308<20`. The unit-disk gate is closed. Its
Cauchy tail is below `0.007863`, so the quarter-disk nonvanishing condition
and hence pointwise reciprocal-slope concavity on the first positive-width
cell are now certified. See
`central-F-prime-unit-disk-theta-coarse-certificate.md`.
