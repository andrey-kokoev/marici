# Photon Connected-Transport Determinant

The source-defined fixed-kinematics outgoing photon state has coefficient
matrix

\[
M=
\begin{pmatrix}
\Phi_1&\Phi_5\\
\Phi_5&\Phi_2
\end{pmatrix}.
\]

Before conjugate doubling or probability normalization, its connected
transport residue is

\[
\boxed{
\bigwedge^2M=\det M=\Phi_1\Phi_2-\Phi_5^2.
}
\]

For real coefficients, let \(N=\operatorname{Tr}(MM^T)\).  The normalized
reduced density matrix is

\[
\rho_A=\frac{MM^T}{N},
\]

and exact algebra gives

\[
\boxed{
\det\rho_A=
\frac{(\Phi_1\Phi_2-\Phi_5^2)^2}{N^2}.
}
\]

Therefore the following are equivalent for this pure two-photon packet:

\[
\bigwedge^2M\ne0
\iff
\operatorname{rank}M=2
\iff
\det\rho_A>0
\iff
\text{the helicity state is not a product state}.
\]

For a pure bipartite state, this is also exactly the support condition for
positive mutual information between the two outgoing helicities.  Appending an
independent spectator vector tensors \(M\) with a rank-one factor and leaves
its rank unchanged.

## Architectural consequence

This supplies the first mature-sector ladder

\[
\boxed{
\text{coefficient transport }M
\xrightarrow{\ \wedge^2\ }
\text{connected algebraic residue}
\xrightarrow{\ M\mapsto M\otimes\bar M\ }
\text{positive density support}
\xrightarrow{\text{effects}}
\text{mutual-information/Bell readout}.
}
\]

The connected precursor is earlier than probability, but it is not supported
by the unweighted Carrier alone.  It requires the Carrier port together with
the physical helicity coefficient adapter.  This is precisely the
ports-and-adapters pattern found independently in the orientation audit.

The result does not establish that dynamics maximizes connected capacity.  It
does establish that a source-defined pre-positive object exists and that its
positive readout detects the same connected-versus-product distinction without
fitting.

Certificate:
`research/nima/checkers/check_photon_connected_transport_determinant.py`
