// Supersession: the legacy SVG-derived routing contract was explicitly removed.
// See docs/isotope-wiring-regression-contract.md. Authored routing is checked by
// apps/isotope-wiring's independent check:routing, not by reviving this API.
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8');
const c=vm.createContext({});vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],c);
const api=c.IsotopeWiring;
const noRouting=value=>{for(const name of ['traceAlternatingEdges','traceRoute','extractRenderedGraph'])assert.equal(typeof value[name],'undefined',`${name}: removed legacy routing must not return`);};

test('legacy routing exports remain removed, with a positive detector control',()=>{
 noRouting(api);
 assert.throws(()=>noRouting({...api,traceAlternatingEdges:()=>({status:'closed'})}),/removed legacy routing/);
 assert.equal(typeof api.renderSVG,'function');assert.equal(typeof api.validate,'function');
});
test('authored arrows remain visible without route playback or trace output',()=>{
 const svg=api.renderSVG(api.fixtures().Li6,{standalone:true});
 assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,8);
 assert.doesNotMatch(svg,/<animate|data-route-step|data-trace|route-marker/);
});
test('obsolete route flags cannot reactivate a legacy route or mutate its definition',()=>{
 const source=api.fixtures().Li6,before=JSON.stringify(source),ordinary=api.renderSVG(source);
 assert.equal(api.renderSVG(source,{routing:true,animate:true,startEdge:'green-top',initialTurn:'left'}),ordinary);
 assert.equal(JSON.stringify(source),before);noRouting(api);
});
test('legacy HTML contains no removed route controls or trace downloads',()=>{
 assert.doesNotMatch(html,/<(?:button|input|select|output)[^>]*id="(?:route|trace|animation|path)-/);
 assert.doesNotMatch(html,/traceAlternatingEdges|extractRenderedGraph/);
 assert.match(html,/id="inspect-toggle"/);assert.match(html,/id="zoom-fit"/);
});
test('rendering and validation preserve explicit model records rather than creating crossing vertices',()=>{
 const source=api.fixtures().Ne20,before=JSON.stringify(source.graph);
 api.renderSVG(source,{standalone:true});api.geometry(source);api.validate(source);
 assert.equal(JSON.stringify(source.graph),before);noRouting(api);
});
test('separate typed routing consumes authored graph and policy, not SVG extraction',()=>{
 const source=readFileSync(new URL('../apps/isotope-wiring/src/domain/route.ts',import.meta.url),'utf8');
 assert.match(source,/export function traceRoute/);assert.match(source,/document\.graph\.edges/);assert.match(source,/document\.policy/);
 assert.doesNotMatch(source,/getBBox|getComputedStyle|querySelector|DOMParser|SVGElement|extractRenderedGraph/);
});
