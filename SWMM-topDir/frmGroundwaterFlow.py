import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QMainWindow, QComboBox
from ui.frmGenericPropertyEditorDesigner import Ui_frmGenericPropertyEditor
from ui.SWMM.frmGroundwaterFlowDesigner import Ui_frmGroundwaterFlow
from ui.property_editor_backend import PropertyEditorBackend
from ui.text_plus_button import TextPlusButton
from ui.help import HelpHandler
from ui.SWMM.frmGroundwaterEquation import frmGroundwaterEquation
from ui.SWMM.frmGroundwaterEquationDeep import frmGroundwaterEquationDeep
from core.swmm.hydrology.subcatchment import GroundwaterFlowType


class frmGroundwaterFlow(QMainWindow, Ui_frmGroundwaterFlow):
    def __init__(self, main_form, edit_these, new_item, title):
        QMainWindow.__init__(self, main_form)
        self.helper = HelpHandler(self)
        self.help_topic = "swmm/src/src/groundwaterfloweditordialog.htm"
        self._main_form = main_form
        self.project = main_form.project
        self.new_item = new_item
        self.refresh_column = -1
        self.setupUi(self)
        self.setWindowTitle(title)
        self.cmdOK.clicked.connect(self.cmdOK_Clicked)
        self.cmdCancel.clicked.connect(self.cmdCancel_Clicked)
        self.backend = PropertyEditorBackend(self.tblGeneric, self.lblNotes, main_form, edit_these, new_item)

        for column in range(0, self.tblGeneric.columnCount()):
            # for aquifers, show available aquifers
            aquifer_section = main_form.project.find_section("AQUIFERS")
            aquifer_list = aquifer_section.value[0:]
            combobox = QComboBox()
            combobox.addItem('')
            selected_index = 0
            for value in aquifer_list:
                combobox.addItem(value.name)
                if edit_these[column].aquifer == value.name:
                    selected_index = int(combobox.count())-1
            combobox.setCurrentIndex(selected_index)
            self.tblGeneric.setCellWidget(1, column, combobox)
            # also set special text plus button cells
            self.set_lateral_equation(column)
            self.set_deep_equation(column)

        if (main_form.program_settings.value("Geometry/" + "frmGroundwaterFlow_geometry")
                and main_form.program_settings.value("Geometry/" + "frmGroundwaterFlow_state")):
            self.restoreGeometry(main_form.program_settings.value("Geometry/" + "frmGroundwaterFlow_geometry",
                                                                  self.geometry(), type=QtCore.QByteArray))
            self.restoreState(main_form.program_settings.value("Geometry/" + "frmGroundwaterFlow_state",
                                                               self.windowState(), type=QtCore.QByteArray))

        self.installEventFilter(self)

    def eventFilter(self, ui_object, event):
        if event.type() == QtCore.QEvent.WindowUnblocked:
            if self.refresh_column > -1:
                self.set_lateral_equation(self.refresh_column)
                self.set_deep_equation(self.refresh_column)
                self.refresh_column = -1
        return False

    def set_lateral_equation(self, column):
        # text plus button for custom lateral equation
        tb = TextPlusButton(self)
        tb.textbox.setText('NO')
        gwf_section = self.project.gwf
        gwf_list = gwf_section.value[0:]
        for value in gwf_list:
            if (value.subcatchment_name == str(self.tblGeneric.item(0, column).text()) and
                    len(value.custom_equation) > 0 and
                    value.groundwater_flow_type == GroundwaterFlowType.LATERAL):
                tb.textbox.setText('YES')
        tb.textbox.setEnabled(False)
        tb.column = column
        tb.button.clicked.connect(self.make_show_lateral(column))
        self.tblGeneric.setCellWidget(14, column, tb)

    def set_deep_equation(self, column):
        # text plus button for custom deep equation
        tb = TextPlusButton(self)
        tb.textbox.setText('NO')
        gwf_section = self.project.gwf
        gwf_list = gwf_section.value[0:]
        for value in gwf_list:
            if (value.subcatchment_name == str(self.tblGeneric.item(0, column).text()) and
                    len(value.custom_equation) > 0 and
                    value.groundwater_flow_type == GroundwaterFlowType.DEEP):
                tb.textbox.setText('YES')
        tb.textbox.setEnabled(False)
        tb.column = column
        tb.button.clicked.connect(self.make_show_deep(column))
        self.tblGeneric.setCellWidget(15, column, tb)

    def make_show_lateral(self, column):
        def local_show():
            editor = frmGroundwaterEquation(self._main_form, str(self.tblGeneric.item(0, column).text()))
            editor.setWindowModality(QtCore.Qt.ApplicationModal)
            editor.show()
            self.refresh_column = column
        return local_show

    def make_show_deep(self, column):
        def local_show():
            editor = frmGroundwaterEquationDeep(self._main_form, str(self.tblGeneric.item(0, column).text()))
            editor.setWindowModality(QtCore.Qt.ApplicationModal)
            editor.show()
            self.refresh_column = column
        return local_show

    def cmdOK_Clicked(self):
        if self.new_item:
            self.project.groundwater.value.append(self.new_item)
        self.backend.new_item = None
        self.backend.apply_edits()

        self._main_form.program_settings.setValue("Geometry/" + "frmGroundwaterFlow_geometry", self.saveGeometry())
        self._main_form.program_settings.setValue("Geometry/" + "frmGroundwaterFlow_state", self.saveState())
        self.close()

    def cmdCancel_Clicked(self):
        self.close()

