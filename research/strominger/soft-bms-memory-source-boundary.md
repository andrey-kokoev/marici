# Source and boundary packet: the leading triangle maps (marici.Strominger)

Companion to `soft-bms-memory-conventions.md` (sources and equation numbers
are there; [HMLS] = arXiv:1401.7026). This packet exports the actual maps,
orientations, support and boundary conditions, and naturality squares that
the checker `checkers/leading_triangle_exact_checks.py` verifies. Nothing
here is proved by citing the correspondence; every identity below is a
check item with a declared left and right side.

## 1. The carrier field

The construction of [HMLS §2] shows that the physical phase space at
\(\mathcal I^+\) is
\(\Gamma^+ = \{C(z,\bar z),\,N(z,\bar z),\,C_{zz}(u,z,\bar z),\,C_{\bar z\bar z}(u,z,\bar z)\}\)
[HMLS 2.20], where the real scalar \(N\) is defined by
\(\int du\,N_{zz} = D_z^2 N\) [HMLS 2.19] and \(C\) by
\(C_{zz}|_{\mathcal I^+_-}=D_z^2 C\) [HMLS 2.18].

Claim to be tested, not assumed: **the single scalar field
\(N(z,\bar z)\) on the \(l\ge 2\) quotient is the common carrier** of all
three corners; each corner is one fixed operation on \(N\) with a
sector-specific coefficient and readout:

\[
\text{soft: } \mathcal F[N]\ \text{(mode map to a soft graviton insertion)}
\qquad
\text{charge: } Q_f^{\rm soft}[N]=-\tfrac{1}{8\pi G}\!\int\! d^2z\,\gamma^{z\bar z} f\,\mathcal O N
\qquad
\text{memory: } \Delta C_{zz}=D_z^2 N .
\]

## 2. Orientations and corner structure

- \(\mathcal I^+_\pm\): past (\(i^0\)-side) and future (\(i^+\)-side)
  boundaries of \(\mathcal I^+\); mirrored at \(\mathcal I^-_\mp\).
- News vanishes at all four corners [HMLS 2.15]; magnetic-parity condition
  \(D_z^2 C_{\bar z\bar z}=D_{\bar z}^2 C_{zz}\) at the corners
  [HMLS 2.16].
- The soft charge is a *total retarded-time derivative*: its value is the
  **difference of corner terms** at \(\mathcal I^+_+\) and
  \(\mathcal I^+_-\). Both corners are retained in the checker; dropping
  one is exercised as a deliberate-failure test (boundary gate).
- Zero-frequency prescription [HMLS 5.17]:
  \(N_{zz}^0=\lim_{\omega\to0^+}\tfrac12(N_{zz}^{\omega}+N_{zz}^{-\omega})\),
  hermitian; used in the mode map.
- Antipodal matching at \(i^0\) [HMLS 3.1–3.3]: \(C=-D\), \(f^-=f\).

## 3. Map S: soft residue (exact kernel)

From the definitions [HMLS 6.5] alone (checker G2), per hard leg:

\[
\boxed{\;\omega\,\frac{[p_k\cdot\varepsilon^+(z)]^2}{p_k\cdot q}
= -\,E_k\,\frac{(\bar z-\bar z_k)\,(1+z\bar z)}{(z-z_k)\,(1+z_k\bar z_k)}\;}
\]

Intermediate exact identities verified on the way:
\(p_k\cdot\varepsilon^+=\sqrt2\,E_k(\bar z_k-\bar z)/(1+z_k\bar z_k)\) and
\(p_k\cdot q=-2E_k\omega\,S_k\) with
\(S_k=\sin^2(\Theta_k/2)=(z-z_k)(\bar z-\bar z_k)/[(1+z\bar z)(1+z_k\bar z_k)]\)
(the same \(S\) as the Green's kernel below).

Polarization-gauge descent [HMLS 4.8]: per leg,
\((q_\mu\Lambda_\nu+q_\nu\Lambda_\mu)p_k^\mu p_k^\nu/(p_k\cdot q)
=2\,\Lambda\cdot p_k\), so \(\delta S_{\rm soft}=\kappa\,\Lambda\cdot
\sum_k\eta_k p_k\): invariant iff \(\mathcal P\) holds.

## 4. Map Q: Ward identity and the corner decomposition

Charge [HMLS 2.11] in flux form:
\[
T^+(f)=\frac{1}{16\pi G}\int du\,d^2z\,f\big[\gamma_{z\bar z}N_{zz}N^{zz}
+2\,\partial_u(\partial_z U_{\bar z}+\partial_{\bar z}U_z)\big],
\qquad U_z=-\tfrac12 D^z C_{zz}\ [\text{HMLS 2.2}].
\]
The \(u\)-integral of the second term is the corner difference
\(\frac{1}{8\pi G}\int d^2z\,f\,[B]_{\mathcal I^+_-}^{\mathcal I^+_+}\) with
\(B=\partial_z U_{\bar z}+\partial_{\bar z}U_z\). The checker derives the
exact pointwise operator identity expressing \(B\) through \(D_z^2\),
\(D_{\bar z}^2\) acting on \(C_{zz},C_{\bar z\bar z}\), applies the corner
condition [HMLS 2.16], and compares coefficients against the soft term of
[HMLS 2.30]. The derived identity (connection terms included) is
\[
B\big|_{\rm corner}=-\,\gamma^{z\bar z}D_{\bar z}^2 C_{zz}
\quad\Longrightarrow\quad
[B]_{\mathcal I^+_-}^{\mathcal I^+_+}
=-\,\gamma^{z\bar z}D_{\bar z}^2D_z^2 N=-\,\gamma_{z\bar z}\,\mathcal O N ,
\]
whose overall sign agrees with the printed soft term of [HMLS 2.30]
(checks G3.3–G3.5). The retained typed residual is the operator
*ordering* \(D_z^2D_{\bar z}^2\) vs \(D_{\bar z}^2D_z^2\), which differs by
curvature action on the spin-2 intermediate and is fixed by the
scalar-\(\mathcal O\) reading of conventions packet §3. **Any factor or
connection-term discrepancy is recorded as a typed residual in the
results JSON, not absorbed.**

With \(f(w,\bar w)=1/(z-w)\) the Ward identity becomes [HMLS 3.6]:
\(\langle:P_z\mathcal S:\rangle=\langle\mathcal S\rangle
\big[\sum_{\rm out}E_k/(z-z_k)-\sum_{\rm in}E_k/(z-z_k)\big]\), with soft
current \(P_z=\frac{1}{4G}\gamma^{z\bar z}\partial_{\bar z}\mathcal O_{zz}\),
\(\mathcal O_{zz}=N_{zz}^0+M_{zz}^0\) [HMLS 5.23–5.24].

## 5. Map M: displacement memory and the zero-frequency link

\(\Delta C_{zz}=\int du\,N_{zz}=D_z^2N\) [HMLS 2.19]. The Fourier
statement (pole ↔ step): the zero-frequency news is the DC shear shift,
and by [HMLS 5.22] \(N_{zz}^0=D_z^2N\); the same \(N\) enters the soft
charge. The geodesic-deviation readout (detector displacement
\(\propto\Delta C_{zz}\)) is the physical observable [L17 §1.1, §6].

## 6. Naturality squares (exact statements to check)

- **SQ1 (soft ↔ charge).** Mode map then Ward:
  \(\langle:\mathcal O_{zz}\mathcal S:\rangle
  =\frac{8G}{1+z\bar z}\sum_k\eta_k E_k
  \frac{\bar z-\bar z_k}{(z-z_k)(1+z_k\bar z_k)}\langle\mathcal S\rangle\)
  [HMLS 6.6] — the checker derives this from the §3 kernel, the prefactor
  \(-\kappa/[2\pi(1+z\bar z)^2]\) of [HMLS 6.3], and \(\kappa^2=32\pi G\).
- **SQ2 (charge ↔ current).** \(\frac{1}{4G}\gamma^{z\bar z}\partial_{\bar z}\)
  of the SQ1 kernel reproduces the [HMLS 3.6] kernel *plus* the residual
  bracket \(\sum_k\eta_k E_k\bar z_k/(1+z_k\bar z_k)\) [HMLS 6.7], and the
  residual equals \(\tfrac12\sum_k\eta_k(p_k^1-ip_k^2)\) — killed exactly
  by \(\mathcal P\). The checker verifies both the rational identity and
  the residual's identification, and re-runs without \(\mathcal P\) to
  exhibit the typed obstruction.
- **SQ3 (memory ↔ soft).** \(\Delta C_{zz}=D_z^2N=N_{zz}^0\) chain:
  corner difference of the shear = zero-frequency news = image of the
  carrier \(N\) under the same \(D_z^2\) that defines the soft charge
  kernel. Coefficient chains of the mode map [HMLS 5.13–5.18] verified
  symbolically.

Green's-function support identities [HMLS 2.25–2.26], with
\(S=(z-w)(\bar z-\bar w)/[(1+z\bar z)(1+w\bar w)]=\sin^2(\Theta_{zw}/2)\):
\[
D_w^2\big(S\ln|z-w|^2\big)=\frac{S}{(z-w)^2},\qquad
D_{\bar z}^2\frac{S}{(z-w)^2}=0\ \ (z\neq w),\quad
D_{\bar z}^2D_w^2\big(S\ln|z-w|^2\big)=\pi\gamma_{z\bar z}\delta^2(z-w).
\]
The first two are exact rational checks; the third's distributional
coefficient uses the standard prescription
\(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2(z-w)\) — declared here as the
retained zero-frequency/boundary prescription, not silently assumed.

## 7. Sphere operator identity (common kernel)

Claimed and tested as an operator identity on a generic scalar:
\[
\mathcal O f\equiv(\gamma^{z\bar z})^2 D_{\bar z}^2\big(D_z^2 f\big)
=\tfrac14 D^2(D^2+2)f .
\]
Consequences checked explicitly on STF harmonics \(l=0..4\):
eigenvalue \(\tfrac14(l-1)l(l+1)(l+2)\); \(\ker D_z^2=\{l=0,1\}\)
(4 real dimensions, the \(C,N\) zero modes of [HMLS footnote 3]);
\(\mathcal O\) invertible on the \(l\ge2\) quotient. The three readouts
then factor as one carrier operation with sector coefficients:
soft \(\kappa/2\) (residue), charge \(1/8\pi G\) (charge), memory \(1\)
(DC shift per unit shear) — with readouts in different spaces
(\(\mathcal S\)-matrix kernel, charge functional, detector displacement).

## 8. External inputs ledger (independence gate)

1. Antipodal matching \(\mathcal A\) [HMLS 3.1–3.3]: needed to combine
   \(T^+\) and \(T^-\) into the diagonal Ward identity closing SQ1/SQ2.
2. Four-momentum conservation \(\mathcal P\): needed to kill the residual
   bracket in SQ2 [HMLS 6.7] and for polarization-gauge descent [HMLS 4.8].
3. The hermitian zero-frequency prescription [HMLS 5.17]: a choice of
   boundary/operator ordering, retained explicitly.

No other input is used. In particular the known soft–BMS–memory
correspondence is nowhere invoked as a proof step; every link is an
explicit identity checked from the declared definitions.
