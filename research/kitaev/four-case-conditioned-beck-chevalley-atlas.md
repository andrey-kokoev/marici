# Four-case conditioned Beck–Chevalley atlas

## Question

How can one distinguish scalar agreement, task-local exactness, finite typed coherence, and completion-stable conditioned coherence for a comparison cell, and what does that distinction say about Grothendieck's tiny modular tail?

## Claim boundary

Let the source and target at cutoff N be the real plane with the standard Gram form. Let the scalar readout be

\[
\pi(x,y)=x.
\]

Use

\[
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
T_N=\begin{pmatrix}0&0\\0&\tau_N\end{pmatrix},\qquad
\beta_N=A+T_N,
\]

where \(\tau_N>0\) and \(\tau_N\to0\). The matrix \(\beta_N\) represents the comparison cell after the tail is retained. This family separates four logically different claims.

### Case 1: scalar coherence only

The scalar routes agree:

\[
\pi A=\pi\beta_N=\pi.
\]

Yet \(A e_2=0\). Scalar agreement therefore proves only equality after projection. It neither proves equality of typed comparison cells nor faithfulness on the ambient state space. The first falsifier is the hidden vector \(e_2\), which is killed before scalar readout.

### Case 2: exact coherence after an authorized task localization

If the declared task identifies states with the same first coordinate, then its state object is the quotient by \(\operatorname{span}(e_2)\). The map induced by \(A\) on that quotient is the identity. This is genuine exact adequacy for the localized task, not ambient faithfulness.

The distinction is constructor-theoretic. Discarding \(e_2\) is legitimate only when the task semantics already authorizes that quotient. Introducing the quotient merely to make the diagram commute changes the allowed constructor theory and is rejected.

### Case 3: finite typed coherence without completion stability

With the tail retained,

\[
\beta_N=\begin{pmatrix}1&0\\0&\tau_N\end{pmatrix}
\]

is invertible for every finite N. Thus the tail removes the typed kernel exactly at every cutoff. Its least gain is

\[
c_N=\inf_{v\ne0}\frac{\|\beta_Nv\|}{\|v\|}=\tau_N.
\]

Since \(c_N\to0\), normalized states \(e_2\) become asymptotically invisible. Every finite comparison square may be exact and faithful while the completed comparison loses strict invertibility. This is the minimal model of a qualitatively decisive but quantitatively vanishing coherence residue.

### Case 4: uniform conditioned coherence

Let an independent, source-authorized constructor contribute

\[
R=\begin{pmatrix}0&0\\0&r\end{pmatrix},\qquad r>0,
\]

and set \(\widetilde\beta_N=A+T_N+R\). Then

\[
c(\widetilde\beta_N)=\min(1,r+\tau_N)\ge\min(1,r)>0.
\]

The comparison is now uniformly faithful through completion. A cutoff-dependent change of basis that makes \(\tau_N\) look constant is not such a repair: the certificate must use the source and target Gram forms, hence the smallest generalized eigenvalue of

\[
(B_N^*\beta_N^*G_Y\beta_NB_N,\;B_N^*G_XB_N)
\]

on the reachable subspace \(S_N=\operatorname{im}B_N\). That quantity is invariant under honest reparameterization.

### Categorical reading

Ordinary Beck–Chevalley coherence asks whether the comparison mate is an isomorphism. Conditioned Beck–Chevalley coherence asks whether it is faithful on the reachable subobject selected by the source constructors. Uniform conditioned coherence additionally asks whether the inverse gain is bounded through the pro-system.

Thus the four levels are:

1. equality after scalar projection;
2. exactness after an independently authorized task localization;
3. finite typed invertibility with no uniform lower gain;
4. uniformly conditioned invertibility on the reachable pro-object.

Neither a scalar identity nor cutoffwise rank decides the next level.

### Application signature for the tiny-tail problem

At each cutoff X, Grothendieck's source calculation must provide, rather than postulate:

- the reachable boundary-state subspace \(S_X\);
- the typed comparison mate \(\beta_X\) between the Green and Ward routes;
- the scalar projection \(\pi_X\) producing the completed section;
- the modular-tail contribution \(T_X\);
- compatible source and target Gram forms.

The finite audit is then:

\[
\pi_X(\beta_X-T_X)=\pi_X\beta_X
\]

tests scalar invisibility of the tail;

\[
\ker((\beta_X-T_X)|_{S_X})\ne0,\qquad
\ker(\beta_X|_{S_X})=0
\]

tests whether the tail repairs an exact typed kernel; and

\[
c_X^2=\lambda_{\min}^{+}
\left(
B_X^*\beta_X^*G_{Y,X}\beta_XB_X,
B_X^*G_{X,X}B_X
\right)
\]

tests conditioned strength. Completion stability requires \(\inf_X c_X>0\). The cutoff residues must also obey the refinement cocycle; failure there means the alleged tail is not a natural comparison cell.

The known identity \(V'''(0)=0\) and the scale of the first omitted modular term show that the tail is source-native and qualitatively decisive at the seam. They do not yet identify \(\beta_X\), prove that the repaired direction lies in \(S_X\), or establish a uniform lower gain. Consequently the evidence currently fits Case 3 at most; it does not establish Case 4.

### Falsifiers

The interpretation is rejected by the first applicable witness:

- the tail changes only the scalar formula and has no typed matrix representative;
- deleting the tail leaves no kernel or mate discrepancy on the reachable subspace;
- the repaired direction is outside the source-generated reachable subspace;
- the residue violates cutoff naturality;
- finite gains are positive but tend to zero;
- uniformity appears only after an unauthorized constructor or cutoff-dependent metric is added.

## Disposition

The four notions are formally separated by one minimal family. A tiny modular tail can be a genuine forward-coherence residue: it can remove a finite typed kernel even while becoming scalar-invisible and losing all uniform conditioning at completion. The immediate next calculation is not another scalar Green identity. It is the source-derived construction of \((S_X,\beta_X,T_X,G_{X},G_{Y,X})\) and the generalized-eigenvalue audit above. Until those data exist, the tail is evidence for finite typed coherence, not for completion-stable observability.