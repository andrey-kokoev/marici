# Theta cubic prime-route cocycle

Status: live arithmetic-transport packet.

## 1. Bounded question

Prime-power valuation routes are translated completed theta sources:

\[
 M_d(u)=d^{-1/2}\Phi(u+\log d).
\]

Their mixed bilinear scores reconstruct the divisibility-resolved companion
matrix.  This packet asks how translation interacts with the physical radial
score operator

\[
 D_0f(u)=\frac{f'(u)}u.                                \tag{1}
\]

## 2. Translation produces an exact shear

Let

\[
 (T_af)(u)=f(u+a),
 \qquad a\ge0.
\]

Then

\[
\boxed{
 D_0T_a
 =J_aT_aD_0,
 \qquad
 J_a(u)=\frac{u+a}{u}.
}                                                       \tag{2}
\]

Equivalently,

\[
 [D_0,T_a]f(u)
 =\frac{a}{u(u+a)}f'(u+a).                             \tag{3}
\]

Thus arithmetic scale transport is not score-equivariant.  It carries a
source-fixed boundary shear determined solely by the displacement of the
physical origin.

## 3. The shear is a multiplicative cocycle

Successive translations satisfy

\[
\boxed{
 J_{a+b}(u)=J_a(u)J_b(u+a).
}                                                       \tag{4}
\]

Indeed,

\[
 \frac{u+a}{u}\frac{u+a+b}{u+a}
 =\frac{u+a+b}{u}.
\]

Therefore the score defect is coherent under prime multiplication.  If

\[
 a=\log d,
 \qquad b=\log e,
\]

then the route for \(de\) carries exactly the composite shear of the routes
for \(d\) and \(e\).  No correction is fitted after composition.

## 4. Exact mixed-route companion formula

For

\[
 a=\log d,
 \qquad b=\log e,
 \qquad c=(de)^{-1/2},
\]

bilinearity gives

\[
\boxed{
\begin{aligned}
 \mathscr B[M_d,M_e](u,v)
 =c\bigg[&
  \frac{v+b}{v}
  \frac{\Phi(u+a)\Phi'(v+b)}{v+b}\\
 &-
  \frac{u+a}{u}
  \frac{\Phi'(u+a)\Phi(v+b)}{u+a}
 \bigg].
\end{aligned}
}                                                       \tag{5}
\]

Let

\[
 \mathscr B_\Phi(U,V)
 =\frac{\Phi(U)\Phi'(V)}V
  -\frac{\Phi'(U)\Phi(V)}U.
\]

Then (5) separates into translated bulk plus two cocycle currents:

\[
\boxed{
\begin{aligned}
 \mathscr B[M_d,M_e](u,v)
 =c\bigg[&\mathscr B_\Phi(u+a,v+b)\\
 &+\frac b v\frac{\Phi(u+a)\Phi'(v+b)}{v+b}\\
 &-\frac a u\frac{\Phi'(u+a)\Phi(v+b)}{u+a}
 \bigg].
\end{aligned}
}                                                       \tag{6}
\]

The two extra terms are the exact arithmetic boundary shear.  They are the
mixed-route analogue of the rank-two seam residue found in divisibility
coordinates.

## 5. Physical route and contextual routes

For the physical route \(d=e=1\), one has \(a=b=0\), so both cocycle currents
vanish and

\[
 \mathscr B[M_1,M_1]=\mathscr B_\Phi.                  \tag{7}
\]

For nontrivial divisibility routes the currents are unavoidable.  Therefore
a raw mixed prime score is not simply a translated physical companion.  It
contains background shear caused by measuring the translated packet against
the unshifted physical radial origin.

This is the exact theta version of the contact-normal warning:

\[
\boxed{
 \text{translated coefficient route}
 \ne
 \text{translated physical score};
 \quad
 \text{the difference is the cocycle current.}
}                                                       \tag{8}
\]

## 6. Cocycle-covariant score

On the translated local chart, define

\[
 \widetilde D_ag(u)=\frac{g'(u)}{u+a}.                 \tag{9}
\]

Then translation is exactly covariant:

\[
\boxed{
 \widetilde D_aT_a=T_aD_0.
}                                                       \tag{10}
\]

Thus the shear appears only when a translated route is read using the
unshifted physical score.  Retaining the chart base removes the cocycle, but
different prime routes then land in different score fibers.

The faithful coefficient object is consequently a bundle of based score
charts, with transition function \(J_a\).  The physical scalar readout lives
only in the zero-based fiber.

## 7. Orientation consequence

The translated bulk \(\mathscr B_\Phi(u+a,v+b)\) inherits the completed
source's orientation only when its two arguments are compared in a common
based chart.  The physical mixed-route score instead includes unequal shears
\(J_a(u),J_b(v)\).  Positivity of the bulk therefore does not imply positivity
of each contextual matrix entry.

Möbius reconstruction remains faithful because it retains the currents and
inverts the complete mixed scores.  But any positivity argument must either:

1. work covariantly in the based-score bundle and derive the physical sewing
   map back to the zero fiber; or
2. retain the two explicit cocycle currents throughout the scalar estimate.

Discarding them would reconstruct the wrong coefficient packet.

## 8. Sharp next theorem and falsifier

The source-derived theorem target is a cocycle-covariant polarization law:

\[
\boxed{
 \text{Does modular sewing of the based score bundle orient the physical
 all-ones contraction while cancelling every prime-route shear current?}
}                                                       \tag{11}
\]

The cheapest falsifier is a closed prime-route composition whose cocycle
product disagrees with (4).  That cannot occur algebraically.  The substantive
falsifier is an oriented bulk packet whose zero-fiber sewing becomes
indefinite after the exact currents in (6) are restored.

This packet establishes the coefficient transport law only.  It does not
assert positivity of the sewn physical moment readout.

## 9. The prime-route cocycle is a coboundary in the open chamber

Put

\[
 h(u)=u.
\]

Then

\[
\boxed{
 J_a(u)=\frac{h(u+a)}{h(u)}.
}                                                       \tag{12}
\]

Thus the multiplicative cocycle is cohomologically trivial wherever
\(u>0\).  The gauge-transformed score

\[
\boxed{
 \widehat Df(u):=h(u)D_0f(u)=f'(u)
}                                                       \tag{13}
\]

commutes with translation:

\[
\boxed{
 \widehat DT_a=T_a\widehat D.
}                                                       \tag{14}
\]

Therefore the prime-route shear has zero bulk curvature.  It is entirely an
artifact of expressing ordinary derivative transport through the radial
score frame \(1/u\).

## 10. The seam is the obstruction to global trivialization

The trivializing gauge vanishes at the modular seam:

\[
 h(0)=0.                                               \tag{15}
\]

Hence the gauge equivalence between \(D_0\) and ordinary differentiation is
singular precisely where modular evenness must cancel the score residue.  The
cocycle is flat on \((0,\infty)\) but has a boundary extension obstruction at
\(u=0\).

This identifies the geometry exactly:

\[
\boxed{
 \text{prime-route shear}
 =\text{bulk coboundary}
 +\text{modular-seam extension class}.
}                                                       \tag{16}
\]

The rank-one seam covector in each companion index is the coefficient-space
image of this failed global trivialization.

## 11. Consequence for the cubic programme

Because the cocycle is bulk-trivial, it cannot supply the missing orientation
of the physical moment lengths.  After restriction to the seam-compatible
coefficient hyperplane and contraction to the physical ray, its boundary
residue vanishes.

Thus the arithmetic route analysis has a definitive disposition:

1. prime and prime-power routes provide faithful coefficient coordinates;
2. their score shear is a coherent but flat cocycle;
3. modular completion removes its sole boundary obstruction;
4. the remaining cubic inequality belongs to the regular bilinear bulk.

Any proposed proof that attributes positive reserve to the cocycle is using a
gauge artifact.  The next theorem must orient the regular companion kernel
itself, after the flat arithmetic transport and seam extension have been
factored away.
