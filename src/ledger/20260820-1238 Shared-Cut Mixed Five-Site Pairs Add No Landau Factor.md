# Entry 1238 — Shared-Cut Mixed Five-Site Pairs Add No Landau Factor

## Source-present class

Among Entry 1236's compatible pairs, consider a one-cut wall and a connected-region wall that share the cut occurrence \(i\):

\[
q_e=5t+2y_i,
\qquad
q_A=mt+y_i+y_j,
\qquad m=|A|.
\]

The frozen census contains eight free \(C_5\)-orbits of this type, or 40 labelled pairs.

## Wall equations

On their common zero locus,

\[
y_i=-\frac52t,
\qquad
y_j=\frac{5-2m}{2}t.
\]

Let \(n_i\) and \(n_j\) denote the signed unit gradients of the two roots. Pair stationarity has the form

\[
(2\alpha+\beta)n_i+\beta n_j=0.
\]

For a genuine two-wall pinch, this forces

\[
n_j=\sigma n_i,
\qquad \sigma\in\{+1,-1\}.
\]

## Routing geometry

The difference between the two labelled routing foci is the region resultant \(P_A\). Hence

\[
P_A^2=(y_i-\sigma y_j)^2.
\]

For \(\sigma=-1\), this gives

\[
P_A^2=m^2t^2.
\]

For \(\sigma=+1\), it gives

\[
P_A^2=(5-m)^2t^2.
\]

These are exactly the one-wall threshold equations for \(A\) and its connected complement \(A^c\), respectively.

## Result

Therefore

\[
\boxed{
\text{the eight shared-cut }M1+A_m\text{ pair orbits add no new nonzero-}t\text{ factor.}
}
\]

Together with Entry 1237, 15 of the 49 compatible pair orbits are now classified against new nonzero-\(t\) support. This does not remove the shared-cut pairs from the Landau complex; it identifies their projected support with already frozen one-wall divisors.

## Scope

The result does not apply to the six disjoint-cut \(M1+A_m\) orbits. Their stationarity involves three distinct routing foci and may produce a genuine anomalous threshold.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_mixed_pair_landau_overlap.rs`
- `research/benincasa/results/five-site-mixed-pair-landau-overlap.json`

## Next falsifier

Derive the three-focus elimination for the six disjoint-cut \(M1+A_m\) representatives. Preserve the exact labelled routing Gram data and signed roots. Test whether each elimination factor belongs to the existing one-wall/Gram carrier or defines new coefficient support.
