# Cat & Mouse: A Study on Gaze-Based Mouse Sensitivity

This program was designed for research on the potential benefit of gaze-based mouse sensitivity</br>

The focus of this application is research and usability. Aesthetics were not considered beyond functionality.

## How to use

### Requirements

Must have both Python and pygame installed.

### Steps
<ol>
  <li>Spin up the app in the terminal.</li>
  <li>Enter user info (Ex: "3b") then press enter.</li>
  <li>Click the screen to move the target around.</li>
  <li>Use "tab" to see the scoreboard. This will automatically display after starting the test and clicking 20 targets.</li>
  <li>Use the spacebar to start the test. The target will move when hitting the spacebar, and when a user clicks it.</li>
  <li>Record results that pop up after the test is over. These will not be saved.</li>
  <li>Restart application to run again.</li>
</ol>

## Acknowledgements

WebGazer.js from Brown University was considered, but not used in the final application</br>
Google Gemini was used to create the draw_table function in table.py</br>
ChatGPT was used to create the equations for calculating the sensitivity divisor when the cursor is near but not very near to the target. Results for the exponential equation were validated in Google Sheets. The divisor was set to never fall below 1.