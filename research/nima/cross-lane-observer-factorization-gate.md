# Cross-Lane Observer Factorization Gate

## Question

Several current lanes have an algebraic readout that separates states. Which
additional structure is required before that readout may be treated as an
executable, completion-stable observer?

## Typed factorization

Let \(S_0\) be the source state carrier, \(S\) its admitted completion, \(A\)
an algebraic feature carrier, and \(R\) a record carrier.

An algebraic readout is a map

\[
J_0:S_0\to A.
\]

An executable observer requires a source-authorized instrument

\[
I_0:S_0\to R
\]

and a declared decoder

\[
d:R\to A
\]

such that

\[
J_0=dI_0.
\]

A completion-stable observer additionally requires extensions

\[
I:S\to R,\qquad J:S\to A
\]

with \(J=dI\), and injectivity or the required quotient-faithfulness on the
admitted completed state class.

These are three different claims:

1. algebraic separation by \(J_0\);
2. executable acquisition through \(I_0\);
3. stable separation after completion.

None implies the next without a source-authorized constructor and a continuity
or closed-range theorem.

## Finite falsifiers

### Acquisition-authority hostile

The formulas defining \(J_0\) exist, but no source operation produces a record
in \(R\). This is not a kernel failure. The arrow \(I_0\) is absent.

### Kernel hostile

There are \(x_0,x_1\in S_0\) with

\[
I_0x_0=I_0x_1,\qquad J_0x_0\ne J_0x_1.
\]

Then the proposed decoder cannot exist.

### Completion hostile

There is a normalized sequence \(x_n\in S_0\) for which

\[
I_0x_n\to0
\]

while the admitted source topology does not send \(x_n\) to zero. Finite
faithfulness then fails to extend uniformly.

### Cocone hostile

For transitions \(F_n:S_n\to S_{n+1}\), a stagewise probe \(p_n\) is not a
probe of the completed object when

\[
p_{n+1}F_n-p_n\ne0.
\]

## Current lane classification

### Flavor

The affine interior action and balanced fourth-order exponent are algebraic
candidates. No single microscopic constructor supplies occurrence, polarity,
normalization, descent, and the required interior. The failure is acquisition
authority before conditioning.

The balance \(s=4\) removes the common coupling fiber but leaves the normalized
prefactor unconstrained. This is nuisance-parameter cancellation, not a
numerical selector.

### Strominger

The 21 magnetic low-harmonic coefficient ports are executable finite
integrals. The hostile pair

\[
x_0=(0,0),\qquad x_1=(1,1)
\]

is collapsed by every admitted magnetic acquisition while the algebraic joint
observer separates it through the electric component.

The electric dimension

\[
d_E(L)=(L+1)^2-4
\]

is unbounded. Another fixed 21-port packet cannot complete the observer. The
remaining object must be field-valued or an unbounded separating electric
family, together with a same-prepared-packet electric/magnetic coherence
binding.

That coherence binding is the pullback

\[
R_E\times_P R_M
\]

over preparation identity \(P\), not the unrestricted product \(R_E\times
R_M\). For source packets with records \((0,0)\) and \((1,1)\), the
unrestricted product fabricates \((0,1)\) and \((1,0)\); the pullback recovers
exactly the two source records. Preparation identity is incidence typing, not
time.

The pullback certifies provenance only. It does not construct a jointly
executable instrument. If preparation is linear or consumable, each marginal
may be authorized while either acquisition destroys the capability required
for the other. Closure then requires a primitive joint refinement

\[
j:P\to R_E\times_P R_M
\]

or independent authority for nondestructive reuse or copying.

### Grothendieck

The positive seam-matched split repairs the first odd seam jet while retaining
pointwise positivity. The third odd jet immediately reopens:

\[
R'''(0)\ne0.
\]

This is a completion hostile. Every finite jet packet controls only a bounded
frequency regime unless a source theorem closes the entire odd germ.

### Kitaev and Aspect

The ideal toric logical Pauli tower closes algebraically at nilpotency class
two. Balanced-word optics supplies an executable finite commutator observer,
and the tetrahedral four-probe frame optimizes its local conditioning.

This tetrahedral frame cannot create missing flavor, electric, or theta
instruments. It transfers only after a lane constructs a finite
source-authorized record carrier.

Kitaev's three-stage witness supplies the compatibility audit for a repair
tower: immediate death, delayed death, birth, surviving blind classes, and the
cocone residual must be tracked separately.

## Cross-lane lifts

### Directed-system audit

Apply the three-stage kernel, cokernel, and cocone table to the seam-jet tower
and to any flavor sequence of effective constructors. This can show whether a
new channel survives transport or merely repairs one cutoff.

### Balance versus reserve

Flavor's fourth-order result and Grothendieck's seam repair have the same
logical shape. A balance condition removes one nuisance dependence while
moving unresolved content into a source-fixed coefficient or reserve. Neither
balance supplies orientation or a lower bound.

### Frame optimization after authority

Aspect's tetrahedral frame is a post-authority compiler. Once a lane has a
finite tangent record space, it minimizes worst-direction noise. Before the
instrument arrow exists, applying it is a category error.

### Source-fixed flags

Strominger's invariant flag shows how a source algebra can explain rank defects
and gauge invariance without supplying execution. Flavor should search for an
analogous microscopic invariant flag only inside one admitted constructor.

### Record pullbacks

Whenever two observers must refer to one source occurrence, compose their
record carriers by pullback over the occurrence or preparation object.
Ordinary products erase provenance and admit synthetic cross-occurrence
records. This lift applies directly to flavor probes calibrated at different
stages or ensembles: they may be joined only through an explicit common-source
incidence object. After provenance is established, a second gate must prove a
joint instrument or nondestructive reuse authority.

## Decisive next test

For every lane, write the proposed square

\[
\begin{array}{ccc}
S_0 & \xrightarrow{I_0} & R\\
\downarrow & & \downarrow d\\
S & \xrightarrow{J} & A
\end{array}
\]

and ask, in order:

1. Is every arrow source-authorized?
2. Does the square commute on labelled generators?
3. Is the acquisition kernel contained in the algebraic kernel?
4. Do the maps form a cocone across cutoffs?
5. Does the completed observer retain the required separation?

The first failed row is the lane frontier.

## Rough edges exposed

On the research side, the word “observable” has been covering algebraic
separation, executable acquisition, and completion stability.

On the communication side, the default short display hides evidence and
epistemic status. Those fields remain in the immutable response and are
available through medium, all-limited, all-unlimited, or an explicit field
list. A short projection must never be treated as the complete packet.

## Sources

- research/flavor/flavor-affine-interior-source-constructor-census.md
- research/flavor/flavor-balanced-fourth-order-coupling-gate.md
- research/grothendieck/a-positive-seam-matched-primitive-split.md
- research/grothendieck/the-third-seam-jet-reopens-after-first-jet-repair.md
- research/kitaev/three-stage-logical-stabilization-witness.md
- research/kitaev/toric-ordered-tower-closes-central-commutator.md
- research/strominger/parity-port-executability-boundary.md
