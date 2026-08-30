# The one-loop source determines an instrument density

Owner: `marici.Nima`

The Breit--Wheeler amplitude and the reconstructed elastic amplitude define
the two branches of the asymptotic scattering map

\[
H_{\gamma\gamma}
\longrightarrow
H_{\gamma\gamma}\oplus H_{e^+e^-}.
\]

Write (S=I+iT) and let (K) be the pair-production branch.  In the
normalization already fixed by the Cut,

\[
2\operatorname{Im}T=K^\dagger K.
\]

Consequently

\[
S^\dagger S+K^\dagger K=I+O(e^8),
\]

where (T_{\gamma\gamma}=O(e^4)) and (K=O(e^2)).  The tree pair amplitude
supplies (K); the vector dispersion theorem supplies the real part and
therefore the coherent phase of (T).  The source boundary jet removes the
last one-loop ambiguity.

For any normalized wavepacket, projection onto the two particle-content
sectors gives the operations

\[
\mathcal I_{\rm el}(\rho)
=P_{\gamma\gamma}S\rho S^\dagger P_{\gamma\gamma},
\]

\[
\mathcal I_{\rm pair}(\rho)
=P_{e^+e^-}S\rho S^\dagger P_{e^+e^-}.
\]

Their sum is trace preserving to the audited perturbative order.  This is a
source-derived instrument density, not merely an effect: both the event
state and the coherent no-event successor are fixed.

## What remains external

Plane waves carry delta-function and flux normalization, so an amplitude
density is not itself a bounded laboratory channel.  Exactly one experiment
object remains to be supplied:

\[
\mathcal N_{\rm exp}
=\text{normalized incoming wavepacket/exposure functional}.
\]

Once \(\mathcal N_{\rm exp}\) is fixed, the source amplitude and the canonical
particle-content projections produce normalized event probabilities and
conditional successor states.  Detector refinements may further split the
pair outcome, but they are not required for the binary elastic/pair
instrument.

## Scope

The exact matrix checker uses the general polar completion

\[
S_{\rm el}=U_{\rm source}\sqrt{I-\tau E_{\rm cut}}
\]

to verify complete positivity and normalization without assuming that the
source phase commutes with the Cut.  This is a finite-exposure realization of
the branch architecture.  Only its expansion through one loop is fixed by
the present QED calculation; higher-order finite-exposure terms require the
corresponding higher-loop source amplitude.
