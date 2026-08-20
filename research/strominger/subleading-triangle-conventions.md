# Conventions packet: the subleading triangle (marici.Strominger)

Companion to `soft-bms-memory-conventions.md` and
`soft-bms-memory-source-boundary.md` (the leading triangle, ledger entry
1056). This packet fixes the conventions, gauge prescription, and
grounding status for the **subleading** triangle before any checker is
built. Proposed to marici.Nima in epistemic event `ev-000000000702`
(2026-08-19); started under the operator directive to continue the
sector, pending Nima's prioritization.

The triangle under test:

- **Soft corner.** The subleading soft graviton factor of
  Cachazo–Strominger [CS] = arXiv:1404.4091.
- **Ward corner.** The superrotation / Virasoro Ward identity of the
  quantum gravity S-matrix, Kapec–Lysov–Pasterski–Strominger [KLPS] =
  arXiv:1406.3312.
- **Memory corner.** The spin memory effect of
  Pasterski–Strominger–Zhiboedov [PSZ] = arXiv:1502.06120.

## 1. Grounding ledger (typed, load-bearing)

Status as of 2026-08-19 (updated after PDF text extraction succeeded):

| item | status |
|---|---|
| [HMLS] = arXiv:1401.7026 full text | grounded (leading-triangle session) |
| [CS] abstract + formulas | grounded. Abstract via arxiv.org/abs/1404.4091; formula level via PDF text extraction to `sources/cs1404.4091.txt` (23 pages): soft expansion (5), subleading factor (6), gauge variation (7), spinor form (18)–(19) |
| [PSZ] abstract + formulas | grounded. Abstract via arxiv.org/abs/1502.06120; formula level via PDF text extraction to `sources/psz1502.06120.txt` (18 pages): spin memory contour formula (4.5), constraint (5.2), Green's function (5.3)–(5.4), flux convolution (5.6), equivalence to the subleading soft theorem (6.1)–(6.9), conserved charges (7.1) |
| [KLPS] = arXiv:1406.3312 | grounded via PDF text extraction to `sources/klps1406.3312.txt` (23 pages): news shift law (5.5)–(5.6), soft charge (5.8), Ward identity (5.14)–(5.16), mode expansion (5.17); §6 read at formula level for the subleading bridge: gauge mechanism (6.4), per-leg operator (6.6), delta scaffold (6.7)/(6.12), spin soft factor (6.11) |
| [SZ] = arXiv:1411.5745 | grounded via PDF text extraction to `sources/sz1411.5745.txt` (leading memory ↔ soft paper). NOTE: an earlier draft of this ledger cited [SZ] for the PSZ (6.8) closure route; that was a mis-citation — PSZ ref [20] is [KLPS], and the grounded (6.8) derivation runs through KLPS §6. [SZ] is retained in the ledger but plays no role in the S5 closure. |

(The arXiv HTML / ar5iv route fails with a fatal conversion error; the
working route is `arxiv.org/pdf/<id>` + `pypdf` text extraction into
`sources/` — used for all four papers above, [SZ] included.)

Rule carried over from the leading packet: nothing is proved by citing
the correspondence; every link becomes an explicit check item, and every
ungrounded input is a typed residual, never silently absorbed.

## 2. The gauge prescription, declared first (known hazard 1)

The subleading soft factor is not gauge invariant by itself. Before any
symbolic comparison, this packet declares the working prescription:

- **G_CS (declared, formula-grounded).** The soft expansion is [CS (5)]
  \(M_{n+1}=S^{(0)}M_n+S^{(1)}M_n+O(q^1)\) with the subleading factor
  [CS (6)]
  \[
  S^{(1)}\equiv -i\sum_{a=1}^{n}
  \frac{E_{\mu\nu}\,k_a^\mu\,(q_\rho J_a^{\rho\nu})}{q\cdot k_a},
  \]
  \(J_a\) the TOTAL (orbital + spin) angular momentum of leg \(a\),
  acting in a momentum eigenbasis as the differential operator
  \(J_a^{\mu\nu}\sim k_a^{[\mu}\partial/\partial k^a_{\nu]}+(\)helicity
  terms\()\) [CS footnote 4]; spinor form [CS (18)]. Note [CS (5)] has no
  explicit \(\kappa/2\) prefactor — the normalization relative to our
  \(\kappa^2=32\pi G\) conventions is itself a check item.
- **Gauge-variation clause (formula-grounded).** Under a polarization
  gauge shift, [CS (7)]:
  \[
  \delta_\Lambda S^{(1)}=-i\,\Lambda_\mu q_\nu\sum_{a=1}^{n}J_a^{\mu\nu}=0
  \]
  by global angular momentum conservation. It is the exact subleading
  analog of the leading triangle's external input \(\mathcal P\)
  (four-momentum conservation, source-boundary packet §8). The checker
  must exercise the removal of angular momentum conservation as a
  deliberate-failure test, mirroring the \(\mathcal P\)-removal
  obstruction of the leading checker.

## 3. Conventions inherited unchanged

\(\kappa^2=32\pi G\); celestial-sphere frame \(z,\bar z\),
\(\gamma_{z\bar z}=2/(1+z\bar z)^2\); covariant derivatives \(D_z,
D_{\bar z}\); the sphere operator
\(\mathcal O=(\gamma^{z\bar z})^2 D_{\bar z}^2 D_z^2
=\tfrac14 D^2(D^2+2)\) with kernel exactly the \(l\le1\) harmonics
(leading checker, 37/37). Retarded time \(u\) on \(\mathcal I^+\);
corners \(\mathcal I^+_\pm\); news \(N_{zz}\), shear \(C_{zz}\), and the
real scalar \(N\) with \(\int du\,N_{zz}=D_z^2N\) [HMLS 2.19].

## 4. The carrier question (known hazard 2)

Leading order: one scalar \(N\) on the \(l\ge2\) quotient carried all
three readouts through the single operator \(\mathcal O\).

Subleading candidate, now partially grounded from [PSZ]: the spin
memory is carried by the magnetic-parity (curl) part of the boundary
graviton data. Grounded facts:

- The observable [PSZ (4.5)]: relative delay of counter-orbiting beams
  \(\Delta_+ u=\frac{1}{2\pi L}\int du\oint_{\mathcal C}
  (D_zC_{zz}\,dz+D_{\bar z}C_{\bar z\bar z}\,d\bar z)\), an infrared
  effect proportional to the \(u\)-zero mode of \(C_{zz}\).
- The constraint [PSZ (5.2)]:
  \(\mathrm{Im}[\partial_{\bar z}D_z^3C_{zz}]
  =2\,\mathrm{Im}[\partial_u\partial_{\bar z}N_z
  +\partial_{\bar z}T_{uz}]\) — note \(D_z^3\), the superrotation-grade
  derivative (hazard 3 is real).
- The right-hand side of the flux formula [PSZ (5.5)] is invariant
  under \(N_z\to N_z+\partial_z X\) for real \(X\): only the CURL part
  of \(N_z\) contributes — the magnetic-parity selection is explicit in
  the source.
- The soft-side master identity [PSZ (6.9)]:
  \[
  \mathrm{Im}\Big[\int du\,D_z^2C_{zz}-\int dv\,D_z^2C_{zz}\Big]
  =-8G\sum_k\gamma_{z_k\bar z_k}\,\mathrm{Im}\Big[
  L_{uz}(z_k)\partial_{\bar z_k}G(z_k;z)
  +\tfrac{i}{2}h_k\,\partial_{z_k}\partial_{\bar z_k}G(z_k;z)\Big],
  \]
  derived using TOTAL angular momentum conservation, with
  \(G(z;w)=\ln\sin^2(\Theta/2)\) [PSZ (5.3)] — the SAME kernel
  \(S=\sin^2(\Theta/2)\) as the leading packet's Green's kernel
  (source-boundary packet, HMLS 2.25–2.26), whose covariant identities
  the leading checker already verifies exactly.

Working hypotheses to be tested, not assumed:

- **H1.** The subleading carrier is the magnetic-parity partner of
  \(N\) — equivalently the combination \(\mathrm{Im}\,D_z^2C_{zz}\)
  appearing on both the memory side [PSZ (4.5)] and the soft side
  [PSZ (6.9)].
- **H2.** The one-operator picture may FAIL here: the memory contour
  uses first derivatives \(D_zC_{zz}\) while the soft side uses
  \(D_z^2C_{zz}\), and the constraint uses \(D_z^3C_{zz}\). If no
  single operator generates all three readouts, the correct admission
  outcome is a typed failure with the obstruction exhibited — exactly
  the mixed-outcome pattern the leading admission test used.

## 5. Declared external inputs ledger (subleading analog of §8 of the
source-boundary packet)

1. \(\mathcal J\): global angular momentum conservation — kills
   \(\delta_\Lambda S^{(1)}\) [CS (7)] and is used inside the soft-side
   master identity [PSZ (6.9)] (formula-grounded, §2/§4).
2. G_CS: the declared gauge prescription of §2.
3. Antipodal matching at \(i^0\) [HMLS 3.1–3.3], inherited; whether the
   superrotation Ward identity needs an extended matching is an OPEN
   item (hazard 3: the Virasoro extension of Barnich–Troessaert is
   extra grounding not yet in hand).
4. The hermitian zero-frequency prescription [HMLS 5.17], inherited;
   its subleading form is the symmetric limit
   \(\frac12(\lim_{\omega\to0^+}+\lim_{\omega\to0^-})\) of [PSZ (6.1)].

## 6. Open items before the admission test

- All three corners are now formula-grounded ([CS], [KLPS], [PSZ] via
  PDF extraction; [HMLS] from the leading session).
- Fix the carrier hypothesis H1/H2 into explicit check items with
  declared left and right sides (source/boundary packet, next).
- Decide whether Barnich–Troessaert Virasoro grounding is in scope or a
  declared external input.
