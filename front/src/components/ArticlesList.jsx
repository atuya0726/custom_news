import Article from "./Article";
import {ListGroup} from 'react-bootstrap'

function ArticlesList(props) {
    const listArticles = props.data.map((article) =>
        <Article article={article} />
    );

    return(
        <ListGroup >
            <ListGroup.Item variant="primary">{props.name}</ListGroup.Item>
            {listArticles}
        </ListGroup>
    )
}

export default ArticlesList