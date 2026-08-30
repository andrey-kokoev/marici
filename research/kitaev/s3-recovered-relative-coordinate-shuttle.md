# Recovered relative-coordinate shuttle

Owner: `marici.Kitaev`

Status: exact finite gadget and conditional single-fault theorem; executable
fault-tolerant logical multiplication and recovery remain uncompiled.

## Question

The encoded-bus audit left one weight-two primitive: the reversible relative
coordinate

\[
(x,y)\longmapsto (x,x^{-1}y),\qquad x,y\in S_3.
\]

Can it be replaced by two-body contacts whose single faults never reach two
data blocks, while returning its workspace coherently clean?

## Three-contact construction

Introduce a six-state relative bus `a`, initialized to the identity.  Apply

\[
a\leftarrow x^{-1}a,\qquad
y\leftarrow ay,\qquad
a\leftarrow xa.
\]

Then `a=e` and `y=x^{-1}y`.  The inverse map uses

\[
a\leftarrow xa,\qquad
y\leftarrow ay,\qquad
a\leftarrow x^{-1}a.
\]

Every contact is between one data block and the relative bus.  The checker
verifies both maps on all `6 x 6` basis inputs, for 72 exact cases total.

## Recovery timing theorem

Encode every data block and every bus with distance at least three.  Recover
both blocks incident to a contact immediately after that contact.  Assume the
logical multiplication contacts are one-fault transversal and recovery is
nonpropagating with fresh verified syndrome ancillas.

For a faulty contact, its two incident blocks are recovered before either can
meet another block.  For a fault in a recovery, nonpropagation leaves at most
one erroneous incident block.  The support automaton propagates that output
error through all later contacts and ideal recoveries.  Across six contact
locations and twelve possible recovery-output errors, all 18 abstract
single-fault paths have maximum data-block weight one.  A terminal recovery
fault may leave one correctable output-block error; it cannot create a
two-data-block error.

Thus the earlier weight-two relative-coordinate path is not fundamental.
Under the stated contracts the complete sector compiler has maximum
single-fault data weight one, so data distance three is sufficient.

## Revised resources

Replacing the forward and inverse direct gates adds four primitives per
controlled power:

\[
45-2+6=49,
\]

or 147 gates for the three controlled powers.  There are now 26 bus--data
contacts and 26 recovery layers per controlled power.  A five-rail encoded
six-state relative bus raises the coherent-bus total from ten to fifteen
rails before syndrome ancillas.

## Boundary and falsifiers

This is a conditional fault-tolerance theorem, not a hardware compiler.  It
does not construct transversal logical `S3` multiplication, the three bus
codes' Fourier/transporter gates, or nonpropagating syndrome circuits.

Run:

```text
python research/kitaev/checkers/check_s3_recovered_relative_coordinate_shuttle.py
```

Saved output:
`research/kitaev/results/s3-recovered-relative-coordinate-shuttle.json`.

Falsifiers are failure of either 36-case group action, dirty ideal workspace,
a single contact/recovery fault reaching two data blocks under the stated
recovery contract, or a fault-tolerant logical implementation requiring
higher arity or a larger light cone.  Omitting recovery of either incident
block after a contact invalidates the distance-three conclusion.
