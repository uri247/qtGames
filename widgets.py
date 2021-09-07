import logging
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtWidgets import (
    QApplication, QDialog, QComboBox, QLabel, QCheckBox, QGroupBox, QRadioButton,
    QStyleFactory,
    QVBoxLayout, QGridLayout, QHBoxLayout
)


class Gallery(QDialog):
    top_left_groupbox: QGroupBox

    def __init__(self, parent=None):
        super().__init__(parent)

        self.originalPalette = QApplication.palette()

        # top
        style_label = QLabel('&Style:')
        style_combobox = QComboBox()
        style_combobox.addItems(QStyleFactory.keys())
        style_label.setBuddy(style_combobox)
        self.use_style_palette_checkbox = QCheckBox('&Use style\'s standard palette')
        self.use_style_palette_checkbox.setChecked(True)
        self.disable_widgets_checkbox = QCheckBox('&Disable widgets')

        top_layout = QHBoxLayout()
        top_layout.addWidget(style_label)
        top_layout.addWidget(style_combobox)
        top_layout.addStretch(1)
        top_layout.addWidget(self.use_style_palette_checkbox)
        top_layout.addWidget(self.disable_widgets_checkbox)

        # top left
        self.create_top_left_groupbox()

        # main
        main_layout = QGridLayout()
        main_layout.addLayout(top_layout, 0, 0, 1, 2)
        main_layout.addWidget(self.top_left_groupbox, 1, 0)
        self.setLayout(main_layout)

        self.setWindowTitle('Styles')
        self.change_style('Windows')

    def change_style(self, style_name):
        QApplication.setStyle(style_name)
        self.change_palette()

    def change_palette(self):
        if self.use_style_palette_checkbox.isChecked():
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def create_top_left_groupbox(self):
        self.top_left_groupbox = QGroupBox('Group 1')
        radio1 = QRadioButton('Radio button 1')
        radio2 = QRadioButton('Radio button 2')
        radio3 = QRadioButton('Radon button 3')
        radio1.setChecked(True)

        checkbox = QCheckBox('Tri-state check box')
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.CheckState.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)
        layout.addStretch(1)
        self.top_left_groupbox.setLayout(layout)


def main():
    import sys
    app = QApplication(sys.argv)
    gallery = Gallery()
    gallery.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
