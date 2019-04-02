class PlotStyle:
    BG = '#1A463B'
    BLUE = '#35D1AA'
    RED = '#F73E5F'
    ORANGE = '#E98144'
    GREEN = '#7BC280'
    BROWN = '#B08669'

    @staticmethod
    def apply(plot_object):
        plot_object.set_facecolor(PlotStyle.BG)
        plot_object.xaxis.set_visible(False)
        plot_object.yaxis.set_visible(False)