# RH odd moment jet is the oriented front differential

## Question

Does the two-front source merely have the right type for primitive
principal-value cancellation, or does it already construct the required
operation?

## Exact source operation

The inner and outer comoving profiles are (I=H-1) and (O=-H). Their
oriented incidence is

\[
C=O-I=1-2H.
\]

For the Gaussian source,

\[
C'(u)=2e^{-\pi u^2}>0.
\]

This derivative is the required odd moment-jet operation. In Fourier
coordinates the odd front carries an inverse-frequency principal-value
symbol, while the boundary differential contributes the frequency symbol.
Away from the separately retained zero mode, their product is the identity:

\[
(i\xi)\frac{1}{i\xi}=1.
\]

Thus the principal-value singularity is removed exactly before arithmetic
aggregation. The odd orientation is not erased; it reappears as the positive
Gaussian boundary density. This is stronger than cancelling finitely many
asymptotic moments and has no off-grid support ambiguity.

## Arithmetic telescope

At one prime, primitive occupancy is (P_p(r)=1) for valuation (r\ge1),
and valuation excess is (Q_p(r)=\max(0,r-1)). Hence

\[
P_p(r)+Q_p(r)=r.
\]

Coupling both to the same oriented density gives

\[
2(\log p)r e^{-\pi u^2}.
\]

Across the finitely many prime divisors of a label (n), the coefficient is

\[
\sum_p v_p(n)\log p=\log n.
\]

The primitive and repeated-valuation channels therefore do not need separate
principal-value scalar completions. They are consecutive traversals of one
oriented interval tower.

## What this repairs

The earlier moment-tail no-go remains correct for direct scalar pushforward
of the principal-value lane. The source avoids that forbidden operation by
applying oriented boundary incidence first. It changes the carrier from a
singular comparison distribution to a positive bulk density while retaining
the zero-frequency overlap as an independent boundary coordinate.

The local first cumulant and the inverse-frequency image of the von Mangoldt
atom still provide an important coefficient audit. They verify that the
primitive traversal has the determinant coefficient dictated by the source;
they are not counterterms.

## Remaining obstruction

The finite arithmetic kernel is now only the vacuum label (n=1). The live
theorem is no longer primitive principal-value renormalization. It is:

1. vacuum transversality for the doubled endpoint problem;
2. continuity of the full interval tower through the constructor-derived
   completion;
3. retention of the zero-frequency archimedean boundary packet;
4. faithfulness of the zero-state bridge on the completed admissible domain.

A nonzero source-authorized vacuum state satisfying both endpoint conditions
is the finite falsifier. A completion sequence of nonvacuum states with unit
state norm and vanishing full-interval energy is the infinite falsifier.

## Verdict

The two-front geometry does determine the odd moment jet. It is the oriented
front differential, and it removes the inverse-frequency singularity exactly
rather than through fitted moment subtraction. The frontier advances to
vacuum transversality and completion stability of the positive interval
tower.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_odd_front_differential.py
```
