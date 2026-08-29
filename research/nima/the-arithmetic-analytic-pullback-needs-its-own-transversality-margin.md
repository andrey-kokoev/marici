# The arithmetic-analytic pullback needs its own transversality margin

## Do not totalize before gluing

The bounded-energy completion must remain typed until arithmetic and analytic realizations are compared.

Let:

- \(L_P\) be the arithmetic restricted limit, with its frozen prime-incidence energy;
- \(L_A\) be the analytic or Mellin restricted limit, with its frozen continuation energy;
- \(L_I\) be the independently constructed seam/intersection object;
- \(r_P:L_P\to L_I\) and \(r_A:L_A\to L_I\) be authorized comparison maps.

The strictly jointly realizable object is
\[
L_P\times_{L_I}L_A
=
\{(x_P,x_A):r_Px_P=r_Ax_A\}.
\]
If residual automorphisms or higher coherence remain, replace this strict pullback by the typed homotopy pullback. The residual equivalences must not be silently quotiented away.

## Difference operator

Define
\[
D:L_P\oplus L_A\longrightarrow L_I,
\qquad
D(x_P,x_A)=r_Px_P-r_Ax_A.
\]
Then the pullback is \(\ker D\).

Let \(G_D\subseteq\ker D\) be the authorized gluing gauge. Stable gluing requires more than closedness of \(\ker D\): on the orthogonal complement of the kernel or gauge-adjusted solution space, seek
\[
\|D(x_P,x_A)\|_{L_I}
\ge
\delta_{\mathrm{glue}}
\operatorname{dist}\big((x_P,x_A),\ker D\big).
\]
Equivalently, the smallest positive singular value of \(D\) must be uniformly bounded below.

This is the inf-sup constant for correcting a seam mismatch. It controls the norm of the gluing inverse or pseudoinverse.

## Three independent margins

The completed instrument requires three typed quantitative gates:

1. arithmetic observability:
   \[
   \delta_P>0;
   \]
2. analytic/Mellin observability:
   \[
   \delta_A>0;
   \]
3. mutual-coherence or seam transversality:
   \[
   \delta_{\mathrm{glue}}>0.
   \]

All three must be uniform over cutoff and compact \(s\)-sets. A total norm can conceal failure of the third because a strongly observed arithmetic or analytic component can dominate the sum while the incidence images become tangent.

Therefore the total Green energy may be formed only after the triple
\[
(\delta_P,\delta_A,\delta_{\mathrm{glue}})
\]
has been retained as typed evidence.

## Friedrichs-angle form

Let
\[
M_P=\overline{\operatorname{ran}r_P},
\qquad
M_A=\overline{\operatorname{ran}r_A}
\]
inside \(L_I\). After removing their authorized common part, the Friedrichs angle \(\theta\) satisfies
\[
\cos\theta
=
\sup
\{|\langle u,v\rangle|:
u\in M_P\ominus(M_P\cap M_A),
v\in M_A\ominus(M_P\cap M_A),
\|u\|=\|v\|=1\}.
\]
Stable gluing requires
\[
\sin\theta\ge\delta_{\angle}>0.
\]
This is equivalent, under the closed-range hypotheses, to a positive lower singular bound for the difference map.

The assembled Green residual is naturally interpreted as the component measuring failure of arithmetic and analytic incidence images to coincide transversely at the seam.

## Hostile family: exact finite pullbacks with tangency

Take \(L_I=\mathbb R^2\). For cutoff \(m\), let
\[
M_{P,m}=\operatorname{span}(e_1),
\qquad
M_{A,m}=\operatorname{span}
(\cos\theta_m\,e_1+\sin\theta_m\,e_2),
\]
where \(\theta_m\downarrow0\).

Let both source coplanes be one-dimensional and map isometrically onto these lines. Each channel is internally complete and perfectly conditioned:
\[
\delta_{P,m}=\delta_{A,m}=1.
\]
For every finite \(m\), the difference map has an exact kernel and closed range. Yet its smallest positive singular value is comparable to
\[
\sin\theta_m\to0.
\]
A normalized antisymmetric pair produces a seam mismatch tending to zero, while the correction norm diverges.

Thus every finite pullback is exact, but completion loses mutual-coherence observability. No invisible vector need exist at finite cutoff.

## Homotopy-pullback correction

When seam matching is defined only up to a residual automorphism groupoid \(\mathcal G_I\), an object consists of
\[
(x_P,x_A,\gamma),
\qquad
\gamma:r_Px_P\overset{\sim}{\longrightarrow}r_Ax_A.
\]
Linearization introduces both the difference operator and the infinitesimal gauge action. The relevant margin is then the smallest positive singular value of the resulting two-term deformation complex after quotienting authorized gauge.

Hence the strict \(D\)-margin is the zero-automorphism control, not the final statement in the presence of clutching symmetries.

## Relation to the Green lift

The earlier assembled feature lift
\[
S_s=J_s^*\Lambda_s
\]
must now be resolved into typed arithmetic, analytic, and seam components. Separate bounded lifts prove only \(\delta_P,\delta_A>0\). They do not prove the assembled identity because the seam comparison may become tangent.

The complete Green residual should therefore be tested as the Schur complement of the seam comparison block. Its positivity or coercivity must dominate the mismatch direction with constant controlled by \(\delta_{\mathrm{glue}}\), rather than by the total channel norm.

## Next finite-cutoff calculation

For each cutoff and \(s\):

1. construct \(L_{P,X}(s)\), \(L_{A,X}(s)\), and \(L_{I,X}(s)\) independently;
2. construct \(r_{P,X}(s)\) and \(r_{A,X}(s)\) from source incidence;
3. remove authorized common gauge;
4. compute the least positive singular value of
   \[
   D_X(s)=r_{P,X}(s)-r_{A,X}(s);
   \]
5. compare it with the smallest Friedrichs angle;
6. retain \(\delta_P,\delta_A,\delta_{\mathrm{glue}}\) separately;
7. only then form the total Green energy and Birman–Schwinger pencil.

A collapse of \(\delta_{\mathrm{glue}}\) with stable internal margins identifies the missing assembled Green residual exactly: arithmetic and analytic completions remain valid in isolation but fail to meet transversely.
