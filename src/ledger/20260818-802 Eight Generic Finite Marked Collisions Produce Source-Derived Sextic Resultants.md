# Eight Generic Finite Marked Collisions Produce Source-Derived Sextic Resultants

## Finite marked arrangement

After the source residue \(q_{\mathcal G_{12}}=0\), set

\[
E=X_1+X_2+X_3.
\]

The five remaining marked sections in the \((a,b)\)-plane are

\[
\begin{array}{c|c}
q_{\mathfrak g_1}&b=E-X_1\\
q_{\mathfrak g_2}&a=E-X_2\\
q_{\mathfrak g_3}&a+b=-X_3\\
q_{\mathcal G_{23}}&a=-E\\
q_{\mathcal G_{31}}&b=-E.
\end{array}
\]

Let \(K_{\rm CM}(a,b)=-\det(\mathrm{CM})/2\) be the source-normalized
generic Cayley--Menger determinant used in Entries 794 and 796.

## Complete pair census

Of the ten marked pairs, eight are generically transverse.  Their unique
intersection points are

\[
\begin{array}{c|c}
(\mathfrak g_1,\mathfrak g_2)&(E-X_2,E-X_1)\\
(\mathfrak g_1,\mathfrak g_3)&(X_1-E-X_3,E-X_1)\\
(\mathfrak g_1,\mathcal G_{23})&(-E,E-X_1)\\
(\mathfrak g_2,\mathfrak g_3)&(E-X_2,X_2-E-X_3)\\
(\mathfrak g_2,\mathcal G_{31})&(E-X_2,-E)\\
(\mathfrak g_3,\mathcal G_{23})&(-E,E-X_3)\\
(\mathfrak g_3,\mathcal G_{31})&(E-X_3,-E)\\
(\mathcal G_{23},\mathcal G_{31})&(-E,-E).
\end{array}
\]

For every row, the collision with the branch surface is exactly

\[
K_{\rm CM}(a_0,b_0)=0.
\]

After imposing the energy-sum relation, exact factorization over
\(\mathbb Q[X_1,X_2,X_3,P_1,P_2,P_3]\) gives eight irreducible degree-six
polynomials.  Their expanded term counts are

\[
54,\ 50,\ 40,\ 50,\ 40,\ 40,\ 40,\ 37.
\]

The other two pairs are parallel.  They coincide only on

\[
\boxed{
X_1+2X_2+2X_3=0,
\qquad
2X_1+X_2+2X_3=0,
}
\]

which are source-labelled linear marked-incidence loci.

## Classification

The eight sextics are genuinely new divisors in the projected external
parameter base; they must not be erased merely because they arise from an
existing determinant.  But none is a new unlabelled component of the carrier.
Each has the canonical provenance

\[
\boxed{
\text{source marked pair}
\longrightarrow (a_0,b_0)
\longrightarrow K_{\rm CM}(a_0,b_0).
}
\]

Thus the hostile finite-chart test refines H2 in the expected direction:

\[
\boxed{
\text{shared Cayley--Menger/marked carrier calculus}
+
\text{sector-specific projected sextic discriminants}.
}
\]

The distinction is essential.  "No new carrier" does not mean "no new
parameter-space singular polynomial."  Projection of a frozen relative
geometry can and here does generate new irreducible coefficient supports.

## Verification

`research/nima/audit_generic_finite_marked_cm_collisions.py` reconstructs
\(K_{\rm CM}\) from the full five-by-five matrix, imposes every marked pair,
substitutes \(E=X_1+X_2+X_3\), and factors the resulting polynomials exactly.
The census and hashes of every expanded polynomial are in
`research/nima/generic-finite-marked-cm-collisions.json`.

Correction recorded with Entry 803: the first certificate used a simultaneous
substitution in which \(E\) could remain inside the marked-point replacement
while being omitted from the declared polynomial generators.  The repaired
certificate substitutes \((a,b)\) first and only then imposes
\(E=X_1+X_2+X_3\).  The irreducibility and degree-six conclusions are
unchanged; the term counts and polynomial hashes above are the corrected ones.

## Next falsifier

Determine whether the eight sextics form fewer cyclic occurrence orbits and
whether their local vanishing cycles are generated functorially by the same
Kato/Gysin kernel calculus as the infinity elliptic boundary.  Failure of
naturality, rather than the appearance of a new polynomial, would be evidence
against H2.

Allocator claim: `seqclaim-4a9da02b9ab2b00469868db4`.
