import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Print the number of available GPUs
    num_gpus = torch.cuda.device_count()
    print(f"Number of CUDA devices: {num_gpus}")
    
    # Loop through each GPU and print its name and ID
    for i in range(num_gpus):
        device_name = torch.cuda.get_device_name(i)
        print(f"Device {i}: {device_name}")
else:
    print("CUDA is not available on this machine.")
