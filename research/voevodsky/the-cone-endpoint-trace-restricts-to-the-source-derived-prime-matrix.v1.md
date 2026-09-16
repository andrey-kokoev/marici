# The cone endpoint trace restricts to the source-derived prime matrix

## Question

Does the complete cone endpoint trace agree with the source-derived reciprocal endpoint matrix on the primitive prime-generated core?

## Claim boundary

The cone endpoint trace is built from the two half-density Wronskian moments \(M_-(g)=\int e^{-u/2}g(u)\,du\) and \(M_+(g)=\int e^{u/2}g(u)\,du\), in that row order. The completed theta forcing satisfies \(M_-(\Phi)=M_+(\Phi)=1/2\).

For \(L=\log p\), translation gives \(M_-(\tau_L\Phi)=e^{L/2}/2\) and \(M_+(\tau_L\Phi)=e^{-L/2}/2\). Primitive half-density loading therefore gives \(p^{-1/2}(M_-(\tau_L\Phi),M_+(\tau_L\Phi))^T=(1/2,p^{-1}/2)^T\).

The reciprocal translate satisfies \(M_-(\tau_{-L}\Phi)=e^{-L/2}/2\) and \(M_+(\tau_{-L}\Phi)=e^{L/2}/2\). Primitive half-density loading gives \(p^{-1/2}(M_-(\tau_{-L}\Phi),M_+(\tau_{-L}\Phi))^T=(p^{-1}/2,1/2)^T\).

Hence the cone endpoint trace of the local source incidence \(\mathcal I_p(c_+,c_-)=p^{-1/2}(c_+\tau_L\Phi,c_-\tau_{-L}\Phi)\) is exactly \(\operatorname{Tr}_{\partial}\mathcal I_p=V_p=\frac12\begin{pmatrix}1&p^{-1}\\p^{-1}&1\end{pmatrix}\).

The row order is \((M_-,M_+)\), the column order is \((e_{p,+},e_{p,-})\), and the source orientation is real before the physical negative channel receives its Clifford phase. The physical convention \(\operatorname{Tr}_-=-i\operatorname{Tr}_+R_{\mathrm{src}}\) applies the phase after this cone/source endpoint identification and leaves all endpoint norms unchanged.

The half-density history theorem makes \(\operatorname{Tr}_{\partial}\) graph-norm continuous, while the prime-diagonal incidence is Hilbert–Schmidt in the seam-weighted direct sum. The equality therefore extends from finite prime packets to the completed primitive source-generated range.

## Disposition

Gate 1 is complete on the primitive seam-weighted source-generated cone range. The cone endpoint trace, source endpoint matrix, and analytic reciprocal trace have the same row order, half-density normalization, and reciprocal exchange. Extension to square and connected response strata requires their separately declared endpoint constructors and is outside this primitive comparison.
