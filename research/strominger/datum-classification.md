# The datum side is classified: four character classes, two reciprocity classes

Companion to `checkers/datum_classification_checks.py` (groups CLS1,
CLS2, CLS3, CLS4, NEC, ELAW, MECH, LIN; 101/101, exit 0; results in
`results/datum_classification.json`). This packet closes the last open
flank of the fold engine. The variation audit (`variation-audit.md` §3)
certified that the character theorem is free inside the even anchor
datum class \(z^{-2}(u^{k}+u^{-k})\); the gauge-mechanism arc
(`gauge-mechanism.md`) classified the connection side (unique modulo
invariant gauge, all grades). What remained was the datum side itself:
*which data give monomial characters at all?* Because the engine is
**linear** in the datum — chain, readouts, and \(P\) are all linear —
the admissible datum space is a union of character eigenspaces, and the
classification is exact linear algebra rather than sampling.

## 1. The defect map

For datum \(D\) and grade \(g\), compute the readouts \(E_g, M_g\) and
the ratios \(R_X=P(X)/X\). A datum is *admissible* if both ratios are
monomial in \(u\) at every grade — then the readouts are
\(P\)-eigenfunctions with monomial characters. Probing monomial data
\(D=z^{-a}\bar z^{m}\) over a wide grid (scratches `_scratch_datum1-4`)
gave a sharp picture: everything probed is either Blaschke
(non-monomial), grade-unstable (monomial at one grade, dead at the
next), or a member of exactly **four grade-stable classes**.

## 2. The four classes

| class | datum | \(R_E\) | \(R_M\) | dim |
|---|---|---|---|---|
| anchor even | \(z^{-2}h(u)\), \(h(1/u)=+h(u)\) | \(+u^{g+2}\) | \(-u^{g+3}\) | \(\infty\) |
| anchor odd | \(z^{-2}h(u)\), \(h(1/u)=-h(u)\) | \(-u^{g+2}\) | \(+u^{g+3}\) | \(\infty\) |
| constant | \(c\) | \((-1)^{g}\) | \((-1)^{g}u^{2}\) | 1 |
| \(z^{-4}\) point | \(c\,z^{-4}\) | \((-1)^{g}u^{2g+4}\) | \((-1)^{g}u^{2g+4}\) | 1 |

Certified: anchor classes for \(k\le3\) at \(g=2,3,4\) and \(k=4,5\) at
\(g=2,3\) (CLS1: 26 checks; CLS2: 18); constant class at \(g=2..5\)
plus scale (CLS3: 10); \(z^{-4}\) class at \(g=2..5\) plus scale (CLS4:
10); linearity within classes (LIN: 4).

Three structural facts stand out:

- **The datum parity flips both character signs.** The unified anchor
  law is \(R_E=\varepsilon u^{g+2}\), \(R_M=-\varepsilon u^{g+3}\) with
  \(\varepsilon\) the \(u\leftrightarrow1/u\) parity of \(h\). The odd
  class is a full second monomial sector the audit never saw.
- **The constant datum is the unique trivially permitted readout.**
  Its electric character is exactly \((-1)^{g}\): at even grades
  \(P(E_g)=+E_g\), a \(P\)-invariant readout with no square-root gate
  at all. Neither anchor class ever has character \(1\) (their exponents
  shift with \(g\)); the \(z^{-4}\) class has both sectors at
  \((-1)^g u^{2g+4}\), never \(1\). This is the concrete bridge to the
  activation question (permitted vs actualized): datum choice moves a
  sector from "passes the cocycle gate" to "invariant on the nose".
- **Both point classes are rigid.** The constant class is one-
  dimensional (u-only non-constant data \(u\), \(u+u^{-1}\), \(u^{2}\)
  are all Blaschke), and the \(z^{-4}\) class dies under any nontrivial
  \(h(u)\) factor. The tower \(z^{-2\ell}\) stops at \(\ell=2\):
  \(z^{-6}\) is Blaschke already at \(g=2\).

## 3. The mechanism: two reciprocity classes (MECH)

The anchor families are explained by the same induction that powers the
gauge theorem. With datum \(z^{-2}h(u)\) the fold keeps the closed form

\[
\operatorname{fold}_g=(1+u)^{-2(g+1)}\,z^{-(g+2)}\,N_g(u),
\]

and \(N_g\) obeys the **signed reciprocity**

\[
N_g(u)=\varepsilon\,(-1)^{g}\,u^{2(g+1)}\,N_g(1/u),
\qquad \varepsilon=\text{parity of } h,
\]

certified exactly at \(g=1,2,3\) for both parities (6 checks). The seed
is \((1+u)^{2}h(u)\): since \((1+u)^{2}\) is self-reciprocal with weight
\(u^{2}\), the seed lies in the reciprocal class iff \(h\) is even and
in the anti-reciprocal class iff \(h\) is odd — and the baseline engine
transmits the class through every grade (the pivot shift is
sign-blind). The two character classes of the readouts *are* the two
reciprocity classes of the fold.

## 4. Necessity (NEC)

Within the anchor family, definite parity is necessary: mixed-parity
\(h=u^{2}+u^{-2}+(u-u^{-1})\) is Blaschke in both sectors at \(g=2,3\)
(the sum of two different characters cannot be monomial), and
single-power \(h=u^{k}\) kills the magnetic sector. Outside the
families: \(z^{-6}\), u-only data, and the sporadic \(g=2\) classes all
fail — the \(\bar z^{-2}\) "class" \((+u^{2},+u^{2})\) exists only at
\(g=2\) and dies at \(g=3\) (the magnetic readout vanishes identically),
as do the \(g=2\) magnetic-zero data \(z^{-a}\bar z^{a+1}\). Grade
stability is the filter that separates the four classes from accidents.

## 5. The E-sector law (ELAW)

The electric sector alone is far more permissive. For
\(D=z^{-a}\bar z^{m}\) with \(a\in\{0,2,4\}\):

\[
R_E=(-1)^{\,m+g(a/2+1)}\,u^{(a/2)(g+2)-m},
\]

certified at 12 \((a,m,g)\) points; outside \(a\in\{0,2,4\}\) the
electric ratio is Blaschke too. The magnetic sector is the real filter
of the classification — it is monomial only in the four classes.

## 6. The completed engine classification

\[
\boxed{\;\text{monomial characters}
\iff
\begin{cases}
\text{datum: one of the four classes (two families, two points)},\\
\text{weights } s=2,3,\dots,g+1,\\
\text{connection } \Gamma=-2\bar z/(1+u)+\partial_z\varphi,\;
\varphi(u)=\varphi(1/u).
\end{cases}\;}
\]

The engine's explanatory content is now fully located: a reciprocity
class (datum side), a gauge-equivalence class (connection side), and an
exact weight law. The variation audit's certificate held over 8
variants; this packet upgrades the datum clause from "the audited even
class works" to the four-class classification with mechanisms and
necessity witnesses.

Honest scope: the classification is certified over the probed space
(monomial data \(z^{-a}\bar z^{m}\) in a wide grid, Laurent \(h\) with
\(|k|\le5\), the named combos) and to the certified grades. A
sixth class hiding outside the grid, or an anchor-family member with
\(|k|>5\) failing at some \(g>4\), are the live falsifiers. The
mechanism (signed reciprocity transmitted by the induction) makes
large-\(k\), large-\(g\) failure structurally implausible but is
certified ingredient-by-ingredient at \(g\le3\).

## 7. Falsifiers

- Any datum outside the four classes with monomial characters stable
  across two consecutive grades refutes the classification.
- Any anchor-family datum failing its class characters at some grade
  refutes the reciprocity mechanism.
- Any mixed-parity \(h\) with monomial ratios refutes necessity.
- A u-only non-constant datum with the constant-class characters
  refutes rigidity of the point classes.

## 8. Checker

`checkers/datum_classification_checks.py`, 101/101, exit 0; results
`results/datum_classification.json`. Groups: CLS1 (26), CLS2 (18),
CLS3 (10), CLS4 (10), NEC (15), ELAW (12), MECH (6), LIN (4). Scratch
precursors: `_scratch_datum1.py` (defect map), `_scratch_datum2.py`
(extension), `_scratch_datum3.py` (stability), `_scratch_datum4.py`
(family extent), logs beside them.
