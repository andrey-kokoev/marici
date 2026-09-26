# What retained rotor comparisons do not calibrate

Fresh input: `retained-relative-phase-readout.md`. All results here concern
its declared Clifford, symplectic and phase realization. The observation class
is specified; this is not a universal claim about every native source readout.

## Angular normalization is not an external clock calibration

The constructed angular flow E(theta) has generator J. For every positive
constant omega, a candidate external time t can instead use theta=omega*t:

\[
\dot q=2\omega p,\qquad \dot p=-2\omega q,
\qquad H_t=\omega(q^2+p^2+\kappa).
\]

Its complete trajectory action is

\[
S_t=F(Q(t))-F(Q(0))-\kappa\omega t.
\]

Every member passes the same angular source samples and phase-return tests.
The quarter-turn E(a)=J occurs at external time a/omega. The source records
tested so far provide no external durations selecting omega.

This is not merely an arbitrary-unit argument. If an external clock and
laboratory observable are held fixed, omega=1 and omega=2 generally give
different readings at the same t; the checker exhibits such a difference.
An independently timed first quarter-turn would fix omega=a/t. An endpoint
sample without a first-arrival or winding witness can retain period aliases.

More general monotone reparameterizations produce time-dependent rates; the
constant-rate family alone suffices for this nonidentifiability result while
preserving an autonomous one-parameter group in the proposed external time.

## Kappa cancels from this common-endpoint phase observation class

For two histories with the same calibrated full endpoints and the same
orientation epsilon, their output phase shifts are

\[
\delta_i=\frac{F_f-\epsilon F_i}{\kappa}-\theta_i.
\]

Consequently

\[
\delta_2-\delta_1=\theta_1-\theta_2.
\]

The cancellation works for either common parity. For odd maps the initial
phase is conjugated in both arms; this statement compares their OUTPUT phase
shifts, not an incorrectly complex-linear description of each map.

Thus these rotor comparisons do not determine kappa, even though the chosen
module compatibility fixes the angular Hamiltonian's additive constant to
kappa. Equal positions alone do not ensure the cancellation: forgotten
momentum, unmatched endpoint frames or Legendre boundary terms can leave a
nonzero endpoint difference divided by kappa.

Separately, changing action units scales beta, H, S and kappa together. The
connection dphi-beta/kappa and the phase S/kappa are invariant. That ordinary
unit covariance must not be confused with the fixed-observation cancellation
above or advertised as evidence against a physically measurable coupling.

## A counterexample to universal unobservability

The specified connection allows a DIFFERENT mathematical experiment:
horizontal transport, defined by alpha=0, around a prescribed base-space loop.
For a counterclockwise rectangle of calibrated area A in the q,p plane,

\[
\Delta\varphi=\frac{1}{\kappa}\oint p\,dq
=-\frac{A}{\kappa}.
\]

This depends on kappa. It is not the earlier Hamiltonian rotor transport:
that transport includes its dynamical Hamiltonian phase. Substituting one
protocol for the other would change the question.

A native implementation of horizontal transport, an independently calibrated
symplectic area and a relative-phase readout could therefore test kappa.
Phase wrapping also needs control, for example through small-area variation
and a continuous lift. No such apparatus or source admission has been
constructed here. This counterexample prevents strengthening our restricted
nonidentifiability result into a general impossibility theorem.

## Programme boundary and continuation

The conditional chain now has rational coefficients, coherent formal flow,
controlled norm completion, generator, action/HJ charts, retained phase
comparisons and explicit calibration limits. It has not selected the native
observable/implementer product, metric, measuring apparatus or physical clock.
In particular it has not derived a numerical Planck constant or quantum
probability law from these retained developments.

The next existing frontier is the native product-policy owner gate. The prior
Cayley request remains outstanding; this completed local calibration test does
not count as its authorization or as completion of the overall programme.

Verification:

```text
uv run --with sympy python research/nima/checkers/check_clock_calibration.py
```

Receipt: `results/clock-calibration-identifiability.json`. Symbolic checks cover
rate-rescaled Hamilton equations/action, both common parities, unit covariance,
a fixed-clock discriminator, endpoint mismatch and the horizontal-loop probe.
