<h1 align="center">Compile Chandra - The Next Gen Compiler</h1>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#about-the-project">About the Project</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-it-works">How It Works</a></li>
  <li><a href="#getting-started">Getting Started</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#media--screenshots">Media &amp; Screenshots</a></li>
  <li><a href="#license">License</a></li>
</ul>

<hr/>

<h2 id="about-the-project">About the Project</h2>
<p><b>Compile Chandra</b> is a modern, web-based mini-compiler suite that allows you to:</p>
<ul>
  <li>Compile and run code in C, C++, Python, and JavaScript directly from your browser.</li>
  <li>Analyze code lexically (tokenization).</li>
  <li>Generate parse trees for expressions.</li>
  <li>Generate and optimize intermediate code (Three-Address Code).</li>
  <li>Learn language syntax and features with an interactive reference guide.</li>
</ul>
<p>The project is built with a Python Flask backend and a single-page HTML/JS frontend, providing a seamless, interactive experience for learning and experimenting with compiler concepts.</p>

<hr/>

<h2 id="features">Features</h2>
<ul>
  <li><b>Online Code Runner:</b> Write, compile, and execute code in C, C++, Python, and JavaScript. Output and errors are displayed instantly.</li>
  <li><b>Lexical Analyzer:</b> Tokenize source code, view token types, counts, and details.</li>
  <li><b>Parse Tree Generator:</b> Visualize the parse tree for arithmetic expressions.</li>
  <li><b>Intermediate Code Generator:</b> Convert expressions to three-address code (TAC).</li>
  <li><b>Code Optimization:</b> Apply optimizations like constant folding, dead code elimination, common subexpression elimination, and strength reduction.</li>
  <li><b>Language Reference:</b> Browse keywords, operators, separators, identifiers, and literals for supported languages.</li>
</ul>

<hr/>

<h2 id="how-it-works">How It Works</h2>
<h3>Backend (<code>app.py</code>)</h3>
<ul>
  <li>Flask API exposes a <code>/run</code> endpoint.</li>
  <li>Receives code and language via POST.</li>
  <li>For C/C++: Saves code to a temp file, compiles with <code>gcc</code>/<code>g++</code>, runs the binary, and returns output/errors.</li>
  <li>For Python/JavaScript: Saves code to a temp file, runs with <code>python3</code>/<code>node</code>, and returns output/errors.</li>
  <li>Cleans up all temp files after execution.</li>
</ul>
<h3>Frontend (<code>project_pbl.html</code>)</h3>
<ul>
  <li>Single-page app with tabs for each feature.</li>
  <li><b>Code Runner:</b> Sends code and language to the backend, displays output/errors.</li>
  <li><b>Lexical Analyzer:</b> Pure JavaScript implementation; tokenizes code and displays results in tables.</li>
  <li><b>Parse Tree Generator:</b> Builds and displays a parse tree for a given expression.</li>
  <li><b>Intermediate Code &amp; Optimization:</b> Generates TAC and applies selected optimizations, showing before/after and step-by-step explanations.</li>
  <li><b>Language Reference:</b> Interactive guide for C, C++, Java, Python, and JavaScript.</li>
</ul>

<hr/>

<h2 id="getting-started">Getting Started</h2>
<h3>Prerequisites</h3>
<ul>
  <li>Python 3.x</li>
  <li><code>pip</code> (Python package manager)</li>
  <li>Node.js (for JavaScript code execution)</li>
  <li>GCC/G++ (for C/C++ code execution)</li>
</ul>
<h3>Installation</h3>
<ol>
  <li><b>Clone the repository:</b><br/>
    <pre>git clone &lt;your-repo-url&gt;
cd CompileChandra</pre>
  </li>
  <li><b>Install Python dependencies:</b><br/>
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li><b>Run the backend server:</b><br/>
    <pre>python app.py</pre>
    The Flask server will start at <code>http://127.0.0.1:5000</code>.
  </li>
  <li><b>Open the frontend:</b><br/>
    Open <code>project_pbl.html</code> in your web browser.
  </li>
</ol>

<hr/>

<h2 id="usage">Usage</h2>
<ul>
  <li><b>Code Runner:</b> Select a language, enter code, and click "Run Code". Output and errors appear below.</li>
  <li><b>Lexical Analyzer:</b> Paste code, click "Analyze Code" to see tokens and their types.</li>
  <li><b>Parse Tree Generator:</b> Enter an expression (e.g., <code>a=b*c+d-e</code>), click "Generate Parse Tree" to visualize.</li>
  <li><b>Intermediate Code:</b> Enter an expression, click "Generate IR" to see three-address code and temp variables.</li>
  <li><b>Code Optimization:</b> Enter an expression, select optimizations, click "Optimize Code" to see original and optimized IR, with step-by-step explanations.</li>
  <li><b>Language Reference:</b> Use the dropdown and tabs to explore language features.</li>
</ul>

<hr/>

<h2 id="project-structure">Project Structure</h2>
<pre>
CompileChandra/
├── app.py                # Flask backend for code execution
├── project_pbl.html      # Main frontend (HTML, CSS, JS)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── Media Resources/      # Images and GIFs for documentation
</pre>

<hr/>

<h2 id="media--screenshots">Media &amp; Screenshots</h2>
<ul>
  <li><b>Demo GIF:</b><br/>
    <img src="Media%20Resources/outputgif.gif" width="650" alt="Demo"/>
  </li>
  <li><b>Sample Source Code:</b><br/>
    <img src="Media%20Resources/mysourcecode.png" width="500" alt="Source Code"/>
  </li>
  <li><b>Output Console:</b><br/>
    <img src="Media%20Resources/outputconsole.png" width="500" alt="Output Console"/>
  </li>
  <li><b>Output File:</b><br/>
    <img src="Media%20Resources/outputfile.png" width="650" alt="Output File"/>
  </li>
</ul>

<hr/>

<h2 id="license">License</h2>
<p>This project is for educational purposes. See <b>LICENSE</b> if present.</p>

<hr/>

<p align="center"><b>Enjoy learning and experimenting with compiler technology!</b></p>

    
