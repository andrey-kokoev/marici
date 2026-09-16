# The prime-power half-density incidence extends endpoint polarity to square and connected strata

## Question

Do the source-weighted prime-power incidences extend the primitive reciprocal endpoint trace to square and connected Euler strata with exact normalization and ideal control?

## Claim boundary

For prime \(p\) and grade \(k\ge1\), put \(L_{p,k}=k\log p\) and \(a_{p,k}=k^{-1}p^{-k/2}\). Define the doubled source incidence \(\mathcal I_{p,k}(c_+,c_-)=a_{p,k}(c_+\tau_{L_{p,k}}\Phi,c_-\tau_{-L_{p,k}}\Phi)\).

The completed theta moments satisfy \(M_-(\Phi)=M_+(\Phi)=1/2\), while translation gives \(M_-(\tau_L\Phi)=e^{L/2}/2\) and \(M_+(\tau_L\Phi)=e^{-L/2}/2\). Therefore the positive grade-\(k\) endpoint column is \((2k)^{-1}(1,p^{-k})^T\), and the negative column is \((2k)^{-1}(p^{-k},1)^T\).

The complete endpoint matrix is \(V_{p,k}=\frac1{2k}\begin{pmatrix}1&p^{-k}\\p^{-k}&1\end{pmatrix}\). It commutes with reciprocal slot exchange and has eigenvalues \((2k)^{-1}(1+p^{-k})\) and \((2k)^{-1}(1-p^{-k})\).

At square grade \(k=2\), \(V_{p,2}=\frac14\begin{pmatrix}1&p^{-2}\\p^{-2}&1\end{pmatrix}\) and its lower eigenvalue is at least \(3/16\). Hence the square endpoint observer is uniformly faithful over primes.

For every connected grade \(k\ge3\), the endpoint matrix remains invertible at each \((p,k)\). Its factor \(1/k\) records the source cyclic weight, so uniform detectability across unbounded grade is stated relative to the source-weighted grade norm rather than an unweighted direct sum.

Reflection satisfies \(R_H\tau_{L_{p,k}}\Phi=\tau_{-L_{p,k}}\Phi\), so reciprocal exchange commutes with every grade incidence and endpoint trace. The relative Adams weights obey the exact cocycle \(\rho_{rs}(p,k)=\rho_s(p,rk)\rho_r(p,k)\), which removes path-dependent normalization across iterated grade changes.

The square columns have coefficient \(\frac12p^{-1}\) and retain the established Hilbert–Schmidt bound. The connected grades satisfy the established nuclear estimate \(\sum_p\sum_{k\ge3}k^{-1}p^{-k/2}\|u_{p,k}\|<\infty\). Unitary reciprocal and Fourier transports preserve these operator ideals.

## Disposition

Higher-Stratum Polarity Functoriality is complete on the source-weighted prime-power carrier. The square and connected endpoint matrices are exact, reciprocal transport commutes with every grade, square incidence remains Hilbert–Schmidt, and the connected tail remains nuclear. The connected lower frame bound is relative to the source-weighted grade topology because the cyclic factor \(1/k\) tends to zero in the unweighted grade norm.
