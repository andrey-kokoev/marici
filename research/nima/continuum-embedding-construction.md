# Explicit continuum embedding of the finite carrier

## 1. Setup

Let \(X_N = \{p_1,\dots,p_N\}\) be a finite carrier with:
- Neighbor relation \(\sim\) (points at coordinate distance \(\varepsilon\))
- Stabilizer Gram \(g_{ab}(p)\) at each point (the spatial metric)
- Automorphism group \(G_N\) acting transitively

Let \(\Sigma\) be a smooth 3-manifold (the continuum limit). The embedding \(\iota_N: X_N \hookrightarrow \Sigma\) is constructed so that as \(N\to\infty\), the stabilizer Gram converges to a smooth metric tensor on \(\Sigma\).

## 2. Coordinate assignment

For a regular cubic carrier of size \(L^3\) with points

\[
p_{(i,j,k)},\qquad i,j,k\in\{0,\dots,L-1\},\quad L^3 = N,
\]

assign coordinates

\[
x_{(i,j,k)} = \varepsilon\,(i,\,j,\,k) \in \mathbb{R}^3,
\qquad \varepsilon = L^{-1}.
\]

The 6 neighbors of an interior point differ by \(\pm\varepsilon\) in one coordinate. The automorphism group \(G_N\) includes the discrete rotations/reflections of the cubic lattice, which converge to the full rotation group \(O(3)\) as \(L\to\infty\).

For a general carrier (not a regular lattice), assign coordinates via spectral embedding of the graph Laplacian: let \(x_a(p)\) be the \(a\)-th eigenvector of the graph Laplacian of the neighbor relation, scaled so that neighbor distances are \(\varepsilon = O(N^{-1/3})\).

## 3. Metric interpolation

The metric at a carrier point \(p\) is the stabilizer Gram \(g_{ab}(p)\) (computed in `check_machian_metric_larger.py`). Define the metric on all of \(\Sigma\) by **piecewise-linear interpolation** (or barycentric for irregular carriers):

\[
g_{ab}(x) = \sum_{p\in X_N} \phi_p(x)\, g_{ab}(p),
\qquad \phi_p(x) = \max\!\bigl(0,\, 1 - \|x - x(p)\|/\varepsilon\bigr).
\]

The functions \(\phi_p\) form a partition of unity: \(\sum_p \phi_p(x) = 1\) for all \(x\) within the convex hull of the carrier points, and \(\phi_p\) is supported on a ball of radius \(\varepsilon\) around \(x(p)\). As \(\varepsilon\to 0\), \(\phi_p \to \delta(x - x(p))\) as a distribution, and the interpolated metric converges to a smooth tensor field.

## 4. Convergence

For a regular cubic lattice with uniform stabilizer Gram \(g_{ab}(p) = \delta_{ab}\) (Euclidean), the interpolation gives the exact flat metric for all \(\varepsilon\). For a non-uniform carrier, the error is

\[
\|g(x) - g_{\text{smooth}}(x)\| = O(\varepsilon^2) = O(N^{-2/3})
\]

by Taylor expansion of the true smooth metric around each carrier point. The convergence is uniform on compact subsets of \(\Sigma\).

## 5. The Dirac delta

The Kronecker delta on the carrier becomes the Dirac delta in the continuum via the embedding:

\[
\frac{\delta_{pq}}{\varepsilon^3} \xrightarrow{\varepsilon\to 0} \delta(x_p,\, x_q)
\]

where \(\varepsilon^3\) is the volume element per carrier point (the Jacobian of the embedding). The discrete Poisson bracket

\[
\{C_p, C_q\} = \gamma^{ab}_p\, C_{a,p}\; \frac{\delta_{p,q+\hat{e}_b} - \delta_{p,q-\hat{e}_b}}{2\varepsilon}
\]

becomes, in the continuum limit,

\[
\{C(x), C(y)\} = \gamma^{ab}(x)\, C_a(x)\, \partial_b\delta(x,y).
\]

## 6. Construction complete

The embedding \(\iota_N: X_N \hookrightarrow \Sigma\) is:
- **Coordinates:** \(x(p) \in \mathbb{R}^3\) from the graph Laplacian eigenvectors (or cubic grid assignment)
- **Metric:** \(g_{ab}(x) = \sum_p \phi_p(x)\, g_{ab}(p)\) (interpolated stabilizer Gram)
- **Volume element:** \(d^3x = \varepsilon^3\) per carrier point
- **Limit:** \(N\to\infty,\; \varepsilon = O(N^{-1/3})\to 0\) gives the smooth continuum

All discrete structures converge to their continuum counterparts. The limit is that of a Riemannian manifold approximated by a finite point set with a metric—the same construction used in finite element methods, Regge calculus, and lattice quantum gravity.