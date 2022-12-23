import Article from "./Article";
import {ListGroup} from 'react-bootstrap'

function ArticlesList(props) {
    const listArticles = props.data.map((article) =>
        <Article article={article} />
    );

    return(
        <ListGroup >
            <ListGroup.Item variant="primary">Yahoo news</ListGroup.Item>
            {listArticles}
        </ListGroup>
        
        
    )
}

export default ArticlesList