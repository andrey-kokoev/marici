# Dualizable Projection Formula Reduces D03 q-Shriek to Omega-q

## Result

For the actual finite-ringed projection of Entries 356 and 358, the value
of the extraordinary inverse image on a dualizable target object is reduced
canonically to the relative dualizing complex

\[
\omega_q:=q^!\mathcal O_X.
\]

Precisely, if \(M\in D(X,\mathcal O_X)\) is dualizable, then

\[
\boxed{
q^!M\simeq Lq^*M\otimes^{L}_{\mathcal O_Z}\omega_q .
}
\]

Consequently, whenever the Entry-352 module
\(\mathcal L^{\check C}\) belongs to the selected perfect/dualizable
subcategory,

\[
q^!\mathcal L^{\check C}
\simeq
Lq^*\mathcal L^{\check C}
\otimes^{L}_{\mathcal O_Z}\omega_q.
\]

This is the strongest computation justified by the current data. It does
not identify \(\omega_q\) with Entry 176's exceptional cap.

## Formal proof

Let \(M^\vee=R\mathcal Hom_X(M,\mathcal O_X)\). For every
\(N\in D(Z,\mathcal O_Z)\), dualizability of \(M\), the projection formula,
and the adjunction \(Rq_*\dashv q^!\) give

\[
\begin{aligned}
R\operatorname{Hom}_Z
 (N,Lq^*M\otimes^L\omega_q)
&\simeq
R\operatorname{Hom}_Z
 (N\otimes^L Lq^*M^\vee,\omega_q)\\
&\simeq
R\operatorname{Hom}_X
 (Rq_*(N\otimes^L Lq^*M^\vee),\mathcal O_X)\\
&\simeq
R\operatorname{Hom}_X
 (Rq_*N\otimes^L M^\vee,\mathcal O_X)\\
&\simeq
R\operatorname{Hom}_X(Rq_*N,M).
\end{aligned}
\]

Yoneda identifies the representing object with \(q^!M\). No purity,
orientation, or Beck--Chevalley assertion enters this argument.

## Perfect/constructible gate

The formula isolates the exact preservation criterion. Because derived
pullback is symmetric monoidal, it preserves dualizable objects. Hence
\(q^!\) preserves perfect objects provided

\[
\omega_q=q^!\mathcal O_X
\quad\text{is perfect over }\mathcal O_Z.
\]

Conversely, preservation of perfect objects forces \(\omega_q\) to be
perfect, since \(\mathcal O_X\) itself is perfect. Thus, at the perfect
level, the remaining condition is exactly

\[
\boxed{q^!\mathcal O_X\in\operatorname{Perf}(Z).}
\]

The finite cardinality of the posets and the identity stalk maps
\(\mathcal O_{X,q(z)}\to\mathcal O_{Z,z}\) do not by themselves prove this
global incidence-module finiteness. One still needs a bounded finite
projective resolution of the dualizing incidence module, or an equivalent
finite-Tor/perfectness theorem applicable to this \(q\).

Constructibility is likewise not automatic until the chosen constructible
subcategory is defined intrinsically and shown stable under tensoring with
\(\omega_q\).

## Exact boundary

Entry 176 remains a candidate local model for a factor of \(\omega_q\),
not its proved value. The following remain open and logically separate:

1. compute \(\omega_q\) as an explicit finite incidence module;
2. prove that it is perfect and constructible;
3. compare it with the exceptional cap;
4. construct the Beck--Chevalley nullhomotopy
   \(dH+Hd=\operatorname{ob}_{03}\); and
5. construct the oriented trace and PC-purity comparison.

Thus the opaque expression \(q^!\mathcal L^{\check C}\) has been reduced
to one concrete unknown, \(\omega_q\), but perfect/constructible
preservation is not yet proved.

## Evidence boundary

The existence of \(q^!\) is Entry 358's application of Theorem 4.1 of
Fernando Sancho de Salas and Juan Francisco Torres Sancho, “Derived
category of Finite Spaces and Grothendieck Duality” (arXiv:1904.06935).
The tensor formula above is a formal dualizability argument. No scheme,
logarithmic, étale, analytic, or Kato--Nakayama realization is inferred.

Delegation runs run-3c8b1ec6e1464d5bbce884b10f6903d1 and
run-c38c8a4e61ed43d3b0754885fb4a169d failed without results and are not
used as evidence.
