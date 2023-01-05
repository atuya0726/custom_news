import Keyword from "./Keyword";
import {ListGroup} from 'react-bootstrap'
import { Accordion } from "react-bootstrap";
import AccordionItem from "react-bootstrap/esm/AccordionItem";

function KeywordsList(props) {
    const listKeywords = props.data.map((keyword, index) =>
        <Keyword keyword={keyword} index={index + 1}/>
    );

    return(
        <Accordion>
            <Accordion.Item>
                <Accordion.Header>
                    Hot Keyword
                </Accordion.Header>
            </Accordion.Item>
            {listKeywords}
        </Accordion>
    )
}

export default KeywordsList