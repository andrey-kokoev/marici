# Invertible archimedean or reciprocal sewing cannot create the missing class

## Conjugation theorem

Suppose a complex has differential `d`, homotopy `h`, and explicit defect
projection `E` satisfying

\[
dh+hd=1-E.
\]

Let `U` be an isomorphism between the relevant completed state spaces and
domains. Define

\[
d_U=UdU^{-1},
\qquad
h_U=UhU^{-1},
\qquad
E_U=UEU^{-1}.
\]

Then

\[
d_Uh_U+h_Ud_U=1-E_U.
\]

Thus invertible transport can move, rotate, or reweight the known boundary
class but cannot create new cohomology or a new divisor.

The same statement holds for boundedly invertible graph-domain maps. For
unitary maps it is immediate with identical norm control.

## Application to the current candidates

Several attractive completion operations fall into this class when correctly
typed:

- Fourier or metaplectic transport on a common rigged space;
- reciprocal exchange implemented by an invertible sheet map;
- opposite exponential weights viewed as isomorphisms between their declared
  weighted Sobolev spaces;
- changes of output frame in the finite active colligation;
- multiplication by a nowhere-zero source unit with bounded inverse on the
  chosen domain.

None can turn the flat prime-seam complex into an RH-bearing complex merely by
conjugation. Any claim that it does must identify a domain, boundary, or
completion feature not transported invertibly by `U`.

## Where a class can actually appear

A genuine anomaly requires a noninvertible categorical operation, for
example:

1. intersection of two transported domains;
2. a pullback imposing independent boundary conditions;
3. a quotient or cokernel at the seam;
4. a trace or determinant completion that is not exact;
5. failure of `U`, `U^{-1}`, or the transported homotopy to be continuous in
   the completed topology;
6. a relative comparison of two inequivalent completions rather than a
   coordinate change inside one completion.

This sharply retypes the archimedean frontier. The gamma factor or Fourier
transform cannot supply RH force as a scalar multiplier or unitary rotation.
It must change the admissible domain diagram.

## Multi-tower interpretation

The missing cell does not live inside any one tower. It can live in the
failure of two individually contractible towers to have a contractible
pullback. Concretely, let `C_+` and `C_-` be the source-normalized sector
complexes and let both map to an interface object `B`. Their sewn object is

\[
C_+\times_B C_-.
\]

Even when `C_+` and `C_-` are individually contractible, the pullback need
not be. Its obstruction measures incompatibility of the two boundary maps,
not cohomology created by an invertible exchange.

This is the correct categorical location for a seam-supported inner-factor
record.

## Immediate test

For every proposed archimedean or reciprocal constructor:

1. state its source and target graph domains;
2. test whether it is an isomorphism there;
3. if it is, transport the fixed-prime homotopy explicitly and close the
   route;
4. if it is not, compute the kernel, cokernel, or domain-intersection defect;
5. compare that defect with the Evans phase-delay record before scalarizing.

## Scope

This closes invertible sewing as the source of new RH cohomology. It does not
construct the sector pullback, calculate its relative defect, identify it
with the Evans inner factor, or prove RH.
