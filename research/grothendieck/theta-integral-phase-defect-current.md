# Theta integral phase-defect current

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator proposed the following ordered interpretation:

1. the two half-planes first acquire distinct orientations;
2. projected integrality is then lost at the observed zero;
3. the oval contours become circles after correcting the angle between the
   two displayed planes.

This packet identifies the exact analytic object behind that intuition.  The
relevant integrality is the integer divisor current of the completed scalar
readout.  The ovals are local equipotential links around its atoms.

## 1. The quantized curvature measure

Let

\[
X(z)=\xi\left(\frac12+iz\right).
\]

For every nonzero entire function, the Poincare--Lelong identity in one
complex dimension gives, distributionally,

\[
\boxed{
\frac1{2\pi}\Delta\log|X(z)|
=\sum_{\rho:X(\rho)=0}m_\rho\,\delta_\rho.
}
\]

Here `m_rho` is the positive integer multiplicity of the zero.  Define this
positive integral measure as

\[
\mu_X:=\frac1{2\pi}\Delta\log|X|.
\]

It is the curvature current of the scalar phase line.  The source remains
defined at a zero; what fails is a local nonvanishing trivialization of that
line.  The failure carries the quantized charge `m_rho`.

## 2. RH as support localization

In the spectral coordinate, the critical line is the real axis.  Therefore

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\operatorname{supp}\mu_X\subseteq\mathbb R.
}
\]

Equivalently,

\[
\Delta\log|X|=0
\]

in each open half-plane.  Since each chamber is simply connected, this is
equivalent to the existence of a holomorphic logarithm of `X` there.

The operator's temporal language is thus correctly read as structural
order.  After the involution distinguishes the two open chambers, each
chamber either has zero curvature charge and admits an integral phase
trivialization, or contains an off-seam divisor atom.  Re-sewing the two
trivial chambers may leave quantized defects on their common boundary.

## 3. Why “seam-supported connection” needs current typing

An ordinary holomorphic one-form cannot be nonzero only on a boundary line.
Thus a proposed decomposition

\[
\frac{X'}X\,dz=dL+\omega_{\rm seam}
\]

cannot literally use a seam-supported holomorphic form.  The identity
theorem would force such a form to vanish.

The correctly typed statement uses the singular phase connection

\[
A=\operatorname{Im}\left(\frac{X'}X\,dz\right).
\]

Away from the divisor this connection is closed.  Its canonical current
extension has curvature

\[
dA=2\pi\mu_X,
\]

or, equivalently, the logarithmic connection is exact in each chamber while
its divisor curvature is a boundary-supported current.  This distinction
prevents a false analytic decomposition while preserving the proposed
geometry exactly.

## 4. What the ovals are circles of

Near a zero `rho` of multiplicity `m`, write

\[
X(z)=(z-\rho)^mU(z),
\qquad U(\rho)\ne0.
\]

Then

\[
\log|X(z)|
=m\log|z-\rho|+\log|U(z)|.
\]

After using the local conformal coordinate

\[
w=(z-\rho)U(z)^{1/m},
\]

the level curves are exactly

\[
|w|=\text{constant}.
\]

Hence the displayed ovals are locally distorted circles of constant
logarithmic potential, or equivalently constant residual scalar amplitude.
Their phase winds `m` times and measures the integral mass of the enclosed
divisor atom:

\[
\frac1{2\pi i}\oint\frac{X'}X\,dz=m.
\]

The “circle” is therefore a small link around a quantized curvature
defect, not a material orbit of a zero.

## 5. The boundary-modulus no-go

The new formulation exposes an exact obstruction to several tempting proof
routes.  For a point `a` in the upper half-plane, the Blaschke factor

\[
B_a(z)=\frac{z-a}{z-\bar a}
\]

satisfies

\[
|B_a(x)|=1
\qquad(x\in\mathbb R),
\]

but contains an interior zero at `a`.  Its Green potential

\[
g_a(z)=\log|B_a(z)|
\]

vanishes on the boundary while carrying an interior Laplacian atom.

Consequently, seam modulus data alone cannot distinguish a chamber with no
interior defect from one multiplied by an inner factor.  Any argument using
only `|X(x)|`, boundary subharmonicity, or a Poisson reconstruction of the
boundary modulus is incomplete.

The completed theta source must control the inner factor, equivalently the
projective phase or winding class.  This independently confirms the
operator's emphasis on meaning rather than magnitude.

## 6. Source-derived theorem target

With

\[
X(z)=F(z)+F(-z),
\qquad
F(z)=\int_0^\infty\Phi(u)e^{izu}\,du,
\]

the required theorem can now be stated without metaphor:

\[
\boxed{
\text{The modularly completed two-sheet theta Carrier induces no inner
divisor in either distinguished spectral chamber.}
}
\]

Equivalent forms are:

1. the projective ratio `F(-z)/F(z)` avoids `-1` in each chamber;
2. the scalar sum has no chamber-interior Blaschke zero factor;
3. the divisor current `mu_X` has no chamber-interior support;
4. every chamber loop has zero logarithmic winding.

These are equivalent targets.  Hermite--Biehler positivity remains a
strictly stronger sufficient construction because it controls a whole
metric region, not only the inner divisor.

## 7. Sharp next move and falsifier

After establishing the relevant bounded-type normalization, factor the
two-sheet projective transition into outer and inner data in one half-plane.
Modular sewing must be tested on the inner factor itself.  The
desired identity would show that its winding is inherited entirely from
boundary incidences and that no Blaschke generator `B_a` is admitted by the
integer theta-label sewing law.

The sharp falsifier is an admissible modular source deformation preserving
all proposed transition laws while acquiring one off-axis Blaschke pair.  If
such a deformation exists, those laws do not encode the required integral
faithfulness.

## 8. Scope

The divisor-current identity, support reformulation, local circle normal
form, and boundary-modulus no-go are standard exact consequences of complex
analysis.  The source-derived exclusion of the inner factor is the missing
RH theorem.  RH is not proved.
