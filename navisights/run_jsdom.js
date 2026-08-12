const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const path = require('path');

const virtualConsole = new VirtualConsole();
virtualConsole.on("error", (...args) => console.log("JSDOM ERROR:", ...args));
virtualConsole.on("warn", (...args) => console.log("JSDOM WARN:", ...args));
virtualConsole.on("log", (...args) => console.log("JSDOM LOG:", ...args));
virtualConsole.on("jsdomError", (err) => console.log("JSDOM EXCEPTION:", err.message, err.stack));

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');

const dom = new JSDOM(html, {
  url: "http://localhost:8080/",
  runScripts: "dangerously",
  resources: "usable",
  virtualConsole
});

setTimeout(() => {
  console.log("Root innerHTML length after 2s:", dom.window.document.getElementById('root').innerHTML.length);
  console.log("Root innerHTML snippet:", dom.window.document.getElementById('root').innerHTML.substring(0, 300));
}, 2000);
