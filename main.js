const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  try {
    // Navigate to the desired page (after manual login)
    await page.goto('https://cloud.jonas-premier.com/');

    console.log('Page loaded. You can now start clicking on elements.');
    console.log('Press Ctrl+C to stop the script.');

    // Set up a listener for console messages from the page
    page.on('console', msg => {
      if (msg.type() === 'log') {
        console.log(msg.text());
      }
    });

    // Listen for click events and log them to the console
    await page.evaluate(() => {
      document.addEventListener('click', (event) => {
        let element = event.target;
        let value = element.textContent || element.value || 'No value';
        console.log(`Clicked element: ${element.tagName}, Value: ${value}`);
      }, true);
    });

    // Keep the script running indefinitely
    await new Promise(() => {});

  } catch (error) {
    console.error('An error occurred:', error);
  } finally {
    await browser.close();
  }
})();