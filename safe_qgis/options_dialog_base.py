# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog_base.ui'
#
# Created: Thu Nov 29 14:42:45 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OptionsDialogBase(object):
    def setupUi(self, OptionsDialogBase):
        OptionsDialogBase.setObjectName(_fromUtf8("OptionsDialogBase"))
        OptionsDialogBase.resize(501, 257)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptionsDialogBase.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(OptionsDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(OptionsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(OptionsDialogBase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 468, 764))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 14, 0, 1, 1)
        self.grpNotImplemented = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.grpNotImplemented.setObjectName(_fromUtf8("grpNotImplemented"))
        self.gridLayout_3 = QtGui.QGridLayout(self.grpNotImplemented)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.cbxBubbleLayersUp = QtGui.QCheckBox(self.grpNotImplemented)
        self.cbxBubbleLayersUp.setEnabled(True)
        self.cbxBubbleLayersUp.setObjectName(_fromUtf8("cbxBubbleLayersUp"))
        self.gridLayout_3.addWidget(self.cbxBubbleLayersUp, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.grpNotImplemented)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton.setEnabled(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.grpNotImplemented)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_2 = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton_2.setEnabled(True)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.grpNotImplemented)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.toolButton_3 = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton_3.setEnabled(True)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.grpNotImplemented)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.toolButton_4 = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton_4.setEnabled(True)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.grpNotImplemented)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox = QtGui.QSpinBox(self.grpNotImplemented)
        self.spinBox.setEnabled(True)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)
        self.gridLayout_2.addWidget(self.grpNotImplemented, 12, 0, 1, 1)
        self.cbxVisibleLayersOnly = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxVisibleLayersOnly.setObjectName(_fromUtf8("cbxVisibleLayersOnly"))
        self.gridLayout_2.addWidget(self.cbxVisibleLayersOnly, 0, 0, 1, 1)
        self.cbxSetLayerNameFromTitle = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxSetLayerNameFromTitle.setEnabled(True)
        self.cbxSetLayerNameFromTitle.setObjectName(_fromUtf8("cbxSetLayerNameFromTitle"))
        self.gridLayout_2.addWidget(self.cbxSetLayerNameFromTitle, 1, 0, 1, 1)
        self.cbxZoomToImpact = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxZoomToImpact.setEnabled(True)
        self.cbxZoomToImpact.setObjectName(_fromUtf8("cbxZoomToImpact"))
        self.gridLayout_2.addWidget(self.cbxZoomToImpact, 2, 0, 1, 1)
        self.lblKeywordCache = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblKeywordCache.setEnabled(True)
        self.lblKeywordCache.setObjectName(_fromUtf8("lblKeywordCache"))
        self.gridLayout_2.addWidget(self.lblKeywordCache, 9, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.leKeywordCachePath = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leKeywordCachePath.setEnabled(True)
        self.leKeywordCachePath.setObjectName(_fromUtf8("leKeywordCachePath"))
        self.horizontalLayout_6.addWidget(self.leKeywordCachePath)
        self.toolKeywordCachePath = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolKeywordCachePath.setEnabled(True)
        self.toolKeywordCachePath.setObjectName(_fromUtf8("toolKeywordCachePath"))
        self.horizontalLayout_6.addWidget(self.toolKeywordCachePath)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 11, 0, 1, 1)
        self.cbxUseThread = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxUseThread.setObjectName(_fromUtf8("cbxUseThread"))
        self.gridLayout_2.addWidget(self.cbxUseThread, 13, 0, 1, 1)
        self.cbxHideExposure = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxHideExposure.setEnabled(True)
        self.cbxHideExposure.setObjectName(_fromUtf8("cbxHideExposure"))
        self.gridLayout_2.addWidget(self.cbxHideExposure, 3, 0, 1, 1)
        self.cbxClipToViewport = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxClipToViewport.setChecked(False)
        self.cbxClipToViewport.setObjectName(_fromUtf8("cbxClipToViewport"))
        self.gridLayout_2.addWidget(self.cbxClipToViewport, 4, 0, 1, 1)
        self.cbxShowPostprocessingLayers = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxShowPostprocessingLayers.setObjectName(_fromUtf8("cbxShowPostprocessingLayers"))
        self.gridLayout_2.addWidget(self.cbxShowPostprocessingLayers, 6, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.dsbFemaleRatioDefault = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.dsbFemaleRatioDefault.setAccelerated(True)
        self.dsbFemaleRatioDefault.setMaximum(1.0)
        self.dsbFemaleRatioDefault.setSingleStep(0.01)
        self.dsbFemaleRatioDefault.setObjectName(_fromUtf8("dsbFemaleRatioDefault"))
        self.horizontalLayout_7.addWidget(self.dsbFemaleRatioDefault)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)
        self.cbxClipHard = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxClipHard.setObjectName(_fromUtf8("cbxClipHard"))
        self.gridLayout_2.addWidget(self.cbxClipHard, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(OptionsDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OptionsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OptionsDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialogBase)
        OptionsDialogBase.setTabOrder(self.cbxVisibleLayersOnly, self.cbxSetLayerNameFromTitle)
        OptionsDialogBase.setTabOrder(self.cbxSetLayerNameFromTitle, self.lineEdit)
        OptionsDialogBase.setTabOrder(self.lineEdit, self.toolButton)
        OptionsDialogBase.setTabOrder(self.toolButton, self.lineEdit_2)
        OptionsDialogBase.setTabOrder(self.lineEdit_2, self.toolButton_2)
        OptionsDialogBase.setTabOrder(self.toolButton_2, self.lineEdit_3)
        OptionsDialogBase.setTabOrder(self.lineEdit_3, self.toolButton_3)
        OptionsDialogBase.setTabOrder(self.toolButton_3, self.lineEdit_4)
        OptionsDialogBase.setTabOrder(self.lineEdit_4, self.toolButton_4)
        OptionsDialogBase.setTabOrder(self.toolButton_4, self.spinBox)
        OptionsDialogBase.setTabOrder(self.spinBox, self.cbxUseThread)
        OptionsDialogBase.setTabOrder(self.cbxUseThread, self.buttonBox)
        OptionsDialogBase.setTabOrder(self.buttonBox, self.scrollArea)

    def retranslateUi(self, OptionsDialogBase):
        OptionsDialogBase.setWindowTitle(QtGui.QApplication.translate("OptionsDialogBase", "InaSAFE - Options", None, QtGui.QApplication.UnicodeUTF8))
        self.grpNotImplemented.setTitle(QtGui.QApplication.translate("OptionsDialogBase", "Not yet implemented", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxBubbleLayersUp.setText(QtGui.QApplication.translate("OptionsDialogBase", "Bubble exposure and hazard layers to top when selected", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OptionsDialogBase", "Location for results", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("OptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OptionsDialogBase", "Report template", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("OptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OptionsDialogBase", "Logo for maps (must be x x y) ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("OptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OptionsDialogBase", "Organisation name (for maps, reports etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("OptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OptionsDialogBase", "DPI (Maps and reports)", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxVisibleLayersOnly.setText(QtGui.QApplication.translate("OptionsDialogBase", "Only show visible layers in InaSAFE dock", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSetLayerNameFromTitle.setText(QtGui.QApplication.translate("OptionsDialogBase", "Set QGIS layer name from \'title\' in keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxZoomToImpact.setText(QtGui.QApplication.translate("OptionsDialogBase", "Zoom to impact layer on scenario estimate completion", None, QtGui.QApplication.UnicodeUTF8))
        self.lblKeywordCache.setText(QtGui.QApplication.translate("OptionsDialogBase", "Keyword cache for remote datasources", None, QtGui.QApplication.UnicodeUTF8))
        self.toolKeywordCachePath.setText(QtGui.QApplication.translate("OptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxUseThread.setText(QtGui.QApplication.translate("OptionsDialogBase", "Run analysis in a separate thread (experimental)", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxHideExposure.setText(QtGui.QApplication.translate("OptionsDialogBase", "Hide exposure layer on scenario estimate completion", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxClipToViewport.setToolTip(QtGui.QApplication.translate("OptionsDialogBase", "Turn on to clip hazard and exposure layers to the currently  visible extent on the map canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxClipToViewport.setText(QtGui.QApplication.translate("OptionsDialogBase", "Clip datasets to visible extent before analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxShowPostprocessingLayers.setToolTip(QtGui.QApplication.translate("OptionsDialogBase", "Turn on to see the intermediate files generated by the postprocessing steps in the map canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxShowPostprocessingLayers.setText(QtGui.QApplication.translate("OptionsDialogBase", "Show intermediate layers generated by postprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OptionsDialogBase", "Female ratio default value", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxClipHard.setText(QtGui.QApplication.translate("OptionsDialogBase", "When clipping, also clip features (e.g. will clip polygon smaller)", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
