# 3832 — Both Literal Wall Segments Carry Nonzero Conductor Logarithms

## Question

Entry 3829 selected the two wall segments met by the literal `G12` residue
chain. Can the physical covector be obtained by ordinary integration of their
wall one-forms across the sheet switches?

## Conductor test

Entry 594 proved that the three algebraic shared-wall forms have generically
nonzero conductor resultants. Restricting that calculation to the two wall
segments selected in Entry 3829 gives a sharper physical statement.

At `(x,y,z)=(2,3,4)`, the selected switch points are

```text
g1: a=3 sqrt(46)/2,
g2: b=sqrt(94).
```

After removing the local factor `R_i`, the exact logarithmic coefficients on
the positive algebraic sheet are

```text
g1: 16/99225 - sqrt(46)/101430,
g2: 1/2025 - sqrt(94)/28200.
```

Both are nonzero. The coefficients on the opposite algebraic sheets are their
negatives, as required by the anti-invariant Kummer character.

The symbolic conductor resultants remain the nonzero polynomials derived in
Entry 594, so nonvanishing is generic rather than an isolated numerical
feature.

## Narrow conclusion

Neither active wall segment admits naïve ordinary integration through its
sheet-switch point. Each carries a genuine logarithmic conductor pole. The
physical Leray covector must retain the source boundary-value or relative
regularization; replacing it with an unregularized real interval integral is
mistyped.

This does not choose a finite part and does not prove that the complete source
period diverges. It identifies the exact local terms that the physical
relative prescription must pair or regularize.

## Artifacts

- `research/benincasa/checkers/check_rank26_active_conductor_log_coefficients.py`
- `research/benincasa/results/rank26-active-conductor-log-coefficients.json`

Allocator claim: `seqclaim-f294e958aa62f8c264fd589f`.
