# Optical attenuation can realize the shell probe only after a label-mode embedding

## Question

Can the shell-generating modulation \(D_t(e)=t^{j(e)}\) be implemented by the existing continuous-mode optical attenuation formalism?

## Claim boundary

At each finite cutoff, \(D_t\) is a positive contraction and therefore has the operator type of passive optical attenuation. The existing optical pullback theorem then transports detector effects and supplies an explicit loss channel. But physical realization requires a new embedding that maps arithmetic shell labels to independently attenuated optical modes and intertwines the history readout. No such embedding is currently sourced.

## Finite shell-control operator

On the finite labelled edge space, define

\[
V_t=\operatorname{diag}(t^{j(e)}),
\qquad 0<t<1.
\]

Then

\[
0<V_t^*V_t\leq I,
\]

so \(V_t\) is a strict contraction. If \(C\) is the common-history detector coupler, the modulated coupler is

\[
CV_t,
\]

and its effect is

\[
E_t=V_t^*C^*CV_t.
\]

The missing probability carried by attenuation cannot be discarded. The optical attachment theorem requires the explicit loss effect

\[
E_{\rm loss}(t)=I-V_t^*V_t
=\operatorname{diag}(1-t^{2j(e)}).
\]

Thus the proposed generating family is compatible with passive-effect calculus only when no-detection events are retained.

## Required crossing

Let \(H_{\rm src}\) denote a finite shell-labelled source packet and \(H_{\rm opt}\) a frequency--polarization mode space. Physical implementation requires an admitted map

\[
\iota:H_{\rm src}\longrightarrow H_{\rm opt}
\]

and an optical contraction \(\widetilde V_t\) satisfying

\[
\widetilde V_t\iota=\iota V_t.
\]

It also requires an optical detector coupler \(\widetilde C\) whose pullback agrees with common history:

\[
\widetilde C\iota=C.
\]

These two commuting equations are the acceptance test. Equal dimensions, a tunable filter, or a formally similar attenuation curve do not construct \(\iota\).

## Mode-separation requirement

The embedding must preserve shell distinctions before codiagonalization. If two shell labels map to the same optical mode with no independent control, \(\widetilde V_t\) cannot implement different factors \(t^j\). If the detector sees only the already-summed common-history mode, every optical effect factors through \(B\) and remains blind to cycles.

A frequency-bin implementation would need a source-derived assignment

\[
j\longmapsto\Omega_j
\]

to disjoint measurable bands and a bounded transfer field equal to \(t^j\) on \(\Omega_j\). A spatial-mode or polarization implementation has the analogous typed assignment. No assignment is preferred here.

## Noise and normalization

Once \(\iota,\widetilde V_t,\widetilde C\) are realized, detected and loss outcomes form a normalized effect family. Repeated calibrated settings \(t_n\) provide the response Gram form. The joint detector noise, including loss counts and cross-setting correlations, determines the Fisher operator. Renormalizing only detected events would condition on survival and change the proposed covariance.

## Disposition

Passive optical attenuation is structurally capable of realizing the shell-generating probe, but capability is not realization. The first missing typed object is the shell-label-preserving optical embedding \(\iota\) satisfying both intertwining equations. Until it is supplied, the optical model neither verifies nor falsifies physical route-residue coupling.
