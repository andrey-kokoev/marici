# Simplex sections now bind to the verified owning migration

## Binding gap closed for declared simplices

The new `SectionSession` extends the migration-gated checkpoint service with attachment of a simplex section. It does not reuse the unrelated square fixture. Each candidate must bind the live migration digest, exactly the public vertices supplied independently by the owning caller, and one original source witness per vertex.

Attachment checks affine independence, dimension, original atom caps, exact projection of each source witness to its declared public vertex, ALL original fine evidence and the current public frames. Only after these checks succeed is an immutable serialized section retained and a new head handle published. Caller-controlled assertions of global coverage are not accepted fields.

## Coverage promise

The section covers precisely the declared simplex. Affine independence makes barycentric representation unique, so interpolation defines a function of the public point, not merely a relation on supplied weights. Convexity of the source box and original linear evidence proves fine admission throughout that simplex.

Requests supply a public point and its barycentric coordinates. The service verifies nonnegativity, sum one, and exact reconstruction before interpolating. It checks all CURRENT public frames before answering. After restriction the supported domain is the intersection of the original simplex with the new public halfspaces. Old vertices can be excluded without invalidating their local source evidence or the interpolation on retained points.

There is no claim that this simplex covers the entire migrated public domain, no simplex-location algorithm, no multi-simplex coherence verifier and no generic triangulation producer. The protocol explicitly labels coverage as declared-simplex-only.

## Real owning control

The coupled-surviving-audit migration supplies two distinct certified query points and their original source witnesses. Their segment is attached to the same independently verified fine plan, not to a substituted fixture.

The service interpolates the midpoint, appends a public total bound through that midpoint, and returns the same source witness at the surviving midpoint without repeating vertex arithmetic. The larger-total endpoint is then refused despite remaining locally source-admitted. The test directly checks the midpoint witness against the original source caps, fine rows, public projection and new public evidence.

Ten refusals cover foreign migration, invalid source witness, unsupported global-coverage claim, wrong independently expected domain, stale bootstrap handle, wrong/negative barycentric inputs, excluded endpoint, archive request and answer-only attachment. A fresh full section replay uses the same arithmetic kernel outside the checkpoint. A separately implemented section verifier has not been delivered.

## Authority and accounting

The initial migration still undergoes full independent owning verification. Attachment performs two vertex checks for this segment. Subsequent restriction reuses them; fresh point membership and interpolation arithmetic still run. Section encodings are reported separately from migration session state, lift context, archive and point-witness cache. The receipt at advance reports two attachment vertex checks; it is a snapshot taken before the following interpolation request.

Sections never authorize fine re-exposure. The retained lift context still contains fine evidence, so method separation is policy rather than information hiding. There is no cross-process checkpoint import, candidate-authorized cache reuse, hostile-process memory boundary or integration into Nima's checkpoint backend.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_migration_section_checkpoint.py

Implementation: `checkers/migration_section_checkpoint.py`.

Artifact: `results/migration-section-checkpoint.json`.

The remaining full-domain task is to bind a complete triangulation and its coverage/coherence certificate to this SAME expected migration. Local simplex validity is now established, but must not be promoted silently into that stronger claim.
