from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QSplitter, QTextEdit, QTreeView, QVBoxLayout, QWidget
import qdarktheme
import sys

class MdEditor(QDialog):
    def __init__(self, parent=None):
        super(MdEditor, self).__init__(parent)
        # Theme
        qdarktheme.setup_theme()

        # Widgets
        editor = QTextEdit()
        tree = QTreeView()
        self.tree = tree

        search_list = QListWidget()
        self.search_list = search_list
        search_list_itemA = QListWidgetItem("A", search_list)
        search_list_itemB = QListWidgetItem("B", search_list)

        splitter = QSplitter()
        splitter.addWidget(search_list)
        splitter.addWidget(tree)
        splitter.addWidget(editor)

        sidebar = QWidget()
        sidebar_tree_button = QPushButton("Tree")
        sidebar_tree_button.clicked.connect(self.open_tree)

        sidebar_search_button = QPushButton("Search")
        sidebar_search_button.clicked.connect(self.open_search)
        self.search_list.setHidden(True)


        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(sidebar_tree_button)
        sidebar_layout.addWidget(sidebar_search_button)

        sidebar.setLayout(sidebar_layout)

        # Layout
        layout = QHBoxLayout()

        layout.addWidget(sidebar)
        layout.addWidget(splitter)

        self.setLayout(layout)

    def open_tree(self):
        self.search_list.setHidden(True)
        self.tree.setHidden(False)

    def open_search(self):
        self.tree.setHidden(True)
        self.search_list.setHidden(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MdEditor()
    form.show()
    sys.exit(app.exec())
