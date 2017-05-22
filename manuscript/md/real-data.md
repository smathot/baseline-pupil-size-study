The simulated data highlights problems that can occur when applying baseline correction, especially divisive baseline correction, if there are blinks in the baseline period. But you may wonder whether these problems actually occur in real data. To test this, we looked at the effects of baseline correction in one representative set of real data.


## Data

The data was collected for a different study, and consisted of 2520 trials (across 15 participants) in two conditions, here labeled Blue and Red. All participants signed informed consent before participating and received monetary compensation. The experiment was approved by the ethics committee of Utrecht University. ++For details, see Exp. 1 from @MathVan+heusden2015.++


%--
figure:
 id: FigRealData
 source: FigRealData.svg
 caption: |
  The effects of divisive and subtractive baseline correction in a real dataset. a, b) No baseline correction. Y-axis reflects pupil size in arbitrary units. c, d) Divisive baseline correction. Y-axis reflects proportional pupil-size change relative to baseline period. e, f) Subtractive baseline correction. Y-axis reflects difference in pupil-size from baseline period in arbitrary units. Individual pupil traces: a, c, e). Average pupil traces: b, d, f).
--%


First, consider the uncorrected data (%FigRealData::a,b). The trial starts with a pronounced pupillary constriction, followed by a gradual redilation. Overall (%FigRealData::b), the pupil is slightly larger in the Blue than the Red condition, but this difference is small. (Whether or not the difference between the two conditions is reliable is not relevant in this context.) The individual traces (%FigRealData::a) show a lot of variability between trials, as well as frequent blinks, which correspond to the vertical spines protruding downward.


## Divisive baseline correction

%FigRealData::c,d shows the data after applying divisive baseline correction (applied in the same way as for the simulated data). Overall, the data now suggests that the pupil is markedly larger in the Blue than the Red condition. But to the expert eye, the pattern is odd, because the difference between Blue and Red is mostly due to a sharp (apparent) pupillary dilation in the Blue condition immediately following the baseline period; afterwards, the difference remains more-or-less constant. This is odd if you know that, because of the latency of the pupillary response, real effects on pupil size develop at the earliest about 220 ms after the manipulation that caused them [e.g. @MathôtVan+der+linden2015EyePrep]; in other words, there should not be any difference between Blue and Red before 220 ms.

If we look at the individual trials, it is clear where the problem comes from: Because of blinks during the baseline period, baseline-corrected pupil size is unrealistically large in a handful of trials (dotted lines). Most of these trials are in the Blue condition, and this causes overall pupil size to be overestimated in the Blue condition. (It is not clear why there are more blinks in the Blue than the Red condition. This may well be due to chance. But even if the two ++conditions++ systematically differ in blink rate—which would be interesting—this difference should not confound the pupil-size data!)


## Subtractive baseline correction

%FigRealData::e,f shows the data after applying subtractive baseline correction (applied in the same way as for the simulated data). Overall, the difference in pupil size between Blue and Red is exaggerated compared to the raw data (compare %FigRealData::f to %FigRealData::b). If we look at the individual trials, this is again due to the same handful of trials (dotted lines), mostly in the Blue condition, in which pupil size is overestimated because of blinks in the baseline period. In other words, subtractive baseline correction suffers from the same problem as divisive baseline correction, but to a much lesser extent. 


## Identifying problematic trials

%FigHist shows a histogram of baseline pupil sizes, that is, of median pupil sizes during the first 10 ms of the trial. In this dataset, baseline pupil sizes are more-or-less normally distributed with only a slightly elongated right tail. (But baseline pupil sizes may be distributed differently in other datasets.)

On a few trials, baseline pupil size is unusually small; but these trials are so rare that they are hardly visible in the original histogram (%FigHist::a). Therefore, we have also plotted a log-transformed histogram, which accentuates bins with few observations (%FigHist::b). Looking at this distribution, a reasonable cut-off seems to be 400 (arbitrary units): Baseline pupil sizes below this value are—in this dataset—unrealistic and can catastrophically affect the results as we have described above.


%--
figure:
 id: FigHist
 source: FigHist.svg
 caption: |
  A histogram of baseline pupil sizes. a) Original historgram. b) Log-transformed histogram. The vertical dotted line indicates a threshold below which baseline pupil sizes appear unrealistically small.
--%


In %FigRealData::d we have marked those trials in which baseline pupil size was less than 400 as dotted lines. As expected, those trials in which baseline-corrected pupil size is unrealistically large are exactly those trials on which baseline pupil size is unrealistically small.


%--
figure:
 id: FigFiltered
 source: FigFiltered.svg
 caption: |
  Overall results for divisive (a) and substractive (b) baseline correction after removing trials in which baseline pupil size was less than 400.
--%


If we remove trials on which baseline pupil size was less than 400, the distortion of the overall results is much reduced. In particular, if we look at the results of the divisive baseline correction, the sharp pupillary dilation immediately following the baseline period in the Blue condition is entirely gone (compare %FigFiltered::a with %FigRealData::d).

Most trials with small baselines would also have been removed if we had removed trials in which a blink was detected during the baseline. But you can think of cases in which baseline pupil size is really small while no blink is detected; for example, the eyelid can close only partly, or noisy recordings may prevent measured pupil size from going to 0 during a blink, preventing detection. Therefore, we feel that it is safer to filter based on pupil size instead of (or in addition to) filtering based on detected blinks.
