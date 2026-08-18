---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Physical G12 Residue Lands in a Labelled Pair of Four-Pole Families

## Scope correction

Entry 589 correctly limits Entries 580--587 to the canonical three-pole
subpacket.  The same qualification applies to Entry 588: its exact Kummer
connection identifies the proper quotient of

\[
H_{21}^{(g_1,g_2,G_{12})},
\]

not yet the complete physical (q_{G_{12}}) source summand.  The algebra and
connection formula of Entry 588 remain valid with this corrected scope.

## Literal physical residue

The two source terms containing (q_{G_{12}}) have denominator sets

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{23}}\},
\]

and

\[
\{q_{g_1},q_{g_2},q_{g_3},q_{G_{12}},q_{g_{31}}\}.
\]

With fiber orientation (dc\wedge da\wedge db), use

\[
q_{G_{12}}=c+x+y+z.
\]

Since \(\partial q_{G_{12}}/\partial c=1\), its Poincare residue has no fitted
Jacobian or sign.  Substitution (c=-E) gives

\[
\begin{aligned}
q_{g_1}&=b-y-z, & q_{g_2}&=a-x-z,\\
q_{g_3}&=a+b+z, & q_{g_{23}}&=b-x,\\
&&q_{g_{31}}&=a-y.
\end{aligned}
\]

Therefore the denominator-level residue is canonically typed as

\[
\boxed{
\operatorname{Res}_{q_{G_{12}}}
:
\text{physical five-pole pair}
\longrightarrow
M_{123,23}\oplus M_{123,31},
}
\]

with the source-prescribed combination of the two labelled summands.  It is
not a map into the three-pole rank-twenty-one packet.

## Consequence

This establishes the correct carrier-level comparison object required by
Entry 589.  The (g_{23}) summand is exactly the rank-34 lower family already
censused in Entry 545; its (g_{31}) partner is the occurrence-reflected
family.  The labels must remain distinct because their final residual walls
are respectively

\[
b=x,qquad a=y.
\]

No projection to the nine-master infinity-Gysin sequence is yet defined.
The next calculation must construct the induced source-master image of this
labelled residue pair and only then test its intersection with the rank-seven
algebraic kernel and rank-two elliptic quotient.

## Evidence

- `research/benincasa/physical_five_pole_g12_residue.py`;
- `research/benincasa/physical-five-pole-g12-residue.json`;
- frozen source equation `eq:Triangle`;
- Entries 545, 588, and 589.

## Outcome contract

~~~json
{
  "claim": "The complete physical q_G12 residue lands in the canonical three-pole rank-twenty-one packet.",
  "status": "falsified",
  "residue_jacobian": 1,
  "target_summands": [
    ["q_g1", "q_g2", "q_g3", "q_g23"],
    ["q_g1", "q_g2", "q_g3", "q_g31"]
  ],
  "residual_occurrence_walls": ["b=x", "a=y"],
  "three_pole_kummer_result_retained": true,
  "three_pole_physical_completeness_withdrawn": true,
  "next_experiment": "Construct the source-master image of the labelled four-pole residue pair and compare it functorially with the nine-master infinity-Gysin sequence."
}
~~~
