# Direct-image reducers must preserve the total differential

## Result

Let the typed source-support descent data form a finite total complex

\[
C^0 \xrightarrow{D_0} C^1 \xrightarrow{D_1} C^2,
\qquad D_1D_0=0,
\]

where degree (0) contains local objects (A), degree (1) contains
pairwise comparison cells (H), and degree (2) contains triple cells
(K).  A proposed direct-image reducer

\[
R=(R_0,R_1,R_2):C^\bullet\longrightarrow \bar C^\bullet
\]

preserves coherent descent only if it is a chain map:

\[
\boxed{\bar D_iR_i=R_{i+1}D_i\quad(i=0,1).}
\]

This is stronger than preserving the scalar output, the local (A) data,
or every pairwise comparison separately.

## Finite falsifier

The smallest relevant obstruction lives on one degree-1 generator.  Over
\(\mathbf F_2\), take

\[
C^1=\langle h\rangle,qquad C^2=\langle k\rangle,qquad D_1h=k.
\]

Let the proposed reducer retain the visible pairwise cell but erase its
triple target:

\[
R_1h=\bar h,qquad R_2k=0,
\qquad \bar D_1\bar h=\bar k.
\]

Then

\[
(\bar D_1R_1-R_2D_1)h=\bar k\ne0.
\]

Thus the reducer can report that the pairwise diamond survived while
destroying the cell that makes it coherent.  The nonzero commutator is a
complete one-vector rejection witness.

## Compiler gate

A reducer certificate must carry:

- its typed maps (R_i);
- the source and target differentials;
- a verified zero matrix for every commutator
  (\bar D_iR_i-R_{i+1}D_i);
- a source-authorized comparison cell if preservation is only up to
  homotopy.

The first nonzero matrix entry is machine-readable:

```json
{
  "code": "direct_image_not_chain_map",
  "degree": 1,
  "source_basis": "h",
  "residual_basis": "k_bar",
  "residual": 1
}
```

## Consequences

- Benincasa's source-wall reducer must act on the entire typed
  ((A,H,K)) tower and pass this commutator gate.
- Strominger's constructor compiler must test coherence preservation at
  every reduction or optimization pass, not merely at the final root.
- Schedule equivalence and scalar functional agreement are insufficient:
  they can lie in the kernel of the observable while the commutator is
  nonzero.
- A chain map transports coherence but does not create authority.  The
  reducer and any homotopy comparison still require their own source
  authority.

## Boundary

This theorem gives a finite falsifier for invalid reductions.  It does
not prove that a chain-map reducer exists, nor that a valid reducer
preserves positivity, fault tolerance, or analytic orientation.

