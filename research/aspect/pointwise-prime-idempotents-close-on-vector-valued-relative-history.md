# Pointwise prime idempotents close on vector-valued relative history

## Question

What exact functional-analytic condition makes prime spectral idempotents compatible with the weighted relative-history domain, endpoint recovery, and the minimal lift?

## Vector-valued carrier

Let \(K\) be the coefficient Hilbert space and let \(e_p:K\to K\) be a bounded idempotent. Define \(\mathcal H_{\rm rel}(K)\) by the same weighted graph norm as the scalar history space:

\[
\|f\|_{\rm rel}^2
=\int_{\mathbb R}w(u)\|f'(u)\|_K^2\,du
+\|f(-\infty)\|_K^2+\|f(+\infty)\|_K^2.
\]

Let the pointwise extension be

\[
(E_pf)(u)=e_pf(u).
\]

Then \((E_pf)'=e_pf'\), and boundedness of \(e_p\) gives

\[
\|E_pf\|_{\rm rel}\le \|e_p\|\,\|f\|_{\rm rel}.
\]

Therefore \(E_p\) extends to the closed relative-history domain and satisfies \(E_p^2=E_p\).

## Endpoint and lift intertwiners

On endpoint space \(K\oplus K\), put

\[
e_p^E(a,b)=(e_pa,e_pb).
\]

Continuity of endpoint traces gives

\[
TE_p=e_p^ET.
\]

The weighted minimal lift is coefficientwise:

\[
(P_{\min}(a,b))(u)=a+(b-a)q(u).
\]

Hence

\[
E_pP_{\min}=P_{\min}e_p^E.
\]

It follows that the zero-trace projection \(A=I-P_{\min}T\) commutes with every pointwise prime idempotent.

## Transported weights

For \(w_L(u)=w(u+L)\), the same estimate holds because \(e_p\) acts on \(K\), not on the carrier coordinate. Translation between the object-indexed weighted spaces commutes with \(E_p\). No uniform comparison with one fixed weight is required.

## Exact source boundary

This theorem reduces the missing prime-descent claim to one typed source question: does the arithmetic prime projector act as a bounded coefficient-space idempotent independent of the carrier coordinate after the incidence map lands in \(\mathcal E_{w,L}(K)\)? If yes, closure and all required intertwiners follow. If the projector depends on \(u\), then

\[
(E_pf)'=e_p'f+e_pf'
\]

and the extra term is the exact graph-domain obstruction. Equal prime labels at endpoints do not remove it.

## Disposition

The functional-analytic closure theorem is proved. What remains source-dependent is the factorization of prime incidence through a coefficient Hilbert space with bounded, carrier-independent spectral idempotents. This is the acceptance test for the outstanding owner handoff.
