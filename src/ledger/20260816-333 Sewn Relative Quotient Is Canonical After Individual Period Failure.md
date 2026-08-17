---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Sewn Relative Quotient Is Canonical After Individual Period Failure

## Record

Status: entry 332 falsified source-canonicity of the two individual physical
occurrence periods. The surviving object has now been constructed at
relative mapping-cone and period-line level. The endpoint polar jets form a
boundary object; occurrence addition descends to a canonical sewn quotient;
and the Kummer period of that quotient obeys an explicit flat rank-one
logarithmic connection.

This does not construct a canonical boundary-evaluation functional for
either occurrence. It does not claim that the full relative extension has
been embedded horizontally into the absolute nine-master connection.

No carrier cell, blowup, endpoint counterterm, regulator hierarchy, support
summand, or normalization is added.

## Deutsch--Popperian conjecture tested

After entry 332, the smaller hard-to-vary claim is

\[
\boxed{
\text{although individual physical periods fail, occurrence addition
descends to a regulator-independent relative Kummer quotient.}
}
\]

The finite falsifiers are failure of the endpoint-jet addition identity,
failure of cyclic covariance, or failure of the sewn period to satisfy one
rank-one flat connection.

## Frozen local normal-crossings model

Use the weighted chart of entries 230--231, 234, 240, 322--331:

\[
E_T=\tau^2,\qquad
q_{\mathfrak g_{31}}=\tau^2r,\qquad
q_{\mathfrak g_{23}}=\tau^2(-r+\tau n).
\]

On the exceptional wall \(r=0\), set

\[
a=xy,\qquad s=x+y,\qquad
w^2=an^2-2s.
\]

At generic nonsoft kinematics, the finite endpoint divisor

\[
D_\partial=\{w=0\}
\]

and the exceptional occurrence wall \(\{r=0\}\) are transverse in local
coordinates \((r,w)\). Thus the source-forced weighted chart already gives
the required local normal-crossings model. Degeneration of this chart is
confined to

\[
xy(x+y)=0,
\]

namely soft or endpoint-collision support already present in the frozen
energy arrangement.

## Relative mapping-cone object

Let \(\mathcal J_\partial^{(9)}\) be the sheaf of polar endpoint jets
through \(w^{-9}\) on \(D_\partial\). The relevant meromorphic relative
complex is the mapping-cone enlargement

\[
\mathcal R
=
\operatorname{Cone}\!\left(
\Omega^\bullet(*D_\partial)
\longrightarrow
\mathcal J_\partial^{(9)}
\right)[-1].
\]

Entry 331 gives

\[
\eta_i
=
c_i\frac{dn}{w}+d\Phi_i,
\qquad
\Phi_i=\frac{H_i(n)}{8a^{3/2}w^9}.
\]

The relative representative retains both pieces:

\[
\widehat\eta_i=(\eta_i,J_\partial\Phi_i).
\]

Changing a meromorphic representative moves data between the bulk form and
its boundary jet; it does not erase the jet. A physical finite-part
evaluation additionally requires a functional

\[
\lambda_\partial:
\mathcal J_\partial^{(9)}\longrightarrow\mathbb C.
\]

Entry 332 proves that the source does not define
\(\lambda_\partial\) occurrence by occurrence.

## Canonical sewing map

Define source sewing by literal occurrence addition:

\[
S(\widehat\eta_{31},\widehat\eta_{23})
=
\left(
\eta_{31}+\eta_{23},
J_\partial\Phi_{31}+J_\partial\Phi_{23}
\right).
\]

Entry 331 proves the polynomial identities

\[
\eta_{31}+\eta_{23}=\eta_{\rm unsplit},
\qquad
\Phi_{31}+\Phi_{23}=\Phi_{\rm unsplit}.
\]

Therefore

\[
\boxed{
S(\widehat\eta_{31},\widehat\eta_{23})
=
\widehat\eta_{\rm unsplit}
}
\]

coefficientwise at all five polar orders

\[
w^{-9},w^{-7},w^{-5},w^{-3},w^{-1}.
\]

The regulator-dependent anti-diagonal allocation belongs to \(\ker S\).
The quotient by this kernel is source-canonical even though no canonical
splitting back to the two occurrences exists.

## Kummer quotient periods

On the physical interval between

\[
n=\pm\sqrt{\frac{2s}{a}},
\]

choose the source sheet

\[
w=i\sqrt{2s-an^2}.
\]

The substitution

\[
n=\sqrt{\frac{2s}{a}}\sin\theta
\]

gives the exact period

\[
\boxed{
\int_{-N}^{N}\frac{dn}{w}
=
-\frac{i\pi}{\sqrt a}.
}
\]

Using the corrected coefficients of entry 331,

\[
\boxed{
\frac{p_{31}}{i\pi}
=
\frac{3x^2+7xy+6y^2}{16(xy)^4},
}
\]

\[
\boxed{
\frac{p_{23}}{i\pi}
=
-\frac{6x^2+7xy+3y^2}{16(xy)^4}.
}
\]

Their exact sum is

\[
\boxed{
\frac{p_{\rm sewn}}{i\pi}
=
-\frac{3(x-y)(x+y)}{16(xy)^4},
}
\]

which is entry 240's unsplit regularized Kummer period.

These \(p_i\) are periods of the Kummer quotients. They are not values of
the full individual relative classes, because evaluating their endpoint
jets would require the noncanonical \(\lambda_\partial\).

## Flat sewn period line

Away from

\[
xy(x-y)(x+y)=0,
\]

the sewn period satisfies

\[
d p_{\rm sewn}=\omega_{\rm sewn}p_{\rm sewn},
\]

with

\[
\boxed{
\omega_{\rm sewn}
=
\left(
\frac{2x}{x^2-y^2}-\frac4x
\right)dx
+
\left(
-\frac{2y}{x^2-y^2}-\frac4y
\right)dy.
}
\]

Since

\[
\omega_{\rm sewn}
=
d\log\!\left(
\frac{x^2-y^2}{(xy)^4}
\right),
\]

its curvature vanishes:

\[
d\omega_{\rm sewn}=0.
\]

Thus the sewn Kummer period spans a horizontal rank-one Tate/Kummer line.
This is a period-level Gauss--Manin statement. Compatibility of the entire
jet extension with the absolute nine-master connection is not inferred.

## Boundary-limit audit

The admissible operations separate as follows.

1. Boundary value before the exceptional grade retains one of the chamber
   currents \(2,0,0,-2\) of entries 231, 332.
2. Exceptional grade before boundary value gives the canonical meromorphic
   classes and endpoint jets of entries 330--331.
3. Endpoint finite part requires \(\lambda_\partial\) and is noncanonical
   for either occurrence.
4. Source sewing kills the anti-diagonal chamber allocation and yields the
   unsplit relative class before evaluation.
5. The total-energy deck action gives sign \(-1\) on both Kummer
   cohomology and transported chain, hence trivial monodromy on the period.
6. Soft limits \(x=0\) or \(y=0\) produce poles already classified as
   soft support. They do not alter the generic no-go or the sewn identity.
7. At \(x=y\), the two nonzero occurrence quotient periods cancel and the
   sewn period vanishes. This is a coefficient zero, not a new carrier
   incidence.

Therefore every generic order either factors through the sewn quotient or
retains an explicitly classified boundary/regulator choice. No
occurrence-level canonical physical number is recovered.

## Infinity-Gysin and \(\mathcal T_7\)

Entries 240, 329--331 show that the wall Kummer class has zero direct image in
the anticanonical Legendre quotient. Hence

\[
R_\infty(\widehat\eta_{\rm unsplit})=0.
\]

The sewn line belongs to the algebraic/relative kernel sector
\(\mathcal T_7\), not the rank-two elliptic quotient. This is type
compatibility only: no canonical coordinate in the absolute
\(\mathcal T_7\) connection or identification with \(L_1\) is claimed.

## Verification

The exact Rust certificate checks:

- 4,096 occurrence-period sewing identities;
- 8,064 rational horizontal-connection identities;
- 12,288 cyclic marked-sector sewing identities;
- warning-denied optimized compilation.

An independent 100-decimal contour calculation checks generic
\((1,2)\), generic \((2,5)\), near-diagonal, and near-soft kinematics.
The largest relative integral error is below \(1.3\times10^{-101}\), and
the largest relative sewing error is below \(2.6\times10^{-101}\).

The near-diagonal test resolves cancellation between two order-one
occurrence periods to a sewn period of order \(10^{-40}\). The near-soft
test reaches periods of order \(10^{159}\) while retaining the sewn
identity.

Evidence:

- research/benincasa/check_occurrence_relative_extension.rs;
- research/benincasa/occurrence-relative-extension.json;
- research/benincasa/verify_occurrence_relative_periods.py;
- research/benincasa/occurrence-relative-periods-numeric.json.

## Verdict

The smaller conjecture survives:

\[
\boxed{
\text{canonical occurrence de Rham/jet pair}
\xrightarrow{\;S\;}
\text{canonical horizontal sewn Kummer period line}.
}
\]

There is no canonical inverse splitting and no source-canonical individual
physical occurrence period.

## Classification

- existing carrier: unchanged exceptional wall, endpoint divisor,
  total-energy cover, and cyclic marked sectors;
- relative-chain data: boundary-value chamber and endpoint functional;
- Tate/Kummer data: two occurrence quotient lines and their sewn line;
- extension data: endpoint polar-jet mapping cone and anti-diagonal kernel;
- soft support: \(xy=0\);
- coefficient zero: \(x^2-y^2=0\);
- Legendre/Gauss--Manin data: zero direct elliptic image;
- algebraic kernel: compatible with \(\mathcal T_7\), without a chosen
  absolute coordinate;
- genuinely new carrier structure: none.

## Next finite falsifier

Compute the Gauss--Manin derivative of the full five-level endpoint-jet
vector

\[
J_i=(J_i^{(-9)},J_i^{(-7)},J_i^{(-5)},J_i^{(-3)},J_i^{(-1)})
\]

using closed symbolic formulas for \(H_{31}\) and \(H_{23}\). Test
whether the anti-diagonal kernel of \(S\) is connection-stable and whether
the quotient connection equals \(\omega_{\rm sewn}\) without choosing a
boundary splitting.

Failure of kernel stability would falsify a horizontal full relative
extension while preserving the period-line result. It would remain
coefficient/extension data unless a missing source incidence were
independently derived.

## Outcome contract

~~~json
{
  "claim": "Occurrence addition descends to a regulator-independent relative Kummer quotient after individual physical periods fail.",
  "status": "survives_at_mapping_cone_and_period_line_level",
  "individual_physical_periods": "not_source_canonical",
  "individual_kummer_quotient_periods": "exactly_computed",
  "endpoint_jet_evaluation": "requires_noncanonical_boundary_functional",
  "sewing_map": "literal_addition",
  "sewn_period": "-3*i*pi*(x-y)*(x+y)/(16*(x*y)^4)",
  "sewn_period_line_horizontal": true,
  "full_relative_extension_horizontal": "uncomputed",
  "direct_legendre_gysin_image": 0,
  "algebraic_kernel_compatibility": "type_level_only",
  "new_carrier_incidence": false,
  "next_experiment": "Derive closed individual endpoint jets and test connection stability of the anti-diagonal sewing kernel."
}
~~~
