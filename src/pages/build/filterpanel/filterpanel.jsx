import React from 'react'
import { SuggestedConfig } from './suggestedConfig'
import { SUGGESTEDCOFIGS } from '../SuggestedConfigData'



export const Filterpanel = () => {
  return (
    <div>
      <div className='Suggested Configs'>
        <p className='label'>Suggested Configs</p>
        <div className='suggested-list'>
          {SUGGESTEDCOFIGS.map((Suggested) => (
            <SuggestedConfig data = {Suggested} />
          ))}
        </div>
      </div>
    </div>
  )
}
