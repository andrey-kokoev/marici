# The fold law, derived: closure iff \(2w_0+p\le0\) and grade \(\ge n-2w_0\) — mechanism, support law, and certification through tower order 4

Companion to `checkers/rung4_foldrule_checks.py` (groups H, M, S, R1–R5;
results in `results/rung4_foldrule.json`). This packet states the
per-channel closure law of the declared weighted distributional fold and
its **derivation**: the fold is a covariant chain whose connection
trivializes; in \(x=1+u\) coordinates it is a diagonal operator with an
explicit kernel; the channel support is exactly \([-(n-1),\,p]\); the
closure rule is the arithmetic consequence. The rung-4 forced pair
\((7,-2)\) of `rung4-foldgrade.md` is one instance.

**Correction recorded.** An earlier version of this packet stated the rule
\(k\ge\max(1,p-1)\), fitted to the order-2/3 closure table. That rule
coincides with the true one for all \(p\le3\) — every datum then in hand —
and is **refuted at \(p=4\)**: the five order-4 \(p=4\) channels close at
\((8,-2)\), not first at \((10,-3)\) (certified; grade 7 open,
witness-proven). The mechanism below explains why the true floor is
\(\lceil p/2\rceil\).

**Epistemic discipline (stated once, applied throughout).** A finite fiber
is not a singleton fiber: every minimality claim carries its probe
explicitly; nonzero claims are proved by exact rational witness
evaluation; zero claims are certified symbolically in the reduced ring
\(\mathbb Q(z,\bar z,z_k,\bar z_k)\) whose faithfulness is certified first
(group H). The support law (group S) is certified **unreduced**.

## 1. The law

For a tower channel \(\alpha=(a,b)\) at tower order \(n\), with
\(p=a+b\) the number of \(c\)-factors, folding with weight start
\(w_0\):

\[
\text{channel }(a,b)\text{ closes at }(\text{grade }g,\,w_0)
\quad\Longleftrightarrow\quad
2w_0+p\le 0\ \ \text{and}\ \ g\ge n-2w_0 .
\]

With \(w_0=-k\): the depth floor is \(k\ge\lceil p/2\rceil\), the minimal
closure pair is

\[
(\text{grade}_{\min},\,w_0^{\min})
=\bigl(n+2\lceil p/2\rceil,\;-\lceil p/2\rceil\bigr).
\]

Every tower channel has \(p\ge1\), so **no channel ever closes at
\(w_0=0\)** — the grounded-weight observations are explained.

## 2. The mechanism (checker group M)

The regular part of the weighted fold is the covariant chain

\[
D_{w_0+g-1}\circ\cdots\circ D_{w_0}\,(G),
\qquad D_w=\partial_z-w\Gamma,\quad
\Gamma=-\frac{2\bar z}{1+u},
\]

certified identity (M2) on every order-2/3 channel at two \((g,w_0)\)
pairs each. The connection **trivializes** (M1):
\(D_w=S^{-w}\partial_z\,S^{w}\) with \(S=(1+u)^2\). Setting \(x=1+u\), the
chain collapses (M3) to

\[
\bar z^{\,g}\;x^{-2(w_0+g-1)}\;
\bigl(\partial_x M_{x^2}\bigr)^{g-1}\partial_x\,
\bigl(x^{2w_0}G\bigr),
\]

and \(\partial_x M_{x^2}\) is **diagonal on monomials** (M4):
\(x^e\mapsto(e+2)x^{e+1}\), so the coefficient of \(x^e\) in
\(x^{2w_0}G\) acquires the factor \(e(e+1)\cdots(e+g-1)\). The kernel of
the operator on Laurent polynomials is exactly (M5)

\[
\operatorname{span}\{x^{-(g-1)},\dots,x^0\},
\]

hence: closure iff \(\operatorname{supp}(x^{2w_0}G)\subseteq
\{-(g-1),\dots,0\}\) — pure support arithmetic. The intuitive hook
recorded earlier,
\(D_w(1+u)^j=(j+2w)\bar z(1+u)^{j-1}\), is the same statement one step
at a time: each chain step shifts \(x\)-degree down by 1 and kills the
resonant exponent \(j=-2w\).

## 3. The support law (checker group S, unreduced)

For every channel of orders 2, 3, 4 (22 channels), the exponent support
of \(G\) as a Laurent polynomial in \(x=1+u\) is **exactly the full
range**

\[
\operatorname{supp} G=[-(n-1),\,p],
\]

edges attained, no interior gaps. The lower edge is the previously
certified \((1+u)\)-pole law (`vtower_polelaw_checks.py`, 6/6). The upper
edge \(p\) is structural: in \(x\)-coordinates each \(c\)-factor has
\(x\)-degree exactly 1 with a nonzero leading coefficient
(\(c_{z_k}\propto(z-z_k)^2/x\), \(c_{E_k}\propto(z-z_k)(1+z\bar z_k)/x\)),
\(V\)-derivatives never raise \(x\)-degree, and the top and bottom edge
coefficients factor into single terms (monomials in \(E_k,\omega,\bar z_k\)
times powers of \(\bar z_k z_k+1\), \(z\bar z_k+1\), \(\bar z-\bar z_k\)),
so no cancellation is possible.

Multiplying by \(x^{2w_0}\) shifts the support to
\([2w_0-(n-1),\,2w_0+p]\); membership in
\(\{-(g-1),\dots,0\}\) is \(2w_0+p\le0\) and \(g\ge n-2w_0\) — the law of
Section 1.

## 4. What the checker proves

- **H.** Reduced-ring certification is without loss (homogeneity
  certificates, order 4).
- **M1–M5.** The mechanism of Section 2: connection trivialization
  (symbolic \(w\)); fold = covariant chain (22 channel-pair identities,
  orders 2–3); \(x\)-space chain form (sample); diagonal monomial action
  (\(m=1..4\), exponents \(-6..5\)); kernel identification
  (\(g=2..5\), exponents \(-8..7\)).
- **S.** The support law, unreduced, all 22 channels of orders 2–4,
  including the pole law as the denominator side.
- **R1.** Order-4 census: 11 channels, \(p\)-classes \(5/3/2/1\).
- **R2.** Every channel of orders 2, 3, 4 **closes at the law's minimal
  pair**, certified: order 2 all at \((4,-1)\); order 3: \(p\le2\) at
  \((5,-1)\), \(p=3\) at \((7,-2)\); order 4: \(p\le2\) at \((6,-1)\),
  \(p=3\) **and** \(p=4\) at \((8,-2)\).
- **R3.** Sharpness, witness-proven, both directions: every channel stays
  open one grade below its minimum at the minimal weight; and every
  channel stays open one weight **shallower at the same grade** — the
  weight gate \(2w_0+p\le0\) fails there independent of grade.
- **R4.** Grounded rung-3 S2 control: closes at \((4,-1)\), open at
  \((3,-1)\) — the independent grounded fold matches the order-2 pattern.

## 5. Instances and the rung ladder

The full-operator minimal pair at order \(n\) is the \(p=n\) instance,
\((\text{grade},w_0)=(n+2\lceil n/2\rceil,\,-\lceil n/2\rceil)\):
order 2 (rung 3): \((4,-1)\); order 3 (rung 4): \((7,-2)\);
order 4 (rung 5): **\((8,-2)\)** — not \((10,-3)\) as the refuted rule
predicted. The grade jump \(4\to7\) that refuted the naive rung-4
extrapolation is the \(p:2\to3\) instance of the depth floor; the
depth-\(\ge1\) sector's early closure at \((5,-1)\) is the \(p\le2\)
instance.

**Derived rung-5 prediction (labeled as prediction, not yet a certified
readout).** Under the arc's declared identification fold grade = readout
grade, the rung-5 grade is \(8\) (even), so the character theorem
\(P(E_g)=+u^{g+2}\), \(P(M_g)=-u^{g+3}\) gives \(P(E_8)=+u^{10}\)
(even: electric gate passes, root \(u^5\)) and \(P(M_8)=-u^{11}\)
(odd: magnetic gate FAILS) — the square-root obstruction sits on the
magnetic sector at rung 5. (The refuted rule's grade 10 was also even;
the gate prediction is unchanged, the grade is corrected.)

**Upgrade (2026-08-23, certified).** The prediction above is now a
certified readout: `rung5-readout.md` proves the character theorem
through grade 8 via the fold closed form and its reciprocity engine
(checker `rung5_readout_checks.py`, 19/19), confirming
\(P(E_8)=+u^{10}\) (gate passes) and \(P(M_8)=-u^{11}\) (gate FAILS,
obstruction \(P(M_8)-M_8=-(1+u^{11})M_8\) exact, unrepairable by
rational cocycle dressing).

## 6. What is proved, and what is not

**Proved:** the mechanism identities M1–M5 (chain identity certified on
orders 2–3 and the \(x\)-space form on a sample; the diagonal action and
kernel are order-independent symbolic facts); the support law on every
channel of orders \(\le4\), unreduced; the closure law of Section 1 on
every channel of orders 2, 3, 4, closures certified, both sharpness
directions witness-proven; the refutation of the old \(k\ge p-1\) rule
at \(p=4\).

**Not proved (labeled):** the rung-5
readout oscillation is a prediction under the declared
fold-grade = readout-grade identification, not a certified readout.
**(Closed 2026-08-23: certified in `rung5-readout.md` — the
identification itself remains declared, same status as rungs 3–4.)**

**Upgrade (all-\(n\) theorem).** The one gap above — the law as a
theorem over **all** tower orders — is now closed:
`channel-closedform.md` proves every tower channel has a universal
closed form with explicit Lah-number coefficients (checker
`channel_closedform_checks.py`), making the support law — and hence
the closure law of Section 1 — a theorem for every tower order \(n\),
not only orders \(\le4\).

## Verification

`uv run --with sympy python research/strominger/checkers/rung4_foldrule_checks.py`
— see `research/strominger/results/rung4_foldrule.json`.
