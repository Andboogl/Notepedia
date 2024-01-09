"""Requests to articles database"""


class Requests:
    """Requests to articles database"""
    DATA_TABLE_CREATION = 'CREATE TABLE IF NOT EXISTS '\
        'data(title PRIMARY KEY, content, creation_time)'
    ARTICLE_ADDITION = 'INSERT INTO data VALUES(?, ?, ?)'
    ARTICLE_TITLE_UPDATION = 'UPDATE data SET title == ? WHERE title == ?'
    ARTICLE_CONTENT_UPDATION = 'UPDATE data SET content == ? WHERE title == ?'
    ARTICLE_DELETION = 'DELETE FROM data WHERE title == ?'
    GET_ALL_ARTICLES = 'SELECT * FROM data'
    GET_ARTICLE = 'SELECT * FROM data WHERE title == ?'
