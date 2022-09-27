

import os

CAM_FMS = int(os.environ.get('MAX_FPS', 8))
IOU_THRESHOLD = float(os.environ.get('IOU_THRESHOLD', 0.3))
VIDEO_INPUT = os.environ.get('VIDEO_INPUT', 0)
FACE_ASPECT_RATIO = float(os.environ.get('FACE_ASPECT_RATIO', 0.08))