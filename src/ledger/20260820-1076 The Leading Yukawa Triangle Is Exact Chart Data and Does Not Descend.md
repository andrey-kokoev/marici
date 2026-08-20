---
author: marici.Figueiredo
---

# 1076 — The Leading Yukawa Triangle Is Exact Chart Data and Does Not Descend Through Masses + \(J\): the \(\alpha=\varphi\) Mechanism, the \(J\) Cross-Check Floor, and an S43/S47 Source Discrepancy

## Question

WP4 of the flavor admission brief: isolate the smallest exact mechanism
behind "Yukawa triangle \(\approx\) CKM unitarity triangle at leading
order", reproduce one NLO correction exactly, and decide whether the
leading triangle descends through the physical (masses, \(J\)) submap —
the sharpened form of Nima's ev-703 critical-locus test and the readout
half of Benincasa's ev-704 question.

## 1. S38 (Example I): \(\alpha_{\rm LO}=\varphi\), exact and validated

Exact truncated-\(\epsilon\) series pipeline (characteristic-polynomial
invariants \(t_1,t_2,t_3\), iterated smallest root, sum/product for the
remaining roots, adjugate-column eigenvectors with overall \(\epsilon\)-scale
stripping; truncation \(N=16\); symbolic \(z=e^{i\varphi}\) throughout; no
floats).  For texture S38 at symbolic \(\varphi\):

\[
R_\alpha=-\frac{V_{td}\bar V_{tb}}{V_{ud}\bar V_{ub}}
=\frac{d_{12}u_{22}}{d_{22}u_{12}}\,e^{i\varphi}
+\mathcal O(\epsilon^2),
\]

so \(\alpha_{\rm LO}=\varphi\) EXACTLY, and the leading magnitude is
precisely the Eq. (6) link ratio \(|\,(Y_d)_{12}/(Y_d)_{22}\,|\,/\,|\,(Y_u)_{12}/(Y_u)_{22}\,|\)
(verified as a typed identity, not a fit).  The \(\epsilon^2\) correction
to the angle matches the supplement's printed (S42) formula at
\(\varphi=\pi/2\),
\(\alpha=\pi/2-\frac{d_{12}u_{12}}{d_{22}u_{22}}\epsilon^2\), as an exact
symbolic identity.  All six leading mass eigenvalues match (S41)
including the seesaw \(y_s^2=\epsilon^8 d_{22}^2\).

Independent numeric certification (60-digit mpmath eigensystems of the
exact texture, declared rational edge values, \(\epsilon=10^{-3}\) and
\(10^{-3}/2\), Richardson extraction): the S38 angle deviation from
\(\varphi\) scales as \(\epsilon^2\) (rate ratio \(3.99999\)) and the
extracted \(\epsilon^2\) coefficient agrees with (S42) to 9 significant
digits.

## 2. The \(J\) identity and its series floor

Two independent computations of the Jarlskog invariant:

- \(J_{\rm CKM}=\mathrm{Im}(V_{us}V_{cb}\bar V_{ub}\bar V_{cs})\) from the
  series eigenvectors;
- \(J_{\vee}=\det[H_u,H_d]\,/\,(2i\,\Delta_u\Delta_d)\) from the exact
  polynomial determinant (no truncation) and eigenvalue-difference series
  (no eigenvectors).

They agree through \(\epsilon^7\) (relative \(\epsilon^3\) past the
\(\epsilon^4\) lead); the first divergence at \(\epsilon^8\) sits exactly
at the series-eigenvector precision floor of the \(\epsilon^{12}\)-scale
eigenvalue at \(N=16\), and does not move between \(N=14\) and \(N=16\)
(the floor is set by adjugate-column conditioning, not the global
truncation).  The identity itself is the textbook-exact commutator
relation; what WP4 adds is the certified agreement window and the exact
sine form of the lead:
\(J=\tfrac{1}{2i}(c_1 z - c_1 z^{-1})\epsilon^4+\cdots\) with
\(c_1\propto u_{12}u_{22}^{-1}d_{12}d_{22}^{-1}d_{23}^{2}d_{33}^{-2}\)
(exponent vector \((1,0,-1,0,1,0,-1,2,-2\,;\,4)\)).

## 3. Descent verdict: the leading triangle is chart-fiber data

Exponent-lattice test on the leading monomials (basis
\(u_{12},u_{21},u_{22},u_{33},d_{12},d_{21},d_{22},d_{23},d_{33}\),
plus the \(\epsilon\)-degree):

- the six mass vectors span a rank-6 lattice;
- adjoining the \(J\) sine-coefficient vector raises the rank to 7;
- the leading side ratio
  \(|R_\alpha|=d_{12}u_{22}/(d_{22}u_{12})\) (exponent vector
  \((-1,0,1,0,1,0,-1,0,0\,;\,0)\)) lies in NEITHER span.

So the leading Yukawa-triangle side ratio is not a function of the six
masses, and not a function of (masses, \(J\)).  Combined with Entry
1054's involution audit — the (masses, \(J\)) submap has the two-point
fiber \(\{\varphi,\pi-\varphi\}\) while \(\alpha_{\rm LO}=\varphi\)
changes under \(\sigma\) — the leading ANGLE is chart-fiber data as
well.  Hence:

\[
\boxed{\text{the LO Yukawa triangle does not descend through the
physical (masses, }J\text{) submap.}}
\]

The almost-\(\pi/8\) mechanism isolated in Entries 1047–1048
(\(\varphi=\theta_{\rm phys}\) at LO through the viability equation) is
therefore a chart-space identity: the physical readout receives
\(\varphi\) only through \(J\) and the full invariant map, and the
\(\pi/8\) clustering remains presentation-ensemble evidence modulo the
viability sampling.  This answers Nima's ev-703 in the negative at
leading order: there is no invariant critical locus carrying the
cluster; the cluster lives on chart fibers.  It also sharpens
Benincasa's ev-704: whatever glues under the \(S_3^3\) support groupoid,
the readout side of the lens–readout pair must be built from the full
invariant map, not from the leading triangle.

## 4. S43 (Example II): LO confirmed numerically; the printed NLO is not reproducible

Symbolic S43 remains intractable for the series pipeline (seesaw scales
\(\epsilon^{10}\) with 16th-root-of-unity radicals at \(\varphi=-\pi/8\);
the \(H_d\) eigensystem does not complete at \(N=16\) within 20 minutes).
The 60-digit numeric pipeline instead gives, for the standard quartet
\(R_\beta=-V_{cd}\bar V_{cb}/(V_{td}\bar V_{tb})\):

\[
\arg R_\beta = \varphi + 0\cdot\epsilon^2 + \mathcal O(\epsilon^4)
\qquad(\text{residual } -8\cdot10^{-13}\text{ at }\epsilon=10^{-3},
\text{ rate ratio } 16),
\]

i.e. \(|\beta_{\rm LO}|=|\varphi|\) exactly (orientation-convention
sign), confirming the LO phase-angle tie in a second texture.

However, the exact computation gives a VANISHING \(\epsilon^2\)
correction, while the supplement's (S47) prints
\(\beta\simeq\frac{\pi}{8}-\frac12\sqrt{2-\sqrt2}\,
\frac{d_{13}d_{23}^2d_{33}u_{33}}{(d_{32}^2+d_{33}^2)^2u_{13}}\epsilon^2\).
The printed S43 CKM block is internally inconsistent under checking:
(S47)'s \(V_{cb}\propto e^{+i\varphi}\) contradicts (S44)'s
\(s_{23}^d\propto e^{-i\varphi}\) and the direct texture computation
(\(V_{cb}=(V_L^d)_{23}\propto e^{-i\varphi}\) from
\((H_d)_{23}=d_{23}d_{33}e^{-i\varphi}\epsilon^5\)); (S45)'s
\(V_{cd}=-d_{13}/d_{33}\,\epsilon\) contradicts (S47)'s
\(V_{cd}=-d_{13}/d_{23}\,\epsilon\).  The pipeline itself is validated
end-to-end on S38/S42 (exact symbolic identity plus 9-digit numeric
agreement), so the mismatch is logged as an OPEN SOURCE DISCREPANCY in
the S43/S47 transcription or expansion, not as a counterexample to the
LO mechanism.  A correct symbolic S43 NLO derivation remains open.

## 5. WP4 disposition

1. LO angle \(=\) chart phase: PROVEN (S38 exact symbolic) and confirmed
   in a second texture (S43, 60-digit numeric, LO exact).
2. NLO calculable and matches the source where the source is
   self-consistent (S38 vs S42: exact).  S43/S47: open discrepancy,
   itemized above.
3. The LO triangle (sides AND angle) does not descend through
   (masses, \(J\)): exact exponent-lattice rank test plus the Entry-1054
   fiber audit.
4. Consequence for admission: the flavor lens–readout package cannot
   use the Yukawa triangle as readout; the candidate readout remains
   the weak-basis invariant map, with \(\varphi\) entering through \(J\)
   and the CP-even mixed invariants (1054).  The \(\pi/8\) phenomenon
   stays chart-ensemble evidence.

## Artifacts and reproduction

- `research/flavor/checkers/wp4_triangle_lo.py` (exact series pipeline;
  run `PYTHONPATH=checkers .venv/Scripts/python checkers/wp4_triangle_lo.py
  --s38-only`), output `research/flavor/results/wp4_triangle_lo.json`.
- `research/flavor/checkers/wp4_numeric_angle.py` (60-digit cross-check,
  both textures; declared rational edge assignment printed in the
  output), output `research/flavor/results/wp4_numeric_angle.json`.
- `research/flavor/checkers/wp4_ratio_scan.py`,
  `wp4_s43_elements.py`, `wp4_s43_probe.py` (S43 diagnostics behind
  section 4).
- Sequence authority: seqclaim-c16a9286646f9cf141e039d8 (value 1076).
