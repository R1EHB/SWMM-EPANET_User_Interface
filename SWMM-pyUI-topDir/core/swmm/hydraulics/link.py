import traceback
from enum import Enum
from core.project_base import Section
from core.metadata import Metadata
from core.coordinate import Link


class SwmmLink(Section, Link):
    """A link in a SWMM model"""

    def __init__(self):
        Section.__init__(self)
        Link.__init__(self)


class Conduit(SwmmLink):
    """A conduit link (pipe or channel) in a SWMM model drainage system that conveys water from one node to another."""

    #    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '',               "User-assigned name of the conduit"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '',               "Node on the inlet end of the conduit"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '',               "Node on the outlet end of the conduit"),
        ("description",             '', "Description",     "",       '', '',               "Optional description of the conduit"),
        ("tag",                     '', "Tag",             "",       '', '',               "Optional label used to categorize or classify the conduit"),
        ("shape",                   '', "Shape",           "",       '', '',               "Click to edit the conduit's cross section geometry"),
        ("max_depth",               '', "Max. Depth",      "",       '(ft)', '(m)',        "Maximum depth of cross section"),
        ("length",                  '', "Length",          "0.0",    '(ft)', '(m)',        "Conduit length"),
        ("roughness",               '', "Roughness",       "0.0",    '', '',               "Manning's N roughness coefficient"),
        ("inlet_offset",            '', "Inlet Offset",    "0.0",    '(ft)', '(m)',        "Depth of conduit invert above node invert at inlet end"),
        ("outlet_offset",           '', "Outlet Offset",   "0.0",    '(ft)', '(m)',        "Depth of conduit invert above node invert at outlet end"),
        ("initial_flow",            '', "Initial Flow",    "0.0",    '', '',               "Initial flow in the conduit (flow units)"),
        ("maximum_flow",            '', "Maximum Flow",    "",       '', '',               "Maximum flow allowed in the conduit (flow units)"),
        ("entry_loss_coefficient",  '', "Entry Loss Coeff.","0.0",   '', '',               "Coefficient for energy losses at the entrance of the conduit"),
        ("exit_loss_coefficient",   '', "Exit Loss Coeff.","0.0",    '', '',               "Coefficient for energy losses at the exit of the conduit"),
        ("loss_coefficient",        '', "Avg. Loss Coeff.","0.0",    '', '',               "Coefficient for energy losses along the length of the conduit"),
        ("seepage",                 '', "Seepage Loss Rate","0.0",   '(in/hr)', '(mm/hr)', "Rate of seepage loss into surrounding soil"),
        ("flap_gate",               '', "Flap Gate",        "False", '', '',               "True if a flap gate prevents reverse flow through conduit"),
        ("culvert_code",            '', "Culvert Code",     "",      '', '',               "Culvert type code (leave blank for no culvert)")
    ))

    def __init__(self):
        SwmmLink.__init__(self)

        ## Conduit length (feet or meters)
        self.length = "0.0"

        ## Manning's N roughness coefficient
        self.roughness = "0.0"

        ## Depth or elevation of the conduit invert above the node invert
        ## at the upstream end of the conduit (feet or meters)
        self.inlet_offset = "0.0"

        ## Depth or elevation of the conduit invert above the node invert
        ## at the downstream end of the conduit (feet or meters)
        self.outlet_offset = "0.0"

        ## Initial flow in the conduit (flow units)
        self.initial_flow = "0.0"

        ## Maximum flow allowed in the conduit (flow units)
        self.maximum_flow = ''

        # TODO: provide access to the following:
        # self.cross_section = ''
        # """See class CrossSection"""             # from [XSECTIONS] table

        ## Head loss coefficient associated with energy losses at the entrance of the conduit
        self.entry_loss_coefficient = 0.0      # from [LOSSES] table

        ## Head loss coefficient associated with energy losses at the exit of the conduit
        self.exit_loss_coefficient = 0.0

        ## Head loss coefficient associated with energy losses along the length of the conduit
        self.loss_coefficient = 0.0

        ## True if a flap gate exists that prevents backflow
        self.flap_gate = False

        ## Rate of seepage loss into surrounding soil (in/hr or mm/hr)
        self.seepage = 0.0

    def get_slope(self):
        lslope = 0.0
        if self.inlet_node and self.outlet_node:
            inlet_elevation = 0.0
            outlet_elevation = 0.0
            try:
                inlet_elevation = float(self.inlet_node.elevation)
            except:
                inlet_elevation = None
            try:
                outlet_elevation = float(self.outlet_node.elevation)
            except:
                outlet_elevation = None

            if inlet_elevation is not None and outlet_elevation is not None:
                ioval = 0.0
                ooval = 0.0
                try:
                    ioval = float(self.inlet_offset)
                except:
                    ioval = None
                try:
                    ooval = float(self.outlet_offset)
                except:
                    ooval = None
                elev_diff = 0.0
                if ioval is not None and ooval is not None:
                    elev_diff = abs(outlet_elevation + ooval - inlet_elevation - ioval)
                else:
                    elev_diff = abs(outlet_elevation - inlet_elevation)
                my_len = 0.0
                try:
                    my_len = float(self.length)
                except:
                    my_len = None

                if my_len is not None:
                    lslope = elev_diff / my_len
        return lslope


class Pump(SwmmLink):
    """A pump link in a SWMM model"""


#    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '',        "User-assigned name of the pump"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '',        "Node on the inlet end of the pump"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '',        "Node on the outlet end of the pump"),
        ("description",             '', "Description",     "",       '', '',        "Optional description of the pump"),
        ("tag",                     '', "Tag",             "",       '', '',        "Optional label used to categorize or classify the pump"),
        ("pump_curve",              '', "Pump Curve",      "*",      '', '',        "Name of pump curve (or * for ideal pump)"),
        ("initial_status",          '', "Initial Status",  "ON",     '', '',        "Initial Status of the pump (ON or OFF)"),
        ("startup_depth",           '', "Startup Depth",   "0.0",    '(ft)', '(m)', "Depth at inlet node when the pump turns on"),
        ("shutoff_depth",           '', "Shutoff Depth",   "0.0",    '(ft)', '(m)', "Depth at inlet node when the pump turns off")
    ))

    def __init__(self):
        SwmmLink.__init__(self)

        ## str: Associated pump curve
        self.pump_curve = "None"

        ## float: Initial status of the pump
        self.initial_status = "ON"

        ## float: Depth at inlet node when the pump turns on
        self.startup_depth = 0.0

        ## float: Depth at inlet node when the pump turns off
        self.shutoff_depth = 0.0


class OrificeType(Enum):
    SIDE = 1
    BOTTOM = 2


class Orifice(SwmmLink):
    """An orifice link in a SWMM model"""

#    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '',        "User-assigned name of orifice"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '',        "Node on the inlet end of orifice"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '',        "Node on the outlet end of orifice"),
        ("description",             '', "Description",     "",       '', '',        "Optional description of orifice"),
        ("tag",                     '', "Tag",             "",       '', '',        "Optional label used to categorize or classify orifice"),
        ("type",                    '', "Type",            "",       '', '',        "Type of orifice"),
        ("cross_section",           '', "Shape",           "",       '', '',        "Orifice shape"),
        ("height",                  '', "Height",          "1.0",    '(ft)', '(m)', "Height of orifice opening when fully opened"),
        ("width",                   '', "Width",           "1.0",    '(ft)', '(m)', "Width of orifice opening when fully opened"),
        ("inlet_offset",            '', "Inlet Offset",    "0.0",    '(ft)', '(m)', "Depth of bottom of orifice opening from inlet node invert"),
        ("discharge_coefficient",   '', "Discharge Coeff.",   "0.0",   '', '',      "Discharge coefficient"),
        ("flap_gate",               '', "Flap Gate",          "False", '', '',      "True if orifice contains a flap gate to prevent backflow"),
        ("o_rate",                  '', "Time to Open/Close", "0.0",   '', '',      "Time in decimal hours to open/close a gated orifice")
    ))

    def __init__(self):
        SwmmLink.__init__(self)

        ## OrificeType: Type of orifice
        self.type = OrificeType.SIDE

        ## Name of cross section in XSECTIONS Section
        self.cross_section = "None"

        ## float: Depth of bottom of orifice opening from inlet node invert
        self.inlet_offset = 0.0

        ## float: Discharge coefficient
        self.discharge_coefficient = 0.0

        ## bool: True if a flap gate exists that prevents backflow.
        self.flap_gate = False

        ## float: Time in decimal hours to open/close a gated orifice
        self.o_rate = 0.0


class WeirType(Enum):
    TRANSVERSE = 1
    SIDEFLOW = 2
    V_NOTCH = 3
    TRAPEZOIDAL = 4
    ROADWAY = 5


class RoadSurfaceType(Enum):
    PAVED = 1
    GRAVEL = 2


class Weir(SwmmLink):
    """A weir link in a SWMM model"""

#    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '',           "User-assigned name of weir"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '',           "Node on the inlet end of weir"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '',           "Node on the outlet end of weir"),
        ("description",             '', "Description",     "",       '', '',           "Optional description of the weir"),
        ("tag",                     '', "Tag",             "",       '', '',           "Optional label used to categorize or classify the weir"),
        ("type",                   '', "Type",            "",       '', '',            "Type of weir"),
        ("height",                  '', "Height",          "1.0",    '(ft)', '(m)',    "Vertical height of weir opening"),
        ("length",                  '', "Length",          "1.0",    '(ft)', '(m)',    "Horizontal length of weir crest (or crown for V-Notch weir)"),
        ("side_slope",              '', "Side Slope",      "0.0",    '', '',           "Slope (width-to-height) of TRAPEZOIDAL weir side walls"),
        ("inlet_offset",            '', "Inlet Offset",    "0.0",    '(ft)', '(m)',    "Depth of bottom of weir opening from inlet node invert"),
        ("discharge_coefficient",   '', "Discharge Coeff.","0.0",    '(CFS)', '(CMS)', "Discharge coefficient for central portion of weir"),
        ("flap_gate",               '', "Flap Gate",       "False",  '', '',           "True if weir contains a flap gate to prevent backflow"),
        ("end_contractions",        '', "End Contractions","0",      '', '',           "Number of end contractions"),
        ("end_coefficient",         '', "End Coeff.",      "0",      '(CFS)', '(CMS)', "Discharge coefficient for flow through the triangular ends of a TRAPEZOIDAL weir"),
        ("can_surcharge",           '', "Can Surcharge",   "False",  '', '',           "True if weir can surcharge"),
        ("coeff_curve",             '', "Coeff. Curve",    "",       '', '',           "Optional name of curve that relates discharge coefficient to head"),
        ("road_width",              '', "Road Width",      "0.0",    '(ft)', '(m)',    "Width of road lanes and shoulders if roadway weir"),
        ("road_surface",            '', "Road Surface",    "",       '', '',           "Type of road surface if roadway weir")
    ))

    def __init__(self):
        SwmmLink.__init__(self)

        ## Type of weir
        self.type = WeirType.TRANSVERSE

        ## float: Depth of bottom of weir opening from inlet node invert
        self.inlet_offset = 0.0

        ## float: Discharge coefficient for central portion of weir
        self.discharge_coefficient = 0.0

        ## bool: True if weir contains a flap gate to prevent backflow
        self.flap_gate = False

        ## Number of end contractions for TRANSVERSE or TRAPEZOIDAL
        self.end_contractions = 0

        ## float: Discharge coefficient for flow through the triangular ends of a trapezoidal weir
        self.end_coefficient = 0.0

        ## bool: True if weir can surcharge
        self.can_surcharge = True

        ## str: Associated coefficient curve
        self.coeff_curve = ""

        ## float: Width of road lanes and shoulders
        self.road_width = 0.0

        ## RoadSurfaceType: Type of road surface
        self.road_surface = RoadSurfaceType.PAVED


class OutletCurveType(Enum):
    TABULAR_DEPTH = 1
    TABULAR_HEAD = 2
    FUNCTIONAL_DEPTH = 3
    FUNCTIONAL_HEAD = 4


class Outlet(SwmmLink):
    """An outlet link in a SWMM model"""

#    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '',                     "User-assigned name of outlet"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '',                     "Node on the inlet end of outlet"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '',                     "Node on the outlet end of outlet"),
        ("description",             '', "Description",     "",       '', '',                     "Optional description of the outlet"),
        ("tag",                     '', "Tag",             "",       '', '',                     "Optional label used to categorize or classify the outlet"),
        ("inlet_offset",            '', "Inlet Offset",    "0.0",    '(ft)', '(m)',              "Depth of outlet above inlet node invert"),
        ("flap_gate",               '', "Flap Gate",       "False",  '', '',                     "True if outlet contains a flap gate to prevent backflow"),
        ("curve_type",              '', "Rating Curve",    "",       '', '',                     "Method of defining flow as a function of either freeboard depth or head across the outlet"),
        ("coefficient",             '', "Functional Curve Coefficient", "0.0",    '(ft)', '(m)', "A-value in expression Outflow = A*y^B for y(=depth or head)"),
        ("exponent",                '', "Functional Curve Exponent",    "0.0",    '(ft)', '(m)', "B-value in expression Outflow = A*y^B for y(=depth or head)"),
        ("rating_curve",            '', "Tabular Curve Name",           "",       '', '',        "Name of rating curve that relates outflow to either depth or head")
    ))

    def __init__(self):
        SwmmLink.__init__(self)

        ## float: Depth of outlet above inlet node invert
        self.inlet_offset = 0.0

        ## bool: True if outlet contains a flap gate to prevent backflow
        self.flap_gate = False

        ## float: Coefficient in outflow expression
        self.coefficient = 10.0

        ## float: Exponent in outflow expression
        self.exponent = 0.5

        ## OutletCurveType: Method of defining flow as a function of either freeboard depth or head across the outlet
        self.curve_type = OutletCurveType.FUNCTIONAL_DEPTH

        ## str: Name of rating curve that relates outflow to either depth or head
        self.rating_curve = "None"


class SubLink(SwmmLink):
    """A symbolic link in a SWMM model drainage system that conveys water from a Sub to its outlet node."""

    #    attribute,         input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                    '', "Name",            "",       '', '', "User-assigned name of the conduit"),
        ("inlet_node",              '', "Inlet Node",      "",       '', '', "Node on the inlet end of the conduit"),
        ("outlet_node",             '', "Outlet Node",     "",       '', '', "Node on the outlet end of the conduit"),
        ("description",             '', "Description",     "",       '', '', "Optional description of the conduit"),
        ("tag",                     '', "Tag",             "",       '', '',
         "Optional label used to categorize or classify the conduit")
    ))

    def __init__(self):
        SwmmLink.__init__(self)
        pass


class CrossSectionShape(Enum):
    NotSet = 0
    CIRCULAR = 1            # Full Height = Diameter
    FORCE_MAIN = 2          # Full Height = Diameter, Roughness
    FILLED_CIRCULAR = 3     # Full Height = Diameter, Filled Depth
    RECT_CLOSED = 4         # Rectangular: Full Height, Top Width
    RECT_OPEN = 5           # Rectangular: Full Height, Top Width
    TRAPEZOIDAL = 6         # Full Height, Base Width, Side Slopes
    TRIANGULAR = 7          # Full Height, Top Width
    HORIZ_ELLIPSE = 8       # Full Height, Max. Width
    VERT_ELLIPSE = 9        # Full Height, Max. Width
    ARCH = 10               # Size Code or Full Height, Max. Width
    PARABOLIC = 11          # Full Height, Top Width
    POWER = 12              # Full Height, Top Width, Exponent
    RECT_TRIANGULAR = 13    # Full Height, Top Width, Triangle Height
    RECT_ROUND = 14         # Full Height, Top Width, Bottom Radius
    MODBASKETHANDLE = 15    # Full Height, Bottom Width, Top Radius
    EGG = 16                # Full Height
    HORSESHOE = 17          # Full Height Gothic Full Height
    GOTHIC = 18             # Full Height
    CATENARY = 19           # Full Height
    SEMIELLIPTICAL = 20     # Full Height
    BASKETHANDLE = 21       # Full Height
    SEMICIRCULAR = 22       # Full Height
    IRREGULAR = 23          # TransectCoordinates (Natural Channel)
    CUSTOM = 24             # Full Height, ShapeCurveCoordinates
    DUMMY = 25


class CrossSection(Section):
    """A cross section of a Conduit, Orifice, or Weir

    Attributes:
        link (str): name of the conduit, orifice, or weir this is a cross-section of.
        shape (CrossSectionShape): name of cross-section shape.
        geometry1 (str): full height of the cross-section (ft or m). For irregular, this is the cross-section name.
        geometry2 (str): auxiliary parameters (width, side slopes, etc.)
        geometry3 (str): auxiliary parameters (width, side slopes, etc.)
        geometry4 (str): auxiliary parameters (width, side slopes, etc.)
        barrels (str): number of barrels (i.e., number of parallel pipes of equal size, slope, and
                       roughness) associated with a conduit (default is 1).
        culvert_code (str): name of conduit inlet geometry if it is a culvert subject to possible inlet flow control
        curve (str): name of associated Shape Curve that defines how width varies with depth.
    """

    def __init__(self):
        Section.__init__(self)

        ## name of the conduit, orifice, or weir this is a cross-section of.
        self.link = "None"

        ## cross-section shape"""
        self.shape = CrossSectionShape.NotSet

        ## float as str: full height of the cross-section (ft or m)
        self.geometry1 = '0.0'

        ## float as str: auxiliary parameters (width, side slopes, etc.)
        self.geometry2 = '0.0'

        ## float as str: auxiliary parameters (width, side slopes, etc.)
        self.geometry3 = '0.0'

        ## float as str: auxiliary parameters (width, side slopes, etc.)
        self.geometry4 = '0.0'

        ## float: number of barrels (i.e., number of parallel pipes of equal size, slope, and
        ## roughness) associated with a conduit (default is 1).
        self.barrels = '1'

        ## code number for the conduits inlet geometry if it is a culvert subject to possible inlet flow control
        self.culvert_code = ''

        ## str: name of associated Shape Curve that defines how width varies with depth.
        self.curve = "None"

    # TODO: access geometry1 as a name such as transect or xsection_name or geometry
    # """str: name of cross-section geometry of an irregular channel"""


class Transects(Section):
    SECTION_NAME = "[TRANSECTS]"
    DEFAULT_COMMENT = ";;Transect Data in HEC-2 format"

    def __init__(self):
        Section.__init__(self)
        self.value = []


class Transect(Section):
    """the cross-section geometry of a natural channel or conduit with irregular shapes"""

    def __init__(self):
        Section.__init__(self)

        ## Transect Name
        self.name = ''

        ## Manning's n of left overbank portion of channel. Use 0 if no change from previous NC line.
        self.n_left = '0'

        ## Manning's n of right overbank portion of channel. Use 0 if no change from previous NC line.
        self.n_right = '0'

        ## Manning's n of main channel portion of channel. Use 0 if no change from previous NC line.
        self.n_channel = '0'

        ## station position which ends the left overbank portion of the channel (ft or m).
        self.overbank_left = '0'

        ## station position which begins the right overbank portion of the channel (ft or m).
        self.overbank_right = '0'

        ## factor by which distances between stations should be multiplied to increase (or decrease) the width of the channel (enter 0 if not applicable).
        self.stations_modifier = '0'

        ## amount added (or subtracted) from the elevation of each station (ft or m).
        self.elevations_modifier = '0'

        ## the ratio of the length of a meandering main channel to the length of the overbank area that surrounds it (use 0 if not applicable).
        self.meander_modifier = '0'

        ## list of (station, elevation) pairs
        self.stations = []
