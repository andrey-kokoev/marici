# 3807 — The Generic and Physical Rank-26 Source Orbits Have Different Word Relations

## Question

The generic twist `gamma = 5` and physical twist `gamma = -1/2` each carry a
rank-26 marked-relative quotient. Does identity on derivative words define a
canonical specialization between their source-generated covariant orbits?

## Frozen comparison

Use the `G12` residue chart at `(x,y,z)=(2,3,4)`, pole depth three, and the
complete labelled word family in the three external derivatives through word
length four:

```text
W_4 = union from r=0 to 4 of {0,1,2}^r.
```

Thus `dim W_4 = 121`. No word is removed after inspecting either fiber.
Let

```text
ev_5    : W_4 -> H_5,
ev_half : W_4 -> H_half
```

be the source-derived covariant-word evaluation maps followed by the complete
twist-specific reduction.

## Exact finite-field result

At both primes `32003` and `32009`:

```text
rank(ev_5)                         = 26
rank(ev_half)                      = 19
dim ker(ev_5)                      = 95
dim ker(ev_half)                   = 102
dim(ker(ev_5) intersect ker(ev_half)) = 86
```

The physical orbit therefore has codimension seven in its rank-26 quotient,
but the relation discrepancy is not exhausted by seven additional physical
relations. The two kernels contain twist-specific directions on both sides.
In particular,

```text
ker(ev_5) is not contained in ker(ev_half).
```

Identity on labelled derivative words consequently does not descend from the
generic source orbit to the physical source orbit.

The mismatch is already visible in the 40-word prefix through length three:
both prefix evaluations have rank 19, both kernels have dimension 21, and
their intersection has dimension 20. It is not produced only by the seven
generic directions appearing at length four.

## Narrow conclusion

Equal quotient dimension does not provide a canonical generic-to-physical
comparison. The physical half-twist is not the identity specialization of the
generic derivative-word module, and its source orbit is only rank 19 while
the generic orbit reaches rank 26.

A comparison now requires an independently derived twist-changing morphism or
a homotopy that transports the full relation defect. Choosing convenient
independent words in each fiber would only choose bases and would not supply
that missing morphism.

This result does not alter the rank-26 geometric closure and does not obstruct
constructing the physical Leray covector directly at `gamma = -1/2`.

## Artifacts

- `research/benincasa/checkers/check_rank26_twist_word_kernel_transport.py`
- `research/benincasa/results/rank26-twist-word-kernel-transport-k3-p32003.json`
- `research/benincasa/results/rank26-twist-word-kernel-transport-k3-p32009.json`

Allocator claim: `seqclaim-9174febfb2a06b7df26b00de`.
