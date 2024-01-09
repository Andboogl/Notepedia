"""Articles view window"""


from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import QFont
from design import ArticlesViewWindowDesign
from database import ArticlesDatabase
from .edit_article import EditArticleWindow


class ArticlesViewWindow(QMainWindow):
    """Articles view window"""
    def __init__(self, main_window: QMainWindow,
                 article_creation_window: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.__articles_database = ArticlesDatabase()
        self.__article_creation_window = article_creation_window
        self.__main_window = main_window

        self.__design = ArticlesViewWindowDesign()
        self.__design.setupUi(self)
        self.articles = self.__design.articles

        self.setFixedSize(797, 506)
        self.load_articles_to_articles_list()

        # Button pressing
        self.__design.search.clicked.connect(self.search)
        self.__design.show_all_articles.clicked.connect(
            self.load_articles_to_articles_list)
        self.__design.main_menu.clicked.connect(self.open_main_window)
        self.__design.open_article.clicked.connect(self.open_article)

    def open_article(self) -> None:
        """Open selected article"""
        selected_article = self.__design.articles.currentItem()

        if selected_article:
            self.close()
            self.__edit_article_window = EditArticleWindow(
                selected_article.text(), self.__main_window, self.__article_creation_window, self)
            self.__edit_article_window.show()

    def open_main_window(self) -> None:
        """Open main window"""
        self.close()
        self.__main_window.show()

    def search(self) -> None:
        """Search articles"""
        search_request = self.__design.search_request.text()

        if search_request.strip():
            self.load_articles_to_articles_list(search_request)

    def load_articles_to_articles_list(self, request: str = None) -> None:
        """Load articles to articles list"""
        self.__design.articles.clear()

        if request:
            articles = self.__articles_database.search(request)

        else:
            articles = self.__articles_database.get_articles()

        item_font = QFont()
        item_font.setBold(True)
        item_font.setPointSize(20)

        for article in articles:
            article_title = article[0]
            item = QListWidgetItem(self.__design.articles)
            item.setFont(item_font)
            item.setText(article_title)
            self.__design.articles.addItem(item)
