# The de Rham Concomitant Does Not Select the Five-Channel Metric

## Question

Does compatibility with the exact Pearson/de Rham and Mellin/Gysin pair select a unique member of the seven-parameter family of degree-invariant five-channel forms?

No. On the free five-component germ module, that compatibility is universal for every constant symmetric form. The hoped-for selection mechanism therefore does not exist at this level.

## Universal identities

Let (X(y)) and (Y(y)) be five-component source germs and let (Q) be any constant symmetric matrix. Define

\[
\langle X,Y\rangle_Q=X^TQY.
\]

The relative de Rham operator obeys

\[
\partial_y\langle X,Y\rangle_Q
=\langle\partial_yX,Y\rangle_Q+\langle X,\partial_yY\rangle_Q.
\]

After integration, its entire defect is the declared endpoint term

\[
\int_0^L
\left(\langle\partial_yX,Y\rangle_Q+\langle X,\partial_yY\rangle_Q\right)dy
=\left[X^TQY\right]_0^L.
\]

The Gysin map is multiplication by the wall coordinate and is automatically symmetric:

\[
\langle yX,Y\rangle_Q=\langle X,yY\rangle_Q.
\]

None of these statements uses the entries of (Q). Imposing them on the seven-parameter family already preserved by every adjacent degree comparison removes zero parameters.

## What this falsifies

The de Rham/Gysin square cannot by itself select a physical Clifford form. Integration by parts transports whichever constant form was supplied; it does not choose one.

The finite-jet terminal projector cannot help. It is the cutoff defect in the Weyl relation, whereas the physical wall is the endpoint concomitant. Treating the projector as an extra boundary current would manufacture a selector from the approximation scheme.

## Remaining source gate

Only the original tail and wall components presently have explicit source germs. The determinant-dual channels still lack independently derived germ sections or adjoint boundary conditions. A genuine selector must therefore enter through additional source data, such as a relative-cohomology realization of the dual channels, endpoint incidence, analytic-strip reality, or a nontrivial pushforward acting differently on the channels.

Until then, the seven parameters are gauge freedom in the comparison presentation, not seven candidate physical metrics.

## Verification

The checker `research/grothendieck/checkers/derham_concomitant_metric_universality.py` verifies the Leibniz concomitant, Green boundary identity, and Gysin symmetry for a general symmetric (5\times5) matrix and polynomial germs.
