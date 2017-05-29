Baseline correction is part of what researchers often refer to as *preprocessing*: cleaning the raw data (i.e. as recorded by the eye tracker) from as many undesirable features as possible. Of course, what constitutes an undesirable feature depends on the context. For example, eye blinks are often considered undesirable in pupillometry, because you cannot measure pupil size while the eyes are closed, and also because blinks are followed by a prolonged constriction of the pupil [@Knapen2016]. But in a different context, for example when using blink rate as a measure of fatigue [@Stern1994], eye blinks can also be the measure of interest. In other words, preprocessing is performed differently in different situations.

In pupillometry research, the following preprocessing steps are often performed. Baseline correction—the focus of this paper—is generally performed last.


### Dealing with missing data

Missing data most often occurs when a video-based eye tracker fails to extract the pupil from the camera image. Most eye trackers will then report a pupil size of 0, or indicate in some other way that data is missing. The first step in dealing with missing data is therefore to find out how the eye tracker reports missing data (e.g. as 0s), and then to ignore these values, for example by treating them as *nan* (not a number) values during the analysis; nan values are offered by most modern programming languages, and are a standard way to silently ignore missing data.

Whether missing data deserves special treatment is a matter of opinion. Some researchers prefer to interpolate missing data [e.g. @Knapen2016], similar to eye-blink reconstruction as discussed below. Other researchers prefer to exclude trials with too much missing data [e.g. @Koelewijn2012]. In our view, missing data needs no special treatment because what is not there does not affect the results anyway—as long as care is taken that missing data is not interpreted as real 0 pupil-size measurements.


### Dealing with eye blinks and other unrealistic pupil size values

A bigger problem occurs when pupil-size values are reported incorrectly but not marked as missing data. Pupil size changes at most by a factor of around 4, when expressed as pupil diameter, or around 16, when expressed as pupil surface [@McdougalGamlin2008]. If measured pupil size changes more than this, this means that something distorted the recording. By far the most common source of distortion is eye blinks; eye blinks are characterized by a rapid decrease in pupil size, followed by a period of missing data, followed by a rapid increase in pupil size. The period of missing data can be treated (or not) as discussed above; but the preceding and following distortions should be corrected, because they can strongly affect pupil size, even when averaged across many trials.

One way to deal with eye blinks, and our preferred method, is to use cubic-spline interpolation. This method is described in more detail elsewhere [@Math2013Simple] but in a nutshell works as follows: Four points (A, B, C, and D) are placed around the on- and offset of the blink. Point B is placed slightly before the onset of the blink; point C is placed slightly after the onset of the blink. Point A is then placed before point B; point D is placed after point C. Points are equally spaced, such that the distances between A and B, B and C, etc. are constant. Finally, a smooth line is drawn through all four points, replacing the missing and distorted data between B and C.


### Dealing with position artifacts

Imagine that a participant looks directly at the lens of a video-based eye tracker. The pupil is then recorded as near-perfect circle. Now imagine that the participant makes an eye movement to the right, thus causing the eye ball to rotate, changing the angle from which the eye tracker records the pupil, and causing the horizontal diameter of the pupil (as recorded) to decrease. In other words, pupil size as recorded by the eye tracker decreases, even though pupil size really did not change. Most eye trackers cannot distinguish such artifactual pupil-size changes due to eye movements from real pupil-size changes.

Several researchers [e.g. @Brisson2013] have suggested that such position artifacts can be corrected by doing a calibration procedure during which participants look at points on different parts of the screen. A multiple linear regression is then performed to predict pupil size from horizontal (X) and vertical (Y) pupil size. Using this regression, position artifacts could then be removed from pupil size during the rest of the experiment. This procedure assumes that, in reality, pupil size does not depend on eye position, and any measured relationship is therefore artifactual.

Unfortunately, this procedure does not work for the simple reason that pupil size may actually (and usually does) change as a function of eye position. For example, if participants need to look up uncomfortably to foveate the top of the screen, the mental and physical effort involved may cause their pupils to dilate. When performing a correction as described above, this real pupil-size change would be corrected as though it were artifactual. Even worse, artifactual pupil-size changes happen immediately when the eyes move, whereas real pupil-size changes occur slowly. Therefore, they have to be treated differently; if not, pupil size may seem completely free of position artifacts just before each eye movement, but catastrophically affected by position artifacts immediately after each eye movement. We have seen this in our data, and decided to leave position artifacts uncorrected for exactly this reason [@MathôtMelmiCastet2015].

To summarize, pupil size changes as a function of eye position, and this is in part an artifact due to the angle from which the eye tracker records the pupil. However, and contrary to popular belief, there are currently no satisfactory techniques to correct this.


### Hope for the best, prepare for the worst

Data preprocessing is useful, improves statistical power (the probability of detecting true effects), and makes it substantially easier to analyze and interpret results. However, eye-movement data is messy, and every form of preprocessing is guaranteed to fail occasionally. For example, blink reconstruction often fails when the eyes close only partly (is that even a blink?) or when due to noise the blink is not detected.

Therefore, results should not crucially depend on whether the data still contains artifacts. Similarly, one preprocessing step should not crucially depend on whether the previous preprocessing step was perfect. For this reason, in this paper we focus on baseline correction in isolation, as if no preprocessing steps are performed beforehand. This is, in a sense, a worst-case scenario, but one that we should be prepared for.
