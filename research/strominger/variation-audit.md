# The variation audit: the alternation is a hard-to-vary explanation

Companion to `checkers/variation_audit_checks.py` (groups V0, V1, KILL,
40/40, exit 0; results in `results/variation_audit.json`). This packet
answers the constructor-theoretic question posed over the rung-5 arc
(`rung5-readout.md`): not "does the pattern hold" but **which
transformations of the engine destroy it, and what does that
impossibility explain**. The method is Deutsch's hard-to-vary criterion
made mechanical: perturb every input of the fold engine and certify the
exact fate of the character theorem under each perturbation.

## 1. The audit frame

The claim under audit (`rung5-readout.md` §3-§4): the grade-\(g\)
readouts of the fold engine obey

\[
P(E_g)=+u^{g+2}E_g,\qquad P(M_g)=-u^{g+3}M_g,
\]

and the parity of the exponents forces exactly one obstructed sector per
rung, alternating E, M, E, M on rungs 2, 3, 4, 5. An explanation of this
alternation is *hard to vary* only if changing its details breaks it.
The engine has three inputs:

- the **datum** \(C=(u+u^{-1})/z^{2}\), \(u=z\bar z\);
- the **weights** \(s=2,3,\dots,g+1\) of the fold chain
  \(D_z(f,s)=\partial_z f-s\Gamma f\);
- the **connection** \(\Gamma=-2\bar z/(1+u)\).

Each was perturbed independently; for every variant and grades
\(g=2,3\) (baseline also \(g=4\)) the checker computes the exact ratio

\[
R_X \;=\; P(X)/X,\qquad X\in\{E_g,M_g\},
\]

and certifies four properties: u-diagonality (\(R_X\) a rational
function of \(u\) alone), the norm-1 law, monomiality, and the leading
valuation.

## 2. The universal law: every variant is norm-1 (INV)

Since \(P^{2}=\mathrm{id}\) and \(P(u)=u^{-1}\), any u-diagonal ratio
obeys

\[
\boxed{\;R(u)\,R(1/u)=1\;}
\]

automatically — \(R\) is a *norm-1* (Blaschke-type) rational function.
The checker certifies this for every readout of every variant,
perturbed or not. The general solution is

\[
R(u)=\pm u^{e}\,\frac{f(u)}{u^{d}f(1/u)}
\]

for some polynomial \(f\) of degree \(d\). The whole content of the
character theorem is therefore: **for the actual engine, the Blaschke
factor collapses to 1** — \(f\) is a monomial. The audit asks how
easily that collapse breaks.

## 3. Datum freedom: the theorem is not fine-tuned (V0, V1)

- Baseline (V0): monomial characters \(+u^{g+2}\), \(-u^{g+3}\) exact at
  \(g=2,3,4\) (6 checks).
- Gap variants (V1): \(C_k=(u^{k}+u^{-k})/z^{2}\) for \(k=2,3\) give
  the *identical* characters at \(g=2,3\) (8 checks) — extending the
  datum-independence already proved at \(g=3,4\) in
  `readout-parity-mechanism.md` (P4).
- Scale (V1): \(7\,C\) gives the identical characters (2 checks).

The character theorem is a property of the *invariant datum class*, not
of the anchor point inside it.

## 4. Engine rigidity: every structural perturbation kills the character (KILL)

Five independent perturbations of the weights and connection were
audited at \(g=2,3\):

| variant | perturbation | result |
|---|---|---|
| V2 | weight step 2: \(s=2,4,6,\dots\) | character destroyed |
| V3 | weight start 3: \(s=3,4,5,\dots\) | character destroyed |
| V4 | connection numerator \(-1\): \(\Gamma=-\bar z/(1+u)\) | destroyed |
| V5 | denominator \(1+u^{2}\) | destroyed |
| V6 | denominator \((1+u)^{2}\) | destroyed |

In every case \(R_X\) remains u-diagonal and norm-1 but becomes a
genuine non-monomial rational function (24 checks; e.g. V2, \(g=2\),
electric: \(R_E=u^{4}\,(6u^{4}-6u^{3}+3u^{2}-4u+9)/(9u^{4}-4u^{3}
+3u^{2}-6u+6)\) — a nontrivial Blaschke factor, denominator the
reciprocal polynomial of the numerator). Two finer facts stand out:

1. **The valuations survive.** Every engine perturbation keeps
   \(\operatorname{val}_u R_E=g+2\) and \(\operatorname{val}_u
   R_M=g+3\): the character "wants" to stay at its baseline value; what
   breaks is exactly the collapse of the Blaschke factor to 1.
2. **The norm-1 law never breaks** — it is forced by \(P^{2}=
   \mathrm{id}\), not by the engine. The engine's contribution is
   precisely monomiality.

V7 marks the boundary of the datum class: the single-sheet datum
\(C_{+}=\bar z/z\) (not invariant under the sheet exchange
\(z\to1/z\)) also destroys monomiality and *shifts* the valuations to
\((g,\,g+1)\) — the symmetry class of the datum is load-bearing for the
exponents, the engine for the collapse.

## 5. The certificate

Within the audited 8-variant family (all inputs perturbed
independently, two grades each, exact symbolic ratios):

\[
\text{monomial characters}
\iff
\begin{cases}
\text{datum in the invariant class } (u^{k}+u^{-k})/z^{2}
 \text{ (any } k\ge1\text{, any scale)},\\
\text{weights } s=2,3,\dots,g+1 \text{ exactly},\\
\Gamma=-2\bar z/(1+u) \text{ exactly}.
\end{cases}
\]

The leftward direction is certified by V1; the rightward by V2-V7.
Honest scope: this is a certified certificate over the audited family,
not a classification theorem over all conceivable engines — the
falsifier is any perturbation outside the family that restores
monomiality.

## 6. What the impossibility explains

Constructor-theoretically: the transformation "keep the alternation
while retuning the connection or the weights" is **impossible** — no
rational cocycle dressing can repair it either (the intrinsic-oddness
lemma of `rung5-readout.md` §4, which used only the character, now
stands on inputs certified as non-negotiable). The transformation
"replace the datum inside its invariant class" is **possible** — it
changes nothing. So the alternation of the obstructed sector is not a
coincidence of the anchor \(C\); it is a property of the *engine*: the
connection \(\Gamma\) and the unit increments are where the explanation
lives.

Combined with Nima's typing of the readout problem (invariant readouts
factor through the coinvariants \(M/(P{-}1)M\); a sector with character
\(\chi\neq1\) is annihilated, not repaired), the audit sharpens the
division of labor: the **engine** decides which sector is permitted to
carry nonzero invariant readout at each rung (rigidly — no retuning of
\(\Gamma\) or the weights preserves the pattern), and the **source** must
still decide whether the permitted sector is actually activated.

## 7. Falsifiers

- Any perturbation of \(\Gamma\) or of the weight law that restores a
  monomial character refutes the rigidity half.
- Any datum in the invariant class that changes the characters refutes
  the freedom half.
- Any variant violating \(R(u)R(1/u)=1\) would refute the u-diagonality
  of the readouts themselves (none occurred).

## 8. Checker

`checkers/variation_audit_checks.py`, 40/40, exit 0; results
`results/variation_audit.json`. Groups: V0 (baseline, 6), V1 (datum
freedom, 10), KILL (V2-V7, 24). Scratch precursors:
`_scratch_variation_audit.py` (bounded character scan),
`_scratch_variation_ratios.py` (ratio structure), logs beside them.
