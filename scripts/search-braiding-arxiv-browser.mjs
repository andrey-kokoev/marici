import { chromium } from '@playwright/test';
import fs from 'node:fs/promises';
const directory=new URL('../references/braiding/',import.meta.url);
const corpus=JSON.parse(await fs.readFile(new URL('download-manifest.json',directory),'utf8'));
const browser=await chromium.launch({headless:true});
const results=[];
try {
  const page=await browser.newPage({viewport:{width:1360,height:1000}});
  for(const work of corpus) {
    const record={number:work.number,title:work.title,doi:work.doi,searches:[]};results.push(record);
    const queries=[{type:'title',query:work.verified_title||work.title}];
    if(work.doi)queries.push({type:'doi',query:work.doi});
    for(const {type,query} of queries) {
      const address='https://arxiv.org/search/?'+new URLSearchParams({query,searchtype:type,abstracts:'show',order:'-announced_date_first',size:'50'});
      const search={type,query,url:address};record.searches.push(search);
      try {
        await page.goto(address,{waitUntil:'domcontentloaded',timeout:45000});
        const text=await page.locator('body').innerText();
        search.noResults=/produced no results/i.test(text);
        search.results=await page.locator('li.arxiv-result').evaluateAll(items=>items.map(item=>({
          title:item.querySelector('.title')?.textContent.trim(),
          authors:item.querySelector('.authors')?.textContent.trim(),
          abstract:item.querySelector('.abstract-full')?.textContent.trim(),
          links:[...item.querySelectorAll('a[href]')].map(a=>({text:a.textContent.trim(),url:a.href})).filter(a=>a.url.includes('/abs/')||a.url.includes('/pdf/')),
        })));
        search.heading=await page.locator('h1').allTextContents();
        if(!search.noResults&&!search.results.length)search.warning='No result cards or explicit no-results message; inspect this response.';
        console.log(work.number,type,search.noResults?'no results':`${search.results.length} results`,query);
        if(type==='title'||search.results.length||search.warning) {
          const name=`arxiv-browser-${String(work.number).padStart(2,'0')}-${type}.png`;
          await page.screenshot({path:new URL(name,directory).pathname.replace(/^\/([A-Za-z]:)/,'$1'),fullPage:true});
          search.screenshot=name;
        }
      }catch(error){search.error=error.message;console.log('Browser error',work.number,type,error.message);}
      await page.waitForTimeout(3100);
    }
    // Checkpoint each work so a later network failure cannot erase earlier searches.
    await fs.writeFile(new URL('arxiv-browser-results.json',directory),JSON.stringify({searchedAt:new Date().toISOString(),works:results},null,2));
  }
} finally {await browser.close();}
const lines=['# Individual corpus searches in the arXiv browser interface','',
  'Chromium opened the arXiv website for each listed title and, where known, its DOI. This is separate from the earlier API search. Screenshots preserve each title-search page.','',
  '| # | Listed work | Browser result |','|---|---|---|'];
for(const work of results) {
  const status=work.searches.map(s=>`${s.type}: ${s.error?'request error':s.warning?'unclassified response':s.noResults?'no results':`${s.results.length} result(s)`}`).join('; ');
  lines.push(`| ${work.number} | ${work.title} | ${status} |`);
}
await fs.writeFile(new URL('arxiv-browser-report.md',directory),lines.join('\n')+'\n');
console.log('Works searched:',results.length,'Result cards:',results.flatMap(r=>r.searches).reduce((n,s)=>n+(s.results?.length||0),0));
