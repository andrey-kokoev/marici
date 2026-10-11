# Three incoming arrows: a cyclic-compatible receiver

## Primitive extension

Keep the four-state proton graph with its twelve directed nonidentity generators. Select ABC and add only

```text
A → e, B → e, C → e.
```

There are fifteen primitive arrows. The induced graph on A,B,C,e has nine arrows: six inherited among A,B,C and three entering e. It is not a second twelve-arrow complete directed graph. There are no outgoing primitive arrows from e.

Every closed primitive traversal remains wholly in the old graph. Thus closed-cycle retention alone cannot justify the new arrows. Their proposed role is instead a retained three-input compatibility relation.

## Signal interpretation, using the existing cyclic character

Give the three source channels and receiver values in K=Q(sqrt(-3)). Use the existing triangle-coordinate action

```text
C(a,b,c)=(b,c,a),
omega=(-1+sqrt(-3))/2.
```

Retain its selected omega character. Seek nonzero scalar incoming maps whose compatible triples are exactly that character's eigenline. This explicitly specifies what the receiver is to preserve; it is not implied by the fifteen-arrow graph alone.

Writing the maps as f_A(a)=αa, f_B(b)=βb, f_C(c)=γc, compatibility on (z,omega z,omega²z) requires

```text
α = beta*omega = gamma*omega².
```

After the common normalization α=1, the three incoming maps are therefore

```text
f_A(a)=a,
f_B(b)=omega² b,
f_C(c)=omega c.
```

These phases are derived from the retained character, not fitted to the later 1836-arrow return matrix.

## The actual pullback

The common target is e. The three maps define the iterated pullback

```text
W = {(a,b,c): a=omega² b=omega c}.
```

Exactly

```text
W = {(z,omega z,omega²z): z in K}.
```

The equal-image map W→e and the decoder

```text
e → W, z ↦ (z,omega z,omega²z)
```

are inverse linear maps. Consequently the receiver value can represent the entire compatible triple, provided the incoming maps and channel labels are retained. This is stronger than merely declaring three arrows to have the same endpoint.

The inverse data maps here certify reconstruction. They do not add outgoing primitive arrows or grant free reverse traversals in the protocol. Implementing reconstruction as an executed process would need its own accounting.

## What happens under the face cycle?

The compatibility relation is preserved, but the common value changes:

```text
C(z,omega z,omega²z) = (omega z,omega²z,z),
receiver value z → omega z.
```

Thus the receiver carries the cyclic action. It is not a value forced to remain invariant under every source move. Requiring that stronger invariance gives z=omega z, hence only z=0.

Similarly, assigning unit weight to all three incoming arrows yields the diagonal line (z,z,z), the trivial cyclic character. It does not retain the selected nontrivial character. Reversing the cycle conjugates the phase pattern.

This is equivariance under the selected face cycle, not a claim that the receiver is an ordinary commuting cocone over all twelve original arrows. The latter would require further transport equations and must not be silently assumed.

## Are all three incoming arrows needed?

Yes, for this specific compatibility relation with all three input channels retained. Delete any one leg and its input becomes unconstrained: the compatible subspace of K³ grows from dimension one to dimension two.

For example, deleting A→e accepts (0,omega,omega²), because the two remaining images are both 1. The missing A image would have been 0, so the original three-way relation rejects it. The checker supplies analogous witnesses for all three deletions.

This is deletion-essentiality of the compatibility relation, not a claim of global minimum implementation cost. If the only observable were an already supplied receiver value z, there would be no such three-input verification obligation.

All fifteen primitive arrows also have explicit finite paths ending at e. These are open terminal-path witnesses, not newly manufactured cycles or a proof of the old closed-cycle pruning theorem.

## What this gives us

The proposal has a concrete mathematical realization:

- one unchanged twelve-arrow proton-like source;
- three incoming legs rather than a second complete arrow network;
- one receiver channel encoding a retained cyclic-compatible triple;
- a deletion test explaining why each leg matters.

It supplies a genuinely different role for the new vertex. It does not yet choose its spatial apex height, identify it with a barycenter, or construct the extended full coefficient protocol. Those must be generated from this new source rather than borrowed from the earlier two-tetrahedron attachment.

## Verification

```text
python research/voevodsky/checkers/check_three_arrow_receiver.py
```

Fifteen exact checks pass: graph preservation, absence of new cycles, terminal-path coverage, exact equality of the pullback and cyclic eigenspace, covariance, reconstruction, three deletion counterexamples, and controls for unweighted or strictly invariant receivers.

Artifacts: `results/three_arrow_receiver_store.json` and `results/three_arrow_receiver.json`. The primitive triangle-character implementation is hash-bound; no existing source or visualization is modified.
