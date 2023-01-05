import { useEffect, useState } from 'react';
import axios from 'axios'
import {Container,Row,Col,Navbar} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import ArticlesList from './components/ArticlesList';
import KeywordsList from './components/KeywordsList';

function App() {
  const [articles, setArticles] = useState([]);
  const [keywords, setKeywords] = useState([]);
  useEffect(() => {
    const getArticles = async () => {
      const response = await axios.get('/fetch');
      setArticles(response.data)
      const response_keywords = await axios.get('/hot_keywords')
      setKeywords(response_keywords.data)
    }
    getArticles();
  },[]);
  return (
  <>
    <Navbar expand="lg" bg = 'primary' variant='dark'>
      <Navbar.Brand>Custom News</Navbar.Brand>
    </Navbar>
    
    <Container>
      <Row bsPrefix='row_hot'>
        <Col><KeywordsList data={keywords} name="Hot Keyword"/></Col>
      </Row>
      <Row>
        <Col> <ArticlesList data={articles} name="Yahoo news!!" /> </Col>
      </Row>
    
    </Container>
  </>
  
  
    
    
  );
}

export default App;
