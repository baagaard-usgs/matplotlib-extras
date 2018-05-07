# ======================================================================
# Brad T. Aagaard
# U.S. Geological Survey
# ======================================================================

"""Helper functions for creating axes."""

class RectFactory(object):
    """Factory for computing figure rect for axes based on rows/cols and
    margins.
    """

    def __init__(self, figure, nrows=1, ncols=1, margins=((0.5, 0.5, 0.1), (0.5, 0.5, 0.1))):
        """Set default number of rows, cols, and margins.

        :param figure: matplotlib.figure.Figure associated with axes.

        :param nrows: Number of subplots in a row.

        :param ncols: Number of subplots in a column.

        :param margins: Tuple with margins and horizontal/vertical
            separation between subplots.  ((left, hsep, right),
            (bottom, vsep, top)
        """
        self.fig_height = figure.get_figheight()
        self.fig_width = figure.get_figwidth()
        self.nrows = nrows
        self.ncols = ncols
        self.margins = margins
        return

    def rect(self, nrows=None, ncols=None, row=1, col=1, margins=None):
        """Compute figure rect for axis based on rows/cols and margins.

        :param nrows: Number of subplots in a row.

        :param ncols: Number of subplots in a column.

        :param row: Row for axes.

        :param col: Column for axes.

        :param margins: Tuple with margins and horizontal/vertical
        separation between subplots.  ((left, hsep, right), (bottom,
        vsep, top)
        """
        nrows = nrows or self.nrows
        ncols = ncols or self.ncols
        margins = margins or self.margins
        
        (margin_left, hsep, margin_right) = margins[0]
        (margin_bot, vsep, margin_top) = margins[1]
        axes_width = (self.fig_width-margin_right-margin_left-hsep*int(ncols-1))/float(ncols)
        axes_height = (self.fig_height-margin_top-margin_bot-vsep*int(nrows-1))/float(nrows)

        left = (margin_left+(col-1)*(axes_width+hsep)) / self.fig_width
        if col <= ncols:
            right = left + axes_width / self.fig_width
        else:
            right = 1.0 - margin_right/self.fig_width
        axes_width = (right-left)*self.fig_width
        bottom = (margin_bot+(nrows-row)*(axes_height+vsep)) / self.fig_height
        #top = bottom + axes_height / h
        #print "left: %.4f, right: %.4f, top: %.4f, bottom: %.4f, self.fig_width: %.4f,
        # self.fig_height: %.4f" % \
        #      (left, right, top, bottom, axes_width/w, axes_height/h)
        return [left, bottom, axes_width/self.fig_width, axes_height/self.fig_height]


def add_background_axes(figure, rect, facecolor=None, alpha=0.5):
    """Add background axis.
    """
    if facecolor is None:
        import matplotlib
        facecolor = matplotlib.rcParams["legend.facecolor"]
    
    ax = figure.add_axes(rect)
    ax.patch.set_facecolor(facecolor)
    ax.patch.set_alpha(alpha)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["right"].set_color("none")
    return ax


# End of file
