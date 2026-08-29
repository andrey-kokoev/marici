# Correction: the polarization test belongs to Fourier square, not Fourier

The previous note used the wall/tail characters as though they were eigenvalues of \(F\). They are eigenvalues of
\[
R=F^2,
\]
the source reflection:

\[
R|_{\mathcal W_{+}}=+I,
\qquad
R|_{\mathcal W_{-}}=-I.
\]

On the tail plane, \(F\) itself is a quarter-turn with \(F^2=-I\), not a minus involution. Therefore the proposed signed covariance must be tested for \(R\), not inferred directly for \(F\).

The correct criterion is
\[
R^{*}\Omega_{\mathcal W}R
=
-\Omega_{\mathcal W}.
\]

Now the isotropy argument is valid. For \(u,v\) in either one of the two \(R\)-eigenspaces,
\[
\omega_{\mathcal W}(Ru,Rv)=\omega_{\mathcal W}(u,v),
\]
because the two eigenvalue signs multiply to \(+1\). Anti-symplecticity simultaneously requires this to equal
\[
-\omega_{\mathcal W}(u,v).
\]
Hence
\[
\omega_{\mathcal W}|_{\mathcal W_{+}}=0,
\qquad
\omega_{\mathcal W}|_{\mathcal W_{-}}=0.
\]

For one wall vector and one tail vector, the eigenvalue product is \(-1\), so the anti-symplectic identity imposes no vanishing. Thus
\[
\Omega_{\mathcal W}
=
\begin{pmatrix}
0&J\\
-J^{*}&0
\end{pmatrix}
\]
still follows, but from reflection anti-symplecticity.

This correction also sharpens the source interpretation. Reflection reverses the orientation of a Green boundary, so anti-symplecticity of \(R\) is geometrically plausible:
\[
\text{orientation reversal}
\quad\Longrightarrow\quad
\text{Green boundary form changes sign}.
\]
Fourier \(F\), by contrast, may be symplectic, metaplectic, or carry a phase depending on the chosen realization. Its direct covariance is a separate theorem.

The finite audit is now:

1. prove \(R=F^2\) on the saturated coefficient quotient;
2. prove \(R\) exchanges the oriented history endpoints;
3. derive
   \[
   R^{*}\Omega_{\mathcal W}R=-\Omega_{\mathcal W}
   \]
   from the Green/Stokes identity;
4. compute the cross matrix \(J\);
5. verify \(\det J\neq0\);
6. only afterward determine the finer action of \(F\) on the resulting Darboux pair.

The full Fourier action should then constrain the cross block. Writing
\[
F=
\begin{pmatrix}
F_{+}&0\\
0&F_{-}
\end{pmatrix}
\]
relative to the \(R\)-character decomposition, with
\[
F_{+}^{2}=I,
\qquad
F_{-}^{2}=-I,
\]
any direct Fourier covariance becomes a relation among \(F_{+}\), \(F_{-}\), and \(J\). It does not create the polarization by itself.

The smallest hostile to the corrected theorem has reflection preserving rather than reversing the Green orientation:
\[
R^{*}\Omega_{\mathcal W}R=+\Omega_{\mathcal W}.
\]
Then the cross block \(J\) must vanish, while wall and tail planes may each carry internal symplectic forms. This is observationally distinct from the desired value/flux split.

Thus event 10183 retains the right target block form but attributed it to the wrong signed operator. The source-native polarization test is reflection anti-symplecticity.
