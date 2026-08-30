# Activation: the invariant readout exists, is unique, and is actualized

Companion to `checkers/activation_checks.py` (results in
`results/activation.json`). This packet answers, on the engine side,
the question Nima's ev-2571 thread left open: not merely which sectors
are *permitted* to carry invariant readout, but whether an invariant
readout *exists, is nonzero, and how many there are*. The datum
classification (`datum-classification.md`) reduced this to inspection:
an invariant readout is a character-1 readout, and exactly one class
has character 1 anywhere — the constant datum, electric sector, even
grades. What remains is to certify the readout itself: its
nonvanishing, its explicit form, and the absence of cross-class
conspiracies.

## 1. Setup

An invariant readout satisfies \(P(X)=X\), i.e. \(R_X=1\) — itself a
monomial character. Hence every invariant readout lives in one of the
four grade-stable classes of the datum classification. Their
characters:

| class | \(R_E\) | \(R_M\) | character 1? |
|---|---|---|---|
| anchor even | \(+u^{g+2}\) | \(-u^{g+3}\) | never |
| anchor odd | \(-u^{g+2}\) | \(+u^{g+3}\) | never |
| constant | \((-1)^{g}\) | \((-1)^{g}u^{2}\) | \(E\), even \(g\) only |
| \(z^{-4}\) | \((-1)^{g}u^{2g+4}\) | \((-1)^{g}u^{2g+4}\) | never |

The candidate is therefore unique: \(E_g\) of the constant datum at
even \(g\). The classification's ratio computations already imply it
is nonzero (a zero readout has no ratio); this arc certifies
invariance and nonvanishing directly, not through a ratio.

## 2. The invariant readout, certified (ACT)

**Invariance, on the nose.** \(P(E)-E=0\) identically at \(g=2,4\), and
\(P(E)+E=0\) identically at \(g=3\) (ACT.INV) — no ratio map involved.

**Actualization.** \(E_g(D{=}1)\neq0\) symbolically, and at the
physical witness \(W2=\{z:3,\ \bar z:2/7\}\) (\(u=6/7\)) it evaluates
to nonzero rationals (ACT.NZ):

\[
E_2|_{W2}=\tfrac{8900}{169},\qquad
E_3|_{W2}=\tfrac{85560}{169},\qquad
E_4|_{W2}=\tfrac{163377480}{28561}.
\]

**Closed form** (ACT.FORM, certified \(g=1..4\)):

\[
\boxed{\,E_g(D{=}1)=\frac{(g+3)!}{6}\,
\frac{z^{g}+\bar z^{g}}{(1+u)^{g}}\,}
\qquad
(4,\ 20,\ 120,\ 840\ \text{for}\ g=1,2,3,4).
\]

The character is now read off by inspection: under \(P\)
(\(z\to-1/z\)), the numerator \(z^g+\bar z^g\) contributes
\((-1)^g u^g\) and the denominator \((1+u)^g\) contributes \(u^g\),
leaving exactly \((-1)^g\). The classification's frozen exponent is
explained, not just observed: the constant datum's readout is the
elementary symmetric object of the fold, and its invariance at even
grade is manifest. Since the character is \(1\), the cocycle's
square-root gate is trivial: \(F=1\) works.

## 3. The rank theorem

Within the probed datum universe (the four grade-stable classes and
their sums):

> The space of data producing an invariant electric readout is exactly
> \(\mathrm{span}\{1\}\) at even grades and \(\{0\}\) at odd grades.
> No datum produces an invariant magnetic readout at any grade.

Engine linearity makes this a statement about character eigenspaces:
an invariant sum requires every component's character to be 1, and
only the constant class has \(R_E=1\) anywhere. The one remaining
loophole — that a cross-class sum might cancel its non-1 parts — is
closed directly (ACT.RANK): for \(D=1+z^{-2}(u+u^{-1})\) and
\(D=1+z^{-4}\), \(P(X)-X\neq0\) in both sectors at \(g=2,3\) (tested
on the readouts themselves, since mixed sums need not be u-diagonal
and the ratio proxy can fail to apply). The magnetic obstruction is
character, not vanishing: every class has \(R_M\neq1\), and the
constant datum's \(M\) is nonzero with \(R_M=u^2\) (ACT.M).

So the engine carries **exactly one trivially permitted invariant
observable, and it is real**: rank 1 at even grades, rank 0 otherwise.
This is the engine-side answer to the rank question of ev-2571;
source-side actualization remains with Nima.

## 4. Falsifiers

- Any non-constant datum (or cross-class sum) with \(P(E)-E=0\) at any
  probed grade.
- Any datum with \(P(M)-M=0\) at any probed grade.
- A failure of the closed form at \(g\ge5\) would confine the theorem
  to the probed range (the coefficient pattern \((g+3)!/6\) predicts
  all grades).
- A counterexample to linearity of the engine in the datum would void
  the eigenspace argument underlying the rank theorem.

## 5. Checker

`checkers/activation_checks.py`, 27/27 pass (exit 0), results in
`results/activation.json`. Groups: ACT.INV (direct invariance),
ACT.NZ (symbolic and witness nonvanishing), ACT.FORM (closed form,
\(g=1..4\)), ACT.RANK (cross-class conspiracy excluded, direct),
ACT.M (magnetic sector never invariant, obstruction is character).
