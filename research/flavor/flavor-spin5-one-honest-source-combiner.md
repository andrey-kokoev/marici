# Spin(5) one-honest-source setting combiner (WP915)

## Question

Can WP914's single setting-source trust be weakened by combining several
reference sources under an explicit causal protocol?

## Exact XOR theorem

Let (H) be a uniform bit independent of the Bell devices and every other
source record (A). Then

\[
S=H\oplus A
\]

is uniform even when (A) is arbitrarily biased. Conditional on any fixed
value of (A), XOR by (A) is a permutation of the two values of (H).
The same theorem applies bitwise to fixed-length strings.

This yields a disjunctive-trust constructor: several sources may contribute,
and the combined setting string is uniform if at least one contribution is
uniform and independent of the devices and of the other contributions at the
time they become binding.

## Commit-then-reveal protocol

For every setting block:

1. each source publishes a signed commitment to its contribution and block
   identifier;
2. all commitments become immutable;
3. sources reveal their strings with inclusion proofs;
4. the verifier rejects missing, late, duplicated, or invalid reveals;
5. the admitted strings are XORed in canonical source order;
6. the combined string is allocated immutably to Bell setting trials.

The NIST randomness-beacon reference specifies signed, timestamped,
hash-chained pulses and precommitment to future randomness, and discusses
combining beacons. It is an implementation precedent for the transcript shape,
not proof that a particular pulse is independent of the Bell devices:
[NIST IR 8213](https://csrc.nist.gov/pubs/ir/8213/ipd).

## Exact attacks

The theorem fails if the independence premise fails. If (A=H), then
(H\oplus A=0) always although both inputs are marginally uniform. An adaptive
source that learns (H) before choosing (A) can make the same cancellation.
Commitment prevents this adaptation only under its binding assumption and only
when the honest contribution remains hidden or unpredictable until the other
sources are bound.

Two weak or biased sources do not automatically amplify one another. XOR is
uniform from the stated one-honest-source condition, not from source count,
marginal health tests, or signed provenance alone.

## Changed groupoid and boundary

WP915 adds a multi-source commitment transcript and an XOR allocation port.
The physical groupoid is the stabilizer of source identities, commitment
order, block identifiers, reveals, and the combined setting allocation.
Permuting unlabeled aggregate bits is not an admitted equivalence.

This reduces trust from one named source to the claim that at least one source
is causally outside the common cause. It cannot remove all causal assumptions.
A real instrument still requires geographically and administratively diverse
sources, authenticated commitments, timing/isolation evidence, a declared
threat model, and a proof that at least one contribution is independent of the
devices when binding occurs.

The combiner supports the Bell reference experiment only. It is neither flavor
selector nor texture rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp915_spin5_one_honest_source_combiner.py
~~~
