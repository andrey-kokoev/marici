# The connection is derived: uniqueness of the fold engine modulo invariant gauge

Companion to `checkers/deformation_theory_checks.py` (groups UNIQ, KER1,
N1, EXACT, MECH, WGHT; 28/28, exit 0; results in
`results/deformation_theory.json`). This packet closes the two gaps left
by the variation audit (`variation-audit.md`): the audit sampled
discrete perturbations, and its first-order follow-up revealed
*collisions* among obstruction directions — evidence of
character-preserving deformations the discrete scan could not see. The
deformation theory settles both: the character theorem has an exact
gauge freedom, and modulo that freedom the engine is unique.

## 1. Setup

Ratio \(R_X=P(X)/X\), \(X\in\{E_g,M_g\}\), baseline characters
\(+u^{g+2}\), \(-u^{g+3}\) (`rung5-readout.md` §3). All computations at
grades \(g=2,3\), exact in the deformation parameter (\(\varepsilon\) or
\(c\)); the character is tested on the nose, not scanned.

## 2. The strength family: \(c=2\) is the only point (UNIQ)

For \(\Gamma_c=-c\,\bar z/(1+u)\) at \(g=2\):

\[
R_E-u^{4}
=-(c-2)\,u^{4}(u-1)(u+1)\,\frac{6c\,u^{2}+6c+5u^{2}+10u+5}{D_E(c,u)},
\]
\[
R_M+u^{5}
=(c-2)\,u^{5}(u+1)\,\frac{6c\,u^{4}+12cu^{3}-12cu^{2}+12cu+6c
+5u^{4}+10u^{3}+10u^{2}+10u+5}{D_M(c,u)}.
\]

Both cofactors are certified non-vanishing as rational functions (the
\(10u\) term, resp. the \(5u^{4}\) term, cannot cancel for any \(c\)).
Hence within this family the monomial character holds **iff \(c=2\)** —
the connection strength is selected, not tuned.

## 3. The first-order obstruction space and its kernel (KER1, N1)

For directions \(\Gamma_\varepsilon=\Gamma_0+\varepsilon\,\bar z\,u^{k}\),
\(k=-4,\dots,2\), the first-order obstruction
\(\rho=dR/d\varepsilon|_{0}\,/\,(\text{character})\) has a striking
form: its **denominator depends only on the sector** — the palindromic
quartic \(6u^{4}-3u^{3}+2u^{2}-3u+6\) for \(E\), and
\((u-1)(3u^{4}+12u^{3}+8u^{2}+12u+3)\) for \(M\) — while the
perturbation only moves the (anti-palindromic) numerator. The magnetic
denominator vanishes at \(u=1\), the fixed point of the involution
\(u\leftrightarrow1/u\): the magnetic obstruction has a resonance
exactly where the norm-1 law pinches.

Every direction satisfies the first-order norm-1 law
\(\rho(u)+\rho(1/u)=0\) (N1, 14 checks). The nullspace of the direction
map — the first-order *character-preserving* deformations — is
three-dimensional in the audited span, for **both** sectors (KER1):

\[
\ker=\operatorname{span}\{\,e_{0}-e_{-2},\;e_{1}-e_{-3},\;e_{2}-e_{-4}\,\}
=\Big\{\,\bar z\,\tfrac{d}{du}\varphi(u):\;
\varphi(u^{m}+u^{-m}),\;m=1,2,3\,\Big\}.
\]

Every first-order character-preserving connection perturbation is the
\(z\)-derivative of a **\(P\)-invariant** function
\(\varphi(u)=\varphi(1/u)\).

## 4. The kernel is exact (EXACT, MECH)

First-order kernels are often artifacts; this one is not:

- \(\Gamma_0+\varepsilon\,\bar z(u^{-2}-1)\) preserves both characters
  **exactly at symbolic \(\varepsilon\)**, certified at \(g=2\) and
  \(g=3\);
- \(\Gamma_0+\varepsilon\,\bar z(2u-2u^{-3})\) (the
  \(\varphi=u^{2}+u^{-2}\) direction) preserves them exactly at \(g=2\);
- the asymmetric control \(\Gamma_0+2\varepsilon\,\bar z\,u\)
  (\(\varphi=u^{2}\), not invariant) does **not** — nonzero residual
  certified.

Mechanism (MECH): under the invariant-exact deformation the fold is
multiplied by a rational factor \(K(u,\varepsilon)\) that is u-only and
\(P\)-invariant, \(P(K)=K\). Since
\(R_{XK}=R_X\cdot P(K)/K=R_X\), the character is untouched. The gauge
freedom is precisely multiplication of the readouts by invariant
rational factors.

## 5. The weights have no kernel (WGHT)

Single-weight perturbations \(s_i\to s_i+\varepsilon\) at \(g=2\) give
linearly independent obstructions
(\(\rho_{s_2}/\rho_{s_3}=2(2u^{2}+u+2)/(3u^{2}+2u+3)\), non-constant):
**no** first-order weight deformation preserves the characters. The
weight law \(s=2,3,\dots,g+1\) is genuinely rigid — no gauge freedom on
that side.

## 6. The derivation

Within rational connections of the form \(\bar z\cdot(\text{rational in
}u)\), the certified statement is:

\[
\boxed{\;\text{monomial }P\text{-characters}
\iff
\Gamma=-\frac{2\bar z}{1+u}+\partial_z\varphi,\quad
\varphi(u)=\varphi(1/u)\;}
\]

—the fold connection is **derived, unique modulo invariant gauge**.
Constructor-theoretically this sharpens the audit's impossible
transformation: the transformations that destroy the alternation are
exactly those outside the invariant-gauge class; the transformations
that preserve it are exactly invariant gauge (connection side) and the
invariant datum class (datum side, `variation-audit.md` §3). The
engine's explanatory content lives in a single gauge-equivalence class.

Honest scope: the kernel is certified within the Laurent direction span
\(k=-4..2\) at \(g=2\) (first order) and for two members exactly
(\(g=2,3\)); the "iff" over *all* rational perturbations is the natural
conjecture, with the falsifier below.

## 7. Falsifiers

- Any rational direction \(\bar z\,\psi(u)\), \(\psi\) not
  invariant-exact, whose exact deformation preserves the characters,
  refutes the kernel classification.
- Any invariant-exact direction that breaks the characters at some
  grade \(g\ge4\) refutes exactness.
- Any \(c\neq2\) with monomial characters refutes uniqueness.

## 8. Checker

`checkers/deformation_theory_checks.py`, 28/28, exit 0; results
`results/deformation_theory.json`. Groups: UNIQ (2), KER1 (2), N1 (14),
EXACT (7), MECH (2), WGHT (1). Scratch precursors:
`_scratch_deformation.py`, `_scratch_deform2.py`, `_scratch_deform3.py`,
logs beside them.
