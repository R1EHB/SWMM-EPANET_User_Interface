# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui-py3qt5\src\ui\SWMM\frmReportOptionsDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmReportOptions(object):
    def setupUi(self, frmReportOptions):
        frmReportOptions.setObjectName("frmReportOptions")
        frmReportOptions.resize(578, 364)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmReportOptions.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmReportOptions)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbxReport = QtWidgets.QGroupBox(self.centralWidget)
        self.gbxReport.setObjectName("gbxReport")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbxReport)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbxInput = QtWidgets.QCheckBox(self.gbxReport)
        self.cbxInput.setObjectName("cbxInput")
        self.horizontalLayout.addWidget(self.cbxInput)
        self.cbxContinuity = QtWidgets.QCheckBox(self.gbxReport)
        self.cbxContinuity.setObjectName("cbxContinuity")
        self.horizontalLayout.addWidget(self.cbxContinuity)
        self.cbxFlow = QtWidgets.QCheckBox(self.gbxReport)
        self.cbxFlow.setObjectName("cbxFlow")
        self.horizontalLayout.addWidget(self.cbxFlow)
        self.cbxAverage = QtWidgets.QCheckBox(self.gbxReport)
        self.cbxAverage.setObjectName("cbxAverage")
        self.horizontalLayout.addWidget(self.cbxAverage)
        self.cbxControls = QtWidgets.QCheckBox(self.gbxReport)
        self.cbxControls.setObjectName("cbxControls")
        self.horizontalLayout.addWidget(self.cbxControls)
        self.verticalLayout.addWidget(self.gbxReport)
        self.fraObjects = QtWidgets.QFrame(self.centralWidget)
        self.fraObjects.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraObjects.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraObjects.setObjectName("fraObjects")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fraObjects)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gbxNode = QtWidgets.QGroupBox(self.fraObjects)
        self.gbxNode.setObjectName("gbxNode")
        self.gridLayout = QtWidgets.QGridLayout(self.gbxNode)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.gbxNode)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)
        self.cmdNodeAll = QtWidgets.QPushButton(self.gbxNode)
        self.cmdNodeAll.setObjectName("cmdNodeAll")
        self.gridLayout.addWidget(self.cmdNodeAll, 1, 0, 1, 1)
        self.cmdNodeNone = QtWidgets.QPushButton(self.gbxNode)
        self.cmdNodeNone.setObjectName("cmdNodeNone")
        self.gridLayout.addWidget(self.cmdNodeNone, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gbxNode)
        self.gbxLinks = QtWidgets.QGroupBox(self.fraObjects)
        self.gbxLinks.setObjectName("gbxLinks")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbxLinks)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.gbxLinks)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.listWidget_2, 0, 0, 1, 2)
        self.cmdLinksAll = QtWidgets.QPushButton(self.gbxLinks)
        self.cmdLinksAll.setObjectName("cmdLinksAll")
        self.gridLayout_2.addWidget(self.cmdLinksAll, 1, 0, 1, 1)
        self.cmdLinksNone = QtWidgets.QPushButton(self.gbxLinks)
        self.cmdLinksNone.setObjectName("cmdLinksNone")
        self.gridLayout_2.addWidget(self.cmdLinksNone, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gbxLinks)
        self.gbxSubcatchments = QtWidgets.QGroupBox(self.fraObjects)
        self.gbxSubcatchments.setObjectName("gbxSubcatchments")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbxSubcatchments)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.gbxSubcatchments)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_3.addWidget(self.listWidget_3, 0, 0, 1, 2)
        self.cmdSubcatchmentsAll = QtWidgets.QPushButton(self.gbxSubcatchments)
        self.cmdSubcatchmentsAll.setObjectName("cmdSubcatchmentsAll")
        self.gridLayout_3.addWidget(self.cmdSubcatchmentsAll, 1, 0, 1, 1)
        self.cmdSubcatchmentsNone = QtWidgets.QPushButton(self.gbxSubcatchments)
        self.cmdSubcatchmentsNone.setObjectName("cmdSubcatchmentsNone")
        self.gridLayout_3.addWidget(self.cmdSubcatchmentsNone, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gbxSubcatchments)
        self.verticalLayout.addWidget(self.fraObjects)
        self.fraButtons = QtWidgets.QFrame(self.centralWidget)
        self.fraButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraButtons.setObjectName("fraButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraButtons)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(375, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.fraButtons)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout_2.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraButtons)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout_2.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraButtons)
        frmReportOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmReportOptions)
        QtCore.QMetaObject.connectSlotsByName(frmReportOptions)
        frmReportOptions.setTabOrder(self.cbxInput, self.cbxContinuity)
        frmReportOptions.setTabOrder(self.cbxContinuity, self.cbxFlow)
        frmReportOptions.setTabOrder(self.cbxFlow, self.cbxControls)
        frmReportOptions.setTabOrder(self.cbxControls, self.listWidget)
        frmReportOptions.setTabOrder(self.listWidget, self.cmdNodeAll)
        frmReportOptions.setTabOrder(self.cmdNodeAll, self.cmdNodeNone)
        frmReportOptions.setTabOrder(self.cmdNodeNone, self.listWidget_2)
        frmReportOptions.setTabOrder(self.listWidget_2, self.cmdLinksAll)
        frmReportOptions.setTabOrder(self.cmdLinksAll, self.cmdLinksNone)
        frmReportOptions.setTabOrder(self.cmdLinksNone, self.listWidget_3)
        frmReportOptions.setTabOrder(self.listWidget_3, self.cmdSubcatchmentsAll)
        frmReportOptions.setTabOrder(self.cmdSubcatchmentsAll, self.cmdSubcatchmentsNone)
        frmReportOptions.setTabOrder(self.cmdSubcatchmentsNone, self.cmdOK)
        frmReportOptions.setTabOrder(self.cmdOK, self.cmdCancel)

    def retranslateUi(self, frmReportOptions):
        _translate = QtCore.QCoreApplication.translate
        frmReportOptions.setWindowTitle(_translate("frmReportOptions", "SWMM Report Options"))
        self.gbxReport.setTitle(_translate("frmReportOptions", "Report Options"))
        self.cbxInput.setText(_translate("frmReportOptions", "Input Summary"))
        self.cbxContinuity.setText(_translate("frmReportOptions", "Continuity Checks"))
        self.cbxFlow.setText(_translate("frmReportOptions", "Flow Stats"))
        self.cbxAverage.setText(_translate("frmReportOptions", "Average Results"))
        self.cbxControls.setText(_translate("frmReportOptions", "Controls"))
        self.gbxNode.setTitle(_translate("frmReportOptions", "Nodes"))
        self.cmdNodeAll.setText(_translate("frmReportOptions", "All"))
        self.cmdNodeNone.setText(_translate("frmReportOptions", "None"))
        self.gbxLinks.setTitle(_translate("frmReportOptions", "Links"))
        self.cmdLinksAll.setText(_translate("frmReportOptions", "All"))
        self.cmdLinksNone.setText(_translate("frmReportOptions", "None"))
        self.gbxSubcatchments.setTitle(_translate("frmReportOptions", "Subcatchments"))
        self.cmdSubcatchmentsAll.setText(_translate("frmReportOptions", "All"))
        self.cmdSubcatchmentsNone.setText(_translate("frmReportOptions", "None"))
        self.cmdOK.setText(_translate("frmReportOptions", "OK"))
        self.cmdCancel.setText(_translate("frmReportOptions", "Cancel"))
