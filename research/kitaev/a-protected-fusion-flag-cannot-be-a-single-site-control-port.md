# A protected fusion flag cannot be a single-site control port

Owner: `marici.Kitaev`

## Bounded question

Can the four-anyon fusion flag directly control the qutrit bus through a
bounded local interaction while its constituent anyons remain separated and
topologically protected?

## Verdict

No on any support class for which the fusion channel is locally
indistinguishable.

The `A_F/B_F` flag is stored in a joint fusion relation. An operator supported
near only one constituent acts as a scalar on the protected fusion space, so
it cannot contain a nonzero term proportional to the flag projector. A
constant-strength flag-conditioned bus interaction must therefore use one of
three actuation corridors:

1. extended support enclosing or connecting the relevant anyons;
2. motion, fusion, or code deformation that makes their joint charge local;
3. a distributed quantum bus crossing the protected cut.

The flag can be protected during storage or locally exposed during actuation.
The transition between those regimes is part of the constructor.

## Exact compression obstruction

Let `Pi_F` project onto the two-dimensional total-vacuum fusion space spanned
by `A_F,B_F`. Let `O_R` be any accepted charge-preserving operator supported
in a correctable region `R` that meets at most one isolated constituent
neighborhood. Local indistinguishability gives

\[
\Pi_F O_R\Pi_F=c_R\Pi_F.
\]

Now couple that region to an arbitrary bus by

\[
H_{RB}=\sum_j O_{R,j}\otimes h_{B,j}.
\]

Compression to the protected fusion space yields

\[
(\Pi_F\otimes I)H_{RB}(\Pi_F\otimes I)
=
\Pi_F\otimes\sum_j c_{R,j}h_{B,j}.
\]

The result is independent of the `A_F/B_F` flag. In particular its coefficient
of

\[
(P_{A_F}-P_{B_F})\otimes h_B
\]

is zero for every non-scalar `h_B`.

Thus no sum of interactions confined to one correctable constituent region
can implement the desired conditional actuator at first order inside the
fixed protected subspace.

## Approximate version

If local indistinguishability is approximate, define

\[
\epsilon_R(O)
=
\inf_c\|\Pi_FO\Pi_F-c\Pi_F\|.
\]

The norm of every flag-dependent compressed component is at most
`epsilon_R(O)`. If this defect decays exponentially with anyon separation,
then a normalized local flag-to-bus coupling is exponentially weak. A gate
using only that projected interaction has an exponentially growing time.

This is not an extra failure of the code. It is the same suppression that
protects the stored fusion flag from local noise.

## Three authorized corridor types

### Extended charge loop or ribbon network

A Wilson loop surrounding the relevant pair, or a ribbon network joining its
world tubes, can resolve their total charge. Its support diameter grows with
their separation. A local microscopic implementation must propagate around
that support, so a bounded-velocity dynamics incurs a time at least linear in
the relevant distance before an order-one conditional signal can form.

The advantage is that the anyons need not be fused. The price is a nonlocal
actuator and an extended fault surface.

### Move, fuse, and separate

Transport the anyons until their joint charge becomes locally measurable or
energetically split. The flag projector can then couple strongly to a local
bus. During approach and fusion, the original separation-based protection is
reduced or absent.

The constructor must specify the return path, dynamical phases, leakage, and
whether the same fusion record that enables control destroys the route
coherence.

### Distributed coherent bus

Keep the anyons separated but send a quantum bus through both neighborhoods.
Sequential interactions can accumulate the joint predicate coherently and
return the bus cleanly.

This preserves spatial separation of the anyons but transfers the vulnerable
logical relation into the bus history. A single bus fault can become a
correlated logical fault, and exact uncomputation is mandatory.

## Locality trilemma

For increasing separation, the following three properties cannot all hold for
one fixed support class:

1. the fusion flag remains locally indistinguishable and hence protected;
2. the actuator has bounded support near one constituent;
3. the flag-conditioned interaction has a separation-independent nonzero
   strength within the protected space.

Keeping the first and second forces the third to vanish. Keeping the first and
third requires extended or distributed support. Keeping the second and third
requires opening the encoding so the flag is no longer locally hidden.

This is the physical meaning of the actuator incidence missing from the
abstract endpoint algebra.

## Middle exchange does not evade the bound

The native middle electric exchange realizes the flag reflection on the
fusion space. Its worldline is a two-anyon operation, not a single-site
Hamiltonian supported near one isolated constituent. If the anyons are far
apart, implementing the exchange requires motion or an extended braid path.

Thus the exact braid word confirms the logical operator but does not violate
local indistinguishability. Its spacetime support is already an actuation
corridor.

## Consequence for the shared-port proposal

Using the fusion qubit itself as the common control port is possible only if
the port-to-bus coupling is placed on one of the three corridors above. The
architectural alternatives are now explicit:

```text
protected remote flag + extended interaction
protected remote flag + travelling coherent bus
temporarily exposed flag + local strong interaction
```

A declaration that the bus is simply adjacent to the flag omits the central
question: which spatial region contains the flag's joint fusion information?

## Highest-information source calculation

Freeze an anyon separation `L` and a candidate microscopic support region.
Compute the compression of the proposed interaction to the `A_F/B_F` space.
The first useful output is one of:

- exactly scalar compression;
- a finite-separation flag component with its norm as a function of `L`;
- an extended-support flag component with explicit diameter;
- a time-dependent deformation path with a recovered-channel bound.

This directly prices the control corridor. Another calculation of the
abstract fusion projector does not.

## Falsifiers

- An accepted operator near one isolated simple anyon distinguishes the joint
  `A_F/B_F` fusion channel inside the locally indistinguishable code space.
- A sum of scalar compressed terms acquires a flag-dependent first-order
  compression without leaving the fixed subspace.
- Exponentially small local splitting is called constant-time control.
- Middle exchange is described as a single-site operation independent of
  anyon separation.
- A distributed bus is claimed to create no correlated fault path.
- Moving or fusing the anyons is treated as preserving the original storage
  projector throughout without a deformation theorem.
- A source-derived bounded-support interaction already has a uniform nonzero
  `P_BF`-conditioned bus component at arbitrary protected separation.

## Claim boundary

This packet applies the established local-indistinguishability control bound
to the specific four-anyon flag. It does not choose among the three corridor
architectures or derive microscopic scaling constants.

Its exact result is a locality classification: the native fusion flag cannot
be used as a single-site control port while remaining hidden in the same
protected support class. Any executable conditional coupling must expose its
joint charge through explicit spacetime support.

No build, checker, or Git operation was used.
