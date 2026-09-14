# Shell attenuation intertwining forces optical mode separation

## Question

What structural constraints does the required optical intertwiner impose, and is there a mathematical obstruction to constructing one?

## Claim boundary

Intertwining the full family \(D_t(e)=t^{j(e)}\) forces different shell sectors into distinct optical attenuation eigenspaces. An abstract isometric optical realization exists by assigning orthogonal mode sectors, but the assignment is noncanonical and supplies no laboratory identification.

## Spectral rigidity

Decompose the source by shell label:

\[
H_{\rm src}=\bigoplus_{j\geq1}H_j,
\qquad
D_t|_{H_j}=t^jI.
\]

Suppose an injective map \(\iota\) satisfies

\[
\widetilde V_t\iota=\iota D_t
\]

for one \(t\in(0,1)\). Since the eigenvalues \(t^j\) are distinct, \(\iota(H_j)\) lies in the \(t^j\)-eigenspace of \(\widetilde V_t\). If \(\widetilde V_t\) is normal, these eigenspaces are mutually orthogonal. Thus a valid normal optical attenuation cannot encode distinct shells into one unresolved mode.

Intertwining the accumulating family \((t_n)\) strengthens the statement: the joint spectral signature

\[
(t_n^j)_{n\geq0}
\]

uniquely identifies \(j\).

## Continuous-mode formulation

For a decomposable optical filter

\[
(\widetilde V_t\psi)(\omega)
=g_t(\omega)\psi(\omega),
\]

the image of \(H_j\) must be supported, up to null sets, where

\[
g_t(\omega)=t^j.
\]

For the full family, define the joint level set

\[
\Omega_j=
\{\omega:g_{t_n}(\omega)=t_n^j\text{ for every }n\}.
\]

Distinct \(\Omega_j\) are disjoint. A shell-preserving implementation therefore requires nonzero detector-accessible mode measure in each used \(\Omega_j\).

## Abstract existence

There is no mathematical Hilbert-space obstruction. Take

\[
H_{\rm opt}=\bigoplus_j H_j,
\qquad
\widetilde V_t=\bigoplus_j t^jI_{H_j},
\]

and let \(\iota\) be the direct-sum identity. Any separable continuous-mode space with countably many disjoint positive-measure sectors can host an isomorphic realization.

This construction does not identify shell number with frequency, polarization, spatial mode, or another laboratory degree of freedom. Choosing such an identification is the missing source-derived map.

## Detector condition

Attenuation intertwining alone is insufficient. The detector must also satisfy

\[
\widetilde C\iota=C_{\rm history}.
\]

A mode separator followed by detectors that sum intensities or amplitudes in the wrong manner may preserve attenuation eigenvalues while failing the common-history readout equation.

## Falsifiers

The proposed optical realization fails if:

- measured transfer functions do not have distinct shell-dependent joint signatures;
- cross-talk mixes the joint eigenspaces beyond the calibrated error budget;
- some shell sector lies entirely in the loss space;
- detector pullback disagrees with common history;
- retained loss outcomes do not restore normalization.

## Disposition

The optical crossing is mathematically feasible but spectrally rigid. The experimental search is now for a physical degree of freedom whose measured transfer family supplies the disjoint joint level sets \(\Omega_j\) and whose detector coupler satisfies the history pullback. Abstract mode partitioning cannot serve as evidence for that identification.
