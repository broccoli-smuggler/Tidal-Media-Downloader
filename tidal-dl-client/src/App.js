import React from 'react';
import './App.css';
import 'iframe-resizer/js/iframeResizer.js'

function App() {
  return (
    <div className="App">
      <main className="App-body">
        <div className="info">
          <p>INFO</p>
        </div>
        <div className="embed">
          <p>TIDAL</p>
          {/*<iframe id="tidal"*/}
          {/*        src="https://embed.tidal.com/tidal-embed.js" scrolling="no" allowfullscreen="0" frameBorder={0}>tidal</iframe>*/}
        </div>
      </main>
      <script type="text/javascript" src="iframeResizer.js"></script>
      <script>
        iFrameResize({}, 'tidal')
      </script>
    </div>
  );
}



export default App;
