#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Dec  2 12:07:20 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.unisigtype = unisigtype = 101
        self.uniselect = uniselect = 0
        self.samp_rate = samp_rate = 32000
        self.f = f = 1000

        ##################################################
        # Blocks
        ##################################################
        self._uniselect_options = (0, 1, )
        self._uniselect_labels = ('Soundcard', 'TestSignal', )
        self._uniselect_tool_bar = Qt.QToolBar(self)
        self._uniselect_tool_bar.addWidget(Qt.QLabel("uniselect"+": "))
        self._uniselect_combo_box = Qt.QComboBox()
        self._uniselect_tool_bar.addWidget(self._uniselect_combo_box)
        for label in self._uniselect_labels: self._uniselect_combo_box.addItem(label)
        self._uniselect_callback = lambda i: Qt.QMetaObject.invokeMethod(self._uniselect_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._uniselect_options.index(i)))
        self._uniselect_callback(self.uniselect)
        self._uniselect_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_uniselect(self._uniselect_options[i]))
        self.top_grid_layout.addWidget(self._uniselect_tool_bar)
        self._f_range = Range(0, 100000, 10, 1000, 200)
        self._f_win = RangeWidget(self._f_range, self.set_f, "f", "counter_slider", float)
        self.top_grid_layout.addWidget(self._f_win)
        self._unisigtype_options = (101, 103, )
        self._unisigtype_labels = ('Sine', 'Square', )
        self._unisigtype_tool_bar = Qt.QToolBar(self)
        self._unisigtype_tool_bar.addWidget(Qt.QLabel("unisigtype"+": "))
        self._unisigtype_combo_box = Qt.QComboBox()
        self._unisigtype_tool_bar.addWidget(self._unisigtype_combo_box)
        for label in self._unisigtype_labels: self._unisigtype_combo_box.addItem(label)
        self._unisigtype_callback = lambda i: Qt.QMetaObject.invokeMethod(self._unisigtype_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._unisigtype_options.index(i)))
        self._unisigtype_callback(self.unisigtype)
        self._unisigtype_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_unisigtype(self._unisigtype_options[i]))
        self.top_grid_layout.addWidget(self._unisigtype_tool_bar)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=uniselect,
        	output_index=0,
        )
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_CONST_WAVE, f, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_selector_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_unisigtype(self):
        return self.unisigtype

    def set_unisigtype(self, unisigtype):
        self.unisigtype = unisigtype
        self._unisigtype_callback(self.unisigtype)

    def get_uniselect(self):
        return self.uniselect

    def set_uniselect(self, uniselect):
        self.uniselect = uniselect
        self._uniselect_callback(self.uniselect)
        self.blks2_selector_0.set_input_index(int(self.uniselect))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.analog_sig_source_x_0.set_frequency(self.f)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
