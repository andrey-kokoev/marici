# Source remainder and order closability require incompatible endpoint coefficients

## Correction

The previous version incorrectly inferred closability of a sum from cancellation of one displayed decomposition term. The sourced decay of \(H\) shows the opposite disposition.

## Claim boundary

The source remainder-localizer identity uniquely requires the endpoint coefficient \(e^{h/4}-1\). Closability in the order topology requires that coefficient to vanish. Since \(h>0\), the requirements are incompatible. A stronger common domain is necessary.

## Two requirements

The source identity is

\[
K_R(a,b)
=
K_H(a,b)
+
\alpha_he^{(a+b)/4},
\qquad
\alpha_h=e^{h/4}-1.
\]

Thus the remainder cone requires coefficient

\[
c_{\rm source}=\alpha_h.
\]

For the order-null sequence

\[
f_a=e^{-a/4}g_a,
\]

the raw completed-heat contribution tends to zero, while

\[
|L_E(f_a)|^2=1
\]

and endpoint evaluation cancels on differences. Hence a form

\[
q_H+c|L_E|^2
\]

can be closable on this sequence only if

\[
c_{\rm close}=0.
\]

For \(h>0\),

\[
c_{\rm source}
=
e^{h/4}-1
\neq
0
=
c_{\rm close}.
\]

## Consequence

The endpoint term cannot be removed without changing the remainder-localizer target, and it cannot be retained on the order completion without destroying closability. The residual does not ask for another scalar counterterm. It rules out the topology.

The required coherencer must strengthen the norm so that \(L_E\) is continuous, for example by including an endpoint graph term. Such a stronger norm remains diagnostic until the prime and gamma source forms are also shown closable on it.

## Disposition

`endpoint_scalar_coherencer_on_H_ord` is rejected. The first missing object is again a stronger common closed-form domain containing the endpoint evaluation continuously. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_unique_endpoint_coherencer.py`
- `research/voevodsky/results/unique_endpoint_coherencer.json`
