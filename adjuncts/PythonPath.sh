# Default Python Path
# ['', '/usr/lib64/python37.zip', '/usr/lib64/python3.7', '/usr/lib64/python3.7/lib-dynload', '/home/erikbeck/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/site-packages', '/usr/lib64/python3.7/site-packages', '/usr/lib/python3.7/site-packages']


PYSYSBASE="/usr/lib64/python3.7:/usr/lib64/python3.7/lib-dynload:/home/erikbeck/.local/lib/python3.7/site-packages:/usr/local/lib/python3.7/site-packages:/usr/lib64/python3.7/site-packages:/usr/lib/python3.7/site-packages"

MYPYLIB="/usr/local/lib"

# For SWMM GUI, need to add

SWMSRC="/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/epanet:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/epanet/hydraulics:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/epanet/options:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/swmm:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/swmm/hydraulics:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/swmm/hydrology:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/core/swmm/options"

SWMEXT="/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/epanet:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/epanet/model:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/epanet/outputapi:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/swmm:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/swmm/model:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/swmm/outputapi:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/test:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/test/epanet:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/Externals/test/epanet/Examples"

SWMUI="/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/icons:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/plugins:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/plugins/ImportExportGIS:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/plugins/MyCalculations:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/plugins/Summary:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/scripts"

SWMO="/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/icons:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/icons/editor:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/icons/svg:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/__pycache__:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/SWMM:/home/erikbeck/OtherGits/SWMM-EPANET_User_Interface/src/ui/SWMM/swmmimages"

PYSIS="/usr/lib64/python3.7/site-packages/PyQt5:/usr/lib64/python3.7/site-packages/wx"

PYQGIS="/usr/lib64/python3.7/site-packages/qgis:/usr/lib64/python3.7/site-packages/qgis/core:/usr/lib64/python3.7/site-packages/qgis/core/additions"

PYTHONPATH=$PYSYSBASE:$MYPYLIB:$SWMEXT:$SWMUI:$SWMO:$PYSIS:$PYQGIS

export PYTHONPATH


