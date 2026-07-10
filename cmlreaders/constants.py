# flake8: noqa

# supported protocols
PROTOCOLS = (
    "r1",
    "ltp",
    "pyfr",
)

PYFR_SUBJECT_CODE_PREFIXES = ("BW", "CH", "CP", "FR", "FZ", "TJ", "UP")

rhino_paths = {
    # data indices
    "r1_index": ["/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/r1.json"],
    "ltp_index": ["/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/ltp.json"],
    "pyfr_index": ["groups/nxh177-lab-herzlab/raw_data/kahana/pyFR/pyFR.json"],
    # root directory to look for pyFR data
    "pyfr_root": ["groups/nxh177-lab-herzlab/raw_data/kahana/pyFR"],
    # Localization-level (subject + localization_
    "localization": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/localizations/{localization}/neuroradiology/current_processed/localization.json",
    ],
    # Montage-level (subject + montage)
    "voxel_coordinates": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/VOX_coords_mother.txt",
    ],
    "prior_stim_results": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/data/eeg/freesurfer/subjects/{subject_montage}/prior_stim/{subject}_allcords.csv",
    ],
    "electrode_coordinates": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/coords/electrode_coordinates.csv",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/electrode_coordinates.csv",
    ],
    "mni_coordinates": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/imaging/autoloc/electrodenames_coordinates_mni.csv"
    ],
    "jacksheet": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/docs/jacksheet.txt",
    ],
    "area": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/docs/area.txt",
    ],
    "electrode_categories": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/electrode_categories/{subject_montage}_electrode_categories.txt"  # ,
        # 	'data10/RAM/subjects/{subject_montage}/docs/electrode_categories.txt', # 2020-01-07 JS-We decided to only use a single, master folder
        #         'scratch/pwanda/electrode_categories/{subject_montage}_electrode_categories.txt',
        #         'scratch/pwanda/electrode_categories/electrode_categories_{subject_montage}.txt',
    ],
    "good_leads": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/good_leads.txt",
    ],
    "leads": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/leads.txt",
    ],
    "classifier_excluded_leads": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/classifier_excluded_leads.txt",
    ],
    "matlab_bipolar_talstruct": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_bipol.mat"
    ],
    "matlab_monopolar_talstruct": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_monopol.mat"
    ],
    "pairs": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/localizations/{localization}/montages/{montage}/neuroradiology/current_processed/pairs.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_bipol.mat",
    ],
    "matlab_pairs": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_bipol.mat",
    ],
    "contacts": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/localizations/{localization}/montages/{montage}/neuroradiology/current_processed/contacts.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_monopol.mat",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database.mat",
    ],
    "matlab_contacts": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database_monopol.mat",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject_montage}/tal/{subject_montage}_talLocs_database.mat",
    ],
    # Report Data
    "session_summary": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_{experiment}_{session}_session_summary.h5",
    ],
    "classifier_summary": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_{experiment}_{session}_classifier_session_{session}.h5",
    ],
    "math_summary": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_{experiment}_{session}_math_summary.h5",
    ],
    "target_selection_table": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_{experiment}_*_target_selection_table.csv",
    ],
    "baseline_classifier": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_retrained_classifier.zip",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/report_database/{subject_montage}_{experiment}_all_retrained_classifier.zip",
    ],
    # Session Data
    "all_events": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/behavioral/current_processed/all_events.json",
        "groups/nxh177-lab-herzlab/raw_data/kahana/pyFR/{subject_montage}_events.mat",
    ],
    "task_events": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/behavioral/current_processed/task_events.json",
        "groups/nxh177-lab-herzlab/raw_data/kahana/pyFR/{subject_montage}_events.mat",
    ],
    "math_events": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/behavioral/current_processed/math_events.json",
        "groups/nxh177-lab-herzlab/raw_data/kahana/pyFR/{subject_montage}_math.mat",
    ],
    "ps4_events": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/behavioral/current_processed/ps4_events.json"
    ],
    "sources": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/ephys/current_processed/sources.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/data/eeg/{subject}/eeg.noreref/{eeg_basename}.params.txt",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/data/eeg/{subject}/eeg.noreref/params.txt",
    ],
    # Processed EEG data basename
    # For data in /protocols, this gets expanded into either a bunch of files or
    # a single HDF5 file in the case of later RAM subjects recorded on the ENS.
    "processed_eeg": [
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/{protocol}/subjects/{subject}/experiments/{experiment}/sessions/{session}/ephys/current_processed/noreref/{basename}"
    ],
    # Ramulator-related information
    "experiment_log": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/experiment.log",
    ],
    "session_log": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/session.log",
    ],
    "session_json": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/session.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/session.jsonl",
    ],
    "ramulator_session_folder": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/*",
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/r1/subjects/{subject}/experiments/{experiment}/sessions/{session}/ephys/current_source/host_pc/*",
    ],
    # Elemem-related information
    "elemem_session_folder": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/elemem/*",
        "/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/r1/subjects/{subject}/experiments/{experiment}/sessions/{session}/ephys/current_source/elemem/*",
    ],
    # There can be multiple timestamped folders for the host pc files for when
    # a session is restarted
    "event_log": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/event_log.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/elemem/{timestamped_dir}/event.log",
    ],
    "experiment_config": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/experiment_config.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/elemem/{timestamped_dir}/experiment_config.json",
    ],
    "raw_eeg": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/eeg_timeseries.h5",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/elemem/{timestamped_dir}/eeg_data.edf",
    ],
    "archived_eeg": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/elemem/{timestamped_dir}/eeg_archive/eeg_data.edf",
    ],
    "odin_config": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/{subject}_*.csv",
    ],
    # There can be multiple classifiers if artifcat detection was enabled and
    # the classifier needed to be retrained. The order is important here In
    # general, the files should be listed in order of preference so that the
    # first file found is returned
    "used_classifier": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/retrained_classifier/{subject}-classifier.zip",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/{subject}-classifier.zip",
    ],
    "excluded_pairs": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/retrained_classifier/excluded_pairs.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/excluded_pairs.json",
    ],
    "all_pairs": [
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/pairs.json",
        "/groups/nxh177-lab-herzlab/raw_data/kahana/subjects/{subject}/behavioral/{experiment}/session_{session}/host_pc/{timestamped_dir}/config_files/retrained_classifier/pairs.json",
    ],
    # scalp experiments subject info
    "subject_info": "/data/eeg/scalp/ltp/{experiment}/cmldb_subj_info_{experiment}.txt",
}

# Maintain separate lists of the file types depending on what information is
# required to be able to find them
localization_files = ("localization",)

# All files that change when a montage changes
montage_files = (
    "pairs",
    "contacts",
    "voxel_coordinates",
    "prior_stim_results",
    "electrode_coordinates",
    "mni_coordinates",
    "jacksheet",
    "good_leads",
    "leads",
    "area",
    "classifier_excluded_leads",
    "electrode_categories",
    "target_selection_file",
    "baseline_classifier",
)

# All files that are constant by subject
subject_files = []

# All files that vary at the session level
session_files = (
    "session_summary",
    "classifier_summary",
    "math_summary",
    "used_classifier",
    "excluded_pairs",
    "all_pairs",
    "experiment_log",
    "session_log",
    "session_json",
    "event_log",
    "experiment_config",
    "raw_eeg",
    "odin_config",
    "all_events",
    "task_events",
    "math_events",
    "ps4_events",
)

# All files that require some extra work to identify
host_pc_files = (
    "event_log",
    "experiment_config",
    "raw_eeg",
    "odin_config",
    "used_classifier",
    "excluded_pairs",
    "all_pairs",
)

# Files related to in-session classifier retraining
used_classifier_files = ("used_classifier", "excluded_pairs", "all_pairs")

# All Ramulator files/directories
ramulator_files = host_pc_files + used_classifier_files + ("ramulator_session_folder",)

# All Elemem files/directories
elemem_files = (
    "event_log",
    "experiment_config",
    "raw_eeg",
    "elemem_session_folder",
    "archived_eeg"
)

# Offset corrections for retrieval events
offset_corrections = ["/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/r1/offset_corrections.csv"]

# Countdown event list corrections
countdown_errors = ["/groups/nxh177-lab-herzlab/processed_data/kahana/protocols/r1/countdown_errors.csv"]
