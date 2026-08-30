# The rung-4 fold grade is forced, not assigned: grade 7, weight start −2, and the derived electric obstruction

Companion to `checkers/rung4_foldgrade_checks.py` (groups H, F1–F8, 13/13,
exit 0; results in `results/rung4_foldgrade.json`). This packet closes the
last conditional clause of the rung-4 arc (`rung4-vtower.md`): the readout
migration was stated *conditional on the fold-grade assignment* \(g=5\).
The fold computation says the assignment guess was wrong — and the verdict
survives, upgraded from conditional to derived.

**Epistemic discipline (stated once, applied throughout).** A finite fiber
is not a singleton fiber: every uniqueness/minimality claim below carries
its scan domain explicitly; nonzero claims are proved by exact rational
witness evaluation; zero claims are certified symbolically in a reduced
ring whose faithfulness is itself certified first (group H). Witness-level
observations (F6) are labeled scan results and never appear in theorem
statements.

## 1. The question and the naive answer, refuted

The grounded rungs fold to pure deltas at grade = order + 2 with weight
start \(w_0=1-\text{order}\): rung 2 at (3, 0), rung 3 at (4, −1) —
\(w_0=-1\) itself selected by scan at rung 3 (T3.4b). The naive
extrapolation to rung 4 (order 3) is \((5,-2)\). It is **refuted**
(F2–F4):

- Grade 4, any \(w_0\in\{-4..4\}\): no channel closes (witness-proven).
- Grade 5, \(w_0=-1\): exactly the **depth ≥ 1 channels**
  \((2,0),(1,1),(1,0)\) close — *certified* — while the principal
  depth-0 sector \((3,0),(2,1),(1,2),(0,3)\) stays open
  (witness-proven).
- Grades 5 and 6 at \(w_0=-2\): nothing closes (witness-proven).

The depth split is structural: the \(V\)-differentiated sector already
admits the rung-3 prescription at grade 5; the principal symbol
\(c\otimes c\otimes c\) does not.

## 2. The forced pair (F5)

At **grade 7, \(w_0=-2\)** all seven rung-4 channels fold to pure deltas:

\[
\text{regular part of } D_z^{7}\bigl(G\,( \bar z-\bar z_k)^{-1}\bigr)
= 0 \quad\text{in every channel, certified.}
\]

Certification path: each channel is a pure monomial in \(E_k\)
(\(\sim E_k^{b-1}\)), in \(\omega\) (\(\sim\omega^{1}\)), and is
\(\sqrt2\)-uniform (group H, exact ratio-constancy certificates), so
zero-recognition is without loss in the reduced ring
\(\mathbb Q(z,\bar z,z_k,\bar z_k)\), where the regular parts are
certified to vanish exactly. The weight start is the **unique**
full-closure value within the declared scan \(w_0\in\{-4..4\}\)
(F5.unique, witness scan), continuing the rung pattern \(0,-1,-2\).

The closure family (F6, witness-level, labeled): closure persists at
\((8,-2),(9,-2),(9,-3)\); the grounded rung-3 control closes at
\((4,-1)\) minimal and persists at \((5,-1),(6,-1),(6,-2)\); the depth
≥ 1 sector closes at \(w_0=-1\) at every grade ≥ 5. Closure sets are
upward-closed in grade and along the diagonal \((\text{grade}+2,w_0-1)\).

## 3. The derived migration (F7)

With the fold grade forced at \(g=7\), the certified character theorem
(P3 of `readout-parity-mechanism.md`), \(P(E_g)=+u^{g+2}\),
\(P(M_g)=-u^{g+3}\), gives

\[
P(E_7)=+u^{9}\;(\text{odd: electric gate FAILS}),\qquad
P(M_7)=-u^{10}\;(\text{even: magnetic gate passes, root } u^{5}).
\]

The rung-4 square-root obstruction migrates to the **electric** sector —
the same sector verdict as the conditional \(g=5\) statement, now derived
from the computed fold rather than an assumed grade. The verdict is
grade-robust: it holds at every odd grade, so the residual uncertainty in
the exact grade (see below) cannot move the obstruction between sectors.

## 4. What is proved, and what is not

**Proved (certified or witness-proven):**

- The derived rung-4 operator \(V^{3}/\mathrm{den}\) admits the declared
  distributional fold; minimal full-closure pair within the scanned
  family is \((7,-2)\) — certified closure, witness-proven minimality
  over grades \(4\!-\!6\) and \(w_0\in\{-4..4\}\).
- The depth ≥ 1 sector closes at \((5,-1)\) — certified.
- At the forced (odd) grade, the electric readout is gate-obstructed and
  the magnetic readout passes — the migration is derived, not assigned.

**Not proved (labeled):**

- Weight uniqueness is relative to the declared scan range; \(w_0\) is a
  per-rung prescription fixed by closure (same status as rung 3's
  \(w_0=-1\), T3.4b), not a theorem over all integers.
- The F6 family structure is a witness-level observation.
- The identification fold grade = readout grade is the grounded rung-3
  correspondence (both were 4 there) applied to the derived rung; it is
  the declared identification of this arc, stated explicitly.

## 5. The updated rung-4 picture

The rung-4 candidate now stands on: the tower anchor (G1), the
closed-form first-order line (G2), the depth-parity alternation with a
\(\sigma\)-invariant root at rung 4 (G3), tower-wide gauge propagation
(G4), and now a **computed** fold grade whose oddness derives the
electric-sector obstruction (F5, F7). The two alternations of the
V-tower packet are joined by a third ladder: the weight starts
\(0,-1,-2\) and minimal full-closure grades \(3,4,7\) across rungs
2, 3, 4 — the grade jump \(4\to7\) being the first visible cost of the
principal sector's growth.

**Update (2026-08-23).** The grade jump is now explained by a derived
per-channel law: `rung4-foldrule.md` proves that channel \((a,b)\) at
tower order \(n\) closes iff \(2w_0+p\le0\) and grade \(\ge n-2w_0\)
(\(p=a+b\)), minimal pair \((n+2\lceil p/2\rceil,-\lceil p/2\rceil)\) —
the fold is a covariant chain with trivializing connection, diagonal in
\(x=1+u\), with channel support exactly \([-(n-1),p]\). The forced pair
\((7,-2)\) is its \(p=3\) instance and the depth-\(\ge1\) closure at
\((5,-1)\) its \(p\le2\) instance. (An earlier version of this note
stated the fitted rule \(k\ge\max(1,p-1)\); it coincides with the true
law for \(p\le3\) and was corrected at \(p=4\).)

## Verification

`uv run --with sympy python research/strominger/checkers/rung4_foldgrade_checks.py`
— 13/13 checks pass, exit 0; see
`research/strominger/results/rung4_foldgrade.json`.
