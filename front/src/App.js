import { useEffect, useState } from 'react';
import axios from 'axios'
import {Container,Row,Col,Navbar} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import ArticlesList from './components/ArticlesList';

function App() {
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    const getArticles = async () => {
      const response = await axios.get('/all');
      setArticles(response.data)
    }
    getArticles();
  },[]);
  

  return (
  <>
    <Navbar bg = 'primary' variant='dark'>
      <Navbar.Brand>Custom News</Navbar.Brand>
    </Navbar>
    <Container>
    
      <Row>
        <Col> <ArticlesList data={articles} /> </Col>
      </Row>
      <Row>
        <Col>ccccccccc</Col>
        <Col>dddddddddddddd</Col>
      </Row>
    
    </Container>
  </>
  
  
    
    
  );
}

export default App;
