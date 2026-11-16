import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
import {prepare as checkExtraction} from './extract-isotope-reference.mjs';
const target=new URL('../examples/isotope-wiring/index.html',import.meta.url);
export async function prepareEmbeddedReference({check=false}={}){
 await checkExtraction({check:true});
 const resource=JSON.parse(await readFile(new URL('../research/matter/isotope-reference.resource.json',import.meta.url),'utf8'));
 const block='<!-- isotope-reference-data:start -->\n<script type="application/json" id="isotope-reference-data">'+JSON.stringify(resource).replaceAll('<','\\u003c')+'</script>\n<!-- isotope-reference-data:end -->';
 const html=await readFile(target,'utf8'),pattern=/<!-- isotope-reference-data:start -->[\s\S]*?<!-- isotope-reference-data:end -->/g;
 assert.equal([...html.matchAll(pattern)].length,1,'Expected one embedded reference block');
 const updated=html.replace(pattern,()=>block);
 if(check)assert.equal(updated===html,true,'Embedded reference is stale; run node scripts/prepare-isotope-wiring-reference.mjs');
 else if(updated!==html)await writeFile(target,updated);
 return {rows:resource.data.length,changed:updated!==html,check};
}
if(process.argv[1]&&pathToFileURL(resolve(process.argv[1])).href===import.meta.url)console.log(await prepareEmbeddedReference({check:process.argv.includes('--check')}));
