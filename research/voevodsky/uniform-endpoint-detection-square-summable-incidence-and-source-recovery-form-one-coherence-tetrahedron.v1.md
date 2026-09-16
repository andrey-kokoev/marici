# Uniform endpoint detection, square-summable incidence, and source recovery form one coherence tetrahedron

## Question

Can the uniformly faithful endpoint observer, Hilbert–Schmidt incidence, and source-retaining joint graph be organized without assigning uniform detectability to the decaying incidence output?

## Claim boundary

Let \(U_{\mathrm{rec}}=\bigoplus_p\mathbb C^2\) carry the weighted norm \(\|x\|_U^2=\sum_p\log(p)\|x_p\|^2\). Define the endpoint observer \(V=\bigoplus_pV_p\), where \(V_p=\frac12\begin{pmatrix}1&p^{-1}\\p^{-1}&1\end{pmatrix}\).

The eigenvalues of \(V_p\) are \(\frac12(1+p^{-1})\) and \(\frac12(1-p^{-1})\). Hence \(\frac14\|x\|_U\le\|Vx\|_E\le\frac34\|x\|_U\), where \(E=\operatorname{ran}(V)\) carries the inherited endpoint norm. Thus \(V:U_{\mathrm{rec}}\to E\) is a bounded isomorphism with \(\|V^{-1}\|\le4\).

Let \(B=B_{\mathrm{rec}}:U_{\mathrm{rec}}\to H_{\mathrm{wall,rec}}\) be the doubled analytic incidence from the reciprocal wall construction. It is Hilbert–Schmidt and satisfies \(\|B\|_{\mathrm{HS}}^2=2C_{\mathrm{cut}}^2\sum_p1/(p\log p)\).

Define the endpoint-to-response attenuation map by \(T=BV^{-1}:E\to H_{\mathrm{wall,rec}}\). The ideal property gives \(\|T\|_{\mathrm{HS}}\le4\|B\|_{\mathrm{HS}}\). The decay and compactness reside in \(T\), while \(V\) retains its uniform lower bound.

Define the joint graph \(G_B=\{(x,Bx):x\in U_{\mathrm{rec}}\}\subset U_{\mathrm{rec}}\oplus H_{\mathrm{wall,rec}}\) and \(j_Bx=(x,Bx)\). Since \(B\) is bounded, \(G_B\) is closed. The projection \(\pi_U:G_B\to U_{\mathrm{rec}}\) is the bounded inverse of \(j_B\), and \(\pi_H:G_B\to H_{\mathrm{wall,rec}}\) satisfies \(\pi_Hj_B=B\).

The four vertices \(U_{\mathrm{rec}}\), \(E\), \(H_{\mathrm{wall,rec}}\), and \(G_B\) form a strict coherence tetrahedron with faces \(B=TV\), \(B=\pi_Hj_B\), \(j_B=(j_BV^{-1})V\), and \(T=\pi_Hj_BV^{-1}\). Every face commutes by the displayed definitions, and their common tetrahedral filler is associativity of bounded operator composition.

This tetrahedron separates three analytic strengths. The map \(V\) supplies uniform endpoint detectability, the map \(B\) supplies square-summable arithmetic response, and the graph embedding \(j_B\) supplies exact source recovery. The map \(T\) records the attenuation between endpoint coordinates and incidence response.

The tetrahedron is analytic for the reflected candidate incidence \(B_{\mathrm{rec}}\). Arithmetic source independence of the negative columns remains a separate APCT provenance face.

## Disposition

The detectability–incidence–recovery reorganization is constructed. It removes the false demand that the Hilbert–Schmidt incidence itself carry a uniform lower bound and places uniform detection, decaying response, source recovery, and attenuation on four distinct edges of one strict tetrahedron.
