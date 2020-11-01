import React from "react"
import "antd/dist/antd.css";

import Index from "./containers/index/Index"
import { AppContainer } from "./AppContainer.style"

function App() {
  return (
    <AppContainer>
      <Index />
    </AppContainer>
  );
}

export default App;
