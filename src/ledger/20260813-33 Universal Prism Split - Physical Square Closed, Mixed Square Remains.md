# Universal Prism Split: Physical Square Closed, Mixed Square Remains

## Record

Date: 2026-08-13

Status: the two forced square facets of every pentagonal-prism carrier have different meanings.

For every dependency block of type \(2+1\):

1. the missing physical facet is a Boolean square of two physical cuts and is closed strictly by
   the coaction of entry 32;
2. the missing scalar facet is a genuine mixed square, transporting one scalar-refinement edge
   across one physical cut.

This classification is exact, all-local, and deck-equivariant through twelve points. It reduces
the coefficient-cosheaf frontier to one universal Beck--Chevalley square.

## The pentagonal prism

A dependency block with partition

\[
2+1
\]

has carrier

\[
K_2\times I.
\]

Entry 29 found that its inherited rank-two system contains two pentagons and three squares but
misses two square facets.

Let \(P\) be the physical core fixed by the rank-three common dissection. The two missing facets
are distinguished by the parity of the additional diagonal fixed on that facet.

## Physical fixed-diagonal square

Fixing the missing physical diagonal enlarges the common core to

\[
P'=P\cup\{g\}.
\]

The four vertex cores of this square are exactly

\[
P',
\qquad
P'\cup\{e\},
\qquad
P'\cup\{f\},
\qquad
P'\cup\{e,f\}.
\]

Every edge changes the core by one physical diagonal. Thus the square is the Boolean cut square

\[
\begin{matrix}
P' & \longrightarrow & P'\cup\{e\}\\
\downarrow && \downarrow\\
P'\cup\{f\} & \longrightarrow & P'\cup\{e,f\}.
\end{matrix}
\]

Entry 32 proves

\[
G_eG_f=G_fG_e
\]

as exact equality of occurrence-valued Laurent expressions. Therefore this forced square has
zero coefficient curvature. No new coefficient operation is needed for it.

Its absence from the direct rank-two carrier list was an order artifact: the relevant starting
core is not a prefix allowed by the original dependency-chain order. The strict physical
coaction removes that artifact.

## Scalar fixed-diagonal square

Fixing the missing scalar diagonal does not enlarge the common physical core. Its four vertices
have core multiset

\[
\{P,P,P\cup\{e\},P\cup\{e\}\}.
\]

At core \(P\), two vertices are joined by a scalar-refinement flip. At core \(P\cup\{e\}\), two
vertices are joined by the corresponding scalar-refinement flip. The remaining two edges add
the same physical channel \(e\).

Thus the square has the form

\[
\begin{matrix}
x_0 & \xrightarrow{h_{\rm scalar}} & x_1\\
\downarrow G_e && \downarrow G_e\\
y_0 & \xrightarrow{h_{\rm split}} & y_1.
\end{matrix}
\]

Its required relation is

\[
\boxed{
G_eh_{\rm scalar}
\simeq
h_{\rm split}G_e.
}
\]

This is the genuine mixed Beck--Chevalley condition.

The scalar presentation square already exists by entry 31. What is missing is its coefficient
and loaded-current image.

## Exact exhaustive certificate

At ten points there are forty marked pentagonal-prism occurrences per polarity. Every one has:

- one Boolean physical square at base core degree \(0\);
- one mixed Beck--Chevalley square at base core degree \(0\).

At twelve points there are 720 marked prism occurrences per polarity:

- 360 based at physical-core degree \(0\);
- 360 based at physical-core degree \(1\).

Every occurrence has exactly one square of each type.

Run:

    python -B research/nima/check_mixed_prism_squares.py

The script checks:

1. the two missing facets are squares;
2. exactly one fixes a physical diagonal and one a scalar diagonal;
3. the physical square has the complete Boolean core lattice;
4. the mixed square has two scalar edges and two physical edges;
5. all edge core changes have the asserted degree;
6. the full classification rotates to the opposite polarity sheet.

## Consequence for the coefficient cosheaf

The open coefficient problem is smaller than stated in entry 32.

The physical square is already controlled by the strict cut coaction. Hence the first missing
map is not a second physical Gysin law. It is the naturality of the existing \(G_e\) under one
scalar associahedral refinement.

Equivalently, the coefficient system must be a module over the scalar associahedral envelope,
and the physical coaction must be a morphism of that module up to the square homotopy supplied
by the envelope.

This is the first place where an \(A_\infty\)-type compatibility is genuinely required.

## What is established

1. every forced prism pair splits canonically into physical and mixed squares;
2. the physical square is Boolean;
3. its coefficient curvature vanishes strictly by entry 32;
4. the scalar square is exactly one refinement transported across one cut;
5. the pattern is independent of ambient arity and base core degree;
6. one-step rotation preserves the split.

## What remains open

This entry does not construct:

1. the scalar-refinement coefficient map \(h_{\rm scalar}\);
2. the split-region map \(h_{\rm split}\);
3. the mixed square homotopy \(H_e\);
4. a loaded-current representative;
5. a filtered Pochhammer/Cousin comparison.

The worldsheet obstruction is now concentrated in

\[
G_eh_{\rm scalar}-h_{\rm split}G_e.
\]

## Primary next test

Choose the universal ten-point prism and construct the two scalar edge transports at its lower
and upper cores.

Transport their endpoints through the regional Catalan bijections and the explicit coaction
\(G_e\). Then compute the route difference

\[
\Omega_e
=
G_eh_{\rm scalar}-h_{\rm split}G_e.
\]

Test, in order:

1. whether \(\Omega_e\) vanishes on the occurrence module;
2. if not, whether it is an exact scalar presentation chain;
3. if so, whether the exact primitive has a finite-\(\alpha'\) loaded-current lift;
4. whether rotation sends \(\Omega_e^+\) to \(\Omega_{\rho e}^-\).

A nonzero cohomology class of \(\Omega_e\) would be the first genuine factorization-naturality
obstruction to \(\mathsf J\).

## Decision

Promote:

> Of the two rank-three facets first missing from the direct transfer, one is already closed by
> strict physical coaction. The only new universal coefficient datum is the mixed
> scalar-refinement/physical-cut Beck--Chevalley square.

The immediate Nima frontier is the chain/current image of that single square.
