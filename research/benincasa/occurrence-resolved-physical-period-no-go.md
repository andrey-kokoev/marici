# Occurrence-resolved physical-period no-go certificate

Date: 2026-08-16

## Frozen source statements

Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2, equations
(4.15)--(4.20), distinguishes two kinds of poles produced by the contour
representation of a cosmological-polytope canonical form.

1. A true facet pole receives a negative imaginary part which is a positive
   linear combination of the positive contour regulators; see (4.16)--(4.18).
2. A spurious pole produced by a subdivision contains a difference
   \(\alpha\epsilon_{\hat b}-\beta\epsilon_{\hat a}\), with
   \(\alpha,\beta>0\). Its side depends on an arbitrarily chosen hierarchy;
   see the paragraph following (4.15) and equations (4.16)--(4.17).
3. The ambiguity is harmless only for the complete canonical form because
   the residue on a spurious boundary is zero.
4. Equations (4.19)--(4.20) induce negative imaginary parts for the physical
   site and edge energies, but do not identify their magnitudes.

These statements are source facts, not a Marici regulator choice.

## Frozen three-site corner

After the ordered \(q_{\mathcal G_{12}}\) residue, the two lower occurrences
have reduced polar coordinates

\[
A=a-X_2,\qquad B=b-X_1,
\]

with boundary values

\[
A+i\alpha,\qquad B+i\beta,
\]

where

\[
\alpha=\xi_2-\eta_{23},\qquad
\beta=\xi_1-\eta_{31}.
\]

On the frozen exceptional divisor, \(B=-A\). Hence

\[
\frac1{A+i0s_\alpha}+
\frac1{-A+i0s_\beta}
=-i\pi(s_\alpha+s_\beta)\delta(A).
\]

The four sign chambers give three currents:

\[
(--),(-+),(+-),(++)\longmapsto
2,0,0,-2
\]

in units of \(i\pi\delta(A)\). This is the exact chamber census of entry
231. The source permits an arbitrary hierarchy precisely at this spurious
corner; it does not select one of these currents for either triangulation
term separately.

## Relative-cohomology obstruction

At weight zero, entries 242--243 give

\[
\eta_i=c_i\frac{dn}{w}+d\Phi_i,
\qquad
\Phi_i=\frac{H_i(n)}{8(xy)^{3/2}w^9},
\]

with \(H_i\) odd and nonzero. At the finite endpoint divisor
\(D=\{w=0\}\), \(\Phi_i\) has a nonzero polar jet. Therefore

\[
d\Phi_i
\]

is exact in absolute meromorphic de Rham cohomology but is not zero in the
relative complex unless a boundary trivialization or subtraction is fixed.
Changing the endpoint subtraction changes the individual finite part by the
corresponding boundary value of \(\Phi_i\). The primary contour prescription
does not provide that occurrence-by-occurrence trivialization.

The sum is different. Entry 243 proves

\[
\eta_{31}+\eta_{23}=\eta_{\rm unsplit},
\qquad
\Phi_{31}+\Phi_{23}=\Phi_{\rm unsplit},
\]

coefficientwise at both endpoints. The source canonical form assigns a
boundary value to this unsplit combination, and the spurious hierarchy
dependence cancels there.

## Limit-order audit

Two source-admissible operations already fail to commute occurrence by
occurrence:

\[
\lim_{\tau\to0}\lim_{\epsilon\to0}
\ne
\lim_{\epsilon\to0}\lim_{\tau\to0}.
\]

Taking the rational weighted grade first gives the regulator-free de Rham
class and endpoint jets of entries 242--243. Taking the boundary value first
retains one of the three chamber currents above. Endpoint finite-part
subtraction supplies a second, independent relative-boundary choice. Soft
or total-energy degeneration can enlarge the supported ambiguity but cannot
remove the generic chamber counterexample.

Thus one generic nonsoft point and two allowed regulator hierarchies are a
finite falsifier of individual source-canonicity. No exhaustive numerical
scan can restore uniqueness after this symbolic counterexample.

## Narrow verdict

The strong conjecture is falsified:

\[
\boxed{
\text{the two occurrence-resolved weight-zero classes do not have
individually source-canonical physical periods.}
}
\]

The surviving statement is

\[
\boxed{
\text{occurrence resolution is canonical in meromorphic de Rham/endpoint-jet
data, while the physical period is canonical only after source sewing.}
}
\]

This is relative-chain/coefficient data over the frozen marked intersection.
It is not a new carrier incidence.

## Classification

- existing carrier: the two marked lower divisors, their exceptional
  intersection, finite endpoint divisor, and total-energy cover;
- relative-chain data: regulator chamber and endpoint trivialization;
- Tate/Kummer coefficient data: the two unequal classes \(c_i[dn/w]\);
- extension data: possible packaging of endpoint jets with the unsplit
  relative class;
- soft support: excluded in the generic counterexample;
- Legendre/Gysin quotient: no direct image, as in entries 240--243;
- genuinely new carrier structure: none.

## Remaining frontier

The next finite problem is not to seek canonical individual periods. It is
to construct the minimal relative extension in which the pair
\((\eta_{31},\eta_{23})\) and its endpoint jets descend functorially to the
single source-canonical unsplit period, and to test horizontality of that
sewn extension under the Gauss--Manin connection.
