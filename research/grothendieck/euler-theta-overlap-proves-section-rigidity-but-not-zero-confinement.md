# Euler--theta overlap proves section rigidity but not zero confinement

## Question

Can a hostile symmetric multiplier insert an off-critical zero quartet while
preserving the complete source provenance, or does the overlap between the
Euler and theta charts already forbid it?

## Two legitimate charts

The completed source has two presentations.

In the Euler chamber

\[
\Re s>1,
\]

the arithmetic determinant packet reconstructs

\[
F_{\mathrm E}(s)
=
B(s)
\prod_p(1-p^{-s})^{-1}.
\]

The theta/Poisson construction gives a global analytic section

\[
F_{\Theta}(s).
\]

The Tate calculation proves on their common domain that

\[
F_{\Theta}(s)=F_{\mathrm E}(s).
\]

This equality is not a comparison inferred from zero data.  It is the Mellin
evaluation of the same labelled source in two coordinate systems.

## Canonical-section rigidity

Suppose a second global analytic section \(\widetilde F_\Theta\) claims the
same source provenance.  It must satisfy

\[
\widetilde F_\Theta(s)=F_{\mathrm E}(s)
\]

throughout the Euler chamber.  Hence

\[
\widetilde F_\Theta(s)=F_\Theta(s)
\]

on a nonempty open set.  The identity theorem then gives equality on the
entire connected continuation domain.

Equivalently, if

\[
\widetilde F_\Theta=H F_\Theta
\]

and both sections have the same Euler normalization, then

\[
H=1
\]

on the Euler chamber and therefore everywhere.

Thus no nontrivial divisor-bearing hostile multiplier is a presentation
change of the same completed theta/Tate source.

## What source data are essential

The conclusion uses more than the functional equation and real symmetry.  It
uses exact agreement with the labelled Euler reconstruction on an open
domain.  A hostile multiplier can preserve

\[
s\longmapsto1-s
\]

and conjugation symmetry, but it cannot preserve this overlap unless it is
identically one.

This gives a noncircular discriminator: rejection occurs in the zero-free
Euler chamber, before inspecting the hostile zeros.

## Why this is not RH

Section rigidity determines which analytic section belongs to the source.  It
does not constrain the divisor of that section after continuation.  The
actual completed section may still, logically, have off-critical zeros.

Therefore the following statements are distinct:

1. no different divisor can be inserted without changing the source;
2. the source-derived divisor lies on the critical seam.

The first statement now follows from overlap descent.  The second remains the
RH-bearing conservation or exactness theorem.

## Consequence for the determinant packet

The arithmetic determinant-three packet is a chart on the Euler chamber, not
a globally continued triple of scalar functions.  Its primitive component
cannot be continued independently without importing the zeta divisor.

The theta chart supplies the unique global section extending the packet's
reconstruction.  It need not supply globally separate continuations of
\(\tau_1\) and \(\tau_2\).  Demanding those continuations was stronger than
the descent problem and reintroduced circularity.

The correct global object is therefore a section with a graded connection on
the overlap, not three globally scalarized cumulants.

## Revised hard theorem

Canonical-section rigidity is closed.  The remaining theorem must operate on
the actual theta section and prove that an off-seam scalar-null state is
impossible.  Candidate mechanisms include:

- a source-derived conserved current for the doubled tail system;
- completion-stable exactness of a source complex;
- or a positive full-sheet relationship energy whose boundary flux vanishes.

None may be replaced by further provenance arguments: provenance now fixes
the section but supplies no sign or transversality law for its zeros.

## Falsifier

This rigidity claim fails only if two distinct global analytic sections can
agree with the same exact Euler reconstruction on an open subset.  The
identity theorem excludes that under the stated analyticity and connectedness
hypotheses.

Its scope is falsified, rather than its proof, if a proposed alternative
changes the source normalization or agrees only asymptotically rather than
exactly in the Euler chamber.

## Result

The Euler--theta overlap makes the completed section unique.  Hostile
divisor-bearing multipliers are not authorized changes of presentation.  The
remaining RH problem is purely zero confinement for this already rigid
section.
