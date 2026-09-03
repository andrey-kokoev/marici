# Theta augmented-kernel Jordan chain

Author: `marici.Grothendieck`
Status: analytic-pencil multiplicity identified
Predecessor: `theta-envelope-common-mode-selection.md`

## Question

How does multiplicity of a noncentral completed-scalar zero appear in the triangular source-amplitude augmentation, whose geometric kernel is one-dimensional?

## Claim boundary

Let \(\mathcal A(z)\) denote the analytic augmented boundary pencil consisting of

\[
u'=-zu-cF_z,
\qquad
v'=zv-cF_z,
\qquad
c'=0,
\]

with the two-ended finite-bulk boundary conditions and

\[
F_z(q)=-e^{-zq}a_\theta'(q).
\]

After fixing \(c=1\), the complete boundary obstruction reduces to the scalar

\[
C(z)=2z\,\xi\!\left(\tfrac12+z\right).
\]

At every noncentral zero \(z_0\), the homogeneous \(c=0\) two-ended kernel is trivial, so the augmented geometric kernel is one-dimensional. If \(\xi(\tfrac12+z)\) has order \(m\) at \(z_0\), then \(C\) has the same order because \(z_0\ne0\).

Differentiate the analytic interior solution and boundary trace with respect to \(z\). The vanishing conditions

\[
C^{(k)}(z_0)=0
\qquad (0\le k<m)
\]

are exactly the boundary conditions required by the first \(m\) differentiated pencil equations

\[
\sum_{j=0}^{k}
\frac1{j!}\mathcal A^{(j)}(z_0)Y_{k-j}=0,
\qquad
Y_k=\frac1{k!}\partial_z^kY(z_0).
\]

Thus the analytic pencil has a Jordan--Keldysh chain of length \(m\), geometric multiplicity one, and algebraic multiplicity equal to the scalar-zero order. For a simple zero, only the kernel vector occurs.

## Positive adjoint-symmetry test

The local augmented generator is triangular:

\[
M_z(q)=
\begin{pmatrix}
-z&0&-F_z(q)\\
0&z&-F_z(q)\\
0&0&0
\end{pmatrix}.
\]

At the central parameter,

\[
M_0(q)=
\begin{pmatrix}
0&0&-F_0(q)\\
0&0&-F_0(q)\\
0&0&0
\end{pmatrix},
\qquad
M_0(q)^2=0.
\]

The theta source has \(F_0=-a_\theta'\ne0\), so \(M_0\) is a nonzero nilpotent. A selfadjoint operator for a positive definite inner product is diagonalizable with real spectrum; a nilpotent selfadjoint operator must therefore be zero. Hence no positive definite metric can make this augmented generator selfadjoint uniformly through \(z=0\).

An indefinite metric can admit selfadjoint nilpotent blocks, but then the positive spectral argument required for confinement is unavailable. Adding the missing lower-left adjoint forcing block removes triangularity only by introducing the dual source coordinate whose endpoint increment is accumulated work.

## Punctured positive-metric singularity

For \(z\ne0\), the three eigendirections of the local triangular generator are represented by

\[
e_1,
\qquad
e_2,
\qquad
w_z=\left(-\frac{F_z}{z},\frac{F_z}{z},1\right).
\]

The first two span the sheet plane. In the background Euclidean metric, the sine of the angle between \(w_z\) and that plane is

\[
\sin\theta_z=
\frac{1}{\sqrt{1+2|F_z/z|^2}}.
\]

At any \(q\) with \(F_0(q)\ne0\), this is asymptotic to \(|z|/(\sqrt2|F_0(q)|)\). A positive symmetrizing metric must make eigenspaces belonging to distinct real eigenvalues orthogonal. Changing an angle \(\theta_z\) to a right angle requires metric condition number at least \(\sin^{-2}\theta_z\); hence

\[
\kappa(G_z)
\ge1+2|F_z/z|^2.
\]

Therefore every positive symmetrizer on the punctured real-parameter family becomes singular at least as \(|z|^{-2}\) when \(z\to0\). Multiplying the generator by \(i\) gives the analogous statement on the imaginary parameter axis. There is no bounded positive metric that bypasses the central nilpotent by deleting only \(z=0\).

## Noncentral pointwise symmetrizers

The central singularity does not by itself forbid positive symmetrization at a fixed noncentral point. For \(z=it\) with \(t\ne0\), the matrix \(iM_{it}(q)\) has distinct real eigenvalues \(t,-t,0\) and is diagonalizable. If \(S_{t,q}\) is an eigenvector matrix, then

\[
G_{t,q}=(S_{t,q}^{-1})^*S_{t,q}^{-1}>0
\]

makes that single matrix selfadjoint. Thus the preceding blow-up theorem is a no-go for a bounded family through \(z=0\), not a pointwise no-go at known noncentral critical-line parameters.

This pointwise construction has no spectral force. It depends on the candidate parameter and on \(q\), and every diagonalizable matrix with real spectrum admits the same construction. A variable metric must also satisfy the differential compatibility equation

\[
G'+M^*G+GM=0
\]

and the two-ended boundary law; pointwise diagonalization proves neither. A confinement theorem requires one source-derived metric and domain before locating zeros, not a metric fitted separately after selecting \(z\).

## Source-independent constant-metric test

On the critical axis \(z=it\), set \(A_t(q)=iM_{it}(q)\). Its diagonal is \((t,-t,0)\), and its source-to-sheet column is

\[
h_t(q)=-iF_{it}(q)
\begin{pmatrix}1\\1\end{pmatrix}.
\]

Because the theta envelope is even, \(a_\theta'(0)=0\), so \(h_t(0)=0\). For \(t\ne0\), the three diagonal eigenvalues at \(q=0\) are distinct. Any constant positive metric \(G\) satisfying

\[
A_t(q)^*G=GA_t(q)
\]

must therefore be diagonal at \(q=0\). At any \(q\) with \(F_{it}(q)\ne0\), comparison of the upper-right block gives

\[
0=(A_t^*G)_{13}=(GA_t)_{13}=G_{11}h_t(q),
\]

which contradicts \(G_{11}>0\). The second sheet gives the same contradiction.

Hence no positive metric constant in \(q\) symmetrizes even one noncentral critical-axis generator family, and a fortiori no source-independent constant metric works for all \(t\).

## Variable-metric tautology test

For any fixed parameter and any fundamental matrix \(T_z(q,q_0)\) of

\[
Y'=M_z(q)Y,
\]

every positive initial metric \(G_0\) generates

\[
G_z(q)=T_z(q,q_0)^{-*}G_0T_z(q,q_0)^{-1}>0.
\]

Direct differentiation gives

\[
G_z'+M_z^*G_z+G_zM_z=0,
\]

so \(Y^*G_zY\) is constant along every solution. Existence of a positive \(q\)-dependent metric is therefore automatic for every invertible linear flow, including flows with arbitrary spectral behavior.

This construction depends on the candidate parameter, a chosen basepoint metric, and the full fundamental solution. It supplies no endpoint boundedness, no common metric across the spectral family, and no restriction on zeros. Treating it as a source positivity theorem would convert the desired conclusion into a fitted transport metric.

## Variable but source-independent metric test

Suppose a positive \(G(q)\), independent of the spectral parameter \(t\), satisfies

\[
G'+M_{it}^*G+GM_{it}=0
\]

for every real \(t\). At any fixed \(q\ne0\) with \(a_\theta'(q)\ne0\), the source column contains the nonpolynomial factor \(e^{-itq}\), whereas \(G'\) is independent of \(t\) and the sheet diagonal is polynomial in \(t\). Linear independence of these functions of \(t\) forces the \(e^{-itq}\) coefficients in the upper-right block to vanish:

\[
G_{11}+G_{12}=0,
\qquad
G_{21}+G_{22}=0.
\]

Thus the positive sheet principal block annihilates \((1,1)^T\), which is impossible. Therefore no positive \(q\)-dependent metric independent of the spectral parameter is compatible with the complete critical-axis family.

The only variable positive metrics left by the transport equation necessarily depend on the candidate \(t\); those are precisely the fitted metrics of the preceding test.

## Reciprocal-completion work coordinate

The one-way source column is

\[
B=(-F,-F)^T.
\]

With the sheet signature \(J=\operatorname{diag}(1,-1)\), its adjoint partner is proportional to

\[
-B^*J=(\bar F,-\bar F).
\]

Thus the reciprocal source equation required by the natural indefinite adjoint completion is

\[
c'=\bar F(u-v).
\]

Its endpoint increment is the complex work pairing,

\[
c(+\infty)-c(-\infty)
=\int_{\mathbb R}\bar F(u-v)\,dq,
\]

whose real part is \(R_\theta\). Requiring the added coordinate to close at both ends imposes work closure and hence, for a nonzero scalar-zero response,

\[
0=R_\theta=-\operatorname{Re}(z)B_\theta.
\]

This does not derive confinement from the original scalar boundary problem. If \(c\) remains the constant source amplitude, the reciprocal equation is incompatible unless its work density vanishes. If \(c\) is allowed to vary, it feeds back into the sheet equations and changes the original scalar mismatch. If only its equal-endpoint condition is imposed, work closure has been added as boundary data. The three desiderata—reciprocal adjoint completion, unchanged scalar zero set, and no inserted work condition—cannot be retained simultaneously.

## Work-coordinate domain test

Let the decoupled accumulator satisfy

\[
j'=\bar F(u-v)=:g.
\]

For the theta response, \(g\) is integrable and decays at both ends, so every solution has finite limits

\[
j_+-j_-=
\int_{\mathbb R}g(q)\,dq.
\]

If the added coordinate is required to lie in ordinary \(L^2(\mathbb R)\), both limiting constants must vanish. The integration constant can set one limit to zero; the other then vanishes exactly when

\[
\int_{\mathbb R}\bar F(u-v)\,dq=0.
\]

Thus the \(L^2\) domain inserts complex work closure and changes the admitted scalar-zero set.

If instead the coordinate is placed in the derivative-only space \(\dot H^1(\mathbb R)/\mathbb C\), finite \(\|j'\|_2\) admits arbitrary endpoint jump. Then every original scalar-zero response survives and no work or critical-line restriction follows. Domain choice does not derive the missing law: the endpoint-sensitive domain assumes it, while the quotient domain erases it.

## Weighted work-coordinate domain test

Let \(j'=g\) have finite limits \(j_\pm\), and place \(j\) in \(L^2(\rho(q)dq)\) for a positive weight. Assume the decaying remainders \(j-j_\pm\) are weighted square-integrable on their respective tails. Define

\[
W_+=\int_0^\infty\rho(q)dq,
\qquad
W_-=
\int_{-\infty}^0\rho(q)dq.
\]

If both \(W_+\) and \(W_-\) diverge, membership forces \(j_+=j_-=0\), hence

\[
\int_{\mathbb R}g(q)dq=0.
\]

If exactly one tail mass diverges, the integration constant sets the corresponding limit to zero while the finite-weight tail admits an arbitrary nonzero limit. If both tail masses are finite, neither limit is constrained. Thus a weighted domain either imposes the same work closure when it detects both endpoints, or imposes no condition on the endpoint jump when at least one endpoint is hidden by finite weight.

No positive scalar weight derives a new intermediate restriction capable of preserving the complete scalar zero set while forcing only its off-line members out.

## Disposition

The source-amplitude augmentation records scalar multiplicity faithfully as analytic-pencil chain length. This does not provide confinement: a hypothetical off-line multiple zero carries the same chain while its base vector still satisfies

\[
R_\theta=-\operatorname{Re}(z_0)B_\theta\ne0.
\]

Multiplicity and Jordan structure strengthen the boundary realization but do not generate a positive selfadjoint metric or zero-work law.
