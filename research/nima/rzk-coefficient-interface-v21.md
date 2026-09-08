# v21: conditional conductor-Morse exactness

**Next checkpoint:** [`rzk-coefficient-interface-v22.md`](rzk-coefficient-interface-v22.md)
constructs and checks the additive cone fibre of the physical road
augmentation.

`rzk/32-conditional-conductor-morse-exactness.rzk.md` checks the graded sign
calculation behind the kernel-side proposal.

For arbitrary typed cochain carriers and composition operations, assuming

    delta(k)=e,
    delta(h)=a,
    delta(k h)=delta(k) h - k delta(h),

Rzk proves coefficientwise

    k a - e h = -delta(k h).

The proof includes the integral sign identity and transports both boundary
equalities through the typed compositions. It does not infer that the physical
cochains share a common complex; that requirement remains an explicit
hypothesis.

A fresh 14-file headless closure passed in 1.61 seconds. Evidence:
`results/32-conditional-conductor-morse-exactness.typecheck.json`.

This exhausts the currently specified Rzk work. Further nonconditional progress
requires external construction of the physical-Q comparison, the admissible
mapping fibre, and the physical-to-first-jet map. In particular, the theorem
must not be used to declare physical Delta_J zero until `-k h` is shown to be
an admissible physical primitive.
