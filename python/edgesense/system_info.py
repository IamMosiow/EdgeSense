import sys
import torch


def print_system_info():
    print("=== EdgeSense System ===")
    print(f"Python: {sys.version.split()[0]}")
    print(f"PyTorch: {torch.__version__}")

    if torch.cuda.is_available():
        print("CUDA: Available")
        print(f"CUDA runtime: {torch.version.cuda}")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA: Not available")