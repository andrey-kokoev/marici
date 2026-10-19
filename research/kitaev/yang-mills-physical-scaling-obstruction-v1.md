# Conditional no-promotion theorem for the retained strong-coupling window

Owner: `marici.Kitaev`. Status: written conditional theorem, not independent certification of its source assumptions. This post-batch follow-up was authorized by the operator after an external literature audit. It does not revise the frozen iteration16 constructor or claim a continuum Yang-Mills result.

## Issue-boundary DPC

- **Problem:** the volume-uniform lattice gap was previously separated from physical refinement chiefly by a coupling-regime warning. What actually follows if the declared physical matching is imposed while remaining in that regime?
- **Conjecture:** the retained lower bound then diverges in physical units; centered finite-energy positive-time vacuum correlations cannot have a nonzero, finite limit at all positive times under that same clock.
- **Rivals:** a fixed source-unit gap is automatically a finite physical mass; subtracting vacuum energy removes the divergence; multiplicative field renormalization preserves a finite nonzero positive-time theory despite the spectral threshold; one rapidly decaying observable proves a gap for the whole physical Hilbert space.
- **Risky consequence:** an explicit lower bound 40/(sqrt(27)*a), with a spectral two-time comparison requiring neither uniform equal-time vector norms nor a common cutoff Hilbert space.
- **Falsification:** exact diagonal fixtures show that renormalizing a fast mode to remain nonzero at a later time makes an earlier positive-time correlation diverge. Changing the clock can evade the conclusion, and an undetected finite-energy spectator defeats an observable-only gap inference. These scope controls are not gauge-theory or continuum proofs.
- **Disposition:** the conditional theorem follows below. Independent review of the source gap and derivation of the physical matching remain open. The retained window is not a finite-mass continuum route under the stated matching; the result does not decide what happens outside that window.

## 1. Assumptions and units

Let a>0 denote physical spatial lattice spacing. For each a let H_a be a nonnegative self-adjoint vacuum-energy-subtracted PHYSICAL Hamiltonian on its own Hilbert space, P_a its declared vacuum-sector projection, and q_a its closed form. Assume

q_a(v)>=m_a*||(I-P_a)v||^2

on the entire physical form domain. A gap observed by only one reader is insufficient. No equality or isometry between the Hilbert spaces at different a is assumed.

Retain the source parameters

eta_a=lambda_a/kappa_a < 27/262144,
R_a=(4096/3)*eta_a,
m_a=kappa_a*(1/2-3R_a),
kappa_a>0, eta_a>=0.

The source construction claims precisely such a form inequality, uniformly over boxes, at fixed lattice scope. Its analytic proof is an INPUT to this theorem, not established by the new checker.

Now additionally ASSUME the physical matching

kappa_a=g_a^2/(2a), lambda_a=2/(a*g_a^2), g_a>0.

The matching is a declared convention conditional here; its applicability to the chosen Hamiltonian/heat-kernel regulator is not proved by this note. The Euclidean parameter in exp(-t H_a) is held fixed in these physical units. No a-dependent clock renormalization is hidden in t.

## 2. Divergent physical spectral threshold

The matching gives eta_a=4/g_a^4. The admitted window therefore implies

g_a^4>1048576/27, hence g_a^2>1024/sqrt(27).

Since R_a<9/64,

m_a>5*kappa_a/64 = 5*g_a^2/(128a) > 40/(sqrt(27)*a).

Thus the bottom of the nonvacuum spectrum is bounded below by a number tending to infinity as a tends to zero. This follows from the assumed form inequality and the spectral theorem. It is not merely a failure to establish a finite lower bound.

For comparison, the parameter-sensitive expression is

a*m_a=g_a^2/4-8192/g_a^2.

At the excluded endpoint g_a^2=1024/sqrt(27), it equals40/sqrt(27); it increases for larger positive g_a^2. The simpler5*kappa/64 estimate already suffices.

Subtracting any scalar vacuum energy leaves spectral differences unchanged. It cannot alter this conclusion.

## 3. Two-time spectral comparison

Let v_a be any Hilbert vector orthogonal to ran(P_a). It may depend on a and its norm may diverge as a tends to zero. Define

C_a(t)=<v_a,exp(-t H_a)v_a>, t>0.

Each C_a is nonnegative. Its scalar spectral measure is supported in [m_a,infinity). Therefore for0<t1<t2,

0<=C_a(t2)<=exp[-m_a*(t2-t1)]*C_a(t1).

If limsup_(a->0) C_a(t1)<infinity, it follows that C_a(t2)->0. Consequently, if C_a(t) has a finite limit at EVERY positive t, that limit is zero at every positive t (choose any smaller positive t1 for each t2).

No uniform bound at time0 is needed. Multiplicative field renormalizations are included by absorbing the cutoff-dependent scalar in v_a. For a centered lattice observable O_a, take v_a=(I-P_a)O_a Omega_a whenever this is a Hilbert vector. If a later-time autocorrelation stays bounded away from zero, the earlier-time correlation must instead grow at least exponentially in m_a*(t2-t1).

For two centered vector families v_a,w_a, the semigroup Cauchy-Schwarz inequality gives

|<v_a,exp(-t H_a)w_a>|^2<=C_(v,a)(t)*C_(w,a)(t).

Thus finite positive-time limits of their diagonal correlations force these later cross-correlations to vanish as well.

## 4. Exact scope of the obstruction

This excludes a nonzero finite-energy positive-time vacuum correlation theory built from such centered vectors, under the stated matching, clock and finite-positive-time-limit hypothesis. It is not a proof that every conceivable distributional limit is zero. In particular it does not dispose of contact terms supported at coincident time, disconnected vacuum expectations, arbitrary nonspectral observables, or limits for which the stipulated correlation convergence fails.

For a continuum reconstruction application one must justify that the intended spatially smeared fields yield these finite positive-time diagonal correlations. Reflection positivity and a reconstruction theorem cannot simply be assumed to supply missing continuum fields or covariance.

The result does not assert that four-dimensional Yang-Mills is trivial. It obstructs THIS retained regime and matching. At least one of the regime, matching/clock, gap premise, or proposed finite-positive-time target must change to evade it. Such a change is necessary to evade the argument, not sufficient to construct a continuum theory.

For example, replacing H_a by s_a H_a changes the spectral threshold to s_a m_a. An a-dependent s_a can remove its divergence, but changes the energy/time matching and requires an independent physical justification. An additive energy shift is different and cannot help.

## 5. Reproducible finite controls

`checkers/check_yang_mills_physical_scaling_obstruction.py` checks exact rational source-window arithmetic and diagonal spectral fixtures. Time samples are t1=log(2),t2=2log(2), so integer spectral exponents give exact fractions without numerical exponentiation.

Controls distinguish:

1. The open source endpoint, including exclusion of equality.
2. Actual matching samples with a*m_a>40/sqrt(27), verified by positive rational squares.
3. Two-time spectral envelopes with arbitrary nonnegative spectral weights.
4. Multiplicative normalization giving C_a(t2)=1 while C_a(t1) diverges.
5. A changed-clock example with finite nonzero correlations, outside the fixed-clock conclusion.
6. A hidden finite-energy mode, rejecting inference of a whole-space gap from a fast reader alone.
7. Weighted block-ell1 localization implying weighted ell2 localization (a separate review clarification).

The checker does not prove the source gap, physical matching, unbounded-operator spectral theorem, existence of any continuum field, or the reviewed Yang-Mills target. The analytical statement above is conditional on those explicitly separated premises.

Contract: `contracts/yang-mills-physical-scaling-obstruction.v1.json`.
Receipt: `results/yang-mills-physical-scaling-obstruction-v1.json`.

## Provenance and reopening

The divergent-gap and two-time arguments were supplied in the operator-forwarded external audit and checked algebraically here. No external bibliography was freshly verified in this session. Supporting source files are the existing uniform-detection and ground-state-transfer notes. The accompanying self-contained Shoshin second-pass packet separates existing localization/domain arguments from the audit's proposed tasks.

Reopen this conditional obstruction only if an assumption changes or its spectral deduction is falsified. Review of the upstream construction remains open independently; neither this negative result nor finite controls certify that construction. No graph mutation, delegation, commit or push is implied by writing this note.
