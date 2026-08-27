# Recovery scope indexes the minimal process provenance

## Question

What is the smallest process record that must accompany an objective endpoint
record in order to authorize a declared recovery operation?

## Claim boundary

Let (mathcal P) be a set of source-authorized invertible processes on a state
space (S). For a declared recovery domain (D\subseteq S), define

\[
U\sim_DV
\quad\Longleftrightarrow\quad
U|_D=V|_D.
\]

The minimal information-theoretic provenance object for exact recovery on (D)
is

\[
P_D=\mathcal P/{\sim_D}.
\]

This quotient distinguishes precisely those process histories whose inverse
actions differ on the image of (D). It does not by itself construct or
physically execute the inverse.

If (D_1\subseteq D_2), restriction induces a canonical forgetting map

\[
q_{21}:P_{D_2}\longrightarrow P_{D_1}.
\]

There is generally no canonical arrow in the opposite direction. Expanding the
recovery scope requires additional provenance rather than inference from the
coarser record.

## Three recovery types

The word recovery must be replaced by one of three typed operations.

### Point recovery

Only one declared source state (x) must be returned from its endpoint. The
required provenance class is determined by (U(x)). This does not authorize a
physical inverse process or restore the environment.

### Domain recovery

Every state in a visible domain (D) must be recovered. The process restriction
(U|_D) must be retained.

### Global uncomputation

The complete system, environment, controller, and correlations must be restored.
The relevant domain is the full admitted carrier, and the full inverse-action
class must be retained.

These types have different information requirements and cannot be promoted into
one another by calling all three inversion.

## Exact finite census

Take all 24 permutations of four basis states as (mathcal P), with source
state zero and visible domain ({0,1}).

- Point recovery has four provenance classes, each containing six processes.
- Visible-domain recovery has twelve classes, each containing two processes.
- Global uncomputation has twenty-four singleton classes.

The forgetting ladder is therefore

\[
24\longrightarrow12\longrightarrow4.
\]

Each point class has three visible-domain lifts, and each visible-domain class
has two global lifts. Neither lift is canonical.

## Two-object DPC

An admissible reversible objective record is not one object. It is a typed pair

\[
(O,P_D),
\]

where (O) is the fault-qualified objective endpoint quotient and (P_D) is
the provenance quotient required by the declared recovery scope.

The interface coherencer must prove:

1. the endpoint represented by (P_D) agrees with the class in (O);
2. changing representatives in (P_D) does not change inverse action on (D);
3. fault correction for (O) does not silently claim correction of (P_D);
4. enlargement of (D) is accompanied by an authorized provenance lift;
5. completion preserves the relevant restriction and inverse-action classes.

## Authority ladder

Information-theoretic sufficiency is only the first gate. Recovery authority
requires three separate certificates:

1. Existence: a unique inverse action is determined on the declared domain.
2. Synthesis: a source-rooted constructor realizes that inverse action in the
   admitted operation language.
3. Execution: the synthesized constructor has an executable physical modality,
   resources, support access, and fault authority.

No arrow between these gates is automatic.

## Hostile cases

1. Same endpoint, different visible-domain actions: point provenance cannot be
   promoted to domain recovery.
2. Same visible restriction, different hidden action: domain provenance cannot
   be promoted to global uncomputation.
3. Unique inverse class without constructor: existence does not imply synthesis.
4. Synthesized inverse without physical modality: synthesis does not imply
   execution.
5. Corrected endpoint record with corrupted provenance: objective fault
   tolerance does not imply reversible recovery.

## Disposition

The finite DPC is closed. It corrects the overstatement that full process history
is always minimal: the necessary provenance is indexed by recovery scope. It
also proves that objective endpoint descent and recovery provenance form a
coupled pair linked by a nontrivial interface coherencer.

Verification is provided by
`research/nima/checkers/check_recovery_scope_provenance_ladder.py` and
`research/nima/results/recovery-scope-provenance-ladder.json`.
