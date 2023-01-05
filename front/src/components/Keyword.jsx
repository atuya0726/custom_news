import ListGroup from 'react-bootstrap/ListGroup'
import {Container,Row,Col} from 'react-bootstrap'
import Accordion from 'react-bootstrap/Accordion'
function keyword(props) {
    return(
       
                
        <Accordion.Item eventKey={String(props.index)}>
            <Accordion.Header>
                <Container>
                    <Row>
                        <Col xs={1}>
                            {props.index}
                        </Col>
                        <Col xs={2}>
                            score: {parseInt(props.keyword[1]["score"])}
                        </Col>
                        <Col>
                            {props.keyword[0]}
                        </Col>       
                    </Row>
                </Container>
                
            </Accordion.Header>
            <Accordion.Body>
                {props.keyword[1]["content"]}
            </Accordion.Body>
        </Accordion.Item>
                
           
    )
}

export default keyword