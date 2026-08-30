# The Affine Origin Fixes the Fourier Center Phase but Not the Maslov Grade

## Reopened obstruction

The Fourier quarter-turn converts radial order into an oriented two-by-two minor. For ordered positions (q_1<q_2) and frequencies (\xi_1<\xi_2),

\[
\Delta
=
e^{-i(\xi_1q_1+\xi_2q_2)}
-e^{-i(\xi_2q_1+\xi_1q_2)}.
\]

Writing

\[
\mathcal A=(\xi_2-\xi_1)(q_2-q_1),
\qquad
\mathcal C=\frac{(\xi_1+\xi_2)(q_1+q_2)}{2},
\]

gives

\[
\Delta=-2ie^{-i\mathcal C}\sin\left(\frac{\mathcal A}{2}\right).
\]

The earlier metaplectic audit left the center phase (\mathcal C) untyped. The new affine cut origin supplies exactly that missing frame.

## Centering is translation-covariant

Define the centered minor

\[
\widetilde\Delta
=
ie^{i\mathcal C}\Delta
=
2\sin\left(\frac{\mathcal A}{2}\right).
\]

A common position translation (q_j\mapsto q_j+L) changes the raw minor by the transport phase and changes (\mathcal C) by the equal compensating amount. Therefore (\widetilde\Delta) is invariant. The same holds under common frequency translation.

Thus retaining the affine origin does more than repair the Pearson operator. It canonically centers the Fourier comparison cell and removes arbitrary phase-frame dependence from its oriented minor.

## What remains

The centered minor still changes sign whenever (\mathcal A) crosses (2\pi n). Define the crossing grade away from the degeneracy surfaces by

\[
m(\mathcal A)=\left\lfloor\frac{\mathcal A}{2\pi}\right\rfloor.
\]

Then

\[
(-1)^{m(\mathcal A)}\widetilde\Delta
=
2\left|\sin\left(\frac{\mathcal A}{2}\right)\right|.
\]

The positive lifted orientation therefore requires the integer grade as well as the centered scalar minor. Reciprocal pairing retains only the square and erases this grade.

## Consequence for the RH lane

One of the previous source gates is now closed: the center phase is fixed by the same affine-origin metadata already forced by Mellin and Clark covariance.

The remaining metaplectic gate is narrower:

1. construct the crossing grade continuously from labelled theta transport;
2. prove independence from the order of prime-cut refinements;
3. identify its primitive, square, and archimedean boundary increments;
4. show how the graded orientation controls the Krein norm rather than only an individual Fourier minor;
5. prove the grade survives restricted-product completion.

High frequency necessarily crosses infinitely many wrapping surfaces, so a global theorem cannot assert that the grade is always zero. It must conserve or cancel the accumulated crossings in the completed boundary current.

## Scope boundary

This result does not orient the de Branges/Krein integral. It removes a gauge ambiguity from a possible orientation mechanism and isolates the remaining integer-valued obstruction. A manually selected branch would still be circular.

## Verification

The checker `research/grothendieck/checkers/affine_origin_centers_fourier_minor.py` verifies the half-angle formula, invariance under common position and frequency translations, and restoration of lifted orientation by the crossing grade.
