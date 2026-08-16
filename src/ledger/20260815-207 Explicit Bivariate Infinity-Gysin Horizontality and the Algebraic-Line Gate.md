---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Explicit Bivariate Infinity--Gysin Horizontality and the Algebraic-Line Gate

## Record

Date: 2026-08-15

Status: exact finite-field certificate for the generic bivariate final
four-master de Rham block. Extension through the discriminant, integral
normalization, physical relative-chain compatibility, and the algebraic
rank-one factor remain open.

This entry continues entries 150, 169, 178, 183, and 199. It adds no
denominator, support component, projector, splitting, or carrier cell.

## Deutsch--Popperian claim

Freeze the reconstructed bivariate source connection
\[
d e=A_4 e,
\]
the binary-quartic boundary
\[
D_\infty:\quad W^2=F(t),
\]
the elliptic connection
\[
d\omega=B_{\rm ell}\omega,
\]
and the explicit infinity-residue matrix
\[
C=R_\infty:
\langle e_6,e_7,e_8,e_9\rangle
\longrightarrow
\langle\omega_0,\omega_2\rangle.
\]

The hard-to-vary claim was:
\[
\boxed{dC+C B_{\rm ell}-A_4C=0}
\]
on the generic bivariate de Rham locus.

Its finite falsifier was any nonzero entry of this residual in either
independent normal direction. All four sign conventions were tested so that a
vanishing residual could not be obtained by choosing a convention after
inspection.

## Independent construction

The source matrix \(A_4\) is the previously reconstructed bivariate
Griffiths--Dwork connection. The target matrix \(B_{\rm ell}\) was not
extracted from \(A_4\): it was derived independently by reducing the
derivatives of
\[
\omega_0=\frac{dt}{W},\qquad
\omega_2=\frac{t^2dt}{W}
\]
on the binary quartic \(W^2=F(t)\).

The matrix \(C\) is the explicit boundary residue:
\[
C=
\begin{pmatrix}
0&0\\
1&0\\
\frac{E^2+y^2}{2}&-\frac{E^2+x^2}{2}\\
\frac{E^2+x^2}{2}&-\frac{x^2(E^2+y^2)}{2y^2}
\end{pmatrix}.
\]
The first row records \(R_\infty(e_6)=0\).

## Hostile finite-field result

Over
\[
\mathbf F_p,\qquad p=2^{61}-1=2305843009213693951,
\]
the checker sampled 1,024 generic bivariate points and both independent
directions, for 2,048 matrix tests.

For the source-fixed row convention,
\[
\boxed{dC+C B_{\rm ell}-A_4C=0}
\]
at every test:

- nonzero residual entries: \(0\);
- maximum residual rank: \(0\);
- rowwise nonzero counts: \((0,0,0,0)\).

The alternatives fail:

\[
\begin{array}{c|c|c}
\text{formula}&\text{nonzero entries}&\text{maximum rank}\\ \hline
dC+C B_{\rm ell}+A_4C&12288&2\\
dC-C B_{\rm ell}-A_4C&12288&2\\
dC-C B_{\rm ell}+A_4C&6144&2
\end{array}
\]

Thus the vanishing is sign-selective rather than a rank-deficient tautology.

## Narrow consequence

Since \(C\) has generic rank two and is horizontal, its generic kernel is a
connection-stable rank-two algebraic plane:
\[
\ker C=\langle e_6,v_{\rm alg}\rangle.
\]
The quotient is exactly the rank-two elliptic boundary system:
\[
\frac{\langle e_6,e_7,e_8,e_9\rangle}
{\langle e_6,v_{\rm alg}\rangle}
\simeq H^1(D_\infty)(-1).
\]

The earlier nonzero symbolic Gysin residual was therefore a
convention/implementation defect, not evidence for a generic extension
obstruction. The defect is repaired by the independently derived target
connection and verified by the hostile sign census.

This does not imply that the full nine-master extension splits. It proves only
that the explicit generic final-block Gysin quotient is a morphism of
connections and that its kernel is preserved.

## Classification

The result is
\[
\boxed{
\text{existing energy carrier}
+
\text{horizontal sector-specific coefficient quotient}.
}
\]

No new carrier datum appears. The pure elliptic quotient is horizontal, while
the unresolved algebraic information remains inside its rank-two kernel.

## Scope boundary

Not proved:

- extension of the Gysin morphism through the discriminant;
- integral lattice normalization;
- compatibility with the physical relative integration chain;
- a canonical splitting of the final block or the full nine-master sequence;
- identification of the flat rank-one algebraic subquotient;
- provenance of \(\mathcal Q\) in \(L_1\), the algebraic connection, or an
  extension class;
- any all-graph or all-loop statement.

Finite-field generic closure is not a supported-extension theorem.

## Exact evidence

- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/infinity-gysin-certificate.json`;
- raw ignored run `gysin-1024.json`, SHA-256
  `b9935e4969d9ccc37edcf062e3f3054d6dcf367fac0f4092280a652b79396a80`;
- 1,024 generic points, 2,048 directional tests;
- release unit tests passed.

## Next hostile falsifier

Compute the induced Gauss--Manin connection on
\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle.
\]
Determine the rank-one flat line or quotient selected by the cyclic
last-three-master module, and test without fitted gauge whether its scalar
connection is rationally equivalent to
\[
\partial-\frac12d\log(-\mathcal Q).
\]

Failure means \(\mathcal Q\) is not the algebraic \(L_1\) line and must be
tested as extension data. Success localizes \(\mathcal Q\) to the algebraic
coefficient sector without changing the carrier.

## Outcome contract

~~~json
{
  "claim": "The explicit infinity-Gysin projection is horizontal for the generic bivariate final four-master connection.",
  "status": "verified_generic_finite_field_de_rham",
  "prime": "2305843009213693951",
  "sample_points": 1024,
  "directions": 2048,
  "horizontal_formula": "dC+C*B_ell-A4*C",
  "horizontal_nonzero_entries": 0,
  "horizontal_max_rank": 0,
  "alternative_sign_conventions_failed": 3,
  "generic_gysin_rank": 2,
  "generic_kernel_rank": 2,
  "generic_kernel_connection_stable": true,
  "new_carrier_datum": false,
  "classification": "existing carrier plus horizontal sector-specific elliptic coefficient quotient",
  "scope": "generic finite-field final-block de Rham locus only",
  "next_experiment": "Compute the induced algebraic-plane connection and test the cyclic rank-one subquotient against -1/2 dlog(-Q)."
}
~~~
