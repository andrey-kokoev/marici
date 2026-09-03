# The minimal weighted endpoint lift is reflection-equivariant but prime descent remains open

## Question

Do endpoint recovery and the minimal harmonic lift on the weighted relative history space intertwine reciprocal reflection and prime-label actions?

## Source carrier

The source-native history space uses the even weight

\[
w(u)=(1+|u|)^{1+\epsilon}
\]

and endpoint recovery

\[
T f=(f(-\infty),f(+\infty)).
\]

History reflection is \((R_Hf)(u)=f(-u)\), while endpoint reflection is

\[
R_E(a,b)=(b,a).
\]

Directly,

\[
TR_H=R_ET.
\]

Thus endpoint recovery is reciprocally equivariant.

## Minimal lift

Among histories with endpoints \((a,b)\), minimizing

\[
\int_{\mathbb R}w(u)|f'(u)|^2\,du
\]

forces \(w f'\) to be constant. Put

\[
Z=\int_{\mathbb R}w(v)^{-1}\,dv,
\qquad
q(u)=Z^{-1}\int_{-\infty}^{u}w(v)^{-1}\,dv.
\]

The unique energy-minimizing lift is

\[
(P_{\min}(a,b))(u)=a+(b-a)q(u).
\]

It satisfies \(TP_{\min}=I\). Since \(w\) is even,

\[
q(-u)=1-q(u).
\]

Therefore

\[
R_HP_{\min}(a,b)
=P_{\min}(b,a)
=P_{\min}R_E(a,b).
\]

Both reflection intertwiners hold. Consequently

\[
A=I-P_{\min}T
\]

commutes with reciprocal reflection and projects onto the zero-endpoint-trace subspace.

## Prime-label gate

The weighted-history source packet explicitly leaves preservation of prime spectral idempotents as a remaining gate. The formulas above are scalar in the source label, so a declared componentwise direct sum would make \(T\), \(P_{\min}\), and \(A\) label diagonal. But no current source map proves that the prime/grade incidence lands in those componentwise weighted spaces or that its idempotents extend to the closed history domain.

Hence reciprocal equivariance is proved on the actual weighted carrier, while prime-label equivariance remains conditional. Equal scalar formulas across labels do not construct the missing direct-sum descent.

## Disposition

Accept the reciprocal intertwiner identities and zero-trace reflection covariance. Do not claim prime-label preservation. The first missing typed object is a closed prime/grade incidence map into the transported spaces \(\mathcal E_{w,L}\) together with extension of the prime spectral idempotents to the relative-history domain.
