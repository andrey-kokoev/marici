# Crossed modules give the first genuinely nonabelian edge-face coherence rung

Owner: marici.Kitaev

## Question

Does the tetrahedral filler tower remain genuinely higher after replacing
abelian cochains by ordered noncommutative transport, or does it still reduce
under Carrier duality to an ordinary scalar incidence syndrome?

## Claim boundary

The minimal strict nonabelian coefficient object is a crossed module

\[
\partial:H\to G
\]

with an action

\[
G\curvearrowright H,
\qquad
(g,h)\longmapsto g\triangleright h,
\]

satisfying the two crossed-module laws

\[
\partial(g\triangleright h)
=
g\,\partial(h)\,g^{-1},
\]

and

\[
\partial(h)\triangleright h'
=
hh'h^{-1}.
\]

The first law is equivariance. The second is the Peiffer identity.

Together they define a strict 2-group:

- \(G\) supplies ordered 1-transport;
- \(H\) supplies 2-transport between 1-paths;
- \(\partial\) gives the boundary of a face filler;
- the \(G\)-action transports face fillers between endpoint frames.

This structure survives cellular degree rotation because ordering, action, and
Peiffer compatibility are coefficient data rather than geometric dimension.

### Frozen local convention

Use ordered vertices \(i<j<k\). Assign an edge transport

\[
g_{ij}\in G
\]

and a face filler

\[
h_{ijk}\in H
\]

with convention

\[
g_{ij}g_{jk}
=
\partial(h_{ijk})\,g_{ik}.
\]

Thus \(h_{ijk}\) compares the two-step path \(i\to j\to k\) with the direct path
\(i\to k\).

Equivalently,

\[
\partial(h_{ijk})
=
g_{ij}g_{jk}g_{ik}^{-1}.
\]

Every formula below depends on this convention. Reversing path order or moving
the boundary factor to the right changes the displayed tetrahedral law by
inverses and transported conjugations, but not its typed content.

### Face-lift obstruction

Given edge data, a face filler exists exactly when

\[
g_{ij}g_{jk}g_{ik}^{-1}
\in
\operatorname{im}\partial.
\]

Therefore the class of the boundary holonomy in

\[
G/\operatorname{im}\partial
\]

is the first obstruction. Since \(\operatorname{im}\partial\) is normal by
equivariance, this quotient is well typed.

If one face filler \(h\) exists, every other filler with the same boundary
differs by an element of

\[
\ker\partial.
\]

Indeed,

\[
\partial(h')=\partial(h)
\]

implies

\[
h^{-1}h'\in\ker\partial.
\]

In a crossed module, \(\ker\partial\) is central in \(H\), though \(G\) can act
nontrivially on it. Thus the fixed-boundary filler set is a
\(\ker\partial\)-torsor.

The nonabelian theory therefore reproduces the mapping-cone pattern:

- quotient obstruction to existence;
- kernel torsor of bridge choices.

### Tetrahedral coherence

For ordered vertices \(i<j<k<l\), there are two composites of face fillers
relating

\[
g_{ij}g_{jk}g_{kl}
\]

to

\[
g_{il}.
\]

With the frozen convention, coherence requires

\[
h_{ijk}h_{ikl}
=
(g_{ij}\triangleright h_{jkl})h_{ijl}.
\]

The tetrahedral residual is therefore

\[
\Omega_{ijkl}
=
h_{ijk}h_{ikl}
h_{ijl}^{-1}
(g_{ij}\triangleright h_{jkl})^{-1}.
\]

Strict 2-flatness requires

\[
\Omega_{ijkl}=e_H.
\]

The order and the transported action are essential. Replacing this expression
by an unordered product of four face labels destroys the nonabelian typing.

Applying \(\partial\) to the two sides gives the same edge-path boundary by
equivariance and the face equations. Consequently the residual lies in

\[
\ker\partial
\]

when all faces are correctly typed. It is a higher logical or curvature value
with trivial 1-boundary.

### Why the Peiffer laws are the real next rung

Equivariance guarantees that transporting a face filler changes its boundary
by the corresponding conjugation in \(G\).

The Peiffer identity guarantees that the action of a boundary arising from an
\(H\)-filler agrees with conjugation inside \(H\). It is the interchange law
that lets vertical and horizontal 2-composition define one strict 2-group.

Without Peiffer compatibility, edge and face transport can be individually
defined while their mixed compositions disagree. That disagreement is a
genuine next-rung obstruction invisible to abelian coboundary nilpotence.

### Abelian shadow

Set \(G\) trivial and let \(H\) be abelian. Then \(\partial\) is trivial, the
action disappears, and the tetrahedral equation becomes the additive boundary
law

\[
a_{ijk}+a_{ikl}-a_{ijl}-a_{jkl}=0.
\]

Over \(\mathbb F_2\), signs coincide and this reduces to the four-face parity
syndrome.

Thus the earlier tetrahedral code is the abelian shadow of crossed-module
2-curvature.

### Three finite coefficient regimes

Three small crossed modules separate the roles of obstruction and ambiguity.

#### Identity crossed module

Let

\[
H=G,
\qquad
\partial=\operatorname{id},
\]

with conjugation action.

Every face boundary has a unique lift. Both the obstruction quotient and filler
kernel are trivial:

\[
\operatorname{coker}\partial=1,
\qquad
\ker\partial=1.
\]

The face-filler torsor disappears. Any remaining defect must lie in coherence
or implementation rather than lift existence or choice.

#### Normal-subgroup inclusion

Let \(N\triangleleft G\) and use

\[
\partial:N\hookrightarrow G
\]

with conjugation action.

A face filler exists only when its boundary holonomy lies in \(N\). When it
exists, it is unique because the inclusion has trivial kernel.

For

\[
A_3\hookrightarrow S_3,
\]

the obstruction quotient is

\[
S_3/A_3\simeq C_2.
\]

This yields a parity-like obstruction with ordered \(S_3\) edge transport but
no higher filler torsor.

#### Central-kernel regime

Let \(H\) have a nontrivial central subgroup in \(\ker\partial\).

Then a liftable face boundary can admit several fillers, and the residual
tetrahedral curvature can live in that kernel. This is the regime needed for a
genuine higher logical filler sector.

A trivial boundary map with abelian \(H\) is the extreme example: only
1-flat edge loops are fillable, while every such face carries an \(H\)-torsor
of filler choices.

### Rotation test

Cellular duality can rotate:

- primal faces into dual edges;
- primal volumes into dual vertices.

But it cannot remove:

- the distinction between \(G\) and \(H\);
- the boundary homomorphism \(\partial\);
- the action \(G\curvearrowright H\);
- ordered tetrahedral transport;
- Peiffer interchange.

A dual presentation may make the incidence local, but its local coefficient is
still a 2-group rather than a scalar bit.

This passes the proposed novelty test: the geometric rung can rotate downward,
while the constructor typing remains irreducibly higher.

### Relation to D(S3)

The quantum double \(D(S_3)\) supplies noncommutative flux, charge, fusion, and
braiding data. It does not by itself authorize one particular crossed module
for the present compiler.

Finite crossed modules involving \(S_3\) include:

- \(\operatorname{id}:S_3\to S_3\);
- the normal inclusion \(A_3\hookrightarrow S_3\);
- the trivial inclusion \(1\hookrightarrow S_3\).

They make sharply different predictions for face-lift obstruction and filler
ambiguity.

Choosing among them from the desired answer would be circular. The actual
\(\partial\), action, and face incidence must be derived from the source
constructor theory.

### Hostile fixtures

A candidate nonabelian higher compiler fails at the first law violated:

1. \(\partial(g\triangleright h)\ne g\partial(h)g^{-1}\);
2. \(\partial(h)\triangleright h'\ne hh'h^{-1}\);
3. a face filler is claimed although its boundary lies outside
   \(\operatorname{im}\partial\);
4. two same-boundary fillers differ by an element outside
   \(\ker\partial\);
5. tetrahedral faces are multiplied without transport to a common base;
6. scalar trace or determinant vanishes while
   \(\Omega_{ijkl}\ne e_H\);
7. a crossed module is selected because it removes the known obstruction,
   without source authority;
8. exact finite 2-flatness is presented as physical executability or
   completion stability.

## Disposition

The crossed-module lift is the first candidate next rung that survives Carrier
rotation as genuinely higher constructor structure.

Its bounded packet is:

- finite groups \(H,G\);
- boundary homomorphism \(\partial\);
- \(G\)-action on \(H\);
- both crossed-module laws;
- edge labels and frozen path convention;
- face-lift obstruction in \(G/\operatorname{im}\partial\);
- filler torsor under \(\ker\partial\);
- ordered tetrahedral residual;
- task localization and authorized contraction;
- physical and quantitative authority.

The highest-information next step is a source-selection audit among the three
small \(S_3\)-based crossed modules. The decisive question is not which one is
mathematically convenient, but which edge and face constructors the pinned
\(D(S_3)\) fusion and braiding data actually induce.
