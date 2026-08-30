# The Remaining Boundary Block Is Controlled by a Sharp Decay-Elasticity Threshold

Grothendieck's centered conditional-band coordinate is globally oriented by

\[
C_a(D)=\int \cosh(2ay)\,\Delta_D(y)\,dy,
\qquad
\Delta_D(y)\ge0.
\]

The remaining scalar obstruction has the form

\[
B_L(D)=D\,W(D)-(D+L)W(D+L),
\qquad D,L>0,
\]

for a positive weight \(W\). Positivity and decay of \(W\) are not enough.
The exact issue is whether \(W\) decays faster than the reciprocal geometric
factor introduced by \(D\).

Define

\[
h(D)=D\,W(D).
\]

Then

\[
B_L(D)>0
\quad\Longleftrightarrow\quad
h(D)>h(D+L).
\]

Equivalently,

\[
\frac{W(D+L)}{W(D)}<\frac{D}{D+L}.
\]

## Exact finite-interval criterion

Assume \(W\) is positive and differentiable. Put

\[
q(D)=-\partial_D\log W(D).
\]

Taking logarithms gives

\[
B_L(D)>0
\]

if and only if

\[
\int_D^{D+L}q(u)\,du
>
\log\left(1+\frac LD\right).
\]

Thus the average logarithmic decay rate must beat the exact geometric
threshold

\[
\frac1L\log\left(1+\frac LD\right).
\]

## Infinitesimal criterion

Define the dimensionless decay elasticity

\[
\varepsilon(D)
=-D\,\partial_D\log W(D)
=Dq(D).
\]

Since

\[
\frac{h'(D)}{h(D)}
=\frac{1-\varepsilon(D)}{D},
\]

the infinitesimal block orientation is

\[
h'(D)<0
\quad\Longleftrightarrow\quad
\varepsilon(D)>1.
\]

The number one is the sharp threshold. Ordinary decay gives only
\(\varepsilon>0\).

## Uniform sufficient margin

If a source theorem proves

\[
\varepsilon(u)\ge1+\eta
\]

throughout \([D,D+L]\), for some cutoff-independent \(\eta>0\), then

\[
\frac{h(D+L)}{h(D)}
\le
\left(\frac{D}{D+L}\right)^\eta
\]

and hence

\[
B_L(D)
\ge
h(D)
\left[
1-left(\frac{D}{D+L}\right)^\eta
\right]>0.
\]

This is the completion-ready certificate: it controls sign and supplies an
explicit modulus.

## Hostile families

For exponential decay

\[
W(D)=e^{-\alpha D},
\]

one has

\[
\varepsilon(D)=\alpha D.
\]

The block is locally misoriented for \(D<1/\alpha\), despite strict positivity,
smoothness, and exponential decay.

For power decay

\[
W(D)=D^{-p},
\]

one has \(\varepsilon=p\). Therefore

\[
B_L(D)
\begin{cases}
>0,&p>1,\\
=0,&p=1,\\
<0,&0<p<1.
\end{cases}
\]

This makes the threshold exact and scale-free.

## Source-authority boundary

This compiler theorem does not identify Grothendieck's \(W(D)\). The theta
source must derive its exact weight, domain, cutoff dependence, and
normalization. Once supplied, the decisive audit is no longer generic
log-concavity but

\[
-D\,\partial_D\log W(D)>1
\]

or its exact finite-interval integral form.

## Falsifiers

- A point with \(\varepsilon(D)<1\) in an infinitesimal required block.
- A finite interval whose integrated log-decay does not beat
  \(\log(1+L/D)\).
- Strict decay of \(W\) without decay of \(D W(D)\).
- Cutoffwise positivity with \(\eta_X\to0\).
- Using the globally oriented \(C_a(D)\) coordinate to infer the independent
  sign of \(B_L(D)\).
- Selecting a favorable normalization of \(W\) not supplied by the source.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to convert the last named block obstruction into a sharp,
source-checkable inequality.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The obstruction is exactly a unit decay-elasticity threshold, with an
explicit uniform completion modulus.
