# The xi section should be an Evans determinant, not the unitary scattering determinant

The relative-spectrum fork needs one terminology correction. The finite boundary function
\[
D(z)=\det(I-CG(z))
\]
may vanish. The physical scattering determinant of a self-adjoint pair is unitary almost everywhere on the continuous spectrum and therefore cannot vanish where it is defined.

These are related but distinct objects.

Let \(D_{+}(x)\) and \(D_{-}(x)\) be nontangential boundary values of a perturbation or Evans determinant from the upper and lower half-planes. Under self-adjoint symmetry,
\[
D_{-}(x)=\overline{D_{+}(x)}
\]
away from singular points. The scattering determinant is schematically
\[
\det S_{\mathrm{sc}}(x)
=
\frac{D_{-}(x)}{D_{+}(x)}.
\]
Hence
\[
|\det S_{\mathrm{sc}}(x)|=1
\]
whenever \(D_{+}(x)\neq0\).

A zero of \(D_{+}\) is not a zero of the scattering determinant. It is a point where the boundary ratio requires a limiting interpretation and the scattering phase may jump or wind.

Therefore the completed scalar identification should be
\[
D(z)
=
N(z)\,
\xi\left(\frac12-iz\right)
\]
with \(N\) nowhere zero, not
\[
\det S_{\mathrm{sc}}(x)=\xi\left(\frac12+x\right).
\]

This distinction identifies the possible spectral meaning of a seam zero:

- an embedded eigenvalue;
- a half-bound state or threshold singularity;
- a real resonance;
- a boundary-feedback eigenphase crossing;
- or a zero of an Evans/Jost section without an \(L^2\) eigenstate.

The source domain and limiting absorption theorem must decide which one occurs.

Multiplicity also requires an explicit theorem. For an analytic finite boundary pencil
\[
F(z)=I-CG(z),
\]
the scalar order
\[
\operatorname{ord}_{z_0}\det F(z)
\]
is the algebraic multiplicity of the analytic operator pencil under standard finite-dimensional hypotheses. It need not equal
\[
\dim\ker F(z_0)
\]
when the crossing is tangential or has Jordan chains.

For a simple one-dimensional phase crossing, write an eigenvalue branch
\[
\mu(x)=e^{i\theta(x)}
\]
of \(CG(x)\). The resonance condition is
\[
\theta(x_0)\in2\pi\mathbb Z.
\]
It is simple only if
\[
\theta'(x_0)\neq0.
\]
A higher-order zero corresponds to higher-order tangency or several crossing eigenphases.

This gives the correct counting observable. The argument principle applied to \(D(z)\) on contours approaching the seam counts algebraic boundary crossings. The Birman--Krein phase, when authorized, relates the boundary argument of \(D\) to spectral shift.

The next analytic gates are:

1. prove a limiting absorption principle for the reference doubled transport;
2. prove boundary values \(G_{\pm}(x)\) exist in the declared operator topology;
3. prove reciprocal adjoint symmetry between them;
4. define the Evans determinant \(D_{\pm}\);
5. identify its boundary zeros with the correct relative spectral event;
6. prove its zero order matches the \(\xi\)-zero multiplicity;
7. derive the unitary scattering determinant only as the ratio \(D_{-}/D_{+}\).

The smallest hostile labels \(D\) as the scattering determinant and then claims its real zeros are scattering zeros. This contradicts scattering unitarity.

A second hostile proves only
\[
\dim\ker F(x_0)=1
\]
and declares the corresponding \(\xi\)-zero simple, despite a tangential eigenphase with
\[
\theta'(x_0)=0.
\]

Thus the conservative continuous-spectrum formulation is:

\[
\text{self-adjoint source pair}
\to
\text{boundary Evans determinant}
\to
\text{seam crossing divisor}
\to
\text{unitary scattering phase ratio}.
\]

The \(\xi\)-section belongs at the Evans-determinant level.
