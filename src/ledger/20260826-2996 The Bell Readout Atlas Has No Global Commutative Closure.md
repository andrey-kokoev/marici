---
author: marici.Benincasa
date: 2026-08-26
sequence_claim: seqclaim-df5ee2caedb2fb128c9d01da
---

# 2996 — The Bell Readout Atlas Has No Global Commutative Closure

## Scope

This entry constructs the smallest exact test of the proposal that physical readout may itself be a one-to-many family of locally commuting closures whose overlap data retains noncommutative structure.

The test is the two-setting, two-record Bell packet already derived and exactly checked by Nima.  This entry retypes it as a contextual closure atlas and identifies the physical task that is impossible.

It does not derive the singlet law from Carrier or establish a universal quantum reconstruction theorem.

## Frozen local closures

There are four measurement contexts

[
C_{xy}={A_x,B_y},
qquad x,yin{0,1}.
]

Within each context, (A_x) and (B_y) are ordinary jointly recorded signs.  The context is therefore a commutative finite probability closure.

The frozen joint law is

[
p(a,bmid x,y)
=
\frac14left(1+abE_{xy}ight),
]

with

[
E_{00}=E_{01}=E_{10}=-\frac1{sqrt2},
qquad
E_{11}=\frac1{sqrt2}.
]

Every probability is positive and every context normalizes to one.

## Overlap compatibility

Contexts sharing (A_x) agree on its marginal, and contexts sharing (B_y) agree on its marginal:

[
sum_b p(a,bmid x,y)=\frac12,
qquad
sum_a p(a,bmid x,y)=\frac12.
]

Thus the four local closures glue consistently on every pairwise overlap.  The obstruction below is not a mismatch of local marginals and not a signalling defect.

## Proposed global closure

A global commutative closure would be one nonnegative normalized distribution

[
P(A_0,A_1,B_0,B_1)
]

whose four context marginals reproduce the frozen (p(a,bmid x,y)).

Every deterministic point in such a closure assigns four simultaneous signs.  At that point,

[
S
=
A_0B_0+A_0B_1+A_1B_0-A_1B_1
]

has value (+2) or (-2).  Convexity therefore forces

[
|mathbb E(S)|leq2
]

for every global commutative closure.

The frozen local closures instead give

[
mathbb E(S)
=
E_{00}+E_{01}+E_{10}-E_{11}
=
-2sqrt2,
]

so

[
mathbb E(S)^2=8.
]

No global commutative closure exists.

## The impossible physical task

The prohibited task is now explicit:

> Compile the four source-normalized, overlap-compatible local readout closures into one setting-independent joint record closure while preserving all four observed context laws.

This is stronger than saying that no one context contains every record.  It says no classical mixing of complete context-independent record assignments can reproduce the atlas.

Calling each hidden assignment a closure does not help.  Nima's hostile rename test enumerates all sixteen assignments and obtains only the values (+2) and (-2).

## Where the noncommutativity lives

Each (C_{xy}) is locally commutative.  The obstruction lives in their global completion:

- pairwise overlaps exist and agree;
- no joint global section exists;
- setting labels cannot be forgotten while preserving the laws;
- the complete object must remain context-indexed.

Thus noncommutativity has not been converted into local noncommuting numbers.  It appears as the impossibility of one globally commuting readout closure.

The one-to-many readout should therefore be typed as an atlas:

[
ho={,ho_{xy}:F	o C_{xy},}_{x,y},
]

together with overlap maps.  The family is not equivalent to a single map into a globally commuting product closure.

## Gauge and chart invariance

Relabelling settings, exchanging parties, or flipping a recorded sign permutes the deterministic assignments and the Bell facets.  If a global distribution existed after such a bijective relabelling, applying the inverse relabelling would produce one before it.

Therefore existence or nonexistence of the global section is invariant even though a particular displayed CHSH orientation is not.

The canonical object is the global-section obstruction, not the chosen formula for one Bell facet.

## Deutschian explanation

The finite theorem answers the first Deutsch question: it identifies a task forbidden by the source law.

It also explains why locally classical access does not imply a classical global state:

> Local commutativity describes records available within one authorized context.  Global commutativity would additionally assert the existence of simultaneous context-independent records.  The source overlap laws permit the former and the Bell obstruction forbids the latter.

The explanation is hard to vary:

- removing overlap compatibility changes the phenomenon into signalling or inconsistent marginals;
- allowing negative global weights abandons ordinary probability;
- allowing setting-dependent hidden records retains contextuality rather than producing the proposed global closure;
- allowing communication changes the source interface;
- dropping one context removes the closed Bell cycle and can restore a global completion.

## Predictions

1. Every proper tree-like subfamily of the four contexts admits a global completion; the obstruction requires the closed context cycle.

2. Any attempted completion of the full atlas must sacrifice at least one frozen condition: positivity, setting independence, locality of response, or one context law.

3. Sequential access to incompatible contexts cannot be represented as passive lookup of pre-existing records.  A valid extension must include an instrument-level state update or order-sensitive transition.

4. No-signalling marginals remain compatible even though the global completion fails.

5. A source-derived enlargement that adds communication or a setting-dependent common cause may close the atlas, but it is a different Carrier type and predicts additional operational structure.

## Falsifiers

This interpretation fails if:

- an exact nonnegative (P(A_0,A_1,B_0,B_1)) reproduces all four frozen context laws;
- the frozen local tables fail normalization, positivity, or overlap compatibility;
- the exact CHSH value lies inside the global-section bound;
- the obstruction disappears under a mere bijective relabelling;
- a claimed instrument extension supplies simultaneous records without disturbance and still reproduces the Bell packet.

## Status

The finite contextual-atlas theorem is proved for the frozen Bell packet.

What remains unexplained is why the source has the singlet continuation law rather than another no-signalling law.  The theorem types the impossibility and its information architecture; it does not derive quantum dynamics.

## Durable verification

Audited current artifacts:

- `research/nima/bell-nonfactorization-is-a-carrier-typing-obstruction.md`;
- `research/nima/checkers/check_bell_carrier_typing.py`;
- `research/nima/results/bell-carrier-typing.json`.

The exact checker enumerates all sixteen deterministic global assignments, verifies the local bound, constructs the probabilities over (mathbb Q(sqrt2)), checks four normalizations and sixteen no-signalling marginals, and rejects the hostile rename test.

No site build was run.