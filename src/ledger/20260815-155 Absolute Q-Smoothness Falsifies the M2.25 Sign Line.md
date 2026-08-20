---
authors:
  - marici.Benincasa
---
# Absolute Q-Smoothness Falsifies the M2.25 Sign Line

## Record

Date: 2026-08-15

Status: falsified in the generic absolute algebraic-kernel sector; the
marked-relative/extension placement of \(\mathcal Q\) remains open.

This is the narrow Deutsch--Popperian outcome of M2.25.  It falsifies entry
152's risk-bearing identification of an absolute rank-one subquotient with
\(\mathcal K_{\sqrt{-\mathcal Q}}(-1)\).  It neither reopens entry 150's
generic infinity-Gysin quotient nor counts a smaller marked-relative
replacement as success of M2.25.

## Claim

Put

\[
E=x+y+z,\qquad h=x^2+y^2-z^2,\qquad
A=h-2xy,\qquad B=h+2xy,
\]

\[
u=E^2+y^2,\qquad v=E^2+x^2,
\qquad
\mathcal Q=4AB-(A+B-E^2)^2.
\]

The absolute compactified \(q_{\mathcal G_{12}}\)-residue branch model is
the degree-two cover

\[
\overline S_E:\quad W^2=\overline K_E(\alpha,\beta,s)
\]

with

\[
\boxed{
\begin{aligned}
\overline K_E={}&x^2(\alpha^2-us^2)^2
-h(\alpha^2-us^2)(\beta^2-vs^2)\\
&+y^2(\beta^2-vs^2)^2+E^2ABs^4.
\end{aligned}}
\]

At \(s=0\) this restricts to the entry-150 binary quartic

\[
x^2\alpha^4-h\alpha^2\beta^2+y^2\beta^4.
\]

Writing \(X=\alpha^2\), \(Y=\beta^2\), and \(Z=s^2\), let \(q(X,Y,Z)\)
be the displayed quadratic form.  Its full and coordinate-restriction
determinants are

\[
\det(q)=-\frac14E^2(AB)^2,
\]

\[
4\det(q|_{Z=0})=-AB,
\]

\[
4\det(q|_{X=0})=-AB(E^2-y^2)^2,
\qquad
4\det(q|_{Y=0})=-AB(E^2-x^2)^2.
\]

The remaining coordinate-axis coefficient is

\[
H=x^2u^2-huv+y^2v^2+E^2AB
=z^2(E^4-hE^2+x^2y^2).
\]

These identities exclude every all-nonzero, one-zero, and two-zero
singularity of the branch quartic whenever the displayed factors and
\(x,y,H\) are nonzero.  The slice certificate below meets those conditions
at a simple zero of \(\mathcal Q\).  Thus \(\mathcal Q=0\) is not an
absolute discriminant component: the compactified surface and its infinity
elliptic divisor are generically smooth across it, away from the absolute
discriminant and soft loci.

Consequently the absolute Gauss--Manin local system extends across a small
transverse disk and has trivial local monodromy around \(\mathcal Q=0\).
By contrast,

\[
\mathcal K_{\sqrt{-\mathcal Q}}
\quad\text{has}\quad
\operatorname{Res}_{\mathcal Q=0}=\frac12\pmod{\mathbb Z},
\qquad T_{\mathcal Q}=-1.
\]

A rational rank-one gauge changes the residue by
\(\operatorname{ord}_{\mathcal Q}(R)\in\mathbb Z\); it cannot change the
trivial character into the sign character.  Therefore the absolute
algebraic-kernel sign-line conjecture of entry 152 is falsified.

There is also a semantic normalization correction to entry 148.  For the
standard Legendre object and the published \(L_2\), the source-compatible
presentations are

\[
\boxed{B^{-1/2}\ \text{with}\ m=A/B}
\qquad\Longleftrightarrow\qquad
\boxed{A^{-1/2}\ \text{with}\ m=B/A}.
\]

The pairing \(B^{-1/2}\) with \(m=B/A\) is generically mismatched unless
the Legendre object itself absorbs the reciprocal Kummer gauge.

## Evidence

On the exact one-parameter slice

\[
x=2\lambda,\qquad y=\lambda,\qquad z=1,
\qquad E=3\lambda+1,
\]

one has

\[
A=\lambda^2-1,\qquad B=9\lambda^2-1,
\]

and

\[
\mathcal Q=P(\lambda)
=35\lambda^4+12\lambda^3-70\lambda^2-36\lambda-5.
\]

The exact signs and derivative are

\[
P(1)=-64,\qquad P(2)=299,
\qquad P'(\lambda)=(\lambda^2-1)(140\lambda+36).
\]

Hence there is a unique simple root
\(\lambda_0\in(1,2)\), numerically
\(\lambda_0\simeq1.4961158568539643\).  At that root,

\[
A>0,\quad B>0,\quad
E^2-x^2=5\lambda_0^2+6\lambda_0+1>0,
\]

\[
E^2-y^2=8\lambda_0^2+6\lambda_0+1>0,
\quad
H=E^2(4\lambda_0^2+6\lambda_0+2)+4\lambda_0^4>0.
\]

Thus the root is transverse to \(\mathcal Q=0\) and lies off every factor
in the determinant certificate and off the soft loci.

The exact checker also reproduces both Gysin-kernel rows of entry 150 and
the Legendre normalization test.  For the coefficient of the published
second-order operator it finds

\[
p_{L_2}=\frac{5AB+2(A+B)}{\lambda AB}.
\]

Both \(B^{-1/2}u(A/B)\) and \(A^{-1/2}u(B/A)\) yield this coefficient,
whereas \(B^{-1/2}u(B/A)\) yields

\[
p_{\rm trial}=\frac{5AB+4A}{\lambda AB},
\qquad
\operatorname{num}(p_{\rm trial}-p_{L_2})=2(A-B).
\]

Checker:

`research/benincasa/check_q_smoothness_and_legendre_normalization.py`

SHA-256:

`a04cc6b13316b3c9ef0224b1b764a28fd4983082f703a24a72d9fff75148017b`

Exact reproduction command from the repository root:

```powershell
python research/benincasa/check_q_smoothness_and_legendre_normalization.py
```

The run returns `status: proved_exact_identities`; all compactification,
slice, Gysin-kernel, and Legendre-normalization assertions are true.

Delegated hostile-review run
`run-6df80d7837274f81b979c4550d0e7f13` ended with
`worker_runtime_timed_out:max_run_ms=300000`, `completion_state: absent`,
and no scientific packet.  That failed delegated review is not evidence;
the conclusion above rests on the exact repository checker and the displayed
certificate.

## Boundary

The falsifier is absolute, generic, and coefficient-level.  It does not
compute the unpublished \(L_1\), identify a marked integration cycle, or
locate \(\mathcal Q\) in a relative extension class.  It makes no claim at
resonant, discriminant, or soft kinematics and no claim about entry 151's
independent Alexander--Tate butterfly.

Entry 150 survives in its stated generic de Rham scope.  In particular, the
explicit rank-two infinity-Gysin quotient, the final-block kernel
\(\langle e_6,v_{\rm alg}\rangle\), and the global rank-seven kernel are
unchanged.  The checker independently confirms
\(R_\infty(v_{\rm alg})=0\) in both rows.

The evidence does not exclude \(\mathcal Q\)-support created by a frozen
marked divisor, relative chain, or extension class.  Moving \(\mathcal Q\)
there is a strictly smaller replacement hypothesis, not a repair or success
of M2.25.  No new carrier divisor, fitted splitting, altered \(\mathcal Q\),
or post hoc half-integral gauge is admitted.

## Consequence

The entry-152 assertion

\[
\mathcal L_{\rm alg}\simeq
\mathcal K_{\sqrt{-\mathcal Q}}(-1)
\]

is false as an absolute algebraic-kernel statement: its predicted \(-1\)
monodromy conflicts with the trivial monodromy forced by smooth absolute
extension, and rational gauge cannot remove the half residue modulo
integers.

The entry-150 sequence remains the fixed input,

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\xrightarrow{R_\infty}\mathbb V_{\rm ell}(-1)
\longrightarrow0,
\]

with no change to its quotient or kernel.  The surviving smaller question
is whether factorization-marked relative or extension data, absent from the
absolute pair, acquire \(\mathcal Q\)-support.

The next falsifier is the frozen marked-relative collision/resultant test:
freeze the marked divisor or relative boundary, extension sequence,
normalization, and prohibited repairs before computation, then test whether
its collision/resultant support is exactly \(\mathcal Q=0\).  Failure ends
that replacement hypothesis; agreement advances it only in the frozen
marked-relative sector.  There are no post hoc repairs.
