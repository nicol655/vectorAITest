import React from "react"
import { Spin } from 'antd';

import { LoaderContainer } from "./Loader.style"

const Loader = () => {
  return(
    <LoaderContainer>
      <Spin size="large" />
    </LoaderContainer>
  )
}

export default Loader