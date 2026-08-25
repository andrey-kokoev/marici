# Compact-source uniform-faithfulness audit (WP138)

Owner: `marici.Figueiredo`.

## Bounded question

Can compact cosmological support remove WP137's inaccessible Gaussian tail and
make a finite-reach multi-point instrument uniformly faithful over the entire
source domain?

Pre-objective process report: excitement `8/10`, confidence `9/10` that
compactness gives a conditional repair but does not select its physical
support scale, expected information gain `8/10`. Confounds are the ideal flat
compact law, reheating matching, and finite four-constructor family. These
reports are non-evidential.

Frozen optionality snapshot: one compact coordinate; one normalized uniform
law; one scale pushforward; two source support scales fixed before rank
calculation; one exact uniform-faithfulness condition; twelve checks.

## Compact source and pushforward

Let `u` be a weak-basis-singlet compact coordinate, for example a normalized
axion angle, with source law

\[
u\sim\operatorname{Uniform}[-1,1].
\]

The law is normalized without relying on a confining quadratic tail and has

\[
\langle u\rangle=0,\qquad
\langle u^2\rangle=\frac13,
\qquad \langle u^4\rangle=\frac15.
\]

After a sign-preserving reheating map, write the crossover scale as

\[
\Lambda(u)=\Lambda_{\max}\sqrt{|u|}.
\]

For detector reach `E_max`, the exact accessible probability is

\[
P_{\rm acc}=
\min\!\left(1,\frac{E_{\max}^2}{\Lambda_{\max}^2}\right).
\]

Unlike the Gaussian source, a finite detector can cover the entire compact
support. Uniform accessibility holds exactly when

\[
\boxed{\Lambda_{\max}\le E_{\max}.}
\]

## Hostile support-scale pair

Set `E_max=1`. The independently frozen packet `Lambda_max=4/5` has
`P_acc=1`; the formal WP133 multi-point probe would be rank four on every draw
of its four-constructor domain. A second admissible packet with
`Lambda_max=4/3` has

\[
P_{\rm acc}=\frac9{16},
\qquad P_{\rm inaccessible}=\frac7{16}.
\]

Both use the same compact geometry and normalized law. They differ only in
the physical support scale, controlled by the decay constant, matching
coefficient, and clock relation. Compactness therefore removes the necessary
tail obstruction but does not select which side of the detector inequality
nature occupies.

The mass readout also retains the `u` versus `-u` kernel. A sign-sensitive
multi-point coupling can refine it, provided that coupling belongs to the
frozen source grammar and has an executable instrument.

## Disposition

WP138 establishes a necessary and sufficient support condition for uniform
finite-reach identification on the declared compact domain. This is a real
capability improvement over WP137: finite reach can cover the full source
support. It remains a **conditional instrument repair**, not a source-derived
numerical prediction, because `Lambda_max/E_max` is not selected.

Choosing the compactification/decay scale after inspecting detector reach is
target-fitted boundary selection. The remaining lawful gate is an independent
relation fixing the compact source scale to a physical clock, followed by the
actual multi-point detector construction and open-rival audit.

The smallest falsifier of unconditional repair is the exact pair
`Lambda_max=4/5,4/3`: identical compact source type, but uniform versus
`9/16` accessibility. No reference port recovers an absolute scale; the
detector comparison defines a new relational experiment.

Post-objective process report: excitement `8/10`, confidence `10/10`, realized
information gain `9/10`. Raw delta: an unavoidable Gaussian tail is removed;
one exact uniform-faithfulness inequality is constructed; one fully accessible
and one partially accessible source packet are separated; twelve of twelve
checks pass; no support-scale selector or physical instrument is added. These
reports are non-evidential.
