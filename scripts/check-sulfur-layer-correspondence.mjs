import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {traceSeedConductors} from '../research/realization-tower/seed-retained-conductors.mjs';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {checkRouteBundleCapacity} from '../research/realization-tower/route-bundle-invariants.mjs';
const seed=buildBranchingSeed(),native=buildSulfurIncomingBundle(),source=traceSeedConductors(seed.layers[0]),alternative=traceSeedConductors(seed.layers[0],{interiorRouting:'cross-colour'});
const sourceEdges=s=>s.memberships.map(e=>({id:e.edge,strands:e.strands}));
const check=checkRouteBundleCapacity(sourceEdges(source),native.edges.map(e=>({id:e.id,strands:e.strandIds})));
assert.deepEqual(source.counts,{bottomSleeves:8,conductors:16,rooted:16,coveredEdges:108,totalEdges:108});
assert.deepEqual(alternative.counts,source.counts);
assert(source.strands.some(s=>s.word!==alternative.strands.find(t=>t.id===s.id).word));
for(const strand of source.strands)assert(seed.layers[0].routes.some(r=>JSON.stringify(r.edges)===JSON.stringify(strand.edgeIds)));
const reflected=seed.layers.map(layer=>{
 const trace=traceSeedConductors(layer);
 for(const s of trace.strands)assert.deepEqual(s.canonicalEdges,source.strands.find(t=>t.id===s.id).canonicalEdges);
 return {layer:layer.id,counts:trace.counts,ancestryPreserved:true};
});
assert.equal(check.source.bySize[4],2);assert.equal(check.target.bySize[4],10);assert.equal(check.necessaryConditionsSatisfied,false);
const paths=['research/realization-tower/seed-retained-conductors.mjs','research/realization-tower/route-bundle-invariants.mjs','research/realization-tower/branching-seed.mjs','research/realization-tower/sulfur-32-incoming-bundle.mjs'];
const hashes=Object.fromEntries(await Promise.all(paths.map(async p=>[p,createHash('sha256').update(await readFile(p)).digest('hex')])));
const receipt={schema:'sulfur-layer-correspondence.v1',verificationPassed:true,correspondenceEstablished:false,
 status:'blocked for a fixed reflection-transported identity map preserving shared segments',sourceHashes:hashes,source,reflected,
 alternative:{counts:alternative.counts,strands:alternative.strands.map(s=>({id:s.id,word:s.word}))},
 targetScope:native.audit.routingStatus,targetIdentities:native.strands.map(s=>({id:s.id,polarities:s.polarities,edges:s.edgeIds})),bundleCheck:check};
const out='research/strominger/results/sulfur-layer-correspondence-v1';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(receipt,null,2)+'\n');
const rows=source.strands.map(s=>`| ${s.pairIndex+1} | ${s.colour} | ${s.word} | ${s.events.length} |`).join('\n');
const report=`# Layer conductors versus the existing Su-32 identities

## Status

**A route-preserving correspondence has not been established.** No native
(a,b,p,e) labels have been assigned to the layer conductors and no viewer paths
have been replaced. The test below finds a concrete obstruction to a fixed
identity relabelling; it does not declare the native reference physically wrong.

## Sixteen real layer routes, not sixteen display lines

Start at the two coloured output ports of every bottom white sleeve. Trace
backward through actual layer edges:

1. Cross the incoming white segment without changing the retained conductor ID.
2. At an interior two-port junction, select the incoming edge with the same
   current port colour.
3. At a boundary with only one incoming edge, follow that existing trunk,
   retaining the conductor ID but updating the edge-role used for further tracing.
4. Stop at the actual layer root. Never introduce a connector or an external
   source where the requested colour is absent.

This is an explicit candidate sleeve-continuation rule. In particular, conductor
identity is not equated with the colour of a shared trunk edge.

The result is **16 distinct complete routes**, two for each of the **8 bottom
sleeves**. All 16 reach the root; together they cover **all 108 layer edges**.
Every route is an existing member of the original directed layer path family.
There is no 16-item truncation or target-count selection in the tracer.

| Bottom sleeve | Retained terminal conductor | Actual branch word | Boundary trunk transitions |
|---|---|---|---|
${rows}

These are precisely the red/blue words with at most one colour-role change.
The two constant-colour routes require no boundary turn. The other fourteen
continue into their sole boundary trunk rather than terminating there.
Canonical lattice ancestry transports these same sixteen template IDs through
all eight reflected layers. This establishes correspondence between layer copies,
not correspondence with the native Su-32 identities.

## Conservation does not uniquely determine the paths

As a countercheck, exchange the two incoming port assignments at every interior
sleeve while keeping the sole-boundary-trunk rule. This also gives sixteen rooted
routes and covers all 108 edges, but changes the actual route words. Thus neither
'16' nor full coverage proves that a continuation rule is the intended wiring.
Both candidates retain exactly two distinct four-conductor trunk groups.

## A route-preservation obstruction

For each occupied segment record the **set of conductor identities sharing it**.
A fixed bijection of identities must preserve those sets, not merely the count
of wires or their rendered shapes. Subdividing a segment repeats its set;
contracting a segment removes its set. Neither creates a new shared group.

| Distinct shared groups | Layer candidate | Native reference |
|---|---:|---:|
| Two-conductor groups | 23 | 32 |
| Four-conductor groups | 2 | 10 |

The four-conductor discrepancy alone excludes every fixed identity permutation:
two distinct source groups cannot become ten distinct target groups by renaming
sixteen identities. This is a membership-set count, not a count of repeated
geometric edges. Full source and target membership sets are in the receipt.

The four-conductor bound is not repaired by choosing other bijective interior
sleeve continuations. Starting with one conductor per terminal coloured edge,
backward conservation gives one on every interior coloured edge and two on every
interior white sleeve. Each boundary trunk at stage n=1…7 carries 9−n conductors.
Consequently the only four-conductor trunks are the left and right ones at n=5;
the adjoining white/coloured segments repeat those same two groups.

## Precisely what is and is not ruled out

The obstruction concerns **one fixed identity map, transported with the layer
copies, preserving the identities sharing each represented segment**. It remains
valid when existing source segments are subdivided or contracted. Tests also
check arbitrary ID renaming and a positive self-comparison control.

It does not rule out a construction with explicit inter-layer sewing, different
partial chart occupancy, or newly specified bundle interactions. Such a
construction must say where a retained conductor changes local chart/slot and
verify its full native route afterward. The present layer model has no such
connection map. Assigning native labels now would conceal that missing operation.

The native model remains its stated candidate: a globally chosen bijective
rim/interior middle matching, not a wiring already derived from these layers.
The accurate result is therefore: **sixteen layer conductor routes can be traced,
but they cannot simply be identified with the sixteen native routes under the
fixed-copy, shared-segment-preserving interpretation tested here.**

## Reproduction

- node --test tests/sulfur-layer-correspondence.test.mjs
- node scripts/check-sulfur-layer-correspondence.mjs
- Tracer: research/realization-tower/seed-retained-conductors.mjs
- Invariant: research/realization-tower/route-bundle-invariants.mjs
- Receipt: results/sulfur-layer-correspondence-v1/verification.json

A passing check verifies the route extraction and the obstruction; it does not
mean a successful Su-32 correspondence. No viewer build or routing change is made.
`;
await writeFile('research/strominger/sulfur-layer-correspondence-v1.md',report);
console.log(JSON.stringify({verificationPassed:true,correspondenceEstablished:false,layer:source.counts,obstructions:check.obstructions,report:'research/strominger/sulfur-layer-correspondence-v1.md'},null,2));
