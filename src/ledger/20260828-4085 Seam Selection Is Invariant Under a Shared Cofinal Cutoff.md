# Seam Selection Is Invariant Under a Shared Cofinal Cutoff

## Common reparameterization

Let the direct and reciprocal Euler boundary currents be compared at a shared
cutoff \(N\). Replace that cutoff by any common cofinal clock

\[
N=\phi(T),
\qquad
\phi(T)\longrightarrow\infty.
\]

The forced boundary comparator becomes

\[
R_s^{\phi}(T)
=
\frac{s}{1-s}
\phi(T)^{1-2s}.
\]

Its modulus is

\[
|R_s^{\phi}(T)|
=
\left|\frac{s}{1-s}\right|
\phi(T)^{1-2\Re s}.
\]

Because \(\phi(T)\) is unbounded, this family and its inverse are both
uniformly bounded if and only if

\[
\Re s=\frac12.
\]

Thus the seam selector does not depend on choosing the integer cutoff itself,
a logarithmic cutoff, or any other shared cofinal reparameterization.

## Independent clocks destroy the theorem

If the sectors are allowed independent clocks

\[
N_+=\phi_+(T),
\qquad
N_-=\phi_-(T),
\]

then the comparator has modulus proportional to

\[
\frac{phi_+(T)^{1-Re s}}
{phi_-(T)^{\Re s}}.
\]

For any fixed off-seam \(s\), one can tune the relative growth of
\(\phi_+\) and \(\phi_-\) to make this ratio bounded. Therefore seam
selection is not invariant under arbitrary independent regulator choices.

The mathematical datum that carries the theorem is a diagonal cofinality map
between the two regulator towers.

## Categorical formulation

Let \(I_+\) and \(I_-\) be the filtered cutoff categories of the two
reciprocal sectors. A shared regulator is a cofinal functor

\[
\Delta:I\longrightarrow I_+\times I_-.
\]

The seam theorem requires that both components of \(\Delta\) represent the
same source scale up to bounded cofinal distortion. It is insufficient merely
to know that each component tends to infinity.

A reciprocal comparison that chooses its clocks independently can conceal an
off-seam grade mismatch. A source-derived diagonal cannot.

## Tate interpretation

Locally, Fourier--Tate sewing reverses valuation orientation while retaining
valuation depth. In logarithmic scale it acts schematically by

\[
q\longmapsto-q.
\]

This supplies a natural candidate for the diagonal: the two sectors use the
same absolute scale \(|q|\) with opposite orientation.

The remaining audit is global. The Euler label cutoff \(n\leq N\) must be
shown to descend from that same absolute adelic scale, rather than being an
unrelated enumeration of labels. Poisson symmetry alone does not establish
this identification.

## Revised source theorem

The RH-bearing claim is now:

> The completed theta/Tate source assigns every reciprocal zero-germ a common
> cofinal regulator, induced by one absolute valuation scale, and its sewing
> morphism is uniformly invertible on the leading boundary class.

Under this theorem, the earlier condition-number calculation forces the
critical line.

## Falsifier

Produce a source-admissible pair of reciprocal zero-germs for which:

- the direct and reciprocal cutoff towers are individually valid;
- their only comparison uses asymptotically unequal clocks;
- no bounded-distortion common cofinal refinement exists.

Such a witness kills the boundary-grade route even if the scalar functional
equation remains exact.

## Explanatory gain

The special line is not selected by a preferred cutoff number. It is selected
by synchronized resolution.

Each sector may regularize its divergent meaning. They denote one reversible
event only when their resolutions can be refined together without one side
running asymptotically faster than the other. The critical line is the neutral
locus of that synchronized comparison.

