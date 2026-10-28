# Channel trade: ordinary coning versus a retained role-transfer rule

## Tested proposal

Starting at rung12 with three inputs and twelve outputs, each downward step
changes (I,O) to (I+1,O-1), through rung4 with eleven inputs and four outputs.
The proposed cause is coning.

This audit tests ordinary finite simplex incidence and a separate labelled
channel-partition interpretation. It does not assume a new routing law or an
identification with the existing WG transport APIs.

## Executed results

Run:

```sh
python research/realization-tower/check_channel_trade.py
```

Receipt: [results/channel-trade-v1.json](results/channel-trade-v1.json).
All audit assertions passed, including 5,460 first-step role-partition cases.
Passing the audit does **not** mean the coning proposal passed.

| Interpretation | Exact result |
|---|---|
| Whole tetrahedral directed-edge carrier | 12 directed edges |
| One tetrahedral vertex | 3 incoming and 3 outgoing edges |
| Link at that vertex in the filled tetrahedron | Triangle: 3 vertices and 6 directed edges |
| Cone over the tetrahedron | Five vertices, 20 directed edges; 4 incoming and 4 outgoing at each vertex |
| General filled simplex with n vertices | Coning changes n(n-1) directed edges to n(n+1), adding 2n |
| Standard twelve FCC nearest-neighbour directions at a point, split by any of the four tetrahedral plane orientations through it | 3 on one side, 6 tangent, 3 on the other |
| Fifteen independently supplied tokens partitioned into inputs and outputs | Moving one output token to inputs gives exactly (I+1,O-1) |

The plane test concerns the standard nearest-neighbour directions, not an
unspecified longer-path reachability or causal channel law. Plane normals alone
do not designate an input/output assignment.

## Surviving conclusions

1. **Cone/link recovery survives exactly.** A marked tetrahedron is the cone
   over its opposite triangle, and its apex link recovers that triangle. The
   three outgoing apex edges correspond to the three link vertices; they are
   not the six directed edges of the triangle.
2. **The proposed arithmetic survives as a retained role-transfer rule.**
   With a supplied fifteen-token carrier, moving a token from outputs to inputs
   preserves all tokens and gives the requested rung12–4 counts.
3. **Ordinary coning does not realize that trade.** It adds vertices and edges;
   it does not turn twelve outputs into eleven. The inverse link operation
   also does not give that one-for-one channel count from ordinary edge incidence.
4. **Three local channels and twelve total arrows are different scopes.**
   The existing tetrahedral carrier cannot supply a disjoint 3-input/12-output
   partition merely by counting its arrows. Additional roles, copies, paths or
   a routing construction would have to specify such a partition.
5. A tetrahedron has fifteen nonempty faces, with counts 4+6+4+1. This is a
   mixed-dimensional face count, not fifteen arrows and not a canonical choice
   of three inputs. The numerical coincidence alone supplies no adapter.

## What is recorded, and what remains open

The claimed identification **ordinary coning = one-input/one-output trade** is
not realized in the tested models. The narrower, explicit survivor is:

> A retained channel-role transfer can implement I+O=15 and the proposed
> numerical rung schedule. A decorated cone/routing construction inducing that
> transfer has not yet been specified or verified.

Do not install the arithmetic schedule as a replacement for the existing
six-object/three-transport diagram. No graph concept version, physical
interpretation, older proof outcome or task frontier is changed by this test.

A next test needs an actual definition of a channel at a selected dot, a
consistent local/global interface, and the decorated operation that selects and
retypes one output as input. That would test a new mechanism rather than rename
the partition update 'coning'.
