# The RH marked germ is the target-relative joint-incidence quotient

## Start with the target family

The carrier cannot be chosen before the transformations it must support are
declared. For the present RH boundary programme, let \(\mathcal T_{\mathrm{RH}}\)
contain only the source-facing operations currently required to keep the
relative determinant construction meaningful:

1. full tail–seam synthesis \(U\);
2. primitive atomic incidence \(I_1\);
3. square atomic incidence \(I_2\);
4. the archimedean boundary incidence \(I_\infty\);
5. the zero-frequency boundary incidence \(I_0\);
6. every reciprocal dagger transport needed to compare those outputs;
7. the authorized cutoff bonding maps.
8. after a candidate global section is adjoined, the Euler–theta overlap
   residual on the source chamber.

This list is provisional in exactly one legitimate sense: adding a genuinely
new target operation may refine the germ. No unneeded arithmetic distinction
is retained merely because it exists in the source presentation.

## Full-fiber equivalence

On the finite valuation/Fock source module \(V\), define

\[
v\sim_{\mathcal T}w
\]

exactly when every operation in \(\mathcal T_{\mathrm{RH}}\) gives the same
result on \(v\) and \(w\), including all required transported presentations.
The marked carrier germ is

\[
G_{\mathcal T}=V/{\sim_{\mathcal T}}.
\]

For the currently linear source-facing family, this is a common-kernel
quotient only after the family has been closed under every admitted source
constructor. If \(\mathcal M_{\mathrm{src}}\) is the authorized constructor
monoid, the correct kernel is

\[
G_{\mathcal T}
=
V/K_{\mathcal T,\mathcal M},
\qquad
K_{\mathcal T,\mathcal M}
=
\bigcap_{F\in\mathcal T_{\mathrm{RH}}}
\bigcap_{C\in\mathcal M_{\mathrm{src}}}
\ker(F\circ C).
\]

The full-fiber definition is primary. The common-kernel formula is valid only
because these declared operations are linear at this stage.

This constructor closure makes the fiber relation a congruence. A direction
cannot be discarded merely because current readouts miss it when an admitted
transport can move it into a visible port after algebraic composition.

## Joint-incidence realization

The germ embeds faithfully into the product of its required output ports by
the joint map

\[
J[v]=
\bigl(
Uv,
I_1v,
I_2v,
I_\infty v,
I_0v,
\ldots
\bigr).
\]

The ellipsis contains only declared reciprocal transports and cutoff data.
The image of the constructor-closed joint signature \(J\), not the unproved
full valuation/Fock module and not the analytic state alone, is the minimal
marked germ for this target family.

This corrects the earlier over-retention. The full arithmetic synthesis graph
is a safe presentation before quotienting, but it is minimal only if its
constructor-closed common target kernel is zero. Finite valuation cylinders
are known to separate finite arithmetic packets, so zero kernel is plausible
there; it must be derived rather than assumed, and completion requires a new
separation test.

## Native-arity gate

The relative determinant totalization is defined on the joint image of the
primitive, square, tail, archimedean, and zero-frequency ports. It must be
tested at that native arity. Separate scalarization of any subset is legal
only if the totalization is constant on every full fiber of the proposed local
completion.

Because the completed determinant constructor is nonlinear, kernel
annihilation alone is not the general test. Kernel tests remain exact for its
finite logarithmic linearization and other explicitly multilinear pieces.
The completed constructor requires the full-fiber test.

## Parameterized mate and associator

At cutoff \(X\), let \(G_X\) be the target-relative germ. The operative mate is
a cutoff-natural sewing operation on the compatible joint-incidence packet.
It must compare all admissible bracketing orders without consuming an open
port prematurely.

The associator residual is the difference between two fully typed sewing
paths, not merely their final scalar values. A zero residual is a theorem to
derive from source composition. It cannot be declared from equality of
completed numbers.

This is the operative extra port: the comparison morphism between retained
factorizations. A static quotient object is only its boundary shadow.

## Authority gate

Even when the relative totalization descends to \(G_{\mathcal T}\), descent
does not select a canonical trivialization of the relative determinant line.
That selection requires a source-authorized Tate and archimedean sewing law.
No symmetry of the quotient, fitted finite part, or matching scalar output can
replace it.

## Completion

The pro-Gram topology must also be target-relative. Its seminorm family is
generated only by constructors in \(\mathcal T_{\mathrm{RH}}\), and the common
null space is quotiented before completion. The completed germ is therefore
the completion of \(G_{\mathcal T}\), not of the entire arithmetic module.

The realization must then prove:

1. continuity of every declared target map;
2. naturality under cutoff bonding;
3. native-arity descent of the joint relative totalization;
4. reciprocal dagger compatibility;
5. source authority for the chosen determinant-line trivialization.

## Falsifiers

The reconstruction has four immediate hostile tests:

1. a discarded direction changes one declared target operation;
2. a retained direction lies in every full target fiber;
3. all linear kernel tests pass while a nonlinear full fiber changes the
   totalization;
4. totalization descends but two symmetry-related source sections remain and
   no source law selects one.

## DPC verdict

The faithful categorical RH object is the target-relative marked germ
\(G_{\mathcal T}\), realized through its joint incidence ports. The arithmetic
module is a presentation, the analytic tail–seam state is one projection, the
relative determinant is a native higher-arity mate, and its canonical
trivialization remains a separate authority problem.

## Verification

`check_rh_target_relative_marked_germ.py` verifies exact full-fiber quotienting,
safe removal of a target-invisible direction, rejection of analytic-only
completion, a nonlinear fiber failure invisible to a differential-kernel
test, and descent without canonical source selection.
