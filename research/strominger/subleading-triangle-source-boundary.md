# Source and boundary packet: the subleading triangle maps (marici.Strominger)

Companion to `subleading-triangle-conventions.md` (sources, grounding
ledger, gauge prescription G_CS, external inputs are there). This packet
exports the actual maps and the check items that
`checkers/subleading_triangle_exact_checks.py` must verify. Same rule as
the leading packet: nothing is proved by citing the correspondence;
every link is a check item with a declared left and right side, and
every discrepancy is a typed residual in the results JSON.

Corners: subleading soft factor [CS] = arXiv:1404.4091; superrotation
Ward identity [KLPS] = arXiv:1406.3312; spin memory [PSZ] =
arXiv:1502.06120. All formula-grounded via PDF text extraction
(`sources/*.txt`); [HMLS] = arXiv:1401.7026 from the leading session.

## 1. The maps and their grounded formulas

**Soft corner.** [CS (5)–(6)]:
\(M_{n+1}=S^{(0)}M_n+S^{(1)}M_n+O(q^1)\),
\(S^{(1)}=-i\sum_a E_{\mu\nu}k_a^\mu(q_\rho J_a^{\rho\nu})/(q\cdot k_a)\),
with \(J_a\) total angular momentum, acting as
\(k_a^{[\mu}\partial/\partial k^a_{\nu]}+(\)helicity terms\()\)
[CS footnote 4]. Gauge variation [CS (7)]:
\(\delta_\Lambda S^{(1)}=-i\Lambda_\mu q_\nu\sum_a J_a^{\mu\nu}=0\) by
global angular momentum conservation \(\mathcal J\).

**Ward corner.** [KLPS (5.14)–(5.16)]:
\(\langle{\rm out}|Q^+(Y)\mathcal S-\mathcal S Q^-(Y)|{\rm in}\rangle=0\)
becomes
\[
\langle:\!Q_S(Y)\mathcal S\!:\rangle
=-i\sum_{k}\Big(Y^z(z_k)\partial_{z_k}
-\tfrac{E_k}{2}D_zY^z(z_k)\partial_{E_k}\Big)\langle\mathcal S\rangle ,
\]
sum over in+out legs; Lie derivative replaces \(\partial_{z_k}\) for
spinning legs. The soft charge [KLPS (5.8)]:
\(Q_S^-=\frac12\int_{\mathcal I^-}dv\,d^2z\,D_z^3Y^z\,vM_{z\bar z}\),
built from the news shift law [KLPS (5.5)]
\(\delta_Y M_{zz}=D_z^3Y^z\): the superrotation soft graviton carries
polarization \(\propto D_z^3Y^z\). The subleading projector
\((1+\omega\partial_\omega)\) kills the Weinberg pole [KLPS (5.33)];
mode correspondence at \(i^0\): \(N_{\bar z\bar z}|_{\mathcal I^+_-}
=-M_{\bar z\bar z}|_{\mathcal I^-_+}\) [KLPS below (5.34)].

**Memory corner.** [PSZ (4.5)]: counter-orbiting delay
\(\Delta_+ u=\frac{1}{2\pi L}\int du\oint_{\mathcal C}
(D_zC_{zz}dz+D_{\bar z}C_{\bar z\bar z}d\bar z)\).
Flux form [PSZ (5.7)]: \(\Delta_+ u=-\frac{1}{\pi^2 L}\,\mathrm{Im}
\int_{D_{\mathcal C}}d^2w\,\gamma_{w\bar w}\int d^2z\,
\partial_{\bar z}G(z;w)\,[\Delta_+ N_z+\int du\,T_{uz}]\), depending only
on the CURL of \(\Delta_+ N_z\) [PSZ below (5.7)].
Green's function [PSZ (5.3)–(5.4)]:
\(G(z;w)=\ln\sin^2(\Theta/2)\) with
\(\partial_z\partial_{\bar z}G=2\pi\delta^2(z-w)-\frac12\gamma_{z\bar z}\)
— the SAME kernel \(S=\sin^2(\Theta/2)\) as the leading packet
(HMLS 2.25–2.26 identities already checked exactly there).

**The equivalence chain (soft ↔ memory).** [PSZ (6.1), (6.5)–(6.9)]:
\[
\tfrac12(\lim_{\omega\to0^+}+\lim_{\omega\to0^-})\mathcal A_{n+1}
=S^{(1)}_{\mu\nu}\varepsilon^{\mu\nu}\mathcal A_n,\qquad
S^{(1)}_{\mu\nu}=i\kappa\sum_k\frac{p_{k\mu}J_{k\nu\lambda}q^\lambda}
{q\cdot p_k}\quad[\text{PSZ (6.5)}],
\]
\[
\int du\,C_{zz}-\int dv\,C_{zz}
=-(\lim_{\omega\to0^+}+\lim_{\omega\to0^-})\,
\frac{i\kappa}{8\pi}\partial_zX^\mu\partial_zX^\nu h_{\mu\nu}
\quad[\text{PSZ (6.6)}],
\]
with the sphere parametrization [PSZ (6.7)]
\(p_k=\frac{E_k}{1+z_k\bar z_k}(1+z_k\bar z_k,\ \bar z_k+z_k,\
i(\bar z_k-z_k),\ 1-z_k\bar z_k)\), \(q\) likewise with \((\omega,z)\),
\(\varepsilon^-_\mu=\frac{1}{\sqrt2}(z,1,i,-z)\). Acting with \(D_z^2\)
[PSZ (6.8)]:
\[
\mathrm{Im}\Big[\int du\,D_z^2C_{\bar z\bar z}
-\int dv\,D_z^2C_{\bar z\bar z}\Big]
=\frac{\kappa}{8\pi}\big[D_{\bar z}^2\hat S^{(1)}_{zz}
-D_z^2\hat S^{(1)}_{\bar z\bar z}\big],
\qquad \hat S^{(1)}_{zz}\equiv\partial_zX^\mu\partial_zX^\nu
S^{(1)}_{\mu\nu},
\]
and with the appendix angular-momentum/stress formulas plus \(\mathcal
J\) this becomes [PSZ (6.9)]:
\[
\mathrm{Im}\Big[\int du\,D_z^2C_{zz}-\int dv\,D_z^2C_{zz}\Big]
=-8G\sum_k\gamma_{z_k\bar z_k}\mathrm{Im}\Big[
L_{uz}(z_k)\partial_{\bar z_k}G(z_k;z)
+\tfrac{i}{2}h_k\,\partial_{z_k}\partial_{\bar z_k}G(z_k;z)\Big].
\]

**Derivation route of (6.8), grounded after the fact.** PSZ defers the
(6.8) step to its ref [20], which is **KLPS = arXiv:1406.3312** (§6 of
the Ward-corner paper, already grounded here — NOT [SZ]
arXiv:1411.5745, which an earlier draft of this ledger cited in
error; [SZ] is grounded at `sources/sz1411.5745.txt` but plays no role
in this closure). The grounded KLPS §6 route, now checked exactly
(checks S5.6–S5.9, S10): the per-leg stripped soft operator is exactly
KLPS (6.6) once the Lorentz generator coefficients are contracted with
RAISED indices, \(A^{mn}=-s^m s^n\beta_{mn}\) (checker S5.6a arbiter:
the operator's pushforward on leg-momentum space is exactly
\(W=(\varepsilon\cdot k)q-(q\cdot k)\varepsilon\)); the tetrad
\(\partial_zX=b\varepsilon^++cX\), \(\partial_{\bar z}X=b\varepsilon^-
+\bar cX\) with \(b=\sqrt2/(1+z\bar z)\), \(c=-\bar z/(1+z\bar z)\)
gives the mixing theorem
\(\hat S^{(1)}_{zz}=b^2S^{(1)+}+\frac{bc}{\omega}\,\mathrm{op}
(\varepsilon^+)\) (S5.8), whose second term is per leg the KLPS (6.4)
first-type gauge response \(\varepsilon^\nu q^\lambda J_{k\nu\lambda}\).
The per-leg bridge residual of (6.8) is exactly
\(M=D_z^2\mathrm{mix}^--D_{\bar z}^2\mathrm{mix}^+\) (S5.9; closed forms
in the checker), nonzero in the two angular channels, zero in the
energy channel, and killed leg-summed by \(\sum_kJ_k=0\) (S10.1): the
bridge closes per leg only in the \(E\)-channel and otherwise exactly
modulo the KLPS (6.4) gauge mechanism. The KLPS (6.7)/(6.12) delta
scaffold as printed is NOT an exact per-leg distributional identity
under the declared prescription: computed deltas are uniformly half the
printed ones (candidate \(\delta^2\)-normalization drift), and the
energy/spin channels carry unprinted plain-\(\delta\) terms
\(-2\pi E_k\bar z_k/(1+z_k\bar z_k)\) and
\(+2\pi\bar z_k/(1+z_k\bar z_k)\,h_k\) (S10.2/S10.3); the endpoint
KLPS (5.16) is unaffected (S4.3).

## 2. Check items (checker specification)

- **S1 (projector).** \((1+\omega\partial_\omega)\) annihilates
  \(a/\omega\) and acts as identity on \(\omega^0\) terms [KLPS (5.33)
  comment]; the symmetric limit \(\frac12(\lim_++\lim_-)\) of a
  hermitian-combined insertion equals the \((1+\omega\partial_\omega)\)
  projection at the pole-plus-finite level. Exact calculus check.
- **S2 (gauge variation).** With \(J_a^{\mu\nu}=k_a^{[\mu}\partial_{k^a_{\nu}]}\)
  on scalar legs, \(\delta_\Lambda S^{(1)}
  =-i\Lambda_\mu q_\nu\sum_a J_a^{\mu\nu}\) identically [CS (7)];
  re-run WITHOUT \(\mathcal J\) to exhibit the typed obstruction.
- **S3 (soft-factor normalization).** Contract [CS (6)] with
  \(\varepsilon^{\mu\nu}\) and compare against [PSZ (6.5)]: the
  \(i\kappa\) vs \(-i\) and the \(\kappa\)-placement must be reconciled
  explicitly ([CS (5)] carries no \(\kappa/2\) prefactor); any mismatch
  is a typed residual, not absorbed.
- **S4 (sphere reduction of the hard operator).** Using [PSZ (6.7)],
  reduce \(J_k^{\mu\nu}\) acting on functions of \((z_k,E_k)\) to the
  [KLPS (5.16)] combination \(Y^z(z_k)\partial_{z_k}
  -\frac{E_k}{2}D_zY^z(z_k)\partial_{E_k}\) (orbital part; helicity
  terms declared separately). Exact rational identity on the sphere —
  the subleading analog of the leading checker's map-S kernel check.
- **S5 (the D² bridge).** Verify [PSZ (6.8)] as an operator statement:
  \(D_z^2\) of the [PSZ (6.6)] right-hand side equals
  \(\frac{\kappa}{8\pi}[D_{\bar z}^2\hat S^{(1)}_{zz}
  -D_z^2\hat S^{(1)}_{\bar z\bar z}]\) when \(\hat S^{(1)}\) is built
  from [PSZ (6.5)] via [PSZ (6.7)]. Symbolic, generic \((z_k,E_k,h_k)\).
  Outcome (checks S5.1–S5.9): the energy channel closes exactly per
  leg; the angular channels equal the exactly named gauge-mixing
  residual \(M=D_z^2\mathrm{mix}^--D_{\bar z}^2\mathrm{mix}^+\), which
  closes only leg-summed via the [KLPS (6.4)] mechanism
  \(\sum_kJ_k=0\) (S10.1). Includes the contraction arbiter S5.6a
  (pushforward \(=\) the soft-factor vector field \(W\)), the exact
  reproduction of [KLPS (6.6)] (S5.6b), and the tetrad mixing theorem
  (S5.7/S5.8).
- **S10 (KLPS §6 scaffold).** Two items: (i) the leg-summed closure
  mechanism [KLPS (6.4)] as an abstract \(J\)-contraction identity
  (S10.1); (ii) the [KLPS (6.7)/(6.12)] delta identities as per-leg
  distributional statements under the declared prescription
  \(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2\) — outcome: uniform
  factor-\(\tfrac12\) on the surviving deltas plus structural
  plain-\(\delta\) contamination in the energy and spin channels
  (S10.2/S10.3); the regular parts vanish identically (S10.2e).
- **S6 (Green-kernel consistency).** [PSZ (5.4)]
  \(\partial_z\partial_{\bar z}G=2\pi\delta^2-\frac12\gamma_{z\bar z}\)
  against the leading packet's checked identities for
  \(S\ln|z-w|^2\) (HMLS 2.25–2.26): same kernel, declared distributional
  prescription \(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2(z-w)\).
- **S7 (news shift law).** [KLPS (5.5)] \(\delta_YM_{zz}=D_z^3Y^z\) is
  the CFT stress-tensor Schwarzian-type shift [KLPS footnote 7]; check
  that \(D_z^3Y^z\) is exactly the \(l=0,1\)-killing operator on
  sphere vector fields \(Y^z\) (globally defined conformal Killing
  vectors = kernel), i.e. \(D_z^3Y^z=0\) iff \(Y\) is a global
  conformal Killing vector. This types the superrotation soft mode as
  the quotient of vector fields by CKVs — the subleading analog of the
  \(l\ge2\) quotient.
- **S8 (carrier question, H2 test).** The memory contour [PSZ (4.5)]
  uses \(D_zC_{zz}\) (one derivative), the soft side [PSZ (6.9)] uses
  corner differences of \(D_z^2C_{zz}\) (two), the constraint
  [PSZ (5.2)] and shift law [KLPS (5.5)] use \(D_z^3\) (three).
  Check the Stokes bridge:
  \(\oint_{\mathcal C}(D_zC_{zz}dz+D_{\bar z}C_{\bar z\bar z}d\bar z)\)
  vs \(\int_{D_{\mathcal C}}\partial_{\bar z}D_zC_{zz}\,d^2z\)-type
  bulk forms, and determine EXACTLY which single field combination
  (\(\mathrm{Im}\,D_z^2C_{zz}\)? the curl of \(N_z\)?) all three
  readouts factor through. Expected outcome: NOT one operator but one
  FIELD with three derivative grades — a typed refinement of the
  leading one-operator picture. Record whichever way it lands.
- **S9 (constraint parity).** [PSZ (5.2)]
  \(\mathrm{Im}[\partial_{\bar z}D_z^3C_{zz}]
  =2\,\mathrm{Im}[\partial_u\partial_{\bar z}N_z
  +\partial_{\bar z}T_{uz}]\): verify the magnetic-parity projection
  structure and the curl-only dependence (\(N_z\to N_z+\partial_zX\)
  invariance, [PSZ below (5.5)]) as exact algebraic statements.

## 3. Boundary and corner data

Inherited from the leading packet: news vanishes at all four corners
[HMLS 2.15]; \(C_{zz}|_{\mathcal I^+_-}=D_z^2C\) [HMLS 2.18]; antipodal
matching [HMLS 3.1–3.3]. Subleading additions: the \(i^0\) mode
correspondence \(N_{\bar z\bar z}|_{\mathcal I^+_-}
=-M_{\bar z\bar z}|_{\mathcal I^-_+}\) [KLPS, below (5.34)]; the corner
differences \(\int du-\int dv\) of [PSZ (6.6), (6.8), (6.9)] run between
\(\mathcal I^+\) and \(\mathcal I^-\) and require the matching to
combine — retained as a declared input, not rederived.

## 4. External inputs ledger (final for this triangle)

1. \(\mathcal J\): global angular momentum conservation [CS (7);
   PSZ (6.9) derivation].
2. G_CS gauge prescription (conventions packet §2).
3. Antipodal matching + the KLPS \(i^0\) mode correspondence (§3).
4. The symmetric/hermitian zero-frequency limit [PSZ (6.1)] ≡
   \((1+\omega\partial_\omega)\) projection [KLPS (5.33)].
5. Distributional prescription \(\partial_{\bar z}(z-w)^{-1}
   =\pi\delta^2(z-w)\), inherited from the leading packet.

No other input. The soft–BMS–memory correspondence is nowhere invoked
as a proof step.
