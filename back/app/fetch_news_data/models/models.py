from database_config import Base
import sqlalchemy as sa


class Article(Base):
    __tablename__ = "articles"
    article_id = sa.Column("article_id",
                      sa.Integer,
                      primary_key=True,
                      autoincrement=True)
    title = sa.Column("title",
                      sa.Text,
                      nullable=False)
    ranking = sa.Column("ranking",
                      sa.Integer,
                      nullable=False)
    keywords = sa.Column("keywords",
                      sa.Text,
                      nullable=False)
    referenced_site = sa.Column("referenced_site",
                      sa.Text,
                      nullable=False)
    content = sa.Column("content",
                      sa.Text,
                      nullable=False)
    created_date = sa.Column("created_date",
                      sa.Date,
                      nullable=False)