# Selective Sheet Addressability Is Obstructed by the First Sheet Class

## Sheet local system

The right/left carrier is globally a principal (C_2)-bundle, or equivalently
a rank-two local system with exchange transition functions. Choose local sheet
frames on a cover. On an overlap (U_i\cap U_j), let

\[
t_{ij}\in C_2
\]

record whether the frames agree or exchange the sheets. These transitions form
a Čech one-cocycle.

A global ordered sheet framing exists exactly when there are local gauge bits
(f_i) satisfying

\[
t_{ij}=f_i+f_j\pmod2.
\]

Equivalently, the cocycle class vanishes:

\[
w_1^{\mathrm{sheet}}=[t]\in H^1(X;C_2)=0.
\]

## Selective sign as a twisted section

The one-sheet sign (Z=\operatorname{diag}(-1,1)) changes sign when the two
sheets are exchanged:

\[
XZX=-Z.
\]

It therefore lives in the sign line associated to the sheet bundle. A global
nowhere-zero linear selective operator exists only after trivializing this
line, which has the same obstruction (w_1^{\mathrm{sheet}}). Entry 3766
corrects the corresponding projective claim: (Z) and (-Z) define the same
projective operation, so the projective class ([Z]) descends without such a
trivialization.

## Smallest hostile fixture

Three local charts may each carry a valid ordered sheet frame while their
cycle contains one net exchange. Every pairwise overlap is locally legal, but
the cycle holonomy is odd. No global framing exists. Changing the three local
labels moves the exchange among edges but cannot remove the odd cycle class.

Thus local sheet labels, pairwise comparison maps, and the faithful electric
and magnetic atlas do not imply global selective addressability.

## Refined source question

The next source calculation is topological rather than another matrix census:

```text
Compute the C2 monodromy of the completed magnetic sheet local system.
```

If (w_1^{\mathrm{sheet}}\ne0), a global linear selective lift is impossible
without passing to the orientation double cover or adding a framing. Its
projective class may nevertheless exist. If (w_1^{\mathrm{sheet}}=0), a
global linear framing exists, but authority for the central loop to induce the
selective projective class remains a separate gate.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/sheet_framing_cech_obstruction_checks.py
```
