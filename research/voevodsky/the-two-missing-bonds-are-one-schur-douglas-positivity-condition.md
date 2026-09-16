# The two missing bonds are one Schur--Douglas positivity condition

## Combined positive horn

After diagonalizing the completed endpoint swap form, retain its odd line as the
single negative coordinate. Let

\[
C_{\alpha,k}\succeq0
\]

be the candidate common physical bulk remainder on the observer source, and let

\[
b_{\alpha,k}:\mathbb C_{odd}\longrightarrow
\overline{\operatorname{ran}C_{\alpha,k}^{1/2}}
\]

be the mixed Sonin-bulk/odd-endpoint Green coupling. The combined \(H_{234}\)--\(H_{134}\) lift is controlled by the block

\[
\mathcal K_{\alpha,k}
=
\begin{pmatrix}
C_{\alpha,k}&b_{\alpha,k}\\
b_{\alpha,k}^*&1
\end{pmatrix}.
\]

The sign convention places the original negative endpoint square on the other
side of the Green identity; cancellation asks for positivity of this completed
block.

## Schur complement

Since the lower-right block is the identity,

\[
\mathcal K_{\alpha,k}\succeq0
\quad\Longleftrightarrow\quad
C_{\alpha,k}-b_{\alpha,k}b_{\alpha,k}^*\succeq0.
\]

Indeed,

\[
\begin{pmatrix}I&-b_{\alpha,k}\\0&I\end{pmatrix}
\mathcal K_{\alpha,k}
\begin{pmatrix}I&0\\-b_{\alpha,k}^*&I\end{pmatrix}
=
\begin{pmatrix}
C_{\alpha,k}-b_{\alpha,k}b_{\alpha,k}^*&0\\
0&1
\end{pmatrix}.
\]

Thus cancellation of the odd endpoint direction is exactly one positive
remainder inequality.

## Douglas form

Douglas factorization gives the equivalent statement

\[
b_{\alpha,k}=C_{\alpha,k}^{1/2}c_{\alpha,k}
\]

for a contraction

\[
\|c_{\alpha,k}\|\le1.
\]

Therefore the completed horn has a positive lift precisely when the mixed Green
coupling factors contractively through the square root of the physical common
bulk.

## Identification with the A--T remainder

The \(H_{234}\) positive lift requires

\[
C_{\alpha,k}
=
G_{\mathrm{phys},\alpha,k}^T-(D_{\alpha,k})_+
=
G_{\mathrm{phys},\alpha,k}^0-(D_{\alpha,k})_-.
\]

The \(H_{134}\) positive lift requires the odd endpoint functional to be the
boundary trace of the Sonin Green form. Under that identification its Riesz map
is exactly \(b_{\alpha,k}\).

Consequently the two formerly separate requirements become

\[
\boxed{
G_{\mathrm{phys},\alpha,k}^T-(D_{\alpha,k})_+
=
G_{\mathrm{phys},\alpha,k}^0-(D_{\alpha,k})_-
=:C_{\alpha,k}
\succeq
b_{\alpha,k}b_{\alpha,k}^*.}
\]

The equality identifies the common Widom bulk; the inequality absorbs the one
negative endpoint parity. They are the equality and positivity parts of one
block-kernel theorem.

## k-axis coherence

Let \(S_k\) be the source successor and \(T_k\) the induced bulk successor.
Naturality of the combined positive lift is the pair

\[
T_kC_{\alpha,k}^{1/2}
=C_{\alpha,k+1}^{1/2}S_k,
\]

\[
T_kb_{\alpha,k}=b_{\alpha,k+1}.
\]

Equivalently, for the Douglas contraction,

\[
\boxed{T_kc_{\alpha,k}=c_{\alpha,k+1}.}
\]

Thus one contraction, transported along the \(k\)-axis, fills both bonds at
every stage.

## Exact remaining analytic statement

The construction has reduced the desired theorem to a source-derived estimate:
for every observer \(u\),

\[
\boxed{
\|b_{\alpha,k}^*u\|^2
\le
\langle u,C_{\alpha,k}u\rangle.}
\]

This is the contractive endpoint estimate anticipated by the generalized
Nevanlinna \(N_1\to N_0\) formulation. It is simultaneously:

- positivity of the completed Schur block;
- existence of the Douglas contraction;
- cancellation of odd endpoint parity;
- positivity of the combined Morse/conductor horn.

No independent proof of two unrelated bonds is required.

## Claim boundary

This note proves the equivalence of the two lifting problems once the physical
common bulk and boundary Riesz map are identified. The displayed norm estimate
is now the single analytic inequality to prove; it is not asserted here as an
existing repository theorem.
