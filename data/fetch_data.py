import os
import requests

def get_karpathy_tiny_shakespeare(save_dir="."):
    """
    Downloads Karpathy's Tiny Shakespeare dataset from GitHub if not already present.

    Args:
        save_dir (str): Directory to save 'input.txt'. Defaults to current directory.

    Returns:
        str: The full dataset text.
    """
    # Build file path
    input_file_path = os.path.join(save_dir, "input.txt")
    
    # Download if not exists
    if not os.path.exists(input_file_path):
        data_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        print(f"Downloading Tiny Shakespeare from {data_url} ...")
        response = requests.get(data_url)
        response.raise_for_status()  # raises an error if download fails
        os.makedirs(save_dir, exist_ok=True)
        with open(input_file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Download complete.")
    
    # Read dataset
    with open(input_file_path, "r", encoding="utf-8") as f:
        data = f.read()
    
    print(f"Length of dataset in characters: {len(data):,}")
    return data


if __name__ == "__main__":
    dataset_text = get_karpathy_tiny_shakespeare(save_dir="./data")
