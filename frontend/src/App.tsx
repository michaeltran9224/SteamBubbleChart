import { RouterProvider } from "react-router-dom";
import { useEffect } from "react";
import { router } from "./constants/router/router";

import NavTest from "./pages/NavTest";
import Home from "./pages/Home/Home";

function App() {
  const steamId = "76561198112529535";

  useEffect(() => {
    // temp for testing
    fetch(`/steam/user/games/${steamId}`)
      .then((res) => {
        console.log(res);
        res.json();
      })
      .then((data) => {
        console.log(data);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
