# Entry-143 Cellular Cosheaf Geometrization

## Result

The literal entry-143 BM--Cech target has an exact geometric realization in
the finite cellular category. It is not yet a ringed/log six-functor object.

Let \(P_{K_6}^{\rm or}\) be the finite state poset whose elements are pairs
\((S,H)\), where \(S\) is a noncrossing dissection of the labelled hexagon
and \(H\subseteq S\) is the retained normal-circle set. Give this poset its
Alexandrov topology and dimension

\[
\deg(S,H)=3-|S|+|H|.
\]

Define the coefficient cosheaf \(\mathscr E^{\check C}\) by the costalks

\[
\mathscr E^{\check C}_{S,H}
=R[X]\bigl[u_a^{-1}:a\in S\setminus H\bigr].
\]

There are two kinds of covering relation. For radial addition
\((S,H)\prec(S\cup\{a\},H)\), corestriction is multiplication by
\(X_a/u_a\). For normal deletion
\((S,H)\prec(S,H\setminus\{h\})\), it is the canonical localization map,
whose coefficient in the chosen generator bases is one.

These maps are functorial. Two radial additions commute because the
coefficient ring is commutative; two normal deletions commute as iterated
localizations; and radial addition commutes with normal deletion. The signs
in entry 143 are therefore the cellular incidence and exterior-fiber signs,
not failures of cosheaf functoriality.

Consequently the compact cellular chain complex of this coefficient cosheaf
is exactly

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C}
=\bigoplus_{(S,H)\notin F_V}
\mathscr E^{\check C}_{S,H}[S,H]
\]

with entry 143's radial \(X_a/u_a\) and signed normal unit differential.
The existing global promotion checker verifies all 215 states, every
square, \(d^2=0\), denominator support, and \(D_3\)-covariance.

The support subsets \(F_V\subset F_B\subset F_K\) are closed under the
cellular boundary and hence define coefficient subcosheaves. Their quotient
realizes the strict filtration

\[
0\to F_B/F_V\to F_K/F_V\to Q\to0
\]

with ranks \((12,57,84,39)\), \((12,57,87,43)\), and \((0,0,3,4)\).

## Remaining boundary

This proves cellular cosheaf geometrization, not a constructible-sheaf
identification on an algebraic or log ringed space. The semilinear finite
dual \(\mathbb D_\iota\) is likewise not yet identified with
\(R\mathcal Hom(-,\omega_X)\).

The next missing datum is therefore narrower than target geometrization:
construct a ringed/log enhancement of \((P_{K_6}^{\rm or},\mathscr E^{\check C})\)
whose exceptional inverse image and proper corestrictions reproduce these
costalks and maps. Only such an enhancement can type \(q^!\), a relative
dualizing trace, and the PC-purity comparison.

Delegation evidence: run-9681aca3750a48678fa421a6ef08c27e and
run-a24fa38ef2644ae280c3692b2363ae97.
