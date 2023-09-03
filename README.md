# searcher





 <h1>Seacher - Web Crawler and Search Script</h1>
   ![searcher](https://github.com/secforumsnet/searcher/assets/143932328/706cd78b-f6e9-48e9-b481-d93e674fbde9)
  <p>This Python script is designed for web crawling and searching for specific words on a website. It allows you to provide a starting URL and a list of words to search for. The script will crawl the website, search for the specified words, and display results in real-time.</p>

  <h2>Features</h2>

  <ul>
        <li>Crawl a website and search for multiple words in real-time.</li>
        <li>Restrict crawling to the same domain to avoid external links.</li>
        <li>Colored output in the terminal for easy identification of search results.</li>
        <li>Avoids revisiting the same URL to optimize crawling.</li>
    </ul>

   <h2>Requirements</h2>

   <p>Before running the script, make sure you have the following Python libraries installed:</p>

   <ul>
        <li><b>requests:</b> For making HTTP requests to web pages.</li>
        <li><b>BeautifulSoup:</b> For parsing HTML content.</li>
        <li><b>colorama:</b> For adding colored text to the console output.</li>
    </ul>

   <h3>Installation</h3>

  <p>Install the required libraries using the following pip command:</p>

   <pre><code>pip install requests beautifulsoup4 colorama</code></pre>

  <h2>How to Use</h2>

   <ol>
        <li>Clone or download this repository to your local machine.</li>
        <li>Open your terminal or command prompt.</li>
        <li>Navigate to the directory where the script is located.</li>
        <li>Run the script by executing the following command:</li>
    </ol>

   <pre><code>python searcher.py</code></pre>

  <li>Follow the on-screen prompts:</li>

  <ul>
        <li>Enter the website URL to start crawling from.</li>
        <li>Specify the words you want to search for (comma-separated).</li>
    </ul>

  <p>The script will start crawling the website, searching for the specified words, and display results in real-time with green text when a match is found. It will continue crawling within the same domain, avoiding duplicate visits.</p>

   <h2>Contributing</h2>

 <p>If you would like to contribute to this project or report issues, please open an issue or create a pull request on the GitHub repository.</p>

   <h2>License</h2>

   <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
