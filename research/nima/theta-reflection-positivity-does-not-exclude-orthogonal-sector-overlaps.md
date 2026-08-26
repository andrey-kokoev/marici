# Reflection positivity does not exclude orthogonal sector overlaps

## Immediate obstruction

Let the reflection-positive quotient carry a positive Hermitian pairing

\[
\langle v,w\rangle_\Theta=B(\Theta v,w).
\]

Reflection positivity states

\[
\langle v,v\rangle_\Theta\ge0.
\]

It controls diagonal norms. A completed scalar readout formed as an overlap

\[
\sigma(s)=\langle v_-(s),v_+(s)\rangle_\Theta
\]

can still vanish while both states have strictly positive norm.

The smallest witness is

\[
G=I_2,
\qquad
v_+=
\begin{pmatrix}1\\0\end{pmatrix},
\qquad
v_-=
\begin{pmatrix}0\\1\end{pmatrix}.
\]

Then

\[
\langle v_+,v_+\rangle_\Theta
=
\langle v_-,v_-\rangle_\Theta
=1,
\]

but

\[
\langle v_-,v_+\rangle_\Theta=0.
\]

There is no null state and no failure of reflection positivity. The zero is
ordinary orthogonality.

## Null-space transport is insufficient

Let

\[
\mathcal N=\ker G
\]

be the reflection-positive null space. A transport \(T\) cannot send a nonnull
state into \(\mathcal N\) if it satisfies

\[
\ker(T^*GT)=\ker G.
\]

Exact \(G\)-unitarity,

\[
T^*GT=G,
\]

is a sufficient source law.

This protects state norm. It still does not prevent two transported nonnull
states from becoming orthogonal. Therefore null-space exclusion is not scalar
zero exclusion.

## Missing bridge

Reflection positivity would imply zero confinement only if the source also
proved a factorization of the distinguished scalar of the form

\[
\sigma(s)=u(s)\langle v(s),v(s)\rangle_\Theta,
\qquad
u(s)\ne0.
\]

Then a scalar zero would imply a reflection-null state.

But this is a new and very strong theorem. It must identify the two sector
states in the reflection-positive quotient up to the source-derived
nonvanishing factor \(u\). Neither functional-equation symmetry nor unitary
sewing provides that identification.

Constructing \(u\) by dividing the scalar section by the positive norm is
circular and is rejected.

## Complex-value obstruction

A diagonal reflection-positive norm is real and nonnegative. The completed xi
section is generally complex away from its real symmetry loci. Therefore it
cannot equal such a norm directly on an open complex domain.

Any diagonal representation requires a nontrivial complex frame \(u(s)\). The
source must derive its analyticity, nonvanishing, reflection law, and cutoff
coherence independently. That frame carries the same dark-overlap risk unless
the factorization is proved before scalar completion.

## Relation to the earlier Clifford picture

The obstruction matches the geometric-algebra correction. A scalar component
can vanish while the bivector or full relational state remains nonzero.
Reflection positivity controls the full norm, not the selected scalar
component.

Thus the mixed tensor grade may preserve orientation information through a
scalar zero without excluding that zero. This is valuable provenance, but not
an RH proof.

## Finite falsifiers

For any proposed reflection-positive construction, compute:

1. the Gram matrix \(G\);
2. the norms of the two distinguished sector states;
3. their mutual overlap;
4. the rank of their two-state Gram block;
5. whether the source identifies their quotient rays.

The route fails as zero exclusion if a positive-definite two-state block has
zero off-diagonal overlap. It also fails if ray identification requires a
post-completion phase choice or division by the scalar section.

## Lakatos disposition

Reflection positivity remains a legitimate source-orientation law for the
full mixed state. By itself it does not prohibit zeros of a selected overlap.

The route should remain open only if labelled theta/Tate operations derive the
additional diagonalization or ray-identification theorem. Without that bridge,
reflection positivity is another faithful lift that survives scalar
cancellation rather than preventing it.
