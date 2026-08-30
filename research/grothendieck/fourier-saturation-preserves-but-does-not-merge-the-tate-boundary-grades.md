# Fourier saturation preserves but does not merge the Tate boundary grades

## Question

Nima's four-orbit construction makes any boundary Gramian invariant under
Fourier sewing.  Does applying it to the actual theta/Tate boundary vessel
produce one canonical Hilbert completion containing the primitive, square,
connected-tail, seam, and archimedean channels?

## The first actual finite-cutoff Gramians

Let (X) be a finite set of primes.  On one prime-label sheet, the
Mellin-analytic primitive rigging has Hilbert seminorms

\[
q_{\delta,X}(c)=\sum_{p\in X}p^{2\delta}|c_p|^2,
\qquad \delta>0.
\]

The square current occupies the unweighted Hilbert grade

\[
q_{0,X}(c)=\sum_{p\in X}|c_p|^2.
\]

Double the label space by the direct and reciprocal sheets.  In their common
source frame, write

\[
J_X=
\begin{pmatrix}
0&-I\\
I&0
\end{pmatrix},
\qquad
J_X^2=-I,
\qquad
J_X^4=I.
\]

Place each one-sheet Gramian on the direct sheet:

\[
Q_{\delta,X}=
\begin{pmatrix}
D_{\delta,X}&0\\
0&0
\end{pmatrix},
\qquad
D_{\delta,X}=\operatorname{diag}_{p\in X}(p^{2\delta}).
\]

The exact Fourier saturation is

\[
Q_{\delta,X}^{\mathrm{sat}}
=
\sum_{j=0}^{3}(J_X^j)^*Q_{\delta,X}J_X^j
=
2
\begin{pmatrix}
D_{\delta,X}&0\\
0&D_{\delta,X}
\end{pmatrix}.
\]

For the square grade this gives

\[
Q_{0,X}^{\mathrm{sat}}=2I.
\]

Thus Fourier saturation succeeds exactly.  It supplies equal direct and
reciprocal control and has trivial kernel at every finite cutoff.

## The obstruction to one Gram completion

The smallest generalized eigenvalue of the square form against the primitive
form is

\[
\lambda_{\min}
\left(
Q_{0,X}^{\mathrm{sat}},Q_{\delta,X}^{\mathrm{sat}}
\right)
=
\min_{p\in X}p^{-2\delta}.
\]

As the cutoff grows, this tends to zero.  Hence the primitive and square
forms are not uniformly equivalent.  Fourier saturation duplicates their
weights across the two sheets but does not alter the ratio between their
regularity grades.

This is source information, not bad conditioning.  The primitive current is
distributional and requires the projective Mellin-analytic family over every
δ greater than zero.  The square current is Hilbert.  The connected tail
is controlled at coefficient level by an absolute-summability seminorm,
which is not itself a single quadratic Gramian.  Seam and archimedean endpoint
functionals add further graph seminorms once their incidence maps have been
derived.

Therefore the phrase "the actual boundary Gramian" is ill-typed for the full
vessel.  The source supplies a locally convex family containing:

- the saturated primitive Hilbert scale;
- the saturated square Hilbert form;
- the saturated connected-tail absolute-summability seminorm;
- graph seminorms for the seam and archimedean boundary maps.

Fourier saturation must be applied to every member of this family.  It
produces a Fourier-invariant pro-Gram boundary topology, not one Hilbert norm.

## Constructor and cutoff audit

The two native constructors already derived from the source survive this
topology.

Mellin translation acts by

\[
(M_tc)_p=p^{it}c_p.
\]

It is isometric for every (q_{\delta,X}), including δ equal to zero, and
commutes with (J_X).  Reciprocal reflection is already represented by the
sheet action and is isometric after saturation.  Cutoff restriction from
(Y) to (X\subset Y) pulls every form back exactly to its (X)-form.

The primitive exponential current and the tempered square current are both
retained, but at different continuous dual grades.  They are not identified.
The connected tail remains a third port rather than being replaced by a
quadratic surrogate.

Finite-cutoff injectivity is automatic for the primitive and square
saturated forms.  Completion injectivity must be stated for the entire
separating seminorm family.  A single smallest Gram eigenvalue is not an
invariant of that locally convex completion.  Generalized eigenvalues between
declared grades are meaningful, and the exact calculation above proves their
floor collapses.

## Typed obstruction

The requested five-channel matrix (Q_X) cannot yet be constructed without
an unauthorized identification:

1. primitive and square channels occupy inequivalent completion grades;
2. the connected-tail port is natively absolute-summable rather than
   Hilbertian;
3. the seam and archimedean graph maps have not yet been derived on the same
   source module.

Aggregating those ports into one Euclidean block would assume the very
comparison topology under investigation.  It would also conceal whether a
boundary functional vanished only after cancellation between differently
typed channels.

## Falsifier and next construction

The pro-Gram proposal fails if an authorized constructor is discontinuous for
one saturated source seminorm, if cutoff restriction fails to commute with
saturation, or if the completed family has a nonzero common kernel.

The next admissible construction is not another finite positive matrix.  It
is the seam and archimedean incidence map into the already separated
primitive, square, and connected ports.  Once those maps exist, add their
Fourier-saturated graph seminorms to the family and test whether the common
kernel remains zero.

## Result

Fourier saturation works exactly on the real theta boundary grades, but it
preserves their distinctions.  The primitive-versus-square generalized
reserve tends to zero, and the connected port is not natively Hilbertian.
The canonical candidate is therefore a Fourier-invariant pro-Gram topology.
Any single five-channel Gram completion would presently be a lossy,
source-unauthorized collapse.
