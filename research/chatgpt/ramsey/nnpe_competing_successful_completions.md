# NNPE: competing successful completions with every primitive retained

Date: 2026-11-02.

## Result

Remove the assumption that a preferred return fails. Keep all six source operations
available. From the same retained packet after AB, the two continuations BA and
BC followed by CA both execute as endpoint-typed paths. Both retain their common
parent and complete histories. Neither execution is a repair of the other.

Under the previously proposed direct-corridor P/E and indirect-corridor N/N
colour binding, their selected active cycles have NNNN and NNPE boundaries.
A common marked neutral input can be protected in both constructions. This is a
positive coexistence result at the path-and-declared-port level. It is not a
physical decay or a proof that the native neutron constructor assigns these
boundary types.

The source extension accepts an explicitly supplied word. It does not decide
which word is executed. Thus the present result is not evidence that an
alternative becomes admissible only on a rare occasion: both remain admissible
under the tested endpoint rule, before and after any number of ordinary returns.

## 1. Source actually inspected

The current connector reads were:

- `research/nima/agda/SeedGeometricResponseState.agda`, lines 115–212, Git blob
  `383cc7c16480954adf0a071de5e7a7cc3aa7bcb2`.
- `research/nima/checkers/retained_path_successor.py`, lines 1–220 and 270–end,
  Git blob `c5432dc9a6ffcb405427130f656866592d0baa51`.
- `research/nima/checkers/check_indexed_path_synthesis.py`, complete file,
  Git blob `8a94b1c9180e0df1b552047335870a2b455d7e42`.
- `research/nima/native-transition-instrument.md`, Git blob
  `6a4e8154093d62e062543ca6aecb37e3b4be8cfd`.

The original six-arrow registry and preceding port assignment are retained from
the attached `nnpe_source_paths_and_selective_return_failure.md`. The registry
was originally extracted from `check_natural_tower_return.py`, blob
`dd8a9978e8d24745e8bb34e1774f5d56d4c00e33`.

The new Python audit independently implements the finite retained-path test and
uses the exact inspected `source`, `target`, and `compose` function bodies as a
labelled excerpt. It does not execute the complete ledger or the Agda compiler.
An attempt to download complete raw files for a wider replay failed because the
container could not resolve the network host. Connector reads succeeded; no
claim of a fresh complete upstream replay is made. No repository was modified.

## 2. Same input, two successful executions

The source registry is

```
AB: A -> B     BC: B -> C     CA: C -> A
BA: B -> A     AD: A -> D     DB: D -> B.
```

The common retained prefix is AB. It is executed once in the finite audit; both
candidate packet trees refer to that same immutable prefix object.

```
root(A) -> AB(B) -> BA(A)
                -> BC(C) -> CA(A).
```

The fork is an enumeration of alternative executions, not a claim that one
physical state was cloned into two simultaneously realized histories.

The inspected Agda `step-native` constructs a pointed target using the actual
edge equivalence and keeps its parent; `execute` recurses on an arbitrary
endpoint-typed word. Both return words therefore fit that declared native unary
transport extension. The module proves that their current effects differ; it
does not require one to fail or identify either history with an empty path.

All six occurrences stay in the registry. The new test has no unavailable-edge
parameter, corrupt-map parameter, error rate, or threshold. The difference is
which valid continuation is executed.

## 3. Complete first-return family and conditional boundary reading

There are two outward corridors and two return corridors:

```
x0 = AB             x1 = AD DB
 y0 = BA             y1 = BC CA.
```

The A-first-return family is exactly:

| Return | Source word | Declared active-cycle boundary |
|---|---|---|
| r00 | AB BA | NNNN |
| r01 | AB BC CA | NNPE |
| r10 | AD DB BA | NNPE |
| r11 | AD DB BC CA | PPEE |

The enumeration is complete: after removing A, the remaining directed graph is
acyclic, with only D->B->C. There are no longer first-return words hidden behind
a search cutoff.

The boundary column uses these additional bindings, unchanged from the prior
note:

```
x0: A.P -- B.E
 y0: B.P -- A.E
x1: A.Nout -- B.Nin
 y1: B.Nout -- A.Nin.
```

One outward and one return corridor are treated as active joins. Unselected
corridors retain their specifications and histories, while their endpoint flags
are external in this proposed presentation. The source does not itself identify
these labels as physical charges or turn traversal into active rewiring.

The four boundary counts are therefore conditional combinatorics, not native
particle-classification results. In particular, two NNPE words do not justify
a 1/2 branching probability. Primitive length also supplies no physical clock.

## 4. Same exterior attachments: an exact compatibility test

After x0 is joined, the free flags are

```
A.Nout, B.Nin, B.Nout, A.Nin, B.P, A.E.
```

The direct completion y0 consumes `B.P,A.E`; the indirect completion y1 consumes
`B.Nout,A.Nin`. They preserve the same flags `A.Nout,B.Nin`.

Let K be a set of protected external attachments: a protected flag cannot also
be used in a new internal join. Both completions are permitted precisely when

```
K is a subset of {A.Nout,B.Nin}.
```

Hence protecting the same marked incoming neutral flag `B.Nin` leaves both
completions available. This gives a concrete common-input context; an extra
operation failure is unnecessary.

If instead all four neutral flags are already fixed to the exterior, only the
direct completion is permitted by that fixed-attachment contract. The alternative
would need a larger reconstruction that accounts for those attachments. This is
not a claim that free-neutron decay is prohibited, nor that those four attachments
must be fixed physically.

All 64 protected subsets of the six-port intermediate were tested:

| Permitted second joins | Context count |
|---|---:|
| Both y0 and y1 | 4 |
| Only y0 | 12 |
| Only y1 | 12 |
| Neither | 36 |

These counts are finite context cases, not a distribution of physical states.
No context was selected because it gives a desired decay result.

## 5. Coexisting candidates are not simultaneous joins

For fixed x0, each of {x0,y0} and {x0,y1} has two junctions, two active corridors,
one independent cycle, and four free flags. Their union {x0,y0,y1} has three
active corridors, two independent cycles, and only the two free N flags of x1.

Thus executing every compatible join at once does not produce a four-leg object
with both interpretations. It produces a different, two-leg object. Retaining
all candidates and realizing one candidate are distinct operations. The user's
four-leg condition restricts the completed objects; it does not pick one of the
two admissible completions.

## 6. Success after arbitrarily many ordinary returns

Let h be any endpoint-typed history ending at A. Then both

```
h AB BA
h AB BC CA
```

are endpoint-typed extensions of that same h. This follows from the append law
and does not depend on how h was constructed. In particular it holds for
`h=(AB BA)^k` for every nonnegative integer k.

The audit checks k=0 through 64 as implementation controls. The universal claim
comes from endpoint typing, not extrapolation from those 65 cases. No primitive
wears out, vanishes, or becomes newly enabled in this model.

The four first-return words form a prefix-free code. Concatenating m returns
retains 4^m different source words. Exact checks for m=1,...,4 confirm this; the
general uniqueness follows by cutting a path at every visit to A. Keeping this
branching history is not the same as physically realizing all branches or
assigning a uniform law to them.

The word-count generating polynomial is `z^2+2z^3+z^4`. It counts primitive
occurrences per first return. It is not a probability-generating function unless
an independent probability model is added.

## 7. What the present source selects—and what it does not

The finite ledger's successor retains every compatible extension, with recoverable
parent slots. Its coefficient interface accepts supplied rational values. Neither
retention, copying, nor a decoder's averaging coefficients are an execution law
selecting a single source history.

The following policies all respect endpoint typing and complete history retention
without removing a primitive:

- repeat the direct return;
- execute the indirect return immediately;
- execute any chosen number of direct returns, then the indirect return.

The audit includes concrete executions of these as counterexamples to uniqueness,
not as new proposed physics. The existence of a source-typed query recorder does
not resolve the choice: the inspected native instrument note supplies different
source-changing operations that record the same query answer.

A genuine completion-selection law must therefore add information beyond the
bare endpoint execution relation: for example source-derived contextual coherence,
a history-sensitive dynamical action, or transition amplitudes on a physically
identified state space. This audit chooses none. It also does not presume that
every successful physical completion must satisfy equality of full retained
histories or full-state identity return.

The corrected next question is: which same-source completed objects satisfy the
actual realization conditions, and what determines their realization when more
than one succeeds? The alternative need not require the ordinary completion to
be impossible. An error probability is not a necessary starting parameter.

## 8. Reproduction and limits

Run `python completion_audit.py` with Python 3.10+ and the standard library.
It writes `results.json` and `external_attachment_contexts.json`.

The completed run passes 118 checks, including both shared-prefix returns,
all four first-return words, all 24 vertex relabellings, all 64 exterior contexts,
65 repeated-return prefixes, retained parent recovery, and the simultaneous-join
control. No floating-point calculation, microscopic error probability, measured
lifetime, particle energy, numerical cutoff for first returns, or new production
projector is used.

This establishes coexistence of successful source executions and compatible
conditional port completions. It does not establish the neutron-to-proton,
electron, antineutrino interpretation, a physical tensor-product output, selection
weights, irreversibility, or a decay time.
