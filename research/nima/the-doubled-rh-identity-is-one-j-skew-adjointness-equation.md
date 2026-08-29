# The doubled RH identity is one J-skew-adjointness equation

The Clifford-weighted Green target can be compressed into a single operator identity.

Let the doubled centered system be written schematically as
\[
\mathcal A(\lambda)
=
\mathcal A_0+\lambda J,
\qquad
J=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix},
\]
where the two sheets carry parameters \(+\lambda\) and \(-\lambda\).

Pair the equation
\[
\mathcal A(\lambda)\Psi=0
\]
against \(J\Psi\). Since \(J^2=I\), the parameter term becomes
\[
\langle \lambda J\Psi,J\Psi\rangle
=
\lambda\|\Psi\|^2.
\]
Taking real parts gives the desired positive centered energy:
\[
2\operatorname{Re}\lambda\,\|\Psi\|^2.
\]

All remaining source content is contained in the formal Green identity
\[
\mathcal A_0^{*}J+J\mathcal A_0
=
\Gamma^{*}\Sigma\Gamma,
\]
where:

- \(\Gamma\) is the complete typed boundary trace;
- \(\Sigma\) is the signed boundary flux matrix;
- the equality is first a quadratic-form identity on a common core.

If interior dissipation remains, the exact form is
\[
\mathcal A_0^{*}J+J\mathcal A_0
=
\Gamma^{*}\Sigma\Gamma-\mathcal Q,
\qquad
\mathcal Q\ge0.
\]

For a solution,
\[
2\operatorname{Re}\lambda\,\|\Psi\|^2
+
\langle\Psi,\mathcal Q\Psi\rangle
=
-\langle\Gamma\Psi,\Sigma\Gamma\Psi\rangle,
\]
up to the frozen sign convention.

A conservative reciprocal boundary condition is a maximal \(\Sigma\)-isotropic relation
\[
\Lambda\subset\mathcal B_{\partial},
\]
so
\[
\Gamma\Psi\in\Lambda
\quad\Longrightarrow\quad
\langle\Gamma\Psi,\Sigma\Gamma\Psi\rangle=0.
\]
Every nonzero closed state then obeys the seam restriction.

This formulation reveals exactly what “forcing cancellation” means. The source coupling, wall carrier, prime currents, and archimedean attachment do not need to cancel termwise by inspection. Together they must make \(\mathcal A_0\) \(J\)-skew-adjoint modulo the complete boundary trace.

The finite block audit is now mechanical. Write
\[
\mathcal A_0=
\begin{pmatrix}
A_{++}&A_{+-}\\
A_{-+}&A_{--}
\end{pmatrix}.
\]
Then
\[
\mathcal A_0^{*}J+J\mathcal A_0
=
\begin{pmatrix}
A_{++}^{*}+A_{++}
&
A_{+-}-A_{-+}^{*}\\
A_{+-}^{*}-A_{-+}
&
-(A_{--}^{*}+A_{--})
\end{pmatrix}.
\]

Thus the mixed forcing disappears from the bulk exactly when
\[
A_{+-}=A_{-+}^{*}
\]
after transporting the reciprocal sheet into the common source metric. Any defect in this identity is the residual indefinite forcing channel.

The diagonal blocks must satisfy opposite Green laws:
\[
A_{++}^{*}+A_{++}
=
\text{positive-sheet boundary flux},
\]
\[
A_{--}^{*}+A_{--}
=
-\text{negative-sheet boundary flux}.
\]

This is the source-native test to apply to the theta forcing. If the reciprocal involution \(R\) maps the positive forcing incidence \(F_{+}\) to the adjoint negative incidence,
\[
F_{-}
=
R F_{+}^{*}R^{-1},
\]
then the mixed block condition follows after the sheet identification. If it maps only scalar Mellin shadows, the Green identity remains unproved.

The boundary relation language also handles the unresolved seam graph. The condition \(\Lambda\) may be a closed maximal isotropic relation rather than the graph of a bounded unitary. No premature tail-to-seam operator is required.

Completion gates are:

1. \(\mathcal A_0\) is closed or closable on the doubled graph domain.
2. The form identity survives closure.
3. \(\Gamma\) contains every wall, seam, prime, and archimedean port.
4. \(\Lambda\) is maximal isotropic, not merely isotropic.
5. The state norm on the parameter term is positive and complete.
6. No nonzero state lies in both \(\ker\Gamma\) and \(\ker\mathcal Q\).

The last condition prevents a dark lossless bulk state. It is the operator-domain version of the five observability margins.

The minimal hostile satisfies
\[
\langle\Psi,
(\mathcal A_0^{*}J+J\mathcal A_0)\Psi
\rangle
=
\langle\Gamma\Psi,\Sigma\Gamma\Psi\rangle
\]
only on scalar test states, while the mixed block defect
\[
A_{+-}-A_{-+}^{*}
\]
is nonzero on an unobserved direction.

Thus the earliest full RH gate is no longer vague:

> Prove the doubled source generator is \(J\)-skew-adjoint modulo the complete boundary system, and prove reciprocal sewing is a maximal isotropic boundary relation.

This one equation simultaneously yields the Green identity, the passive scattering law, and seam confinement.
