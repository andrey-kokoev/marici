# Vanishing Deformations Remove the Reflection Obstruction

## Result

Entry 387 does more than remove coefficient ambiguity. It also decides the
reflection bit isolated in Entry 141, conditional only on existence of the
underlying connector.

Let \(\mathcal C_{03}\) denote the space of admissible connectors with the
generic, Cartier, lower-Cech, and two endpoint faces frozen. If nonempty,
its components form a torsor under the degree-zero relative deformation
group. Entries 384--387 compute the relevant fine-graded group as

\[
\boxed{D_{03}^{0}=0.}
\]

Consequently

\[
\boxed{
\mathcal C_{03}\text{ is either empty or a singleton up to admissible
homotopy.}
}
\]

This is the precise dichotomy left by the calculations.

## Reflection

Physical reflection \(f_3\) preserves the frozen target faces: Entry 140
proves the target purity square has sign \(+1\), while the orientation
twist of Entries 136 and 143 is already included in the road object.
Therefore, if \(h\in\mathcal C_{03}\), then \(f_3h\) is another element
of the same connector space.

The difference

\[
f_3h-h
\]

is a relative endpoint deformation, hence represents an element of
\(D_{03}^{0}\). Since that group vanishes,

\[
\boxed{[f_3h-h]=0.}
\]

Thus the endpoint defect class from Entry 141 is forced to be

\[
p_{\partial,Q}=0
\in H^1(D_3;\mathbb Z_{\rm or})
\]

whenever the connector exists.

Entry 141 proves that the conductor Bockstein

\[
\partial_{\rm pol}:
H^1(D_3;\mathbb Z_{\rm or})
\xrightarrow{\sim}
H^2(D_3;\mathbb Z)
\]

is an isomorphism. Therefore

\[
\boxed{
\omega_{\rm load}
=\partial_{\rm pol}(p_{\partial,Q})
=0.
}
\]

The previously possible \(\mathbb Z/2\) obstruction does not survive the
literal fine grading.

## What is and is not proved

This does not construct a connector. It proves:

- if no nonequivariant connector exists, the realization fails already at
  the mixed-variance existence step;
- if one exists, it is unique up to the admissible relative homotopy;
- its reflection defect is necessarily zero; and
- it admits the unique loaded equivariant component predicted by Entry 141.

So the remaining frontier is no longer “existence plus a parity choice.”
It is only existence.

## Consequence for the next computation

The rank-nine strict carrier family from Entry 136 should not be searched
for a reflection-preferred point. All those representatives describe the
same unpointed roof before the admissible support and grading constraints.
After the faces are frozen and fine grading is imposed, the connector fibre
has at most one component.

The next test should therefore be a solvability test for

\[
d_{\operatorname{Hom}}h
=i_{\rm road}a\pi-\delta_E\Phi
\]

in the normal-Cech enhanced mixed-variance complex. No parity variable and
no free coefficient should be included. A solution proves the unique
equivariant connector; inconsistency proves a genuine existence
obstruction.

## Evidence

research/voevodsky/check_d03_zero_torsor_reflection_gate.py checks the
zero-torsor and Bockstein implication. Its mathematical inputs are:

- Entry 387: \(D_{03}^{0}=0\);
- Entry 140: target reflection naturality has sign \(+1\);
- Entry 141: the parity-to-loaded-obstruction Bockstein is an isomorphism;
  and
- Entry 136: front/back AW representatives differ by an equivariant
  homotopy and cannot themselves toggle parity.

## Outcome contract

~~~json
{
  "claim": "The fine-graded endpoint-relative deformation group is zero. Hence the admissible connector space is either empty or a singleton up to relative homotopy. If a connector exists, its reflected connector has zero difference class, so p_partial,Q=0 and the Entry-141 loaded Bockstein obstruction vanishes.",
  "status": "proved_conditional_reflection_obstruction_zero",
  "closed": [
    "endpoint coefficient deformation",
    "reflection parity conditional on existence",
    "loaded Z/2 obstruction conditional on existence"
  ],
  "not_closed": [
    "existence of the mixed-variance connector",
    "construction of the normal-Cech enhanced AW collar",
    "full D3 realization",
    "full primal trace"
  ],
  "next_experiment": "Solve the frozen connector equation in the literal normal-Cech mixed-variance mapping complex with no coefficient or parity parameters."
}
~~~
