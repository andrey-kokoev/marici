# The fifth sector forces a hypercrossed-complex probe

Owner: marici.Kitaev

## Question

What survives one rung above a 3-crossed module, and does the clean
repair-versus-new-kernel law still explain the next sector when the compact
nonabelian presentation ceases to be evident?

## Claim boundary

The safe source-native object is a simplicial group whose Moore complex has
length four:

\[
J\xrightarrow{\partial_4}K\xrightarrow{\partial_3}L
\xrightarrow{\partial_2}H\xrightarrow{\partial_1}G.
\]

Its complete nonabelian constructor data is the associated length-four
hypercrossed complex, not merely the displayed complex of groups.

The primary source used here is Arvasi, Kuzpinari, and Uslu:

<https://arxiv.org/pdf/0812.4685>

That paper states that general hypercrossed complexes are equivalent to
simplicial groups, presents the Peiffer pairings indexed by pairs of disjoint
degeneracy patterns, and explicitly lists 25 degree-four pairing patterns.
It gives a compact 3-crossed-module presentation for Moore length three. This
packet does not claim that an equally compact and established
“4-crossed-module” presentation has been supplied.

### Stable linear shadow

At the level of homotopy sectors, the pattern continues:

\[
\pi_1=G/\operatorname{im}\partial_1,
\]

\[
\pi_2=\ker\partial_1/\operatorname{im}\partial_2,
\]

\[
\pi_3=\ker\partial_2/\operatorname{im}\partial_3,
\]

\[
\pi_4=\ker\partial_3/\operatorname{im}\partial_4,
\qquad
\pi_5=\ker\partial_4.
\]

Thus \(J\) repairs some old fourth-sector residue through
\(\operatorname{im}\partial_4\), while \(\ker\partial_4\) is the new
fifth-sector ambiguity.

For the abelian shadow

\[
J\xrightarrow{f}K\longrightarrow1\longrightarrow1\longrightarrow1,
\]

one obtains

\[
\pi_4=\operatorname{coker}f,
\qquad
\pi_5=\ker f.
\]

Surjectivity repairs the old sector, injectivity prevents a new one, and
bijectivity self-closes the two-term shadow.

### Pure survival and exact repair

The pure fixture

\[
C_2\longrightarrow1\longrightarrow1\longrightarrow1\longrightarrow1
\]

has trivial \(\pi_1,\pi_2,\pi_3,\pi_4\) and nontrivial

\[
\pi_5=C_2.
\]

It falsifies universal closure through the fourth homotopy sector.

The exact repair fixture

\[
A\xrightarrow{\mathrm{id}}A\longrightarrow1\longrightarrow1
\longrightarrow1
\]

has

\[
\pi_4=\pi_5=0.
\]

Therefore the repair/kernel explanation survives one more rung in every
abelian or homotopy-group projection.

### The nonabelian phase change

The full constructor theory does not grow linearly.

For a simplicial group, hypercrossed Peiffer pairings have the form

\[
F_{\alpha,\beta}:
NG_{n-\lvert\alpha\rvert}\times
NG_{n-\lvert\beta\rvert}\longrightarrow NG_n,
\]

where \(\alpha,\beta\) are disjoint degeneracy patterns with an ordering
condition.

At degree four, the cited source lists 25 admissible pairing patterns. These
include interactions between:

- degree-one and degree-three data;
- degree-two and degree-two data;
- degree-two and degree-three data;
- degree-three and degree-three data;

with different degeneracy placements producing inequivalent ordered
constructors.

The previous 3-crossed-module presentation packages the relevant lower
pairings into seven named lifting types and eighteen laws. At the present rung,
the raw degree-four table already contains 25 pairing types before deriving
relations, actions, quotient identifications, or a compact presentation.

This changes the interpretation of “one rung up.” The homotopy-group shadow
adds one kernel and one quotient, but the nonabelian constructor surface adds a
network of mixed operations.

### What remains structural

Three facts survive the expansion.

First, the repair law is stable:

\[
\text{old residue}/\text{new boundaries}.
\]

Second, the new ambiguity law is stable:

\[
\text{new closed constructors}=\ker\partial_4.
\]

Third, source authority becomes more demanding. A source must derive not only
\(J\) and \(\partial_4\), but every task-relevant hypercrossed pairing and its
simplicial identities.

The tower picture is therefore accurate for homotopy groups but misleading
for constructor theory. Higher rungs are not a line of independent ports.
They are increasingly dense incidence networks among all preceding degrees.

### Geometric audit

The new degree represents comparisons among four-dimensional constructors.
Its first closed global composition is expected on a 6-simplex boundary.

An ordered 6-simplex word must not be guessed from alternating signs. In the
nonabelian setting, degeneracy placement, whiskering, action, and order are
part of the datum. The safe derivation is:

1. freeze a finite simplicial group with Moore length four;
2. compute its normalized groups \(NG_0,\ldots,NG_4\);
3. generate the degree-four \(F_{\alpha,\beta}\);
4. derive their boundaries from the simplicial identities;
5. quotient only by source-authorized degenerate relations;
6. test the resulting 6-simplex composition.

### A sharper self-closure criterion

Homotopy-sector closure requires

\[
\ker\partial_3=\operatorname{im}\partial_4
\quad\text{and}\quad
\ker\partial_4=1.
\]

Constructor closure additionally requires that all task-relevant degree-four
Peiffer pairings be generated and related by the source simplicial structure.
The homotopy groups can vanish while the proposed implementation remains
under-typed.

This gives three distinct outcomes:

1. **sector closure**: \(\pi_4=\pi_5=0\);
2. **constructor closure**: every mixed pairing is coherently generated;
3. **embodied closure**: those constructors survive the physical interface.

None implies the next without an additional theorem.

### Hostile falsifiers

Reject at the first applicable case:

1. \(\partial_3\partial_4\neq1\);
2. a nonzero fifth-sector class is hidden by lower projection;
3. \(\pi_4\) is computed as \(\ker\partial_3\) without quotienting by
   \(\operatorname{im}\partial_4\);
4. the 25 raw degree-four pairings are replaced by one scalar residual;
5. two degeneracy patterns are identified without a simplicial identity;
6. the chain-complex shadow is called a complete nonabelian model;
7. a compact “4-crossed module” axiom system is asserted without a source;
8. a 6-simplex word is inferred from abelian alternating signs;
9. sector closure is treated as constructor or physical closure;
10. the next rung is added without a named task-visible fifth-sector
    distinction.

## Disposition

The next rung can be probed cleanly, but it no longer looks like one more copy
of the previous algebraic gadget.

The repair-versus-kernel law survives:

\[
\pi_4=\ker\partial_3/\operatorname{im}\partial_4,
\qquad
\pi_5=\ker\partial_4.
\]

The pure \(C_2\) fixture proves that a fifth logical sector can exist while all
lower sectors vanish. The identity fixture proves that the rung can also
self-close exactly.

What changes is constructor density. The source-native degree-four structure
has 25 raw Peiffer pairing types. The useful prediction is therefore:

> Higher reality is not primarily additional height; it is rapidly increasing
> relationship density among existing levels.

No current marici sector authorizes this fifth-level port. The highest-value
next experiment is to find the smallest finite simplicial group of Moore
length four with nontrivial mixed degree-four pairings, then test whether
vanishing \(\pi_4,\pi_5\) is sufficient for constructor closure. That would
decide whether relationship density contains residual information not visible
in the homotopy-group tower.
