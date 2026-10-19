import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { normalizeNet, repositoryPath } from '../src/conjecture-nets/model.js';
import { normalizeImplications } from '../src/conjecture-nets/ports.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export async function prepareConjectureNets(base = root, {check = false} = {}) {
  const source = path.join(base, 'src/conjecture-nets');
  const catalog = JSON.parse(await fs.readFile(path.join(source, 'catalog.json'), 'utf8'));
  const nets = [], paths = new Set(), ids = new Set();
  for (const item of catalog.nets) {
    if (!repositoryPath(item.path) || paths.has(item.path)) throw Error('Unsafe or duplicate catalog path: ' + item.path);
    const bytes = await fs.readFile(path.join(base, item.path));
    const contract = JSON.parse(bytes.toString('utf8'));
    const net = normalizeNet(contract, item.path, item.title);
    normalizeImplications(net);
    if (ids.has(net.id)) throw Error('Duplicate catalog net ID: ' + net.id);
    ids.add(net.id); paths.add(item.path);
    nets.push({title:item.title,source:item.path,sha256:createHash('sha256').update(bytes).digest('hex'),contract});
  }
  for (const net of nets) for (const n of net.contract.conjectures) {
    if (!n.external_dependency) continue;
    const target=nets.find(t=>t.source===n.external_dependency.contract);
    if (!target || !target.contract.conjectures.some(t=>t.id===n.external_dependency.node)) throw Error('Missing bundled external prerequisite: '+n.id);
  }
  const payload={schema:'marici.conjecture-net-explorer.snapshot.v1',scope:'Curated source snapshot; not formal admission or a full registry',nets};
  const json=JSON.stringify(payload,null,2)+'\n';
  const template=await fs.readFile(path.join(source,'app.html'),'utf8');
  const model=(await fs.readFile(path.join(source,'model.js'),'utf8')).replaceAll('export function ', 'function ');
  const portModel=(await fs.readFile(path.join(source,'ports.js'),'utf8')).replaceAll('export function ', 'function ').replaceAll('export const ', 'const ');
  const portView=await fs.readFile(path.join(source,'port-view.js'),'utf8');
  const app=await fs.readFile(path.join(source,'app.js'),'utf8');
  const d3License=await fs.readFile(path.join(root,'node_modules/d3/LICENSE'),'utf8');
  const d3='/* D3 license\n'+d3License.replaceAll('*/','* /')+'\n*/\n'+await fs.readFile(path.join(root,'node_modules/d3/dist/d3.min.js'),'utf8');
  if (/<\/script/i.test(model+portModel+portView+app+d3)) throw Error('Script terminator in application code');
  let html=template;
  for (const [marker,value] of [['__NET_DATA__',json.replaceAll('<','\\u003c').replaceAll('\u2028','\\u2028').replaceAll('\u2029','\\u2029')],['__D3_CODE__',d3],['__MODEL_CODE__',model+'\n'+portModel],['__APP_CODE__',portView+'\n'+app]]) {
    if (html.split(marker).length!==2) throw Error('Missing/duplicated template marker: '+marker);
    html=html.replace(marker,()=>value);
  }
  const out=path.join(base,'website/public/experiments');
  if (!check) await fs.mkdir(out,{recursive:true});
  for (const [name,content] of [['conjecture-nets.html',html],['conjecture-nets.json',json]]) {
    const file=path.join(out,name);
    if (check) {
      if (await fs.readFile(file,'utf8').catch(()=>null)!==content) throw Error('Stale '+name+'; run pnpm nets:prepare');
    } else await fs.writeFile(file,content,'utf8');
  }
  return {nets:nets.length,nodes:nets.reduce((n,x)=>n+x.contract.conjectures.length,0),check};
}
if (process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  console.log(JSON.stringify(await prepareConjectureNets(root,{check:process.argv.includes('--check')})));
}
