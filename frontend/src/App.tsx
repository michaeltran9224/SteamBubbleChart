import { useEffect } from 'react'
import { RouterProvider } from "react-router-dom";

import { router } from "./constants/router/router";

function App() {
  const steamId = '76561198017166729';

  useEffect(() => {
    fetch(`/steam/user/games/${steamId}`)
  .then(res => {
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    return res.json();
  })
  .then(data => {
    console.log("Fetched data:", data);
  })
  .catch(error => console.error("Error fetching games:", error));
  }, []);

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  )
}

export default App
