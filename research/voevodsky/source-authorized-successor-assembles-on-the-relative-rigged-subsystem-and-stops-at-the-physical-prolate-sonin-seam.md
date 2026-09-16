# Source-authorized successor assembles on the relative rigged subsystem and stops at the physical prolate--Sonin seam

## Question

Can the previously separated conductor, packet, cutoff, and cycle-port
transitions be assembled into one source-authorized stage map on the rigged
observer graph?

## Common stage index

Use the directed index

\[
\iota=(L,n,F,N),
\]

where:

- \(L\) is radial/cutoff placement after common recentering;
- \(n\) is dyadic Halmos refinement depth;
- \(F\) is conductor truncation;
- \(N\) is the initial arithmetic edge/observer cutoff.

Admissibility retains the existing inequality \(L\geq F+C_S\), and the order is
coordinatewise. The prior joint-cutoff theorem proves this region is directed.

## Source object and successor

Let

\[
E_\iota=
\mathcal D_S^{(F)}\cap E_N
\]

with the projective arithmetic edge coordinate and the global Tate form-domain
coordinate both retained. For \(\iota\preceq\iota'\), define

\[
U_{\iota'\iota}:E_\iota\longrightarrow E_{\iota'}
\]

as the composite of the source inclusions:

1. conductor spectral inclusion \(Z_F\leq Z_{F'}\);
2. observer/edge initial-cutoff inclusion \(P_N\leq P_{N'}\);
3. dyadic defect refinement;
4. common radial recentering transport.

These operations commute on their shared declared domains:

- conductor projections commute with the Tate connection and radial Mellin
  recentering;
- global Tate legs restrict rather than being recomputed packetwise;
- dyadic functional calculus commutes with unitary recentering;
- the greedy forest is inherited by initial edge cutoffs.

Hence the order of the four generating successor moves does not affect the
result. The maps obey

\[
U_{\iota''\iota'}U_{\iota'\iota}=U_{\iota''\iota}.
\]

This constructs a strict directed source system on the relative subsystem.
Only the recentering component is invertible at fixed support; conductor,
packet, and cutoff inclusions are generally one-way.

## Relative observer

Define

\[
\mathcal O_\iota^{\rm rel}=
\left(
\Phi_{S,F}^{\rm boundary}|_{E_N},
D_0M_{(-)},
\widehat Z_DP_N
\right).
\]

Its three components are respectively:

1. the globally defined positive/negative Tate boundary legs;
2. the recentered trace-ideal relative cutoff boundary;
3. the projective cycle/chord port.

Let \(T_{\iota'\iota}^{\rm rel}\) be ordinary inclusion on the global Tate
legs, stationary identification on the recentered relative boundary, and chord
truncation/inclusion on the cycle presentation as appropriate. The prior exact
identities give

\[
\boxed{
T_{\iota'\iota}^{\rm rel}\mathcal O_\iota^{\rm rel}
=
\mathcal O_{\iota'}^{\rm rel}U_{\iota'\iota}.}
\]

Thus seam naturality is already available on this relative rigged subsystem.
Lifting to observer graphs gives strict maps

\[
\widetilde U_{\iota'\iota}
=g_{\iota'}U_{\iota'\iota}g_\iota^{-1}.
\]

## Why this is not yet the full C14 seam

The physical fourth presentation contains the unrecentered ordered cutoff pair,
its moving volume/placement term, and the Sonin eigenvalue-one intersection.
The relative observer deliberately removes or separates those pieces.

The missing physical comparison is an intertwiner from orthogonally
bulk-removed prolate residuals to the global Tate multiplication legs:

\[
R_{\Lambda,\pm}g
\longrightarrow
R_{S,\pm}\mathcal M_Sg,
\]

including a typed image for

\[
P_{\{1\}}(B_\Lambda).
\]

No combination of conductor commutation, recentering stationarity, or cycle
faithfulness supplies that intertwiner. Consequently the assembled theorem is
not a proof that the original scalar finite-part C14 map is an equivalence and
not a proof of physical full-turn monodromy.

## Exact obstruction object

Define the physical seam residual formally by

\[
\mathfrak R_{\iota'\iota}
=
T^{\rm phys}_{\iota'\iota}\mathcal O^{\rm phys}_\iota
-
\mathcal O^{\rm phys}_{\iota'}U_{\iota'\iota}.
\]

Every already constructed relative component of \(\mathfrak R\) is zero. Its
support is confined to:

1. the moving ordered prolate placement/volume component;
2. the prolate-to-Tate bulk-removal comparison;
3. the Sonin/intersection atom;
4. endpoint channels present only in the globally completed explicit formula.

This is the source-authorized seam frontier. Future work should not recheck
conductor, packet, recentering, or projective cycle naturality unless the
underlying definitions change.

## Consequence for the helix

On the relative rigged subsystem, the four presentation phases admit a strict
directed full-turn successor. A genuine reversible monodromy can occur only on
a subcategory where every generating inclusion is replaced by a bicontinuous
identification or by passage to a two-sided completed system.

For the physical helix, the relation

\[
\tau^4=U
\]

remains conditional precisely on vanishing of \(\mathfrak R\) in the four
listed residual channels.

## Verdict

Prior source dynamics do assemble:

\[
\boxed{
\text{strict successor and seam naturality on the relative rigged subsystem}.}
\]

The first unconstructed datum is now sharply localized: a source-derived
physical prolate-to-Tate/Sonin seam intertwiner. This, rather than another
finite coherence enumeration, is the next mathematical gate.
