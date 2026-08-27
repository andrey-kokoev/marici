# Provenance determines a maximal recovery domain

## Question

Given the process distinctions actually retained by a provenance record, what
is the largest state domain on which an inverse action is determined?

## Claim boundary

Let (mathcal P) be a source-declared process family acting on a state set
(S). A provenance record induces an equivalence relation (E) on
(mathcal P): processes in the same class are no longer distinguished.

Its recoverable domain consists of the states on which every provenance-
equivalent pair agrees:

\[
R(E)=
\{x\in S:\forall(U,V)\in E,\ U(x)=V(x)\}.
\]

Conversely, a declared probe domain (D\subseteq S) induces the process
equivalence

\[
K(D)=
\{(U,V):U|_D=V|_D\}.
\]

These operations satisfy

\[
D\subseteq R(E)
\quad\Longleftrightarrow\quad
E\subseteq K(D).
\]

Thus retained provenance and recoverable state scope form a Galois connection.
The induced domain closure is

\[
C(D)=R(K(D)).
\]

It contains every explicitly probed state and may contain more when the source
process laws force the missing action.

## Exact permutation witness

Let (mathcal P=S_4), the 24 permutations of four states.

- No probes determine no state action.
- One probe closes only itself.
- Two probes close only themselves.
- Three probes determine the fourth image by bijectivity, so their closure is
  the complete four-state domain.

Therefore three ordered state probes determine every permutation in (S_4).
The fourth port is not an independent measurement; it is forced by the
source-authorized conservation law that every process is bijective.

## Hostile noninvertible family

For the family of all functions (S\to S), agreement on three states does not
determine the fourth. Two functions may agree on the probed triple and differ
arbitrarily on the remaining input.

The three-to-four closure is therefore not a dimensional fact. It depends on
the declared process law. Dropping bijectivity removes the coherencer that
derived the fourth action.

## Extensional and intensional recovery

The Galois connection recovers extensional process action: what the composite
does to states. It does not recover an intensional factorization history.

Distinct histories may have the same composite action. For example, a
two-stage identity history and a two-stage history using the same involution
twice both compose to identity. Even probing every state cannot distinguish
their factorization.

Accordingly there are two provenance carriers:

1. action provenance, sufficient for a declared extensional inverse;
2. factorization provenance, required to replay, audit, fault-localize, or
   authorize the original constructor stages.

No state-probe closure reconstructs the second from the first.

## Inverted DPC

Given a candidate provenance packet (E):

1. derive (E) from the actual record format rather than declaring desired
   distinctions;
2. compute (R(E));
3. prove the source process family and its conservation laws;
4. distinguish extensional action from intensional factorization;
5. test fault survival of the provenance packet;
6. establish inverse existence, synthesis, and execution separately;
7. verify that completion does not shrink (R(E)) or merge required process
   classes.

The first finite falsifier is a pair (U\mathrel E V) and a claimed recovery
input (x) for which (U(x)\neq V(x)).

## Disposition

The inverted finite DPC is closed. Provenance determines a maximal recoverable
domain, and source laws can enlarge that domain beyond the explicit probe set.
For permutations of four states, three probes force the fourth. This closure
does not reconstruct factorization history or grant physical execution
authority.

Verification is provided by
`research/nima/checkers/check_provenance_recovery_galois.py` and
`research/nima/results/provenance-recovery-galois.json`.
