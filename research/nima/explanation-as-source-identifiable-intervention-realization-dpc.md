# Deutsch--Popperian conjecture: explanation is a source-identifiable intervention realization

## Aim

Exact prediction is not yet explanation. A Sum or Product readout may classify
all observed outcomes while leaving many incompatible ordered mechanisms.
Control theory suggests a nonpsychological criterion: first construct the
minimal state needed for every admitted future intervention, then ask whether
the source independently determines a realization of that state and its
transition laws.

## Behavioural state

Let \(\mathcal H\) be the set of admitted finite histories, \(\mathcal W\) the
set of admitted future intervention words, and \(\mathcal R\) the frozen probe
family. Define future equivalence by

\[
h\sim_{\mathrm{fut}}h'
\]

exactly when every continuation and probe gives the same result:

\[
r(hw)=r(h'w)
\qquad
\forall\,w\in\mathcal W,\ r\in\mathcal R.
\]

The quotient

\[
X_{\min}=\mathcal H/{\sim_{\mathrm{fut}}}
\]

is the canonical minimal predictive state. Each admitted intervention acts on
it by an endomorphism. This is the control/automata-theoretic Endo object
forced by the declared counterfactual interface.

The construction is relative to the admitted interventions and probes. Adding
a new intervention or probe can refine the state quotient.

## Deutsch--Popperian conjecture

An explanation of a declared phenomenon packet consists of a realization

\[
\rho:X_{\mathrm{src}}\longrightarrow X_{\min}
\]

with source-derived state types and intervention actions, satisfying all of
the following:

1. **Predictive sufficiency:** every frozen Sum and Product readout factors
   through \(X_{\mathrm{src}}\).
2. **Intervention closure:** every admitted intervention has a typed action on
   \(X_{\mathrm{src}}\), and composition agrees with experiment.
3. **Behavioural minimality:** no nontrivial source-state quotient preserves
   every admitted future probe.
4. **Source identifiability:** any source-admissible realization with the same
   complete intervention behaviour is equivalent by an independently
   authorized change of realization frame.
5. **Completion stability:** normalized explanatory states do not become
   behaviourally invisible only in the limit.
6. **Prospective constraint:** the realization determines outcomes for
   predeclared composite or held-out interventions not used to fit its
   presentation.

The hard-to-vary condition is therefore an identifiability fiber:

\[
\Sigma^{-1}(\Sigma(E))
\cap
\operatorname{Adm}_{\mathrm{src}}
=
[E]_{\mathrm{auth}},
\]

where \(\Sigma\) is the complete declared intervention/readout behaviour and
\([E]_{\mathrm{auth}}\) is the authorized realization gauge orbit.

If the left side contains inequivalent admissible realizations, the evidence
confirms a behavioural shadow but does not yet explain its constructor.

## Why minimal prediction is not sufficient

The quotient \(X_{\min}\) is a canonical predictive machine. It need not expose
the source mechanism. A finite lookup table can realize the same transition
behaviour. Therefore behavioural minimality removes redundant dark states but
does not establish source authority.

The explanatory content lies in a source-derived factorization of the
transition action whose parts retain their meanings under independently
admitted interventions. A post-hoc relabelling of lookup-table states does not
supply that factorization.

## Attack 1: determinant observation

For

\[
\dot U=A_{u(t)}U,
\qquad
y=\det U,
\]

the output satisfies

\[
\frac{d}{dt}\log y=\operatorname{Tr}A_{u(t)}.
\]

All trace-zero commutator dynamics is future-equivalent under determinant-only
probing. The resulting \(X_{\min}\) is merely the abelianized gain state.
Distinct shears and mode couplings remain in the identifiability fiber.

Disposition: determinant prediction passes sufficiency for its frozen probe
but fails source identifiability for the ordered plant.

## Attack 2: the Pauli packet

Pauli labels in \(\mathbf F_2^{2n}\) supply the additive state. The central
cocycle records the commutator phase, and together they reconstruct Pauli
multiplication up to a section:

\[
P(v)P(w)=\omega(v,w)P(v+w).
\]

For Pauli interventions and phase-sensitive probes, the Sum-plus-Product
packet closes the finite Endo law because the commutator algebra is central.

Disposition: algebraic realization identifiability passes up to phase-frame
gauge. Physical actuator authority does not follow and remains a separate
constructor gate.

## Attack 3: minimal scalar transfer

A controllable and observable finite realization of

\[
G(s)=D+C(sI-A)^{-1}B
\]

is unique up to similarity. Thus the complete transfer behaviour can identify
the minimal Endo realization modulo coordinate gauge.

However, arbitrary finite Blaschke products possess passive, controllable, and
observable realizations. Minimal realization explains the internal memory of
the chosen transfer but does not explain why one source has that transfer
rather than another.

Disposition: realization-relative explanation passes; source-selective
explanation remains open.

## Attack 4: completion escape

Let every finite system be observable but let

\[
\lambda_{\min}W_N\longrightarrow0
\]

for its observability Gramian. Then each finite history class is separated,
while normalized state sequences become indistinguishable at completion.

Disposition: finite explanation does not compose into a completed explanation
without a uniform lower bound or an explicitly typed quotient by the escaping
states.

## Falsifiers

The conjecture fails or a proposed explanation is downgraded when:

- two inequivalent source-admissible realizations have identical complete
  declared intervention behaviour;
- a claimed state direction is unreachable or unobservable;
- a new admitted intervention cannot act on the proposed state type;
- identifiability is obtained by declaring the entire fiber to be gauge;
- the realization stores the raw history while claiming minimal explanatory
  state;
- prospective composite interventions require fitted transition corrections;
- finite observability constants collapse at completion;
- a Product or Sum equality is used to authorize an Endo constructor.

## Research consequence

The programme should compare sectors by the kernel tower

\[
\text{history}
\longrightarrow
\text{future-behaviour state}
\longrightarrow
\text{Product shadow}
\longrightarrow
\text{Sum shadow}.
\]

For each arrow it should classify:

- the information erased;
- the smallest probe that restores it;
- the authorized gauge;
- whether reconstruction is finite or completion-stable;
- whether the reconstructed action is source-derived or merely fitted.

RH is useful only as a hostile example in which extraordinarily complete
scalar shadows coexist with an unresolved source realization. The conjecture
does not depend on RH and should be judged across quantum control, software
state machines, physical transport, and finite algebraic sectors.
