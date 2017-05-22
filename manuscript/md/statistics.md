Statistically speaking, what does baseline correction do?

Baseline correction is a way to reduce the impact of random pupil-size fluctuations from one trial to the next; it is *not* a way to control for overall differences in pupil size between participants. Of course, some participants have larger pupils than others [see @Tsukahara2016 for a fascinating study on the relationship between pupil size and intelligence]; and the distance between camera and eye, which varies slightly from participant to participant, also affects pupil size, at least as measured by most eye trackers. But such between-subject differences are better taken into account statistically, through a repeated measures ANOVA or a linear mixed-effects model with by-participant random intercepts [e.g. @Baayen2008JMemLang]—just like between-subject differences in reaction times are usually taken into account.

Phrased differently, baseline correction is a way to turn a between-trial design, in which pupil sizes are compared between trials, into a within-trial design, in which pupil sizes are compared between one moment in a trial (i.e. the baseline period) and another moment in the same trial (i.e. a sample during the epoch of interest). To illustrate this, let's consider two ways to analyze pupil size data, as shown in %FigStatistics. These two ways seem very different at first sight, but are equivalent on closer inspection.

Here, we have hypothetical data of four trials with two conditions (Blue and Red). Let's assume that we want to analyze the effect of condition at time 1. (The exact same principles would apply if we wanted to analyze the effect of condition at time 2)


%--
figure:
 id: FigStatistics
 source: FigStatistics.svg
 caption: |
  Two different ways to take baseline pupil size into account. a) Baseline pupil size can be taken into account statistically, by conducting a linear mixed-effects model. b) After performing subtractive baseline correction, the same analysis is reduced to independent-samples t-test. 
--%


%FigStatistics::a shows an analysis that takes baseline pupil size into account without doing explicit baseline correction. To do so, the analysis includes two time points: one time point (0) that corresponds to the baseline, and one time point (1) that corresponds to the sample that we want to analyze. We are then interested in the interaction between time and condition: This reflects the effect of condition, while taking changes in baseline pupil size into account. Because each trial now contributes two observations to the analysis, the observations in the analysis are no longer independent. To take this into account, we need to conduct a linear mixed-effects model where trial is a random effect, and we allow the intercept to randomly vary by trial (i.e. random by-trial intercepts). The outcome of this analysis is t = 2.668, p = 0.116 for the time by condition interaction.

%FigStatistics::b shows the same analysis, but done after subtractive baseline correction, so that pupil size is set to 0 at time 0 for all trials. The analysis now reduced to a simple independent samples t-test between the Blue and Red trials. The outcome is t = 2.668, p = 0.116—identical to the linear-mixed effects analysis described above.

In other words, by conducting a linear mixed-effects analysis, you can accomplish the exact same thing as by doing subtractive baseline correction. However, in most cases baseline correction is simpler to do.
