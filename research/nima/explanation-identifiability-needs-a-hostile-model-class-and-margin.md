# Explanation identifiability needs a hostile model class and a margin

## Attack on the first conjecture

The condition

\[
\Sigma^{-1}(\Sigma(E))
\cap
\operatorname{Adm}_{\mathrm{src}}
=
[E]_{\mathrm{auth}}
\]

is vacuous if the admissible model class is defined after seeing \(E\), or if
it is restricted to one preferred model. Uniqueness inside a singleton class
does not make that model explanatory.

The admissible class is therefore load-bearing evidence. It must be frozen by
source rules independently of the observed target behaviour and must contain
the hostile variations those rules genuinely permit.

## Lookup-table hostile

Every finite deterministic input-output behaviour has a canonical minimal
Moore or Mealy realization obtained from future equivalence of histories.
That realization is unique up to state relabelling.

Consequently:

- predictive sufficiency can hold;
- intervention closure can hold;
- behavioural minimality can hold;
- realization uniqueness can hold;

while the transition table merely enumerates the behaviour and exposes no
source factorization.

Thus minimality plus uniqueness explains the black-box state complexity, not
necessarily the mechanism generating the transitions.

The missing gate is that the transition law factor through source-derived
constructors whose meanings and composition laws are fixed before the
behaviour table is known.

## Hostile-closure requirement

Let \(\mathcal G_{\mathrm{src}}\) be the frozen source grammar generating
candidate realizations. The admitted class must be closed under every
variation that preserves that grammar:

\[
E\in\operatorname{Adm}(\mathcal G_{\mathrm{src}}),
\quad\Longrightarrow\quad
H(E)\in\operatorname{Adm}(\mathcal G_{\mathrm{src}}).
\]

Here \(H\) ranges over variations preserving \(\mathcal G_{\mathrm{src}}\).
A preferred explanation earns identifiability only after surviving this
hostile closure. Excluding \(H(E)\) because it changes the desired output is
circular unless the source grammar independently prohibits \(H\).

## Local identifiability

Suppose admissible realizations form a finite-dimensional manifold
\(\mathcal M\), authorized gauge transformations generate a tangent subspace
\(\mathcal G_E\subset T_E\mathcal M\), and

\[
\Sigma:\mathcal M\longrightarrow\mathcal Y
\]

is the complete declared intervention/readout map.

Local identifiability modulo gauge requires

\[
\ker D\Sigma_E=\mathcal G_E.
\]

Equivalently, the derivative of \(\Sigma\) must be injective on a transverse
complement to the gauge orbit. A non-gauge vector

\[
\delta E\in\ker D\Sigma_E
\]

is an infinitesimal hard-to-vary falsifier: the model can be changed without a
first-order change in any declared consequence.

This is only a local condition. Disconnected globally equivalent
realizations can remain.

## Explanatory margin

Choose source-derived norms and let

\[
T_E\mathcal M=\mathcal G_E\oplus\mathcal N_E.
\]

Define the finite explanatory margin

\[
\mu(E)
=
\inf_{\substack{\delta E\in\mathcal N_E\\
\|\delta E\|=1}}
\|D\Sigma_E(\delta E)\|.
\]

Then:

- \(\mu(E)>0\) gives quantitatively stable local identifiability;
- \(\mu(E)=0\) gives a locally invisible non-gauge direction;
- \(\mu(E_N)>0\) at every cutoff but \(\mu(E_N)\to0\) gives explanatory
  collapse under completion.

The margin is the parameter-identifiability analogue of the smallest
observability-Gramian eigenvalue.

It is meaningful only after the parameter norm, output norm, intervention
family, and gauge directions are source-typed. Rescaling parameters after the
fact can manufacture an arbitrary margin.

## Intervention design

When \(\mu(E)=0\), an additional probe is useful only if it detects the hidden
tangent:

\[
D R_E(\delta E)\ne0
\qquad
\forall\,\delta E\in
\left(\ker D\Sigma_E/\mathcal G_E\right)\setminus\{0\}.
\]

This is the same kernel-reference rule found in syndrome and observability
problems. The minimal explanatory experiment is the smallest authorized probe
family whose derivatives are jointly injective transverse to gauge.

Control theory can synthesize a separating row. It cannot authorize the
physical availability or source meaning of that row.

## Revised conjecture

An explanation is a source-derived intervention realization whose complete
behaviour is:

1. minimal under future equivalence;
2. globally identifiable modulo authorized gauge inside a predeclared
   hostile-closed source model class;
3. locally identifiable with a positive source-normalized margin;
4. stable under the declared completion;
5. prospectively successful on composite interventions not used to choose
   the realization.

This still does not claim that every explanation must be minimal in ordinary
language. It claims that redundant dark structure carries no explanatory
authority unless an independent source probe makes it operative.

## Falsifiers

- The admissible class is introduced after the preferred model.
- A hostile variation is rejected solely because its output is unwanted.
- A lookup table passes every stated gate because no source factorization was
  required.
- \(\ker D\Sigma_E\) contains a non-gauge direction.
- Local identifiability holds but a disconnected equivalent realization
  exists.
- The explanatory margin depends on an arbitrary parameter rescaling.
- Every finite margin is positive but tends to zero.
- A synthesized separating probe has no admitted source or physical port.

## Consequence

“Hard to vary” should not mean syntactically awkward to edit. It should mean
that every source-admissible, non-gauge deformation changes some predeclared
intervention consequence by a completion-stable amount.
