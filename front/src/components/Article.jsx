import ListGroup from 'react-bootstrap/ListGroup'
function article(props) {
    return(
        <ListGroup.Item action href = {props.article["URL"]}>
            {props.article["ranking"]}:{props.article["title"]}
        </ListGroup.Item>
    )
}

export default article