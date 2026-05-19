# Dataset YAML Configuration

This file explains the `data.yaml` used for YOLO training.

## Contents of data.yaml

```yaml
path: D:/Puru_VNR/Projects/IIITH/Internship/Week4_Task2
train: images/train
val: images/val
test: images/test

nc: 2
names:
  0: car
  1: truck
```

## Field Descriptions

| Field | Meaning |
|---|---|
| `path` | Root directory of the dataset |
| `train` | Relative path to training images |
| `val` | Relative path to validation images |
| `test` | Relative path to test images |
| `nc` | Number of classes |
| `names` | Class index to class name mapping |

## Notes
- Forward slashes must be used even on Windows
- Class indices in label `.txt` files must match the `names` mapping above
- `0` = car, `1` = truck