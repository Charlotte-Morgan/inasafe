# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keywords_dialog_base.ui'
#
# Created: Fri Jun  6 16:34:30 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_KeywordsDialogBase(object):
    def setupUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setObjectName(_fromUtf8("KeywordsDialogBase"))
        KeywordsDialogBase.resize(718, 553)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KeywordsDialogBase.sizePolicy().hasHeightForWidth())
        KeywordsDialogBase.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KeywordsDialogBase.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(KeywordsDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblLayerName = QtGui.QLabel(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLayerName.sizePolicy().hasHeightForWidth())
        self.lblLayerName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLayerName.setFont(font)
        self.lblLayerName.setText(_fromUtf8(""))
        self.lblLayerName.setWordWrap(True)
        self.lblLayerName.setObjectName(_fromUtf8("lblLayerName"))
        self.gridLayout.addWidget(self.lblLayerName, 0, 0, 1, 1)
        self.tab_widget = QtGui.QTabWidget(KeywordsDialogBase)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.core_fields_tab = QtGui.QWidget()
        self.core_fields_tab.setObjectName(_fromUtf8("core_fields_tab"))
        self.formLayout = QtGui.QFormLayout(self.core_fields_tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblTitle = QtGui.QLabel(self.core_fields_tab)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblTitle)
        self.leTitle = QtGui.QLineEdit(self.core_fields_tab)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leTitle)
        self.lblCategory = QtGui.QLabel(self.core_fields_tab)
        self.lblCategory.setObjectName(_fromUtf8("lblCategory"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblCategory)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radHazard = QtGui.QRadioButton(self.core_fields_tab)
        self.radHazard.setObjectName(_fromUtf8("radHazard"))
        self.horizontalLayout_3.addWidget(self.radHazard)
        self.radExposure = QtGui.QRadioButton(self.core_fields_tab)
        self.radExposure.setChecked(True)
        self.radExposure.setObjectName(_fromUtf8("radExposure"))
        self.horizontalLayout_3.addWidget(self.radExposure)
        self.radPostprocessing = QtGui.QRadioButton(self.core_fields_tab)
        self.radPostprocessing.setObjectName(_fromUtf8("radPostprocessing"))
        self.horizontalLayout_3.addWidget(self.radPostprocessing)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.lblSubcategory = QtGui.QLabel(self.core_fields_tab)
        self.lblSubcategory.setObjectName(_fromUtf8("lblSubcategory"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblSubcategory)
        self.cboSubcategory = QtGui.QComboBox(self.core_fields_tab)
        self.cboSubcategory.setObjectName(_fromUtf8("cboSubcategory"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboSubcategory)
        self.lblSource = QtGui.QLabel(self.core_fields_tab)
        self.lblSource.setObjectName(_fromUtf8("lblSource"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblSource)
        self.leSource = QtGui.QLineEdit(self.core_fields_tab)
        self.leSource.setDragEnabled(True)
        self.leSource.setObjectName(_fromUtf8("leSource"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.leSource)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(583, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.tab_widget.addTab(self.core_fields_tab, _fromUtf8(""))
        self.aggregation_tab = QtGui.QWidget()
        self.aggregation_tab.setObjectName(_fromUtf8("aggregation_tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.aggregation_tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.aggregation_tab)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 678, 428))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.lblAggregationAttribute = QtGui.QLabel(self.groupBox_3)
        self.lblAggregationAttribute.setEnabled(True)
        self.lblAggregationAttribute.setObjectName(_fromUtf8("lblAggregationAttribute"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblAggregationAttribute)
        self.cboAggregationAttribute = QtGui.QComboBox(self.groupBox_3)
        self.cboAggregationAttribute.setObjectName(_fromUtf8("cboAggregationAttribute"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboAggregationAttribute)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.lblFemaleRatioAttribute = QtGui.QLabel(self.groupBox_2)
        self.lblFemaleRatioAttribute.setObjectName(_fromUtf8("lblFemaleRatioAttribute"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFemaleRatioAttribute)
        self.cboFemaleRatioAttribute = QtGui.QComboBox(self.groupBox_2)
        self.cboFemaleRatioAttribute.setObjectName(_fromUtf8("cboFemaleRatioAttribute"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboFemaleRatioAttribute)
        self.lblFemaleRatioDefault = QtGui.QLabel(self.groupBox_2)
        self.lblFemaleRatioDefault.setObjectName(_fromUtf8("lblFemaleRatioDefault"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblFemaleRatioDefault)
        self.dsbFemaleRatioDefault = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.dsbFemaleRatioDefault.setAccelerated(True)
        self.dsbFemaleRatioDefault.setMaximum(1.0)
        self.dsbFemaleRatioDefault.setSingleStep(0.01)
        self.dsbFemaleRatioDefault.setProperty("value", 0.0)
        self.dsbFemaleRatioDefault.setObjectName(_fromUtf8("dsbFemaleRatioDefault"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbFemaleRatioDefault)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblYouthRatioAttribute = QtGui.QLabel(self.groupBox)
        self.lblYouthRatioAttribute.setObjectName(_fromUtf8("lblYouthRatioAttribute"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblYouthRatioAttribute)
        self.cboYouthRatioAttribute = QtGui.QComboBox(self.groupBox)
        self.cboYouthRatioAttribute.setObjectName(_fromUtf8("cboYouthRatioAttribute"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboYouthRatioAttribute)
        self.lblYouthRatioDefault = QtGui.QLabel(self.groupBox)
        self.lblYouthRatioDefault.setObjectName(_fromUtf8("lblYouthRatioDefault"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblYouthRatioDefault)
        self.dsbYouthRatioDefault = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsbYouthRatioDefault.setMaximum(1.0)
        self.dsbYouthRatioDefault.setSingleStep(0.01)
        self.dsbYouthRatioDefault.setObjectName(_fromUtf8("dsbYouthRatioDefault"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbYouthRatioDefault)
        self.lblAdultRatioAttribute = QtGui.QLabel(self.groupBox)
        self.lblAdultRatioAttribute.setObjectName(_fromUtf8("lblAdultRatioAttribute"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblAdultRatioAttribute)
        self.cboAdultRatioAttribute = QtGui.QComboBox(self.groupBox)
        self.cboAdultRatioAttribute.setObjectName(_fromUtf8("cboAdultRatioAttribute"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboAdultRatioAttribute)
        self.lblAdultRatioDefault = QtGui.QLabel(self.groupBox)
        self.lblAdultRatioDefault.setObjectName(_fromUtf8("lblAdultRatioDefault"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblAdultRatioDefault)
        self.dsbAdultRatioDefault = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsbAdultRatioDefault.setMaximum(1.0)
        self.dsbAdultRatioDefault.setSingleStep(0.01)
        self.dsbAdultRatioDefault.setObjectName(_fromUtf8("dsbAdultRatioDefault"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dsbAdultRatioDefault)
        self.lblElderlyRatioAttribute = QtGui.QLabel(self.groupBox)
        self.lblElderlyRatioAttribute.setObjectName(_fromUtf8("lblElderlyRatioAttribute"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblElderlyRatioAttribute)
        self.cboElderlyRatioAttribute = QtGui.QComboBox(self.groupBox)
        self.cboElderlyRatioAttribute.setObjectName(_fromUtf8("cboElderlyRatioAttribute"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.cboElderlyRatioAttribute)
        self.lblElderlyRatioDefault = QtGui.QLabel(self.groupBox)
        self.lblElderlyRatioDefault.setObjectName(_fromUtf8("lblElderlyRatioDefault"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.lblElderlyRatioDefault)
        self.dsbElderlyRatioDefault = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsbElderlyRatioDefault.setMaximum(1.0)
        self.dsbElderlyRatioDefault.setSingleStep(0.01)
        self.dsbElderlyRatioDefault.setObjectName(_fromUtf8("dsbElderlyRatioDefault"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.dsbElderlyRatioDefault)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tab_widget.addTab(self.aggregation_tab, _fromUtf8(""))
        self.advanced_tab = QtGui.QWidget()
        self.advanced_tab.setObjectName(_fromUtf8("advanced_tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.advanced_tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radPredefined = QtGui.QRadioButton(self.advanced_tab)
        self.radPredefined.setObjectName(_fromUtf8("radPredefined"))
        self.horizontalLayout_4.addWidget(self.radPredefined)
        self.radUserDefined = QtGui.QRadioButton(self.advanced_tab)
        self.radUserDefined.setObjectName(_fromUtf8("radUserDefined"))
        self.horizontalLayout_4.addWidget(self.radUserDefined)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.framePredefined = QtGui.QFrame(self.advanced_tab)
        self.framePredefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePredefined.setFrameShadow(QtGui.QFrame.Raised)
        self.framePredefined.setObjectName(_fromUtf8("framePredefined"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.framePredefined)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.framePredefined)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.cboKeyword = QtGui.QComboBox(self.framePredefined)
        self.cboKeyword.setObjectName(_fromUtf8("cboKeyword"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(0, _fromUtf8("subcategory"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(1, _fromUtf8("unit"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(2, _fromUtf8("datatype"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(3, _fromUtf8("key_attribute"))
        self.horizontalLayout.addWidget(self.cboKeyword)
        self.label_5 = QtGui.QLabel(self.framePredefined)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lePredefinedValue = QtGui.QLineEdit(self.framePredefined)
        self.lePredefinedValue.setObjectName(_fromUtf8("lePredefinedValue"))
        self.horizontalLayout.addWidget(self.lePredefinedValue)
        self.pbnAddToList1 = QtGui.QPushButton(self.framePredefined)
        self.pbnAddToList1.setObjectName(_fromUtf8("pbnAddToList1"))
        self.horizontalLayout.addWidget(self.pbnAddToList1)
        self.gridLayout_4.addWidget(self.framePredefined, 1, 0, 1, 1)
        self.frameUserDefined = QtGui.QFrame(self.advanced_tab)
        self.frameUserDefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameUserDefined.setFrameShadow(QtGui.QFrame.Raised)
        self.frameUserDefined.setObjectName(_fromUtf8("frameUserDefined"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameUserDefined)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.frameUserDefined)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.leKey = QtGui.QLineEdit(self.frameUserDefined)
        self.leKey.setObjectName(_fromUtf8("leKey"))
        self.horizontalLayout_2.addWidget(self.leKey)
        self.label_7 = QtGui.QLabel(self.frameUserDefined)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.leValue = QtGui.QLineEdit(self.frameUserDefined)
        self.leValue.setObjectName(_fromUtf8("leValue"))
        self.horizontalLayout_2.addWidget(self.leValue)
        self.pbnAddToList2 = QtGui.QPushButton(self.frameUserDefined)
        self.pbnAddToList2.setObjectName(_fromUtf8("pbnAddToList2"))
        self.horizontalLayout_2.addWidget(self.pbnAddToList2)
        self.gridLayout_4.addWidget(self.frameUserDefined, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.advanced_tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
        self.lstKeywords = QtGui.QListWidget(self.advanced_tab)
        self.lstKeywords.setAlternatingRowColors(True)
        self.lstKeywords.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lstKeywords.setObjectName(_fromUtf8("lstKeywords"))
        self.gridLayout_4.addWidget(self.lstKeywords, 4, 0, 1, 1)
        self.pbnRemove = QtGui.QPushButton(self.advanced_tab)
        self.pbnRemove.setObjectName(_fromUtf8("pbnRemove"))
        self.gridLayout_4.addWidget(self.pbnRemove, 5, 0, 1, 1)
        self.tab_widget.addTab(self.advanced_tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tab_widget, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.lblTitle.setBuddy(self.leTitle)
        self.lblCategory.setBuddy(self.radHazard)
        self.lblSubcategory.setBuddy(self.cboSubcategory)
        self.lblSource.setBuddy(self.leSource)
        self.lblAggregationAttribute.setBuddy(self.cboAggregationAttribute)
        self.lblFemaleRatioAttribute.setBuddy(self.cboFemaleRatioAttribute)
        self.lblFemaleRatioDefault.setBuddy(self.dsbFemaleRatioDefault)
        self.lblYouthRatioAttribute.setBuddy(self.cboYouthRatioAttribute)
        self.lblYouthRatioDefault.setBuddy(self.dsbYouthRatioDefault)
        self.lblAdultRatioAttribute.setBuddy(self.cboAdultRatioAttribute)
        self.lblAdultRatioDefault.setBuddy(self.dsbAdultRatioDefault)
        self.lblElderlyRatioAttribute.setBuddy(self.cboElderlyRatioAttribute)
        self.lblElderlyRatioDefault.setBuddy(self.dsbElderlyRatioDefault)
        self.label_4.setBuddy(self.cboKeyword)
        self.label_6.setBuddy(self.leKey)
        self.label_7.setBuddy(self.leValue)
        self.label_8.setBuddy(self.lstKeywords)

        self.retranslateUi(KeywordsDialogBase)
        self.tab_widget.setCurrentIndex(1)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setHidden)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setHidden)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setVisible)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setVisible)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), KeywordsDialogBase.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), KeywordsDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(KeywordsDialogBase)
        KeywordsDialogBase.setTabOrder(self.leTitle, self.radHazard)
        KeywordsDialogBase.setTabOrder(self.radHazard, self.radExposure)
        KeywordsDialogBase.setTabOrder(self.radExposure, self.radPostprocessing)
        KeywordsDialogBase.setTabOrder(self.radPostprocessing, self.cboSubcategory)
        KeywordsDialogBase.setTabOrder(self.cboSubcategory, self.leSource)
        KeywordsDialogBase.setTabOrder(self.leSource, self.cboAggregationAttribute)
        KeywordsDialogBase.setTabOrder(self.cboAggregationAttribute, self.cboFemaleRatioAttribute)
        KeywordsDialogBase.setTabOrder(self.cboFemaleRatioAttribute, self.dsbFemaleRatioDefault)
        KeywordsDialogBase.setTabOrder(self.dsbFemaleRatioDefault, self.cboYouthRatioAttribute)
        KeywordsDialogBase.setTabOrder(self.cboYouthRatioAttribute, self.dsbYouthRatioDefault)
        KeywordsDialogBase.setTabOrder(self.dsbYouthRatioDefault, self.cboAdultRatioAttribute)
        KeywordsDialogBase.setTabOrder(self.cboAdultRatioAttribute, self.dsbAdultRatioDefault)
        KeywordsDialogBase.setTabOrder(self.dsbAdultRatioDefault, self.cboElderlyRatioAttribute)
        KeywordsDialogBase.setTabOrder(self.cboElderlyRatioAttribute, self.dsbElderlyRatioDefault)
        KeywordsDialogBase.setTabOrder(self.dsbElderlyRatioDefault, self.radPredefined)
        KeywordsDialogBase.setTabOrder(self.radPredefined, self.radUserDefined)
        KeywordsDialogBase.setTabOrder(self.radUserDefined, self.cboKeyword)
        KeywordsDialogBase.setTabOrder(self.cboKeyword, self.lePredefinedValue)
        KeywordsDialogBase.setTabOrder(self.lePredefinedValue, self.pbnAddToList1)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList1, self.leKey)
        KeywordsDialogBase.setTabOrder(self.leKey, self.leValue)
        KeywordsDialogBase.setTabOrder(self.leValue, self.pbnAddToList2)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList2, self.lstKeywords)
        KeywordsDialogBase.setTabOrder(self.lstKeywords, self.pbnRemove)
        KeywordsDialogBase.setTabOrder(self.pbnRemove, self.buttonBox)
        KeywordsDialogBase.setTabOrder(self.buttonBox, self.tab_widget)
        KeywordsDialogBase.setTabOrder(self.tab_widget, self.scrollArea_2)

    def retranslateUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setWindowTitle(_translate("KeywordsDialogBase", "InaSAFE - Keyword Editor", None))
        self.lblTitle.setText(_translate("KeywordsDialogBase", "Title", None))
        self.lblCategory.setText(_translate("KeywordsDialogBase", "Category", None))
        self.radHazard.setToolTip(_translate("KeywordsDialogBase", "A hazard is a situation that poses a level of threat to life, health, property, or environment. (Wikipedia)", None))
        self.radHazard.setText(_translate("KeywordsDialogBase", "Hazard", None))
        self.radExposure.setToolTip(_translate("KeywordsDialogBase", "Where people and property are situated.", None))
        self.radExposure.setText(_translate("KeywordsDialogBase", "Exposure", None))
        self.radPostprocessing.setText(_translate("KeywordsDialogBase", "Postprocessing", None))
        self.lblSubcategory.setText(_translate("KeywordsDialogBase", "Subcategory", None))
        self.cboSubcategory.setToolTip(_translate("KeywordsDialogBase", "A subcategory represents the type of hazard.", None))
        self.lblSource.setText(_translate("KeywordsDialogBase", "&Source", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.core_fields_tab), _translate("KeywordsDialogBase", "Core fields", None))
        self.groupBox_3.setTitle(_translate("KeywordsDialogBase", "Report labels", None))
        self.lblAggregationAttribute.setText(_translate("KeywordsDialogBase", "Aggregation attribute", None))
        self.groupBox_2.setTitle(_translate("KeywordsDialogBase", "Gender Ratio", None))
        self.lblFemaleRatioAttribute.setText(_translate("KeywordsDialogBase", "Female ratio attribute", None))
        self.lblFemaleRatioDefault.setText(_translate("KeywordsDialogBase", "Female ratio default", None))
        self.groupBox.setTitle(_translate("KeywordsDialogBase", "Age Ratios", None))
        self.lblYouthRatioAttribute.setText(_translate("KeywordsDialogBase", "Youth ratio attribute", None))
        self.lblYouthRatioDefault.setText(_translate("KeywordsDialogBase", "Youth ratio default", None))
        self.lblAdultRatioAttribute.setText(_translate("KeywordsDialogBase", "Adult ratio attribute", None))
        self.lblAdultRatioDefault.setText(_translate("KeywordsDialogBase", "Adult ratio default", None))
        self.lblElderlyRatioAttribute.setText(_translate("KeywordsDialogBase", "Elderly ratio attribute", None))
        self.lblElderlyRatioDefault.setText(_translate("KeywordsDialogBase", "Elderly ratio default", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.aggregation_tab), _translate("KeywordsDialogBase", "Aggregation", None))
        self.radPredefined.setText(_translate("KeywordsDialogBase", "Predefined", None))
        self.radUserDefined.setText(_translate("KeywordsDialogBase", "User defined", None))
        self.label_4.setText(_translate("KeywordsDialogBase", "Keyword", None))
        self.label_5.setText(_translate("KeywordsDialogBase", "Value", None))
        self.pbnAddToList1.setText(_translate("KeywordsDialogBase", "Add to list", None))
        self.label_6.setText(_translate("KeywordsDialogBase", "Key", None))
        self.label_7.setText(_translate("KeywordsDialogBase", "Value", None))
        self.pbnAddToList2.setText(_translate("KeywordsDialogBase", "Add to list", None))
        self.label_8.setText(_translate("KeywordsDialogBase", "Current keywords", None))
        self.pbnRemove.setText(_translate("KeywordsDialogBase", "Remove selected", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.advanced_tab), _translate("KeywordsDialogBase", "Advanced", None))

import resources_rc
