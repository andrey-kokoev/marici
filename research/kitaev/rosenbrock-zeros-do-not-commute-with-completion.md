# Rosenbrock zeros do not automatically commute with completion

## Bounded question

What does Grothendieck's finite terminal pencil prove, and which additional
uniform data are required before its scalar transfer zeros can be interpreted
as zeros of a completed state-space realization?

## Frozen finite system

For a finite state space, use

\[
\dot x=Ax+Bu,\qquad y=Cx,
\]

with zero feedthrough. Its transfer and Rosenbrock pencil are

\[
F(s)=C(sI-A)^{-1}B,
\qquad
\mathcal R(s)=
\begin{pmatrix}
sI-A&-B\\
C&0
\end{pmatrix}.
\]

Grothendieck's terminal operator is the unbounded finite-interval analogue:
the transport block is bijective on its declared terminal Sobolev domain and
the scalar truncated transform is its exact Schur complement.

## Five distinct notions

1. A transfer zero is a point \(s\notin\operatorname{spec}(A)\) where
   \(F(s)=0\). It is a statement about the input-output rational function.
2. An invariant zero is a point where \(\mathcal R(s)\) loses normal rank.
   It is presentation-aware and remains meaningful at state eigenvalues.
3. An unobservable mode has \(Av=\lambda v\), \(Cv=0\), \(v\ne0\).
   Equivalently the PBH matrix \(\binom{\lambda I-A}{C}\) loses column rank.
4. An uncontrollable mode has a nonzero left eigenvector \(w^*A=\lambda w^*\)
   with \(w^*B=0\). Equivalently \((\lambda I-A\;B)\) loses row rank.
5. Invariant zero dynamics are nonzero pairs \((v,u)\) satisfying

   \[
   (sI-A)v-Bu=0,\qquad Cv=0.
   \]

   They are kernel states of the full pencil, not merely zeros of a scalar
   expression.

For a minimal finite SISO realization and \(s\notin\operatorname{spec}(A)\),
transfer zero and invariant zero coincide by Schur complement. Outside those
hypotheses they must not be identified.

## Hidden-state hostile pair

The one-state realization

\[
A=(0),\quad B=(1),\quad C=(1)
\]

and the two-state realization

\[
A=\operatorname{diag}(0,2),\quad B=(1,0)^{\mathsf T},
\quad C=(1,0)
\]

have the same scalar transfer \(1/s\). The latter contains a mode at \(2\)
that is both uncontrollable and unobservable. Thus scalar transfer data do not
reconstruct the state object, its dimension, or its hidden invariant modes.

## Pointwise minimality can collapse

Let \(\varepsilon_N=1/N\) and

\[
A_N=\operatorname{diag}(0,1),\quad
B_N=(1,\varepsilon_N)^{\mathsf T},\quad
C_N=(1,\varepsilon_N).
\]

For every finite \(N\), the controllability and observability matrices both
have determinant \(\varepsilon_N\), so the realization is minimal. Yet their
action on the second mode has squared norm \(2\varepsilon_N^2\), which tends
to zero. Moreover

\[
F_N(s)=\frac1s+\frac{\varepsilon_N^2}{s-1}
\longrightarrow\frac1s
\]

away from \(0,1\). The limit realization has a hidden mode at \(1\). Every
finite PBH test passes while no cutoff-independent observability or
controllability lower bound survives.

The finite zero

\[
s_N=\frac{1}{1+\varepsilon_N^2}
\]

approaches the state pole at \(1\) and disappears into pole-zero cancellation
in the reduced limit transfer. This is a concrete zero lost under a
non-uniform realization limit.

## Pointwise nonvanishing can also fail in the limit

There are minimal strictly proper two-state realizations with

\[
F_N(s)=\frac{s+1/N}{(s+1)(s+2)}.
\]

No finite member vanishes at \(s=0\), while the limit does. Its zeros
\(-1/N\) approach zero, as required by locally uniform analytic convergence.
Hence pointwise nonvanishing at one fixed point is not a completion-stable
property.

Conversely,

\[
G_N(s)=\frac{s}{(s+1/N)(s+1)}
\]

has a zero at zero for every \(N\), but converges on the punctured domain to
\(1/(s+1)\), whose analytic extension is nonzero at zero. A pole enters the
point, so convergence is not locally uniform on any neighborhood of zero.

The analytic guardrail is therefore precise: locally uniform convergence of
nonzero analytic functions controls interior zeros through the usual zero
continuity principle. Scalar pointwise convergence does not.

## Cutoff composition versus uniform completion

Grothendieck's terminal-zero domains do not nest. Retaining terminal amplitude
\(\beta_b=G(b)\) enlarges the cutoff state so restriction is the shear

\[
S_{a,b}=
\begin{pmatrix}
1&F_{a,b}\\
0&1
\end{pmatrix},
\qquad
S_{a,b}S_{b,c}=S_{a,c}.
\]

This is the minimal algebraic state channel making cutoff composition exact.
It repairs functoriality of the finite domains. It does not supply uniform
graph norms, reachability, observability, or bounded inverse control. The
known factor \(e^{2|\delta|L}\) remains an analytic completion falsifier.

## Required completion certificate

A completion-stable realization requires more than pointwise finite
minimality:

- typed cutoff maps intertwining \(A_N,B_N,C_N\) and the terminal-amplitude
  shear;
- one source-authorized graph topology on states and boundary channels;
- cutoff-independent lower bounds for the reachable and observable sectors,
  or an equivalent uniform PBH/Gramian certificate;
- locally uniform transfer convergence on the claimed zero domain, with pole
  control;
- convergence of Rosenbrock graphs strong enough that kernel appearance or
  disappearance is explicitly tracked.

Minimality does not imply passivity, conservativity, KYP positivity, or an RH
orientation. None is assumed here.

## Exact audit and falsifiers

The checker verifies a minimal transfer/invariant zero and its zero-dynamics
kernel, the identical-transfer hidden-state pair, the rational collapse family,
both zero-creation/loss families, and the terminal shear cocycle. All arithmetic
is exact.

The completed claim is falsified by any normalized sequence whose reachable
or observable output tends to zero, any cutoff map that omits terminal
amplitude, any pole entering the asserted analytic domain, or any limiting
Rosenbrock kernel not represented by compatible finite graph states.

## Claim boundary

This is a finite algebraic taxonomy plus exact hostile families. It types
Grothendieck's finite pencil as a legitimate zero-to-state constructor and
shows why scalar convergence and finite minimality do not prove completion
stability. It does not construct the adelic completion, prove uniform graph
control, passivity, conservativity, KYP positivity, or RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The alternatives were scalar control of completed zero dynamics versus
loss of hidden state geometry and uniform conditioning. Exact ranks, kernels,
determinants, transfer identities, and limits were frozen as measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Scalar sufficiency was eliminated by three independent hostile
mechanisms. Terminal amplitude repaired algebraic composition but left the
uniform analytic gate untouched. The missing completion certificate is now a
finite list of typed bounds rather than an undifferentiated continuity claim.
