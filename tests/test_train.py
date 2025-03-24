import subprocess

def test_train_script():
    result = subprocess.run(["python", "src/train.py"], capture_output=True, text=True)
    assert result.returncode == 0  # Checks if it ran without errors
    assert "Training complete!" in result.stdout  # Checks the output

if __name__ == "__main__":
    test_train_script()