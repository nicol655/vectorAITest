import React from 'react'
import { 
  Card as AntdCard,
  Image as AntdImage,
  Spin as AntdSpin
} from 'antd'

const { Meta } = AntdCard

interface ICard {
  title: string;
  img_src: string;
  img_alt: string;
  position: number;
}

const Card = (props: ICard) => {
 
  return(
    <AntdCard
      hoverable
      style={{ width: 240 }}
      cover={
        <AntdImage alt={props.img_alt} src={props.img_src} loading="lazy" 
          placeholder={<AntdSpin />}
        />
      }
    >
      <Meta title={props.title} description="www.instagram.com" />
    </AntdCard>
  )
}

export default Card