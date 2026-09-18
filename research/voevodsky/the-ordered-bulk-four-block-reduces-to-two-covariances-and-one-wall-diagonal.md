# The ordered bulk four-block reduces to two covariances and one wall diagonal

> **Retracted:** this packet used a linear reflection law on an antiunitary oriented channel. See `correction-antiunitary-reflection-leaves-two-prime-cell-defect-coordinates.md`. The correct defect space has two real coordinates, requiring both even-wall and oriented-linking comparisons.

## Fresh-state refinement

The ordered bulk residual is not four unrelated scalar integrals. On the local even/odd prime-cell frame, the completed theta columns fix

\[
Q=\begin{pmatrix}1/2&1/4\\1/2&-1/4\end{pmatrix},
\qquad \det Q=-1/4.
\]

The induced quarter turn and reflection are

\[
F=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\qquad
P=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

with \(F^2=-I\), \(P^2=I\), and \(PF=-FP\).

## Rigidity of the defect

Let

\[
\Delta=G_{\rm source}-Q^*G_{\rm arith}Q
=\begin{pmatrix}a&x+iy\\x-iy&d\end{pmatrix}.
\]

Common quarter-turn covariance

\[
F^*\Delta F=\Delta
\]

forces

\[
a=4d,\qquad x=0.
\]

Common reflection covariance

\[
P^*\Delta P=\Delta
\]

then forces \(y=0\). Therefore

\[
\Delta=a\begin{pmatrix}1&0\\0&1/4\end{pmatrix}.
\]

One independently sourced even-wall diagonal equality gives \(a=0\), hence the entire ordered four-block vanishes.

Thus the local bulk theorem reduces exactly to three source predicates:

1. common \(C_4\) covariance;
2. common reflection covariance;
3. one even-wall diagonal normalization.

No further finite matrix tomography is necessary once these symmetries are established on the same form domain.

## Radical correction

The local resolved response graph already retains the all-seam source coordinate and has a continuous left inverse. Its positive graph form contains the faithful source term \(\|\pi_Bx\|^2\), so its radical is zero. Consequently local radical descent is closed on the complete response essential image.

This does not prove radical compatibility after the global arithmetic pushout, theta-label completion, connected-grade assembly, or codiagonal observation.

## Remaining constructor

The unresolved map is the completed comparison

\[
Q_p=R_{\rm comp}Q_p^{\rm pre},
\]

where \(Q_p^{\rm pre}\) already preserves the rapid-core differential, labels, endpoint order, finite jets, and polarized Stokes boundary. The missing `R_comp` must carry wall extraction, Wronskian traces, causal/anti-causal resolution, tail/PV propagation, and the global quotient while proving the three predicates above.

## Corrected coordinates

Separate local and global radical claims and replace the generic four-block gate by its rigidity predicates:

\[
(b_{C4},b_P,b_{\rm wall},b_{\rm ord},b_{\rm rad,loc},b_{\rm rad,glob})
=(0,0,0,\bot,1,0).
\]

Here \(b_{\rm ord}=\bot\) means the full equality is not independently testable until the covariance and normalization inputs are supplied; exact algebra proves it automatically once all three equal one.

## Verification

Fresh execution of

`research/voevodsky/checkers/check_prime_cell_c4_reflection_rigidity.py`

passes every exact symbolic identity and writes

`research/voevodsky/results/prime-cell-c4-reflection-rigidity.json`.

## Claim boundary

This is a reduction theorem and a local radical closure, not a construction of `R_comp`, a global arithmetic comparison, or an RH result.
