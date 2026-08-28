# Weyl Phase Rigidity Does Not Confine Theta Cross-Transfer Zeros

## Source typing

The self-adjoint logarithmic transport has two independently typed rigged
ports:

\[
b_f=\Phi,
\qquad
b_0=\delta_0.
\]

For the causal resolvent $R_z$, the theta scalar is the cross-transfer

\[
X(z)=\langle b_f,R_zb_0\rangle
\]

up to the fixed nowhere-zero normalization.  The full two-port Weyl matrix
also contains both diagonal self-energies and the reciprocal cross-transfer:

\[
W(z)=A_\partial(z)-
\begin{pmatrix}
\langle b_f,R_zb_f\rangle&\langle b_f,R_zb_0\rangle\\
\langle b_0,R_zb_f\rangle&\langle b_0,R_zb_0\rangle
\end{pmatrix}.
\]

Consequently $X$ is one matrix coordinate of $W$, not its determinant.

## What full Weyl compatibility supplies

If two boundary selectors intertwine an irreducible clock-shift Weyl pair,
their relative transformation commutes with both generators and is therefore
scalar.  Fixing the normalized theta distribution removes that scalar.

This proves uniqueness of an admitted phase frame, conditional on the source
establishing the full intertwining requirement.  It does not relate a
cross-transfer minor to the determinant of the full boundary matrix.

## Universal finite hostile

Let $F(z)$ be any analytic scalar with the required real structure and put

\[
F^\sharp(z)=\overline{F(\overline z)}.
\]

The matrix family

\[
M_F(z)=
\begin{pmatrix}
1&F(z)\\
F^\sharp(z)&1+F(z)F^\sharp(z)
\end{pmatrix}
\]

satisfies

\[
\det M_F(z)=1.
\]

Its full determinant is everywhere invertible while its upper-right
cross-transfer has exactly the arbitrary zero divisor of $F$.  Freezing the
basis and its phase does not change this fact.

Thus none of the following confines cross-transfer zeros:

- invertibility of the full two-port matrix;
- determinant normalization;
- reciprocal real structure;
- uniqueness of the port frame;
- scalarity of the simultaneous Weyl commutant.

## Exteriorization gate

A Weyl route can affect the theta divisor only if the source provides an
additional relation such as

\[
X(z)=u(z)\det W(z),
\qquad
u(z)\ne0,
\]

or realizes $X$ as a canonical exterior section whose vanishing is a rank
defect of the complete boundary object.  No such relation follows from phase
rigidity.

This is a rank or Pluecker theorem, not another normalization theorem.  It
must be derived before inspecting the zero set.  Otherwise replacing the
cross-transfer by a determinant changes the divisor.

## Reciprocal quotient after phase selection

Phase selection is also insufficient after reciprocal completion.  A
palindromic packet is already equal to its reciprocal reverse, so every
reversal-odd phase port vanishes.  Nevertheless such a packet can have
off-unit reciprocal zero pairs.

For an even reciprocal polynomial,

\[
P(w)=w^mQ(y),
\qquad
y=w+w^{-1}.
\]

The unit circle descends to $y\in[-2,2]$.  Zero confinement is therefore
equivalent to interval hyperbolicity of $Q$: every root must be real and
belong to that interval.

The smallest positive palindromic hostile is

\[
P(w)=w^4+4w^3+4w+1,
\qquad
Q(y)=y^2+4y-2.
\]

It has no reversal-phase ambiguity, but one quotient root lies below $-2$.
This rejects any route that ends after selecting a reciprocal phase frame.

## Minimal operator certificate for the next route

For a finite monic quotient $Q_X$, interval hyperbolicity would follow from
a source-derived self-adjoint contraction $J_X$ satisfying

\[
Q_X(y)=\det(yI-J_X),
\qquad
\lVert J_X\rVert\le2.
\]

Constructing $J_X$ backward from the roots or from $Q_X$ is circular.  It
must be the compression of an independently defined source transport, and
its determinant identity must hold before zero inspection.

The degree-two hostile already has a finite norm obstruction.  If both roots
of $Q(y)=y^2+4y-2$ belonged to $[-2,2]$, their sum $-4$ would force both
to equal $-2$, contradicting their product $-2$.  Hence no self-adjoint
matrix with norm at most two can have this characteristic polynomial.

## Disposition

The phase-bearing Weyl module repairs spectral-factor ambiguity but does not
provide zero confinement.  The live alternatives are now narrower:

1. derive a source exteriorization turning the theta cross-transfer into a
   characteristic section;
2. derive a source quotient operator whose spectrum is confined to the
   physical interval;
3. close the Weyl phase route if neither constructor exists independently of
   the scalar theta divisor.

## Source-local quotient operator

The bilateral valuation module already contains the finite-interval operator
required by the second alternative.  For each prime $p$, reciprocal
completion gives a unitary shift

\[
U_pe_j=e_{j+1},
\qquad
U_p^*=U_p^{-1}.
\]

The reflection-invariant quotient operator is

\[
Y_p=U_p+U_p^*.
\]

It is self-adjoint and satisfies

\[
\lVert Y_p\rVert=2,
\qquad
\operatorname{spec}(Y_p)=[-2,2].
\]

Under a scalar valuation character $U_p\mapsto w$, its readout is exactly

\[
Y_p\mapsto w+w^{-1}.
\]

Thus reciprocal descent and the physical quotient interval are already
source-derived on every local valuation chain.  The palindromic hostile is
rejected by any characteristic-section realization of $Y_p$.

## Global typing obstruction

Different primes do not share one scalar quotient coordinate.  At centered
spectral parameter $z$, their characters are

\[
w_p=p^{-z},
\qquad
y_p=p^{-z}+p^z=2\cosh(z\log p).
\]

The natural global object is therefore a commuting family or joint spectrum

\[
(Y_p)_p,
\]

not one bounded operator $Y$.  On the seam, every $w_p$ is unimodular and
every $y_p$ belongs to $[-2,2]$.  Off the seam, the same one-parameter
spectral character leaves this joint real cube.

The remaining bridge is now exact: construct the completed theta boundary
section as a source-authorized joint characteristic or exterior section of
the family $(Y_p)_p$, including its archimedean member.  Local interval
spectra alone do not constrain zeros of an arbitrary joint matrix
coefficient.

The first global falsifier is a section on the joint valuation module that
preserves every local $Y_p$, reciprocal reflection, and normalized vacuum,
but differs from the theta cross-transfer by a nonvanishing-frame-compatible
off-torus factor.  If such a section is source-admissible, the declared joint
constructor list cannot orient the divisor.

## Bordered exteriorization is canonical but formal

The one-prime bordered colligation makes the exteriorization issue explicit.
On a finite valuation chain, let $S_N$ be the truncated shift, $e_0$ its
source vector, and $\ell_N(e_k)=1$ its augmentation.  Put

\[
A_N(q)=I-qS_N.
\]

Since $S_N$ is nilpotent,

\[
\det A_N(q)=1.
\]

Its source transfer is

\[
g_N(q)=\ell_NA_N(q)^{-1}e_0
=\sum_{k=0}^Nq^k.
\]

Adjoin the input and output borders:

\[
\mathcal R_N(q)=
\begin{pmatrix}
A_N(q)&e_0\\
\ell_N&0
\end{pmatrix}.
\]

The Schur determinant identity gives

\[
\det\mathcal R_N(q)=-g_N(q).
\]

Thus the cross-transfer is exactly a characteristic section of the bordered
system.  Its finite roots are the nontrivial $(N+1)$-st roots of unity.

However, the construction is universal.  Whenever an invertible bulk block
$A$ realizes a scalar transfer $F=CA^{-1}B$, the bordered matrix

\[
\begin{pmatrix}
A&B\\
C&0
\end{pmatrix}
\]

has determinant equal to $-\det(A)F$.  It exteriorizes any scalar divisor.
Therefore bordered exteriorization by itself adds no zero-confining force.

The one-prime roots also belong to the finite valuation carrier, not to the
completed zeta section.  Under the actual Euler scaling, their spectral line
and their zero-versus-pole incidence must be retained before reciprocal and
archimedean completion.  Treating them as candidate zeta zeros would confuse
a presentation determinant with the completed section.

## Strengthened global gate

The required global construction must provide more than a determinant
identity.  It must establish, from the crossed-product source, a metric law
for the complete bordered operator that survives restricted-product and
archimedean completion.  At minimum it must specify:

1. the common domain of the scale generator and every valuation shift;
2. the primitive and terminal boundary defects;
3. zero-versus-pole incidence of every local determinant factor;
4. the global relative determinant normalization;
5. a self-adjoint, unitary, or interval-stable quotient law applying to the
   completed bordered section rather than only to each local carrier.

Without the fifth item, the crossed product proves exact arithmetic
provenance but does not orient the completed divisor.
