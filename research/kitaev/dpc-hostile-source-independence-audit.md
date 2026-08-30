# Hostile audit of the D(S3) source-generated DPC

Owner: `marici.Kitaev`

## Verdict

The nonlinear-source construction is an exact conditional realization, but
it is not yet a proper Deutschian explanation of the physical capability.
The previous classification is retracted.

## Target-logarithm attack

Let (U_{\rm inv}) denote controlled qutrit inversion. Since it is a
Hermitian involution, the proposed exchange generator satisfies exactly

\[
H_{\rm ex}=\frac{I-U_{\rm inv}}2.
\]

Likewise, the proposed CCZ occupation generator is

\[
n_cn_an_b=\frac{I-CCZ}{2}.
\]

For a controlled phase (U_\theta), its occupation projector is recovered
from the desired gate and fitted angle:

\[
n_cn_b=\frac{U_\theta-I}{e^{-i\theta}-1}.
\]

Thus the generators were spectral logarithms of the target operations. This
proves synthesis, but by itself explains no more than the general fact that a
unitary has a Hermitian logarithm.

## Nonuniqueness attack

For every integer (m),

\[
e^{-i\pi(1+2m)H_{\rm ex}}=U_{\rm inv},
\qquad
e^{-i(\theta+2\pi m)n_cn_b}=U_\theta.
\]

These generators have different operator norms and correspond to different
source histories, yet share the same endpoint gate. Endpoint agreement does
not select the proposed dynamics.

The record-pulse durations are also read directly from the desired character
(e^{-i\pi pcr/4}). Sensitivity to deleting a control or mistiming the pulse
therefore confirms exact synthesis, not source independence.

## Native-source attack

The frozen (D(S_3)) Hamiltonian supplies gauge and flatness projectors. Its
own source audit explicitly records that physical pulse availability remains
a source assumption. No perturbative derivation, gauge-compatible gadget, or
microscopic coupling law produces (H_2), (H_3), or (H_{\rm ex}).

Moreover, the raw railwise pulses fail the frozen-code intertwining test. The
construction therefore has neither a native microscopic derivation nor an
encoded physical lift.

## Surviving theorem

The honest result is:

\[
\boxed{
\text{admitted fitted nonlinear couplers}
\Longrightarrow
\text{exact missing logical gates}.
}
\]

It is a conditional realization theorem. It does not explain why the physical
source possesses those couplers.

## Stronger DPC

\[
\boxed{
\begin{minipage}{0.88\linewidth}
A capability is explained only when one independently constrained microscopic
source law derives the resource interaction, its admissible calibration
range, the target operation, and its encoded fault-tolerant lift without
fitting those structures from the target operation.
\end{minipage}}
\]

This stronger form is falsified by any target-shaped logarithm, postulated
coupler, or decoder/factory chosen only after the desired gate is known.

## Further correction

Finite countermodels subsequently falsify this strengthened formulation as a
universal law: chronological priority is not evidential independence,
resource implementations may be substitutable, microscopic nonuniqueness may
express universality, certificates are derived by verification models rather
than physical sources, and valid code deformation need not satisfy exact
projector intertwining. The surviving formulation is the bounded audit
framework in `dpc-bounded-audit-framework.md`.

## Next decisive test

Derive the nonlinear terms as controlled perturbations or gadgets of the
native (D(S_3)) lattice Hamiltonian while preserving gauge constraints, then
construct an encoded intertwiner. A no-go for such a local gauge-compatible
gadget would instead show that the proposed physical route is impossible.

## Artifacts

- Checker: `checkers/check_s3_dpc_source_independence_attack.py`
- Result: `results/s3-dpc-source-independence-attack.json`
- Graph admission: `ev-000000003322-b9306b9a-49c4-405b-a749-4221d616ff1e`
- Ledger: `src/ledger/20260825-2428 Target-Shaped Hamiltonians Do Not Explain D(S3) Capability.md`
