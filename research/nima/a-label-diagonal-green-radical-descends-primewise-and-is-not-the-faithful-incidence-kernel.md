# A label-diagonal Green radical descends primewise and is not the faithful incidence kernel

## Question

If G4 retains labels through recovery, does quotienting a Green radical preserve prime and grade projections?

## Claim boundary

Yes when the Green form itself is label diagonal. Its radical is invariant under every label projection, so the quotient retains the direct-sum grading and the reduced return can remain prime diagonal. Moreover, the faithful labelled theta incidence has zero kernel; any nonzero G4 Green radical must therefore come from a different Green feature form, not from the incidence synthesis.

## Label-diagonal form

Let

\[
\mathcal A_{\exp}
=igoplus_{\lambda}^{\rm proj}A_\lambda,
\qquad
\lambda=(p,k,\pm),
\]

with continuous label projections \(P_\lambda\). Suppose a continuous sesquilinear Green form has no cross-label blocks:

\[
G(P_\lambda c,P_\mu d)=0
\qquad(\lambda\ne\mu).
\]

Equivalently,

\[
G(c,d)=\sum_\lambda G_\lambda(P_\lambda c,P_\lambda d)
\]

with convergence in the declared projective topology.

Define

\[
N=\operatorname{rad}G
=\{c:G(c,d)=0\text{ for every }d\}.
\]

## Projection invariance

If \(n\in N\), then for every \(d\),

\[
G(P_\lambda n,d)
=G(P_\lambda n,P_\lambda d)
=G(n,P_\lambda d)
=0.
\]

Hence

\[
P_\lambda N\subset N.
\]

The radical is label invariant. The quotient projection

\[
\overline P_\lambda(c+N)
=P_\lambda c+N
\]

is therefore well-defined and continuous on \(\mathcal A_{\exp}/N\).

If \(G\) is continuous, then

\[
N=\bigcap_d\ker G(\,\cdot\,,d)
\]

is closed. The quotient is consequently Hausdorff; for a Fréchet projective source it is again complete and locally convex.

## Primewise quotient return

Let \(q:\mathcal A_{\exp}\to\mathcal A_{\exp}/N\) be the quotient map. Projection invariance gives

\[
qP_\lambda=\overline P_\lambda q.
\]

Combining this with the labelled recovery port yields

\[
q\mathcal R:\mathfrak H_{\exp}^{\rm lab}
\longrightarrow\mathcal A_{\exp}/N.
\]

If \(\mathcal R\) is label diagonal, then

\[
\overline P_\lambda q\mathcal R P_\mu
=0
\qquad(\lambda\ne\mu).
\]

Thus quotient descent does not itself create cross-prime blocks. Such blocks arise only if the form, metric, codiagonal, or return already couples labels.

## Incidence radical versus Green radical

The labelled theta incidence \(\mathcal I\) has a continuous left inverse:

\[
\mathcal R\mathcal I=I.
\]

Therefore

\[
\ker\mathcal I=0.
\]

For a positive target metric, its synthesis Gram satisfies

\[
\ker(\mathcal I^*\mathcal I)=\ker\mathcal I=0.
\]

Hence a nonzero radical in the eventual G4 Green form cannot be attributed to loss of source labels under the faithful labelled incidence. It must come from another declared object, such as a boundary Green feature map, gauge relation, mixed form, or later codiagonal compression.

Conflating these radicals would incorrectly turn faithful recovery into quotient annihilation.

## G4 conformance consequence

A retained-label G4 witness must identify:

1. which form defines the radical;
2. whether that form is label diagonal;
3. whether every label projection preserves the radical;
4. whether the quotient return is formed before codiagonalization;
5. whether any later metric introduces cross-label blocks.

The existing source incidence already answers none of these questions for an undeclared G4 Green form.

## Direction rescore

- Label invariance of a diagonal Green radical: completed.
- Hausdorff projective quotient: completed for continuous forms.
- Prime-diagonal quotient return: completed conditionally on label-diagonal form and pre-codiagonal return.
- Identification of the actual G4 Green radical: interface-blocked.
- Cross-prime estimates: unnecessary for Architecture A unless G4 later couples labels.

## Disposition

Retained labels are compatible with nontrivial Green quotient descent: the quotient remains prime and grade resolved whenever the defining form is label diagonal. The faithful incidence itself has no radical. G4 must expose the separate form or feature map that creates its proposed radical before quotient or cross-prime claims can be tested. No RH conclusion is authorized.
