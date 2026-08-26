# Thermal sideband detailed-balance instrument

Owner: `marici.Aspect`

Strength: finite Markov detailed-balance identification theorem.

## Bounded question

Does a calibrated linewidth determine thermal quantum noise, or must an
instrument separately resolve the upward and downward bath rates?

## Source and typed ports

The source is one stable oscillator with downward transition rate
\(\Gamma_\downarrow\) and upward rate \(\Gamma_\uparrow\), with
\(\Gamma_\downarrow>\Gamma_\uparrow\geq0\). The instrument has a coherent
probe port for linewidth estimation and two frequency-resolved heterodyne or
photon-counting sideband ports. The detector calibration fixes gain,
bandwidth, frequency frame, and the ordering of upper and lower sidebands.

Constructor order is: declare the two transition rates, form the dynamical
linewidth, collect both calibrated sideband records, then infer occupation or
detailed-balance ratio. No measured ratio is used to create the source rates.

## Exact identities

The amplitude-damping scale is controlled by the rate difference,

\[
\kappa=\Gamma_\downarrow-\Gamma_\uparrow,
\]

whereas the symmetrized Markov noise weight is their sum. The stationary
occupation and sideband ratio are

\[
n=\frac{\Gamma_\uparrow}
        {\Gamma_\downarrow-\Gamma_\uparrow},
\qquad
R=\frac{\Gamma_\uparrow}{\Gamma_\downarrow}.
\]

For the exact instance \((\Gamma_\downarrow,\Gamma_\uparrow)=(2,1)\), the
linewidth is 1, noise weight is 3, occupation is 1, and sideband ratio is
\(1/2\).

## Smallest linewidth-preserving hostile

The rates \((3,2)\) have the same linewidth 1 but noise weight 5, occupation
2, and sideband ratio \(2/3\). Therefore response linewidth alone is not
faithful on thermal bath state. This is not a calibration defect: it is a
source fiber left unresolved by the response map.

Joint linewidth and symmetrized-noise measurement recovers the two rates by

\[
\Gamma_\downarrow=\frac{S+\kappa}{2},
\qquad
\Gamma_\uparrow=\frac{S-\kappa}{2}.
\]

Resolved sideband asymmetry provides the independent rate ratio. The
instrument identifies which thermal realization occurred; a source thermal
law explains why that ratio holds.

## Conservation and completion

The full oscillator-bath constructor preserves canonical commutators while
the reduced oscillator dissipates energy. Sideband counts are positive stable
records, not selected source extensions. This finite model does not prove a
frequency-dependent KMS relation, non-Markov memory kernel, continuum bath
topology, or microscopic material coupling. Those remain the completion gate.

Run:

```powershell
python research/aspect/checkers/thermal_sideband_detailed_balance_instrument.py
```
