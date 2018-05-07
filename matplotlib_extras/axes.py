# ======================================================================
# Brad T. Aagaard
# U.S. Geological Survey
# ======================================================================

"""Helper functions for creating axes."""

def axes_rect_from_margins(figure, nrows=1, ncols=1, row=1, col=1,
                           margins=((0.5, 0.5, 0.1), (0.5, 0.5, 0.1))):
    """Compute figure rect for axis based on rows/cols and margins.

    :param figure: matplotlib.figure.Figure associated with axes.

    :param nrows: Number of subplots in a row.

    :param ncols: Number of subplots in a column.

    :param row: Row for axes.

    :param col: Column for axes.

    :param margins: Tuple with margins and horizontal/vertical
        separation between subplots.  ((left, hsep, right), (bottom,
        vsep, top)
    """
    fig_height = figure.get_figheight()
    fig_width = figure.get_figwidth()
    (margin_left, hsep, margin_right) = margins[0]
    (margin_bot, vsep, margin_top) = margins[1]
    axes_width = (fig_width-margin_right-margin_left-hsep*int(ncols-1))/float(ncols)
    axes_height = (fig_height-margin_top-margin_bot-vsep*int(nrows-1))/float(nrows)

    left = (margin_left+(col-1)*(axes_width+hsep)) / fig_width
    if col <= ncols:
        right = left + axes_width / fig_width
    else:
        right = 1.0 - margin_right/fig_width
        axes_width = (right-left)*fig_width
    bottom = (margin_bot+(nrows-row)*(axes_height+vsep)) / fig_height
    #top = bottom + axes_height / h
    #print "left: %.4f, right: %.4f, top: %.4f, bottom: %.4f, fig_width: %.4f, fig_height: %.4f" % \
    #      (left, right, top, bottom, axes_width/w, axes_height/h)
    return [left, bottom, axes_width/fig_width, axes_height/fig_height]


# End of file
