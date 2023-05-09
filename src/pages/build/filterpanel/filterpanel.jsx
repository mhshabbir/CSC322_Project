import React from 'react'
import { SuggestedConfig } from './suggestedConfig'
import { SUGGESTEDCOFIGS } from '../SuggestedConfigData'
import "./filterstyle.css"


export const Filterpanel = () => {
  return (
    <div>
      <div className='Suggested Configs'>
        <p className='label'>
          <b>Suggested Configeration</b>
          </p>
        <div className='suggested-list'>
        <button className='suggested-button'>Create My Own</button>
          {SUGGESTEDCOFIGS.map((Suggested) => (
            <button className='suggested-button'><SuggestedConfig data = {Suggested} /></button>
          ))}
        </div>
      </div>
    </div>
  )
}
