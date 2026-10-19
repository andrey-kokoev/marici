import {createWriteStream,mkdirSync} from 'node:fs';
import {dirname} from 'node:path';
import {createGzip} from 'node:zlib';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {compileTessellatedAtlas,generateTessellatedAtlas} from './tessellated-atlas.mjs';

const usage='node research/nima/generate-tessellated-atlas.mjs --max-origin N [--mode native|experimental-terminal-PE] [--max-configurations N] [--graph output.jsonl.gz]';
async function main(){
 const args=process.argv.slice(2),options={mode:'experimental-terminal-PE',maxConfigurations:1000000};
 for(let i=0;i<args.length;i++){const key=args[i];if(key==='--help'){console.log(usage);return;}if(!['--max-origin','--mode','--max-configurations','--graph'].includes(key)||!args[i+1])throw Error(usage);const v=args[++i];if(key==='--max-origin')options.maxOrigin=Number(v);if(key==='--mode')options.mode=v;if(key==='--max-configurations')options.maxConfigurations=Number(v);if(key==='--graph')options.graph=v;}
 if(!Number.isInteger(options.maxOrigin)||options.maxOrigin<0)throw Error('--max-origin must be a nonnegative integer');
 if(!Number.isInteger(options.maxConfigurations)||options.maxConfigurations<1)throw Error('--max-configurations must be a positive integer');
 const c=compileTessellatedAtlas(options),r=generateTessellatedAtlas(c,options);let certificates=0;for(const n of r.nodes)certificates+=+c.obligations(n.mask,n.active).certified;
 const summary={schema:'marici.nima.tessellated-atlas-run.v1',maxOrigin:options.maxOrigin,mode:c.mode,complete:r.complete,reason:r.reason??null,configurations:r.nodes.length,certificates,fieldAttachment:c.fieldAttachment};
 if(options.graph){mkdirSync(dirname(options.graph),{recursive:true});const gzip=createGzip(),writing=pipeline(gzip,createWriteStream(options.graph));let buffer='';const put=async row=>{buffer+=JSON.stringify(row,(_,v)=>typeof v==='bigint'?v.toString():v)+'\n';if(buffer.length>131072){if(!gzip.write(buffer))await once(gzip,'drain');buffer='';}};
  await put({type:'header',...summary,edgeColumns:['from','to','interfaceIndex'],macros:'Not included: atomic materialization is a separate planner operation.'});
  await put({type:'registry',geometry:c.geometry,readers:c.readers,variablePackets:c.packets,interfaces:c.interfaces});let edges=0;
  for(let i=0;i<r.nodes.length;i++){const n=r.nodes[i];await put({type:'configuration',id:i,...n,obligations:c.obligations(n.mask,n.active)});for(const o of c.interfaces)if(n.mask&o.sourceBit){const to=r.byMask.get(n.mask|o.targetBit);if(to!==undefined&&(r.nodes[to].active&o.bit)){await put({type:'edge',data:[i,to,o.index]});edges++;}}}
  await put({type:'end',...summary,edges});if(buffer)gzip.write(buffer);gzip.end();await writing;
 }
 console.log(JSON.stringify(summary));if(!r.complete)process.exitCode=2;
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
