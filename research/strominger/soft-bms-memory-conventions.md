# Radiative GR conventions and equivalence packet (marici.Strominger)

Scope: the leading infrared triangle on future null infinity —
soft-graviton residue ↔ BMS supertranslation Ward identity ↔
displacement memory — as an admission test for a shared Marici carrier.

Sources (equation numbers below are the sources' own):

- [HMLS] T. He, V. Lysov, P. Mitra, A. Strominger, *BMS Supertranslations
  and Weinberg's Soft Graviton Theorem*, arXiv:1401.7026. HTML text
  extraction via ar5iv (https://ar5iv.org/abs/1401.7026), retrieved
  2026-08-19; the full body including all equations cited here was
  extracted and read directly.
- [S14] A. Strominger, *On BMS Invariance of Gravitational Scattering*,
  arXiv:1312.2229 (cited inside HMLS as [2]; Ward identity (3.6) below is
  derived there).
- [SZ] A. Strominger, A. Zhiboedov, *Gravitational Memory, BMS
  Supertranslations and Soft Theorems*, arXiv:1411.5745. ar5iv/arXiv-vanity
  HTML conversion failed on 2026-08-19; no equation-level claims from SZ
  are used below. The memory-side statements used here are instead the
  ones present verbatim inside HMLS (Eqs. 2.18–2.19, 5.22) and the
  lectures [L17].
- [L17] A. Strominger, *Lectures on the Infrared Structure of Gravity and
  Gauge Theory*, arXiv:1703.05448, sections 1–2 as extracted via ar5iv,
  retrieved 2026-08-19. Used for the sphere/antipodal conventions
  (Eq. 2.4.2 there) and the stated Fourier step-function relation between
  the soft pole and the memory shift (section 1.1).
- [W65] S. Weinberg, *Infrared Photons and Gravitons*, Phys. Rev. 140,
  B516 (1965) — cited inside HMLS as [1]; the soft factor used here is
  HMLS Eq. 4.7, derived in HMLS section 4 from Feynman rules.

This document fixes conventions for all marici.Strominger checkers. Where a
source formula is only meaningful after an interpretation (index
contractions, distributional prescriptions), the interpretation is stated
explicitly and marked [reading].

## 1. Geometry and coordinates

- Retarded Bondi coordinates \((u,r,z,\bar z)\) near \(\mathcal I^+\);
  advanced \((v,r,z,\bar z)\) near \(\mathcal I^-\) [HMLS 2.1, 2.3].
- Celestial sphere metric \(\gamma_{z\bar z}=2/(1+z\bar z)^2\)
  [HMLS 2.1]. Its inverse: \(\gamma^{z\bar z}=(1+z\bar z)^2/2\).
  In two dimensions with \(\gamma_{zz}=\gamma_{\bar z\bar z}=0\), the only
  nonzero Christoffels are
  \(\Gamma^z_{zz}=\partial_z\ln\gamma_{z\bar z}=-2\bar z/(1+z\bar z)\) and
  \(\Gamma^{\bar z}_{\bar z\bar z}=-2z/(1+z\bar z)\); all mixed
  \(\Gamma^z_{z\bar z}=\Gamma^z_{\bar z\bar z}=0\) — computed from the
  metric in the checker, not asserted.
- Covariant derivatives act on pure-\(z\) rank-\(s\) tensors as
  \(D_z T_{z\cdots z}=\partial_z T_{z\cdots z}-s\,\Gamma^z_{zz}T_{z\cdots z}\).
  For a scalar \(f\): \(D_z^2 f=\partial_z^2 f-\Gamma^z_{zz}\partial_z f\).
- Direction map [HMLS 5.5, 6.5]: a null direction \((z,\bar z)\) is
  \(\hat x(z,\bar z)=(1+z\bar z)^{-1}(z+\bar z,\,-i(z-\bar z),\,1-z\bar z)\);
  null four-vector \(q^\mu=\omega(1,\hat x)\).
  Minkowski metric \(\eta=\mathrm{diag}(-1,1,1,1)\).
- Antipodal map: \(z\to -1/\bar z\); it sends \(\hat x\to-\hat x\)
  [L17 2.4, text below Eq. 2.4.5].

## 2. Radiative data (Bondi gauge representatives)

- Shear \(C_{zz}(u,z,\bar z)\), news \(N_{zz}=\partial_u C_{zz}\)
  [HMLS 2.5]; at \(\mathcal I^-\): \(D_{zz}\), \(M_{zz}=\partial_v D_{zz}\).
- Mass aspect \(m_B\); \(U_z=-\tfrac12 D^z C_{zz}\) [HMLS 2.2].
- Boundary conditions at the corners \(\mathcal I^+_\pm\) of \(\mathcal I^+\)
  [HMLS 2.14–2.17]: \(N_{zz}|_{\mathcal I^+_\pm}=0\) and
  \([D_z^2 C_{\bar z\bar z}-D_{\bar z}^2 C_{zz}]_{\mathcal I^+_\pm}=0\)
  (equivalently \(\mathrm{Im}\,\Psi_2^0|_{\mathcal I^+_\pm}=0\)).
- Constraint solutions at the corners [HMLS 2.18–2.19]:
  \(C_{zz}|_{\mathcal I^+_-}=D_z^2 C\) and
  \(\int_{-\infty}^{\infty}du\,N_{zz}=D_z^2 N\), with real boundary fields
  \(C(z,\bar z)\), \(N(z,\bar z)\). The \(l=0,1\) modes of \(C\) and \(N\)
  are annihilated by \(D_z^2\) and do not appear in the metric
  [HMLS footnote 3].

## 3. The scalar operator on the sphere [reading]

HMLS Eq. 2.30 writes the soft charge term as
\(-\frac{1}{8\pi G}\int d^2z\,\gamma^{z\bar z} f\,D_z^2 D_{\bar z}^2 N\).
Taken literally, \(D_z^2 D_{\bar z}^2 N\) carries two \(z\) and two
\(\bar z\) indices and cannot contract with the single \(\gamma^{z\bar z}\)
shown. The reading used throughout this packet, and implemented in the
checker, is the scalar operator
\[
\mathcal O\,f \;\equiv\; (\gamma^{z\bar z})^2\,D_{\bar z}^2\!\left(D_z^2 f\right),
\qquad\text{claimed identity}\qquad
\mathcal O \;=\; \tfrac14\,D^2(D^2+2),
\]
with \(D^2 = 2\gamma^{z\bar z}\partial_z\partial_{\bar z}\) the scalar
Laplacian on the unit sphere. The claimed identity is *tested* (on a
generic symbolic scalar, i.e. as an operator identity), not assumed. On
scalar harmonics it gives eigenvalue
\(\tfrac14 (l-1)\,l\,(l+1)\,(l+2)\): invertible for \(l\ge 2\), with
four-dimensional kernel \(l=0,1\) — exactly the \(C,N\) zero modes of
[HMLS footnote 3].

## 4. The three source-defined maps

Declared with fixed coefficients before any comparison (no-fit gate);
\(\kappa^2 = 32\pi G\) [HMLS 4.1].

- **S (soft residue).** Outgoing \(+\)-helicity soft graviton,
  \(q=\omega(1,\hat x(z))\), hard legs \(p_k=E_k(1,\hat x(z_k))\) with
  \(\eta_k=+1\) (outgoing) / \(-1\) (incoming). Weinberg [HMLS 4.7, 6.4]:
  \[
  S_{\rm soft}(z)=\frac{\kappa}{2}\sum_k \eta_k\,
  \frac{[p_k\cdot\varepsilon^+(z)]^2}{p_k\cdot q},\qquad
  \varepsilon^{+\mu}=\tfrac{1}{\sqrt2}(\bar z,1,-i,-\bar z)\quad[\text{HMLS 6.5}].
  \]
- **Q (supertranslation charge / Ward).** [HMLS 2.30]:
  \[
  T^+(f)=\underbrace{\frac{1}{16\pi G}\!\int\! du\,d^2z\,f\,\gamma_{z\bar z}
  N_{zz}N^{zz}}_{\text{hard}}
  \;\underbrace{-\;\frac{1}{8\pi G}\!\int\! d^2z\,\gamma^{z\bar z} f\,
  \mathcal O N}_{\text{soft, with }\mathcal O\text{ as in \S3 [reading]}} .
  \]
  Ward identity of the diagonal subgroup [HMLS 3.3–3.4]:
  \(T^+(f)\,\mathcal S-\mathcal S\,T^-(f)=0\), \(f^-(z,\bar z)=f(z,\bar z)\).
- **M (displacement memory).** Between stationary vacua, the DC shear
  shift
  \[
  \Delta C_{zz}(z,\bar z)=\int_{-\infty}^{\infty} du\,N_{zz}=D_z^2 N
  \qquad[\text{HMLS 2.19}],
  \]
  is the relative displacement of nearby inertial detectors at
  \(\mathcal I^+\) (geodesic deviation; [L17] §1.1 and §6: the memory
  formula is the Fourier transform of the soft theorem — pole in
  \(\omega\) ↔ step in \(u\)). The Goldstone representative \(C\) itself is
  *not* a readout; only its \(D_z^2\)-image is.

## 5. Comparison maps (declared, not proved by citation)

- **Mode map** \(\mathcal F\): stationary-phase/asymptotic identification
  of the radiative field with graviton creation/annihilation operators
  [HMLS 5.11–5.18], including the hermitian zero-frequency prescription
  \(N_{zz}^0=\lim_{\omega\to0^+}\tfrac12(N_{zz}^{\omega}+N_{zz}^{-\omega})\)
  [HMLS 5.17] — the zero-frequency prescription is *retained*, per the
  boundary gate.
- **Antipodal matching** \(\mathcal A\): continuity across \(i^0\),
  \(C_{zz}|_{\mathcal I^+_-}=-D_{zz}|_{\mathcal I^-_+}\), i.e.
  \(C=-D\) [HMLS 3.1–3.2], and the diagonal restriction
  \(f^-=f\) [HMLS 3.3]. This is an *external physical input* (it encodes
  Lorentz invariance of the scattering problem; [S14]/[L17 §2.3]).
- **Momentum conservation** \(\mathcal P\): \(\sum_k\eta_k p_k^\mu=0\),
  used to kill the second bracket in [HMLS 6.7].

## 6. Equivalence relations (keep distinct)

1. **Bondi-coordinate representative changes** preserving the Bondi gauge
   form of the metric: the BMS\(^+\) action itself. Supertranslations act
   as \(\mathcal L_f C_{zz}=f\partial_u C_{zz}-2D_z^2 f\) [HMLS 2.7].
2. **Vacuum (Goldstone) shifts**: time-independent supertranslations map
   vacua to vacua, \(C\to C-2f\); \(N\), the news, and the flux are
   invariant (using \(N_{zz}|_{\mathcal I^+_\pm}=0\)); \(\Delta C_{zz}\) is
   invariant. Only the \(D_z^2\)-annihilated \(l=0,1\) data of \(C\)
   (position of the geometry) is unphysical.
3. **Polarization gauge** \(\delta\varepsilon_{\mu\nu}=q_\mu\Lambda_\nu+
   q_\nu\Lambda_\mu\): \(S_{\rm soft}\) is invariant iff \(\mathcal P\)
   holds [HMLS 4.8].
4. **Antipodal/diagonal identification** \(\mathcal A\): not a gauge
   redundancy — a scattering input. Flagged as the one extra ingredient
   closing the soft↔charge leg.
5. **Physical radiative observables**: equivalence class of Bondi
   representatives modulo (1)–(3), with boundary conditions
   \(N_{zz}|_\partial=0\), \(\mathrm{Im}\Psi_2^0|_\partial=0\) retained.
   The readouts \(S_{\rm soft}\), \(T^\pm(f)\), \(\Delta C_{zz}\) must all
   descend to this quotient — the descent checks are part of the checker.

## 7. Gate map

| gate | where enforced |
|---|---|
| gauge/descent | §6 items 1–3,5; checker groups G5 |
| naturality | §5 maps \(\mathcal F,\mathcal A,\mathcal P\); checker G2–G4, G6 |
| boundary | §2 corner conditions, §5 zero-mode prescription; checker G3 |
| no-fit | §4 coefficient table fixed a priori; checker asserts exact equality |
| independence | new content sought: operator-level factorization through \(\mathcal O\) on the \(l\ge2\) quotient, plus typed residuals for the two external inputs |
