# Master integral parity-cohomology theorem

## Scope

Fix:

- a grade `g>=2`;
- any finite admitted depth set `A subset 2*Z_{>=0}`;
- any finite Laurent source interval `I=[m_min,m_max] cap Z`;
- the full target lattice after clearing the common denominator.

This is an engine-side theorem.  It does not assert that a physical source
constructs these Laurent states or that a physical target retains the full
Laurent target.

## I. Complete parity kernels

For every visible depth `a in A`, define

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)}.
\]

At grade two define

\[
E_1^-=1-\bar z^{-2},
\qquad
E_2^-=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6},
\]

and their electric partners

\[
E_1^+=1+\bar z^{-2},
\qquad
E_2^+=\bar z^{-8}+3z^{-4}\bar z^2-2z^{-6}.
\]

Only classes whose complete source supports lie in `A x I` are visible.  Then

\[
\boxed{
\ker M_g
=\bigoplus_{a\in A\text{ visible}}\mathbb QD_{g,a}
\oplus\langle E_1^-\rangle^{v_1}
\oplus\langle E_2^-\rangle^{v_2},
}
\]

\[
\boxed{
\ker E_g
=\langle E_1^+\rangle^{v_1}
\oplus\langle E_2^+\rangle^{v_2}.
}
\]

Both exceptional indicators vanish unless `g=2`; `v_1` also requires
`0 in A` and Laurent support `{-2,0}`, while `v_2` requires
`{0,4,6} subset A` and support `{-8,0,2}`.

Towers are structural absence of the odd port on reflection-fixed orbits.
The two exceptional families are alignment circuits among nonzero columns.
There are no other kernel classes and no source-cutoff artifacts.

## II. Transport and complementary parity reconstruction

Folded mixed-derivative transport is injective:

\[
J_g(D)=(A_D,B_D),
\qquad\ker J_g=0.
\]

The character readouts

\[
E=A+B,
\qquad M=A-B
\]

have the half-Hadamard inverse.  Therefore

\[
\boxed{\ker E_g\cap\ker M_g=0.}
\]

Moreover `E` is injective on `ker M`, and `M` is injective on `ker E`.
Every single-port kernel class is rerouted into the complementary character
channel; it is not erased by transport.

## III. Closedness and logarithmic normal form

The folded one-form

\[
F_g(D)=f_D\,dz+\bar f_D\,d\bar z
\]

satisfies

\[
dF_g(D)=-M_g(D)\,dz\wedge d\bar z.
\]

Thus the magnetic kernel is precisely the folded closed sector.

For a tower, write `u=z*bar(z)` and

\[
T_s=\partial_u+\frac{2s}{1+u},
\qquad L_g=T_{g+1}\cdots T_2.
\]

The covariant chain radializes exactly:

\[
F_g(D_{g,a})=L_gu^{-a}\,du.
\]

For every positive admitted even depth,

\[
\boxed{
F_g(D_{g,a})=d\Phi_{g,a}+r_{g,a}\eta,
}
\]

\[
\eta=d\log\frac{u}{1+u},
\qquad
r_{g,a}=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

The only logarithmic residues are `r_{g,a}` at `u=0` and `-r_{g,a}` at
`u=-1`; the residue at infinity vanishes.

## IV. Complete rational-exact classification

The depth-zero tower and both magnetic exceptional circuits are
rational-exact.  Let `T` be the visible positive-depth set.  An arbitrary
magnetic kernel vector

\[
D=c_0D_{g,0}+\sum_{a\in T}c_aD_{g,a}
+e_1E_1^-+e_2E_2^-
\]

is rational-exact if and only if

\[
\boxed{\sum_{a\in T}c_ar_{g,a}=0.}
\]

Consequently

\[
\boxed{
\dim(\ker M_g/K_g^{rat})=\mathbf1_{T\ne\varnothing}.
}
\]

All positive-depth towers are representatives of one ordinary rational
cohomology line, not independent depthwise lines.  A depth-labelled residue
associated grade is a different typed object.

## V. Integral augmentation and Smith form

On the integral tower lattice,

\[
\rho_{g,T}:\bigoplus_{a\in T}\mathbb ZD_{g,a}
\longrightarrow\mathbb Z\eta,
\qquad D_{g,a}\mapsto r_{g,a}\eta.
\]

Let

\[
d_{g,T}=\gcd_{a\in T}|r_{g,a}|.
\]

Sequential Bezout reduction constructs `U in GL_|T|(Z)` with

\[
(r_{g,a})_{a\in T}U=(d_{g,T},0,\ldots,0).
\]

The final columns of `U` are a saturated integral basis of the rational-exact
tower relations.  Hence

\[
\operatorname{SNF}(\rho_{g,T})=(d_{g,T},0,\ldots,0),
\]

\[
L_T/\ker\rho_{g,T}\simeq d_{g,T}\mathbb Z\eta\simeq\mathbb Z.
\]

The quotient is free.  Torsion occurs only in the ambient accessibility
cokernel

\[
\mathbb Z\eta/d_{g,T}\mathbb Z\eta
\simeq\mathbb Z/d_{g,T}\mathbb Z.
\]

Pairwise primitive circuits need not generate this saturated kernel; the
grade-three row `(10,21,36)` gives an index-five counterexample.

## VI. Stable arithmetic law

For `n=g-1`, the fixed divisor on all positive even depths is

\[
\delta_n
=\gcd_{a\in2\mathbb Z_{>0}}a^{\overline n}
=\begin{cases}
n!,&n\text{ even},\\
n!2^{\nu_2(n+1)},&n\text{ odd}.
\end{cases}
\]

Odd primes contribute exactly their valuations in `n!`; the even-depth
constructor contributes the additional 2-adic factor at odd `n`.  Therefore

\[
\boxed{
d_g^{stable}
=g(g+1)C_{g+1}(g-1)!
\begin{cases}
1,&g\text{ odd},\\
2^{\nu_2(g)},&g\text{ even}.
\end{cases}}
\]

## VII. Exact cutoffs

Let `S_g(A)` be the union of all Laurent exponents in the admitted named
supports.  Every predicted class is visible exactly when

\[
m_{min}\le\min S_g(A),
\qquad
m_{max}\ge\max S_g(A).
\]

The rational quotient activates exactly when at least one positive tower is
visible.

The exact minimal prefix length stabilizing the infinite even-depth Smith
divisor is

\[
s_g=\min\left\{s:\gcd_{1\le j\le s}
\frac{(2j)^{\overline{g-1}}}{\delta_{g-1}}=1\right\},
\qquad s_g\le g.
\]

Its exact Laurent hull is

\[
-(g+2s_g-1)\le m\le-(g+1).
\]

The uniform sufficient lower bound is `m_min<=-(3g-1)`.

## VIII. Naturality

At fixed grade, depth and Laurent inclusions preserve every old sparse column.
Fold transport, parity reconstruction, closedness, exactness, and residue
augmentation commute with these inclusions.  Integral residue images nest by

\[
d_{g,T'}\mid d_{g,T}\qquad(T\subset T').
\]

Coordinate deletion is not a map on kernels: removing one vertex of a circuit
destroys the relation.  Naturality is covariant under source inclusion, not
contravariant under arbitrary projection.

## IX. Constructor and target boundary

Only finite subsets of the nonnegative even constructor inherit this theorem.

- Isolated odd or shifted congruence lanes are algebraically defined but lack
  an unbounded kernel theorem and source authorization.
- The all-integer constructor is nonconservative: at grade two and depths
  `{0,4,5}`, two new mixed-parity circuits occur.
- Fractional/cyclic-cover constructors require the full pulled-back operator,
  deck representations, and equivariant descent data.  The virtual values
  `q=35/3,55/3` fail ordinary scalar descent on every finite cyclic cover.
- Target truncation can create new kernels; it is a different operator.

## X. Failure taxonomy

\[
\begin{array}{c|c|c}
\text{class}&\text{mechanism}&\text{witness}\\
\hline
\text{tower}&\text{fixed-orbit odd-port absence}&D_{g,a}\\
\text{local parity circuit}&\text{free-orbit alignment defect}&E_1,E_2\\
\text{global residue circuit}&\ker\rho_g&\text{Bezout/Smith vector}\\
\text{chart failure}&\text{one Plucker coordinate vanishes}&\text{surviving atlas chart}\\
\text{transport loss}&\ker J_g&\text{excluded}\\
\text{target loss}&\text{postcomposition truncation}&\text{explicit rank-drop falsifier}\\
\text{physical loss}&\text{physical source/readout map}&\text{not presently typed}
\end{array}
\]

The first nonfaithful arrow, not the visual form of a null vector, determines
the meaning of each kernel.

## Evidence boundary

The unbounded quantifiers come from symbolic component transfer,
radialization, residue adjunction, Hermite reduction, Bezout/Smith reduction,
and the prime-local fixed-divisor proof.  Bounded checkers are hostile audits
of these identities and of the declared scope.  The companion evidence
manifest is `checkers/integral_parity_cohomology_master_checks.py`.
