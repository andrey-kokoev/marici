# Mixed-axis tail-margin certificate

## Question

How can a finite arithmetic approximation certify an observer statement about the completed coupled form without requiring cutoff-wise positivity?

## Claim boundary

The certificate derives the tail-to-eigenvalue comparison and verifies its logic. The constants governing the actual completed prime kernel and positivity for all packets remain unsupplied.

## Entrywise prime tail

At fixed observer width, suppose every omitted prime-derived matrix entry is bounded by

\[
\epsilon_N
\leq
2C\sum_{n>N}
\log(n)n^{-1/2}e^{-c\log(n)^2}.
\]

For \(L=\log N\) beyond the monotonicity threshold, the integral test gives

\[
\sum_{n>N}\log(n)n^{-1/2}e^{-c\log(n)^2}
\leq
e^{1/(16c)}
\left[
\frac{e^{-c(L-1/(4c))^2}}{2c}
+
\frac{\sqrt{\pi}}{8c\sqrt c}
\operatorname{erfc}\!\left(\sqrt c(L-1/(4c))\right)
\right].
\]

The checker verifies this antiderivative symbolically.

## Passage from source cutoff to observer packet

For an observer packet \(I\) of rank \(r\), an entrywise tail bound gives

\[
\|R_{I,N}\|_{\mathrm{op}}
\leq r\epsilon_N.
\]

Let \(G_{I,N}\) be the truncated Gram matrix and

\[
G_I=G_{I,N}+R_{I,N}
\]

the completed packet. Weyl's bound yields three dispositions:

| Computed margin | Certified completed disposition |
|---|---|
| \(\lambda_{\min}(G_{I,N})-r\epsilon_N\geq0\) | positive semidefinite |
| \(\lambda_{\min}(G_{I,N})+r\epsilon_N<0\) | not positive semidefinite |
| \(|\lambda_{\min}(G_{I,N})|\leq r\epsilon_N\) | unresolved at this cutoff |

The unresolved interval must not be reported as positivity or negativity.

## Deeper role

This estimate is the comparison cell between the opposed limits. The arithmetic index \(N\) approaches the completed source covariantly. The packet index \(I\) imposes positivity contravariantly. The factor \(r\) quantifies their coupling: larger observer packets require deeper arithmetic cutoffs unless their eigenvalue margins grow correspondingly.

Therefore the two limits are not independent. A valid diagonal schedule must choose \(N=N(I)\) so that

\[
r(I)\epsilon_{N(I)}
<
\lambda_{\min}(G_{I,N(I)})
\]

whenever the intended packet has a positive margin. Strict positivity permits finite certification; a zero limiting eigenvalue may remain forever inside the unresolved band and requires a separate semidefinite argument.

## Disposition

The mixed-axis certificate replaces the false demand for cutoff-wise positivity. It allows indefinite arithmetic truncations while providing rigorous positive or negative conclusions about completed finite observer packets. The remaining source gate is an explicit derivation of \(C,c\) and compatibility of the tail estimate with endpoint and gamma terms. The remaining global gate is positivity for every packet, including zero-margin boundary cases.

## Verification

- `research/voevodsky/mixed-axis-tail-margin-certificate-v1.json`
- `research/voevodsky/checkers/check_mixed_axis_tail_margin_certificate.py`
- `research/voevodsky/results/mixed_axis_tail_margin_certificate.json`
