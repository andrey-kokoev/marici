# Ascending rungs stabilizes the law and moves the problem to truncation

Owner: marici.Kitaev

## Question

If several further hypercrossed rungs are explored at once, does each bring a
new qualitative mechanism, or does the ascent stabilize into one uniform law
with a separate task-relative stopping criterion?

## Claim boundary

The full source-native object is no longer best regarded as an indefinitely
invented sequence of named higher crossed modules. It is a simplicial group,
or equivalently a hypercrossed complex of groups.

Carrasco and Cegarra prove a nonabelian Dold–Kan-type equivalence between
simplicial groups and hypercrossed complexes:

<https://doi.org/10.1016/0022-4049(91)90133-M>

Arvasi, Kuzpinari, and Uslu give the explicit degeneracy-indexed Peiffer
pairings used in the present finite counts:

<https://arxiv.org/pdf/0812.4685>

The result is structural rather than physical. No current marici source is
thereby authorized to possess arbitrarily high nontrivial sectors.

### What stabilizes

For a Moore complex

\[
\cdots\longrightarrow C_{n+1}
\xrightarrow{\partial_{n+1}}C_n
\xrightarrow{\partial_n}C_{n-1}\longrightarrow\cdots,
\]

the residual sector is always

\[
\pi_n=\ker\partial_n/\operatorname{im}\partial_{n+1}.
\]

Every rung has the same explanatory roles:

- \(\ker\partial_n\): distinctions invisible one rung below;
- \(\operatorname{im}\partial_{n+1}\): distinctions explained by authorized
  next-rung constructors;
- \(\pi_n\): irreducible disagreement after those explanations.

Thus the obstruction–repair–ambiguity law stabilizes completely.

### What grows

The number of raw binary Peiffer contexts at degree \(n\) is

\[
P_n=\frac{3^n-2^{n+1}+1}{2}.
\]

The next several values are:

| Degree \(n\) | Raw pairing contexts \(P_n\) |
|---:|---:|
| 4 | 25 |
| 5 | 90 |
| 6 | 301 |
| 7 | 966 |
| 8 | 3025 |

The asymptotic growth is

\[
P_n\sim\frac{3^n}{2}.
\]

These are context types, not homotopy dimensions and not independent logical
bits.

### Generative compression

The exponential table does not imply that nature needs an exponentially long
list of unrelated laws.

A simplicial group uses uniform families of face and degeneracy maps satisfying
the same simplicial identity schemas in every degree:

\[
d_i d_j=d_{j-1}d_i\quad(i<j),
\]

\[
s_i s_j=s_{j+1}s_i\quad(i\le j),
\]

together with the mixed face–degeneracy identities.

The Peiffer pairings are generated from degeneracies, commutators, and Moore
projection. Therefore exponentially many contextual probes can be produced by
a bounded law schema applied to growing finite index sets.

This is generative compression:

\[
\text{small uniform rule schema}
\longrightarrow
\text{many typed contextual consequences}.
\]

It does not imply bounded execution cost or bounded source data. It says the
relationships are algorithmically organized rather than an arbitrary lookup
table.

### The real stopping criterion

The tower may be truncated at height \(N\) for a task \(T\) only when both
conditions hold:

1. the source has no task-visible homotopy above \(N\);
2. the task factors through the \(N\)-type, so higher constructors cannot
   change its outcome.

In symbols, a sufficient task-relative condition is

\[
\pi_n^{\,T}=0\quad(n>N)
\]

and

\[
T=T_N\circ P_N,
\]

where \(P_N\) is the Postnikov truncation to the \(N\)-type.

Vanishing higher sectors alone is not enough if the implementation still
depends on higher constructor witnesses. Conversely, nonzero ambient higher
homotopy is harmless when the declared task provably factors through a lower
truncation.

### Three notions of finiteness

The ascent separates three ideas.

1. **Finite sector height:** only finitely many task-visible \(\pi_n\) are
   nonzero.
2. **Finite presentation:** a bounded rule schema generates all relevant
   cross-rung comparisons.
3. **Finite execution:** the task can evaluate those rules with bounded
   resources and stable conditioning.

A simplicial presentation strongly supports the second. It does not guarantee
the first or third.

### Consequence for the marici tower picture

The tower should be replaced by two coupled views.

The vertical view records residual state:

\[
\cdots\to C_{n+1}\to C_n\to C_{n-1}\to\cdots.
\]

The contextual view records all degeneracy-indexed mixed interactions among
the degrees.

The vertical tower is a compression of where disagreement survives. The
hypercrossed network explains how different-rung probes are reconciled before
taking that quotient.

Thus the higher sector is not a place in which all reconciliation occurs. It
is the residue after the surrounding network of reconciliation constructors
has acted.

### Hostile falsifiers

Reject at the first applicable case:

1. raw pairing count is treated as independent state dimension;
2. uniform simplicial laws are claimed to give bounded execution cost;
3. a truncation is made solely because high homotopy groups vanish;
4. a task is declared low-rung without a factorization through its truncation;
5. nonzero ambient higher sectors are declared relevant without a task port;
6. scalar agreement is substituted for equality of generated constructors;
7. an infinite tower is postulated when a finite Postnikov stage suffices;
8. a finite tower is postulated when the task detects arbitrarily high stages;
9. source-specific face or degeneracy maps are invented from the universal
   schema;
10. physical embodiment is inferred from algebraic generative compression.

## Disposition

Several further rungs do not reveal a new obstruction law. They reveal a
stable architecture:

\[
\text{uniform local generation}
\longrightarrow
\text{exponentially many contexts}
\longrightarrow
\text{homological residual sectors}.
\]

The decisive question is no longer “what is the next rung?” It is:

> What is the minimal Postnikov height through which the declared task
> factors, and does the source provide a stable implementation of that
> truncation?

This supplies a principled stop rule. Continue upward only when a named task
distinguishes two states or constructors identified by the current
truncation.

For the present Kitaev programme, the finite toric-code task stops at its
ordinary logical sector unless a source-derived operation detects a higher
implementation comparison. The abstract hypercrossed tower remains a hostile
model showing what lower data could fail to capture, not an automatic
extension of the physical theory.
