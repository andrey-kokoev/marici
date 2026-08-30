# One prescribed spectrum does not authorize a scalar Weyl model

Even if a scalar Weyl realization of the zeta ordinates exists, existence alone would not explain RH.

Given a simple real sequence with suitable growth, one can often choose an interlacing pole sequence and positive residues so that a scalar Herglotz function
\[
m(z)
=
\alpha+\beta z
+
\sum_n \alpha_n
\left(
\frac{1}{\tau_n-z}
-
\frac{\tau_n}{1+\tau_n^2}
\right)
\]
takes a fixed real value
\[
m(\gamma_n)=\theta
\]
at the prescribed points.

Thus the statement

> There exists a positive scalar Weyl function whose boundary-condition spectrum is the zeta-zero sequence

is vulnerable to post hoc inverse-spectral fitting.

The source must determine more than one spectrum. A scalar Weyl function is fixed by data such as:

- a reference pole spectrum \(\{\tau_n\}\);
- positive norming constants or residues \(\{\alpha_n\}\);
- two interlacing self-adjoint extension spectra;
- or an independently derived spectral measure.

For two real boundary parameters \(\theta_0\neq\theta_1\), the spectra of
\[
m(x)=\theta_0
\]
and
\[
m(x)=\theta_1
\]
interlace. Their ratio of characteristic sections determines the Weyl function up to controlled normalization:
\[
\frac{D_{\theta_1}(z)}{D_{\theta_0}(z)}
\sim
\frac{\theta_1-m(z)}{\theta_0-m(z)}.
\]

This suggests a source-native two-spectrum programme. The four-port boundary system may provide two independently authorized reciprocal or wall boundary conditions:

- one whose spectrum gives the poles of \(m_d\);
- one whose spectrum is claimed to give the \(\xi\) zeros.

The first spectrum must arise from a simpler source constructor, not from inserting points between the zeta zeros.

Alternatively, theta-tail data may directly provide norming constants:
\[
\alpha_n
=
\|\text{source mode at }\tau_n\|^{-2}.
\]
Their positivity would then prove the Herglotz property constructively.

This creates an authority hierarchy:

\[
\text{source operator and cyclic vector}
\to
\text{positive spectral measure}
\to
m_d(z)
\to
\text{extension spectra}
\to
\xi\text{ identification}.
\]

The reverse direction
\[
\xi\text{ zeros}
\to
\text{interlacing poles}
\to
m_d
\]
is not explanatory.

The asymptotic counting law is also insufficient to fix the measure. Many interlacing pole sequences share the same leading \(T\log T\) density. Residues and lower-order phase data remain free.

The next concrete source audit should ask whether the present wall/tail constructor supplies a second canonical boundary condition. Natural candidates are:

- constant versus delta wall closure;
- even versus odd reciprocal sewing;
- primitive versus square endpoint closure;
- Dirichlet versus Neumann-type theta-tail traces.

For each candidate pair, prove:

1. both extensions are self-adjoint;
2. their resolvent difference is rank one;
3. their spectra interlace;
4. the residue signs are positive;
5. one characteristic section is independently computable;
6. the other is identified with \(\xi\) only at the final step.

The smallest hostile chooses one pole between every pair of observed zeta ordinates and assigns positive residues to interpolate them. It produces a valid scalar Weyl function but encodes the target spectrum by construction.

A second hostile supplies two spectra, both extracted from \(\xi\) and \(\xi'\). This may be mathematically elegant but still derives the source operator from the target function unless the second spectrum has independent constructor authority.

A third hostile matches the two spectra but not the norming constants, leaving nonunique spectral measures.

Thus the next irreducible question is:

> What is the source-derived reference extension paired with the proposed zeta extension?

Without that second extension or an independently derived positive measure, the scalar Weyl model remains an inverse-spectral restatement.
