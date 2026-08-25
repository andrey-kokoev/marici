# Theta cubic six-copy certificate

Author: `marici.Grothendieck`

## Objective

Audit whether the exceptional residual

\[
\mathscr R_{34}=36K_4^3-\mathcal E_{34}^2,
\qquad
\mathcal E_{34}=35Z_2Z_5^2-81Z_4^3+27Z_4K_4,
\]

has a source-derived six-copy positivity explanation stronger than the cubic
Jensen statement itself.

## 1. Exact discriminant factorization

Write

\[
J_2^{(3)}(X)=d+3CX+3BX^2+AX^3
\]

with

\[
(d,C,B,A)=(b_2,b_3,b_4,b_5),
\qquad
D=B^2-AC.
\]

The cleared centering error is

\[
E=dA^2-B^3+3BD=dA^2+2B^3-3ABC.
\]

Direct expansion gives the polynomial identity

\[
\boxed{
4D^3-E^2=\frac{A^2}{27}\operatorname{disc}(J_2^{(3)}).
}
\]

No positivity assumption enters this identity. With

\[
G=\Gamma(9/2),
\qquad
D=\frac{K_4}{9G^2},
\qquad
E=\frac{\mathcal E_{34}}{81G^3},
\qquad
A=b_5=\frac{2Z_5}{9G},
\]

it becomes

\[
\boxed{
\mathscr R_{34}
=12G^4Z_5^2\operatorname{disc}(J_2^{(3)}).
}
\]

The prefactor is strictly positive. Therefore the proposed six-copy
certificate is exactly the cubic discriminant with a positive source factor;
it is not yet an independent explanation of its sign.

## 2. Canonical symmetric polarization

Let

\[
K_4=\sum_{i,j}\bar\kappa(i,j),
\]

where `bar-kappa` is the symmetrization of the ordered companion coefficient
matrix. Let the symmetric three-label centering kernel `e(i,j,k)` satisfy

\[
\mathcal E_{34}=\sum_{i,j,k}e(i,j,k).
\]

For six labels `I=(i_1,...,i_6)`, let `PM_6` be the fifteen perfect matchings
of the six positions and let `Part_(3,3)` be the ten unordered partitions
into two triples. Define

\[
\mathcal K_6(I)
=\frac1{15}\sum_{M\in PM_6}
\prod_{\{a,b\}\in M}\bar\kappa(i_a,i_b),
\]

and

\[
\mathcal E_6(I)
=\frac1{10}\sum_{\{S,S^c\}\in Part_{(3,3)}}
e(i_S)e(i_{S^c}).
\]

The fully symmetric polarized residual is

\[
\boxed{
\mathfrak r_6(I)=36\mathcal K_6(I)-\mathcal E_6(I).
}
\]

Because every matching and every triple partition gives the same total after
summing all ordered labels,

\[
\boxed{
\sum_{i_1,\ldots,i_6}\mathfrak r_6(i_1,\ldots,i_6)
=\mathscr R_{34}.
}
\]

This completes the requested polarization without selecting a preferred
pairing or triple decomposition.

## 3. Orbit types

Permutation symmetry separates label multiplicities, not signs. The six
positions have eleven multiplicity types, indexed by partitions of six:

\[
6, 5+1, 4+2, 4+1+1, 3+3, 3+2+1,
3+1+1+1, 2+2+2, 2+2+1+1,
2+1+1+1+1, 1^6.
\]

They correspond respectively to diagonal, two-label, and genuinely
multi-label packets. This is only a permutation-orbit census. A physical
sign claim requires modular closure as well: raw theta labels are not
individually closed under reciprocal-scale completion.

## 4. Immediate warning

Pointwise positivity of `mathfrak r_6(I)` would be much stronger than the
desired theorem and is not implied by positivity of the completed companion.
Individual companion coefficients can have either seam orientation, whereas
only their completed contraction is positive. Thus the symmetric
polarization supplies the correct bookkeeping object, but not termwise
positivity.

## 5. Seam removal precedes polarization

In each companion index the boundary residue is the rank-one coefficient
packet

\[
a_m(u)b_n,
\qquad
a_m(u)=\phi_m(u),
\qquad
b_n=\phi_n'(0).
\]

The completed physical coefficient vector `1` satisfies

\[
b^*\mathbf1=\sum_n\phi_n'(0)=\Phi'(0)=0.
\]

Consequently every occurrence of the companion in `K_4^3` is already
contracted through the seam hyperplane `ker(b^*)`. Tensoring three copies
does not create a new boundary class: a rank-one residue in any factor is
annihilated by the physical contraction in that factor.

The `Z` terms are moments of the completed even source and contain no radial
score pole. Therefore

\[
\boxed{
\text{the polarized residual has no surviving rank-one seam factor.}
}
\]

Any later Gram construction that uses a seam vector as a positive repair
would reintroduce a channel that the physical source has already quotiented
out.

## 6. No finite modularly closed label packet

The individual positive-chart labels obey

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n),
\]

whereas reciprocal completion is the global identity

\[
\Phi(-u)=\Phi(u).
\]

It is not a labelwise involution. For a finite nonempty label set `S`, the
positive-chart sum `sum_(n in S) phi_n(u)` decays super-exponentially as
`u -> +infinity`. Its reflected sum has the small-argument asymptotics of a
finite collection of theta exponentials and decays only exponentially.
Hence it cannot equal any finite positive-chart label sum for all `u`.

Equivalently, Poisson summation implements reciprocal reflection by the full
lattice, not by a finite permutation of positive integers. Thus

\[
\boxed{
\text{no nonempty finite raw-label packet is closed under modular reflection.}
}
\]

The minimal modularly closed physical packet is the entire completed theta
sum. The eleven multiplicity types above are valid coefficient bookkeeping,
but none is separately authorized as a physical sign block.

## 7. Reciprocal-scale action on six copies

Before the even quotient, reciprocal reflection acts diagonally on source
coordinates:

\[
\mathcal R_6(u_1,\ldots,u_6)=(-u_1,\ldots,-u_6).
\]

It has

\[
|\det D\mathcal R_6|=1.
\]

On the full completed product source its density ratio is exactly one. On
raw arithmetic labels it is an infinite Poisson transform, not a finite
label permutation, so no finite-orbit density ratio exists. After passing to
the even moments `Z_t` and the completed companion `K_t`, the action becomes
trivial.

Therefore reciprocal reflection supplies neither a negative-to-positive
finite-orbit pairing nor an additional repair term for `mathscr R_34`. Its
role is to define the completed source on which the scalar residual is
formed. The remaining sign problem is internal to that completed packet.

## 8. Consequence for orbit classification

Diagonal, two-label, and genuinely multi-label coefficient sectors have the
following disposition:

\[
\begin{array}{c|c}
\text{sector}&\text{status}\\
\hline
\text{diagonal}&\text{not seam-oriented and not modularly closed}\\
\text{two-label}&\text{contains the rank-one cross-label seam repair but is
not modularly closed}\\
\text{three/six-label}&\text{algebraically faithful after full summation but
not a finite physical orbit}.
\end{array}
\]

Thus negative coefficient packets, if present, are allowed to cancel only
after full cross-orbit completion. A proof by a bounded census of modular
label orbits is structurally unavailable.

## 9. Elimination of the companion symbol

The companion moment is not algebraically independent:

\[
K_t=(2t+1)Z_t^2-(2t-1)Z_{t-1}Z_{t+1}.
\]

At `t=4`,

\[
K_4=9Z_4^2-7Z_3Z_5.
\]

Therefore

\[
\mathcal E_{34}
=35Z_2Z_5^2+162Z_4^3-189Z_3Z_4Z_5
\]

and the residual is the explicit moment polynomial

\[
\boxed{
\begin{aligned}
\mathscr R_{34}={}&
36(9Z_4^2-7Z_3Z_5)^3\\
&-(35Z_2Z_5^2+162Z_4^3-189Z_3Z_4Z_5)^2.
\end{aligned}
}
\]

This confirms that a Schur complement using `K_4` as an independent positive
block would be misleading: `K_4` is the quadratic Jensen minor built from
the same four adjacent moments. The final Schur complement is exactly the
cubic discriminant again.

## 10. Universal Gram mechanism is analytically falsified

Consider the single completed source

\[
\Phi_\delta(u)=e^{-u^2-\delta u^6},
\qquad \delta>0.
\]

It is positive, even, entire, and reflection-closed. Its radial stiffness is

\[
\frac{V_\delta'(u)}u=2+6\delta u^4,
\]

which is strictly increasing on `u>0`. Hence it satisfies the universal
source-curvature hypothesis that makes the completed bilinear companion
positive.

At the Gaussian endpoint, exact differentiation of its moments gives

\[
\varepsilon_t(\delta)
=6\left(t+\frac32\right)\delta+O(\delta^2).
\]

Thus

\[
F(\varepsilon_t(\delta))
=\frac1{\sqrt{6(t+3/2)\delta}}+O(\sqrt\delta),
\]

and consequently

\[
|F(\varepsilon_4)-F(\varepsilon_3)|\longrightarrow\infty
\qquad(\delta\downarrow0).
\]

For every sufficiently small positive `delta`, the cubic gate fails and

\[
\boxed{\mathscr R_{34}[\Phi_\delta]<0.}
\]

This is a one-source, fully diagonal six-copy packet: multiplicity type `6`.
It is therefore the smallest possible analytically indefinite orbit. No
cross-label ambiguity, finite truncation, nonanalytic origin, seam pole, or
missing reflection partner is involved.

It follows that there is no universal Gram representation of
`mathscr R_34` whose positivity uses only:

- positivity and evenness of the source;
- strict radial curvature;
- positivity of the bilinear companion;
- reciprocal reflection with unit density ratio; or
- removal of the rank-one seam factor.

Such a representation would also be positive for `Phi_delta`, contradicting
the exact asymptotic above.

## 11. Canonical reflection does not repair the hostile orbit

On the six-copy hostile packet, reciprocal reflection is

\[
(u_1,\ldots,u_6)\longmapsto(-u_1,\ldots,-u_6).
\]

Its Jacobian magnitude and completed density ratio are both one, and the
source is fixed pointwise as an even function. Nevertheless the integrated
residual is negative. Hence reflection-fixed packets need not be positive;
there is no negative orbit that reflection transports to a distinct positive
orbit in this minimal example.

This proves that the missing theta mechanism must use arithmetic information
strictly stronger than reciprocal symmetry. Prime-route score shear cannot
supply it because its bulk class is a coboundary and its physical seam class
vanishes.

## 12. Gram and Schur-complement disposition

A tautological Gram representation exists after assuming the desired sign,
and the classical Hermite/Bezout matrix of `J_2^(3)` is positive precisely
when that cubic is real-rooted. Neither is explanatory: their last principal
minor is the discriminant itself.

The positive bilinear companion supplies the quadratic minor `K_4>0`, but
its putative final Schur complement is

\[
\frac{\mathscr R_{34}}{\text{positive quadratic factors}}.
\]

Therefore the Schur-complement route does not reduce the sign problem unless
theta arithmetic independently constructs the full Hermite matrix as a Gram
matrix. The hostile source proves that no construction from the universal
companion data alone can do so.

## 13. Smallest surviving theta-specific target

The six-copy/Gram mechanism has been minimally falsified as a universal
source theorem. What remains for theta is not another finite label orbit but
the full-lattice pointed moment inequality

\[
\boxed{
\begin{aligned}
&36(9Z_4^2-7Z_3Z_5)^3\\
&\quad\ge
(35Z_2Z_5^2+162Z_4^3-189Z_3Z_4Z_5)^2,
\end{aligned}
}
\]

with all `Z_t` taken from the single Poisson-completed theta source.

The missing discriminator must distinguish that full lattice from the
hostile even source. The existing audits exclude generic curvature, modular
reflection alone, prime-route bulk shear, seam repair, finite labelwise
positivity, and companion-only Schur complements. A viable next mechanism
must therefore be a genuinely arithmetic full-lattice identity—most
naturally a Poisson-summed Hermite/Bezout energy whose final boundary term is
the pointed moment `Z_2`.

## 14. Disposition

The proposed six-copy positivity explanation is sharply falsified in its
universal Gram form:

1. its scalar is exactly a positively dressed cubic discriminant;
2. its symmetric polarization has no finite modular sign units;
3. all seam repairs vanish before the physical contraction;
4. reciprocal reflection acts trivially on the completed residual;
5. the single-source analytic family `Phi_delta` makes the fully diagonal
   six-copy orbit negative;
6. companion-only Gram and Schur-complement constructions are therefore
   impossible without inserting theta-specific arithmetic information.

This does not falsify the exceptional inequality for theta. It identifies
the smallest remaining object and precisely which additional explanation it
must contain.

## Scope

The factorization and polarization are exact. They do not prove the
exceptional cubic discriminant nonnegative and do not prove RH.
