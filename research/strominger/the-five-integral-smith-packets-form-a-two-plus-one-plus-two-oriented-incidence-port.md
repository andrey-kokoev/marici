# The Five Integral Smith Packets Form a Two-Plus-One-Plus-Two Oriented Port

## Structural classifier

The five exact integral Smith packets are classified without their large
integer values. They form

\[
A_+\sqcup A_-\sqcup B\sqcup C_+\sqcup C_-.
\]

For an endpoint-repeated presentation, define

\[
\omega_A
=
(\text{orientation of the repeated endpoint})
(\text{common tail sign}).
\]

Then \(\omega_A=\pm1\) gives \(A_\pm\).

For a through-repeated presentation with opposite tail polarity, define

\[
\omega_C
=
(\text{orientation of the ordered tail labels})
(\text{sign of the first tail}).
\]

Then \(\omega_C=\pm1\) gives \(C_\pm\).

The equal-polarity through stratum has one packet \(B\); the coupled tail
inversion does not change its exact Smith factors.

## Exact theorem

The map from these five structural classes to the five exact integral Smith
packets is bijective. Their presentation multiplicities are

\[
8,\quad8,\quad8,\quad4,\quad4.
\]

Taking 2-adic valuations forgets both oriented-incidence characters:

\[
A_+,A_-\longmapsto A,\qquad
B\longmapsto B,\qquad
C_+,C_-\longmapsto C.
\]

Thus the passage from five packets to three profiles is not arbitrary
numerical compression. It is precisely the erasure of two source-derived
orientation bits, each supported only on its own stratum.

## Different algebraic support

The two orientation bits do not live at the same layer.

The packets \(A_+\) and \(A_-\) have identical relational Smith factors and
identical first two full Smith factors. They differ only in the terminal full
factor. Thus \(\omega_A\) is supported purely in the full gauge extension and
is invisible after relational quotient.

The packets \(C_+\) and \(C_-\) differ in both their terminal full factor and
their terminal relational factor. Thus \(\omega_C\) survives relational
reduction. Moreover,

\[
\frac{s^{\mathrm{full}}_3(C_+)}
     {s^{\mathrm{rel}}_2(C_+)}
=28^2,
\qquad
\frac{s^{\mathrm{full}}_3(C_-)}
     {s^{\mathrm{rel}}_2(C_-)}
=36^2.
\]

So the endpoint bit is extension-only, whereas the opposite-polarity bit is
already relational.

## Replay

Run:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies seventy-three exact gates.
