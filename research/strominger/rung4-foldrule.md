# The depth-graded fold rule: closure iff \(k\ge\max(1,p-1)\) and grade \(\ge n+2k\), certified through tower order 4

Companion to `checkers/rung4_foldrule_checks.py` (groups H, R1–R5;
results in `results/rung4_foldrule.json`). This packet states the
per-channel closure law of the declared weighted distributional fold,
extracted from the order-2/3 closure table and then **tested against
tower order 4 before being recorded** — the rung-4 forced pair \((7,-2)\)
of `rung4-foldgrade.md` becomes one instance of a single rule.

**Epistemic discipline (stated once, applied throughout).** A finite fiber
is not a singleton fiber: every uniqueness/minimality claim carries its
scan domain explicitly; nonzero claims are proved by exact rational
witness evaluation; zero claims are certified symbolically in the reduced
ring \(\mathbb Q(z,\bar z,z_k,\bar z_k)\) whose faithfulness is certified
first (group H: every channel is a pure monomial in \(E_k\), in \(\omega\),
and \(\sqrt2\)-uniform). The rule was fixed a priori from orders 2–3
(15+ closure/refutation points) and only then applied to order 4 — no
parameter was adjusted after seeing order-4 output.

## 1. The rule

For a tower channel \(\alpha=(a,b)\) at tower order \(n\), with
\(p=a+b\) the number of \(c\)-factors, folding with weight start
\(w_0=-k\):

\[
\text{channel }(a,b)\text{ closes}
\quad\Longleftrightarrow\quad
k\ge \max(1,\,p-1)\ \ \text{and}\ \ \text{grade}\ge n+2k .
\]

Equivalently the minimal closure pair is

\[
(\text{grade}_{\min},\,w_0^{\min})
=\bigl(n+2\max(1,p-1),\;-\max(1,p-1)\bigr).
\]

## 2. What the checker proves

- **H.** Reduced-ring certification is without loss (homogeneity
  certificates, order 4: channels \(\sim E_k^{\,b-1}\), \(\sim\omega^2\),
  \(\sqrt2\)-uniform).
- **R1.** Order-4 census: 11 channels, \(p\)-classes \(5/3/2/1\)
  (\(p=4,3,\le2\)).
- **R2.** Every order-4 channel **closes at its predicted minimal pair**,
  certified: \(p\le2\) at \((6,-1)\); \(p=3\) at \((8,-2)\); \(p=4\) at
  \((10,-3)\).
- **R3.** Sharpness, witness-proven, in both directions: every channel
  stays open one grade below its predicted minimum at the minimal weight;
  and every channel with \(k\ge2\) stays open at weight \(-(k-1)\) even
  one grade *above* that weight's own rule grade — the depth floor
  \(k\ge p-1\) is sharp, not a grade artifact.
- **R4.** The rule re-certified on orders 2 and 3 (all channels, both
  directions), reproducing F3/F5 of the fold-grade arc as instances and
  cross-validating the per-step-cancel fold variant against the
  plain-fold certification of `rung4_foldgrade_checks.py`; the grounded
  rung-3 S2 control closes at \((4,-1)\) and stays open at \((3,-1)\).

## 3. Instances and the rung ladder

The full-operator minimal pair at order \(n\) is the \(p=n\) instance:

\[
(\text{grade}, w_0) = \bigl(3n-2,\;-(n-1)\bigr)
\quad(n\ge2),
\]

giving the ladder: order 2 (rung 3): \((4,-1)\); order 3 (rung 4):
\((7,-2)\); order 4 (rung 5): \((10,-3)\). The grade jump \(4\to7\)
that refuted the naive rung-4 extrapolation is the \(p:2\to3\) instance
of the depth floor; the depth-\(\ge1\) sector's early closure at
\((5,-1)\) is the \(p\le2\) instance.

**Derived rung-5 prediction (labeled as prediction, not yet a certified
readout).** Under the arc's declared identification fold grade = readout
grade, the rung-5 grade \(10\) is even, so the character theorem
\(P(E_g)=+u^{g+2}\), \(P(M_g)=-u^{g+3}\) gives \(P(E_{10})=+u^{12}\)
(even: electric gate passes, root \(u^6\)) and \(P(M_{10})=-u^{13}\)
(odd: magnetic gate FAILS) — the square-root obstruction oscillates
back to the magnetic sector at rung 5. This is the rule's first
falsifiable downstream consequence.

## 4. Mechanism status

**Certified structural fact** (`checkers/vtower_polelaw_checks.py`, 6/6,
exit 0, symbolic, all 22 channels of orders 2–4): every order-\(n\)
channel has \((1+u)\)-pole order **exactly** \(n-1\),

\[
G_\alpha = H_\alpha\,(1+u)^{-(n-1)},\qquad H_\alpha\ (1+u)\text{-free},
\]

and \(G_\alpha(1+u)^{n-2}\) still poles. Pole order is therefore uniform
across a rung and **cannot** be the source of the \(p\)-dependence; the
depth floor \(k\ge p-1\) lives in the numerator structure \(H_\alpha\).

**Candidate hook (open).** The regular part of the fold is the covariant
chain \(D_{w_0+n-1}\circ\cdots\circ D_{w_0}(G)\) with
\(D_w=\partial_z-w\Gamma\), \(\Gamma=-2\bar z/(1+u)\), whose action on
\((1+u)\)-powers is

\[
D_w\,(1+u)^{j} = (j+2w)\,\bar z\,(1+u)^{j-1},
\]

a weighted shift with zeros at \(j=-2w\). Why the composition of these
shifts kills exactly the \(k\ge\max(1,p-1)\), grade \(\ge n+2k\) sector
is the mechanism question, taken up by the next arc.

## 5. What is proved, and what is not

**Proved:** the closure/refutation pattern of Section 1 on every channel
of tower orders 2, 3, 4 (22 channels), closures certified, both
sharpness directions witness-proven; the uniform pole-order law of
Section 4 (`vtower_polelaw_checks.py`, certified).

**Not proved (labeled):** closure-set statements outside the probed
grades/weights are witness-level scan results; the rule is a certified
pattern on orders \(\le4\), not a theorem over all orders; the rung-5
readout oscillation is a prediction under the declared
fold-grade = readout-grade identification, not a certified readout; the
mechanism is open.

## Verification

`uv run --with sympy python research/strominger/checkers/rung4_foldrule_checks.py`
— see `research/strominger/results/rung4_foldrule.json`.
