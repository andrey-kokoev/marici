# The two-shift overlap graph gives the exact prime-operator norm

Put `ell=2L=1.1`, `a=log 2`, `b=log 3`, and `delta=b-a`.
Both zero-extension shifts are square-zero and cross the midpoint. Write the
prime operator in bipartite form `[[0,B*],[B,0]]`, with edge weights

\[
u=\frac{\log2}{2\sqrt2},\qquad v=\frac{\log3}{2\sqrt3}.
\]

Almost every translation fiber is a single `u` edge. On the small overlap
interval for the `b` shift, the only nontrivial component has two inputs and
two outputs, with incidence matrix

\[
B_*=\begin{pmatrix}u&0\\v&u\end{pmatrix}.
\]

There are no longer components: adding `delta` once moves the `b`-domain into
the right edge of the `a`-domain, and adding it again exits that domain.
Therefore

\[
\|P_L\|=\|B\|=\|B_*\|
=\sqrt{u^2+\frac{v^2}{2}+\frac v2\sqrt{v^2+4u^2}}.
\]

This retains the exact cross-prime overlap instead of applying the triangle
inequality to the two square-zero shifts.
