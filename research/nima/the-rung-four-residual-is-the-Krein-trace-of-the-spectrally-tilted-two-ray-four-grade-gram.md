# The rung-four residual is the Krein trace of the spectrally tilted two-ray four-grade Gram

## Untilted translated Gram

For the source-fixed translated rays, write

\[
G_p(L)=
\begin{pmatrix}
D_p(L)&C_p(L)\\
\overline{C_p(L)}&D_p(L)
\end{pmatrix}.
\]

The equality of the diagonal entries is the reciprocal equal-energy theorem.
The cross term contains the translated four-grade interference.

## Spectral valuation tilt

Let the local spectral transport act on the reciprocal rows by

\[
T_{p,z}=\operatorname{diag}(1,p^{-z}).
\]

The transported Gram is

\[
G_{p,z}=T_{p,z}^{*}G_pT_{p,z}
=
\begin{pmatrix}
D_p&p^{-z}C_p\\
p^{-\bar z}\overline{C_p}&p^{-2\operatorname{Re}z}D_p
\end{pmatrix}.
\]

With the reciprocal Krein orientation

\[
J=\operatorname{diag}(1,-1),
\]

its oriented metric trace is

\[
\operatorname{Tr}(JG_{p,z})
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)D_p(L).
\]

Identifying the retained local energy with the diagonal ray energy,

\[
E_p(b_z)=D_p(L)>0,
\]

gives exactly

\[
\boxed{
\mathcal R_p(b_z)=\operatorname{Tr}(JG_{p,z})
}.
\]

## Role of translated-history complexity

The off-diagonal translated-history coefficient `C_p` is essential for the
full Gram and for the symmetric/defect eigenmodes, but cancels from the Krein
trace. Hence:

- the four-grade packet supplies a positive, source-fixed diagonal energy;
- translated history supplies the forward/backward correlation;
- valuation transport supplies the transverse modulus;
- Krein orientation extracts the final rung-four residual.

The raw Plucker point alone cannot produce the residual because it lacks both
the Green metric and the spectral tilt.

## Determinant check

The transported determinant is

\[
\det G_{p,z}
=p^{-2\operatorname{Re}z}
\left(D_p(L)^2-|C_p(L)|^2\right).
\]

Thus spectral transport rescales Gram volume while the Krein trace measures
its reciprocal diagonal imbalance. These are distinct invariants; determinant
matching cannot replace rung-four closure.

## Closure statement

Since `D_p(L)>0`,

\[
\operatorname{Tr}(JG_{p,z})=0
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

This is an exact representation of the residual in the two-ray four-grade
carrier. It does not independently prove that the Krein trace vanishes. The
remaining filler must impose metric-balanced transport, rather than another
linear or Plucker relation.