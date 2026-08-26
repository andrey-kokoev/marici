# Markov oscillator loss-noise identity

Owner: `marici.Aspect`

Strength: source-typed Markov input-output identity.

## Bounded question

Can the absorptive response and its required quantum noise be derived from one
common finite source constructor rather than fitted independently?

## Source and typed ports

The source is one harmonic mode with external coupling \(\kappa_e=1\),
internal coupling \(\kappa_i=4\), and resonance \(\Omega=1\). The typed inputs
are the observable external field and an unobserved internal Markov bath. The
detector sees only the external output. This is a source model for a damped
resonator, not a microscopic derivation of a specific magneto-optic material.

With \(\Delta=\omega-\Omega\), constructor order is: add the independently
declared coupling rates, solve the Langevin equation, apply the external
input-output relation, then trace the internal bath. The response is

\[
\chi(\omega)=\frac{1}{(\kappa_e+\kappa_i)/2-i\Delta},
\]

and the external output takes the form

\[
a_{\rm out}=r(\omega)a_{\rm in}+q(\omega)b_{\rm in},
\quad r=1-\kappa_e\chi,
\quad q=-\sqrt{\kappa_e\kappa_i}\,\chi.
\]

The pole \(\Omega-i(\kappa_e+\kappa_i)/2\) is strictly in the lower
half-plane.

## Exact loss-noise identity

The common coupling constructor gives

\[
1-|r(\omega)|^2=|q(\omega)|^2
=\kappa_e\kappa_i|\chi(\omega)|^2.
\]

Therefore the same internal coupling that broadens the response also fixes the
noise amplitude required by the canonical commutator. At resonance,
\(\chi=2/5\), \(r=3/5\), and \(q=-4/5\). Deleting the bath noise retains the
mean lossy reflection but leaves commutator weight \(9/25\), not one. This is
the smallest hostile.

For a bath occupation \(n\), the detected added occupation is
\(|q|^2n\), which is nonnegative. Setting internal coupling to zero removes
the internal noise port and restores unit-modulus single-port reflection.

## Frame, conservation, and detector boundary

The rotating frequency frame and input-output sign convention are fixed before
forming \(r\) and \(q\). Total system-plus-input-field commutators are
conserved; energy in the retained external channel may dissipate into the
internal bath. The external detector cannot reconstruct the bath realization
from one record.

## Completion gate

This is the Markov, single-mode loss-noise identity. It does not establish a
non-Markov spectral density, thermal equilibrium, the full frequency-dependent
fluctuation-dissipation theorem, spatial dispersion, or a microscopic
material-specific coupling. Those require new source data, not additional
detector rank.

Run:

```powershell
python research/aspect/checkers/markov_oscillator_loss_noise_identity.py
```
