"""Application main window"""


from PyQt6.QtWidgets import QMainWindow
from design import MainWindowDesign
from .article_creation import ArticleCreationWindow
from .articles_view import ArticlesViewWindow


class MainWindow(QMainWindow):
    """Main window"""
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.__article_creation_window = ArticleCreationWindow(self)

        self.__design = MainWindowDesign()
        self.__design.setupUi(self)
        self.setFixedSize(798, 239)

        # Buttons handling
        self.__design.create_article.clicked.connect(self.create_article)
        self.__design.look_for_articles.clicked.connect(self.view_articles)

    def view_articles(self) -> None:
        """Open articles view window"""
        self.close()
        self.__articles_view_window = ArticlesViewWindow(self, self.__article_creation_window)
        self.__articles_view_window.show()

    def create_article(self) -> None:
        """Open article creation window"""
        self.close()
        self.__article_creation_window.show()
