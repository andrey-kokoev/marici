# Labelled prime transport forces infinite closure

Author: `marici.Nima`

## 1. Ownership and scope

Grothendieck owns the adelic construction and the proposed archimedean
counterterm.  This packet audits only transport closure, leakage, and the
smallest finite falsifier.  It does not alter his construction.

The scalar identity

\[
Q_{\rm end}+Q_\Gamma+Q_{\rm prime}=Q_{\Xi}
\]

is taken as established provenance, not as a positivity theorem.  Endpoint,
gamma, and prime-power terms remain one coupled boundary system.

## 2. Labelled probe module

Let

\[
\mathcal L=\ell^2(\mathbb Q_{>0})
\]

with orthonormal source labels \(e_r\).  For each prime \(p\), define

\[
S_p e_r=e_{pr},\qquad J e_r=e_{1/r}.
\]

Thus \(S_p\) records multiplication by a prime and \(J\) is reciprocal
reflection.  The labels are retained before scalar readout.  In particular
\(e_6=S_2S_3e_1=S_3S_2e_1\) is a **path state**.  It is not a connected
boundary atom: \(\Lambda(6)=0\).

For a finite prime-power cutoff \(\mathcal N_Y\), the coupled quadratic
form must have the shape

\[
Q_Y(f)=
\sum_{N\in\mathcal N_Y}a_N\|(I-S_N)f\|^2+
\langle f,C_Yf\rangle,
\qquad
a_N=\frac{\Lambda(N)}{\sqrt N},
\]

where the one shared vertex counterterm is

\[
C_Y=Q_{\rm end+\Gamma}^{(Y)}-2A_YI,
\qquad
A_Y=\sum_{N\in\mathcal N_Y}a_N.
\]

This is the exact coherence relation required to join endpoint, gamma, and
prime flux.  Neither \(Q_{\rm end+\Gamma}^{(Y)}\) nor the degree subtraction
is an independently positive port.

## 3. Leakage of the two-dimensional seed

Take the smallest prime-two seed

\[
V_0=\operatorname{span}\{e_1,e_2\},\qquad P_0:\mathcal L\to V_0.
\]

Its one-step leakage operator is

\[
L_2=(I-P_0)S_2P_0.
\]

Since

\[
L_2e_1=0,\qquad L_2e_2=e_4,
\]

we have

\[
\boxed{L_2^*L_2=
\begin{pmatrix}0&0\\0&1\end{pmatrix},
\quad \det(I+L_2^*L_2)=2.}
\]

This source-local \(2\times2\) matrix is the finite falsifier.  Any claim
that the current two-vector Gram/Pick block is closed under multiplication by
one prime predicts \(L_2=0\), contradicted by its lower-right entry.

Adding \(e_4\) repairs only one step.  Repeated prime-two transport forces
\(e_{2^k}\) for every \(k\ge0\).  Reciprocal reflection forces
\(e_{2^{-k}}\) as well.  Hence the smallest \(S_2,J\)-stable extension is

\[
\overline{\operatorname{span}}\{e_{2^k}:k\in\mathbb Z\},
\]

which is infinite-dimensional.

## 4. Mixed-prime square and typing

With primes two and three, the first commuting square is

\[
e_1\xrightarrow{S_2}e_2,\qquad
e_1\xrightarrow{S_3}e_3,\qquad
S_3e_2=S_2e_3=e_6.
\]

The square closes only after adding the typed path state \(e_6\).  Giving
that state connected scalar weight would manufacture a forbidden squarefree
von Mangoldt atom.  Omitting it before transport closure leaves a norm-one
square leakage.  Therefore the correct order is

\[
\text{labelled path closure}\longrightarrow
\text{connected/prime-power typing}\longrightarrow
\text{scalar projection}.
\]

Closure under all primes, prime powers, and reflection contains
\(e_r\) for every positive rational \(r\); it is necessarily infinite.

## 5. Endpoint--gamma gate

The divergent quantity \(A_Y\) shows why the channels cannot be split.
The only potentially noncircular positivity law is a source-derived limit

\[
C_Y\longrightarrow C_{\rm ren}
\]

on a common form domain, with

\[
Q(f)=\sum_N a_N\|(I-S_N)f\|^2+
\langle f,C_{\rm ren}f\rangle\ge0
\]

proved before scalar projection.  At present no independent proof that
\(C_{\rm ren}\ge0\), or that the full coupled form is monotone in \(Y\),
is available.  Asserting the sign of the resulting Schur complement is
exactly the RH-equivalent Weil/Pick positivity already known.

## 6. Hostile-source test

Reciprocal symmetry and the scalar functional equation constrain paired
boundary data but do not fix the local edge weights.  A finite signed
perturbation \(a_2\mapsto a_2+\varepsilon\), accompanied by its reciprocal
boundary partner and the compensating diagonal change
\(-2\varepsilon I\), preserves the same reflection bookkeeping and scalar
completion pattern.  For \(\varepsilon<-a_2\), however, the coefficient of
\(\|(I-S_2)f\|^2\) is negative.  Thus archimedean symmetry plus a scalar
functional equation does not force the transport orientation.

This is a hostile source model, not a deformation of the Riemann primes.  Its
role is to falsify any proposed law derived only from symmetry, scalar
completion, or separate edge factorization.

## 7. Decisive outcome

\[
\boxed{\textbf{Forced infinite closure.}}
\]

The current \(2\times2\) block is a finite observation window, not an
explanatory carrier.  The labelled transport prevents forbidden fill-in and
identifies the exact shared counterterm, but it supplies no new orientation
law by itself.  Until the endpoint--gamma counterterm is independently
positive or monotone on the completed labelled module, scalar compression
returns precisely the RH-equivalent Weil kernel.

No division by \(\Xi\), zero-location input, assumed Herglotz positivity,
or separate channel positivity is used.
