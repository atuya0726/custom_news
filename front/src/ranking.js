import React from 'react'
import axios from 'axios'



const Ranking = async () => {
  let data;
  try{
    data = await axios.get("http://custom-news")
  }
  catch(e){
    console.log(e)
  }
  finally{
    return (
      <div>{data}</div>
    )
  }
 
 
  
}

export default Ranking