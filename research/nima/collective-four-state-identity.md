# Twelve four-state elements and one collective identity

## Local four-state split

Each element has states A,B,C,D. Its sixteen operator coordinates split into twelve off-diagonal relations and four diagonal coefficients. The diagonal coefficients split as

    (a,b,c,d) = mean(a,b,c,d)*(1,1,1,1) + three independent contrasts.

Thus there are four states, not a separate three-state subsystem. The three contrast directions can be AA-DD, BB-DD and CC-DD. Their common complement represents the local unit I4=AA+BB+CC+DD.

The previous phase-net's H ports can encode these contrast coordinates. Its Fourier weights require an orthonormal contrast basis if interpreted with the Hilbert-Schmidt norm; the simple differences above are a spanning basis, not an orthonormal basis. This is a linear coefficient model, not an asserted quantum channel.

## Explicit collection and return

Let z_c be the complex amplitude of the local unit contribution at element c. Define the collection and return maps

    G(z) = (z_0+...+z_11)/12,
    S(alpha) = (alpha,...,alpha).

Then GS=1 on the common scalar and SG=P, where

    P=ones(12,12)/12, P²=P, rank(P)=1.

Twelve aligned unit contributions give G(1,...,1)=1. Returning that common amplitude reconstructs the same aligned vector. This gives an explicit double-pass identity on the collective line.

Alternating signs cancel. Twelve equally spaced phases cancel. A common phase is preserved by P, but exp(i*theta)*I is not an algebraic unit unless that phase equals one. The fixed collective eigenline and its possibly rotating amplitude are distinct objects.

The relative complement I-P has rank eleven. If the input amplitudes are independent, those eleven modes must be retained for lossless recovery. Projection alone suppresses them; no phase alignment dynamics is proved by writing P.

## Arrow budget for explicit transport

Use actual local-unit ports u_c and one common port Omega:

    u_c -> Omega   weight 1/12,
    Omega -> u_c   weight 1.

These are twenty-four unique directed endpoint pairs. The effective projector P has 144 nonzero matrix entries because it composes these arrows; those 144 composite entries are not twenty-four primitive links.

Adding the explicit interface to the preceding net gives:

| Part | Arrows |
|---|---:|
| Relation transport | 1728 |
| Diagonal-contrast transport | 108 |
| Collection into Omega | 12 |
| Return from Omega | 12 |
| Total | 1860 |

There are 193 port nodes: 180 active coefficient ports, twelve local-unit ports and Omega. All common-interface arrows have different endpoint types from the 1836 active transport arrows, so none disappears under deduplication.

For simultaneous hub transport W, W² is the projector onto the coherent local-unit line plus the hub coordinate. Its rank is two in the thirteen-port interface. W^12=W². The twelve-step return fixes that coherent interface subspace, not arbitrary relative local-unit inputs.

## Alternative: one unit shared algebraically

There is a different implementation if every local element is an algebra on a factor of a composite system. Its local identity embeds as the SAME global unit:

    embed_c(I4)=I_global, for all twelve c.

The eleven differences between these representations are then redundant coordinates, not independent physical amplitudes. The one-body operator space has dimension

    1 + 12*(16-1) = 181.

It consists of one common unit, 144 local off-diagonal coordinates and 36 local diagonal contrasts. It is an operator subspace, not the whole tensor-product algebra and not closed under general products of different sites' operators.

In this shared-unit representation the earlier 1836 active arrows can be retained with the global unit fixed. There is no collection transport to count. If the global identity's own self-loop is explicitly included in the arrow set, it contributes one additional arrow.

This alternative must not be called an implementation of the twenty-four-link collection graph. One identifies a unit algebraically; the other transports independently presented contributions and takes their coherent projection.

## Verification

    python research/nima/checkers/check_collective_four_state_identity.py

Exact rational tests verify the local four-state split, both collective inverse/projector identities, ranks 1 and 11, alternating-phase cancellation, lossless reconstruction when the relative component is retained, all twenty-four interface arrows, the hub's twelve-step projector return and the eleven shared-unit relations. A complex numerical check also verifies cancellation of uniformly distributed phases.

Artifact: `results/collective-four-state-identity.json`.
