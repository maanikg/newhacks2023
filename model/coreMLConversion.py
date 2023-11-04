import onnxmltools
import coremltools

# Load a Core ML model
coreml_model = coremltools.utils.load_spec("model/handposeModel.mlmodel")
# print(coreml_model) 

# Convert the Core ML model into ONNX
onnx_model = onnxmltools.convert_coreml(coreml_model)

# # Save as protobuf
# onnxmltools.utils.save_model(onnx_model, "example.onnx")
