import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const api=c.IsotopeWiring,d=api.fixtures().Ca46;
test('editor and export restore enclosing diamonds and the shell-1 vertex contact',()=>{
 for(const standalone of [false,true]){const svg=api.renderSVG(d,{stackedContact:true,standalone});assert.match(svg,/data-cell="s2-01" d="M0 134 L0 234"/);assert.match(svg,/class="stacked-contact" cx="0" cy="134"/);assert.equal((svg.match(/class="space-frame /g)||[]).length,6);assert.equal((svg.match(/class="neutron sketch-cross"/g)||[]).length,20);assert.doesNotMatch(svg,/class="layer-panel"|class="wrapper-attachment"|data-presentation="transport-loop"/);assert.match(svg,/data-shells="s1 s2" d="M0 24 L160 184 L0 344 L-160 184 Z"/);}
});
test('rejected redesigns require explicit opt-in and are not the editor default',()=>{
 assert.match(api.renderSVG(d,{stackedContact:true,presentation:'layers'}),/data-presentation="shell-layers"/);assert.match(api.renderSVG(d,{stackedContact:true,presentation:'terminal-map'}),/class="wrapper-attachment"/);
});
test('historical research projection and other isotope drawings remain unchanged',()=>{
 const baseline=api.renderSVG(d);assert.match(baseline,/data-cell="s2-01" d="M0 154 L0 254"/);assert.doesNotMatch(baseline,/class="layer-panel"/);const ca44=api.fixtures().Ca44;assert.equal(api.renderSVG(ca44,{stackedContact:true}),api.renderSVG(ca44));
});
