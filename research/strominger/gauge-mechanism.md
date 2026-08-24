# The invariant-gauge theorem holds at all grades: the mechanism is conjugation

Companion to `checkers/gauge_mechanism_checks.py` (groups OPID, REDUC,
PIVOT, REC, CHAR; 13/13, exit 0; results in
`results/gauge_mechanism.json`). This packet closes the gap left by the
deformation theory (`deformation-theory.md`): there the
character-preserving deformations were classified as exactly the
invariant-exact directions \(\Gamma_0+\varepsilon\,\partial_z\varphi\),
\(\varphi(u)=\varphi(1/u)\), but exactness was *spot-certified* at
grades \(g=2,3\) only. Here the mechanism behind that exactness is
exhibited and certified, and it upgrades the spot checks to a theorem
at every grade.

## 1. The conjugation identity (OPID)

Let \(\Gamma'=\Gamma_0+\varepsilon\,\partial_z\varphi\) with
\(\varphi\) \(P\)-invariant, and let \(D'_s=\partial_z-s\Gamma'\) be a
deformed fold step of weight \(s\). With the group element

\[
G_s=e^{\varepsilon s\varphi},
\qquad \partial_z\log G_s=\varepsilon s\,\partial_z\varphi,
\]

the deformation is cancelled exactly by conjugation:

\[
D'_s\bigl(G_s\,f\bigr)=G_s\,D_s(f),
\qquad\text{i.e.}\qquad
D'_s=G_s\,D_s\,G_s^{-1}.
\]

Certified at **symbolic weight \(s\)** for
\(\varphi=u+u^{-1}\) and \(\varphi=u^{2}+u^{-2}\) against a generic
probe \(f\). The invariant-exact deformation is not merely
infinitesimally special: it is gauge in the literal group-element
sense. The connection transforms as
\(\Gamma\mapsto\Gamma+\partial_z\log G\), and the fold transforms
covariantly.

## 2. The chain reduction (REDUC)

Conjugation telescopes along the fold chain. For the K1 direction
(\(\varphi=u+u^{-1}\), deformation
\(\varepsilon\,\bar z\,(u^{-2}-1)=-\varepsilon\,\partial_z\varphi\)):

\[
\operatorname{fold}_2(\varepsilon)
=e^{-3\varepsilon\varphi}\,
D_3\!\Bigl(e^{\varepsilon\varphi}\,
D_2\!\bigl(e^{2\varepsilon\varphi}\,C\bigr)\Bigr),
\]

and the analogous three-step identity at \(g=3\); both certified
**exactly at symbolic \(\varepsilon\)**. In general:

\[
\operatorname{fold}_g(\varepsilon)
=e^{-(g+1)\varepsilon\varphi}\cdot
\bigl(\text{baseline chain with invariant insertions }
e^{\varepsilon\varphi}\bigr).
\]

The deformed fold is the baseline fold dressed by invariant factors —
nothing else happens.

## 3. Pivot preservation and the induction (PIVOT)

The baseline engine proves the character theorem by an induction whose
step is: the fold numerator \(N_g\) stays in a reciprocity class, and
each fold step shifts the pivot by 1 (`rung5-readout.md` Q3). The
insertions respect exactly this structure:

\[
\bigl(\varphi^{j}h\bigr)(1/u)=u^{-4}\,\bigl(\varphi^{j}h\bigr)(u)
\quad\text{whenever}\quad h(1/u)=u^{-4}h(u),
\]

certified for \(h=(1+u)^{4}(u+u^{-1})\), \(j=1,2,3\). Expanding the
reduced chain order by order in \(\varepsilon\), every order is a
baseline-chain term multiplied by invariant rational factors, which by
PIVOT stay in the same reciprocity class. Hence the baseline induction
lifts verbatim to the whole deformation family:

\[
N_g(u,\varepsilon)=(-1)^{g}\,u^{2(g+1)}\,N_g(1/u,\varepsilon)
\qquad\text{at every grade } g,
\]

and reciprocity of \(N_g\) is exactly what the character theorem reads
off. This is the all-grades statement: the spot checks of
`deformation-theory.md` are instances, not evidence-by-sampling.

## 4. Direct evidence (REC, CHAR)

The induction's conclusion is also verified head-on:

- the deformed fold keeps the closed form
  \(\operatorname{fold}_g(\varepsilon)=(1+u)^{-2(g+1)}z^{-(g+2)}N_g(u,\varepsilon)\)
  with \(N_g\) reciprocal, exactly at symbolic \(\varepsilon\), for
  \(g=1,2,3,4\) (REC);
- consequently the characters
  \(P(E_g)=+u^{g+2}E_g\), \(P(M_g)=-u^{g+3}M_g\) hold exactly at
  symbolic \(\varepsilon\) at \(g=4\) (CHAR) — extending the exact
  certification of `deformation-theory.md` beyond \(g=3\).

## 5. The completed classification

Putting the three arcs together:

\[
\boxed{\;\text{character-preserving deformations of the fold connection}
\;=\;\text{invariant-exact gauge},\ \Gamma\mapsto\Gamma+\partial_z\varphi,
\ \varphi(u)=\varphi(1/u),\ \text{at every grade}\;}
\]

- *Only these*: the first-order kernel is exactly the invariant-exact
  directions (`deformation-theory.md` KER1, both sectors), and the
  asymmetric control fails exactly.
- *All of these, at all grades*: the deformation is conjugation by
  \(e^{\varepsilon s\varphi}\) (OPID), the chain reduces to the
  baseline chain with invariant insertions (REDUC), the insertions
  preserve the reciprocity class (PIVOT), so the baseline induction
  lifts (REC, CHAR).

The character theorem is therefore a statement about a single
gauge-equivalence class of connections, established at every grade —
not a property of a tuned representative. Combined with the uniqueness
of the strength \(c=2\) and the rigidity of the weights
(`deformation-theory.md` UNIQ, WGHT), the engine is fully classified
on the connection side: unique modulo invariant gauge.

Honest scope: the classification of the kernel is first-order and
within the audited Laurent span (\(k=-4..2\), \(g=2\)); the exactness
half is now grade-general but direction-specific (certified for the
\(\varphi=u+u^{-1}\) and \(u^{2}+u^{-2}\) members, with the conjugation
identity itself certified at symbolic \(s\) — the mechanism is
direction-generic, the chains are certified per member).

## 6. Falsifiers

- An invariant-exact direction \(\partial_z\varphi\),
  \(\varphi=\varphi\circ(u\leftrightarrow1/u)\)-invariant, whose
  conjugation identity \(D'_s=G_sD_sG_s^{-1}\) fails — the identity is
  algebraic in \(\partial_z\log G_s\), so a failure would mean the
  deformation is not a pure connection shift.
- A grade \(g\ge5\) where the deformed \(N_g(u,\varepsilon)\) fails
  reciprocity (REC is the direct probe).
- A character-preserving direction outside the invariant-exact class
  (refutes the kernel half, as before).

## 7. Checker

`checkers/gauge_mechanism_checks.py`, 13/13, exit 0; results
`results/gauge_mechanism.json`. Groups: OPID (2), REDUC (2), PIVOT (3),
REC (4), CHAR (2). Scratch precursors: `_scratch_deform4.py`,
`_scratch_deform5.py` (multiplicative-insertion dead end),
`_scratch_deform6.py`, logs beside them.
