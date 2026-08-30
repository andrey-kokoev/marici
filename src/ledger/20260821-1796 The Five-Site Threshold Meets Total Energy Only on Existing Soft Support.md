# 1796 — The Five-Site Threshold Meets Total Energy Only on Existing Soft Support

## Question

Entry 1795 proves that the cyclic slice does not see the total-energy
intersection of the physical \(g_5\) threshold. What carrier stratum can
contain that intersection in the full multivariate family?

## Source-labelled incidence

The first member of the disjoint marked pair is

\[
q_e=E_T+2y_e.
\]

Every point of the threshold closure retains \(q_e=0\). Therefore

\[
(E_T,q_e)=(E_T,2y_e)
\]

and, over characteristic zero,

\[
\boxed{
\overline{\mathscr D}_{g_5}\cap\{E_T=0\}
\subseteq
\{E_T=0,\ y_e=0\}.
}
\]

The coordinate change

\[
(E_T,y_e)\longmapsto(E_T,q_e)
\]

has determinant \(2\), so this is a transverse Cartier identification before
the deeper Landau critical equations are imposed.

## Result

The physical five-site threshold cannot meet a generic total-energy cusp. Its
entire total-energy intersection is confined to the already frozen
total-energy/site-soft carrier corner.

This classifies the carrier incidence only. It does not determine whether
Entry 1792's logarithmic extension specializes trivially, is killed by a soft
character, or leaves a supported coefficient class.

## Architectural consequence

No new carrier divisor or incidence generator is needed at total energy. The
remaining falsifier is entirely coefficient-theoretic:

\[
\psi_{E_T}\psi_{y_e}\mathcal V_{g_5}.
\]

## Next falsifier

Compute the completed Landau/Morse normal form at
\(E_T=y_e=0\), retain the source \(i0\) orientation, and compare its iterated
nearby cycles with the existing total-energy and site-soft maps.

## Evidence

- research/benincasa/checkers/five_site_g5_total_energy_soft_incidence.py
- research/benincasa/results/five-site-g5-total-energy-soft-incidence.json
- allocator claim: seqclaim-fd2b278ba0903665e41cb624
