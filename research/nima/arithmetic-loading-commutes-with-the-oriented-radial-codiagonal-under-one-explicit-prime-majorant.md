# Arithmetic loading commutes with the oriented radial codiagonal under one explicit prime majorant

## Question

Can the six-coordinate radial boundary feature be assembled over primes before G4 exposes its canonical arithmetic loading?

## Claim boundary

Analytic assembly can be proved for any label-diagonal loading satisfying one explicit weighted majorant. Under that condition, prime summation commutes with the oriented wall codiagonal, endpoint-minus-Wronskian factorization, shell completion, and every compact-local parameter jet. Existing source coefficients satisfy stronger bounds, so convergence is not the current obstruction. Selecting which coefficient is G4's canonical loading remains open.

## Local feature packet

For each prime shell retain

\[
X_p=
\bigl(
-\rho_p(0),E_{p,+},W_{p,+};
+\rho_p(0),E_{p,-},W_{p,-}
\bigr).
\]

For a compact parameter set \(K\) and jet order \(j\), let \(s_{K,j}(X_p)\) be the sum of the two wall magnitudes and compact suprema of the four endpoint/Wronskian jet probes. Completed-theta decay and the existing rapid radial topology give a bound of the form

\[
s_{K,j}(X_p)
\le C_{K,j}\bigl(1+(\log p)^{M_j}\bigr)
\]

for some finite \(M_j\). The sharper shell formulas are superexponentially smaller, but the polylogarithmic bound suffices for the admitted mixed Euler weight.

## Sufficient loading criterion

Let \(\omega_p\) be a label-diagonal source coefficient. If

\[
\sum_p |\omega_p|
\bigl(1+(\log p)^{M_j}\bigr)<\infty
\]

for every fixed jet order, then

\[
X^{\rm ar}=\sum_p\omega_pX_p
\]

converges absolutely in every compact-local feature seminorm. Prime truncations are Cauchy uniformly on \(K\), and parameter differentiation commutes with summation by the same majorant.

## Existing admissible coefficients

The mixed primitive-square coefficient

\[
\omega_p^{\rm mix}(\sigma)
=\frac12p^{-3/2-\sigma}
\]

satisfies the criterion uniformly for \(\sigma\ge0\), including the seam. The source-derived Euler-to-theta coefficient

\[
c_p=2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p)
\]

has superexponential prime-power decay and also satisfies it. These facts prove two admissible analytic assemblies; they do not identify the two coefficients or authorize either as G4's canonical codiagonal loading.

## Commutation with the oriented codiagonal

Define the local source codiagonal

\[
C_pX_p
=E_{p,+}+E_{p,-}
-\frac12\bigl(W_{p,+}+W_{p,-}\bigr).
\]

Absolute convergence gives

\[
\sum_p\omega_pC_pX_p
=C\left(\sum_p\omega_pX_p\right),
\]

where \(C\) is the direct-sum codiagonal with the same frozen wall signs and Wronskian coefficient. Since the wall entries are retained in \(X_p\), their opposite-sign cancellation occurs locally before any prime labels are mixed. Scalar cancellation across different primes is neither needed nor allowed.

The same argument commutes adjacent-shell completion with prime truncation, provided every finite packet is obtained by restricting one fixed local family rather than recomputing cutoff-dependent normalizations.

## What convergence does not prove

The majorant does not establish:

1. that G4 chooses \(\omega_p^{\rm mix}\), \(c_p\), or another coefficient;
2. prime diagonality of the complete Green form;
3. radical annihilation or closable descent;
4. equality of analytic transpose and metric adjoint;
5. the arithmetic cancellation identity on Xi jets.

Cross-prime Green blocks would require a separate Schur or Hilbert-Schmidt estimate. The source incidence is label diagonal, but that alone does not prohibit nonlocal cross-prime return blocks.

## Direction rescore

- Analytic arithmetic assembly of the oriented feature packet: completed conditionally, with two existing coefficients meeting the condition.
- Canonical coefficient selection: 10/10 but interface-blocked by G4.
- Prime-diagonal Green return and radical descent: 9/10 after interface exposure.
- Additional convergence estimates: 2/10 unless a proposed G4 loading violates the majorant.

## Disposition

The radial boundary feature has no remaining prime-summability obstruction for either existing source loading. The frontier is typed identification: G4 must declare its coefficient, prime return structure, feature metric, and codiagonal before the finite polarized comparison can decide conformance. No RH conclusion is authorized.
