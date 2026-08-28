# The Positive Mellin Ray Has Two Additive Tate Lifts

## The missing binary port

A state on the positive multiplicative ray does not determine a state on the
additive real line. It has two canonical parity lifts:

\[
f_+(x)=f_+( -x),
\qquad
f_-(x)=-f_-(-x).
\]

After the unitary logarithmic half-density identification, these give the two
Hankel operators

\[
(K_+g)(r)=2\int e^{(r+q)/2}\cos(2\pi e^{r+q})g(q)\,dq,
\]

\[
(K_-g)(r)=-2i\int e^{(r+q)/2}\sin(2\pi e^{r+q})g(q)\,dq.
\]

The positive-ray Mellin carrier alone has forgotten which lift was chosen.
Additive parity is therefore an independent comparison port, not a property
of reciprocal reflection (q\mapsto-q\).

## Exact squared sheet laws

Additive Fourier transform satisfies

\[
\mathcal F_x^2f(x)=f(-x).
\]

Consequently its two logarithmic lifts satisfy

\[
K_+^2=I,
\qquad
K_-^2=-I.
\]

Thus the even lift is a self-adjoint involution with possible phases
(1,-1\), while the odd lift is a skew-adjoint complex structure with possible
phases (i,-i\). The quarter-phase exists natively, but only in the additive
odd port. It cannot be inferred from oddness under reciprocal reflection.

The complete archimedean transport is therefore the parity double

\[
K_{\mathrm{full}}=K_+\oplus K_-.
\]

Its square is the grading operator

\[
K_{\mathrm{full}}^2=I\oplus(-I).
\]

## Separation and orientation use different witnesses

The logarithmic Hermite state (q e^{-\pi q^2}\) points the Mellin endpoint,
but it does not choose additive parity and is not an eigenstate of (K_+\).

Conversely, the additive Gaussian derivative

\[
x e^{-\pi x^2}
\]

is an authentic odd Tate state with Fourier phase (-i\), but its logarithmic
profile is proportional to

\[
e^{3q/2}e^{-\pi e^{2q}},
\]

not the endpoint-pointing logarithmic Hermite state. The two capabilities
exist, but they occupy different source ports.

## Consequence for the programme

The prior attempt tried to make one witness do two jobs. The corrected carrier
has at least two archimedean channels:

1. a logarithmic derivative port that points the Mellin endpoint;
2. an additive odd-parity port that carries the Fourier quarter-phase.

The missing theorem is a source-derived incidence between these ports and the
prime seam current. Without that incidence, their coexistence does not orient
the scalar theta readout. The standard even Gaussian theta vacuum occupies
the (K_+\) channel; importing the odd channel after scalarization would be an
unauthorized repair.

## Falsifier

Any proposed single-port construction must reproduce both squared laws. It
fails if it identifies reciprocal oddness with additive odd parity, or if it
obtains the phase (-i\) while remaining entirely inside the even theta vacuum.
