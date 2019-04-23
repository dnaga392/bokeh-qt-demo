import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

def main(argv):
    app = QApplication(argv)
    wv = QWebEngineView()

    plot = figure(plot_width=1200, plot_height=1200)
    # plot.circle([1, 2], [3, 4])
    plot.annulus(x=[1, 2, 3], y=[1, 2, 3], color="#7FC97F",
                 inner_radius=0.2, outer_radius=0.5)

    wv.setHtml(file_html(plot, CDN, 'test plot'))
    wv.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
