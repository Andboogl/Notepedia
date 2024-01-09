"""Edit article window"""


from sqlite3 import IntegrityError
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from design import EditArticleWindowDesign
from database import ArticlesDatabase


class EditArticleWindow(QMainWindow):
    """Edit article window"""
    def __init__(self,
                 title, main_window: QMainWindow,
                 article_creation_window: QMainWindow,
                 articles_view_window: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.__articles_database = ArticlesDatabase()
        self.__title = title
        self.__main_window = main_window

        # Windows
        self.__article_creation_window = article_creation_window
        self.__articles_view_window = articles_view_window

        self.__design = EditArticleWindowDesign()
        self.__design.setupUi(self)

        self.setFixedSize(919, 536)

        # Loading article
        self.__design.article_title.setText(title)
        self.__design.content.setPlainText(
            self.__articles_database.get_article(title)[1])

        # Button pressing
        self.__design.save_article.clicked.connect(self.save_changes)
        self.__design.delete_article.clicked.connect(self.delete_article)
        self.__design.create_new_article.clicked.connect(self.create_new_article)
        self.__design.view_other_articles.clicked.connect(self.view_other_articles)

    def delete_article(self) -> None:
        """Delete article"""
        msg = QMessageBox.question(
            self, 'Видалити статью?',
            'Чи точно ви хочете видалити цю статью? '\
            'Ви більше НІКОЛИ не зможете її відновити після видалення!',)

        if msg == QMessageBox.StandardButton.Yes:
            self.__articles_database.delete_article(self.__title)

            self.close()

            self.__articles_view_window.load_articles_to_articles_list()

            self.__main_window.show()

    def save_changes_on_close(self) -> None:
        """Save changes on window close?"""
        article_title = self.__design.article_title.text()
        article_content = self.__design.content.toPlainText()

        # If user has unsaved changes
        if article_title != self.__articles_database.get_article(self.__title)[0]\
            or article_content != self.__articles_database.get_article(self.__title)[1]:
            msg = QMessageBox(self)
            msg.setText(
                'У вас є незбережені зміни. Чи хочете'\
                    'ви зберегти їх перед вихідом?')
            msg.addButton(QMessageBox.StandardButton.Cancel)
            msg.addButton(QMessageBox.StandardButton.No)
            msg.addButton(QMessageBox.StandardButton.Yes)
            msg.setDefaultButton(QMessageBox.StandardButton.Yes)
            msg.exec()

            clicked_button = msg.clickedButton().text()
            print(clicked_button)

            if clicked_button == 'Cancel':
                return 'Cancel!'

            elif clicked_button == '&Yes':
                self.save_changes()

    def view_other_articles(self) -> None:
        """Open articles view window"""
        if not self.save_changes_on_close():
            self.close()
            self.__articles_view_window.show()

    def create_new_article(self) -> None:
        """Open new article creation window"""
        if not self.save_changes_on_close():
            self.close()
            self.__article_creation_window.show()

    def save_changes(self) -> None:
        """Save user changes to article"""
        new_article_title = self.__design.article_title.text()
        new_article_content = self.__design.content.toPlainText()

        if new_article_title.strip():
            try:
                self.__articles_database.update_article(
                    self.__title, new_article_title, None)
                self.__title = new_article_title

            # If article with this name is already exists
            except IntegrityError:
                QMessageBox(
                    QMessageBox.Icon.Information,
                    'Статья з таким заголовком вже існує',
                    'Статья з таким заголовком вже існує').exec()

        else:
            QMessageBox(
                QMessageBox.Icon.Information,
                'Введіть новий заголовок',
                'Введіть новий заголовок').exec()

        # Content updation
        self.__articles_database.update_article(
            self.__title, None, new_article_content)

        self.__articles_view_window.load_articles_to_articles_list()
