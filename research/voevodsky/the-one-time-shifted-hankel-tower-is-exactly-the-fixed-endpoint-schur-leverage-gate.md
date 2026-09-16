# The one-time shifted Hankel tower is exactly the fixed endpoint Schur leverage gate

## Objective

Identify the fixed completed endpoint channel inside the one-time Stieltjes Hankel hierarchy.

The endpoint is a positive rank-one summand in the ordinary Hankel tower and a negative rank-one summand in the shifted tower. Consequently shifted Hankel positivity is exactly an endpoint leverage inequality against the gamma--prime remainder.

## Endpoint moment vector

Fix \(t_0>0\). The endpoint heat term is

\[
E(t)
=

e^{t/4}.
\]

Its alternating derivatives are

\[
d_k^E
=
(-1)^k
4^{-k}

e^{t_0/4}.
\]

For rank \(r\), define

\[
v_r
=
\begin{pmatrix}
1\\
-1/4\\
(-1/4)^2\\
\vdots\\
(-1/4)^r
\end{pmatrix}.
\]

Then the endpoint contribution to the ordinary Hankel matrix is

\[
\boxed{
H_r^E(t_0)
=

e^{t_0/4}
v_rv_r^*.
}
\]

It is positive rank one.

This is the moment matrix of one positive atom at the negative squared-spectral coordinate

\[
\lambda_E
=
-
\frac14.
\]

## Shifted endpoint matrix

The endpoint contribution to the shifted tower is

\[
(
d_{i+j+1}^E
)_{0\le i,j\le r}.
\]

Since

\[
d_{i+j+1}^E
=
-
\frac14

e^{t_0/4}
(-1/4)^{i+j},
\]

we obtain

\[
\boxed{
H_r^{E,+}(t_0)
=
-
\frac14

e^{t_0/4}
v_rv_r^*.
}
\]

Thus the shifted tower sees the endpoint atom with negative sign, exactly because the support condition requires \(\lambda\ge0\) while \(\lambda_E=-1/4\).

## Gamma--prime remainder

Write

\[
R(t)
=
\Theta(t)-

e^{t/4}
\]

and define its alternating jets

\[
r_k
=
(-1)^k
R^{(k)}(t_0).
\]

Let

\[
H_r^R
=
(
r_{i+j}
)_{0\le i,j\le r},
\]

\[
H_r^{R,+}
=
(
r_{i+j+1}
)_{0\le i,j\le r}.
\]

Then the complete towers split exactly as

\[
\boxed{
H_r
=
H_r^R
+

e^{t_0/4}
v_rv_r^*,
}
\]

\[
\boxed{
H_r^+
=
H_r^{R,+}
-
\frac14

e^{t_0/4}
v_rv_r^*.
}
\]

No endpoint approximation or asymptotic limit is involved.

## Shifted positivity as leverage

The shifted Stieltjes condition is

\[
H_r^+
\succeq0.
\]

Equivalently,

\[
\boxed{
H_r^{R,+}
\succeq
\frac14

e^{t_0/4}
v_rv_r^*.
}
\]

This is precisely a rank-one Schur--Douglas leverage inequality.

If \(H_r^{R,+}\succeq0\), Douglas factorization gives the equivalent range and norm conditions

\[
v_r
\in
\operatorname{ran}
(
H_r^{R,+}
)^{1/2},
\]

and

\[
\frac14

e^{t_0/4}
\left\|
(
H_r^{R,+}
)^{\dagger/2}
v_r
\right\|^2
\le
1,
\]

where \(\dagger\) denotes the Moore--Penrose inverse on the support.

Thus the endpoint gate in the heat-moment chart is the same rank-one leverage problem found in the Green/Sonin chart.

## Rank-zero condition

At rank zero,

\[
H_0^+
=
d_1
=
r_1
-
\frac14

e^{t_0/4}.
\]

Therefore the first endpoint leverage inequality is

\[
\boxed{
r_1
\ge
\frac14

e^{t_0/4}.
}
\]

This is the scalar monotonicity condition

\[
-
\Theta'(t_0)
\ge0.
\]

The gamma--prime remainder must overcome the negative shifted endpoint derivative.

## Rank-one condition

For \(r=1\),

\[
v_1
=
\begin{pmatrix}
1\\
-1/4
\end{pmatrix}.
\]

The shifted matrix is

\[
\begin{pmatrix}
r_1&r_2\\
r_2&r_3
\end{pmatrix}
-
\frac14

e^{t_0/4}
\begin{pmatrix}
1&-1/4\\
-1/4&1/16
\end{pmatrix}.
\]

Its positivity requires both the scalar leverage inequality and the coupled determinant condition

\[

d_1d_3
-
d_2^2
\ge0.
\]

Thus endpoint control is not exhausted by the rank-zero derivative bound.

## Ordinary tower

In the ordinary tower the endpoint contributes positively:

\[
H_r
=
H_r^R
+

e^{t_0/4}
v_rv_r^*.
\]

This positive atom can repair at most one remainder direction at each finite rank. It cannot absorb an arbitrary higher-dimensional hostile interior model space.

Translated Gaussian totality makes that limitation decisive in the completed source.

## Quarter-shift normalization

Set

\[
F(t)
=

e^{-t/4}
\Theta(t).
\]

The endpoint becomes the constant atom at shifted coordinate zero. This removes it from the weak normalized \(1-y\) localizer but not from the sharp support localizer corresponding to the lower spectral bound.

The positive diagonal congruence relating raw and quarter-shifted Hankel matrices preserves inertia. Therefore quarter-shift normalization does not eliminate the leverage theorem; it only moves the endpoint atom to the support boundary.

## Tetrahedral identification

The vector \(v_r\) is the finite-rank heat-moment presentation of the fixed endpoint row

\[
b_r.
\]

The shifted gamma--prime matrix \(H_r^{R,+}\) is the corresponding candidate common bulk

\[
C_r.
\]

Hence

\[
H_r^+
\succeq0
\]

is exactly

\[
\boxed{
C_r
\succeq
b_rb_r^*.
}
\]

The one-time Stieltjes tower and the terminal tetrahedral Schur gate are therefore two presentations of the same endpoint obstruction.

## Interaction with the moving rotor

A moving real-boundary rotor contributes additional model-space directions, while the endpoint vector remains rank one. At the crossing limit their direct coupling vanishes.

Therefore the endpoint atom can address only its own shifted support defect. It cannot cancel a symmetry-completed rank-two hostile rotor.

## Infinite-rank gate

For every finite \(r\), the endpoint leverage condition is explicit. Passing to the completed tower requires:

1. consistency under principal restriction;
2. bounded leverage constants;
3. convergence in the source moment graph;
4. no loss of range at the limit.

A proof at each fixed rank without uniform leverage does not produce the completed endpoint contraction.

## Disposition

The shifted one-time Hankel tower is the endpoint Schur gate in exact matrix form:

\[
\boxed{
H_r^+
=
H_r^{R,+}
-
\frac14

e^{t_0/4}
v_rv_r^*,
}
\]

so

\[
\boxed{
H_r^+
\succeq0
\Longleftrightarrow
H_r^{R,+}
\succeq
\frac14

e^{t_0/4}
v_rv_r^*.
}
\]

This identifies the previously separate heat-moment and Sonin/Green endpoint gates as one rank-one leverage problem.
