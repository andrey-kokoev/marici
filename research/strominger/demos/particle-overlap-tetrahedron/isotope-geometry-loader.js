// Display-only client. Research searches and certificate audits run at publication.
const base=new URL('./isotope-geometry/',import.meta.url);
let manifest=null,grid=null;
const cache=new Map();
async function getManifest(signal){
  if(manifest)return manifest;
  const response=await fetch(new URL('manifest.json',base),{signal,cache:'no-cache'});
  if(!response.ok)throw Error(`Geometry manifest: HTTP ${response.status}`);
  const value=await response.json();
  if(value.schema!=='marici.isotope-geometry-manifest.v1')throw Error('Unsupported geometry manifest');
  manifest=value;return value;
}
async function asset(name,manifest,signal){
  const expected=manifest.assets[name];if(!expected)throw Error(`Missing geometry asset: ${name}`);
  const url=new URL(name,base);url.searchParams.set('v',expected);
  const response=await fetch(url,{signal});
  if(!response.ok)throw Error(`${name}: HTTP ${response.status}`);
  const bytes=await response.arrayBuffer();
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),b=>b.toString(16).padStart(2,'0')).join('');
  if(digest!==expected)throw Error(`${name}: geometry digest mismatch`);
  return JSON.parse(new TextDecoder().decode(bytes));
}
export async function loadIsotopeGeometry(id,{signal}={}){
  if(cache.has(id))return cache.get(id);
  const manifest=await getManifest(signal);
  if(!manifest.isotopes.includes(id))throw Error(`Unknown isotope: ${id}`);
  const [record,sourceGrid]=await Promise.all([asset(`${id}.json`,manifest,signal),grid??asset('grid.json',manifest,signal)]);
  if(record.schema!=='marici.isotope-geometry.v1'||record.isotope!==id)throw Error('Invalid isotope geometry record');
  const items=record.items.map(item=>({species:item.species,tetrahedra:item.cells.map(cell=>({
    addresses:cell.map(n=>sourceGrid.nodes[n].address),points:cell.map(n=>sourceGrid.nodes[n].point)
  }))}));
  const result={isotope:id,items,grid:sourceGrid};
  signal?.throwIfAborted();grid=sourceGrid;cache.set(id,result);return result;
}
