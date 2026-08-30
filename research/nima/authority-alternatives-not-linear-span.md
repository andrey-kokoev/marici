# Alternative authority domains form a tagged coproduct, not a linear span

## Problem

The admissible-Hom criterion assumes a single active authority domain.
When several domains are alternatives, taking the linear span of their
admissible cells silently creates mixed witnesses authorized by none of
them.

Conjunctive restrictions behave differently: intersections of linear
subcomplexes remain subcomplexes.  Disjunctive authority is not modeled
by span.

## Minimal hostile witness

Over (mathbf F_2), let the degree (-2) comparison space be

\[
U=\langle e_1,e_2\rangle
\]

and the degree (-1) ambiguity space be

\[
Z=\langle z_1,z_2\rangle,
\qquad
\partial e_1=z_1,quad
\partial e_2=z_2.
\]

The obstruction to be filled is

\[
z=z_1+z_2.
\]

Authority domain (A) admits only (langle e_1\rangle); domain (B)
admits only (langle e_2\rangle).  Neither domain contains a filler
for (z).  But their linear span contains

\[
e_1+e_2,qquad \partial(e_1+e_2)=z.
\]

Thus spanning the alternatives reports vanishing by manufacturing a
cross-domain filler.

## Correct representation

Alternative domains must remain tagged:

\[
\operatorname{Hom}_{A}\;\sqcup\;
\operatorname{Hom}_{B}.
\]

A witness is accepted only if one branch fills the entire obligation.
A mixed witness requires a named authority-crossing constructor

\[
\mu_{A,B}:(A\text{-cell},B\text{-cell})
\rightharpoonup AB\text{-cell}
\]

with its own support, resource, fault, temporal, and coherence laws.
Vector addition is not that constructor.

## Compiler gate

For each authority tag (a):

1. compute the admissible complex (H_a^\bullet);
2. test the full obstruction within that branch;
3. accept if one branch supplies a complete filler;
4. otherwise reject unless a source-authorized crossing constructor
   explicitly creates a new branch.

```json
{
  "code": "cross_authority_span_fabrication",
  "obstruction": ["z1", "z2"],
  "partial_fillers": {
    "domain_A": ["z1"],
    "domain_B": ["z2"]
  },
  "span_would_fill": true,
  "crossing_constructor_present": false
}
```

## Local Tate application

Grothendieck's one-prime doubled charts are authorized by the local Tate
functional equation:

\[
Z_+(s)=\frac1{1-p^{-s}},qquad
Z_-(s)=\frac1{1-p^{s-1}},
\qquad
\gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}}.
\]

On (s=\tfrac12+it), the charts are conjugate and
(|\gamma_p|=1).  They must remain tagged (+) and (-), with
(gamma_p) as the authorized sewing constructor.  Treating them as
unlabelled linear coordinates would erase the very local authority that
explains the half offset.

The local seam establishes unitary sewing, not global restricted-product
implementability and not a zero-selection law.

## Cross-sector consequence

- Crash and Byzantine proofs cannot be spanned into a hybrid proof.
- Source-wall and gradient-pivot homotopies cannot be added without an
  admitted crossing.
- Separately safe physical schedules cannot be superposed into a
  common-cause-safe schedule.
- Endpoint, gamma, and prime channels cannot be independently combined
  without their named coherence constructor.

