# Dynamic-storage residual is a transported cohomology class

## Bounded question

When can a discrepancy between observed path energy and source-derived boundary
supply be removed by changing endpoint storage?

## Typed residual

Let \(W_{a,b}\) be the positive observation Gramian, \(B_{a,b}\) the
independently derived boundary-supply form, and \(S_{a,b}\) the state
transport. Define

\[
C_{a,b}=W_{a,b}-B_{a,b}.
\]

A choice of endpoint storage \(P_a\) closes the dynamic balance exactly when

\[
C_{a,b}=P_a-S_{a,b}^*P_bS_{a,b}.
\]

Equivalently, the typed residual

\[
\Delta_{a,b}
=W_{a,b}+S_{a,b}^*P_bS_{a,b}-P_a-B_{a,b}
\]

vanishes. Storage is gauge data; the invariant question is whether the
transported cocycle \(C\) is a coboundary.

## Cocycle law

If both \(W\) and \(B\) compose on the same carriers by

\[
X_{a,c}=X_{a,b}+S_{a,b}^*X_{b,c}S_{a,b},
\]

then so do \(C\) and \(\Delta\):

\[
\Delta_{a,c}
=\Delta_{a,b}+S_{a,b}^*\Delta_{b,c}S_{a,b}.
\]

A single nonzero local residual therefore propagates by an invertible
congruence unless another typed residual cancels it. Scalar cancellation is
not matrix closure.

## Closed-loop obstruction

For a loop based at \(a\), write its total transport as \(S\). The storage
equation becomes

\[
C_{\mathrm{loop}}=L_S(P),
\qquad
L_S(P)=P-S^*PS.
\]

The obstruction is the class of \(C_{\mathrm{loop}}\) in

\[
\operatorname{coker}L_S.
\]

Under the trace pairing, dual obstruction witnesses satisfy

\[
K-SKS^*=0.
\]

If \(\operatorname{Tr}(KC_{\mathrm{loop}})\ne0\) for such a \(K\), no
storage gauge closes the loop. For identity holonomy, \(L_I=0\), so every
nonzero \(C_{\mathrm{loop}}\) is an absolute obstruction.

## Exact cokernel for the unit shear

For

\[
S=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

and Hermitian coordinates

\[
P=\begin{pmatrix}a&u+iv\\u-iv&d\end{pmatrix},
\]

one obtains

\[
L_S(P)=
\begin{pmatrix}
0&-a\\
-a&-a-2u
\end{pmatrix}.
\]

The real-linear map has rank two on the four-dimensional Hermitian space. Its
cokernel is two-dimensional: a removable loop form must have zero upper-left
entry and real off-diagonal entry. Dual witnesses may be chosen as

\[
K_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
K_2=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
\]

They detect the upper-left and imaginary off-diagonal obstruction coordinates.

## Four hostile fixtures

### Scalar projection hides a matrix residual

The nonzero residual

\[
\Delta=\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]

has \(e_1^*\Delta e_1=0\). A selected scalar readout can vanish while the
typed matrix identity fails.

### Mismatched carriers

If \(W\) acts on a two-coordinate tail state while \(B\) acts on a
three-coordinate tail-plus-seam state, \(W-B\) is undefined until a canonical
comparison map is supplied. Padding, projecting, or identifying coordinates by
name is not storage gauge.

### Cutoffwise gauges without one topology

Let \(S_N=S(1/N)\) and

\[
C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Every cutoff equation \(C=L_{S_N}(P_N)\) is solvable, for example with

\[
P_N=\begin{pmatrix}-N&1/2\\1/2&0\end{pmatrix}.
\]

The off-diagonal equation forces the upper-left storage coordinate to be
\(-N\), so every solution diverges in the fixed coordinate norm. Cutoffwise
vanishing residual therefore does not define a coboundary in a common bounded
graph topology.

### One local residual becomes global

If \(\Delta_{a,b}=0\) and \(\Delta_{b,c}\ne0\), then

\[
\Delta_{a,c}=S_{a,b}^*\Delta_{b,c}S_{a,b}\ne0
\]

because \(S_{a,b}\) is invertible. Local failure cannot disappear merely by
composing more exact segments.

## Source-authority boundary

The compiler may test a frozen \(B_{a,b}\), but it may not synthesize
boundary supply from \(W\) or choose a projection that kills \(\Delta\).
Grothendieck must derive the tail, seam, primitive, square, and archimedean
supply rows and their common carrier maps. Only then is \([C]\) a typed
theta/Tate storage class.

## Exact audit and falsifiers

The checker verifies the residual cocycle on exact fixtures, computes the
unit-shear map rank and cokernel, evaluates both trace-pairing witnesses, and
requires all four hostiles to exhibit their predicted obstruction.

The balance is falsified by the first nonzero typed \(\Delta\). Storage-gauge
closure is falsified by a nonzero cokernel pairing. Completion closure is
falsified by any cutoff family whose necessary storage potentials have
unbounded graph norm.

## Claim boundary

This is a finite algebraic and pro-topological compiler theorem. It does not
derive theta boundary supply, establish a common theta graph topology, prove
uniform observability, identify physical energy flux, or prove RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The alternatives were universal storage-gauge removability and surviving
closed-loop cokernel classes. Cocycle, map rank, dual cokernel, four hostiles,
and gauge divergence were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Universal removability was eliminated. The discrepancy became a typed
transported cohomology class; the unit shear has a two-dimensional cokernel;
and cutoffwise exact gauges were separated from a common bounded storage
topology. Theta source supply remains unresolved.
