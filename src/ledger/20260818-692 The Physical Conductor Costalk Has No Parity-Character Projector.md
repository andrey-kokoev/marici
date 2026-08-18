---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 692 — The Physical Conductor Costalk Has No Parity-Character Projector

## Hard-to-vary claim

The normalization-sheet character of the physical \(g_3\) conductor
costalk cannot be matched to one of the
\(C_2^{(a)}\times C_2^{(b)}\) character blocks of the absolute
nine-master module. The physical wall has trivial stabilizer under that
parity group, and the involution \(w\mapsto-w\) is a different action.

Therefore character multiplicities do not select a canonical line inside
the rank-seven infinity-Gysin kernel.

## Absolute parity decomposition

The source master representatives have fiber parities

\[
\begin{array}{c|c}
\text{parity}&\text{masters}\\
\hline
(1,1)&e_1\\
(1,0)&e_2,e_3\\
(0,1)&e_4,e_5\\
(0,0)&e_6,e_7,e_8,e_9.
\end{array}
\]

The infinity-Gysin kernel consequently has multiplicities

\[
(1,2,2,2)
\]

under the sign changes of \(a\) and \(b\).

## Physical-wall stabilizer

The source wall is

\[
q_{g_3}=a+b+z.
\]

Its orbit under \((a,b)\mapsto(\epsilon_a a,\epsilon_b b)\) is

\[
\begin{aligned}
a+b+z,qquad
a-b+z,qquad
-a+b+z,qquad
-a-b+z.
\end{aligned}
\]

At generic \(z\ne0\), these are four distinct affine walls. Hence

\[
\boxed{
\operatorname{Stab}_{C_2^{(a)}\times C_2^{(b)}}(q_{g_3})=\{1\}.
}
\]

The physical costalk on one wall therefore does not carry a character of
the absolute parity group.

## Distinct involutions

Entry 689 finds that the oriented costalk is anti-invariant under exchange
of the two normalization sheets

\[
w=\pm R_3(b).
\]

This is the hyperelliptic/coefficient involution

\[
w\longmapsto-w,
\]

not either of the base-coordinate sign changes

\[
a\longmapsto-a,
\qquad
b\longmapsto-b.
\]

Equating them would smear two distinct actions and manufacture a projector.
Thus

\[
\boxed{
\text{the Entry-689 costalk character does not canonically select a
summand of }\mathcal T_7.
}
\]

## Consequence

The character shortcut proposed at the end of Entry 689 is rejected. A
canonical connecting class, if present, must be obtained from the
nonequivariant local Gysin morphism for the actual source wall. Completing
the wall to its four-element parity orbit solely to recover equivariance is
also prohibited: the additional walls are not part of the frozen physical
residue object.

## Classification

- rank-seven parity decomposition: valid for the absolute module;
- physical conductor sheet character: valid for the normalized wall;
- identification of those characters: ill-typed;
- canonical algebraic target line: not selected;
- new carrier datum: none;
- next admissible mechanism: oriented local Gysin connecting morphism.

## Next falsifier

Compute the local Gysin boundary of the normalized \(g_3\) wall directly
as a two-form/current on the surface, reduce it against the frozen
nine-master exact complex, and test whether the resulting class is
independent of tubular coordinate and primitive choice. Only that
choice-independent class may be placed in \(\mathcal T_7\).

## Evidence

- `research/benincasa/check_g3_costalk_character_typing.py`;
- `research/benincasa/g3-costalk-character-typing.json`;
- Entries 150, 685, and 689;
- allocator claim `seqclaim-b99badbf2effc516515e86e4`.

## Outcome contract

~~~json
{
  "claim": "The anti-invariant normalization-sheet character canonically selects one parity-character line inside the rank-seven algebraic Gysin kernel.",
  "status": "falsified",
  "physical_wall_stabilizer_order": 1,
  "normalization_involution_equals_base_parity": false,
  "canonical_T7_line_selected": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute the nonequivariant oriented local Gysin boundary and reduce it in the frozen exact complex."
}
~~~
