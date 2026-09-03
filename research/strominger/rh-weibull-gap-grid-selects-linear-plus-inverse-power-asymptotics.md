# The unnormalized determinant grid contains a removable linear term

## Question

Which finite asymptotic model best predicts held-out hard-edge gap determinants?

Using \(n=3,\ldots,9\) for training and \(n=10,11,12\) for holdout, compare models for

\[
L_n=\log(D_n^{\geq X}/D_n).
\]

The holdout errors are

\[
\begin{array}{c|c}
\text{model}&\text{error}\\
\alpha n+\beta&6.80\times10^{-3}\\
\alpha n+\beta+\gamma/n&6.47\times10^{-5}\\
\alpha n+\beta+\gamma/n+\delta/n^2&4.77\times10^{-6}\\
\alpha n+\beta+c\log n+\gamma/n&2.65\times10^{-5}.
\end{array}
\]

The inverse-square model predicts best. Its fitted \(\gamma=0.0912\) remains consistent with the direct determinant and recurrence proxies. A subsequent normalization audit identifies the fitted linear coefficient as exactly the omitted factor \(2X^{1/4}\) per moment. It is not a physical gap rate.

## Disposition

Complete finite model discrimination after restoring normalization. The corrected gap logarithm favors

\[
L_n^{\rm gap}=\beta_X+\gamma_X/n+\delta_X/n^2+\cdots
\]

over an added logarithmic term. The apparent \(\alpha_Xn\) term is removed.

The next leaf is `weibull-gap-linear-rate`: derive the leading gap rate \(\alpha_X\), then seek the inverse-power corrections through a source asymptotic.

## Claim boundary

Three held-out degrees do not prove the expansion or exclude later logarithmic terms.
