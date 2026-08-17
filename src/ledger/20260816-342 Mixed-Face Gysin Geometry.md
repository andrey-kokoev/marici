---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Mixed-Face Rank-One Grades Are Conductor Graph Cohomology

## Question

Entries 340--341 left two proper mixed grades

\[
m_{101}=m_{110}=1
\]

and proposed constructing their connection to the
\(q_{\mathcal G_{12}}\)-only rank-nine module.

The frozen geometry gives a sharper answer:

\[
\boxed{
\text{both mixed grades are rank-one conductor graph cohomology on
source-defined reducible wall curves.}
}
\]

It also corrects the proposed map direction. There is no canonical direct
map from either wall \(H^1\) class into the absolute rank-nine \(H^2\)
module.

## Frozen residue surface and walls

Take the \(q_{\mathcal G_{12}}\)-residue surface

\[
S_E:\qquad w^2=K_E(a,b),
\qquad c=-E,
\qquad E=x+y+z.
\]

The two lower denominators cut the source walls

\[
W_1:\quad b=y+z,
\]

\[
W_2:\quad a=x+z.
\]

These are precisely the physical \(cb--=q_{\mathfrak g_1}\) and
\(ca--=q_{\mathfrak g_2}\) lines already present in the frozen signed-face
census of entry 161.

## Exact square restrictions

Put \(a=t\) on \(W_1\). Exact symbolic expansion gives

\[
K_E(t,y+z)=R_1(t)^2,
\]

where

\[
\begin{aligned}
R_1(t)={}&xt^2-z^3-yz^2+y^2z+y^3\\
&-2xz^2-2xyz-xy^2-x^2z-x^2y.
\end{aligned}
\]

Put \(b=t\) on \(W_2\). Then

\[
K_E(x+z,t)=R_2(t)^2,
\]

where

\[
\begin{aligned}
R_2(t)={}&yt^2-z^3-2yz^2-y^2z-xz^2\\
&-2xyz-xy^2+x^2z-x^2y+x^3.
\end{aligned}
\]

Both identities are exact over \(\mathbb Z[x,y,z,t]\). Equivalently, the
quadratic discriminant after writing each quartic as a polynomial in
\(u=t^2\) is identically zero.

These square identities were already latent in the broader twelve-face
audit. The new point is that the deletion cube selects these two physical
walls and explains their proper rank-one grades.

## Normalization and the rank-one class

Upstairs on \(S_E\),

\[
W_i=C_i^+\cup C_i^-,
\qquad
C_i^\pm:\quad w=\pm R_i(t).
\]

Generically \(R_i\) has two distinct roots. Thus \(C_i^+\) and \(C_i^-\)
are two affine-line normalization components meeting at two conductor
nodes.

The dual graph is

\[
\bullet
\mathrel{\substack{\displaystyle\longleftrightarrow\\[-2mm]
                   \displaystyle\longleftrightarrow}}
\bullet,
\]

with two vertices and two edges. Hence

\[
b_1=2-2+1=1.
\]

More invariantly, the normalization sequence contains

\[
H^0(C_i^+)\oplus H^0(C_i^-)
\longrightarrow
H^0(N_i^+)\oplus H^0(N_i^-)
\longrightarrow
H^1(W_i)
\longrightarrow0.
\]

In constant bases the first map is

\[
(u,v)\longmapsto(u-v,u-v).
\]

Its cokernel has rank one. Therefore

\[
\boxed{
\operatorname{rank}H^1(W_i)=1,
}
\]

and this exactly accounts for

\[
m_{101}=m_{110}=1.
\]

The generator is the difference of the two node occurrences. It is
deck-odd/polarity-sensitive Tate data, not elliptic period data.

## Residual coefficient support

Write

\[
R_1(t)=xt^2+D_1,
\qquad
R_2(t)=yt^2+D_2.
\]

The two node discriminants are

\[
\Delta_{W_1}=-4xD_1,
\qquad
\Delta_{W_2}=-4yD_2.
\]

Thus the normalization graph degenerates only when a root moves to infinity
or the two finite conductor nodes collide:

\[
xD_1=0
\quad\text{or}\quad
yD_2=0.
\]

These loci are resultants of the already frozen wall and Cayley--Menger
branch geometry. They are coefficient support; they are not new carrier
incidence generators.

The second wall is obtained from the first by \(x\leftrightarrow y\).

## Compatibility with the top class

Let

\[
\Lambda=E(-x+y+z)(x-y+z).
\]

At the intersection of the two source walls,

\[
R_1(x+z)=R_2(y+z)=-\Lambda.
\]

Therefore, away from \(\Lambda=0\),

\[
C_1^+\cap C_2^+=\{P_+\},
\qquad
C_1^-\cap C_2^-=\{P_-\},
\]

while the cross-sheet intersections are empty. The two points lie over the
triple point of entry 341 with

\[
w(P_\pm)=\mp\Lambda.
\]

This realizes the top \(111\) occurrence class as the same-sheet
intersection datum of the two mixed conductor curves. Its degeneration
\(\Lambda=0\) reproduces exactly the existing-energy support found in entry
264.

## Type correction: no direct map into \(\mathcal M_q^{(9)}\)

The mixed class lives in wall cohomology

\[
H^1(W_i;\mathcal K|_{W_i})(-1).
\]

The frozen localization sequence is

\[
H^2(S_E;\mathcal K)
\longrightarrow
H^2(S_E\setminus W_i;\mathcal K)
\longrightarrow
H^1(W_i;\mathcal K|_{W_i})(-1)
\longrightarrow
H^3(S_E;\mathcal K).
\]

Since

\[
\mathcal M_q^{(9)}
\subset H^2(S_E;\mathcal K),
\]

the canonical continuation of the wall residue points toward \(H^3(S_E)\),
not backward into \(\mathcal M_q^{(9)}\).

Hence

\[
\boxed{
\text{there is no canonical frozen arrow }
H^1(W_i)(-1)\longrightarrow\mathcal M_q^{(9)}.
}
\]

This agrees with entry 326. A direct arrow would require a splitting of
localization, a contracting homotopy, or a separately derived physical
relative-realization map.

The divisor classes

\[
[C_i^+]-[C_i^-]\in H^2(S_E)
\]

are legitimate \(H^0\)-Gysin classes, but they are not canonically identical
to the \(H^1(W_i)\) residue generator. Conflating them would silently change
cohomological degree.

## Deutsch--Popperian verdict

The tested conjecture was

\[
\boxed{
\text{a mixed-face extension requires a singular support or incidence map
outside the frozen arrangement.}
}
\]

At the level now computed, it is falsified:

- both walls are source denominator lines;
- both pullbacks split by exact Cayley--Menger square roots;
- both rank-one grades are conductor graph cohomology;
- their residual discriminants are derived from the frozen wall/branch
  geometry;
- the top class is their occurrence-resolved same-sheet intersection.

No new carrier datum appears.

However, the stronger claim that the mixed classes map canonically into the
absolute rank-nine module is itself false by type. The unresolved object is
the localization extension, not a missing projector.

## Classification

\[
\boxed{
\begin{array}{c|c}
\text{structure} & \text{home}\\
\hline
W_1,W_2 & \text{existing denominator walls}\\
C_i^\pm & \text{normalization of frozen wall pullback}\\
H^1(W_i) & \text{rank-one Tate/conductor coefficient data}\\
xD_1,\ yD_2 & \text{coefficient discriminant support}\\
P_\pm & \text{occurrence-resolved top intersection}\\
\text{new carrier datum} & \text{none}
\end{array}
}
\]

## Limits

This result does not determine:

- the localization boundary
  \(H^1(W_1)\oplus H^1(W_2)\to H^3(S_E)\);
- whether the relative extension splits;
- a coordinate of either wall class in the nine-master basis;
- the physical relative-chain pairing;
- simultaneous degeneration at soft, signed-energy, or conductor loci.

## Exact evidence

- research/benincasa/marici-gm/src/bin/elliptic_top_support_geometry.rs;
- research/benincasa/elliptic-mixed-face-geometry.json;
- entry 161 and research/benincasa/check_marked_relative_q.rs for the frozen
  signed-face census;
- entry 326 for the localization type gate;
- entries 340--341 for the exact ranks and top incidence.

## Next hostile falsifier

Construct the normalization/conductor square for

\[
W_1\cup W_2\subset S_E
\]

and compute the actual localization boundary

\[
H^1(W_1)\oplus H^1(W_2)
\longrightarrow
H^3(S_E),
\]

including the two same-sheet intersection points \(P_\pm\).

The finite falsifier is:

\[
\boxed{
\text{the relative extension cannot be generated by the frozen conductor
square and requires a new incidence object.}
}
\]

Only that failure would justify a new cosmological carrier primitive.

## Outcome contract

~~~json
{
  "claim": "A mixed-face extension requires singular support or incidence outside the frozen arrangement.",
  "status": "falsified_at_wall_geometry_level",
  "mixed_proper_ranks": {"101": 1, "110": 1},
  "geometric_home": "H1 of two-component two-node conductor curves",
  "coefficient_type": "rank-one Tate/conductor graph cohomology",
  "direct_map_to_Mq9": false,
  "direct_map_failure_reason": "localization degree/type mismatch",
  "residual_support": ["x*D1=0", "y*D2=0", "Lambda=0"],
  "new_carrier_datum": false,
  "relative_extension_split": "uncomputed",
  "next_problem": "Compute the two-wall normalization/conductor localization boundary."
}
~~~
