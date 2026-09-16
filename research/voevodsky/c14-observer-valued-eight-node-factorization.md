# Observer-valued C14 has one eight-node semilocal path presentation

## Question

Can the source-to-trace edge be subdivided without using the nonfaithful scalar map \(h\mapsto W_S(h)\) as a presentation equivalence?

## Claim boundary

One admissible sequential path exists on the observer-generated Bruhat--Schwartz carrier when \(V_4\) retains the complete Hermitian form \((g_1,g_2)\mapsto W_S(g_1*g_2^*)\). Its signed composite is exact modulo the rapid cutoff ideal, and its positive lift has the iterated-regulator relative-feature strength proved for \(C_{34}\). The seven positions are not yet identified with the uniform edgewise-subdivision positions of the other conductor edges. This does not give a faithful scalar evaluation map or an ordinary simultaneous-regulator Hilbert realization.

Write \(h_{12}=g_1*g_2^*\). The eight presentations are:

\[
C_{14}[0]=(g_1,g_2),
\]

\[
C_{14}[1]=h_{12},
\]

\[
C_{14}[2]=\overline{m_{g_2}}m_{g_1},
\]

\[
C_{14}[3]=
\left(\overline{m_{g_2}}m_{g_1},V_{\mathrm{loc},S},E_{\mathrm{end}}\right),
\]

\[
C_{14}[4]=\{W_v(h_{12})\}_{v\in S},
\]

\[
C_{14}[5]=W_S(h_{12})=\sum_{v\in S}W_v(h_{12}),
\]

\[
C_{14}[6]=
\operatorname{Tr}(P_\Lambda\widehat P_\Lambda U_S(h_{12}))
-2\log\Lambda\,h_{12}(1),
\]

\[
C_{14}[7]=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}(P_\Lambda\widehat P_\Lambda U_S(h_{12})).
\]

The seven arrows are:

1. \(\sigma_{14}[0]\): convolution polarization;
2. \(\sigma_{14}[1]\): multiplicative Mellin transform;
3. \(\sigma_{14}[2]\): insert the reflected logarithmic differential and endpoint residue row;
4. \(\sigma_{14}[3]\): identify gamma and prime-power currents with normalized local principal-value distributions;
5. \(\sigma_{14}[4]\): sum over places;
6. \(\sigma_{14}[5]\): realize the Weil sum as the centered product-cutoff trace modulo the rapid error;
7. \(\sigma_{14}[6]\): remove the cutoff by finite part.

The terminal equality is

\[
C_{14}[7](g_1,g_2)=W_S(g_1*g_2^*).
\]

The endpoint and interior current in segment \(2\) are one contour differential:

\[
\Omega_S(z)\,dz=
\left[
\frac1{2i}\partial_z\log\mathcal S_S(z)
+\varepsilon_{\mathrm{end}}\frac{2z}{z^2+1/4}
\right]dz.
\]

Contour displacement gives the gamma--prime current on the real line and endpoint residues at \(z=\pm i/2\). This prevents endpoint data from being appended after scalarization.

## Coherence

The route through \(C_{13}\) and \(C_{34}\) and the route through \(C_{12}\) and \(C_{24}\) produce the same terminal form through the tetrahedral equation. Their intermediate semantic stages occur in different orders. In particular, the spectral route forms the dual/canonical pair and its phase before the trace presentation, while the geometric route inserts cutoffs before the finite-part observation. Therefore equal numerical segment indices across these paths do not define rowwise comparisons. Coherence is indexed by the dependency-poset chambers and their face homotopies. The regulator-relative positive feature supplies the non-scalar middle comparison.

## Transition-granularity audit

The seven arrows above are not in bijection with the seven coarse dependency labels \(A,J,P,C,T,E,F\). In particular, \(\sigma_{14}[2]\) combines scattering-current insertion with endpoint completion, while \(\sigma_{14}[5]\) combines cutoff realization with centered trace asymptotics. Conversely, the local principal-value identification is a separate arrow here but is internal to the coarse trace transition. Therefore this path is not itself one of the 28 linear extensions until a refinement map from fine arrows to coarse transitions is declared.

Because the place stage \(S\) is fixed at \(C_{14}[0]\), semilocal amplification \(A\) belongs to the initial context rather than to a fine arrow. A monotone map to order ideals of the coarse dependency poset is

\[
I_0=\{A\},
\quad I_1=\{A,P\},
\quad I_2=\{A,P,J\},
\quad I_3=\{A,P,J,E\},
\]

\[
I_4=I_5=I_3,
\quad I_6=\{A,P,J,E,C,T\},
\quad I_7=\{A,P,J,E,C,T,F\}.
\]

The equal ideals at nodes \(4,5\) type principal-value identification and place summation as internal refinements of the \(J\)-to-\(T\) comparison. The jump \(I_5\subset I_6\) bundles \(C\) followed by \(T\); subdividing it once yields the admissible coarse order

\[
A<P<J<E<C<T<F.
\]

This order satisfies every mandatory dependency. The resulting map is monotone but degenerate: not every fine analytic arrow adds a coarse transition, and one fine arrow realizes two successive coarse transitions.
## Disposition

The retyped observer-valued \(C_{14}\) has one source-backed seven-arrow path presentation assembled from source, spectral, local-distribution, and semilocal trace formulas. It is not yet a canonical rowwise alignment with the seven positions on \(C_{13}\) or \(C_{24}\). Such alignment must be represented by the 28 admissible chambers of the seven-transition dependency poset and their comparison cells. Scalar evaluation at one observer remains a terminal readout.