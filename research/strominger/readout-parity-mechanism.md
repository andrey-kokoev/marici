# The readout-parity mechanism: where the odd \(u^{7}\) of the rung-3 magnetic obstruction is manufactured

Companion to `checkers/readout_parity_mechanism_checks.py` (groups P1–P6,
16/16, exit 0; results in `results/readout_parity_mechanism.json`). This
packet closes the question left open by the rung-3 cocycle arc
(`rung3-cocycle.md`, checks K1–K5): the coefficient line is exactly even —
every determinant line has even diagonal \(u\)-valuation, and the
intrinsic-oddness lemma forbids any rational cocycle dressing from
manufacturing odd parity — yet the rung-3 magnetic readout carries the odd
character \(P(M_3)=-u^{7}M_3\) (R3.2 of `rung3-s2-bridge.md`). If the
coefficient line cannot supply the oddness, where is it born?

Answer: at the readout projection, and by a mechanism that is forced, not
conventional. The full grade-resolved picture below also upgrades the
certified rung-3 datum identity to its monomial core and produces a
character theorem for the whole readout ladder.

## 1. Setup (P1)

The anchor datum is the \(P\)-invariant spin-2 field
\(C=(u+u^{-1})/z^{2}\), \(u=z\bar z\), with \(P(C)=z^{4}C\) exactly. It
splits into two sheets of definite \(u\)-support,

\[
C=C_{+}+C_{-},\qquad C_{+}=\frac{\bar z}{z}\;(u^{+1}),\qquad
C_{-}=\frac{1}{z^{3}\bar z}\;(u^{-1}),
\]

and \(\sigma\) maps each sheet to the same-\(u\)-support sheet of
\(C_{\bar z\bar z}=\sigma(C)\). Neither sheet is \(P\)-invariant (typed
obstruction P1.3!: the residuals are exactly nonzero and opposite,
\(P(C_\pm)-z^{4}C_\pm=\pm(z-z^{3}\bar z^{2})/\bar z\)) — \(P\)-invariance is
a property of the total datum only.

The grade-\(g\) readouts, on the rank sequence \(2,3,\dots,2+g\), are

\[
E_g=D_z^{g}C+D_{\bar z}^{g}C_{\bar z\bar z},\qquad
M_g=A_g-B_g,\quad A_g=\partial_{\bar z}D_z^{g}C,\quad
B_g=\partial_z D_{\bar z}^{g}C_{\bar z\bar z}=\sigma(A_g) .
\]

Rung 1 is \(g=3\); rung 3 is \(g=4\).

## 2. The monomial closure theorem (P2)

The structural heart of the mechanism is a single grade-indexed identity,
certified exactly for \(g=0,\dots,5\):

\[
\boxed{\;z^{\,g+1}A_g=\bar z^{\,g+1}B_g\;}
\]

- \(g=3\): \(z^{4}A=\bar z^{4}B\) — the certified rung-1 identity (C3.2).
- \(g=4\): \(z^{5}A=\bar z^{5}B\) — the monomial core of the certified
  rung-3 identity: \((z^{10}+u^{5})A=(\bar z^{10}+u^{5})B\) is exactly
  equivalent to it, since \(z^{10}+u^{5}=z^{5}(z^{5}+\bar z^{5})\) (P2.3).

The rung-1 identity does not lift *verbatim* to grade 4 — the typed
obstruction R2.4! is retained exactly (P2.4!) — but the correct lift
exists and is the family above. Alongside it, the separate diagonal
weights are certified at every grade (P2.2):

\[
P(A_g)=z^{2g+4}\bar z^{2}A_g,\qquad
P(B_g)=z^{2}\bar z^{2g+4}B_g .
\]

## 3. The character theorem (P3)

Certified exactly for \(g=0,\dots,5\):

\[
\boxed{\;P(E_g)=+u^{g+2}E_g,\qquad P(M_g)=-u^{g+3}M_g\;}
\]

**Upgrade (2026-08-23).** The theorem is now certified through the
rung-5 grade: `rung5-readout.md` proves \(P(E_g)=+u^{g+2}E_g\),
\(P(M_g)=-u^{g+3}M_g\), the monomial closure, and the diagonal weight
exactly for \(g=0..8\) (checker `rung5_readout_checks.py`, 19/19), via a
closed form for the grade-\(g\) fold whose reciprocity engine makes the
theorem structural rather than a finite-range accident.

which subsumes the whole certified ladder — rung-0 electric \(+u^{4}\)
(\(g=2\)), rung-1 magnetic \(-u^{6}\) (\(g=3\)), rung-3 electric \(+u^{6}\)
and magnetic \(-u^{7}\) (\(g=4\)) — and continues it: \(g=5\) gives
\(-u^{8}\), even again. The parity corollary is immediate:

\[
\text{magnetic square-root gate fails}\quad\Longleftrightarrow\quad
g\ \text{even}.
\]

The gate verdict alternates with the readout fold grade. Rung 1 passes
because \(g=3\) is odd; rung 3 fails because \(g=4\) is even. There is no
new physics in the failure — it is the parity of the grade.

## 4. The datum contributes nothing to the exponent (P4)

Repeating the entire computation for the modified data
\(C_k=(u^{k}+u^{-k})/z^{2}\), \(k=1,2,3\) (all exactly \(P\)-invariant,
\(P(C_k)=z^{4}C_k\)): the monomial closure holds and the characters are
identical, \(+u^{g+2}\) electric and \(-u^{g+3}\) magnetic, at \(g=3,4\).
The datum's \(u\)-support gap does not enter the exponent. The datum
supplies closure; the projection grade manufactures the parity.

## 5. The birth locus (P5)

Per datum *sheet*, the monomial closure holds exactly (P5.1):
\(z^{g+1}A_\pm=\bar z^{g+1}B_\pm\) for \(g=3,4\) — closure is sheetwise
and does not require \(P\)-invariance. But per sheet the magnetic
combination \(M_\pm=A_\pm-\sigma(A_\pm)\) carries no single \(u\)-character
at all (typed obstruction P5.2!: ten candidate monomials
\(\pm u^{g+1},\dots,\pm u^{g+5}\) per sheet per grade, all exact nonzero
residuals). The single character exists only for the \(P\)-invariant
total. It is born exactly at the readout projection.

## 6. The mechanism (P6)

Assembling the certified pieces:

\[
P(M_g)=u^{2}\bigl(z^{2g+2}A_g-\bar z^{2g+2}B_g\bigr)
\]

exactly (P6.1) — before the datum closure is applied, the magnetic
readout carries only the even diagonal factor \(u^{2}\) times a
non-diagonal bracket. The closure \(z^{g+1}A_g=\bar z^{g+1}B_g\) then
collapses the bracket to \(-u^{g+1}M_g\), giving \(-u^{g+3}\). At rung 3
(\(g=4\)) the shift is \(u^{5}\): odd. The closed-form obstruction is
retained exactly (P6.2),

\[
P(M_4)-M_4=-(1+u^{7})M_4 ,
\]

and the W2 witness values reproduce rung3_s2_bridge R2.6 exactly (P6.3).

## Verdict

The rung-3 odd magnetic parity is **born at the readout projection**,
completing the verdict of the cocycle arc:

1. *Coefficient line* (K-arc): every determinant line has even diagonal
   \(u\)-valuation; by the intrinsic-oddness lemma
   \(\operatorname{val}_u(h\sigma(h))=2\operatorname{val}_u(h)\), no
   rational cocycle dressing can manufacture odd parity there.
2. *Readout projection* (this packet): the oddness enters through exactly
   one step — the grade-indexed datum closure
   \(z^{g+1}A_g=\bar z^{g+1}B_g\), whose shift \(u^{g+1}\) has the parity
   of \(g+1\). The character \(-u^{g+3}\) is independent of the datum's
   \(u\)-support (P4) and invisible to either datum sheet alone (P5).

So the obstruction is forced, not conventional: given the grounded
readout grade \(g=4\), the odd exponent \(7\) follows from the projection
structure alone, and no datum choice within the \(P\)-invariant family
\(C_k\) can avoid it. A magnetic readout whose gate passes must sit at an
odd fold grade — as rung 1 does.

Checker: `checkers/readout_parity_mechanism_checks.py`, 16/16 pass,
exit 0. Results: `results/readout_parity_mechanism.json`.
