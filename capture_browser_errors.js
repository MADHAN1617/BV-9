const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();
    
    page.on('console', msg => console.log('BROWSER LOG:', msg.type(), msg.text()));
    page.on('pageerror', err => console.log('BROWSER UNCAUGHT ERROR:', err.message, err.stack));
    page.on('requestfailed', req => console.log('REQUEST FAILED:', req.url(), req.failure().errorText));

    console.log('Navigating to http://localhost:8080 ...');
    await page.goto('http://localhost:8080', { waitUntil: 'networkidle2', timeout: 10000 });
    
    const bodyHtml = await page.evaluate(() => document.body.innerHTML);
    console.log('BODY HTML LENGTH:', bodyHtml.length);
    console.log('BODY HTML SNIPPET:', bodyHtml.substring(0, 300));
    
    await browser.close();
  } catch (e) {
    console.error('Puppeteer Script Error:', e);
  }
})();
