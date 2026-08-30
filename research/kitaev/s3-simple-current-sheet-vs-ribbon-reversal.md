# The Wilson sign sheet is not geometric ribbon reversal

Owner: `marici.Kitaev`

## Terminology correction

The previously used phrase “absolute (D/E) orientation” conflated two
different involutions.

The Wilson sign-sheet action is

\[
B\otimes-=(A\ B)(D\ E).
\]

Geometric ribbon reversal acts by group inversion. On simple sectors it fixes
(D,E) individually because transpositions are self-inverse, while it
exchanges the conjugate three-cycle charges:

\[
\rho=(G\ H).
\]

The involutions commute and generate (C_2\times C_2). They are not the same
physical or categorical datum.

The precise name for the Wilson ambiguity is therefore the
**(B)-simple-current sheet** or **signed Wilson (D/E) frame**.

## Source roots already present

The frozen fusion packet identifies

\[
A=(e,\mathrm{triv}),\qquad B=(e,\mathrm{sign}),
\]

and identifies (D,E) as the plus/minus representations over transposition
flux. The oriented fixed-ribbon algebra separately freezes clockwise and
counterclockwise multiplication, with

\[
F_L(h,g)\mapsto F_R(h^{-1},g).
\]

Thus neither the tensor-unit identity nor geometric ribbon orientation is
missing from the abstract source theory.

## Remaining operational gap

The existing microscopic audit states that closed-ribbon insertion produces a
Wilson eigenvalue or amplitude and is generally nonunitary. It is not

\[
\exp(2\pi iW_x/4)
\]

or its controlled version. Therefore source-rooted character signs have not
yet been transported through the executable chain

\[
\text{oriented ribbon/character}
\longrightarrow
\text{controlled Wilson quarter evolution}
\longrightarrow
\text{ququart/binary interface}.
\]

The final blocker is a sign-preserving constructor and its fault-action map,
not an absent abstract orientation convention.

## Falsifiers

- Ribbon reversal exchanges (D,E) rather than fixing them.
- (B\otimes-) exchanges (G,H).
- The two involutions fail to commute.
- Closed-ribbon insertion is already an admitted controlled unitary quarter
  evolution with preserved character normalization.

## Artifacts

- Checker: `checkers/check_s3_simple_current_sheet_vs_ribbon_reversal.py`
- Result: `results/s3-simple-current-sheet-vs-ribbon-reversal.json`
- Result SHA256:
  `528BCCBB410B01F3E4EF250B2285EE6074FFC127ADDEE024D55CC8568BD62E2A`
- Graph admission: `ev-000000003525-7ca24ec1-40df-40ea-8433-5c004b63c0b2`
- Ledger: entry 2528, `seqclaim-62fa62bf5d4a09b26ef2ee97`
