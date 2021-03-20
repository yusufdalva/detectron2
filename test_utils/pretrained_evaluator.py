

# TODO: Method for constructing the model from the yaml file

# TODO: Method for evaluation

class InstSegEvaluator:

    MODEL_PATH_MAPPING = {
        "ResNet_50_C4_x1": "COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.yaml",
        "ResNet_50_DC5_x1": "COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_1x.yaml",
        "ResNet_50_FPN_x1": "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml",
        "ResNet_50_C4_x3": "COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml",
        "ResNet_50_DC5_x3": "COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x.yaml",
        "ResNet_50_FPN_x3": "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml",
        "ResNet_101_C4_x3": "COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml",
        "ResNet_101_DC5_x3": "COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x.yaml",
        "ResNet_101_FPN_x3": "COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml",
        "ResNext_101_FPN_x3": "COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml"
    }

    def __init__(self, backbone):
        pass

    def evaluate(self):
        pass
