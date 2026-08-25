# The product-formula charge covector is a pure spinor

## 1. Finite-place hyperbolic double

Fix a finite place set \(S\), including the real place when appropriate. Let

\[
  V_S=\bigoplus_{v\in S}\mathbb C e_v
\]

be the place-current space and \(V_S^*\) its dual. Form the hyperbolic double

\[
  \mathbb H_S=V_S\oplus V_S^*
\]

with split symmetric pairing

\[
  B(x+\alpha,y+\beta)
  =
  \alpha(y)+\beta(x).
\]

Both \(V_S\) and \(V_S^*\) are maximal isotropic. The associated geometric
algebra is

\[
  \operatorname{Cl}(\mathbb H_S,B)
  \cong
  \operatorname{Cl}(|S|,|S|)
\]

after choosing a real form.

## 2. Product-formula spinor

Define the finite-place charge covector

\[
  \varepsilon_S=\sum_{v\in S}e_v^*\in V_S^*.
\]

The corresponding charge-zero current space is

\[
  \ker\varepsilon_S\subset V_S.
\]

Now set

\[
  L_S
  =
  \ker\varepsilon_S
  \oplus
  \mathbb C\varepsilon_S
  \subset
  \mathbb H_S.
\]

Every pairing inside \(L_S\) vanishes:

- current--current and covector--covector pairings vanish because the two
  summands are null;
- the mixed pairing vanishes because
  \(\varepsilon_S(x)=0\) for \(x\in\ker\varepsilon_S\).

Moreover,

\[
  \dim L_S=(|S|-1)+1=|S|,
\]

half the dimension of \(\mathbb H_S\). Therefore

\[
  \boxed{L_S=L_S^{\perp_B}.}
\]

The product formula has produced a maximal isotropic relation without any
Riesz identification of \(\varepsilon_S\) with a vector.

## 3. Exterior spin representation

Represent the Clifford algebra on

\[
  \mathcal S_S=\Lambda^\bullet V_S^*
\]

by

\[
  c(x)=\iota_x,
  \qquad
  c(\alpha)=\alpha\wedge.
\]

Regard the one-form \(\varepsilon_S\) itself as a spinor. Then:

\[
  \iota_x\varepsilon_S=\varepsilon_S(x),
\]

so every \(x\in\ker\varepsilon_S\) annihilates it; and

\[
  \alpha\wedge\varepsilon_S=0
\]

exactly when \(\alpha\) is proportional to \(\varepsilon_S\). Hence

\[
  \boxed{
  \operatorname{Ann}(\varepsilon_S)
  =
  \ker\varepsilon_S
  \oplus
  \mathbb C\varepsilon_S
  =
  L_S.}
\]

Since its annihilator is maximal isotropic, \(\varepsilon_S\) is a pure
spinor.

## 4. Why this repairs the Fisher completion error

The Fisher topology tried to turn the charge covector into a Hilbert vector
and failed because the charge functional was discontinuous. The hyperbolic
double keeps currents and charges in complementary null sectors:

\[
\boxed{
\text{energy current }x\in V_S,
\qquad
\text{integrality charge }\varepsilon_S\in V_S^*.}
\]

Their incidence \(\varepsilon_S(x)=0\) remains exact independently of any
positive energy metric.

Thus geometric algebra does not merely rename the obstruction. It supplies
the correct type for the datum that positive Hilbert completion erased.

## 5. Pure-spinor transversality

Maximal isotropic subspaces correspond projectively to pure-spinor lines.
For two pure spinors \(\psi,\chi\), their invariant spinor pairing is
nonzero precisely on the open transverse locus of their annihilator
relations, with the usual parity/component qualification.

This gives the desired finite-dimensional dictionary:

\[
\boxed{
\begin{aligned}
\text{pure-spinor pairing nonzero}
&\Longleftrightarrow
\text{maximal null sectors transverse},\\
\text{pure-spinor pairing zero}
&\Longleftrightarrow
\text{incidence/meaning defect}.
\end{aligned}}
\]

It is the geometric-algebra analogue of the unitary vacuum-defect theorem.

## 6. Relation to theta

The Clifford spinor encodes the all-place charge boundary. It does not
replace the bosonic symmetric-power Fock source:

\[
\text{bosonic Fock layer}
\quad\text{encodes prime occupations},
\]

\[
\text{Clifford pure-spinor layer}
\quad\text{encodes integrality and polarization incidence}.
\]

The completed theta object must couple these layers. Fourier/Poisson rotation
acts on the hyperbolic phase space and lifts projectively to the spinor or
metaplectic module. The half-density is the accompanying representation
correction, not an arbitrary scalar shift.

## 7. Deutsch--Popperian conjecture

**Adelic pure-spinor descent conjecture.** The compatible finite-place
product-formula spinors \(\varepsilon_S\), coupled to the positive prime Fock
vacua and the archimedean oscillator vacuum, possess a canonical
restricted-product spinor completion. Its pairing with the
character-transported reciprocal spinor is \(X(z)\) up to a nowhere-zero
source unit. The two annihilator relations are transverse off the unitary
fixed locus.

The conjecture is falsified if:

1. the finite spinor lines have no canonical connecting maps;
2. the infinite pairing depends on place exhaustion;
3. bosonic and Clifford layers cannot be coupled without erasing labels;
4. a hostile scalar multiplier admits the same pure-spinor lift; or
5. determinant equality requires prior divisor information.

## 8. Scope

The finite-place maximal-isotropic relation and pure-spinor annihilator
calculation are exact. They establish a genuine geometric-algebra connection
and preserve product-formula incidence without a Hilbert metric. No
restricted-product spinor, theta pairing identity, off-seam transversality,
or RH theorem is constructed.
