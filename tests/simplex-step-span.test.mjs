import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { chromium } from '@playwright/test';
import { buildShell } from '../examples/simplex-step-span/model.js';

test('ESD7 shell matches canonical boundary census exactly',async()=>{
  const shell=buildShell();
  assert.equal(shell.tetrahedronCount,343);
  assert.deepEqual([shell.vertices.length,shell.edges.length,shell.triangles.length],[100,294,196]);
  assert.equal(shell.vertices.length-shell.edges.length+shell.triangles.length,2);
  for(const vertex of shell.vertices){assert.equal(vertex.barycentric.reduce((a,b)=>a+b),7);assert.ok(vertex.barycentric.includes(0));}
  for(let facet=0;facet<4;facet++)assert.equal(shell.triangles.filter(t=>t.every(i=>shell.vertices[i].barycentric[facet]===0)).length,49);
  const incidences=new Map();
  for(const t of shell.triangles)for(const [a,b] of [[0,1],[1,2],[2,0]]){
    const key=[t[a],t[b]].sort((x,y)=>x-y).join(',');incidences.set(key,(incidences.get(key)||0)+1);
  }
  assert.ok([...incidences.values()].every(n=>n===2));
  const census=JSON.parse(await readFile(new URL('../research/voevodsky/results/esd7_explicit_analytical_census.json',import.meta.url),'utf8'));
  const vertices=new Map(census.vertices.map(v=>[v.id,v.barycentric]));
  const key=points=>points.map(p=>p.join(',')).sort().join('|');
  const expected=census.triangles.filter(f=>f.incidence===1).map(f=>key(f.vertices.map(id=>vertices.get(id)))).sort();
  const actual=shell.triangles.map(t=>key(t.map(i=>shell.vertices[i].barycentric))).sort();
  assert.deepEqual(actual,expected);
});

test('shell draws locally with camera and opacity controls, without path UI',async()=>{
  const root=new URL('../website/public/experiments/simplex-step-span/',import.meta.url);
  const server=createServer(async(req,res)=>{
    try {
      const pathname=new URL(req.url,'http://localhost').pathname;
      const file=new URL('.'+(pathname==='/'?'/index.html':pathname),root);
      if(!file.href.startsWith(root.href))throw Error('Invalid path');
      const body=await readFile(file);
      res.setHeader('Content-Type',file.pathname.endsWith('.js')?'text/javascript':file.pathname.endsWith('.css')?'text/css':'text/html');res.end(body);
    }catch{res.statusCode=404;res.end();}
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const browser=await chromium.launch({headless:true});
  try {
    const page=await browser.newPage(),errors=[],url=`http://127.0.0.1:${server.address().port}/`;
    page.on('pageerror',e=>errors.push(e.message));
    await page.route('**/*',route=>route.request().url().startsWith(url)?route.continue():route.abort());
    await page.goto(url);await page.waitForFunction(()=>window.ReferenceViewer?.snapshot().calls>0);
    assert.equal(await page.locator('#fallback').isVisible(),false);
    assert.equal(await page.locator('#step, #green-mode').count(),0);
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().triangleCount),196);
    assert.equal(await page.evaluate(()=>ReferenceViewer.snapshot().calls),2);
    await page.locator('#opacity').fill('0');await page.waitForFunction(()=>ReferenceViewer.snapshot().opacity===0);
    const before=await page.evaluate(()=>ReferenceViewer.snapshot().azimuth);
    await page.locator('#right').click();assert.notEqual(await page.evaluate(()=>ReferenceViewer.snapshot().azimuth),before);
    await page.locator('#reset').click();
    await page.setViewportSize({width:390,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.evaluate(()=>ReferenceViewer.dispose());assert.equal(await page.locator('#fallback').isVisible(),true);
    assert.deepEqual(errors,[]);
    const noJS=await browser.newPage({javaScriptEnabled:false});await noJS.goto(url);assert.equal(await noJS.locator('#fallback').isVisible(),true);
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
});
