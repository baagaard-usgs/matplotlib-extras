# ======================================================================
# Brad T. Aagaard
# U.S. Geological Survey
# ======================================================================

"""Add custom colors.
"""

from matplotlib.colors import ColorConverter

def add_general():
    """Add some general custom colors."""
    colors = {
        "c_dkgray": (0.25, 0.25, 0.25),
        "c_mdgray": (0.50, 0.50, 0.50),
        "c_ltgray": (0.75, 0.75, 0.75),

        "c_dkslate": (0.18, 0.21, 0.28),
        "c_slate": (0.45, 0.50, 0.68),
        "c_ltslate": (0.85, 0.88, 0.95),

        "c_ltyellow": (1.0, 1.0, 0.45),
        "c_yellow": (0.9, 0.9, 0.0),

        "c_ltorange": (1.0, 0.74, 0.41),
        "c_orange": (0.96, 0.50, 0.0),

        "c_ltred": (1.0, 0.25, 0.25),
        "c_red": (0.79, 0.00, 0.01),

        "c_ltblue": (0.67, 0.85, 0.91),
        "c_blue": (0.17, 0.48, 0.71),

        "c_ltlt_green": (0.70, 1.00, 0.70),
        "c_ltgreen": (0.37, 0.80, 0.05),
        "c_green": (0.23, 0.49, 0.03),

        "c_ltpurple": (0.81, 0.57, 1.0),
        "c_purple": (0.38, 0.00, 0.68)
    }
    ColorConverter.colors.update(colors)
    return


def add_mmi():
    """Add MMI colors."""
    colors = {
        "c_mmi_1": (0.82, 0.75, 1.00),
        "c_mmi_2": (0.75, 0.80, 1.00),
        "c_mmi_3": (0.63, 0.90, 1.00),
        "c_mmi_4": (0.50, 1.00, 1.00),
        "c_mmi_5": (0.48, 1.00, 0.58),
        "c_mmi_6": (1.00, 1.00, 0.00),
        "c_mmi_7": (1.00, 0.78, 0.00),
        "c_mmi_8": (1.00, 0.57, 0.00),
        "c_mmi_9": (1.00, 0.00, 0.00),
        "c_mmi_10": (0.78, 0.00, 0.00),
    }
    ColorConverter.colors.update(colors)
    return


def add_usgs():
    """Add USGS colors."""
    colors = {
        # Main Colors
        "c_usgs_green": "#006F41",
        "c_usgs_teal": "#0061A3",
        "c_usgs_blue": "#0071B7",
        "c_usgs_navy": "#180F9B",
        "c_usgs_purple": "#8F009A",
        "c_usgs_red": "#FB0032",
        "c_usgs_orange": "#F99B00",

        # USGS Dark Colors
        "c_usgs_dkgreen": "#1E4D2B",
        "c_usgs_dkgreen2": "#00443F",
        "c_usgs_dkblue": "#002F57",
        "c_usgs_dknavy": "#201258",
        "c_usgs_dkpurple": "#641B56",
        "c_usgs_dkred": "#881535",
        "c_usgs_dkorange": "#8D4200",

        # USGS Light and Neutral Colors
        "c_usgs_ltblue": "#6AC3F2",
        "c_usgs_yellow": "#FFBD00",
        "c_usgs_ltgreen": "#66A48B",
        "c_usgs_ltgray": "#91B0BD",
    }
    ColorConverter.colors.update(colors)
    return


# End of file



