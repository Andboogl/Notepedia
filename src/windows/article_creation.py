"""Article creation window"""


from sqlite3 import IntegrityError
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from design import ArticleCreationWindowDesign
from database import ArticlesDatabase
from .edit_article import EditArticleWindow
from .articles_view import ArticlesViewWindow


class ArticleCreationWindow(QMainWindow):
    """Article creation window"""
    def __init__(self, main_window: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.__articles_db = ArticlesDatabase()
        self.__main_window = main_window

        self.__design = ArticleCreationWindowDesign()
        self.__design.setupUi(self)

        self.setFixedSize(805, 301)

        # Buttons handling
        self.__design.back.clicked.connect(self.back)
        self.__design.create_article.clicked.connect(self.create_article)

    def back(self) -> None:
        """Back to main window"""
        self.close()
        self.__main_window.show()

    def create_article(self) -> None:
        """Create new article"""
        title = self.__design.article_title.text()

        if title.strip():
            try:
                self.__articles_db.add_article(title, '')
                self.close()
                self.__edit_article_window = EditArticleWindow(
                    title, self.__main_window,
                    self, ArticlesViewWindow(self.__main_window, self))
                self.__edit_article_window.show()

            # If article with this name is already exists
            except IntegrityError:
                QMessageBox(
                    QMessageBox.Icon.Information,
                    'Не вдалося створити статью',
                    'Статья с таким імʼям вже існує').exec()

        # If user hasn't writen article name
        else:
            QMessageBox(
                QMessageBox.Icon.Information,
                'Введіть всі данні',
                'Введіть всі данні для створення статії').exec()

