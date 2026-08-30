# The wall--endpoint overlap block is already uniformly invertible

## Correction after source rehydration

The arithmetic-to-endpoint incidence is not missing. The source Stieltjes
construction already defines

\[
J_pe_1=W_{\log p},
\qquad
J_pe_2=W_{2\log p},
\]

and its Pauli-twirled observer has the prime-uniform bound

\[
2m_\nu^2I
\le
XJ_p^*J_pX+YJ_p^*J_pY
\le
2I.
\]

Accordingly, every statement below that calls \(J_p\) missing must be read more
narrowly: the unresolved datum is the intertwining of this established cyclic
Stieltjes incidence with the complete enlarged wall--history--tail/PV Green
block. The incidence itself and its cyclic lower bound are already proved.

## Source matrices

Two previously established source calculations determine the finite
wall--endpoint block.

The primewise endpoint observer is

\[
V_p
=
\frac12
\begin{pmatrix}
1&p^{-1}\\
p^{-1}&1
\end{pmatrix}.
\]

The normalized Hadamard frame separates wall and jump coordinates. In that
frame,

\[
H^*V_pH
=
\begin{pmatrix}
\frac12(1+p^{-1})&0\\
0&\frac12(1-p^{-1})
\end{pmatrix}.
\]

Thus this part of the overlap calculation contains no off-diagonal correction.

## Exact completion columns

The completed theta histories give the two source trace columns

\[
v_0=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix},
\qquad
v_1=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}.
\]

Their determinant is

\[
\det(v_0,v_1)=-\frac14.
\]

In wall--jump coordinates these become

\[
Hv_0=
\begin{pmatrix}
2^{-1/2}\\
0
\end{pmatrix},
\qquad
Hv_1=
\begin{pmatrix}
0\\
-(2\sqrt2)^{-1}
\end{pmatrix}.
\]

Therefore the completion wall and reciprocal jump are not merely linearly
independent. They are exactly orthogonal in the source frame.

## Uniform finite inverse

For every prime \(p\ge2\),

\[
\sigma_{\min}(V_p)
=
\frac12(1-p^{-1})
\ge
\frac14,
\]

and hence

\[
\|V_p^{-1}\|\le4.
\]

The completion column matrix has singular values

\[
\frac1{\sqrt2},
\qquad
\frac1{2\sqrt2},
\]

so its inverse norm is

\[
2\sqrt2.
\]

Consequently the pure wall--endpoint comparison has a cutoff-independent
inverse before any prime-history propagation is attached.

This closes the first finite overlap gate. There is no hidden wall--jump
cancellation inside the two-port observer.

## History lift normalization

For \(L=\log p\), affine interpolation gives a right inverse for the endpoint
trace with

\[
\|R_L\|^2
\le
\frac L2+\frac2L.
\]

The raw graph norm therefore grows as \(O(\sqrt{\log p})\). This is not a
failure of endpoint rank. It records the physical length of the comoving
history cell.

Define the normalized boundary-to-history coordinate

\[
\widetilde R_L
=
R_LD_L^{-1},
\]

where \(D_L\) is the source metric comparison between endpoint data and the
length-\(L\) graph energy. If the endpoint norm is the pullback graph norm,

\[
\|b\|_{\partial,L}
=
\|R_Lb\|_{\mathcal G_L},
\]

then \(\widetilde R_L\) is isometric by construction. But this normalization
is source-authorized only if the half-density trace theorem identifies that
pullback with the Mellin endpoint metric.

Thus the remaining growth question is a metric-comparison theorem, not a
surjectivity theorem.

## First nontrivial overlap block

Let

\[
J_p:
\mathcal P_{\sigma,p}\oplus\mathcal Q_p
\longrightarrow
\mathcal H\oplus\mathcal H
\]

be the missing arithmetic-to-endpoint incidence. The actual prime lift is

\[
R_{\mathrm{prime},p}=R_{\log p}J_p.
\]

After the wall--endpoint diagonalization, the first nontrivial joint overlap
operator is

\[
K_p^{\mathrm{wp}}
=
\Gamma_{\mathrm{wall}}
R_{\log p}J_p
\]

together with its reciprocal endpoint return.

Everything analytic outside \(J_p\) is now explicit:

- \(V_p\) is uniformly invertible;
- the Hadamard wall--jump transform is unitary;
- the theta completion columns have fixed nonzero determinant;
- \(R_{\log p}\) is an exact endpoint right inverse;
- its growth is only \(O(\sqrt{\log p})\).

Therefore the overlap spectrum cannot be computed until \(J_p\) is
source-derived. Any numerical matrix formed without it would invent the
arithmetic-to-analytic crossing.

## Available summability budget

The primitive-square coefficient product is

\[
\frac12p^{-3/2-\sigma}.
\]

Even two history lifts contribute only \(O(\log p)\), leaving the convergent
majorant

\[
\sum_p
\frac{\log p}{p^{3/2+\sigma}}.
\]

Hence diagonal completion remains safe through the seam. If twisted Mellin
equivariance makes \(J_p\) prime diagonal, no cross-prime overlap estimate is
needed.

The live issue is exact source incidence and metric authority, not analytic
summability.

## Hostiles

1. Use the exact endpoint inverse but attach an arbitrary \(J_p\).
2. Declare the pullback graph norm to be the source metric without proving the
   half-density comparison.
3. Collapse the two completion columns to their scalar sum and lose the jump.
4. Infer joint trace surjectivity from endpoint rank while ignoring the
   arithmetic crossing.
5. Retain primewise invertibility but allow \(J_p\) to mix coherent rows across
   all primes.

## Verdict

The wall--endpoint part of the finite overlap matrix is solved and uniformly
invertible. Its wall and jump channels are exactly diagonal in the source
Hadamard frame.

The earliest unresolved entry is now uniquely identified:

\[
J_p:
\text{primitive--square arithmetic packet}
\longrightarrow
\text{analytic endpoint pair}.
\]

Once \(J_p\) is derived, the finite wall--endpoint--prime overlap matrix is a
literal computation. Until then, no additional abstract boundary-triple
refinement can move the gate.
