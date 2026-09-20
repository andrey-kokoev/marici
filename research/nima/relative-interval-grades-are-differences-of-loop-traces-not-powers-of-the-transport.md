# Relative interval grades are differences of loop traces, not powers of the transport

## Question

Does the interval-compression constructor fail only at source identification, or has it also assigned the wrong low grades to a relative arrow?

Active SCC obligation: attachment transport and route/coherencer compatibility on the fixed finite determinant-unit stratum. The candidate is a relative determinant packet of two source compressions, not an assertion that the Evans comparison has been constructed.

## Conjecture, rivals, and source operation

Conjecture: relative low grades are differences of source trace powers. Powers of the relative transport are a competing construction and need not have the required orientation law. A moment-fitted spectrum is excluded: retain the same independently declared finite matrix C, labelled prefix projections P_m, and coupling lambda as in the predecessor constructor.

Write

\[
A_m=\lambda P_mCP_m,\qquad F_m=I+A_m,
\qquad K_{m,n}=F_m^{-1}F_n-I.
\]

The domain consists of cuts with invertible F_m on one retained carrier. No limit or source-state quotient is used. The oriented relative object is the pair (A_n,A_m), retaining both operators, rather than the single difference A_n-A_m. Cut dependence is explicit; compatibility with changes of the ambient carrier is unproved.

## Constructor and grading

Define the relative coordinates

\[
J_k(m,n)=\frac1k\left(\operatorname{Tr}A_n^k-\operatorname{Tr}A_m^k\right),
\qquad
D_3(m,n)=\frac{\det_3(I+A_n)}{\det_3(I+A_m)}.
\]

These are derived from the retained source operators. They are not yet identified with the named endpoint–Euler currents. The formal spectral parameter z distinguishes perturbation degree from interval extent:

\[
\log\frac{\det(I+zA_n)}{\det(I+zA_m)}
=\sum_{k\ge1}(-1)^{k+1}z^kJ_k(m,n).
\]

This is a formal series at z=0, not a globally selected logarithm. At z=1, where the two factors are units,

\[
\frac{\det F_n}{\det F_m}
=D_3(m,n)\exp(J_1(m,n)-J_2(m,n)).
\]

At line level use the target determinant line tensored with the dual source line. Contraction of the middle line supplies composition. The scalar ratios above are its coordinates in the declared common frames, not an additional source constructor.

## Composition, orientation, and anomaly

Differences telescope, so

\[
J_k(m,r)=J_k(m,n)+J_k(n,r),
\qquad D_3(m,r)=D_3(m,n)D_3(n,r).
\]

Reversal negates each J_k and inverts D_3. Thus signed cut comparisons are coherent on this relative packet.

The bare det3 of the transport K is a different coordinate. With

\[
r(A)=-\operatorname{Tr}A+\tfrac12\operatorname{Tr}A^2,
\]

define

\[
\gamma(m,n)=r(A_n)-r(A_m)-r(K_{m,n}).
\]

Since A_n=A_m star K_mn in the plus convention,

\[
\gamma(m,n)=\alpha_3(A_m,K_{m,n}),\qquad
D_3(m,n)=e^{\gamma(m,n)}\det_3(I+K_{m,n}).
\]

The correction is source-derived, not fitted. Its composition law is

\[
\gamma(m,r)=\gamma(m,n)+\gamma(n,r)
-\alpha_3(K_{m,n},K_{n,r}).
\]

This explains why strict composition of the relative packet coexists with the nonzero multiplicative anomaly of the single relative operator. No extra triangle scalar is introduced.

## Finite falsification and boundary loops

Use six labels, C_ii=1/5 and C_ij=1/4 for nearest neighbours, with all other entries zero and lambda=1. The exact checker compares all cut triples. Ten checks pass, including a deliberate failure of the rival grading:

\[
\tfrac12\operatorname{Tr}K_{1,2}^2
+\tfrac12\operatorname{Tr}K_{2,1}^2
=\frac{88122173}{728642400}\ne0.
\]

An oriented additive square current must instead change sign. Thus half the square trace of K cannot simply be called that current.

The relative square grade gives

\[
J_2(1,2)=\frac{33}{400}
=\frac1{50}+\frac1{16}.
\]

The first term is the newly included diagonal contribution. The second is the loop crossing between old and new labels. In general the source formula

\[
\operatorname{Tr}(P_mCP_m)^k
=\sum_{i_1,\ldots,i_k<m}
C_{i_1i_2}\cdots C_{i_ki_1}
\]

shows what must be retained: relative traces count loops admitted by one cut and absent at the other. They are not merely traces of an isolated added interval. The checker also detects a cross-boundary cubic contribution. This supplies explicit connected data from C, rather than reconstructing it from the low moments.

## Disposition and surviving scope

Constructed: relative determinant grades of finite source compressions, with oriented cut transport, composition, cross-boundary loops, and the exact anomaly correction connecting them to the earlier K-based packet. This is a finite relative determinant identity.

Rejected: identifying additive square endpoint data directly with half the square trace of the relative transport without a comparison correction.

The endpoint source bridge remains absent. For the independently retained endpoint fixture g(j)=j, the corrected primitive grade from 0 to 1 is 1/5, not 1; the residual is -4/5. This does not refute a theta-specific identity not represented by this rational model. It does prove that the constructor alone supplies no such identity.

The remaining source obligation is to compare the full-state interval endpoint grades with these relative loop traces on the same admitted source carrier. Merely replacing arbitrary frames by compression, or correcting the relative grading, does not provide that comparison. Reciprocal dagger transport, prime-ratio identification, archimedean sewing, completion topology and full-packet noncollapse remain unproved; ordinary arrow reversal supplies none of them automatically.

Verification: `research/nima/checkers/check_relative_interval_determinant_grades.py`, exit 0; result `research/nima/results/relative-interval-determinant-grades.json`. The predecessor is `interval-compression-constructs-determinant-transport-but-not-the-endpoint-comparison.md`.
