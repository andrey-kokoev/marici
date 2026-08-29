# The sixth sector separates linear height from exponential constructor density

Owner: marici.Kitaev

## Question

What happens one rung above the fifth-sector hypercrossed probe, and can the
growth of nonabelian constructor data be stated exactly rather than described
qualitatively?

## Claim boundary

The safe algebraic carrier is a simplicial group with Moore complex of length
five:

\[
I\xrightarrow{\partial_5}J\xrightarrow{\partial_4}K
\xrightarrow{\partial_3}L\xrightarrow{\partial_2}H
\xrightarrow{\partial_1}G.
\]

It models a connected homotopy 6-type through its length-five hypercrossed
complex. This packet does not assert a compact sourced “5-crossed-module”
presentation.

The source definition of hypercrossed Peiffer pairings is in Arvasi,
Kuzpinari, and Uslu:

<https://arxiv.org/pdf/0812.4685>

For degree \(n\), pairings are indexed by ordered pairs
\((\alpha,\beta)\) of disjoint nonempty degeneracy patterns, with one ordering
chosen to remove exchange duplication.

### Residual-sector shadow

The new top sectors are

\[
\pi_5=\ker\partial_4/\operatorname{im}\partial_5,
\qquad
\pi_6=\ker\partial_5.
\]

Thus the stable law persists:

- \(I\)-boundaries repair old fifth-sector residue;
- closed \(I\)-constructors form the new sixth-sector ambiguity.

For the abelian two-term shadow

\[
I\xrightarrow{f}J\longrightarrow1\longrightarrow1
\longrightarrow1\longrightarrow1,
\]

one has

\[
\pi_5=\operatorname{coker}f,
\qquad
\pi_6=\ker f.
\]

The shadow self-closes exactly when \(f\) is an isomorphism.

### Exact constructor-density count

There are \(n\) possible degeneracy positions at degree \(n\). For a pair of
disjoint subsets \(\alpha,\beta\), each position has three assignments:

1. belong to \(\alpha\);
2. belong to \(\beta\);
3. belong to neither.

Hence there are \(3^n\) ordered disjoint pairs if empty subsets are allowed.

There are \(2^n\) assignments with \(\alpha\) empty and \(2^n\) with
\(\beta\) empty. The doubly empty assignment has been removed twice and must be
restored once. Therefore the number with both subsets nonempty is

\[
3^n-2^{n+1}+1.
\]

Exchange \((\alpha,\beta)\leftrightarrow(\beta,\alpha)\) has no fixed point
when both are nonempty and disjoint. Choosing one lexicographic orientation
therefore gives

\[
P_n=\frac{3^n-2^{n+1}+1}{2}.
\]

This reproduces the published degree-four list:

\[
P_4=\frac{81-32+1}{2}=25.
\]

At the new degree,

\[
P_5=\frac{243-64+1}{2}=90.
\]

So the raw Peiffer-pairing surface jumps from 25 to 90 types in one rung.

### What the count means

The number 90 is not the number of independent logical sectors. It is the
number of raw binary mixed-composition types before:

- evaluating boundaries;
- imposing simplicial identities;
- quotienting degenerate relations;
- identifying source-specific redundancies;
- restricting to task-visible constructors.

The homotopy tower gains only one new residual group, but the constructor
theory must coordinate operations involving every partition of degeneracy
positions between two nonempty inputs.

Asymptotically,

\[
P_n\sim\frac{3^n}{2}.
\]

Therefore height is linear while raw relationship density is exponential.

This gives a sharper interpretation of the earlier “reality is relationship
density” conjecture. Higher coherence is not mainly additional hidden state.
It is the requirement that a rapidly growing family of contextual
compositions agree.

### Pure and exact fixtures

The pure fixture

\[
C_2\to1\to1\to1\to1\to1
\]

has trivial lower sectors and

\[
\pi_6=C_2.
\]

It proves that complete closure through \(\pi_5\) does not force universal
sixth-sector closure.

The exact fixture

\[
A\xrightarrow{\mathrm{id}}A\to1\to1\to1\to1
\]

has

\[
\pi_5=\pi_6=0.
\]

It proves that the new rung can still close without residue in the linear
shadow.

Neither fixture tests the 90 nonabelian pairing types. They are falsifiers for
sector closure only.

### A new compression question

At this rung the central question changes from existence to compressibility:

> Can the 90 raw pairings be generated from a bounded constructor basis and a
> bounded family of coherence laws?

There are three possible outcomes.

1. **Finite presentation:** a small generating family plus identities derives
   all 90 pairings.
2. **Task-relative compression:** only a bounded subset is relevant to the
   declared interface.
3. **Irreducible contextual growth:** increasingly many pairings remain
   independent as the rung rises.

Only the third outcome would make the full higher constructor tower
intrinsically unscalable. Raw pairing count alone does not prove it.

### Geometric audit

The degree-five comparison data first closes globally on a 7-simplex boundary.
The ordered composition cannot be recovered from alternating signs alone. A
finite audit must derive it from:

- one frozen Moore-length-five simplicial group;
- its face and degeneracy maps;
- the 90 \(F_{\alpha,\beta}\) pairing types;
- the corresponding boundary identities.

A homotopy-sector computation that skips this constructor audit can prove
\(\pi_5=\pi_6=0\) while leaving the implementation under-specified.

### Hostile falsifiers

Reject at the first applicable case:

1. \(\partial_4\partial_5\neq1\);
2. \(\pi_5\) is computed without quotienting by
   \(\operatorname{im}\partial_5\);
3. a nonzero class in \(\ker\partial_5\) is discarded;
4. the 90 raw pairings are described as 90 independent logical bits;
5. exchange symmetry is divided out when ordered input roles remain typed;
6. empty degeneracy patterns are incorrectly counted as Peiffer pairs;
7. a small generator basis is asserted without deriving all pairing types;
8. vanishing homotopy sectors are equated with constructor closure;
9. a compact higher-crossed-module presentation is invented by analogy;
10. a seventh sector is added before the compression question is tested.

## Disposition

The next rung confirms and sharpens the phase change.

The sector law remains linear:

\[
\pi_5=\ker\partial_4/\operatorname{im}\partial_5,
\qquad
\pi_6=\ker\partial_5.
\]

The raw nonabelian constructor surface grows as

\[
P_n=\frac{3^n-2^{n+1}+1}{2},
\]

giving 25 pairing types at degree four and 90 at degree five.

The strongest conclusion is not that reality requires infinitely many towers.
It is that higher coherence presents a compression problem: a small residual
state may be the quotient shadow of a very dense network of contextual
relations.

No current marici source authorizes the sixth-sector port. The highest-value
next move is to test whether the degree-five pairing family admits a bounded
generating basis under simplicial identities. That decides whether the
observed exponential density is real independent structure or merely a
redundant presentation.
