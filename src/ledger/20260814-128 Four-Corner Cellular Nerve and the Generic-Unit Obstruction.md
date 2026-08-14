# Four-Corner Cellular Nerve and the Generic-Unit Obstruction

## Record

Date: 2026-08-14

Status: proved integral pre-Cousin cellular descent; falsified reconstruction
of the complete entry-97 road trace from corner local-cohomology objects
alone. The obstruction is support and variance, not torsion.

This entry tests the four-corner experiment proposed in entry 121. It does
not invalidate the \(v_{10}\) corner residue proved there. It identifies the
additional generic and codimension-one data required to place that residue
inside the complete road object.

## Claim

Let

\[
V=\{00,10,01,11\}
\]

be the four vertices of the weighted road square \(Q\). For each vertex
\(v\), let

\[
A_v=\mathbb D(Q/B_v)\subset\mathbb D(Q)
\]

be the corresponding corner dual, and for nonempty \(J\subseteq V\) set

\[
A_J=\bigcap_{v\in J}A_v.
\]

Before applying any target Koszul--Cech functor, the full augmented
intersection nerve

\[
\boxed{
0\longrightarrow A_V
\longrightarrow\!\!\bigoplus_{|J|=3}A_J
\longrightarrow\!\!\bigoplus_{|J|=2}A_J
\longrightarrow\!\!\bigoplus_{v\in V}A_v
\longrightarrow\mathbb D(Q)
\longrightarrow0
}
\]

is degreewise split exact over \(\mathbb Z\).

Cell by cell, this is the augmented simplex on the set of corners containing
that cell:

- a vertex belongs to one corner;
- an edge belongs to its two endpoint corners;
- the face belongs to all four corners.

On the face line the nerve is

\[
\mathbb Z\longrightarrow\mathbb Z^4
\longrightarrow\mathbb Z^6
\longrightarrow\mathbb Z^4
\longrightarrow\mathbb Z,
\]

with differential ranks \((1,3,3,1)\) and only unit Smith factors. The full
normalized totalization has ranks

\[
(1,12,14,4)
\]

in degrees \((-1,0,1,2)\), differential ranks \((1,10,4)\), and

\[
H^\bullet=(0,\mathbb Z,0,0).
\]

Thus the cellular nerve reconstructs \(\mathbb D(Q)\) integrally, with no
hidden torsion or denominator.

The higher intersections are essential. On the face-overlap row, keeping
only the four adjacent pairs leaves the primitive harmonic cycle

\[
a+d-b-c.
\]

The coupled adjacent-only totalization is acyclic, so it loses the generic
rank-one class rather than reconstructing it. Keeping all six pairs but
omitting triples and the quadruple leaves three free classes on the face row
and two free classes in the coupled totalization. Neither truncation is a
Cech cover of the cellular object.

## Failure after corner Koszul--Cech realization

The four corner support ideals are

\[
\begin{aligned}
I_{00}&=(x_0,x_3),&
I_{10}&=(x_1,x_3),\\
I_{01}&=(x_0,x_4),&
I_{11}&=(x_1,x_4).
\end{aligned}
\]

The cellular intersections above are not sent to ordinary
Mayer--Vietoris intersections of these supports. For example,

\[
I_{00}+I_{10}=(x_0,x_1,x_3),
\qquad
I_{00}\cap I_{10}=(x_3,x_0x_1).
\]

Hence

\[
V(I_{00})\cap V(I_{10})=V(x_0,x_1,x_3)
\]

and

\[
V(I_{00})\cup V(I_{10})=V(x_3,x_0x_1).
\]

Neither is the road-edge support \(V(x_3)\). The map from the shifted
one-normal road object to the two corners is a Gysin/residue map, carrying
the missing \(1/x_0\) and \(1/x_1\) factors and the normal orientation. It
has the opposite variance from an ordinary restriction map.

The total corner support is

\[
\boxed{
\bigcup_vV(I_v)
=V\!\left(\bigcap_vI_v\right)
=V(x_0x_1,x_3x_4).
}
\]

It is a proper closed subset. Every totalization made solely from these
corner local-cohomology objects and their supported intersections remains
supported there and becomes zero after Laurent localization. The complete
entry-97 road trace instead remains the nonzero normalized \(H^0\)
augmentation on the Laurent torus.

Therefore

\[
\boxed{
\operatorname{Tot}_{v}
R\Gamma_{I_v}\mathbb D(Q)
\not\simeq
\Theta_{03}^{\rm loc}
}
\]

for any interpretation using only the four corner supports and road-edge
local cohomologies. The exact supported Mayer--Vietoris nerve reconstructs
at most

\[
R\Gamma_{(x_0x_1,x_3x_4)}\mathbb D(Q),
\]

not the absolute road object or its generic unit.

## The distinct lcm open descent

There is a second, valid construction which must not be confused with the
supported corner residues. Put

\[
m_{00}=x_0x_3,\quad
m_{10}=x_1x_3,\quad
m_{01}=x_0x_4,\quad
m_{11}=x_1x_4.
\]

The principal opens \(D(m_v)\) cover

\[
U_{\rm lcm}
=\operatorname{Spec}R
\setminus\bigl(V(x_0,x_1)\cup V(x_3,x_4)\bigr).
\]

The ordinary functions \(1/m_v\) are unequal on overlaps. They do glue as
coordinates of the dual principal-line system: on an overlap use

\[
g_{vw}=m_w/m_v.
\]

After multiplying by the loaded frame \(m_v\), every local value is the unit
one. The transition cocycle is integral and the complete overlap nerve is
the full \(3\)-simplex, including both diagonal, all triple, and the
quadruple overlaps.

This recovers the normalized generic principal-line section on
\(U_{\rm lcm}\). It does not recover a corner residue. Restricting the
extended Cech complex for \(I_v=(x_i,x_j)\) to \(D(m_v)\) makes that supported
complex acyclic. Replacing it by the visible top fraction \(1/m_v\) discards
the forced one-variable terms and is not a chain map.

## Evidence

Exact certificate:

- research/voevodsky/check_d03_four_corner_descent_obstruction.rs,
  SHA-256 74a2bcc8ae97be715f65cdb6ec2a444bd0271ae7db91a7365d0f6955c29b3ce9.

The certificate verifies every cellular intersection, the full nerve and
its Smith data, the truncated-nerve free classes, the four monomial-support
calculations, the principal-lcm transition cocycle, and the Laurent
localization negative control.

Reproduce with rustfmt --edition 2021 --check, compile with
rustc --edition=2021 -D warnings -O, and execute the resulting binary. Its
stdout is the structured result packet.

## Boundary

The no-go is scoped. It rules out deriving the absolute road trace from the
supported corner residues by ordinary four-chart descent. It does not rule
out:

- the entry-121 \(v_{10}\) residue;
- the split-exact cellular corner nerve before Koszul--Cech realization;
- the generic principal-line section on \(U_{\rm lcm}\);
- a full generic--edge--corner Cousin or recollement construction.

Entry 38 already supplies the undecorated facewise Pochhammer/Cousin
differential on transverse cells. What is not yet supplied here is the
occurrence-loaded six-functor comparison that places the generic line, road
Gysin terms, and corner residues in one total complex.

## Consequence

The immediate target is no longer a corner-only hypercover. Construct the
occurrence-loaded generic--edge--corner object

\[
\boxed{
\mathcal C_{03}^{\rm occ}
=\operatorname{Tot}\!\left[
\mathbf1_T
\xrightarrow{\operatorname{can/var}}
\bigoplus_{e\subset F_{03}}\mathcal C_e[1]
\xrightarrow{\operatorname{Res}}
\bigoplus_{v\subset F_{03}}\mathcal C_v[2]
\right].
}
\]

The discriminating formula is

\[
\boxed{
\Theta_{03}^{\rm loc}|_T=\mathbf1_T,
\qquad
\operatorname{Res}_{v_{10}}^{\rm Cousin}\Theta_{03}^{\rm loc}
=\Theta_{03,v_{10}}^{\rm corner}.
}
\]

Entry 121 fixes the second component. The first is genuinely generic data
and must arrive through the nonzero \(Q\)-leg of the scalar specialization;
it cannot be inferred from boundary costalks. The next falsifier is a
nonzero obstruction to extending \(\mathbf1_T\) through the road Gysin terms
with the prescribed four corner residues.

## Outcome contract

~~~json
{
  "claim": "The four corner duals form an integral split-exact cellular nerve before target Koszul-Cech realization. After realization, their local-cohomology supports and Mayer-Vietoris variance do not reconstruct the complete road trace; a separate generic unit and the codimension-one Gysin layer are required.",
  "status": "falsified",
  "assumptions": [
    "The falsified claim is the entry-121 proposal that corner local-cohomology descent alone reconstructs the complete entry-97 trace.",
    "The entry-121 individual corner residue remains valid.",
    "Generic and supported Cech objects are kept distinct."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_four_corner_descent_obstruction.rs",
    "ledger entries 38, 97, 120, and 121"
  ],
  "factorization_test": {
    "pre_KC_full_nerve": "split exact, unimodular",
    "normalized_total_homology": "(0,Z,0,0)",
    "adjacent_only_overlap": "one primitive face-row cycle; coupled total acyclic",
    "all_pairs_without_higher": "face-row cycle rank three; coupled H1 rank two",
    "corner_support_union": "V(x0*x1,x3*x4), proper",
    "road_edge_MV_typing": "falsified",
    "Laurent_supported_total": "zero",
    "full_road_trace": "nonzero",
    "lcm_generic_line_descent": "compatible on the full nerve"
  },
  "counterevidence": [
    "The road-edge support V(x3) is neither the supported intersection nor union of the adjacent corner ideals.",
    "All corner-supported complexes vanish on the Laurent torus.",
    "The principal-line functions glue only after retaining their line transitions, and this is generic open descent rather than supported residue descent."
  ],
  "next_experiment": "Construct the occurrence-loaded generic-edge-corner Cousin totalization, derive its can/var and Gysin maps, and test whether the generic unit extends uniquely to the four prescribed corner residues."
}
~~~
