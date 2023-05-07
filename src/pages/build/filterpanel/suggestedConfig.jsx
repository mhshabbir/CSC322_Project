import React from 'react'
import { SUGGESTEDCOFIGS } from '../SuggestedConfigData'

export const SuggestedConfig = (props) => {
  const {id, configName} = props.data

  return (
    <p>
      {configName}
    </p>
  )
}
