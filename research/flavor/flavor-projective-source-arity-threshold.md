# The complex projective flavor source has an arity-three threshold: WP959

## Question

What is the smallest source packet of complex family triplets whose canonical
projector map can carry relational information capable of three-family CP?

## Canonical map

For a nonzero complex triplet \(u\), define

\[
\pi(u)=\frac{uu^\dagger}{u^\dagger u}.
\]

This map is invariant under nonzero complex rescaling and equivariant under a
common weak-basis transformation:

\[
\pi(\lambda u)=\pi(u),\qquad
\pi(Uu)=U\pi(u)U^\dagger.
\]

Thus the map itself, unlike a chosen ray, is a legal candidate interface into
\(\operatorname{Proj}_1(\mathbb C^3)\).

## Arity one and two

The common \(U(3)\) action is transitive on projective rays, so one triplet has
no relational quotient coordinate.  Two projectors have ranges spanning at
most a two-dimensional subspace and therefore share a nonzero annihilated
line.  Every word in the two projectors preserves that line.  Any two sector
operators constructed from this algebra have a commutator of rank at most two
and zero cubic trace.

Hence neither one nor two projective triplets can supply the WP957
three-family CP constructor.

## Arity three

For three projectors, the cyclic Bargmann invariant

\[
\mathcal B(P,Q,R)=\operatorname{Tr}(PQR)
\]

is invariant under simultaneous weak-basis conjugation and under independent
rescaling of the three source vectors.  Its imaginary part is an intrinsic
relational orientation of the three projective rays.  For the exact rays

\[
p=(1,0,0)^T,\qquad q=(1,1,0)^T,\qquad r=(1,i,1)^T,
\]

the projectors span the full family carrier and

\[
\mathcal B(P,Q,R)=\frac{1+i}{6}.
\]

Complex conjugation preserves the CP-even projector overlaps and reverses
\(\operatorname{Im}\mathcal B\), so CP-even source data alone cannot choose
the orientation.

## Claim boundary and disposition

This is an interface and minimum-arity theorem, not a source selector.  It
identifies the first source object on which a CP-sensitive projective quotient
coordinate can exist: an ordered triple of complex family rays spanning
\(\mathbb C^3\).  No current source action derives the triple, fixes its
Bargmann invariant, proves completion stability, or supplies a calibrated
instrument.

The next admissible selector candidate must therefore derive an ordered
three-triplet packet or an equivalent irreducible complex tensor directly
from flavor dynamics or geometry.  A reference that orders or orients the
triple changes the stabilizer groupoid and defines a new relational
experiment.  No composition is assigned physical time or causality.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp959_projective_source_arity_threshold.py

Generated result:
`research/flavor/results/wp959_projective_source_arity_threshold.json`.
