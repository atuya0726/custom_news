import ListGroup from 'react-bootstrap/ListGroup'
import {Container,Row,Col} from 'react-bootstrap'
function article(props) {
    return(
        
           
        <ListGroup.Item action href = {props.article["URL"]}>
            <Container>
                <Row>
                    <Col xs={1}>
                        {props.article["ranking"]}
                    </Col>
                    <Col>
                        {props.article["title"]}
                    </Col>
                </Row>
            </Container>   
        </ListGroup.Item>
            

        
        
    )
}

export default article