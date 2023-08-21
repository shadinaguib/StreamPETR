# Visualization Tools

## 1. Multi-camera Tracking Video
* `INFO_FILE_PATH`: path to the infos file.
* `TRACKING_RESULT`: path to your tracking result file in `.json` format.
* `SHOW_DIR`: directory to save the images and videos.

The command is:
```bash
python tools/tracking/visualize_tracking.py --data_infos_path INFO_FILE_PATH --result TRACKING_RESULT --show-dir SHOW_DIR
```

For example, if you want to visualize the results on the validation set of mini-split for `results.json`, please run the following commands:
```bash
python tools/tracking/visualize_tracking.py --data_infos_path ./data/nuscenes/nuscenes2d_temporal_infos_val.pkl --result tracking.json --show-dir ./work_dirs/visualizations/