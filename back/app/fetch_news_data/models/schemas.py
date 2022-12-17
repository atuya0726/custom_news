from pydantic import BaseModel


class UserBase(BaseModel):
    article_id: str
    title: str
    ranking: int
    keywords: str
    referenced_site: str
    content: str
    created_date: str

    class Config:
        orm_mode = True