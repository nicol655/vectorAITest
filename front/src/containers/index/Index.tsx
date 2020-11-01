import React, { useState } from "react"
import { SortableContainer, SortableElement } from 'react-sortable-hoc';
import arrayMove from 'array-move';

import Card from "../../components/card/Card"
import { getAllCards } from "../../__fixtures__/cards"
import { 
  CardsContained, CardsContainer, IndexContainer, IndexTitle 
} from "./IndexContainer.style"

interface ICardObject {
  type: string;
  title: string;
  position: number;
  img_src: string;
}

interface IOnSortEnd {
  oldIndex: number;
  newIndex: number;
}

const Index = () => {

  const [cards, setCards] = useState(getAllCards)

  
  const SortableItem = SortableElement(({value}: any) => {
    return(
      <CardsContained>
        <Card title={value.title} img_src={value.img_src} img_alt="" 
          position={value.position}/>  
      </CardsContained>
    )
  })

  const SortableList = SortableContainer(({items}: any) => {
    return (
      <CardsContainer>
        { items.map((card: ICardObject, index: number) => (
          <SortableItem key={`item-${card.type}`} index={index} value={card} />
        ))}
      </CardsContainer>
    )
  })

  const onSortEnd = ({oldIndex, newIndex}: IOnSortEnd) => {
    setCards(arrayMove(cards, oldIndex, newIndex))
  }
    
  return(
    <IndexContainer>
      <IndexTitle>Cats List</IndexTitle>
        <SortableList items={cards} onSortEnd={onSortEnd} axis="xy"/>
    </IndexContainer>
  )
}

export default Index;