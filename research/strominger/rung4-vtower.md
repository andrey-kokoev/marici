# The rung-4 V-tower: a derived candidate operator, two alternations, and the migration of the oddness obstruction

Companion to `checkers/rung4_vtower_checks.py` (groups G1–G6, 26/26,
exit 0; results in `results/rung4_vtower.json`). This packet takes the
next step past the rung-3 bridge (`rung3-s2-bridge.md`): there is **no
grounded \(S^{(3)}\) source** in the admitted corpus, so the rung-4
candidate is *derived*, not grounded — extracted from the \(V\)-operator
structure that the grounded rungs already certify. Everything below is
exact rational-function arithmetic over
\(\mathbb{Q}(\sqrt{2})(u,z,\bar z,z_k,\bar z_k,E_k,\omega)\); every claim
carries a check id.

**Status boundary (read first).** Rung 4 here is a candidate: the tower is
*anchored* to the grounded rung-3 channels (G1), but no independent
source formula for \(S^{(3)}\) exists in the corpus, so nothing below is a
confirmation of an external expression. The rung-4 readout claim (G5) was
originally stated *conditional on the fold-grade assignment*; the
follow-up packet `rung4-foldgrade.md` computes the fold and FORCES the
grade at \(g=7\) (weight start \(-2\)), deriving the same sector verdict
unconditionally — see that packet for the certified version of §5.

## 1. The tower and its anchor (G1)

The grounded datum is the leading soft operator as a vector field on the
soft sector,

\[
V=c_{z_k}\partial_{z_k}+c_{E_k}\partial_{E_k},\qquad
S^{(2)-}=\frac{V^2}{\mathrm{den}},
\]

with \(\mathrm{den}=-4E_k\,\omega^2(z-z_k)(\bar z-\bar z_k)/
\bigl((1+u)(1+z_k\bar z_k)\bigr)\) — the bridge identity J1 of
`rung3-s2-bridge.md`, re-certified here as the anchor. The tower recursion
promotes any channel polynomial \(A^n_\alpha\) at operator order \(n\) to

\[
A^{n+1}_\alpha = V(A^n_\alpha)+\sum_i c_i\,A^n_{\alpha-e_i},
\]

so that the rung-\(r\) candidate is \(V^{r-1}/\mathrm{den}\). G1.anchor
certifies that the order-2 tower channels reproduce the four grounded
rung-3 channels \(A^2_{(2,0)},A^2_{(1,1)},A^2_{(0,2)},A^2_{(1,0)}\)
exactly — the recursion is not an extrapolation into the dark; its first
step *is* the grounded rung.

**The census.** The number of nonzero channels at operator order \(n\) is

\[
\frac{n(n+3)}{2}-(n-1):\qquad 2,\;4,\;7,\;11\quad(n=1,2,3,4).
\]

**The vanishing shadow (G1.shadow).** Exactly the pure-\(E_k\)
subprincipal channels \((0,k)\), \(k=1,\dots,n-1\), vanish at every order;
the pure-\(E_k\) principal channel \((0,n)=c_{E_k}^n\) survives. The root
is grounded: \(V(c_{E_k})=0\) (R1.3, the Hamiltonian collapse J2), and
the recursion propagates that zero up the whole tower. The tower's
channel geometry is therefore not the generic multi-index count — the
collapse carves a permanent shadow into it at every rung.

## 2. The first-order line in closed form (G2)

The magnetic first-order channel is solvable at *every* order. The
mechanism (G2.mech) is that \(c_{z_k}\) is \(E_k\)-free with
\(\partial_{z_k}c_{z_k}=-2c_{z_k}/(z-z_k)\), so on the first-order line
the tower closes on itself. Writing \(c_{z_k}=K(z-z_k)^2\) with \(K\)
\(z_k\)-free, the induction step is certified with symbolic multi-index
(G2.induction):

\[
V\bigl(K^{a}(z-z_k)^{2a+b}\bigr)=-(2a+b)\,K^{a+1}(z-z_k)^{2a+b+1}.
\]

Iterating from \((a,b)=(1,0)\), the factor product
\(\prod_{k=0}^{n-1}(-(k+2))=(-1)^n(n+1)!\) gives

\[
\boxed{\;V^{n}(c_{z_k})=(-1)^{n}(n+1)!\;
\frac{c_{z_k}^{\,n+1}}{(z-z_k)^{n}}\;}
\]

certified against the tower channels at \(n=1,2,3\) (G2.value.1–3). The
first-order line of the rung-4 candidate is therefore known *exactly*:
\(V^{3}(c_{z_k})=-24\,c_{z_k}^{4}/(z-z_k)^{3}\).

## 3. The depth-parity rule and the gate alternation (G3)

The square-root gate of the cocycle program asks whether a determinant
character is a rational square. The character atoms (G3) are

\[
D(z-z_k)=\frac{X}{u},\qquad D(c_{z_k})=X^{2},\qquad
D(\mathrm{den})=X^{2},
\]

with \(X=(1+z\bar z_k)(1+\bar z z_k)/\bigl((z-z_k)(\bar z-\bar z_k)\bigr)\).
Exponent arithmetic on the closed form then gives the first-order line
character at every order (G3.charline):

\[
D\!\left(\frac{V^{n}(c_{z_k})}{\mathrm{den}}\right)=(uX)^{n}.
\]

**The depth-parity rule (G3.depthrule).** On all 18 channels of orders 3
and 4, the \(z\)-valuation of a channel's determinant character *equals
the channel's \(V\)-depth*. Parity therefore alternates with depth:
even, odd, even, odd. The gate does not sit at a fixed location — it
marches up the tower one step per rung.

**The alternation (G3.alternation).** On the magnetic first-order line:

- rung 3: character \(uX\), odd \(z\)-valuation 1 — no rational root
  (the known rung-3 obstruction);
- rung 4: character \((uX)^{2}\) — a rational **square**, with root
  \(uX\) that is exactly \(\sigma\)-invariant;
- rung 5: predicted \((uX)^{3}\), odd again.

So the derived rung-4 candidate passes the square-root gate on its
first-order line, with an explicitly \(\sigma\)-invariant root — the
obstruction that blocked rung 3 lifts at rung 4 and is predicted to
return at rung 5.

## 4. Gauge invariance propagates up the tower (G4)

With the covariant completion \(A^{\nu}=J^{\nu\rho}q_\rho\), the gauge
atoms are exactly zero (G4):

\[
q\!\cdot\! A=0,\qquad q^{2}=0,\qquad
dE_{mn}\,q^{m}A^{n}=0,\qquad dE_{mn}\,A^{m}A^{n}=0,
\]

by antisymmetry plus nullness of the soft momentum alone (the R1.1a/R1.1b
mechanism). Since \(\delta(C^{n})=nC^{n-1}\delta C\) with \(\delta C\)
built from these atoms, per-leg gauge invariance propagates up the
**whole** tower (G4.tower): no new conservation law is required at any
rung. The rung-4 candidate inherits gauge invariance; it does not need to
earn it.

## 5. The readout migration: the falsifiable rung-4 prediction (G5)

The certified readout characters (`readout-parity-mechanism.md`, P3) are

\[
P(E_g)=+u^{g+2},\qquad P(M_g)=-u^{g+3},
\]

whose exponents have opposite parity at every grade: **exactly one**
readout sector is square-root-obstructed at each grade — the obstruction
never lifts, it migrates (G5.perpetual). At the rung-4 candidate grade
\(g=5\):

\[
P(E_5)=+u^{7}\;(\text{odd: gate FAILS}),\qquad
P(M_5)=-u^{8}\;(\text{even: gate PASSES}).
\]

The obstruction migrates to the **electric** sector (G5.migration). This
is the falsifiable signature of the derived rung 4: where rung 3 was
magnetically obstructed, rung 4 is electrically obstructed.

**Update (fold-grade packet).** The fold computation
(`rung4-foldgrade.md`, F2–F5) refutes the naive assignment \(g=5\) and
forces \(g=7\) with weight start \(-2\): the depth ≥ 1 channels close at
grade 5 but the principal sector needs grade 7. The sector verdict is
unchanged and now derived: \(P(E_7)=+u^{9}\) odd (electric gate fails),
\(P(M_7)=-u^{10}\) even (magnetic gate passes, root \(u^{5}\)).

## 6. Verdict (G6)

The rung-4 operator is derived as \(V^{3}/\mathrm{den}\), anchored to the
grounded rung-3 channels (G1); its magnetic first-order line is closed
form at every order (G2); its first-order determinant character is
\((uX)^{n}\), so the square-root gate alternates along the tower and
passes at rung 4 with a \(\sigma\)-invariant root (G3); per-leg gauge
invariance propagates up the whole tower without any new conservation law
(G4); and the readout obstruction migrates to the electric sector at the
rung-4 grade (G5).

\[
\boxed{\text{Two alternations — tower depth and readout grade — govern
where oddness can live.}}
\]

**Open edges.** (i) The tower is derived, not grounded: an independent
\(S^{(3)}\) source formula would either confirm or kill the candidate —
the anchor makes the first step safe, not the third. (ii) *Resolved:* the
fold-grade assignment is computed in `rung4-foldgrade.md` — the grade is
forced at \(g=7\) (\(w_0=-2\)), and the G5 sector verdict survives
unconditionally. (iii) The
depth-parity rule is certified on 18 channels of orders 3–4; a symbolic
proof for all orders is the natural next certificate.
