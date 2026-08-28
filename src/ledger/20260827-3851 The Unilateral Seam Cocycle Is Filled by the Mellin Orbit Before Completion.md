# The Unilateral Seam Cocycle Is Filled by the Mellin Orbit Before Completion

For real `f`, let

\[
A(w)=\int_0^\infty f(q)e^{wq}\,dq.
\]

The unilateral seam cocycle is

\[
C_f(z)=A(-\overline z)-A(\overline z).
\]

It is not a new algebraic interface class. The source-derived Mellin orbit
`t -> A(tw)` from `w` to `-w` gives the exact filling

\[
C_f(z)
=-w\int_{-1}^{1}A'(tw)\,dt
=-2\int_0^\infty f(q)\sinh(wq)\,dq,
\qquad
w=\overline z.
\]

Thus the residual is fillable on the ordinary test-function domain. The only
remaining obstruction is whether this canonical filling survives the
completed boundary category. That requires continuity of the dilation
generator `Qf=qf`, the full reciprocal orbit, endpoint evaluation, and the
primitive and prime-square boundary channels under cutoff completion.

The next falsifier is a boundary-null source sequence whose Mellin-orbit
filling converges to a nonzero boundary packet. Such a witness would be a
genuine asymptotic completion class rather than an algebraic seam cocycle.

Research packet:
`research/grothendieck/the-unilateral-seam-cocycle-is-filled-by-the-mellin-orbit-before-completion.md`.

Allocator claim: `seqclaim-59d6d342bbf56dcf65660365`.

Epistemic graph event: `8356`.
