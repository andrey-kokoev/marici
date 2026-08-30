# Spin(7) Orbifold Projection Realizes A but Does Not Select Its Parities

Work package: WP922

## Question

Can a five-dimensional orbifold or domain-wall projection remove WP921's
forced neutral surplus while retaining exactly the Completion-A charged
packet?

## Fixed involution and matter parities

Use the involution that breaks

\[
\mathrm{Spin}(7)\longrightarrow
\mathrm{Spin}(5)\times\mathrm{Spin}(2).
\]

Assign involution grade (+1) to the first component in

\[
8=4_{+1/2}\oplus4_{-1/2}
\]

and grade (-1) to the second. In the adjoint,

\[
21=(10_0\oplus1_0)_{+}\oplus(5_{+1}\oplus5_{-1})_{-}.
\]

For a bulk matter field with intrinsic parity (eta=\pm1), retain a
four-dimensional zero mode precisely when (eta) times its involution grade
is (+1). These are matter parities; the gauge field uses the usual even
unbroken-algebra assignment and is not being projected by the matter rule.

## Exact constructor

One matter (21) with (eta_{21}=-1) retains

\[
5_{+1}\oplus5_{-1}
\]

and removes exactly (10_0\oplus1_0). A single parent (8) retains only one
of its two charged spinors. Therefore use two bulk spinors (8_a,8_b) with
opposite intrinsic parities. Their combined zero modes are

\[
4_{+1/2}\oplus4_{-1/2}.
\]

Together the zero-mode packet is exactly the shared portal plus Completion A,
with no neutral surplus.

## Finite parity fiber

The three independent intrinsic parities give (2^3=8) assignments. Exact
enumeration finds two ordered assignments producing the target:

\[
(eta_{8a},\eta_{8b},\eta_{21})=(-1,+1,-1),
\]

\[
(+1,-1,-1).
\]

The two differ only by exchanging the labelled parent spinors. The other six
assignments produce different zero-mode spectra. Thus the projection is an
exact conditional constructor but the desired parity orbit is not selected by
the declared five-dimensional source.

The smallest hostile flips only (eta_{21}) to (+1). Then (10_0\oplus1_0)
returns and (5_{+1}\oplus5_{-1}) disappears. Geometry of the breaking
involution alone therefore does not determine the matter intrinsic parity.

## Classification

Conditional on the parity choice, the operation rigidifies the exact
four-dimensional field presentation. It is not yet a source-derived
completion selector and it does not select physical16. It explicitly defines
a new five-dimensional source experiment/category; it does not reveal that A
was already selected by the four-dimensional Spin(5) theory.

The next gate is twofold:

1. derive the intrinsic parities from boundary topology, locality, or an
   endpoint-resolved index independently of the target spectrum;
2. enumerate the parity-even bulk and boundary interactions and determine
   whether the same construction constrains the complete three-family Yukawa
   tensors.

No detector instrument is missing at this stage.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp922_spin7_orbifold_zero_mode_projection_fiber.py
~~~
