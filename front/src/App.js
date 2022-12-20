import axios from 'axios';
import {useEffect} from 'react';
import {useState} from 'react';

function App() {
  const [data,setData] = useState([]);
  useEffect(() => {
    const getData = async () => {
      const response = await axios.get('/data');
      setData(response.data)
    }
    getData()
  }, [])
  return (
    <div>
      {data}
      <input type="text"/>
      <button>タスクを追加</button>
      <button>タスクを削除</button>
    </div>
    

  );
}

export default App;
