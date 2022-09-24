import axios from 'axios';
import {useEffect} from 'react';
import {useState} from 'react';

function App() {
  const [data,setData] = useState([]);
  useEffect(() => {
    const getUser = async () => {
      const response = await axios.get('/data');
      setData(response.data)
    }
    getUser()
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
