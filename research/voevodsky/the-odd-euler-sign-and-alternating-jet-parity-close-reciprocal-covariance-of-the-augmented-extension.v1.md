# The odd Euler sign and alternating jet parity close reciprocal covariance of the augmented extension

## Question

Which Euler-coordinate sign makes the reciprocal augmented extension compatible with the sign-free exchange of Euler chart multipliers, the odd jet shift, and the even endpoint evaluation?

## Claim boundary

Let \(P_J(a_0,a_1,\ldots)=(a_0,-a_1,a_2,-a_3,\ldots)\). Then \(P_JSP_J=-S\) and \(\pi_0P_J=\pi_0\).

Use the positive extension \(A_{p,+}(z)=\begin{pmatrix}\lambda_{p,+}(z)&-\pi_0\\0&S\end{pmatrix}\), where \(\lambda_{p,+}(z)=1-p^{-1}e^{-2z\log p}\).

Define the reciprocal transport from the positive extension carrier to the negative extension carrier by \(C_J(q,a)=(-q,P_Ja)\). This choice makes the Euler coordinate reciprocal-odd and preserves the source-derived jet parity.

Define the negative extension by \(A_{p,-}(z)=\begin{pmatrix}\lambda_{p,-}(z)&+\pi_0\\0&-S\end{pmatrix}\), where \(\lambda_{p,-}(z)=1-p^{-1}e^{2z\log p}\).

Since \(\lambda_{p,-}(-z)=\lambda_{p,+}(z)\), direct block multiplication gives \(C_JA_{p,+}(z)=A_{p,-}(-z)C_J\). The upper-right identity uses \((-1)(-\pi_0)=+\pi_0P_J\), and the lower-right identity uses \(P_JS=-SP_J\).

The inverse transport equals \(C_J^{-1}=C_J\), so the opposite chart identity follows automatically. On the doubled extension, sector exchange by \(R_{\mathrm{aug}}\) satisfies \(R_{\mathrm{aug}}A_{p,\mathrm{rec}}(z)R_{\mathrm{aug}}=A_{p,\mathrm{rec}}(-z)\).

The associated source Clifford transport \(K_{\mathrm{aug}}=iR_{\mathrm{aug}}\) satisfies \(K_{\mathrm{aug}}^2=-I\) and \(K_{\mathrm{aug}}A_{p,\mathrm{rec}}(z)=A_{p,\mathrm{rec}}(-z)K_{\mathrm{aug}}\). This is reciprocal chart covariance rather than fixed-parameter anticommutation.

## Disposition

Reciprocal Augmented-Extension Coherence is complete. The Euler coordinate is reciprocal-odd, the endpoint coordinate is reciprocal-even, the jet shift is reciprocal-odd, and the two Euler multipliers are exchanged by \(z\mapsto-z\). These four identities fill the augmented-extension coherence tetrahedron.
