# A fixed readout is a zeroth-order observation, not a response constructor

## Theorem

Let \(x\) be a source parameter, let \(w(x)\) be a latent source-to-state map, and let \(S\) be a known downstream readout.

Suppose a release supplies only the fixed state

\[
w(0)=w_0
\]

and the corresponding readout

\[
y_0=Sw_0.
\]

This does not determine the source-response derivative

\[
\left.\frac{d}{dx}Sw(x)\right|_{x=0}.
\]

For any latent direction \(u\), the two completions

\[
w_A(x)=w_0
\]

and

\[
w_B(x)=w_0+xu
\]

agree on every released fixed-state datum at \(x=0\), while

\[
\left.\frac{d}{dx}Sw_A(x)\right|_{x=0}=0
\]

and

\[
\left.\frac{d}{dx}Sw_B(x)\right|_{x=0}=Su.
\]

Whenever \(Su\ne0\), the derivative is underdetermined.

## Jet typing

A fixed observation supplies a zeroth jet:

\[
j^0w=w_0.
\]

A response constructor requires at least the first jet:

\[
j^1w=(w_0,w'(0)).
\]

There is no canonical promotion

\[
j^0w\longmapsto j^1w.
\]

The missing derivative is not statistical noise. It is absent source structure.

## Collider realization

The public triple-Higgs reinterpretation suffix includes event selection, trained classifiers, fixed signal templates, nuisance-bearing likelihoods, and downstream detector readout.

It does not include the coupling-basis events, reweighting cards, polynomial coefficients, normalization law, or validated map from public score histograms to detector templates.

Therefore it determines fixed template values but not the derivative from portal coordinates to detector bins.

A nuisance-complete likelihood cannot repair this missing source map.

## Fisher-information consequence

Let \(J\) be the source-to-readout Jacobian and let \(W\) be a positive detector information matrix. The pulled-back source information is

\[
G=J^T WJ.
\]

If \(J\) is undefined, \(G\) is undefined.

If \(J\) has a source kernel, positive \(W\) cannot remove it:

\[
Jv=0
\quad\Longrightarrow\quad
Gv=0.
\]

Covariance calibration can quantify an admitted response. It cannot construct a missing response direction.

## Rank repair

For a two-coordinate source \((\lambda,z)\), one scalar observable has Jacobian rank at most one. A second readout repairs local identifiability exactly when the two response covectors are independent.

If one readout is

\[
r=1-z
\]

and another is

\[
q=\frac{\lambda z^2}{\lambda_H},
\]

their Jacobian is

\[
J=
\begin{pmatrix}
0&-1\\
z^2/\lambda_H&2\lambda z/\lambda_H
\end{pmatrix},
\]

with

\[
\det J=\frac{z^2}{\lambda_H}.
\]

Thus the pair is algebraically identifying for \(z>0\) and \(\lambda_H>0\). It becomes a physical instrument only after both source-to-template maps and their joint covariance are admitted.

## Software analogue

A serialized snapshot of an object does not determine its update law.

Two implementations may return identical current bytes while responding differently to the next command. A state dump therefore cannot authorize:

- a migration function;
- a controller derivative;
- a policy transition;
- a source reweighting;
- a future capability.

The constructor that produces the transition must be independently identified and authorized.

## Live-authority analogue

Sontag's twin-world result gives a relational version. Byte-identical closures execute differently when the live target epoch differs. The closure captures a claim and stable data; it does not capture current authority standing.

Both cases separate value from law:

- fixed template versus source derivative;
- captured certificate versus live authority relation.

Transporting the value does not transport the constructor that determines valid variation.

## Optical analogue

Aspect's boundary-mode tomography supplies a physical version. Two ordered lifts may have the same scalar determinant while differing in their internal state transport. The scalar invariant does not reconstruct the ordered response.

A compensating direct term can restore the determinant after two-way coupling, but that compensation is a new source input. It cannot be inferred from determinant equality.

## Constructor contract

A source-response claim is admitted only when it supplies:

1. source coordinates and their domain;
2. a parameterized latent-state or event-weight map;
3. downstream normalization;
4. the readout map;
5. nuisance and covariance transport;
6. validation joining public or physical intermediate states to the likelihood states;
7. a finite derivative falsifier.

A fixed endpoint plus downstream machinery is insufficient.

## Minimal falsifier

Choose \(S=I_2\) and \(u=(1,-1)^T\). The two completions

\[
w_A(x)=w_0,
\qquad
w_B(x)=w_0+x(1,-1)^T
\]

agree at \(x=0\) but have different first derivatives.

Any compiler that infers source-identification authority from the fixed template alone accepts both incompatible response laws and is unsound.

## Disposition

Values, derivatives, and constructors are different types.

A fixed readout can validate a predicted point. It cannot identify how the source moves through that point. That requires a parameterized, source-authorized first-jet constructor.
