# Seam Placement Is Governed by Transfer Current, Not Connectivity

Let \(L\) be the positive grounded Laplacian of an anchored graph. Let \(h\)
represent the anchor-to-target difference and \(b\) the incidence vector of a
candidate seam edge. Define

\[
R=h^*L^{-1}h,
\qquad
r_b=b^*L^{-1}b,
\qquad
\tau=b^*L^{-1}h.
\]

Adding seam conductance \(t\) gives the rank-one update

\[
L_t=L+tbb^*.
\]

Sherman–Morrison yields the exact target-resistance law

\[
R_t
=R-rac{t|\tau|^2}{1+tr_b}.
\]

For a fixed state \(u\) with original energy \(E=u^*Lu\) and seam gradient
\(g=b^*u\),

\[
E_t=E+t|g|^2.
\]

Therefore the first-order change of the target certificate is

\[
\left.\frac d{dt}(R_tE_t)\right|_{t=0}
=R|g|^2-E|\tau|^2.
\]

The seam improves the certificate initially exactly when its normalized
transfer-current leverage exceeds its normalized state-gradient cost:

\[
\frac{|\tau|^2}{R}
>
\frac{|g|^2}{E}.
\]

Connectivity or resistance reduction alone does not decide this comparison.

## Smallest worsening hostile

On the chain \(0-1-2\), anchor \(0\), target \(2\), duplicate the edge
\(0-1\) with conductance \(t\). For the state

\[
u=(1,0,0),
\]

the original target resistance and energy are both

\[
R=2,
\qquad E=1.
\]

The added edge has \(r_b=1\), \(\tau=1\), and \(|g|=1\). Thus the initial
score is positive:

\[
R|g|^2-E|\tau|^2=1.
\]

In fact,

\[
R_t=1+\frac1{1+t},
\qquad
E_t=1+t,
\qquad
R_tE_t=2+t.
\]

The graph becomes better connected while the target certificate becomes
worse.

For the same state, a direct anchor-to-target seam has negative score and
decreases the product monotonically toward the true endpoint defect one. For
the state \((1,1,0)\), the \(0-1\) candidate has zero gradient and therefore
improves the certificate. Seam value is state- and target-dependent.

## Source-authority consequence

A control-theoretic or graph optimizer may rank a frozen list of authorized
seam rows using \((r_b,\tau,g)\). It may not invent a new edge because it has
a favorable score. Nor may it choose the seam after inspecting a prohibited
state coordinate: a usable design requires source-accessible bounds or a
worst-case certificate over the admitted state class.

The direct anchor-target seam is exceptional because the resistance inequality
guarantees nonincrease for every state. Arbitrary seam rows have no such
universal monotonicity.

## Theta/Tate consequence

Grothendieck should type each seam/current candidate by:

\[
(r_b,\tau,g)
=
(\text{self-resistance},\text{target transfer current},
\text{state gradient}).
\]

This decides whether the row improves the specific scalar normalization
certificate once its energy cost is included. Merely proving that a seam
connects the tail graph or lowers some resistance is insufficient.

## Falsifiers

- Resistance reduction is evaluated without the added seam energy.
- Seam rows are ranked only by connectivity.
- A state-dependent favorable row is selected using inaccessible state data.
- An unauthorized edge is introduced by the optimizer.
- The universal monotonicity of the direct seam is assigned to arbitrary
  seam placements.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to determine whether the direct-seam monotonicity extends
to arbitrary authorized seam rows.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. It does not: the exact transfer-current score classifies improvement,
and a three-vertex hostile shows connectivity can increase while the target
certificate worsens.
