import spikeextractors as se
import spikewidgets as sw
import spikecomparison as sc
import matplotlib.pyplot as plt
import unittest


class TestWidgets(unittest.TestCase):
    def setUp(self):
        self._RX, self._SX = se.example_datasets.toy_example(num_channels=4, duration=10)
        self.num_units = len(self._SX.get_unit_ids())

    def tearDown(self):
        pass

    def test_timeseries(self):
        sw.plot_timeseries(self._RX)

    def test_spectrum(self):
        sw.plot_spectrum(self._RX)

    def test_spectrogram(self):
        sw.plot_spectrogram(self._RX, channel=0)

    def test_geometry(self):
        sw.plot_electrode_geometry(self._RX)

    def test_unitwaveforms(self):
        sw.plot_unit_waveforms(self._RX, self._SX)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_unit_waveforms(self._RX, self._SX, axes=axes)

    def test_unittemplates(self):
        sw.plot_unit_templates(self._RX, self._SX)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_unit_templates(self._RX, self._SX, axes=axes)

    def test_unittemplatemaps(self):
        sw.plot_unit_template_maps(self._RX, self._SX)

    def test_ampdist(self):
        sw.plot_amplitudes_distribution(self._RX, self._SX)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_amplitudes_distribution(self._RX, self._SX, axes=axes)

    def test_amptime(self):
        sw.plot_amplitudes_timeseries(self._RX, self._SX)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_amplitudes_timeseries(self._RX, self._SX, axes=axes)

    def test_features(self):
        sw.plot_pca_features(self._RX, self._SX)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_pca_features(self._RX, self._SX, axes=axes)

    def test_ach(self):
        sw.plot_autocorrelograms(self._SX, bin_size=1, window=10)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_autocorrelograms(self._SX, axes=axes)

    def test_cch(self):
        sw.plot_crosscorrelograms(self._SX, bin_size=1, window=10)
        fig, axes = plt.subplots(self.num_units, self.num_units)  # for cch need square matrix
        sw.plot_crosscorrelograms(self._SX, axes=axes)

    def test_isi(self):
        sw.plot_isi_distribution(self._SX, bins=10, window=1)
        fig, axes = plt.subplots(self.num_units, 1)
        sw.plot_isi_distribution(self._SX, axes=axes)

    def test_rasters(self):
        sw.plot_rasters(self._SX)

    def test_confusion(self):
        gt_comp = sc.compare_sorter_to_ground_truth(self._SX, self._SX)
        sw.plot_confusion_matrix(gt_comp, count_text=True)

    def test_agreement(self):
        comp = sc.compare_sorter_to_ground_truth(self._SX, self._SX)
        sw.plot_agreement_matrix(comp, count_text=True)
        
        gt_comp = sc.compare_sorter_to_ground_truth(self._SX, self._SX)
        sw.plot_agreement_matrix(gt_comp, ordered=True, count_text=True, )
        sw.plot_agreement_matrix(gt_comp, ordered=False, count_text=True, )

    def test_multicomp_graph(self):
        msc = sc.compare_multiple_sorters([self._SX, self._SX, self._SX])
        sw.plot_multicomp_graph(msc, edge_cmap='viridis', node_cmap='rainbow', draw_labels=False)
        sw.plot_multicomp_agreement(msc)
        sw.plot_multicomp_agreement_by_sorter(msc)
        fig, axes = plt.subplots(len(msc.sorting_list), 1)
        sw.plot_multicomp_agreement_by_sorter(msc, axes=axes)


if __name__ == '__main__':
    unittest.main()
