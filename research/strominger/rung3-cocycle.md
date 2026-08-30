# Rung 3: the sub-subleading diagonal-parity cocycle — per-channel F2, determinant lines, and the birthplace of the odd-parity obstruction

Companion to `checkers/rung3_cocycle_checks.py` (groups K1–K5, 61/61,
exit 0; results in `results/rung3_cocycle.json`). This packet extends the
diagonal-parity cocycle object of the descent-gate arc
(`diagonal-parity-cocycle.md`, rung 0: \(F\) with \(F\sigma(F)=(z\bar z)^{-2}\))
to rung 3, the sub-subleading Cachazo–Strominger \(S^{(2)}\), on top of the
grounded rung-3 angular bridge (`rung3-s2-bridge.md`, checks R1–R4).

The rung-3 bridge ended with an open structural question. The magnetic
readout carries an ODD character, \(P(M_3)=-u^{7}M_3\), so the third
square-root gate fails on the magnetic line (R3). Is that odd parity
inherited from the coefficient line — a property of the \(S^{(2)}\) soft
factor itself — or is it manufactured by the readout projection onto the
anchor datum? This packet builds the rung-3 cocycle and settles the
question exactly.

## 1. The coefficient line (K1)

The line is the grounded \(S^{(2)-}\) per-leg operator datum of R1.2/R1.3:
five nonzero channels

\[
K^+\in\{c_{z_k},\;c_{E_k},\;A^{(2)}_{z},\;A_{zE},\;A^{(2)}_{E},\;A^{(1)}_{z}\}
\]

with \(K^-=\sigma(K^+)\) and the deck involution \(\sigma(K^-)=K^+\)
certified per channel. The first-order electric channel vanishes
identically, \(A^{(1)}_E=0\) (grounded), so the \(A^{(1)}\) line is
magnetic-only — remembered below, where it becomes the odd one out.

## 2. The per-channel cocycle (K2)

With \(P=\alpha\circ\sigma\) and \(\sigma,\alpha\) commuting,
\(F_2=\alpha(K^+)/K^-=P(K^-)/K^-\). Every channel carries a rational
cocycle in factored closed form:

\[
\begin{aligned}
c_{z_k}:&\quad F_2=\frac{z}{\bar z}\Big(\frac{1+\bar z z_k}{\bar z-\bar z_k}\Big)^{\!2}
&
c_{E_k}:&\quad F_2=-\frac{z}{\bar z}
\\
A^{(2)}_z:&\quad F_2=\frac{z^2(z-z_k)(1+\bar z z_k)^3}{\bar z^2(\bar z-\bar z_k)^3(1+z\bar z_k)}
&
A_{zE}:&\quad F_2=-\frac{z^2(z-z_k)(1+\bar z z_k)}{\bar z^2(\bar z-\bar z_k)(1+z\bar z_k)}
\\
A^{(2)}_E:&\quad F_2=\frac{z^2(z-z_k)(\bar z-\bar z_k)}{\bar z^2(1+\bar z z_k)(1+z\bar z_k)}
&
A^{(1)}_z:&\quad F_2=-\frac{z^2(z-z_k)(1+\bar z z_k)^2}{\bar z(\bar z-\bar z_k)^2(1+z\bar z_k)}
\end{aligned}
\]

and each satisfies the full rung-0 axioms, certified exactly (K2.*.b–d):

\[
P(K^+)=\sigma(F_2)\,K^+,\qquad
P(K^-)=F_2\,K^-,\qquad
\alpha(F_2)\,\sigma(F_2)=1 .
\]

## 3. The determinant lines (K3)

With the \(\sigma\)-invariant leg factor
\(X=\dfrac{(1+z\bar z_k)(1+\bar z z_k)}{(z-z_k)(\bar z-\bar z_k)}\)
(\(\sigma(X)=X\), certified), the determinant lines are

\[
F_2\,\sigma(F_2)=\;\underbrace{X^2}_{c_{z_k}},\;\underbrace{1}_{c_{E_k}},\;
\underbrace{X^2}_{A^{(2)}_z},\;\underbrace{1}_{A_{zE}},\;
\underbrace{X^{-2}}_{A^{(2)}_E},\;\underbrace{u\,X}_{A^{(1)}_z},
\qquad u=z\bar z .
\]

Three exact consistency facts (K3.pairing, K3.rung0):

- the \(C\)-operator channel and its quadratic descendant agree pairwise:
  \(\det(c_{z_k})=\det(A^{(2)}_z)=X^2\) and
  \(\det(c_{E_k})=\det(A_{zE})=1\);
- the mixed channel is the rung-0 cocycle in disguise:
  \(F_2(A_{zE})=-z^2\,\sigma(F_0)\) with \(F_0\) the rung-0 cocycle, whose
  determinant \(F_0\sigma(F_0)=u^{-2}\) is re-certified;
- every determinant is \(\sigma\)-invariant, and every diagonal
  u-valuation \(\operatorname{val}_u=\operatorname{val}_z+
  \operatorname{val}_{\bar z}\) (exact order of vanishing along the
  diagonal \(u=0\)) is EVEN: \(0,0,0,0,0\) and \(2\) for \(uX\) — the
  explicit single \(u\) in the \(A^{(1)}_z\) determinant is accompanied by
  the diagonal leg pole, so \(\operatorname{val}_u(uX)=2\), not \(1\).

## 4. The intrinsic-oddness lemma (K4)

For any rational \(h\), \(\sigma\) exchanges the two diagonal valuations,
so \(\operatorname{val}_u(\sigma h)=\operatorname{val}_u(h)\) and

\[
\operatorname{val}_u\!\big(h\,\sigma(h)\big)=2\operatorname{val}_u(h)
\quad\text{is ALWAYS even.}
\]

Certified on a 10-member generic rational witness family (valuations
\(3,0,2,-2,0,-2,-1,-4,0,-4\), all doubled even). Consequence: no rational
cocycle dressing \(F_2\mapsto hF_2\) can convert an odd-parity character
to even. Odd parity, wherever it appears, is intrinsic — not gauge.

## 5. The verdict (K5)

**The sharp odd-parity prediction is FALSIFIED at coefficient-line level.**
Every rung-3 channel determinant has even diagonal u-valuation, so the
obstruction \(P(M_3)=-u^7M_3\) is NOT inherited from the \(S^{(2)}\)
coefficient line: **the odd parity is born at readout projection.** The
candidate mechanism is visible in the bridge datum identities — the
anchor \(C_{zz}=(u+u^{-1})/z^2\) itself supplies the odd effective
u-power through the \((z^{10}+u^5)\) mixing — flagged as an observation,
not a proof.

The sharper rational-square-root gate separates the channels anyway: five
determinants are rational squares (\(X^2,1,X^2,1,X^{-2}\), roots
\(\sigma\)-invariant) and exactly one is not —

\[
\det\big(A^{(1)}_z\big)=uX,\qquad
\operatorname{val}_z(uX)=1\ \text{odd}\ \Rightarrow\ \text{no rational
square root},
\]

and the failing channel is precisely the one whose electric partner
vanishes identically (\(A^{(1)}_E=0\)). A coincidence worth cherishing:
the only magnetic-only line is the only line whose determinant has
nonzero u-valuation and the only one failing the root gate — the
rung-3 cocycle knows, at coefficient level, which channel the readout
obstruction will shadow.

## Verdict

The rung-3 \(S^{(2)}\) coefficient line carries a per-channel rational
cocycle \(F_2\) with \(\sigma\) deck, twisted diagonal action
\(P(K^\pm)=\sigma(F_2)^{\pm1}K^\pm\), and involutivity
\(\alpha(F_2)\sigma(F_2)=1\) on all five nonzero channels (K1–K2). The
determinant lines are \(X^2,1,X^2,1,X^{-2},uX\) — all of EVEN diagonal
u-valuation (K3) — so the rung-3 magnetic obstruction is born at readout
projection, not inherited (K5). The intrinsic-oddness lemma
\(\operatorname{val}_u(h\sigma(h))=2\operatorname{val}_u(h)\) is proven
(K4), the rung-0 anchor is preserved via \(F_2(A_{zE})=-z^2\sigma(F_0)\)
(K3), and the rational-square-root gate isolates \(A^{(1)}_z\) — the
helicity-degenerate channel — as the unique failure (K5).
