# Timeless calculus on the mixed-Green hostile

## Known packet

This illustrates the calculus on Kitaev's packet
`research/kitaev/the-mixed-green-pairing-does-not-descend-through-endpoint-compression.md`.
The packet supplies a source-admissible hostile, not an invented analogy.

## Marked carrier germs

The two units are half-line graph-carrier germs

\[
G_+\in H^1(\mathbb R_+),
\qquad
G_-\in H^1(\mathbb R_+).
\]

Their types distinguish the two oriented sectors. Their identity tokens retain
which source graph each carrier belongs to. Their comparison ports are the
endpoint traces

\[
\tau_0(G_+),\qquad\tau_0(G_-).
\]

Nothing here is an event. The half-line coordinate labels the carrier domain;
it need not be interpreted as time.

## The two local `2+1` cells

For each sign, the forward incidence is the source operator

\[
D_{s_\pm}G_\pm=G_\pm'+s_\pm G_\pm.
\]

The reciprocal incidence solves the source equation back to its graph carrier.
The local mate is endpoint compatibility. Sewing locally forms the trace
equalizer

\[
\mathcal D_+\times_{\mathbb C}\mathcal D_-.
\]

This mate constrains the ports without consuming the full carriers.

## Outer `+1`

The outer relational mate is the mixed Green pairing

\[
\beta(G_+,G_-)=\int_0^\infty G_+(q)\overline{G_-(q)}\,dq.
\]

Choose a nonzero smooth compactly supported carrier `h` away from the endpoint
and set both graph carriers to `h`. Define each source by applying its declared
incidence operator. Then both endpoint ports are zero, so the local equalizer
passes, while

\[
\beta(h,h)=\lVert h\rVert_2^2>0.
\]

## Failure of local-first `3+2+1`

If each local tower consumes its carrier into the scalar endpoint quotient
first, the available record is only `(0,0)`. Every choice of nonzero zero-trace
tail produces that same completed record. The mixed pairing cannot be a
function of those two scalars.

The descent residual is the positive norm of `h`. This is an exact kernel
obstruction, not numerical instability.

## Success of relational-first `2(2+1)+1`

The correct composition is:

```text
plus graph cell  -- endpoint port --\
                                     trace equalizer -- mixed Green mate
minus graph cell -- endpoint port --/
```

Both local `2+1` cells close their source and trace compatibility while keeping
the carrier germs. The outer `+1` evaluates the mixed pairing. Only afterward
may the radical of the complete relation be quotiented and scalar readouts be
formed.

## Where realization and time enter

They do not enter this obstruction. A later realization map may identify a
carrier with a sampled tail, spectral record, cutoff history, or laboratory
trace. An ordering may then be imposed on those records. The non-descent proof
is already complete before either operation.

## Finite executable shadow

The checker uses one boundary coordinate and two interior carrier modes. The
hostile `h=(0,1,-1)` has endpoint trace zero and self-pairing two. Declared
finite incidence maps generate exact plus and minus sources. Local scalar
completion returns `(0,0)`; relational-first sewing returns pairing two.

## Claim boundary

This illustrates the packet's proved mixed Green obstruction. It does not
promote that result to the complete alternating physical polarization, whose
independent-tail audit remains open in Kitaev's packet.

## Disposition

The hostile shows the timeless calculus in its minimal nontrivial form:
carrier germs, incidence pairs, a port equalizer, a relational mate, and a
quotient whose admissibility is decided by the mate's kernel contraction.

## Verification

Run:

```text
python research/aspect/checkers/check_timeless_calculus_on_mixed_green_hostile.py
```
