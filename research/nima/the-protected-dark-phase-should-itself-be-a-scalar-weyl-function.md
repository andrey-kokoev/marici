# The protected dark phase should itself be a scalar Weyl function

Once reciprocal parity forces the dark-to-radiative coupling to vanish, the seam problem becomes scalar. The strongest source theorem is then a scalar Weyl realization.

Let the complete boundary space split as
\[
\mathcal B
=
\mathcal B_{\mathrm{dark}}
\oplus
\mathcal B_{\mathrm{rad}},
\]
with each summand one-dimensional and invariant under the source Weyl function:
\[
M(z)
=
\begin{pmatrix}
m_d(z)&0\\
0&m_r(z)
\end{pmatrix}.
\]

Assume the dark boundary condition is a real constant
\[
\theta_d\in\mathbb R.
\]
The dark Evans factor is
\[
a(z)
=
\theta_d-m_d(z).
\]

If \(m_d\) is a scalar Nevanlinna function, then
\[
\operatorname{Im}z>0
\quad\Longrightarrow\quad
\operatorname{Im}m_d(z)>0
\]
for a minimal nonconstant channel. Hence
\[
a(z)\neq0
\]
in the upper half-plane. Reflection excludes the lower half-plane. Every zero of \(a\) lies on the real seam.

This is the scalar form of the whole RH mechanism.

The Nevanlinna representation is
\[
m_d(z)
=
\alpha+\beta z
+
\int_{\mathbb R}
\left(
\frac{1}{t-z}
-
\frac{t}{1+t^2}
\right)d\mu_d(t),
\]
with
\[
\beta\ge0,
\qquad
\mu_d\ge0.
\]

The dark channel's boundary radiation density is
\[
\operatorname{Im}m_d(x+i0)
=
\pi\frac{d\mu_d^{\mathrm{ac}}}{dx}(x).
\]
If the channel is radiation-dark on the full regular seam, then its absolutely continuous density vanishes there. The measure \(\mu_d\) must be singular in that sector.

The cleanest outcome is a pure point measure:
\[
\mu_d
=
\sum_n \alpha_n\delta_{\tau_n},
\qquad
\alpha_n>0.
\]
Then
\[
m_d(z)
=
\alpha+\beta z
+
\sum_n
\alpha_n
\left(
\frac{1}{\tau_n-z}
-
\frac{\tau_n}{1+\tau_n^2}
\right).
\]

Between consecutive poles, one has
\[
m_d'(x)
=
\beta
+
\sum_n\frac{\alpha_n}{(\tau_n-x)^2}
>0.
\]
Therefore the equation
\[
m_d(x)=\theta_d
\]
has at most one solution in each pole interval, every solution is simple, and the zeros interlace the poles.

This gives a powerful prediction: a symmetry-protected Hilbert--Pólya channel should come with a hidden positive spectral measure whose support interlaces the zeta ordinates.

The poles need not themselves be zeta zeros. They belong to a reference self-adjoint extension or uncoupled dark Hamiltonian. Changing the real boundary condition from one value of \(\theta_d\) to another shifts the interlacing spectrum.

The source responsibilities are now:

1. prove reciprocal parity reduces \(M(z)\);
2. prove \(m_d\) is Nevanlinna from a positive dark-state norm;
3. identify its representing measure from theta, wall, and archimedean data;
4. prove the dark boundary constant \(\theta_d\) is source-fixed;
5. identify
   \[
   \theta_d-m_d(z)
   \]
   with the completed \(\xi\)-section up to a zero-free factor.

There is a severe falsifier. A scalar entire function with infinitely many real zeros is not itself a Nevanlinna function in general. The intended identification must be with
\[
\theta_d-m_d(z)
\]
after a zero-free normalization, and the resulting quotient must have the pole structure required of a Weyl function.

If one defines
\[
m_d(z)=\theta_d-\xi\left(\frac12-iz\right),
\]
Nevanlinna positivity is an additional highly nontrivial claim and may simply be false. It cannot be assumed from real zeros alone.

The minimal hostile constructs a real meromorphic \(m_d\) whose zeros lie on the seam but whose residues at poles have mixed signs. It has the desired divisor but no positive spectral measure and no self-adjoint realization.

A second hostile proves \(m_d\) is Herglotz only after dividing by a canonical product built from the zeta zeros. That imports the spectrum into the metric.

Thus the next source-native scalar target is exact:

> Construct a positive measure \(\mu_d\) from the reciprocal theta-wall source such that its Weyl function \(m_d\) has the completed zeta divisor as one real boundary-condition spectrum.

If achieved, the categorical RH tower collapses to classical rank-one extension theory.
