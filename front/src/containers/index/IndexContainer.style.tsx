import styled from "styled-components"

export const CardsContainer = styled.ul`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-row-gap: 20px;
  justify-items: center;
  padding: 0;
  list-style: none;
`

export const CardsContained = styled.li`
  list-style: none;
`

export const IndexContainer = styled.div`
  padding: 20px;
`

export const IndexTitle = styled.h1`
  border-bottom: 1px solid #dcdcdc;
  color: #565656;
  margin: 20px 0;
`