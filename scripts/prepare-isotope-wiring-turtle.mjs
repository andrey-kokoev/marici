// Embed a Python-validated snapshot; refuse stale data or validation inputs.
import assert from 'node:assert/strict';
import {readFile,readdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
const root=new URL('../',import.meta.url);
const snapshotPath=new URL('examples/isotope-wiring/core/ne20-inventory.json',root);
const htmlPath=new URL('examples/isotope-wiring/index.html',root);
const prefix='research/strominger/isotope-schema/';
const artifact=prefix+'results/neon-20-inventory.ttl';
const reference='research/matter/isotope-reference.resource.json';
const hash=raw=>createHash('sha256').update(raw).digest('hex');
const marker=/<!-- isotope-turtle-inventory:start -->[\s\S]*?<!-- isotope-turtle-inventory:end -->/g;

export async function prepareEmbeddedTurtle({check=false,snapshotFile=snapshotPath}={}){
 const snapshot=JSON.parse(await readFile(snapshotFile,'utf8'));
 assert.equal(snapshot.schema,'marici.editor-turtle-inventory.v1');
 assert.equal(snapshot.definitionId,'Ne20');
 assert.equal(snapshot.validation,'SHACL-and-source-replay-at-build-time');
 assert.equal(snapshot.subject,'urn:marici:isotope-reference:Neon-20');
 assert.deepEqual(snapshot.readouts,{Z:10,N:10,A:20,electrons:null,charge_e:null});
 assert.equal(snapshot.artifactPath,artifact);
 assert.equal(snapshot.source.path,reference);
 assert.equal(snapshot.source.operation,'urn:marici:isotope:ReferenceNuclearInventoryV1');
 const expected=[...(await readdir(new URL(prefix,root))).filter(n=>/\.(py|ttl)$/.test(n)).map(n=>prefix+n),artifact,reference,'scripts/prepare-isotope-wiring-turtle.py'].sort();
 assert.deepEqual(Object.keys(snapshot.inputs).sort(),expected,'Validation input set changed; regenerate the Python snapshot');
 for(const file of expected)assert.equal(hash(await readFile(new URL(file,root))),snapshot.inputs[file],`Stale validated Turtle snapshot: ${file}; run prepare-isotope-wiring-turtle.py`);
 const raw=await readFile(new URL(artifact,root));
 assert.equal(snapshot.turtle,raw.toString('utf8'));
 assert.equal(snapshot.turtleSha256,hash(raw));
 assert.equal(snapshot.source.sha256,snapshot.inputs[reference]);
 const encoded=JSON.stringify(snapshot).replaceAll('<','\\u003c').replaceAll('>','\\u003e').replaceAll('&','\\u0026');
 const block=`<!-- isotope-turtle-inventory:start -->\n<script type="application/json" id="isotope-turtle-inventory">${encoded}</script>\n<!-- isotope-turtle-inventory:end -->`;
 const html=await readFile(htmlPath,'utf8');
 assert.equal([...html.matchAll(marker)].length,1,'Expected one Turtle snapshot embedding slot');
 const updated=html.replace(marker,()=>block);
 if(check)assert.equal(html,updated,'Embedded Turtle snapshot is stale');
 else if(html!==updated)await writeFile(htmlPath,updated);
 return {definitionId:'Ne20',changed:html!==updated,turtleSha256:snapshot.turtleSha256};
}
if(process.argv[1]&&pathToFileURL(resolve(process.argv[1])).href===import.meta.url){
 assert(process.argv.slice(2).every(arg=>arg==='--check'));
 console.log(await prepareEmbeddedTurtle({check:process.argv.includes('--check')}));
}
