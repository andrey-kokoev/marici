# Boundary augmentation is a lifted Picard functor before exponentiation

## Typed transition packet

For finite cutoffs \(X\subset Y\), retain the boundary increment

\[
\Delta_{Y/X}
=
\left(
\Delta C_1,
\Delta C_2,
\Delta C_{\ge3},
\Delta C_\infty
\right)_{Y/X}.
\]

Each coordinate has its own target topology. The primitive coordinate is exponentially rigged, the square coordinate is tempered or Hilbert but non-trace-class, the connected tail is trace-class, and the archimedean coordinate is a boundary current.

For \(X\subset Y\subset Z\), source additivity is componentwise:

\[
\Delta_{Z/X}
=
\Delta_{Z/Y}+\Delta_{Y/X}.
\]

This makes finite cutoffs and their transition packets a category enriched in an additive typed current object.

## Augmentation as a Picard functor

Let \(\ell\) be the source-authorized coherence map that combines the four typed coordinates only after they have been constructed:

\[
\ell(\Delta)
=
\Delta C_1+\Delta C_2+\Delta C_{\ge3}+\Delta C_\infty.
\]

At finite cutoff, the determinant-line transition is

\[
\tau_{Y/X}
=
\exp\bigl(\ell(\Delta_{Y/X})\bigr).
\]

Componentwise additivity gives

\[
\tau_{Z/X}
=
\tau_{Z/Y}\tau_{Y/X}.
\]

Thus finite boundary augmentation is a symmetric monoidal functor from the additive transition category into the Picard groupoid of one-dimensional lines.

The word “authorized” remains essential. The direct sum of typed coordinates does not itself provide \(\ell\). The endpoint–gamma–prime coherence law must supply that comparison.

## Why the logarithmic lift must remain

Exponentiation is not faithful:

\[
\exp(z+2\pi i m)=\exp(z)
\]

for every integer \(m\). Therefore the scalar line transition forgets the winding grade that detects a divisor. The completed object must retain both:

\[
\left(\Delta_{Y/X},\ell(\Delta_{Y/X}),\tau_{Y/X}\right).
\]

A scalar transition without its lifted logarithmic coordinate cannot distinguish zero winding from a nonzero integral charge.

This also prevents cancellation from erasing type. Two packets may have the same total logarithmic increment while assigning opposite residuals to primitive and archimedean channels. They are not the same source transition unless a declared coherence relation identifies them.

## What finite augmentation proves

At every finite cutoff:

- all transition lines are invertible;
- the transition triangle commutes;
- prime-addition paths telescope;
- Fourier transports the positive and negative line systems;
- the first two anomaly coordinates obey their cyclic recurrence.

None of these statements proves that the completed transition remains invertible.

## Completion obstruction

Let \(t_X\) be a finite trivializing section. A sequence can satisfy

\[
t_X\ne0
\]

at every cutoff while \(t_X\to0\), so the inverses escape. This creates a kernel or divisor at completion even though every finite transition square commutes.

The actual remaining theorem is compact-local stability of the lifted augmentation:

1. the regularized logarithmic connections converge on every compact loop inside an open sector;
2. their primitive and square coordinates remain controlled in their declared topologies;
3. the finite trivializations and their inverses remain bounded in the completed graph topology;
4. the completion map preserves the determinant-line transition class.

Failure of any one condition can create a derived-limit divisor.

## Finite falsifiers

### Exponential alias

The lifted increments \(0\) and \(2\pi i\) have identical scalar exponentials but different winding grades. Any compiler equating them after exponentiation loses the divisor detector.

### Typed cancellation

The packets

\[
(a,0,0,-a)
\quad\text{and}\quad
(0,0,0,0)
\]

have the same scalar total. They are not the same typed transition unless the source coherence law specifically identifies the primitive and archimedean terms.

### Vanishing trivializations

The finite sequence \(t_N=1/N\) consists entirely of invertible scalar trivializations, but \(t_N\to0\) and \(t_N^{-1}\to\infty\). Finite invertibility and path coherence do not survive automatically.

## DPC

A proposed boundary augmentation passes only if:

1. transition packets are retained componentwise;
2. each coordinate stays in its source-defined topology;
3. the combining map is source-authorized;
4. transition composition is verified before exponentiation;
5. the logarithmic lift and winding grade remain attached to the line transition;
6. Fourier comparison commutes with cutoff transitions between the two polarized towers;
7. completion controls both trivializations and inverses on compact open-sector loops;
8. no scalar regularization is used to manufacture the combining map or its convergence.

## Outcome

The finite boundary-augmentation constructor exists categorically once the endpoint–gamma–prime coherence map is supplied. Its algebra is not the remaining RH problem. The unresolved content is the completion-stability theorem for the lifted Picard functor. That is the precise location where an off-seam divisor can still be created.
