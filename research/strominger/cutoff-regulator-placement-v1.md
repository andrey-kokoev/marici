# Cutoff regulator placement: a failed rewrite and its correction

## Finding

Before evaluating a physical cutoff residual, the [source's observer-factor trace rewrite](../voevodsky/exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md) needs a correction or an additional commutation hypothesis.

The displayed rewrite is not a consequence of cyclicity alone when the finite regulator does not commute with the observer. An exact finite projection counterexample gives:

    original ordered trace = -11/2,
    displayed factorization = -21/4,
    difference = -1/4.

The [checker](checkers/check_cutoff_regulator_placement.py) supplies the counterexample, the correct cyclic formula and a compatible unequal-leg feature reconstruction. **12 checks pass**, including24 exact corrected-identity controls.

These matrices test an algebraic claim. They are **not** substituted for the actual physical cutoff or its Tate scattering symbol. The source's direct unitary conjugation identity is not refuted, and the owning source file was not changed.

## The precise placement error

Write P for the transported cutoff, DeltaQ for the physical/reference projection difference, A and B for the observer factors, and Z for the self-adjoint finite regulator.

The ordered expression is

    T = tr(Z P DeltaQ A B* Z).

Cyclicity gives

    T = tr(B* Z^2 P DeltaQ A).

The source's displayed observer-factor expression is

    T_claimed = tr((Z B)* P DeltaQ (A Z))
              = tr(B* Z P DeltaQ A Z)
              = tr(Z B* Z P DeltaQ A).

Thus the exact defect is

    T - T_claimed
      = tr((B* Z^2 - Z B* Z) P DeltaQ A).

It vanishes under sufficient commutation conditions, but those conditions must be supplied rather than assumed. A special physical model could have an additional trace cancellation; the generic cyclicity argument does not establish it.

## Counterexample with the relevant finite algebraic structure

Let

    P = Z = Q0 = (1/2)[1 1; 1 1],
    V = diag(1,-1),
    QT = V P V*,
    A = diag(1,2), B = diag(3,4).

P,Z,Q0,QT are orthogonal projections. The observer matrices commute and are normal; V is a diagonal unitary phase. Z does not commute with B. The exact values above therefore do not depend on using nonnormal observers or an invalid projection.

This rejects only the unrestricted observer-leg rewrite, not the physical cutoff theorem or the global assembly conjecture.

## Corrected cross-feature construction

With the relative feature satisfying `Psi* J Psi = DeltaQ`, retain

    left = Z^2 B,
    right = A.

Then

    tr(Psi(P left)* J Psi(right))
      = tr(B* Z^2 P DeltaQ A)
      = T.

The two-leg extension `Theta(X)=(Psi(P X),Psi(X))/sqrt(2)` reconstructs the same ordered trace through its Hermitian and skew readout matrices:

    tr(Theta(left)* (K_herm + i K_skew) Theta(right)) = T.

Both channels are retained. The controls include complex phases with a nonzero skew contribution and a non-idempotent self-adjoint regulator. Replacing Z^2 by Z is allowed only for an actual projection.

Because the left and right regulated legs differ, a Hermitian feature readout matrix does not by itself turn this cross expression into a positive or Hermitian form of the original observer arguments. No such promotion is made.

## Remaining physical task

Use the exact transported physical regulator `Ztilde = U Zphysical U*`, with the actual cutoff, Fourier-conjugate cutoff, source observer multipliers, scattering symbol and common domain. Evaluate the packet matrix with the corrected placements, or prove the extra identity that makes the source's displayed placement valid for that specific physical regulator.

The pure-reference calibration and regulator-removal limits remain separate analytic obligations. A symmetric Mellin window, a seam selector or this2x2 control cannot be inserted as the physical regulator without an independent comparison theorem.

```sh
python research/strominger/checkers/check_cutoff_regulator_placement.py
```

- [Matrices, exact defect and corrected formulas](results/cutoff-regulator-placement.json).
- [Verification receipt](results/cutoff-regulator-placement-verification.json).
