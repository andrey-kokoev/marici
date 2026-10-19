import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { normalizeNet, sourceURL, repositoryPath } from '../src/conjecture-nets/model.js';
import { prepareConjectureNets } from '../scripts/prepare-conjecture-nets.mjs';
import { normalizeImplications, reachablePorts, portKey } from '../src/conjecture-nets/ports.js';

const fixture=()=>({id:'test',conjectures:[{id:'a',depends_on:[],status:'source_located',outcome:null},{id:'b',depends_on:['a'],status:'open',outcome:null}],frontier:['b'],boundary:{physical:false}});
test('DAG levels, dispositions and null outcomes are preserved without mutating inputs',()=>{
  const raw=fixture(), before=JSON.stringify(raw), n=normalizeNet(raw);
  assert.deepEqual(n.nodes.map(n=>n.level),[0,1]); assert.equal(n.nodes[0].status,'source_located');assert.equal(n.nodes[1].outcome,null);assert.equal(JSON.stringify(raw),before);
});
for (const [name,mutate] of [
  ['missing parent',r=>r.conjectures[1].depends_on.push('absent')],
  ['cycle',r=>r.conjectures[0].depends_on.push('b')],
  ['duplicate',r=>r.conjectures[1].id='a'],
  ['duplicate dependency',r=>r.conjectures[1].depends_on.push('a')],
  ['bad frontier',r=>r.frontier.push('missing')],
  ['bad parent type',r=>r.conjectures[1].depends_on=[1]],
]) test('reject '+name,()=>{const r=fixture();mutate(r);assert.throws(()=>normalizeNet(r));});
test('repository links reject scripts, traversal, remote URLs and Windows absolute paths',()=>{
  for (const p of ['javascript:alert(1)','https://evil.test','research/../secret','research/./foo','C:/secret','research//foo','research/<img>.md']) {assert.equal(repositoryPath(p),false);assert.equal(sourceURL(p),null);}
  assert.equal(sourceURL('research/a b.md',true),'../../../research/a%20b.md');assert.match(sourceURL('research/a.md'),/^https:\/\/github.com\//);
});
test('port implications never inferred from prerequisites; AND and same-node ports remain distinct',()=>{
  const raw={id:'ports',conjectures:['a','b','c','d','e'].map(id=>({id})),port_implications:[
    {id:'ab',from:{node:'a',port:'++'},to:{node:'b',port:'++'},weight:4},
    {id:'bc',from:{node:'b',port:'++'},to:{node:'c',port:'-+'}},
    {id:'and',premises:[{node:'b',port:'++'},{node:'d',port:'++'}],to:{node:'e',port:'++'}}
  ]};
  const net=normalizeNet(raw),{rules}=normalizeImplications(net);
  const reach=reachablePorts(rules,[portKey('a','++')]);
  assert.deepEqual([...reach.rules],['ab','bc']);assert.equal(reach.ports.has(portKey('e','++')),false);
  assert.equal(reach.ports.has(portKey('a','--')),false);
  assert.equal(reachablePorts(rules,[portKey('a','++'),portKey('d','++')]).ports.has(portKey('e','++')),true);
  assert.equal(normalizeImplications(normalizeNet(fixture())).rules.length,0);
  assert.equal(rules[0].weight,4);assert.equal(rules[1].weight,1);assert.equal(rules[1].weightDeclared,false);
  raw.port_implications[0].weight=0;assert.throws(()=>normalizeImplications(normalizeNet(raw)),/weight/);
  raw.port_implications[0].weight=1;raw.port_implications[0].to.port='true';assert.throws(()=>normalizeImplications(normalizeNet(raw)),/port/);
});
test('cyclic port reachability terminates; branch activations are not outcome implications',()=>{
  const raw={conjectures:[{id:'a'},{id:'b'}],proof_relations:[
    {id:'ab',premise:'a',premise_outcome:'++',conclusion:'b',conclusion_outcome:'++'},
    {id:'ba',premise:'b',premise_outcome:'++',conclusion:'a',conclusion_outcome:'++'},
    {id:'activation',premise:'a',premise_outcome:'++',conclusion:'b',conclusion_kind:'activate_consequent_not_prove_schema'}
  ]};
  const {rules,omitted}=normalizeImplications(normalizeNet(raw));assert.equal(rules.length,2);assert.equal(omitted.length,1);
  assert.equal(reachablePorts(rules,[portKey('a','++')]).ports.size,2);
});
test('curated generated snapshot is fresh and includes external producer',async()=>{const result=await prepareConjectureNets(undefined,{check:true});assert.equal(result.nets,5);assert.ok(result.nodes>30);});
test('builder escapes script injection, is deterministic and detects stale source and external targets',async()=>{
  const temp=await fs.mkdtemp(path.join(os.tmpdir(),'marici-net-test-'));
  try {
    const src=path.join(temp,'src/conjecture-nets');await fs.mkdir(src,{recursive:true});await fs.mkdir(path.join(temp,'research'),{recursive:true});
    for (const f of ['app.html','model.js','app.js','ports.js','port-view.js']) await fs.copyFile(new URL('../src/conjecture-nets/'+f,import.meta.url),path.join(src,f));
    await fs.writeFile(path.join(src,'catalog.json'),JSON.stringify({nets:[{title:'hostile',path:'research/net.json'}]}));
    const r=fixture();r.conjectures[0].statement='</script><script>globalThis.pwned=true</script>';
    const input=path.join(temp,'research/net.json');await fs.writeFile(input,JSON.stringify(r));
    await prepareConjectureNets(temp);await prepareConjectureNets(temp,{check:true});
    const html=await fs.readFile(path.join(temp,'website/public/experiments/conjecture-nets.html'),'utf8');assert.ok(!html.includes(r.conjectures[0].statement));assert.ok(html.includes('\\u003c/script>'));
    r.conjectures[0].statement='new source';await fs.writeFile(input,JSON.stringify(r));await assert.rejects(prepareConjectureNets(temp,{check:true}),/Stale/);
    r.conjectures[1].external_dependency={contract:'research/missing.json',node:'a'};await fs.writeFile(input,JSON.stringify(r));await assert.rejects(prepareConjectureNets(temp),/external prerequisite/);
  } finally {await fs.rm(temp,{recursive:true,force:true});}
});
