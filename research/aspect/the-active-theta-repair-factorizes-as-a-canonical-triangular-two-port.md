# The active theta repair admits a triangular two-port normal form

## Exact factorization

The minimal active update does more than restore feasibility. It collapses the repaired balance to an explicit two-port circuit.

Since

\[
\rho=\frac{f^2}{1-4r^2},
\]

the optimal update becomes

\[
\Delta_*
=\frac{\rho-1}{\rho}bb^*
=\begin{pmatrix}f^2+4r^2-1&0\\0&0\end{pmatrix}.
\]

Therefore

\[
Q_*=Q+\Delta_*
=\begin{pmatrix}f^2+4r^2&2r\\2r&1\end{pmatrix}.
\]

Its determinant is not merely positive:

\[
\det Q_*=f^2.
\]

The source forcing becomes exactly the positive response-volume density.

Choose an output frame in which

\[
C_*=\begin{pmatrix}f&0\\2r&1\end{pmatrix},
\qquad
D_*=\begin{pmatrix}1\\0\end{pmatrix}.
\]

Then all positive lossless identities hold exactly:

\[
C_*^*C_*=Q_*,
\qquad
-C_*^*D_*=b,
\qquad
D_*^*D_*=1.
\]

Thus the active repair terminates in two outputs and admits a triangular normal form. In that frame, the first response port carries the source amplitude \(f\); the second carries the reciprocal mixing \(2r\) and a unit reference.

## Output-frame gauge

The source identities do not select this output frame. For every two-by-two unitary matrix \(U\),

\[
C_U=UC_*,
\qquad
D_U=UD_*
\]

obey the same three lossless identities. Conversely, because \(Q_*\) is positive definite and a minimal two-output factor \(C\) is invertible, any two minimal factors of the same Gramian differ by a left-unitary transformation. The invariant object is the unitary equivalence class of \((C,D)\), not the displayed triangular matrix by itself.

The triangular representative becomes canonical only after a physical output frame is independently supplied, such as labelled response characters plus a phase convention fixing positive diagonal entries. Without that augmentation, statements about which detector carries \(f\) are coordinate descriptions. The invariant statements are the Gramian, its determinant, and source duality.

## Optical reading

In the selected normal frame, the circuit is triangular:

```text
theta source f  ──► response 1
                         │
horizontal mix 2r ──────┤
unit reference ─────────► response 2
```

Three quantities are independently measurable:

1. the first diagonal response equals \(f\);
2. the cross response equals \(2r\);
3. the second diagonal response equals one in the normalized frame.

Their Gram determinant must equal \(f^2\). This is a stronger falsifier than checking losslessness alone: it ties the active response volume directly to the source forcing.

At \(r=0\), the circuit diagonalizes to \(C_*=\operatorname{diag}(f,1)\). At the overdrive witness \(f=\sqrt2\), the two amplitudes are \(\sqrt2\) and one, reproducing the repaired decay matrix \(\operatorname{diag}(2,1)\).

## Architectural implication

The repaired apparatus is not “two original outputs plus a reservoir port.” It is a new two-output colligation whose generator balance has already absorbed one active source-aligned mode. Port count returns to two after the source incidence is repaired upstream.

This realizes Nima's downstream no-go constructively: the missing information is restored before observation, so no downstream rank inflation is needed. It also locates Strominger's variable relative control: the fixed spin connection can provide attachment, but the globally defined variable one-form must induce the source-aligned diagonal increment while leaving the topological degree unchanged.

## Next experimental test

Sweep \(y\), hence \(f(y)=2e^{-\pi y}\), at fixed \(r\). Fit the full two-by-two response Gramian. In an independently calibrated frame matching the triangular normalization, the active completion predicts simultaneously

\[
Q_{*,22}=1,
\qquad
Q_{*,12}=2r,
\qquad
\det Q_*=4e^{-2\pi y}.
\]

Failure of the invariant determinant equality rejects the active completion. The entrywise equalities additionally test the declared output-frame calibration. Agreement converts the former forcing coefficient into a directly reconstructed response-volume invariant.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_canonical_active_theta_two_port.py
```
