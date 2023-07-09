# Project: Firefly Light Accumulation

## Description

This simple Python project aims to quickly complete the task of accumulation by capturing the faint light emitted by fireflies. The project focuses on accumulating small pieces of data or results to achieve a larger goal.

The application simulates the behavior of fireflies and collects the light emitted by each individual firefly. It then accumulates this light over time to create a comprehensive dataset that represents the collective luminosity of the fireflies.

## Features

- **Firefly Chapture**: Finding the video keyframes of the behavior of fireflies and their light emission
- **Light Accumulation**: Collects and accumulates the light emitted by each firefly
- **Data Visualization**: Provides visualizations to showcase the accumulated light over time

## Installation

1. Clone the repository:

```bash
git clone https://github.com/5418XR/StackVideoFirefly.git
```

2. Navigate into the cloned repository:

```bash
cd StackVideoFirefly
```

3. Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the application, run the main script with Python:

```bash
python readData.py
```
This will help you to extract the keyframes from the video into the folder "output_frames" (which will be created if there is no such folder). And store all the keyframes in a new folder in the format "keyframe_photoNumber.png".

```bash
python newPhoto.py
```
This will extract the photos you have stored in the folder "output_frames". You can adjust the range of keyframes and how many frames are extracted at a time to your liking.
### Note: 

Ensure that you have Python 3 installed on your machine before running the application.

## Contribution

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/5418XR/StackVideoFirefly/issues) if you want to contribute.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, please feel free to contact me. You can also raise an issue for any suggestions or improvements.

**Happy Coding!**
