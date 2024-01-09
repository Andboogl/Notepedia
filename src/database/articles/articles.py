"""Articles database"""


import os
import sqlite3
from datetime import datetime
from .__requests import Requests
from ..__config import ARTICLES_DATABASE, DATABASE_FOLDER


class ArticlesDatabase:
    """Articles database"""
    def __init__(self) -> None:
        if not os.path.exists(DATABASE_FOLDER):
            os.mkdir(DATABASE_FOLDER)

        self.__db = sqlite3.connect(ARTICLES_DATABASE)
        self.__db.execute(Requests.DATA_TABLE_CREATION)

    def add_article(self, title: str, content: str) -> None:
        """Add article"""
        creation_time = datetime.now()
        data = (title, content, creation_time)
        self.__db.execute(Requests.ARTICLE_ADDITION, data)
        self.__db.commit()

    def update_article(self,
                       old_title: str,
                       new_title: str,
                       new_content: str) -> None:
        """Updata article"""
        data = ((new_title, old_title), (new_content, old_title))

        if new_title:
            self.__db.execute(Requests.ARTICLE_TITLE_UPDATION, data[0])

        if new_content:
            self.__db.execute(Requests.ARTICLE_CONTENT_UPDATION, data[1])

        self.__db.commit()

    def delete_article(self, title: str) -> None:
        """Delete article"""
        data = (title,)
        self.__db.execute(Requests.ARTICLE_DELETION, data)
        self.__db.commit()

    def get_articles(self) -> tuple:
        """Get list of articles"""
        return self.__db.execute(
            Requests.GET_ALL_ARTICLES).fetchall()

    def get_article(self, title: str) -> tuple:
        """Get article by its title"""
        data = (title,)
        return self.__db.execute(Requests.GET_ARTICLE, data).fetchone()

    def search(self, request: str) -> list:
        """Search article"""
        articles = self.get_articles()
        founded = []

        for article in articles:
            if request.lower() in article[0].lower():
                founded.append(article)

        return founded
