import { useEffect } from 'react'
import { RouterProvider } from "react-router-dom";

import { router } from "./constants/router/router";

function App() {
  const steamId = '76561198112529535';

  useEffect(() => { // temp for testing
    fetch(`/steam/user/games/${steamId}`).then(res => {
      console.log(res);
      res.json();
    }).then(data => {
      console.log(data);
    }).catch(error => console.log(error));
  }, []);

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  )
}

export default App
