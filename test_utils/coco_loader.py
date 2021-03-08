import wget
import os
import shutil
import zipfile


def download_coco_dataset(dataset_type):
    if dataset_type not in ("train", "val", "test"):
        raise ValueError("Dataset type invalid, should be one of \"train\", \"val\" or \"test\"")
    dataset_path = "/" + os.path.join(os.path.join(os.path.join(*os.getcwd().split("/")[:-1])), "datasets")
    coco_path = os.path.join(dataset_path, "coco")
    if os.path.isdir(coco_path):
        shutil.rmtree(coco_path)
    os.makedirs(coco_path)
    coco_data_path = "http://images.cocodataset.org/zips/{}2017.zip".format(dataset_type)
    wget.download(coco_data_path, os.path.join(coco_path, "{}2017.zip".format(dataset_type)))
    if dataset_type in ("train", "val"):
        annotation_path = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
        wget.download(annotation_path, os.path.join(coco_path, "annotations_trainval2017.zip"))
    elif dataset_type == "test":
        annotation_path = "http://images.cocodataset.org/annotations/image_info_test2017.zip"
        wget.download(annotation_path, os.path.join(coco_path, "image_info_test2017.zip"))
    print("\nINFO: Done downloading COCO-{}-2017 dataset".format(dataset_type))


def unzip_loaded_data(dataset_type):
    if dataset_type not in ("train", "val", "test"):
        raise ValueError("Dataset type invalid, should be one of \"train\", \"val\" or \"test\"")
    coco_path = "/" + os.path.join(os.path.join(*os.getcwd().split("/")[:-1]), "datasets/coco")
    if not os.path.isdir(coco_path):
        raise RuntimeError("COCO data not yet downloaded, you can download by using download_coco_dataset() method!")
    coco_data_path = os.path.join(coco_path, "{}2017.zip".format(dataset_type))
    if dataset_type in ("train", "val"):
        annotation_path = os.path.join(coco_path, "annotations_trainval2017.zip")
    # Will implement for test set later
    with zipfile.ZipFile(coco_data_path, "r") as data_zip:
        data_zip.extractall(coco_path)
    with zipfile.ZipFile(annotation_path, "r") as annotation_zip:
        annotation_zip.extractall(coco_path)


def clear_zip_files(dataset_type):
    if dataset_type not in ("train", "val", "test"):
        raise ValueError("Dataset type invalid, should be one of \"train\", \"val\" or \"test\"")
    coco_path = "/" + os.path.join(os.path.join(*os.getcwd().split("/")[:-1]), "datasets/coco")
    if not os.path.isdir(coco_path):
        raise RuntimeError("COCO data not yet downloaded, you can download by using download_coco_dataset() method!")
    coco_data_path = os.path.join(coco_path, "{}2017.zip").format(dataset_type)
    if dataset_type in ("train", "val"):
        annotations_path = os.path.join(coco_path, "annotations_trainval2017.zip")
    else:
        annotations_path = os.path.join(coco_path, "image_info_test2017.zip")
    os.remove(coco_data_path)
    os.remove(annotations_path)
