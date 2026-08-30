# Temporal composition and Cut sewing require retained memory

Let the observed and internal occurrences be two binary systems, with the internal one initialized in (|0\rangle).  Use CNOT as the interaction.  For the observed input (|+\rangle\langle+|):

- one global interaction followed by internal pushforward is dephasing;
- two global interactions with the same retained internal occurrence give (U^2=I), hence the identity channel;
- pushing forward after the first step, resetting the lost internal state, and composing the reduced channel gives dephasing again.

Therefore

\[
\operatorname{Tr}_E\!left[U^2(\rho\otimes|0\rangle\langle0|)U^{\dagger2}\right]
\ne
\Phi_U\bigl(\Phi_U(\rho)\bigr).
\]

The discrepancy is not a failure of global composition or Cut sewing.  It is caused by applying the internal-state pushforward before temporal sewing.  If the labelled internal occurrence is retained, both routes are the same global composition.  If it is forgotten between steps, its memory cannot be reconstructed from the reduced channel.

Thus the required coherence is a process-tensor/memory object, not a new carrier cell.  A Beck--Chevalley comparison may exist between composition and Cut only on the retained labelled object; ordinary reduced-channel composition is the wrong target on correlated or repeatedly interacting support.
