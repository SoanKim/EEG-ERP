import mne
epochs = mne.io.read_epochs_eeglab('001_sync.set')
epochs.events             # show the events array
epochs.plot()             # show the epochs
epochs.plot_image()       # show each epoch as a row of an image, with amplitude coded as pixel color
epochs.plot_psd(fmax=40)  # show the frequency spectrum of the epochs
