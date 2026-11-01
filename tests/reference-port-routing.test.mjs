import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { chromium } from '@playwright/test';
import { createPortRouter } from '../public/experiments/reference-port-router.mjs';
import { buildReferencePortRouting } from '../scripts/build-reference-port-routing.mjs';

const read=p=>readFileSync(new URL(p,import.meta.url),'utf8');
const extract=html=>JSON.parse(html.match(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
const data=extract(read('../research/chatgpt/reflection_port_routing.html'));
const prior=extract(read('../research/chatgpt/reflection_32_connection_view.html'));
const router=createPortRouter(data);
const labels=['O','A','B','D','E'];
const payload=Object.fromEntries(labels.map((label,i)=>[label,{token:label,nested:[i,'opaque']}])) ;
const identity=[[['1','0'],['0','1']],['0','0']];

function paths(a,b,adj,seen=[]) {
  const path=[...seen,a];if(a===b) return [path];
  return adj.get(a).filter(c=>!path.includes(c)).flatMap(c=>paths(c,b,adj,path));
}

test('generated standalone page is reproducible and retains the reference geometry and all histories',()=>{
  assert.equal(read('../public/experiments/reflection-port-routing.html'),buildReferencePortRouting());
  assert.deepEqual(data.histories,prior.histories);
  for(const c of data.cells) {
    assert.deepEqual(c.triangle,prior.cells[c.id].exact_vertices);
    assert.deepEqual(c.histories,prior.cells[c.id].histories);
  }
  const edges=list=>list.map(pair=>[...pair].sort((a,b)=>a-b).join('-')).sort();
  assert.deepEqual(edges(data.seams.map(s=>s.cells)),edges(prior.contacts));
  const pairs=list=>list.map(pair=>[...pair].sort().join('-')).sort();
  assert.deepEqual(pairs(data.routes.map(r=>[r.history_from,r.history_to])),pairs(prior.links.map(l=>[l.a,l.b])));
  assert.deepEqual(router.audit,{requests:32,cells:14,seams:14,ports:42,externalPorts:14,simpleRoutes:54,shortestTraversals:80});
});

test('independent path enumeration, paired ports, continuous 4D routes and load census',()=>{
  const adj=new Map(data.cells.map(c=>[c.id,[]]));
  for(const [a,b] of prior.contacts){adj.get(a).push(b);adj.get(b).push(a);}
  const loads=new Map(),lengths={};
  for(const r of data.routes) {
    const all=paths(r.source,r.target,adj),shortest=Math.min(...all.map(p=>p.length));
    assert.equal(all.filter(p=>p.length===shortest).length,1);
    assert.deepEqual(all.map(JSON.stringify).sort(),r.all_simple_paths.map(JSON.stringify).sort());
    lengths[r.length]=(lengths[r.length]??0)+1;
    for(let i=1;i<r.path.length;i++) {
      const key=[r.path[i-1],r.path[i]].sort((a,b)=>a-b).join('-');loads.set(key,(loads.get(key)??0)+1);
    }
    for(const lift of ['centered','asymmetric']) for(const [routeIndex,path] of r.all_simple_paths.entries()) {
      const packet=router.packet({requestId:r.id,routeIndex,lift});
      assert.equal(packet.polyline4.length,2*path.length-1);
      for(let i=0;i<path.length;i++) {
        assert.deepEqual(packet.polyline4[2*i],data.cells.find(c=>c.id===path[i]).centers4[lift]);
        if(i+1<path.length) {
          const a=data.ports.find(p=>p.cell===path[i]&&p.neighbor===path[i+1]);
          const b=data.ports.find(p=>p.cell===path[i+1]&&p.neighbor===path[i]);
          assert.deepEqual(a.midpoint4,b.midpoint4);
          assert.deepEqual(packet.polyline4[2*i+1],a.midpoint4);
        }
      }
    }
  }
  assert.deepEqual(lengths,{1:10,2:12,3:4,4:1,5:2,6:2,8:1});
  assert.equal(loads.size,13);assert.equal(loads.get('2-3'),12);assert.equal(loads.has('1-8'),false);
  for(const seam of data.seams) assert.equal(seam.shortest_route_load,loads.get([...seam.cells].sort((a,b)=>a-b).join('-'))??0);
});

test('every prefix of all 54 routes, both lifts and directions transports all five labelled payload slots exactly',()=>{
  for(const r of data.routes) for(const [routeIndex,path] of r.all_simple_paths.entries())
    for(const lift of ['centered','asymmetric']) for(const reverse of [false,true]) {
      for(let position=0;position<path.length;position++) {
        const p=router.packet({requestId:r.id,routeIndex,lift,reverse,position,payload});
        const cell=data.cells.find(c=>c.id===p.currentCell);
        assert.equal(p.historyFrom,reverse?r.history_to:r.history_from);
        assert.equal(p.historyTo,reverse?r.history_from:r.history_to);
        assert.deepEqual(p.slots.map(s=>s.coordinates),cell.vertices4[lift]);
        assert.deepEqual(p.slots.map(s=>s.value),labels.map(l=>payload[l]));
        assert.deepEqual(p.visitedRoute,p.path.slice(0,position+1));
        assert.deepEqual(p.cellHistories,cell.histories);
        assert.equal(p.ingress?.neighbor??null,position?p.path[position-1]:null);
        assert.equal(p.egress?.neighbor??null,position+1<p.path.length?p.path[position+1]:null);
        if(p.egress) assert.deepEqual(p.egress.midpoint4,p.pairedEgress.midpoint4);
        assert.equal(p.completed,position===path.length-1);
        if(position===0) assert.deepEqual(p.transport,identity);
        assert.deepEqual(p.endpointTransport,reverse?router.inverse(r.transport):r.transport);
      }
      const last=router.packet({requestId:r.id,routeIndex,lift,reverse,position:path.length-1,payload});
      assert.deepEqual(last.transport,last.endpointTransport);
    }
  const p=router.packet({payload});p.slots[0].value.nested[0]='changed';
  assert.equal(payload.O.nested[0],0);
  assert.equal(router.packet({payload}).slots[0].value.nested[0],0);
});

test('rejects invalid navigation, label swaps, corrupt seam maps and non-seam shortcuts',()=>{
  for(const args of [{requestId:-1},{requestId:32},{requestId:0.5},{routeIndex:99},{position:-1},{position:999},{lift:'other'},{reverse:'yes'}])
    assert.throws(()=>router.packet(args));
  for(const modify of [
    d=>{d.seams[0].label_permutation=[1,0,2,3,4];},
    d=>{d.seams[0].reflection[1][0]='99';},
    d=>{d.ports[0].midpoint4[0]='99';},
    d=>{d.routes[0].all_simple_paths=[[0,2]];},
    d=>{const r=d.routes.find(r=>r.previous_contact==='separated');r.all_simple_paths=[[r.source,r.target]];},
    d=>{d.cells[0].vertices4.centered[3][2]='2';},
  ]) {const bad=structuredClone(data);modify(bad);assert.throws(()=>createPortRouter(bad));}
});

test('browser: integrated mode, payload editing, every request and alternative, reversal, lifts and mobile',async()=>{
  const browser=await chromium.launch({headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
    page.on('pageerror',error=>errors.push(error.message));
    await page.goto(new URL('../public/experiments/hex-edge-grid.html',import.meta.url).href);
    await page.locator('[data-stage="4"]').click();
    await page.locator('#process').selectOption('reference');
    const frame=page.frameLocator('#reference-router');
    await frame.locator('#packet-audit').waitFor();
    assert.equal(await page.locator('#hex-workspace').isVisible(),false);
    assert.equal(await page.locator('#radius').isVisible(),false);
    await frame.locator('#payload-O').fill('<opaque>&unchanged');
    await frame.locator('#next').click();
    assert.match(await frame.locator('#values').innerText(),/<opaque>&unchanged/);
    await frame.locator('#request').selectOption('1');
    assert.equal(await frame.locator('#payload-O').inputValue(),'request-2:O');
    await frame.locator('#request').selectOption('0');
    assert.equal(await frame.locator('#payload-O').inputValue(),'<opaque>&unchanged');
    const child=page.frames().find(f=>f.url().endsWith('/reflection-port-routing.html'));
    const result=await child.evaluate(()=>{
      let states=0;
      const change=(id,value)=>{const el=document.getElementById(id);el.value=String(value);el.dispatchEvent(new Event('change'));};
      for(const request of auditViewer.data.routes) {
        change('request',request.id);
        for(let choice=0;choice<request.all_simple_paths.length;choice++) {
          change('route',choice);
          for(const lift of ['centered','asymmetric']) {
            change('lift',lift);
            for(let direction=0;direction<2;direction++) {
              const path=auditViewer.getState().path;
              for(let i=0;i<path.length;i++) {
                const p=referenceRouting.getPacket();
                if(p.position!==i||p.currentCell!==path[i]) throw Error('Viewer packet drift');
                if(!document.getElementById('packet-summary').textContent.includes('C'+path[i])) throw Error('Stale inspector');
                states++;
                if(i+1<path.length) document.getElementById('next').click();
              }
              if(!document.getElementById('next').disabled) throw Error('Missing endpoint guard');
              document.getElementById('reverse').click();
            }
          }
        }
      }
      return {states};
    });
    assert.ok(result.states>500);
    await frame.locator('#ports').uncheck();await frame.locator('#loads').check();
    await frame.locator('#next').click();await frame.locator('#prev').click();
    assert.equal(await child.evaluate(()=>referenceRouting.getPacket().position),0);
    await page.locator('#process').selectOption('process1');
    assert.equal(await page.locator('[data-stage="4"]').getAttribute('aria-pressed'),'true');
    await page.locator('#process').selectOption('reference');
    await frame.locator('#request').selectOption('0');
    assert.equal(await frame.locator('#payload-O').inputValue(),'<opaque>&unchanged');
    await page.setViewportSize({width:390,height:844});
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.ok(await child.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.deepEqual(errors,[]);
  } finally {await browser.close();}
});
