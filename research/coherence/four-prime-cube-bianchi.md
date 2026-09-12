# The mixed prime-window curvature is cubically closed

## Operators

On the four-prime exterior-label packet tensored with a half-line seam, set

\[
D=\sum_p d_p,
\qquad
d_p=c_p\otimes R_p,
\]

and use the aggregate contraction candidate

\[
H=\sum_p h_p,
\qquad
h_p=i_p\otimes S_p.
\]

The boundary curvature is the even operator

\[
A=DH+HD.
\]

Its diagonal terms contain the single-prime windows \(P_p\); its off-diagonal terms contain the previously computed mixed residuals

\[
c_qi_p\otimes K_{q,p}.
\]

Thus \(A\neq I\) and is strongly nonzero at the boundary.

## Cube identity

Because the prime-seam differential satisfies

\[
D^2=0,
\]

associativity gives

\[
\begin{aligned}
DA-AD
&=D(DH+HD)-(DH+HD)D\\
&=D^2H-HD^2\\
&=0.
\end{aligned}
\]

This is the cube-level Bianchi identity. The nonzero square residuals do not disappear; they assemble into a covariantly closed curvature packet.

Hence the dimensional structure is not

\[
\text{nonzero square}\Rightarrow\text{nonzero cube boundary}.
\]

It is

\[
\boxed{
\text{flat source differential}
\;\Rightarrow\;
\text{nonzero boundary curvature}
\;\Rightarrow\;
\text{closed cube transport of that curvature}.
}
\]

## Four-dimensional implication

Once curvature is cubically closed, the next invariant is not another ordinary boundary. In four dimensions the natural object is quadratic in curvature, schematically

\[
A\smile A
\quad\text{or}\quad
\operatorname{Tr}(A\wedge A),
\]

with the product and trace determined by the source coefficient system. This is the first candidate that uses the full 4-cell rather than only its square faces or cubic facets.

This gives a sharper interpretation of the power sequence:

- prime edges carry the odd differential \(D\);
- squares carry even curvature \(A\);
- cubes carry the Bianchi coherence \([D,A]=0\);
- the 4-cell can carry a characteristic pairing of curvature with itself.

The final line is a candidate, not yet a constructed invariant: ordinary operator multiplication, a cubical cup product, and a cyclic trace are different typings and must not be identified silently.

## Exact finite check

`check_four_prime_cube_bianchi.py` realizes the exterior algebra on four generators and half-line shifts on a finite seam window. It checks all 272 basis vectors and finds:

- \(D^2=0\);
- \(A\neq0\) on 270 basis columns;
- \(DA-AD=0\) on every basis column.

The integer shifts \((1,2,3,4)\) are order-preserving finite proxies for \((\log2,\log3,\log5,\log7)\). The Bianchi cancellation itself is algebraic and does not depend on their numerical values; the finite model is an exact implementation check, not an approximation claim about the logarithms.

Artifacts:

- `check_four_prime_cube_bianchi.py`
- `four-prime-cube-bianchi.v1.json`
