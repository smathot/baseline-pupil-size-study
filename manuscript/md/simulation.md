We first investigate the effect of divisive and subtractive baseline correction in simulated data. The advantage of simulated data over real data is that it allows us to control noise and distortion, and therefore to see how robust baseline correction is to imperfections of the kind that also occur in real data. In addition, simulated data allows us to simulate two experimental conditions that differ in pupil size by a known amount, and therefore to see how baseline correction affects the power to detect this difference.


## Data generation

We started with a single real 3 s recording of a pupillary response to light, recorded at 1000 Hz with an EyeLink 1000 (SR Research). This recording did not contain blinks or recording artifacts, but did contain the slight noise that is typical of pupil-size recordings. Pupil size was measured in arbitrary units as recorded by the eye tracker, ranging from roughly 1600 to 4200.

Based on this single recording, 200 trials were generated. To each trial, a constant value, randomly chosen for each trial, between -1000 and 2000 was added to each sample. In %FigSimulation::b, this is visible as a random shift of each trace up or down the y-axis. In addition, one simulated eye blink was added to each trial. Eye blinks were modeled as a period of 10 ms during which pupil size linearly decreased to 0, followed by 50 to 150 ms (randomly varied) during which pupil size randomly fluctuated between 0 and 100, followed by a period of 10 ms during which pupil size linearly increased back to its normal value. This resembles real eye blinks as they are recorded by video-based eye trackers [e.g. @Mathôt2013Simple].

To simulate two conditions that differed in pupil size, we added a series of values that linearly increased from 0 to 200 to half the trials. These trials are the Red condition; the other trials are the Blue condition. As shown in %FigSimulation::a, pupil size is slightly larger in the Red condition than in the Blue condition, and this effect increases over time.

Crucially, in the Blue condition there were two trials in which a blink started at the first sample, and therefore affected the baseline period. In none of the other trials did the baseline period contain a blink.


%--
figure:
 id: FigSimulation
 source: FigSimulation.svg
 caption: |
  The effects of divisive and subtractive baseline correction in a simulated dataset. Data after: a, b) no baseline correction; c, d) divisive baseline correction; and e, f) subtractive baseline correction. Average pupil traces: a, c, e). Individual pupil traces: b, d, f).
--%


## Divisive baseline correction

First, median pupil size during the first 10 samples (corresponding to 10 ms) was taken as baseline pupil size. Next, all pupil sizes were divided by this baseline pupil size. This was done separately for each trial.

The results of divisive baseline correction are shown in %FigSimulation::c,d. In the two Blue trials in which there was a blink during the baseline period, baseline pupil size was very small; consequently, baseline-corrected pupil size was very large. These two trials are clearly visible in %FigSimulation::d as unrealistic baseline-corrected pupil sizes ranging from 40 to 130 (as a proportion of baseline), whereas in this dataset realistic baseline-corrected pupil sizes tend to range from 0.3 to 1. Pupil sizes on these two trials are so strongly distorted that they even affect the overall results: as shown in %FigSimulation::c, the overall results suggest that the pupil is largest in the Blue condition, whereas we had simulated an effect in the opposite direction.


## Subtractive baseline correction

Subtractive baseline correction was identical to divisive baseline correction, except that baseline pupil size was subtracted from all pupil sizes.

The results of subtractive baseline correction are shown in %FigSimulation::e,f. Again, the two Blue trials with a blink during the baseline period are clearly visible in %FigSimulation::f. However, their effect on the overall dataset is not as catastrophic as for divisive baseline correction.


## Statistical power

The results above show that the effects of blinks during the baseline period can be catastrophic, and much more so for divisive than subtractive baseline correction. However, it may be that divisive baseline correction nevertheless leads to the highest statistical power when there are no blinks during the baseline period. To test this, we generated data as described above, while varying the following:

- Effect size, from 0 (no difference between Red and Blue) to 500 (Red larger than Blue) in steps of 50
- Baseline correction: no correction, divisive, or subtractive
- Blinks during baseline in Blue condition: yes (2 blinks) or no

We generated 10,000 datasets for each combination, giving a total of (10,000 × 11 × 3 × 2 =) 660,000 datasets. For each dataset, we conducted an independent-samples t-test to test for a difference in mean pupil size between the Red and Blue conditions during the last 50 samples. We considered three possible outcomes (for convenience, we treat the 0 effect size as if it still constitutes a true positive effect):

- Detection of a true effect: *p* < .05 and pupil size smallest in the Blue condition
- Detection of a spurious effect: *p* < .05 and pupil smallest in the Red condition
- No detection of an effect: *p* >= .05

%--
figure:
 id: FigPower
 source: FigPower.svg
 caption: |
  Proportion of detected real (a,c) and spurious (b,d) effects when applying subtractive baseline correction (green), divisive baseline correction (pink), or no baseline correction at all (gray). Data with different effect sizes (x-axis: 0-500) and with (a,b) or without (c,d) blinks during the baseline was generated, 
--%

The proportion of datasets in which a true effect was detected is shown in %FigPower::a,c; the proportion on which a spurious effect was detected is shown in %FigPower::b,d. By chance (i.e. if there was no effect and no systematic distortion of the data) and given our two-sided *p* < .05 criterion, we would expect to find a .025 proportion of detections of true and spurious effects; this is indicated by the horizontal dotted lines.

First, consider the data with blinks in the baseline (%FigPower::a,b). With divisive baseline correction (pink), neither true nor spurious effects are detected (except for a handful of true effects for the highest effect sizes, but these are so few that they are hardly visible in the figure); this is because the blinks introduce so much variability in the signal that it is nearly impossible for any effect to be detected.

With subtractive baseline correction (green), true effects are often observed, and spurious effects are not. However, for weak effects, subtractive baseline correction is less sensitive than no baseline correction at all (gray). This is because, for weak effects, the blinks introduce so much variability that true effects cannot be detected; however, the variability is less than for divisive baseline correction, and for medium-to-large effects subtractive baseline correction is actually more sensitive than no baseline correction at all—despite blinks during the baseline.

Now consider the data without blinks in the baseline (%FigPower::b). An effect in the true direction is now detected in all cases, but there is a clear difference in sensitivity: subtractive baseline correction is most sensitive, followed by divisive baseline correction, in turn followed by no baseline correction at all. The three approaches do not differ markedly in the number of detected spurious effects.