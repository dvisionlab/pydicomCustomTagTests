from pydicom.data import get_testdata_file
from pydicom import dcmread
from pydicom.dataset import FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the DICOM file relative to the script's directory
fpath = os.path.join(script_dir, "../testlungo2.dcm")
print(fpath)
ds = dcmread(fpath)
print(ds)
# Modify the patient's name (tag: (0010, 0010))
ds[0x10,0x10].value = "knixp"
ds.StudyDescription = "knixpgblgjbsxglob"



# Save the modified dataset to a new DICOM file
new_file_path = "../modified_testlungo3.dcm"
ds.save_as(new_file_path)

print("Modified DICOM file saved to:", new_file_path)
# python3 ./examples/CustomTag.py