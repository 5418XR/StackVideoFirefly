# Project: Firefly Light Accumulation
![d9c037f6f35838b1d14a042d2433b76](https://github.com/5418XR/StackVideoFirefly/assets/72371666/637b4822-0d87-44de-9380-a5227dfc7d24)

## Description

This simple Python project is designed to quickly complete the stacking task by capturing the faint light emitted by fireflies. The project focuses on the image stacking function itself, avoiding the high price you pay for a computer that supports intense video processing and unnecessary professional photo post-processing tools. (Money, time and unnecessary software features. When I built this project, I spent 5$ on "professional camera software" at the Apple Store. However, to this day, I still don't understand how it works.) .
The application collects key frames from the video of the light emitted by each individual firefly. Then by stacking the images, it eventually blends them into a single photo that represents the collective glow of the fireflies. Theoretically, you can also take it to any fixed-camera video footage.

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

This project is licensed under the terms of the MIT license. See the [LICENSE](https://github.com/5418XR/StackVideoFirefly/blob/main/LICENSE.txt) file for details.

## Contact

If you have any questions, please feel free to contact me. You can also raise an issue for any suggestions or improvements.

**Happy Coding!**
