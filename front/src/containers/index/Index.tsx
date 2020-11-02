import React, { useState, useEffect } from "react"
import { SortableContainer, SortableElement } from 'react-sortable-hoc';
import arrayMove from 'array-move';

import Card from "../../components/card/Card"
import Loader from "../../components/loader/Loader";
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

  const [albums, setAlbums] = useState<ICardObject[]>([])
  const [loading, setLoading] = useState(false)
  const albums_endpoint = process.env.REACT_APP_PUBLIC_BACK_ALBUMS_ENDPOINT || null
  const [initialAlbums, setInitialAlbums] = useState<ICardObject[]>([])

  const getAlbums = () => {
    if(albums_endpoint){
      fetch(albums_endpoint)
      .then((res) => {
        if (res.status === 200) return res.json();
        setLoading(false);
        throw Error(res.statusText);
      })
      .then((json) => {
        setAlbums(json);
        setInitialAlbums(json)
        setLoading(false);
      })
      .catch(() => {});
    } else {
      setAlbums(getAllCards)
    }
  }

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
    setAlbums(arrayMove(albums, oldIndex, newIndex))
  }

  const setNewOrder = () => {
    let newAlbums: ICardObject[] = []
    albums.map((album: ICardObject, idx: number) => {
      if(initialAlbums[idx] !== album){
        album.position = idx
        newAlbums.push(album)
      }
    })
    fetch(`${albums_endpoint}bulk_update/`, {
      method: 'POST',
      body: JSON.stringify(newAlbums),
      headers: {'Content-Type': 'application/json'}
    })
    .then((res) => {
      if (res.status === 200) return res.json();
      throw Error(res.statusText);
    })
    .then(() => {})
    .catch(() => {});
  }

  useEffect(() => {
    setLoading(true);
    getAlbums()
  }, []);
    
  return(
    <IndexContainer>
      <IndexTitle>
        Cats List
        <button onClick={setNewOrder}>Update</button>
      </IndexTitle>
      { loading && <Loader />}
      <SortableList items={albums} onSortEnd={onSortEnd} axis="xy"/>
    </IndexContainer>
  )
}

export default Index;