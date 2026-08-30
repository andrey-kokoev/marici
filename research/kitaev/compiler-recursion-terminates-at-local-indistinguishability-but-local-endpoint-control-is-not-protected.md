# Compiler recursion terminates at local indistinguishability but local endpoint control is not protected

## Bounded question

What physical principle can terminate the regress of clean ancillary
comparators, and can the same localized endpoint region remain both fully
controllable and fault protected?

The regress terminates when the propagated elementary fault algebra compresses
to scalars or correctable syndrome sectors on an encoded logical space. For a
topological code, bounded local support can supply this condition through local
indistinguishability.

But a region that supports a nontrivial logical endpoint algebra cannot also be
correctable against every operator fault on that same region. Full local
control and full local fault correction are algebraically incompatible.

## Accepted-fault compression criterion

Let \(P_{\mathrm{in}}\) and \(P_{\mathrm{out}}\) project onto the input and
output code spaces of an ideal gadget \(U\), with

\[
UP_{\mathrm{in}}
=P_{\mathrm{out}}U.
\]

Insert one elementary fault at location \(\ell\), and propagate it through the
remaining ideal circuit to obtain output operator \(F_\ell\). The accepted
faulty branch is

\[
P_{\mathrm{out}}F_\ell U P_{\mathrm{in}}.
\]

That branch is harmless up to a scalar precisely when

\[
P_{\mathrm{out}}F_\ell U P_{\mathrm{in}}
=c_\ell U P_{\mathrm{in}}.
\]

Equivalently, after pulling the fault back through the ideal logical map,

\[
P_{\mathrm{in}}U^\dagger F_\ell U P_{\mathrm{in}}
=c_\ell P_{\mathrm{in}}.
\]

If the accepted compression is nonzero and non-scalar, the gadget contains an
undetected logical fault. If it is zero, the branch is rejected. If it belongs
to a declared correctable syndrome family, a recovery must occur before output
release.

This is the exact one-fault acceptance gate. A clean ancilla or satisfied code
membership test is evidence only insofar as it establishes this compression.

## Last-actuator obstruction

Suppose the final unverified physical location directly implements a
nontrivial logical generator \(H_L\). An overrotation fault gives

\[
e^{-i\epsilon H_L}.
\]

Because it preserves the code space, a later code-membership or clean-return
test accepts it. Its compression is non-scalar whenever \(H_L\) is a genuine
logical observable.

Therefore no gadget can be one-fault detecting under a fault model that treats
a complete logical overrotation as one elementary fault at its last actuator.
The logical operation must be decomposed into smaller locations whose
individual faults are correctable, detected, or neutral.

This is why declaring the two-rail relative predicate primitive does not close
the compiler theorem.

## Local indistinguishability termination

Let \(P\) project onto a code with the property that every operator \(O_R\)
supported in an admitted correctable region \(R\) obeys

\[
P O_R P=c(O_R)P.
\]

This is local indistinguishability. In a distance-\(d\) code, regions below the
appropriate distance or correctable-size threshold have this property for the
declared operator family.

If every elementary physical fault, after propagation to the next recovery
boundary, remains supported in such a region, then its accepted compression is
scalar. Syndrome extraction may identify and correct the orthogonal component.

The compiler regress stops here. It does not stop because the lowest-level
ancilla is perfect. It stops because the physical noise model is local, the
gadget bounds fault spread, and the code turns every admitted one-fault causal
cone into a correctable operator family.

The three ingredients are all necessary:

- locality bounds the initial fault support;
- the gadget bounds propagation;
- the code makes the resulting support logically indistinguishable.

Removing any one reopens the possibility of a non-scalar accepted fault.

## Control-protection incompatibility theorem

Let \(\mathcal A(R)\) be the full physical operator algebra supported in region
\(R\). Suppose \(R\) is correctable against every fault in \(\mathcal A(R)\).
Then

\[
P O P=c(O)P
\]

for every \(O\in\mathcal A(R)\).

Now suppose the same region supports a nontrivial logical operation
\(L\in\mathcal A(R)\) with

\[
P L P
\]

non-scalar. This contradicts correctability of \(R\).

Therefore:

> A region cannot both realize a nontrivial logical algebra as primitive local
> control and be correctable against the full operator fault algebra on that
> region.

The theorem is immediate from the same compression map. Protection means local
operators look scalar; control means at least one local operator looks
non-scalar.

## Consequence for the 36-dimensional endpoint algebra

The full localized \(D(S_3)\) endpoint algebra has dimension 36 and contains
many non-scalar operations. Algebraic generation by two flux-resolved ports
therefore establishes local controllability of the endpoint block, not
topological protection of an encoded logical qudit against arbitrary endpoint
faults.

If the entire endpoint algebra is admitted as a primitive local fault algebra,
no code supported on the same endpoint block can make that region correctable.
The desired controls and the hostile faults occupy the same algebra.

Fault-tolerant use requires at least one additional structure:

- distribute logical information over separated anyons or code blocks;
- restrict the elementary endpoint fault algebra;
- realize logical gates transversally across an outer code;
- use verified measurement or teleportation gadgets;
- or accept a calibrated analog-control assumption rather than an exact
  one-fault theorem.

This sharpens the programme's central distinction. Full endpoint algebra span
is not merely weaker than physical controllability; even physical local
controllability is weaker than protected logical executability.

## Fusion-space route

Non-Abelian topological computation normally stores logical information in a
fusion space of several separated excitations rather than in the complete
local algebra of one endpoint. Operators confined near one well-separated
anyon cannot resolve the global fusion channel under the ideal topological
code assumptions.

Logical gates are then implemented by braiding, code deformation, joint charge
measurement, or other extended constructors. Their elementary pieces remain
local while the ordered global history acts nontrivially on the fusion space.

This is exactly the architecture required by the termination theorem:

- no one local fault is logical;
- the complete ordered constructor is logical;
- syndrome and separation prevent one fault from acquiring the whole logical
  support.

The present endpoint-algebra results can supply local interaction primitives
inside such an architecture, but they do not by themselves define the protected
encoding.

## Mobile-bus diagnosis

The naked holonomy bus violates the bounded-propagation ingredient. One
ancilla phase fault can spread through inverse contacts to a four-edge
operator. The naked relative comparator violates it again by contacting both
protected shares.

Encoding the bus helps only if each elementary contact and each predicate
location preserves the correctable-support bound. A mobile unverified degree
of freedom that sequentially visits the entire logical support defeats local
indistinguishability by enlarging one fault's causal cone.

The relevant resource is therefore not gate count alone but maximum propagated
fault support before recovery.

## Fault-filtered functor criterion

For each ideal generator \(g\), a physical compiler assigns a gadget
\(\Gamma(g)\). For each elementary fault \(f\) in that gadget, define its
accepted logical compression

\[
\kappa_g(f)
=P\Gamma(g)^\dagger F_f\Gamma(g)P.
\]

A one-fault filtered compiler requires every \(\kappa_g(f)\) to be:

- scalar;
- rejected;
- or accompanied by a retained syndrome selecting a proved recovery.

Composition additionally requires recovery boundaries to keep one fault from
spreading across consecutive gadgets. Algebraic generator relations alone do
not imply this functorial fault condition.

## Where the regress honestly terminates

The termination chain is:

1. microscopic elementary faults have bounded support;
2. each primitive interaction has bounded fanout;
3. recovery occurs before one fault meets another data block or share;
4. the propagated error family satisfies the code's correction conditions;
5. accepted compression is scalar on the logical space.

The chain bottoms out in an empirical physical noise and locality model plus an
exact code theorem. It cannot bottom out in another unverified abstract
constructor.

This does not eliminate calibration assumptions. It states exactly which
assumptions are physical and which consequences follow algebraically.

## Exact falsifiers

- A clean-return condition used without evaluating accepted logical
  compression.
- A primitive nontrivial logical actuator claimed protected against arbitrary
  overrotation at the same location.
- A region claimed correctable against all local operators while also
  supporting a non-scalar local logical operator.
- Endpoint algebra span identified with protected logical executability.
- A mobile bus called local because each individual contact is two-body while
  one persistent fault reaches the full support.
- Code distance cited without a bound on propagated fault support.
- A fusion-space protection claim with no separation or local
  indistinguishability theorem.
- Recovery placed after the erroneous carrier has interacted with another
  logical block.
- Another abstract comparator offered as the bottom physical primitive without
  a fault algebra.

## Machine-readable termination certificate

```json
{
  "code": "compiler_recursion_local_indistinguishability_termination",
  "accepted_fault_gate": "P_out*F_l*U*P_in = c_l*U*P_in or reject/recover",
  "local_indistinguishability": "P*O_R*P = c(O_R)*P",
  "bounded_initial_fault_support_required": true,
  "bounded_propagation_required": true,
  "recovery_before_recontact_required": true,
  "primitive_logical_overrotation_detectable_by_membership": false,
  "full_local_control_and_full_local_fault_correction_compatible": false,
  "endpoint_algebra_dimension": 36,
  "endpoint_span_implies_protected_executability": false,
  "distributed_fusion_encoding_candidate": true,
  "physical_noise_model_required": true
}
```

## Deutschian explanation

An infinite tower of verifiers appears only when every verifier is allowed to
fail in a way that already has logical reach. A code ends the tower by making
the reach of one elementary fault too small to distinguish logical states.

That same fact explains why full local control is dangerous. If a local region
can perform every logical transformation, then an uncontrolled local
perturbation can also point in a logical direction. Protection comes from
making logical action a property of an extended, ordered construction while
keeping every individual physical event logically incomplete.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier statement is a support-versus-kernel theorem: a constructor
is protected when every admitted elementary causal cone lies in the kernel of
the logical distinction map, up to recoverable syndrome.

The quantum coefficient lens supplies code compression, coherent logical
operators, syndrome subspaces, and fusion-space encodings. It turns the
geometric support bound into the scalar local-indistinguishability equation.

## Claim boundary

This packet proves the accepted-compression gate and the incompatibility
between full operator correction and nontrivial logical control on one region.
It gives a conditional termination theorem from locality, bounded propagation,
and code correction. It does not construct the required distributed
\(D(S_3)\) fusion encoding, synthesize its gates, or establish a microscopic
noise model for the existing apparatus.

## Process calibration

Excitement is 10/10 and confidence in the structural theorem is 10/10. The
compiler regress now has an honest bottom, and the programme's next object is
clearer: not a fault-tolerant version of the full local endpoint algebra, but a
distributed protected logical encoding whose extended constructors use only
fault-filtered local endpoint primitives.
