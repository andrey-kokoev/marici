# Run-2 production-rate reach: WP463

## Question

Does the positive rate portal of WP462 have enough source-supported event yield to become an executable second coordinate in the ATLAS full Run-2 dijet experiment?

## Frozen collider packet

Use the source and detector choices before evaluating reach:

- triplet mass (m_1=5 TeV) and proton energy (sqrt(s)=13 TeV);
- WP461's conservative kaon-conditioned coupling endpoint;
- the ATLAS full Run-2 integrated luminosity of (139 inverse femtobarns);
- the `NNPDF23_lo_as_0130_qed` set used by the ATLAS signal-simulation family, member zero and all 100 Monte Carlo replicas;
- factorization scale (Q=m_1);
- the source-required ordered channels (d anti-s), (anti-s d), (s anti-d), and (anti-d s);
- leading-order narrow-width production, inclusive quark-jet decay, and unit acceptance as an intentionally optimistic reach ceiling.

The PDF archive is fetched from the official LHAPDF set repository and checked against SHA-256 digest `60d3c1df1c31e5840f91f4217163ae30a256b9291a5adc894882e86607ef5d63`. The pure-Python `parton` 0.2.2 reader evaluates the grids. No PDF normalization is fitted to the ATLAS limit.

## Source-to-rate map

For each charge-conjugate entrance channel, WP462's positive residue gives half of the summed entrance width. In the declared color-singlet spin-one narrow-width convention, summing the four ordered proton channels gives

\[
\sigma(pp\to V_1\to jj)
=\frac{\pi g_F^2}{4s}\mathcal L_{d\bar s+s\bar d}(\tau,Q^2),
\qquad
\tau=\frac{m_1^2}{s}.
\]

The conversion (1 inverse GeV squared equals 389379365.6 picobarns) is frozen numerically. Showering and acceptance can only lower this unit-acceptance ceiling.

The evaluated luminosities are

\[
\mathcal L_0=0.0011785691192713744
\]

for the central member, and

\[
\max_{1\ldots100}\mathcal L=0.006117350025077182
\]

for the most favorable replica. The replica standard deviation is about (0.00076125), demonstrating a large high-x flavor uncertainty; WP463 therefore uses the maximum replica for its hostile reach test.

## Event ceiling and experimental comparison

At WP461's conditional coupling endpoint, the unit-acceptance cross sections are approximately

\[
\sigma_0=1.91\mathbin{\cdot}10^{-6}\ {\rm fb},
\qquad
\sigma_{\rm replica\ max}=9.90\mathbin{\cdot}10^{-6}\ {\rm fb}.
\]

The corresponding produced-event ceilings in the full Run-2 luminosity are

\[
N_0=2.65\mathbin{\cdot}10^{-4},
\qquad
N_{\rm replica\ max}=1.38\mathbin{\cdot}10^{-3}.
\]

The [ATLAS full Run-2 search](https://arxiv.org/abs/1910.08447) quotes generic Gaussian effective-cross-section limits reaching (0.08 to 0.2 fb) at 6 TeV. Even comparing to the optimistic lower endpoint (0.08 fb), the maximum-replica source ceiling is smaller by a factor above 8000. The exact 5 TeV acceptance cannot repair this deficit because the calculation already grants unit acceptance.

## Contextual partition and disposition

The rate map is algebraically faithful for positive (g_F) when a nonzero parton luminosity is available. On the actual Run-2 counting domain, however, every kaon-allowed point produces much less than one expected event and is operationally equivalent to background-only. The first nonfaithful arrow is finite luminosity/counting support, not the source residue, PDF channel, or detector mass resolution.

WP463 is a negative current-instrument reach result. It neither selects (g_F f/v) nor rigidifies a presentation. No reference port is used.

## Smallest exact falsifiers

- either positive production weight vanishes;
- an official PDF replica yields enough unit-acceptance events to reach one;
- the source ceiling exceeds the most optimistic quoted generic limit;
- the claimed rate sensitivity relies on an initial state other than the source-authorized flavor-changing channels.

A future collider can reopen the route only with enough energy and luminosity to make the source-specific yield non-negligible; luminosity alone would require an increase of hundreds to thousands merely to approach one produced event at this benchmark.
